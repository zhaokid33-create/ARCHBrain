#!/usr/bin/env python3
"""
brain-wakeup.py -- External Brain CLI for AI agents
Standalone: no Hermes dependency required.

Commands:
  wake-up                               -- INDEX.md + recent wiki for system prompt
  search <query>                        -- semantic search (MemPalace) or grep fallback
  add-raw <category> <title> <content>  -- write to raw/<category>/
  update-wiki <topic> <content>         -- upsert wiki/topics/<topic>.md
  add-output <type> <title> <content>   -- write to outputs/<type>/
  compile                               -- run MemPalace mine on brain/wiki/
  delete-raw <filename>                 -- delete a file from raw/ (by filename or partial match)
  delete-wiki <topic>                   -- delete a wiki/topics/<slug>.md file
  delete-output <type> <filename>       -- delete a file from outputs/<type>/
"""
import sys
import io
import os
import json
import re
import subprocess
from pathlib import Path
from datetime import date

# Force UTF-8 -- same pattern as mempalace-wakeup.py
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BRAIN_ROOT = Path(r"E:\codex\brain")
MEMPALACE_SCRIPT = Path(os.environ.get("MEMPALACE_SCRIPT", r"E:\codex\mempalace\mempalace-wakeup.py"))


# -- helpers ------------------------------------------------------------------

def _slug(title: str) -> str:
    import hashlib
    ascii_title = re.sub(r'[^\x00-\x7f]', '', title).strip()
    slug = re.sub(r'[^a-z0-9]+', '-', ascii_title.lower()).strip('-')
    # If slug is too short (< 4 chars), the title is mostly CJK — use hash
    if len(slug) < 4:
        return hashlib.md5(title.encode('utf-8')).hexdigest()[:8]
    return slug


def _today() -> str:
    return date.today().isoformat()


def _rebuild_index() -> None:
    """Rebuild INDEX.md from all files currently in wiki/topics/ and subdirs."""
    import datetime
    index_path = BRAIN_ROOT / "INDEX.md"
    wiki_dir = BRAIN_ROOT / "wiki" / "topics"
    pages = sorted(wiki_dir.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True) if wiki_dir.exists() else []

    # Group by subdir
    groups: dict = {}
    all_recent = []
    for page in pages:
        rel_parts = page.relative_to(wiki_dir).parts
        group = rel_parts[0] if len(rel_parts) > 1 else "topics"
        try:
            first_line = page.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
            title = first_line if first_line else page.stem
        except Exception:
            title = page.stem
        try:
            mdate = datetime.date.fromtimestamp(page.stat().st_mtime).isoformat()
        except Exception:
            mdate = _today()
        rel = str(page.relative_to(BRAIN_ROOT)).replace('\\', '/')
        entry = f"- [{page.stem}]({rel}) -- {title} | updated: {mdate}"
        groups.setdefault(group, []).append(entry)
        all_recent.append(f"- {mdate} [{page.stem}]({rel})")

    content = "# Brain Index\n\nAuto-maintained by brain-wakeup.py. Do not edit manually.\n\n"
    for group, entries in sorted(groups.items()):
        content += f"## {group}\n\n"
        content += "\n".join(entries) + "\n\n"
    content += "## Recent Updates\n\n"
    content += "\n".join(all_recent[:10]) + "\n"

    index_path.write_text(content, encoding='utf-8')


def _update_index(topic_slug: str, description: str = "") -> None:
    """Update index entry for one topic, then rebuild full index."""
    _rebuild_index()


# -- commands -----------------------------------------------------------------

def wake_up():
    _rebuild_index()
    index_path = BRAIN_ROOT / 'INDEX.md'
    if index_path.exists():
        print('=== BRAIN INDEX ===')
        print(index_path.read_text(encoding='utf-8'))
    else:
        print('Brain index not yet initialized.')

    wiki_dir = BRAIN_ROOT / 'wiki' / 'topics'
    if wiki_dir.exists():
        pages = sorted(wiki_dir.glob('*.md'), key=lambda p: p.stat().st_mtime, reverse=True)[:5]
        if pages:
            print('\n=== RECENT WIKI PAGES ===')
            for page in pages:
                content = page.read_text(encoding='utf-8')
                preview = '\n'.join(content.splitlines()[:20])
                print(f'\n--- {page.stem} ---\n{preview}')


