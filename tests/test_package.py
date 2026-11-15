import importlib.util
import json
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('npm') and shutil.which('node'), 'npm and Node.js required')
class PackageTests(unittest.TestCase):
    def test_package_installs_skills_without_website(self):
        with tempfile.TemporaryDirectory() as tmp:
            packed = subprocess.run(
                ['npm', 'pack', '--ignore-scripts', '--json', '--pack-destination', tmp],
                cwd=ROOT, capture_output=True, text=True, check=True,
            )
            archive = Path(tmp) / json.loads(packed.stdout)[0]['filename']
            with tarfile.open(archive) as tar:
                names = tar.getnames()
                self.assertFalse(any(name.startswith(('package/website/', 'package/app/', 'package/components/')) for name in names))
                for member in tar:
                    if member.isfile():
                        self.assertNotIn('..', Path(member.name).parts)
                        destination = Path(tmp) / member.name
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        destination.write_bytes(tar.extractfile(member).read())
            package = Path(tmp) / 'package'
            manifest = json.loads((package / 'package.json').read_text())
            self.assertFalse(manifest.get('dependencies'))
            target = Path(tmp) / 'target'
            result = subprocess.run(
                ['node', str(package / 'bin/pdi.js'), str(target), '--hosts', 'agents', '--standalone-skills'],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            skills = list((target / '.agents/skills').glob('*/SKILL.md'))
            self.assertEqual(len(skills), 9)
            spec = importlib.util.spec_from_file_location('package_validator', package / 'scripts/validate_skills.py')
            validator = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(validator)
            for skill in skills:
                self.assertEqual(validator.validate(skill), [], str(skill))
            self.assertFalse((target / 'website').exists())

            all_target = Path(tmp) / 'target-all'
            all_result = subprocess.run(
                ['node', str(package / 'bin/pdi.js'), str(all_target), '--hosts', 'all', '--standalone-skills'],
                capture_output=True, text=True,
            )
            self.assertEqual(all_result.returncode, 0, all_result.stderr)
            for expected in (
                'AGENTS.md',
                'CLAUDE.md',
                '.claude/skills/ux-audit/SKILL.md',
                '.cursor/rules/pdi-coordinator.mdc',
                '.windsurfrules',
                '.github/copilot-instructions.md',
            ):
                self.assertTrue((all_target / expected).is_file(), f'Missing host file: {expected}')
