#!/usr/bin/env python3
"""Install PDI skills, knowledge, workflows, and multi-agent host adapters into a target project."""
import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALL_HOSTS = ('agents', 'claude', 'cursor', 'windsurf', 'copilot')
VALID_MODES = ('solo', 'team', 'enterprise')

MODE_GUIDANCE = {
    'solo': (
        'Operating Mode: SOLO (Identical 8-Stage Product Designer Workflow, Adapted to Project Complexity). '
        'Validate project complexity (`quick`, `standard`, `complex`) and active UI kit (`shadcn/ui`, `Nuxt UI`, '
        '`Apple HIG`, `Material 3`, or `Custom`) first. All 9 PDI skills are available and follow the same universal '
        'Product Designer workflow (Research → Framing → IA/Flows/State Logic → UX Writing → UI Kit/Tokens → '
        'Prototype → Audit → Handoff & Changelog). Never jump to UI without foundations unless pre-framed specs '
        'are supplied. Strictly reuse unmodified UI kit components by default.'
    ),
    'team': (
        'Operating Mode: SMALL TEAM (Identical 8-Stage Product Designer Workflow, Nimble Cross-Functional Focus). '
        'Validate what the PM or engineers have already defined and which UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, '
        '`Material 3`, or `Custom`) is active in the repo. Keep execution lightweight and collaborative: reuse stock '
        'UI kit components without inventing bespoke widgets, maintain a shared UI copy glossary, and deliver the '
        'multi-audience handoff & decision changelog (`templates/handoff-and-changelog.md`).'
    ),
    'enterprise': (
        'Operating Mode: ENTERPRISE (Identical 8-Stage Product Designer Workflow, Scoped to Role & Governance). '
        'Ask for the user\'s exact role scope and upstream/downstream team dependencies first (e.g., whether Research '
        'or Design Systems are owned by partner squads, and which organizational policies, UI kit libraries, and '
        'approval owners apply). Execute the required workflow stages within their scope, reuse unmodified '
        'design-system components by default and document essential task or accessibility gaps, run `scripts/audit_artifact.py --strict-pii`, and maintain '
        'a formal Product Decision Changelog.'
    ),
}


def compute_source_Lock():
    h = hashlib.sha256()
    for p in sorted((ROOT / '.agents' / 'skills').glob('*/SKILL.md')):
        h.update(p.read_bytes())
    for p in sorted((ROOT / 'knowledge').rglob('*.md')):
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


def parse_frontmatter(text):
    parts = text.split('---\n', 2)
    if len(parts) != 3 or parts[0] != '':
        return {}, text
    meta = {}
    for line in parts[1].splitlines():
        if ': ' in line:
            k, v = line.split(': ', 1)
            meta[k.strip()] = v.strip()
    return meta, parts[2]


def rewrite_skill_links_for_standalone(skill_dir):
    """Copy referenced repo files into skill_dir/references/bundle/ and rewrite ../../../ links."""
    skill_md = skill_dir / 'SKILL.md'
    text = skill_md.read_text(encoding='utf-8')
    bundle_dir = skill_dir / 'references' / 'bundle'
    copied = set()

    def copy_with_local_links(src_file):
        src_file = src_file.resolve()
        if src_file in copied or not src_file.is_file() or ROOT not in src_file.parents:
            return
        copied.add(src_file)
        rel = src_file.relative_to(ROOT)
        dest = bundle_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest)
        if src_file.suffix.lower() == '.md':
            src_text = src_file.read_text(encoding='utf-8')
            for sub_link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', src_text):
                if '://' not in sub_link and not sub_link.startswith('mailto:'):
                    copy_with_local_links(src_file.parent / sub_link)

    def repl(match):
        label, rel_url = match.group(1), match.group(2)
        if not rel_url.startswith('../../../'):
            return match.group(0)
        clean_rel = rel_url.split('#')[0]
        anchor = ('#' + rel_url.split('#', 1)[1]) if '#' in rel_url else ''
        repo_rel = clean_rel.replace('../../../', '', 1)
        src = (ROOT / repo_rel).resolve()
        if not src.is_file():
            return match.group(0)
        copy_with_local_links(src)
        new_rel = f'references/bundle/{repo_rel}{anchor}'
        return f'[{label}]({new_rel})'

    updated = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl, text)
    skill_md.write_text(updated, encoding='utf-8')


