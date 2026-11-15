#!/usr/bin/env python3
"""Audit HTML/CSS/Markdown artifacts for PDI compliance: accessibility, UI anti-slop, PII/secrets, and tokens."""
import argparse
import re
import sys
from pathlib import Path

PII_PATTERNS = [
    (r'\b[A-Za-z0-9._%+-]+@(?!example\.com|acme\.com|company\.com|domain\.com|test\.com|users\.noreply\.github\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', 'potential unredacted email address'),
    (r'\b(?:sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{30,}|AIza[0-9A-Za-z-_]{35})\b', 'exposed API key or token'),
    (r'\b\d{3}-\d{2}-\d{4}\b', 'potential SSN pattern'),
]

AUTHOR_NOTE_PATTERNS = [
    (r'\bsample data\b', 'author-facing "sample data" note inside UI'),
    (r'\bthis is a prototype\b', 'author-facing "this is a prototype" note inside UI'),
    (r'\billustrative only\b', 'author-facing "illustrative only" note inside UI'),
]

VAGUE_BUTTON_RE = re.compile(r'<button[^>]*>\s*(submit|ok|yes|click here|manage)\s*</button>', re.I)
APOLOGY_ERROR_RE = re.compile(r'\b(oops|uh-oh|something went wrong)\b', re.I)
FALSE_SOPH_RE = re.compile(
    r'\b(?:feels?\s+more\s+modern|creates?\s+a\s+premium\s+experience|makes?\s+the\s+ui\s+cleaner)\b',
    re.I,
)
PRIMARY_BTN_RE = re.compile(
    r'<(?:button|a)\b[^>]*\bclass=["\'](?:[^"\']*\s)?(?:btn-primary|primary|bg-primary)(?=\s|["\'])[^"\']*["\'][^>]*>',
    re.I,
)
CARD_CLASS_RE = re.compile(
    r'<(?:div|article|section)\b[^>]*\bclass=["\'](?:[^"\']*\s)?(?:card|kpi-card|stat-card)(?=\s|["\'])[^"\']*["\'][^>]*>',
    re.I,
)


def strip_tags(html_fragment):
    return re.sub(r'<[^>]+>', ' ', html_fragment).strip()


