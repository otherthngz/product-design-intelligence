#!/usr/bin/env python3
"""Validate the deliberately simple frontmatter used by this repository's skills."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'

def validate(path):
    errors = []
    text = path.read_text(encoding='utf-8')
    parts = text.split('---\n', 2)
    if len(parts) != 3 or parts[0] != '':
        return ['missing YAML frontmatter delimiters']
    # This validator supports single-line scalars only; full YAML needs a YAML parser.
    lines = parts[1].splitlines()
    if len(lines) not in (2, 3) or not lines[0].startswith('name: ') or not lines[1].startswith('description: ') or (len(lines) == 3 and not lines[2].startswith('license: ')):
        return ['expected single-line name and description, with optional license']
    name, description = lines[0][6:], lines[1][13:]
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != path.parent.name:
        errors.append('invalid name or directory mismatch')
    if not description or len(description) > 1024 or ': ' in description or ' #' in description:
        errors.append('invalid or unsupported plain-scalar description')
    if len(lines) == 3:
        license_value = lines[2][9:]
        if not license_value:
            errors.append('empty license')
        elif license_value.endswith('.txt'):
            license_file = license_value.rsplit(' ', 1)[-1]
            if not (path.parent / license_file).is_file():
                errors.append(f'missing license file: {license_file}')
    if not parts[2].strip():
        errors.append('missing instructions')
    for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', parts[2]):
        if '://' not in link and not (path.parent / link).exists():
            errors.append(f'broken local link: {link}')
    return errors

def main():
    paths = sorted(SKILLS.glob('*/SKILL.md'))
    if not paths:
        print('No skills found', file=sys.stderr)
        return 1
    failed = False
    for path in paths:
        errors = validate(path)
        print(f'{path.parent.name}: ' + ('; '.join(errors) if errors else 'OK'))
        failed |= bool(errors)
    return int(failed)

if __name__ == '__main__':
    sys.exit(main())
