#!/usr/bin/env python3
"""Validate PDI's JSON-compatible YAML catalogs and linked topic files offline."""
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ('What and why', 'When to apply', 'Fundamental principles', 'Practical implementation', 'Good and bad examples', 'Common mistakes', 'Evaluate the result', 'AI application', 'Related concepts', 'References and further learning')

def validate(root):
    errors = []
    knowledge = root / 'knowledge'
    try:
        taxonomy = json.loads((knowledge / 'taxonomy.yaml').read_text(encoding='utf-8'))
        registry = json.loads((knowledge / 'sources.yaml').read_text(encoding='utf-8'))
        topics, sources = taxonomy['topics'], registry['sources']
        domains, depths = taxonomy['domains'], taxonomy['depths']
    except (OSError, ValueError, KeyError, TypeError) as error:
        return [f'invalid catalog: {error}']
    source_ids = set()
    for source in sources:
        try:
            sid = source['id']
            if sid in source_ids: errors.append(f'duplicate source: {sid}')
            source_ids.add(sid)
            for field in ('name', 'url', 'domain', 'type', 'usage', 'verified', 'status', 'review_scope'):
                if not source.get(field): errors.append(f'{sid}: missing {field}')
            date.fromisoformat(source['verified'])
            url = source['url']
            parsed = urlparse(url)
            if source['type'] == 'internal PDI guidance':
                if not (knowledge / url).is_file(): errors.append(f'{sid}: invalid source URL {url}')
            elif parsed.scheme not in ('http', 'https') or not parsed.netloc:
                errors.append(f'{sid}: invalid source URL {url}')
            if source['type'] not in ('official specification reference', 'recognized professional reference', 'community learning resource', 'internal PDI guidance'):
                errors.append(f'{sid}: invalid source type')
        except (KeyError, TypeError, ValueError) as error:
            errors.append(f'invalid source: {error}')
    try:
        index = (knowledge / 'index.md').read_text(encoding='utf-8')
    except OSError as error:
        return [f'missing knowledge index: {error}']
    seen = set()
    for topic in topics:
        try:
            tid = topic['id']
            if tid in seen: errors.append(f'duplicate topic: {tid}')
            seen.add(tid)
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', tid): errors.append(f'{tid}: invalid topic id')
            if f'`{tid}`' not in index or f']({topic["path"]})' not in index:
                errors.append(f'{tid}: missing index entry')
            if topic['domain'] not in domains: errors.append(f'{tid}: invalid domain')
            if not topic['depths'] or any(depth not in depths for depth in topic['depths']): errors.append(f'{tid}: invalid depth')
            if not topic['sources']: errors.append(f'{tid}: missing sources')
            for source in topic['sources']:
                if source not in source_ids: errors.append(f'{tid}: unknown source {source}')
            path = (knowledge / topic['path']).resolve()
            if knowledge.resolve() not in path.parents or not path.is_file():
                errors.append(f'{tid}: missing topic {topic["path"]}')
                continue
            text = path.read_text(encoding='utf-8')
            match = re.search(r'^<!-- pdi-topic: (.+) -->$', text, re.M)
            metadata = json.loads(match.group(1)) if match else {}
            if metadata != {key: topic[key] for key in ('id', 'domain', 'depths', 'sources')}:
                errors.append(f'{tid}: metadata mismatch')
            for heading in HEADINGS:
                if f'## {heading}' not in text: errors.append(f'{tid}: missing heading {heading}')
            for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', text):
                if '://' not in link and not (path.parent / link).exists(): errors.append(f'{tid}: broken link {link}')
        except (KeyError, TypeError, ValueError, OSError) as error:
            errors.append(f'invalid topic: {error}')
    for domain in domains:
        if not any(topic.get('domain') == domain for topic in topics):
            errors.append(f'{domain}: domain has no topic')
    for skill in (root / '.agents/skills').glob('*/SKILL.md'):
        text = skill.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', text):
            if 'knowledge/' in link and not (skill.parent / link).exists():
                errors.append(f'{skill.parent.name}: broken skill link {link}')
    return errors

def main():
    errors = validate(ROOT)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('Knowledge catalogs, topic metadata and local topic links: OK')
    return 0

if __name__ == '__main__':
    sys.exit(main())