def search(query: str):
    if MEMPALACE_SCRIPT.exists():
        result = subprocess.run(
            [sys.executable, str(MEMPALACE_SCRIPT), 'search', query, '--wing', 'brain_wiki'],
            capture_output=True,
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            timeout=20,
        )
        out = result.stdout.decode('utf-8', errors='replace').strip()
        if out:
            print(out)
            return

    hits = []
    for search_dir in [BRAIN_ROOT / 'wiki', BRAIN_ROOT / 'outputs']:
        for md_file in search_dir.rglob('*.md'):
            text = md_file.read_text(encoding='utf-8', errors='replace')
            if query.lower() in text.lower():
                for line in text.splitlines():
                    if query.lower() in line.lower():
                        hits.append(f'{md_file.relative_to(BRAIN_ROOT)}: {line.strip()}')
                        break
    if hits:
        print('\n'.join(hits[:20]))
    else:
        print('No results found.')


def add_raw(category: str, title: str, content: str):
    valid = {'articles', 'links', 'notes', 'media'}
    if category not in valid:
        print(f'Error: category must be one of {valid}', file=sys.stderr)
        sys.exit(1)
    dest_dir = BRAIN_ROOT / 'raw' / category
    dest_dir.mkdir(parents=True, exist_ok=True)
    slug = _slug(title)
    dest = dest_dir / f'{slug}-{_today()}.md'
    dest.write_text(f'# {title}\n\ndate: {_today()}\n\n{content}\n', encoding='utf-8')
    print(json.dumps({'status': 'ok', 'path': str(dest)}))


def update_wiki(topic: str, content: str):
    slug = _slug(topic)
    wiki_dir = BRAIN_ROOT / 'wiki' / 'topics'
    wiki_dir.mkdir(parents=True, exist_ok=True)
    dest = wiki_dir / f'{slug}.md'
    if dest.exists():
        existing = dest.read_text(encoding='utf-8')
        dest.write_text(existing.rstrip() + f'\n\n## Update {_today()}\n\n{content}\n', encoding='utf-8')
        action = 'updated'
    else:
        header = f'# {topic}\n\ntags: []\nupdated: {_today()}\nsources: []\n\n'
        dest.write_text(header + content + '\n', encoding='utf-8')
        action = 'created'
    _update_index(slug, topic)
    print(json.dumps({'status': 'ok', 'action': action, 'path': str(dest)}))


def add_output(output_type: str, title: str, content: str):
    valid = {'qa', 'summaries', 'projects'}
    if output_type not in valid:
        print(f'Error: type must be one of {valid}', file=sys.stderr)
        sys.exit(1)
    dest_dir = BRAIN_ROOT / 'outputs' / output_type
    dest_dir.mkdir(parents=True, exist_ok=True)
    slug = _slug(title)
    filename = f'{slug}.md' if output_type == 'projects' else f'{slug}-{_today()}.md'
    dest = dest_dir / filename
    full_content = f'# {title}\n\ndate: {_today()}\n\n{content}\n'
    if output_type == 'projects' and dest.exists():
        existing = dest.read_text(encoding='utf-8')
        full_content = existing.rstrip() + f'\n\n## {_today()}\n\n{content}\n'
    dest.write_text(full_content, encoding='utf-8')
    print(json.dumps({'status': 'ok', 'path': str(dest)}))


def _mempalace_delete(filepath: Path) -> None:
    """Tell MemPalace to remove a file's vectors from the index."""
    if MEMPALACE_SCRIPT.exists():
        subprocess.run(
            [sys.executable, str(MEMPALACE_SCRIPT), 'delete', str(filepath), '--wing', 'brain_wiki'],
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            timeout=30,
        )


def delete_raw(filename: str):
    """Delete a file from raw/ by exact filename or partial match."""
    raw_dir = BRAIN_ROOT / 'raw'
    matches = list(raw_dir.rglob(filename))
    if not matches:
        # try partial match
        matches = [p for p in raw_dir.rglob('*.md') if filename.lower() in p.name.lower()]
    if not matches:
        print(json.dumps({'status': 'error', 'message': f'No file matching "{filename}" found in raw/'}))
        sys.exit(1)
    if len(matches) > 1:
        print(json.dumps({'status': 'error', 'message': 'Multiple matches', 'files': [str(m) for m in matches]}))
        sys.exit(1)
    target = matches[0]
    _mempalace_delete(target)
    target.unlink()
    print(json.dumps({'status': 'ok', 'deleted': str(target)}))


