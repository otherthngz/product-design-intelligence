import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    'product-framing',
    'ux-research',
    'ux-audit',
    'interaction-design',
    'ux-writing',
    'design-system',
    'ui-prototyping',
    'design-handoff',
)

class FoundationTests(unittest.TestCase):
    def test_skill_metadata_and_contracts(self):
        for name in SKILLS:
            with self.subTest(name=name):
                content = (ROOT / '.agents/skills' / name / 'SKILL.md').read_text()
                self.assertTrue(content.startswith('---\nname: ' + name + '\ndescription: '))
                self.assertIn('\n---\n', content[4:])
                for term in ('Inputs', 'Workflow', 'Artifacts', 'Quality', 'Failure', 'Tools', 'Example'):
                    self.assertIn(term, content)

    def test_validator_detects_bad_metadata_and_broken_links(self):
        spec = importlib.util.spec_from_file_location('validate_skills', ROOT / 'scripts/validate_skills.py')
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'sample'
            folder.mkdir()
            skill = folder / 'SKILL.md'
            skill.write_text('---\nname: wrong\ndescription: Use for tests.\n---\n[missing](missing.md)\n')
            errors = validator.validate(skill)
            self.assertTrue(any('mismatch' in error for error in errors))
            self.assertTrue(any('broken local link' in error for error in errors))
            skill.write_text('---\nname: sample\ndescription: Use for tests.\n---\nInstructions.\n')
            self.assertEqual(validator.validate(skill), [])

    def test_skill_validator_supports_bundled_license(self):
        spec = importlib.util.spec_from_file_location('validate_skills', ROOT / 'scripts/validate_skills.py')
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'sample'
            folder.mkdir()
            skill = folder / 'SKILL.md'
            skill.write_text('---\nname: sample\ndescription: Use for tests.\nlicense: LICENSE.txt\n---\nInstructions.\n')
            self.assertTrue(any('license' in error for error in validator.validate(skill)))
            (folder / 'LICENSE.txt').write_text('license text')
            self.assertEqual(validator.validate(skill), [])

    def test_frontend_design_is_discoverable_and_licensed(self):
        skill = ROOT / '.agents/skills/frontend-design/SKILL.md'
        spec = importlib.util.spec_from_file_location('validate_skills', ROOT / 'scripts/validate_skills.py')
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        self.assertEqual(validator.validate(skill), [])
        self.assertIn('frontend-design', (ROOT / 'workflows/route-task.md').read_text())
        self.assertTrue((skill.parent / 'LICENSE.txt').is_file())

    def test_cases_cover_skills_and_fallback(self):
        cases = (ROOT / 'tests/evaluation-cases.md').read_text()
        for name in SKILLS:
            self.assertIn(name, cases)
        self.assertIn('fallback', cases.lower())

    def test_generator_creates_artifact_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'prototype.html'
            cmd = [sys.executable, str(ROOT / 'scripts/create_onboarding.py'), str(target)]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(target.read_bytes(), (ROOT / 'examples/onboarding/index.html').read_bytes())
            target.write_text('keep me')
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(target.read_text(), 'keep me')

    def test_example_has_basic_accessibility_and_states(self):
        html = (ROOT / 'examples/onboarding/index.html').read_text()
        for term in ('lang="en"', 'viewport', '<label', 'required', 'aria-live', 'type="submit"', '@media', 'Back', 'success'):
            self.assertIn(term, html)

    def test_manifest_and_llms_bundles_are_valid(self):
        cmd = [sys.executable, str(ROOT / 'scripts/build_manifest.py')]
        res = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stderr)
        manifest = json.loads((ROOT / 'pdi-manifest.json').read_text())
        skill_names = {s['name'] for s in manifest['skills']}
        for name in SKILLS + ('frontend-design',):
            self.assertIn(name, skill_names)
        self.assertEqual(len(manifest['knowledge']['topics']), 11)
        self.assertTrue((ROOT / 'llms.txt').is_file())
        self.assertTrue((ROOT / 'llms-full.txt').is_file())
        self.assertTrue((ROOT / 'templates/handoff-and-changelog.md').is_file())

    def test_multi_host_installer_and_standalone_packaging(self):
        spec = importlib.util.spec_from_file_location('validate_skills', ROOT / 'scripts/validate_skills.py')
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'external-project'
            cmd = [
                sys.executable,
                str(ROOT / 'scripts/install_pdi.py'),
                str(target),
                '--hosts', 'all',
                '--mode', 'enterprise',
                '--standalone-skills',
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, res.stderr)
            self.assertTrue((target / 'AGENTS.md').is_file())
            self.assertTrue((target / 'CLAUDE.md').is_file())
            self.assertTrue((target / '.windsurfrules').is_file())
            self.assertTrue((target / '.github/copilot-instructions.md').is_file())
            self.assertTrue((target / '.cursor/rules/pdi-coordinator.mdc').is_file())
            self.assertIn('ENTERPRISE', (target / 'AGENTS.md').read_text())
            # Validate every installed standalone skill has zero broken links even without root knowledge/ folder
            for skill_md in (target / '.agents/skills').glob('*/SKILL.md'):
                self.assertEqual(validator.validate(skill_md), [], f'Broken standalone skill: {skill_md}')
                # Also verify every bundled reference file has no broken internal links
                for bundled_md in (skill_md.parent / 'references').rglob('*.md'):
                    b_text = bundled_md.read_text()
                    for link in validator.re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', b_text):
                        if '://' not in link:
                            self.assertTrue((bundled_md.parent / link).exists(), f'Broken link {link} in {bundled_md}')
            # Verify lockfile and drift check (--check)
            check_cmd = [sys.executable, str(ROOT / 'scripts/install_pdi.py'), str(target), '--check']
            check_res = subprocess.run(check_cmd, capture_output=True, text=True)
            self.assertEqual(check_res.returncode, 0, check_res.stderr)
            self.assertIn('up to date', check_res.stdout)

    def test_artifact_auditor_catches_violations_and_passes_examples(self):
        for example in ('examples/onboarding/index.html', 'examples/analytics-dashboard/index.html'):
            cmd = [sys.executable, str(ROOT / 'scripts/audit_artifact.py'), str(ROOT / example), '--strict-pii']
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, res.stderr)
        with tempfile.TemporaryDirectory() as tmp:
            bad_html = Path(tmp) / 'bad.html'
            bad_html.write_text('<html><body><h1>Title</h1><h3>Skipped</h3><input type="text"><p>Sample data here contact john.doe@gmail.com</p></body></html>')
            cmd = [sys.executable, str(ROOT / 'scripts/audit_artifact.py'), str(bad_html), '--strict-pii']
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn('missing <html lang', res.stderr)
            self.assertIn('skipped heading level', res.stderr)
            self.assertIn('input missing associated', res.stderr)
            self.assertIn('sample data', res.stdout)
            self.assertIn('unredacted email', res.stderr)

    def test_p0_knowledge_depth_judgment_and_antislop_coverage(self):
        # 1. Verify P0-A Expert Knowledge Depth across core knowledge topics
        outcomes = (ROOT / 'knowledge/product-design/outcomes.md').read_text()
        for term in ('stated request', 'underlying problem', 'counter-metric', 'Evidence hierarchy'):
            self.assertIn(term, outcomes)
        hierarchy = (ROOT / 'knowledge/ux-design/task-hierarchy.md').read_text()
        for term in ('Tables vs. Cards', 'Single-Page Form vs. Multi-Step Wizard', 'Progressive Disclosure vs. Direct Visibility', 'Search vs. Browse'):
            self.assertIn(term, hierarchy)
        cognition = (ROOT / 'knowledge/ux-design/cognitive-human-factors.md').read_text()
        for term in ('intrinsic load', 'extraneous load', 'Hick–Hyman law (with exceptions)', 'Slips vs. mistakes, confirmation vs. Undo'):
            self.assertIn(term, cognition)
        copy_doc = (ROOT / 'knowledge/ux-design/interface-copy.md').read_text()
        self.assertIn('Text overload vs. essential disclosure', copy_doc)
        contracts = (ROOT / 'knowledge/design-systems/component-contracts.md').read_text()
        self.assertIn('Reuse vs. Proliferation Decision Rule', contracts)

        # 2. Verify P0-B Design Judgment Engine & Progressive Depth in router and output contract
        router = (ROOT / 'workflows/route-task.md').read_text()
        for term in ('Context → Evidence → Alternatives → Trade-offs → Decision → Evaluation', 'Low Complexity', 'Medium Complexity', 'High Complexity', 'Graceful Degradation'):
            self.assertIn(term, router)
        output_contract = (ROOT / 'workflows/output-contract.md').read_text()
        for term in ('Generic design', 'Overdesign', 'Overengineering', 'Text overload', 'Interaction clutter', 'Context mismatch', 'False sophistication', 'Ten Evaluation Dimensions', 'Critical', 'Major', 'Minor', 'Opportunity'):
            self.assertIn(term, output_contract)

        # 3. Verify P0-C Anti-Slop Auditor warnings (card fragmentation, competing primary CTAs, apology errors, false sophistication)
        spec = importlib.util.spec_from_file_location('audit_artifact', ROOT / 'scripts/audit_artifact.py')
        auditor = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(auditor)
        with tempfile.TemporaryDirectory() as tmp:
            slop_html = Path(tmp) / 'slop.html'
            cards_markup = ''.join(f'<div class="card">Setting {i}</div>' for i in range(10))
            slop_html.write_text(
                '<!doctype html><html lang="en"><head><meta name="viewport" content="width=device-width">'
                '<title>Settings</title><style>:focus-visible{outline:2px solid blue}@media(max-width:600px){}</style></head>'
                '<body><h1>Settings</h1><p>Oops! Something went wrong.</p>'
                '<button class="btn-primary">Save</button><button class="btn-primary">Apply</button><button class="btn-primary">Update</button>'
                + cards_markup + '</body></html>'
            )
            errs, warns = auditor.audit_html(slop_html)
            self.assertEqual(errs, [])
            self.assertTrue(any('apologetic or vague error copy' in w for w in warns))
            self.assertTrue(any('competing primary buttons' in w for w in warns))
            self.assertTrue(any('card fragmentation' in w for w in warns))

            # Negative check: dense table with 0 cards or standard onboarding does not trigger false-positive slop warnings
            clean_errs, clean_warns = auditor.audit_html(ROOT / 'examples/analytics-dashboard/index.html')
            self.assertEqual(clean_errs, [])
            self.assertEqual(clean_warns, [])

            # Check false sophistication rationale detection in Markdown specs
            slop_md = Path(tmp) / 'spec.md'
            slop_md.write_text('# Redesign\nWe added glassmorphism because this feels more modern and creates a premium experience.\n')
            md_errs, md_warns = auditor.audit_markdown(slop_md)
            self.assertEqual(md_errs, [])
            self.assertTrue(any('false sophistication' in w for w in md_warns))

        # 4. Verify all 10 required P0 evaluation scenarios are documented in tests/evaluation-cases.md
        eval_cases = (ROOT / 'tests/evaluation-cases.md').read_text()
        for scenario in (
            '1. Expert enterprise workflow',
            '2. Consumer onboarding',
            '3. Analytics dashboard',
            '4. High-consequence form',
            '5. Design system component decision',
            '6. Context-dependent pattern selection',
            '7. Anti-slop correction',
            '8. Appropriate complexity protection',
            '9. Missing evidence discipline',
            '10. Simple task proportionality',
        ):
            self.assertIn(scenario, eval_cases)

    def test_governance_and_codeowners_present(self):
        codeowners = (ROOT / '.github/CODEOWNERS').read_text()
        self.assertIn('@otherthngz', codeowners)
        contributing = (ROOT / 'CONTRIBUTING.md').read_text()
        self.assertIn('@otherthngz', contributing)
        self.assertNotIn('246957476+otherthngz', contributing)
        self.assertNotIn('246957476+otherthngz', (ROOT / 'SECURITY.md').read_text())
        self.assertTrue((ROOT / 'LICENSE').is_file())
        self.assertIn('MIT License', (ROOT / 'LICENSE').read_text())
        self.assertTrue((ROOT / 'SECURITY.md').is_file())
        self.assertIn('otherthngz', (ROOT / 'SECURITY.md').read_text())
        self.assertFalse((ROOT / 'index.html').exists())

    def test_startercn_template_and_package_cli(self):
        self.assertTrue((ROOT / 'package.json').is_file())
        self.assertTrue((ROOT / 'bin/pdi.js').is_file())
        self.assertTrue((ROOT / 'scripts/install.sh').is_file())
        self.assertTrue((ROOT / 'packaging/homebrew/pdi.rb').is_file())
        website = ROOT / 'website'
        self.assertTrue((website / 'app/(app)/(root)/page.tsx').is_file())
        self.assertTrue((website / 'components/command-box.tsx').is_file())
        self.assertTrue((website / 'content/docs/(root)/index.mdx').is_file())
        self.assertTrue((website / 'content/docs/(root)/installation.mdx').is_file())
        self.assertIn('Product Design Intelligence', (website / 'app/(app)/(root)/page.tsx').read_text())
        self.assertIn('otherthngz', (website / 'constants/site.ts').read_text())

if __name__ == '__main__':
    unittest.main()
