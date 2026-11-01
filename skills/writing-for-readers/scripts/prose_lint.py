"""PostToolUse hook: flag AI slop and rejected words in text an agent just wrote to a reader-facing file.

Reads the hook JSON on stdin and checks only the new text (Edit new_string, Write content, MultiEdit
edits). Files: .md .tex .rst .txt, except agent instruction files (CLAUDE.md, AGENTS.md, SKILL.md,
memory, .claude/). Project words: the nearest .claude/rejected-words.txt above the file, one word or
phrase per line, optionally "phrase -> use instead". A .claude/prose-lint-off file turns it off for
that project. Never blocks: hits go back to the agent as additional context.
"""
import json
import re
import sys
from pathlib import Path

EXTS = {'.md', '.tex', '.rst', '.txt'}
SKIP_NAMES = {'CLAUDE.md', 'AGENTS.md', 'SKILL.md', 'MEMORY.md'}
SKIP_PARTS = {'.claude', 'memory', 'node_modules', '.venv', '.git', 'skills'}
SLOP = [
    (r'\b(?:it seems(?: possible)?|to our knowledge|arguably|it is worth noting|interestingly|notably|importantly|crucially)\b', 'hedge or filler'),
    (r'\b(?:slightly|somewhat)\b', 'hedge: give the number instead'),
    (r'\b(?:content warning|trigger warning|quotes offensive|this paper quotes|offensive by design)\b', 'content warning'),
    (r'\b(?:pre-?regist\w*|set in advance|chosen after seeing|exploratory analys\w*)\b', 'process note'),
    (r'\bto check that\b', 'defensive setup: start with the action'),
    (r'\bis expected to\b', 'announce-then-say'),
    (r'\b(?:delve|leverag\w*|showcas\w*|nuanced)\b', 'buzzword: use the ordinary word or the measured quantity'),
    (r'^\s*(?:Moreover|Furthermore|Additionally|Overall|In conclusion),', 'transition standing in for content: drop it'),
]
MAX_WORDS = 45


def new_text(inp):
    ti = inp.get('tool_input') or {}
    if 'edits' in ti:
        return '\n'.join(e.get('new_string', '') for e in ti['edits'])
    return ti.get('new_string') or ti.get('content') or ''


def project_file(path, name):
    for d in path.parents:
        f = d / '.claude' / name
        if f.exists():
            return f
    return None


def plain(text, tex):
    text = '\n'.join(ln for ln in text.splitlines()
                     if not (' & ' in ln or ln.lstrip().startswith(('|', '<')) or ln.rstrip().endswith('\\\\')))  # table rows
    text = re.sub(r'<[^>]+>', ' ', text)
    if tex:
        text = re.sub(r'\\begin\{(tabular\w*|align\*?|equation\*?)\}.*?\\end\{\1\}', ' ', text, flags=re.S)
        text = re.sub(r'(?<!\\)%.*', '', text)
        text = re.sub(r'\\(?:begin|end|label|ref|cite\w*|input|includegraphics|usepackage)\*?(?:\[[^]]*\])?\{[^}]*\}', ' ', text)
        text = re.sub(r'\\[a-zA-Z]+\*?', ' ', text)
        text = re.sub(r'[{}$]', ' ', text)
    return text


def main():
    try:
        inp = json.load(sys.stdin)
    except ValueError:
        return
    path = Path((inp.get('tool_input') or {}).get('file_path', ''))
    if path.suffix not in EXTS or path.name in SKIP_NAMES or SKIP_PARTS & set(path.parts):
        return
    if project_file(path, 'prose-lint-off'):
        return
    raw = new_text(inp)
    if not raw.strip():
        return
    tex = path.suffix == '.tex'
    text = plain(raw, tex)
    hits = []
    if '\u2014' in raw or (tex and re.search(r'(?<!-)---(?!-)', raw)):
        hits.append('em dash in prose: use a comma or a new sentence')
    for pat, why in SLOP:
        for m in re.finditer(pat, text, re.I | re.M):
            hits.append(f'"{m.group()}": {why}')
    words = project_file(path, 'rejected-words.txt')
    if words:
        for line in words.read_text(encoding='utf-8').splitlines():
            phrase, _, instead = (s.strip() for s in line.partition('->'))
            if phrase and not phrase.startswith('#'):
                for m in re.finditer(r'(?<!\w)' + r'\s+'.join(map(re.escape, phrase.split())) + r'(?!\w)', text, re.I):
                    hits.append(f'"{m.group()}": rejected in this project' + (f'; use {instead}' if instead else ''))
    for s in re.split(r'(?<=[.!?])\s+|\n\s*\n|\n\s*(?:[-*]|\d+\.)\s+', text):
        n = len(s.split())
        if n > MAX_WORDS:
            hits.append(f'{n}-word sentence: "{" ".join(s.split()[:8])} ..."')
    if hits:
        seen = list(dict.fromkeys(hits))
        msg = (f'prose-lint on {path.name} (plain-words): ' + '; '.join(seen[:10])
               + (f'; and {len(seen) - 10} more' if len(seen) > 10 else '')
               + '. Fix the ones that are real; quoted text and defined terms may stand.')
        print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': msg}}))


if __name__ == '__main__':
    main()