def write_or_skip(dest, content, force=False, append=False):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        if append:
            existing = dest.read_text(encoding='utf-8')
            if content.strip() not in existing:
                dest.write_text(existing.rstrip() + '\n\n' + content, encoding='utf-8')
            return 'appended'
        if not force:
            return 'skipped (exists)'
    dest.write_text(content, encoding='utf-8')
    return 'written'


def build_host_instructions(mode, standalone=False):
    base = (ROOT / 'AGENTS.md').read_text(encoding='utf-8').strip()
    if standalone:
        base = base.replace('(workflows/route-task.md)', '(.agents/workflows/route-task.md)')
        base = base.replace('(workflows/output-contract.md)', '(.agents/workflows/output-contract.md)')
        base = base.replace('(knowledge/index.md)', '(.agents/knowledge/index.md)')
    mode_block = f'\n\n## Default Operating Mode\n\n{MODE_GUIDANCE[mode]}\n'
    skills_list = []
    for path in sorted((ROOT / '.agents' / 'skills').glob('*/SKILL.md')):
        meta, _ = parse_frontmatter(path.read_text(encoding='utf-8'))
        skills_list.append(f"- `{meta.get('name', path.parent.name)}`: {meta.get('description', '')}")
    catalog_block = (
        '\n## Installed PDI Skills (Load on demand via `.agents/skills/<name>/SKILL.md`)\n\n'
        + '\n'.join(skills_list)
        + '\n'
    )
    return base + mode_block + catalog_block


def check_sync(target_dir):
    target = Path(target_dir).resolve()
    lock_file = target / '.agents' / 'pdi-lock.json'
    if not lock_file.is_file():
        return False, 'missing .agents/pdi-lock.json in target'
    lock_data = json.loads(lock_file.read_text(encoding='utf-8'))
    current_hash = compute_source_Lock()
    if lock_data.get('content_hash') != current_hash:
        return False, f"drift detected: target has {lock_data.get('content_hash')}, source is {current_hash}"
    return True, f"up to date (hash {current_hash}, mode {lock_data.get('mode')})"


