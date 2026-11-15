import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/validate_knowledge.py'

class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.exists(), 'knowledge validator must exist')
        spec = importlib.util.spec_from_file_location('knowledge_validator', SCRIPT)
        self.validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.validator)
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'knowledge', self.root / 'knowledge')
        shutil.copytree(ROOT / '.agents', self.root / '.agents')

    def tearDown(self):
        if hasattr(self, 'tmp'):
            self.tmp.cleanup()

    def test_library_passes(self):
        self.assertEqual(self.validator.validate(self.root), [])

    def test_missing_source_is_rejected(self):
        path = self.root / 'knowledge/sources.yaml'
        registry = json.loads(path.read_text())
        registry['sources'] = []
        path.write_text(json.dumps(registry))
        self.assertTrue(any('unknown source' in e for e in self.validator.validate(self.root)))

    def test_missing_topic_file_is_rejected(self):
        index = self.root / 'knowledge/taxonomy.yaml'
        data = json.loads(index.read_text())
        data['topics'][0]['path'] = 'missing.md'
        index.write_text(json.dumps(data))
        self.assertTrue(any('missing topic' in e for e in self.validator.validate(self.root)))

    def test_missing_domain_topic_is_rejected(self):
        path = self.root / 'knowledge/taxonomy.yaml'
        data = json.loads(path.read_text())
        data['topics'] = [topic for topic in data['topics'] if topic['domain'] != 'ux-design']
        path.write_text(json.dumps(data))
        self.assertTrue(any('domain has no topic' in e for e in self.validator.validate(self.root)))

    def test_bad_source_url_is_rejected(self):
        path = self.root / 'knowledge/sources.yaml'
        data = json.loads(path.read_text())
        data['sources'][0]['url'] = 'not a url'
        path.write_text(json.dumps(data))
        self.assertTrue(any('invalid source URL' in e for e in self.validator.validate(self.root)))

    def test_broken_skill_knowledge_link_is_rejected(self):
        path = self.root / '.agents/skills/product-framing/SKILL.md'
        path.write_text(path.read_text() + '\n[missing](../../../knowledge/missing.md)\n')
        self.assertTrue(any('broken skill link' in e for e in self.validator.validate(self.root)))

    def test_missing_index_entry_is_rejected(self):
        path = self.root / 'knowledge/index.md'
        path.write_text('Empty index')
        self.assertTrue(any('missing index entry' in e for e in self.validator.validate(self.root)))

    def test_duplicate_topic_and_broken_link_are_rejected(self):
        path = self.root / 'knowledge/taxonomy.yaml'
        data = json.loads(path.read_text())
        data['topics'].append(dict(data['topics'][0]))
        path.write_text(json.dumps(data))
        topic = self.root / 'knowledge' / data['topics'][0]['path']
        topic.write_text(topic.read_text() + '\n[broken](absent.md)\n')
        errors = self.validator.validate(self.root)
        self.assertTrue(any('duplicate topic' in e for e in errors))
        self.assertTrue(any('broken link' in e for e in errors))

if __name__ == '__main__':
    unittest.main()
