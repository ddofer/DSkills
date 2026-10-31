"""Mechanical checks for an editing pass: python3 check_edit.py OLD NEW [--reject WORDS.txt]

Run on built text (pdftotext main.pdf, or the rendered page), not on LaTeX or Markdown source:
undefined references show as ?? only after a build. Every line it prints is a candidate to review,
not an automatic error: a lost number may be a deliberate cut, a doubled word may be right ("had had").
It checks tokens, not meaning: a swapped or misattributed number still needs a source check.
"""
import argparse
import re
from collections import Counter

NUM = re.compile(r'(?<![\w.])[-+−]?(?:\d[\d,]*(?:\.\d+)?|\.\d+)(?:[eE][-+]?\d+)?%?')


def nums(text):
    return Counter(re.sub(r'^(-?)\.', r'\g<1>0.', n.replace('−', '-').replace(',', '').lstrip('+')) for n in NUM.findall(text))


def sentences(text):
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    text = re.sub(r'\b(e\.g|i\.e|cf|vs|Fig|Eq|Tab|al)\.\s', r'\1 ', text)  # abbreviations do not end a sentence
    text = re.sub(r'\n\s*(?:[-*•]|\d+\.)\s+', '. ', text)  # list items end a sentence
    text = re.sub(r'\n{2,}', '. ', text)
    return re.split(r'(?<=[.!?])\s+', ' '.join(text.split()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('old')
    ap.add_argument('new')
    ap.add_argument('--reject', help='file with one rejected word or phrase per line')
    ap.add_argument('--max-words', type=int, default=40)
    a = ap.parse_args()
    old, new = (open(p, encoding='utf-8').read() for p in (a.old, a.new))
    print('lost numbers:', sorted((nums(old) - nums(new)).elements()))
    print('new numbers:', sorted((nums(new) - nums(old)).elements()))
    for s in sentences(new):
        if len(s.split()) > a.max_words:
            print(f'long sentence ({len(s.split())} words):', s[:100], '...')
    for m in re.finditer(r'\b([A-Za-z]+)\s+\1\b', new, re.I):
        print('doubled word:', m.group())
    print('undefined refs (??):', new.count('??'))
    if a.reject:
        joined = re.sub(r'(\w)-\n(\w)', r'\1\2', new)  # undo line-end hyphenation
        for line in open(a.reject, encoding='utf-8'):
            w = line.partition('->')[0].strip()
            if not w or w.startswith('#'):
                continue
            for m in re.finditer(r'(?<!\w)' + r'\s+'.join(map(re.escape, w.split())) + r'(?!\w)', joined, re.I):
                print(f'rejected word "{w}":', joined[max(0, m.start() - 40):m.end() + 40].replace('\n', ' '))


if __name__ == '__main__':
    main()
