"""Print the skim view of a paper: python3 skim_view.py main.tex|report.md [more files]

What an experienced reader sees first: title, abstract, headings, figure and table captions, the
first and last paragraph of each section, and the whole conclusion. LaTeX \\input and \\include
files are followed. Use it to give a reader only this view, so they cannot read the rest.
"""
import re
import sys
from pathlib import Path


def tex_text(path, seen=None):
    seen = seen or set()
    if path in seen or not path.exists():
        return ''
    seen.add(path)
    out = []
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        line = re.sub(r'(?<!\\)%.*', '', line)
        m = re.search(r'\\(?:input|include)\{([^}]+)\}', line)
        if m:
            sub = path.parent / m.group(1)
            sub = sub if sub.suffix else sub.with_suffix('.tex')
            out.append(tex_text(sub, seen))
        else:
            out.append(line)
    return '\n'.join(out)


def paragraphs(block):
    return [' '.join(p.split()) for p in re.split(r'\n\s*\n', block) if p.strip()]


def skim_tex(text):
    yield 'TITLE', ' '.join(re.findall(r'\\title\{(.+?)\}', text, re.S))
    m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', text, re.S)
    yield 'ABSTRACT', ' '.join(m.group(1).split()) if m else ''
    for cap in re.findall(r'\\caption\{((?:[^{}]|\{[^{}]*\})*)\}', text, re.S):
        yield 'CAPTION', ' '.join(cap.split())
    parts = re.split(r'(\\(?:sub)*section\*?\{[^}]*\})', text)
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        yield 'HEADING', re.search(r'\{([^}]*)\}', head).group(1)
        body = re.sub(r'\\begin\{(figure|table|tabular|align|equation)\*?\}.*?\\end\{\1\*?\}', '', body, flags=re.S)
        ps = [p for p in paragraphs(body) if len(p.split()) > 15]
        if 'onclusion' in head:
            for p in ps:
                yield 'PARA', p
        elif ps:
            yield 'FIRST', ps[0]
            if len(ps) > 1:
                yield 'LAST', ps[-1]


def skim_md(text):
    parts = re.split(r'^(#{1,4} .*)$', text, flags=re.M)
    if parts[0].strip():
        yield 'FIRST', paragraphs(parts[0])[0]
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1]
        yield 'HEADING', head.lstrip('# ')
        ps = paragraphs(body)
        caps = [p for p in ps if re.match(r'(\*|_)?(Figure|Table|Fig\.)\s*\d', p)]
        for c in caps:
            yield 'CAPTION', c
        ps = [p for p in ps if p not in caps and not p.startswith(('|', '!', '```')) and len(p.split()) > 15]
        if re.search(r'abstract|summary|conclusion|tl;dr', head, re.I):
            for p in ps:
                yield 'PARA', p
        elif ps:
            yield 'FIRST', ps[0]
            if len(ps) > 1:
                yield 'LAST', ps[-1]


def main():
    for arg in sys.argv[1:]:
        path = Path(arg)
        if path.suffix == '.tex':
            items = skim_tex(tex_text(path))
        else:
            items = skim_md(path.read_text(encoding='utf-8', errors='replace'))
        for kind, s in items:
            if s:
                print(f'[{kind}] {s}\n')


if __name__ == '__main__':
    main()
