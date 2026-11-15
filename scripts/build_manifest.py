#!/usr/bin/env python3
"""Generate machine-readable pdi-manifest.json, llms.txt, and llms-full.txt for universal AI consumption."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_skill(path):
    text = path.read_text(encoding='utf-8')
    parts = text.split('---\n', 2)
    meta = {}
    body = text
    if len(parts) == 3 and parts[0] == '':
        for line in parts[1].splitlines():
            if ': ' in line:
                k, v = line.split(': ', 1)
                meta[k.strip()] = v.strip()
        body = parts[2].strip()
    links = [
        link for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', body)
        if '://' not in link
    ]
    return {
        'name': meta.get('name', path.parent.name),
        'description': meta.get('description', ''),
        'license': meta.get('license', 'Repository default'),
        'path': str(path.relative_to(ROOT)).replace('\\', '/'),
        'knowledge_links': [
            link.replace('../../../', '') for link in links if 'knowledge/' in link
        ],
        'workflow_links': [
            link.replace('../../../', '') for link in links if 'workflows/' in link
        ],
        'body': body,
    }


def build_all(root=ROOT):
    skills_dir = root / '.agents' / 'skills'
    skills = [parse_skill(p) for p in sorted(skills_dir.glob('*/SKILL.md'))]
    taxonomy = json.loads((root / 'knowledge' / 'taxonomy.yaml').read_text(encoding='utf-8'))
    sources = json.loads((root / 'knowledge' / 'sources.yaml').read_text(encoding='utf-8'))

    manifest = {
        'schema_version': '1.0.0',
        'name': 'Product Design Intelligence (PDI)',
        'maintainer': '@otherthngz (https://github.com/otherthngz)',
        'entrypoints': {
            'agents_md': 'AGENTS.md',
            'router': 'workflows/route-task.md',
            'output_contract': 'workflows/output-contract.md',
            'knowledge_index': 'knowledge/index.md',
            'llms_txt': 'llms.txt',
            'llms_full_txt': 'llms-full.txt',
        },
        'supported_hosts': [
            {'id': 'agents', 'files': ['AGENTS.md', '.agents/skills/*/SKILL.md']},
            {'id': 'claude', 'files': ['CLAUDE.md', '.claude/skills/*/SKILL.md']},
            {'id': 'cursor', 'files': ['.cursor/rules/pdi-*.mdc']},
            {'id': 'windsurf', 'files': ['.windsurfrules']},
            {'id': 'copilot', 'files': ['.github/copilot-instructions.md']},
            {'id': 'web-llm', 'files': ['llms.txt', 'llms-full.txt', 'pdi-manifest.json']},
        ],
        'operating_modes': ['solo', 'team', 'enterprise'],
        'complexity_levels': ['quick', 'standard', 'complex'],
        'skills': [
            {
                'name': s['name'],
                'description': s['description'],
                'license': s['license'],
                'path': s['path'],
                'knowledge_links': s['knowledge_links'],
                'workflow_links': s['workflow_links'],
            }
            for s in skills
        ],
        'knowledge': {
            'domains': taxonomy['domains'],
            'depths': taxonomy['depths'],
            'topics': taxonomy['topics'],
            'source_count': len(sources['sources']),
        },
    }

    (root / 'pdi-manifest.json').write_text(
        json.dumps(manifest, indent=2) + '\n', encoding='utf-8'
    )

    llms_lines = [
        '# Product Design Intelligence (PDI)',
        '',
        '> Portable, multi-host AI agent skill suite and curated knowledge library for product discovery, UX research, interaction design, UX writing, design systems, UI prototyping, UX auditing, and developer handoff.',
        '',
        '## Core Instructions & Contracts',
        '- [AGENTS.md](AGENTS.md): Primary agent operating rules and evidence labeling contract.',
        '- [Task Router](workflows/route-task.md): Skill selection matrix, complexity levels (quick, standard, complex), and operating modes (solo, team, enterprise).',
        '- [Output Contract](workflows/output-contract.md): Required structure for evidence tags, trade-offs, artifacts, and honest validation.',
        '- [Machine Manifest](pdi-manifest.json): Complete JSON index of skills, hosts, and knowledge taxonomy.',
        '',
        '## Agent Skills (`.agents/skills/`)',
    ]
    for s in skills:
        llms_lines.append(f"- [{s['name']}]({s['path']}): {s['description']}")

    llms_lines.extend([
        '',
        '## Curated Knowledge Topics (`knowledge/`)',
        '- [Knowledge Index](knowledge/index.md): Topic lookup table across foundation, practitioner, and advanced depths.',
    ])
    for t in taxonomy['topics']:
        llms_lines.append(f"- [{t['id']}](knowledge/{t['path']}): Domain `{t['domain']}`")

    (root / 'llms.txt').write_text('\n'.join(llms_lines) + '\n', encoding='utf-8')

    full_sections = [
        '# Product Design Intelligence (PDI) — Full AI Context Bundle',
        '',
        'This file bundles all PDI instructions, routing contracts, skills, and knowledge topics into a single document so any AI assistant (Web LLM, IDE agent, or custom RAG) can read and apply PDI immediately.',
        '',
        '---',
        '## 1. AGENTS.md',
        (root / 'AGENTS.md').read_text(encoding='utf-8').strip(),
        '',
        '---',
        '## 2. workflows/route-task.md',
        (root / 'workflows' / 'route-task.md').read_text(encoding='utf-8').strip(),
        '',
        '---',
        '## 3. workflows/output-contract.md',
        (root / 'workflows' / 'output-contract.md').read_text(encoding='utf-8').strip(),
        '',
        '---',
        '## 4. Skills (`.agents/skills/`)',
    ]
    for s in skills:
        full_sections.extend([
            '',
            f"### Skill: `{s['name']}` ({s['path']})",
            f"**Description:** {s['description']}",
            '',
            s['body'],
        ])

    full_sections.extend([
        '',
        '---',
        '## 5. Knowledge Base (`knowledge/`)',
        (root / 'knowledge' / 'design-practice.md').read_text(encoding='utf-8').strip(),
    ])
    for t in taxonomy['topics']:
        t_path = root / 'knowledge' / t['path']
        full_sections.extend([
            '',
            f"### Topic: `{t['id']}` (knowledge/{t['path']})",
            t_path.read_text(encoding='utf-8').strip(),
        ])

    (root / 'llms-full.txt').write_text('\n'.join(full_sections) + '\n', encoding='utf-8')
    return manifest


def main():
    manifest = build_all(ROOT)
    print(
        f"Generated pdi-manifest.json, llms.txt, and llms-full.txt "
        f"({len(manifest['skills'])} skills, {len(manifest['knowledge']['topics'])} topics)."
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
