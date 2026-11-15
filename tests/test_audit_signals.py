import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_artifact', ROOT / 'scripts/audit_artifact.py')
auditor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditor)


class AuditSignalTests(unittest.TestCase):
    def test_missing_artifact_fails_cli_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'missing.html'
            result = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/audit_artifact.py'), str(path)],
                capture_output=True, text=True,
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('does not exist', result.stderr)
        self.assertNotIn('audit passed', result.stdout)

    def test_disclosure_about_simulated_payment_is_not_an_error(self):
        html = (
            '<html lang="en"><meta name="viewport"><title>Checkout</title>'
            '<style>:focus{} @media(max-width:600px){}</style><h1>Checkout</h1>'
            '<p>This is a prototype. No payment will be charged.</p></html>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'checkout.html'
            path.write_text(html)
            errors, warnings = auditor.audit_html(path)
        self.assertEqual(errors, [])
        self.assertTrue(any('prototype' in w and 'review' in w.lower() for w in warnings))

    def test_catalog_and_separate_actions_are_review_signals(self):
        html = (
            '<html lang="en"><meta name="viewport"><title>Catalog</title>'
            '<style>:focus{} @media(max-width:600px){}</style><h1>Catalog</h1>'
            + ''.join('<article class="card">Product</article>' for _ in range(9))
            + ''.join('<section><button class="primary">Action</button></section>' for _ in range(3))
            + '</html>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'catalog.html'
            path.write_text(html)
            errors, warnings = auditor.audit_html(path)
        self.assertEqual(errors, [])
        signals = [w for w in warnings if 'primary buttons' in w or 'card fragmentation' in w]
        self.assertEqual(len(signals), 2)
        self.assertTrue(all('review' in w.lower() for w in signals))
        self.assertFalse(any('detected in active view' in w for w in signals))

    def test_markdown_heading_does_not_suppress_unrelated_rationale(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'spec.md'
            path.write_text('# False sophistication\n\nThe redesign feels more modern.\n')
            errors, warnings = auditor.audit_markdown(path)
        self.assertEqual(errors, [])
        self.assertTrue(any('feels more modern' in w for w in warnings))
        self.assertTrue(all('review' in w.lower() for w in warnings))

    def test_related_css_class_names_are_not_counted_as_components(self):
        html = (
            '<html lang="en"><meta name="viewport"><title>Styles</title>'
            '<style>:focus{} @media(max-width:600px){}</style><h1>Styles</h1>'
            + ''.join('<button class="text-primary">Action</button>' for _ in range(3))
            + ''.join('<div class="discard-card">Content</div>' for _ in range(8))
            + '</html>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'styles.html'
            path.write_text(html)
            errors, warnings = auditor.audit_html(path)
        self.assertEqual(errors, [])
        self.assertFalse(any('primary buttons' in w or 'card fragmentation' in w for w in warnings))

    def test_fluid_css_avoids_false_positive_responsive_warning(self):
        html = (
            '<html lang="en"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Fluid</title><style>:focus-visible{} main{padding:clamp(16px,4vw,48px)}</style>'
            '<h1>Fluid</h1></html>'
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'fluid.html'
            path.write_text(html)
            errors, warnings = auditor.audit_html(path)
        self.assertEqual(errors, [])
        self.assertFalse(any('responsive' in w for w in warnings))


if __name__ == '__main__':
    unittest.main()