def install(target_dir, hosts=ALL_HOSTS, mode='solo', standalone=False, force=False, append=False):
    target = Path(target_dir).resolve()
    if not target.exists():
        target.mkdir(parents=True, exist_ok=True)

    report = []
    skills_dest = target / '.agents' / 'skills'
    skills_dest.mkdir(parents=True, exist_ok=True)

    for skill_src in sorted((ROOT / '.agents' / 'skills').iterdir()):
        if not skill_src.is_dir() or not (skill_src / 'SKILL.md').is_file():
            continue
        dest_skill = skills_dest / skill_src.name
        if dest_skill.exists():
            if not force:
                report.append(f'.agents/skills/{skill_src.name}: skipped (exists)')
                continue
            shutil.rmtree(dest_skill)
        shutil.copytree(skill_src, dest_skill)
        if standalone:
            rewrite_skill_links_for_standalone(dest_skill)
        report.append(f'.agents/skills/{skill_src.name}: installed')

    support_root = (target / '.agents') if standalone else target
    for folder in ('workflows', 'knowledge', 'adapters', 'templates'):
        src_folder = ROOT / folder
        dest_folder = support_root / folder
        if dest_folder.exists():
            if force:
                shutil.rmtree(dest_folder)
                shutil.copytree(src_folder, dest_folder)
                report.append(f'{dest_folder.relative_to(target)}: overwritten')
            else:
                report.append(f'{dest_folder.relative_to(target)}: skipped (exists)')
        else:
            shutil.copytree(src_folder, dest_folder)
            report.append(f'{dest_folder.relative_to(target)}: installed')

    instructions = build_host_instructions(mode=mode, standalone=standalone)

    if 'agents' in hosts:
        status = write_or_skip(target / 'AGENTS.md', instructions, force=force, append=append)
        report.append(f'AGENTS.md: {status}')

    if 'claude' in hosts:
        status = write_or_skip(target / 'CLAUDE.md', instructions, force=force, append=append)
        report.append(f'CLAUDE.md: {status}')
        claude_skills = target / '.claude' / 'skills'
        claude_skills.mkdir(parents=True, exist_ok=True)
        for skill_dir in sorted(skills_dest.iterdir()):
            if skill_dir.is_dir():
                c_dest = claude_skills / skill_dir.name
                if c_dest.exists() and force:
                    shutil.rmtree(c_dest)
                if not c_dest.exists():
                    shutil.copytree(skill_dir, c_dest)
        report.append('.claude/skills: synced')

    if 'cursor' in hosts:
        cursor_dir = target / '.cursor' / 'rules'
        cursor_dir.mkdir(parents=True, exist_ok=True)
        router_mdc = (
            '---\n'
            'description: PDI Product Design Intelligence coordinator, router, and output contract\n'
            'globs: \n'
            'alwaysApply: true\n'
            '---\n\n'
            + instructions
        )
        status = write_or_skip(cursor_dir / 'pdi-coordinator.mdc', router_mdc, force=force)
        report.append(f'.cursor/rules/pdi-coordinator.mdc: {status}')
        for skill_dir in sorted(skills_dest.iterdir()):
            skill_file = skill_dir / 'SKILL.md'
            if not skill_file.is_file():
                continue
            meta, body = parse_frontmatter(skill_file.read_text(encoding='utf-8'))
            mdc = (
                '---\n'
                f"description: {meta.get('description', skill_dir.name)}\n"
                'globs: \n'
                'alwaysApply: false\n'
                '---\n\n'
                + body.strip() + '\n'
            )
            write_or_skip(cursor_dir / f'pdi-{skill_dir.name}.mdc', mdc, force=force)
        report.append('.cursor/rules/pdi-*.mdc: synced')

    if 'windsurf' in hosts:
        status = write_or_skip(target / '.windsurfrules', instructions, force=force, append=append)
        report.append(f'.windsurfrules: {status}')

    if 'copilot' in hosts:
        status = write_or_skip(
            target / '.github' / 'copilot-instructions.md',
            instructions,
            force=force,
            append=append,
        )
        report.append(f'.github/copilot-instructions.md: {status}')

    # Write lockfile to prevent silent version drift
    lock_file = target / '.agents' / 'pdi-lock.json'
    lock_payload = {
        'schema_version': '1.0.0',
        'content_hash': compute_source_Lock(),
        'mode': mode,
        'standalone': standalone,
        'hosts': list(hosts),
    }
    lock_file.write_text(json.dumps(lock_payload, indent=2) + '\n', encoding='utf-8')
    report.append(f".agents/pdi-lock.json: recorded ({lock_payload['content_hash']})")

    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='Target project directory path')
    parser.add_argument(
        '--hosts',
        default='all',
        help='Comma-separated AI hosts to configure: all, or subset of agents,claude,cursor,windsurf,copilot',
    )
    parser.add_argument(
        '--mode',
        choices=VALID_MODES,
        default='solo',
        help='Default operating mode to configure in host instructions (solo, team, enterprise)',
    )
    parser.add_argument(
        '--standalone-skills',
        action='store_true',
        help='Bundle referenced knowledge and workflows inside each skill folder and under .agents/ so root stays clean',
    )
    parser.add_argument('--force', action='store_true', help='Overwrite existing PDI files in target')
    parser.add_argument('--append', action='store_true', help='Append PDI instructions to existing host rule files')
    parser.add_argument('--check', action='store_true', help='Check if target installation is in sync with source PDI')
    args = parser.parse_args()

    if args.check:
        ok, msg = check_sync(args.target)
        print(msg)
        return 0 if ok else 1

    if args.hosts == 'all':
        hosts = ALL_HOSTS
    else:
        hosts = tuple(h.strip() for h in args.hosts.split(',') if h.strip())
        invalid = [h for h in hosts if h not in ALL_HOSTS]
        if invalid:
            print(f'Unknown host(s): {", ".join(invalid)}', file=sys.stderr)
            return 1

    results = install(
        args.target,
        hosts=hosts,
        mode=args.mode,
        standalone=args.standalone_skills,
        force=args.force,
        append=args.append,
    )
    for line in results:
        print(line)
    return 0


if __name__ == '__main__':
    sys.exit(main())
