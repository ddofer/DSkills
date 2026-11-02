#!/usr/bin/env bash
# Link every skill in this repo into the folders agents read:
# ~/.claude/skills (Claude Code) and ~/.agents/skills (Codex and other Agent Skills tools).
# The Codex orchestration skills work only in Claude Code, so they skip ~/.agents/skills.
# Safe to rerun. Never replaces a real folder; move it aside first.
set -eu
src="$(cd -- "$(dirname "$0")/skills" >/dev/null && pwd)"
for dest in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
  mkdir -p "$dest"
  for skill in "$src"/*/; do
    name="$(basename "$skill")"
    case "$dest:$name" in */.agents/skills:codex-workers|*/.agents/skills:hybrid|*/.agents/skills:council) continue ;; esac
    if [ -e "$dest/$name" ] && [ ! -L "$dest/$name" ]; then
      echo "skip $dest/$name: a real folder is there" >&2
      continue
    fi
    ln -sfn "${skill%/}" "$dest/$name"
    echo "linked $dest/$name"
  done
done