def delete_wiki(topic: str):
    """Delete a wiki/topics/<slug>.md file."""
    slug = _slug(topic)
    wiki_dir = BRAIN_ROOT / 'wiki' / 'topics'
    dest = wiki_dir / f'{slug}.md'
    if not dest.exists():
        # try partial match
        matches = [p for p in wiki_dir.rglob('*.md') if topic.lower() in p.name.lower()]
        if not matches:
            print(json.dumps({'status': 'error', 'message': f'No wiki file matching "{topic}" found'}))
            sys.exit(1)
        if len(matches) > 1:
            print(json.dumps({'status': 'error', 'message': 'Multiple matches', 'files': [str(m) for m in matches]}))
            sys.exit(1)
        dest = matches[0]
    _mempalace_delete(dest)
    dest.unlink()
    _rebuild_index()
    print(json.dumps({'status': 'ok', 'deleted': str(dest)}))


def delete_output(output_type: str, filename: str):
    """Delete a file from outputs/<type>/."""
    valid = {'qa', 'summaries', 'projects'}
    if output_type not in valid:
        print(f'Error: type must be one of {valid}', file=sys.stderr)
        sys.exit(1)
    out_dir = BRAIN_ROOT / 'outputs' / output_type
    matches = list(out_dir.rglob(filename))
    if not matches:
        matches = [p for p in out_dir.rglob('*.md') if filename.lower() in p.name.lower()]
    if not matches:
        print(json.dumps({'status': 'error', 'message': f'No file matching "{filename}" found in outputs/{output_type}/'}))
        sys.exit(1)
    if len(matches) > 1:
        print(json.dumps({'status': 'error', 'message': 'Multiple matches', 'files': [str(m) for m in matches]}))
        sys.exit(1)
    target = matches[0]
    _mempalace_delete(target)
    target.unlink()
    print(json.dumps({'status': 'ok', 'deleted': str(target)}))


def compile_brain():
    if not MEMPALACE_SCRIPT.exists():
        print(f'Error: MemPalace not found at {MEMPALACE_SCRIPT}', file=sys.stderr)
        sys.exit(1)
    # Mine only content dirs — skip root-level scripts and config files
    for subdir in ['wiki', 'raw', 'outputs']:
        target = BRAIN_ROOT / subdir
        if not target.exists():
            continue
        print(f'Mining {subdir}...')
        result = subprocess.run(
            [sys.executable, str(MEMPALACE_SCRIPT), 'mine', str(target)],
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            timeout=600,
        )
        if result.returncode != 0:
            sys.exit(result.returncode)
    _rebuild_index()
    print('Done.')


# -- entry point --------------------------------------------------------------

def _resolve_content(raw: str) -> str:
    """If raw starts with @, read content from that file path.
    Otherwise replace literal \\n with real newlines."""
    if raw.startswith('@'):
        path = Path(raw[1:])
        if path.exists():
            return path.read_text(encoding='utf-8')
        print(f'Error: file not found: {path}', file=sys.stderr)
        sys.exit(1)
    return raw.replace('\\n', '\n')


if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv or argv[0] == 'wake-up':
        wake_up()
    elif argv[0] == 'search' and len(argv) > 1:
        search(argv[1])
    elif argv[0] == 'add-raw' and len(argv) >= 4:
        add_raw(argv[1], argv[2], _resolve_content(argv[3]))
    elif argv[0] == 'update-wiki' and len(argv) >= 3:
        update_wiki(argv[1], _resolve_content(argv[2]))
    elif argv[0] == 'add-output' and len(argv) >= 4:
        add_output(argv[1], argv[2], _resolve_content(argv[3]))
    elif argv[0] == 'compile':
        compile_brain()
    elif argv[0] == 'delete-raw' and len(argv) >= 2:
        delete_raw(argv[1])
    elif argv[0] == 'delete-wiki' and len(argv) >= 2:
        delete_wiki(argv[1])
    elif argv[0] == 'delete-output' and len(argv) >= 3:
        delete_output(argv[1], argv[2])
    else:
        print(
            'Usage:\n'
            '  brain-wakeup.py wake-up\n'
            '  brain-wakeup.py search <query>\n'
            '  brain-wakeup.py add-raw <category> <title> <content|@file>\n'
            '  brain-wakeup.py update-wiki <topic> <content|@file>\n'
            '  brain-wakeup.py add-output <type> <title> <content|@file>\n'
            '  brain-wakeup.py compile\n'
            '  brain-wakeup.py delete-raw <filename>\n'
            '  brain-wakeup.py delete-wiki <topic>\n'
            '  brain-wakeup.py delete-output <type> <filename>\n'
            '\n'
            'Content can be:\n'
            '  "直接文字内容，用\\\\n换行"\n'
            '  @E:\\path\\to\\file.md  (从文件读取)\n'
        )