def audit_html(path, strict_pii=False):
    text = path.read_text(encoding='utf-8')
    errors = []
    warnings = []

    if not re.search(r'<html[^>]+lang=["\'][^"\']+["\']', text, re.I):
        errors.append('missing <html lang="..."> attribute')
    if not re.search(r'<meta[^>]+name=["\']viewport["\']', text, re.I):
        errors.append('missing responsive <meta name="viewport"> tag')
    if not re.search(r'<title>.*?</title>', text, re.I | re.S):
        errors.append('missing <title> element')
    if not re.search(r':focus-visible|:focus', text):
        errors.append('missing visible keyboard focus styles (:focus-visible or :focus)')
    if not re.search(r'@media\s*\(|clamp\s*\(|minmax\s*\(', text):
        warnings.append('no @media responsive query or fluid layout function detected')

    # Check heading hierarchy
    headings = [int(m.group(1)) for m in re.finditer(r'<h([1-6])\b', text, re.I)]
    if not headings or headings[0] != 1:
        warnings.append('document does not start with an <h1> heading')
    for prev, curr in zip(headings, headings[1:]):
        if curr > prev + 1:
            errors.append(f'skipped heading level: <h{prev}> followed by <h{curr}>')

    # Check inputs have accessible labels (explicit <label for>, aria-label, or implicit wrapping <label>...<input>...</label>)
    wrapped_inputs = set()
    for lbl in re.finditer(r'<label\b[^>]*>(.*?)</label>', text, re.I | re.S):
        for inp in re.finditer(r'<input\b([^>]*)>', lbl.group(1), re.I):
            wrapped_inputs.add(inp.group(1))
    for match in re.finditer(r'<input\b([^>]*)>', text, re.I):
        attrs = match.group(1)
        if re.search(r'type=["\'](?:hidden|submit|button|reset)["\']', attrs, re.I):
            continue
        has_aria = re.search(r'aria-label(?:ledby)?=["\'][^"\']+["\']', attrs, re.I)
        id_match = re.search(r'\bid=["\']([^"\']+)["\']', attrs, re.I)
        has_for = id_match and re.search(rf'<label[^>]+for=["\']{re.escape(id_match.group(1))}["\']', text, re.I)
        is_wrapped = attrs in wrapped_inputs
        if not (has_aria or has_for or is_wrapped):
            errors.append(f'input missing associated <label> or aria-label: <input{attrs[:40]}...>')

    # Check vague button labels
    for match in VAGUE_BUTTON_RE.finditer(text):
        warnings.append(f'vague button CTA label detected: "{match.group(1)}"')

    # Strip script and style before checking visible UI copy and structural anti-slop signals
    visible = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', ' ', text, flags=re.I | re.S)
    visible_text = strip_tags(visible)
    for pattern, desc in AUTHOR_NOTE_PATTERNS:
        if re.search(pattern, visible_text, re.I):
            warnings.append(f'UI copy: review {desc}; retain disclosures needed to prevent misunderstanding')

    if APOLOGY_ERROR_RE.search(visible_text):
        warnings.append('anti-slop: review possible apologetic or vague error copy ("oops" / "something went wrong"); check its context and recovery guidance')

    # Static markup cannot establish rendered visibility, task regions, or design intent.
    primary_ctas = PRIMARY_BTN_RE.findall(visible)
    if len(primary_ctas) > 2:
        warnings.append(f'anti-slop: {len(primary_ctas)} primary-styled elements in markup; review whether competing primary buttons share a task region (visibility not checked)')

    cards = CARD_CLASS_RE.findall(visible)
    if len(cards) >= 8:
        warnings.append(f'anti-slop: {len(cards)} card-class elements in markup; review for card fragmentation in context (visibility not checked)')

    if strict_pii:
        for pattern, desc in PII_PATTERNS:
            if re.search(pattern, text):
                errors.append(f'security/PII violation: {desc}')

    return errors, warnings


def audit_markdown(path, strict_pii=False):
    text = path.read_text(encoding='utf-8')
    errors = []
    warnings = []
    for match in FALSE_SOPH_RE.finditer(text):
        warnings.append(f'anti-slop (false sophistication): review "{match.group(0)}" in context for a concrete user/system benefit')
    if strict_pii:
        for pattern, desc in PII_PATTERNS:
            if re.search(pattern, text):
                errors.append(f'security/PII violation: {desc}')
    return errors, warnings


def audit_path(target_path, strict_pii=False):
    target = Path(target_path)
    if not target.exists():
        return {str(target): ['artifact path does not exist']}, {}
    files = [target] if target.is_file() else sorted(
        p for p in target.rglob('*') if p.suffix.lower() in ('.html', '.md')
    )
    all_errors = {}
    all_warnings = {}
    for f in files:
        if f.suffix.lower() == '.html':
            errs, warns = audit_html(f, strict_pii=strict_pii)
        else:
            errs, warns = audit_markdown(f, strict_pii=strict_pii)
        if errs:
            all_errors[str(f)] = errs
        if warns:
            all_warnings[str(f)] = warns
    return all_errors, all_warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', help='File or directory to audit')
    parser.add_argument('--strict-pii', action='store_true', help='Enforce PII and secret scanning (recommended for Team/Enterprise)')
    args = parser.parse_args()

    errors, warnings = audit_path(args.path, strict_pii=args.strict_pii)
    for f, warns in warnings.items():
        for w in warns:
            print(f'WARN [{f}]: {w}')
    for f, errs in errors.items():
        for e in errs:
            print(f'ERROR [{f}]: {e}', file=sys.stderr)

    if errors:
        return 1
    print(f'Artifact audit passed for {args.path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
