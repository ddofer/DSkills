# DSkills

Skills for Claude Code, Codex and other agents that read the [Agent Skills](https://agentskills.io) format: plain writing, paper checks, inventive thinking, and running Codex from Claude Code. By Dan Ofer.

| Skill | What it does | Starts |
|---|---|---|
| `plain-words` | Everyday or standard words, one idea per sentence, no hedges or AI filler | On any text a person will read |
| `writing-for-readers` | What to say and in what order: the finding first, every number with a comparison. Includes an editing-pass guide and paper rules | On any text a person will read |
| `native-voice` | Rewrites stiff, machine-sounding sentences the way a fluent native researcher would; shortens headings, captions and figure labels | On drafts an LLM wrote, or text called wordy or AI-sounding |
| `academic-rebuttal` | Triages peer reviews, says whether to rebut or resubmit, ranks the experiments, then drafts or checks the rebuttal | When you share reviews |
| `sit` | Systematic Inventive Thinking: change the structure of what you have first, then ask what the change is good for | When you ask to brainstorm or invent, or `/sit <goal or trade-off>` |
| `idea-audit` | The doubt that decides whether an idea is worth pursuing, and the cheapest check that settles it | `/idea-audit <idea>` |
| `skim-review` | Finds strong findings that fell out of a paper, or that a skimming reviewer would miss. Ends with a ready-or-not verdict | `/skim-review <paper> [--full]` |
| `results-page` | One self-contained results page from finished analyses | `/results-page` |
| `codex-workers` | Claude plans and integrates; Codex reads, debugs and edits | `/codex-workers [--write] <task>` |
| `council` | A Codex view next to Claude's: a second opinion, a critique, two independent attempts, or a judge | `/council <question>` |
| `hybrid` | A run of Claude Code's Workflow tool in which some stages are Codex agents | `/hybrid <task>` |

A skill that starts with `/` runs only when you type it. In Codex, type `$name`.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/ddofer/DSkills/main/install.sh | bash
```

This clones the repo to `~/DSkills` (or pulls it) and links each skill into `~/.claude/skills` and `~/.agents/skills`. Run it again to update. Start a new agent session afterwards.

The link step is `link.sh`. It skips a real folder with a skill's name and replaces a symlink with that name. To install one skill, copy its folder instead; `plain-words` and `writing-for-readers` go together, `results-page` needs both, and `council` or `hybrid` need `codex-workers`.

## Codex skills

`codex-workers`, `council` and `hybrid` run Codex from inside Claude Code, so they are linked only for Claude Code. They need the Codex plugin and a logged-in Codex CLI: in Claude Code, `/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex`, then `/codex:setup`.

- `hybrid` needs Claude Code's Workflow tool. Without it, use `/codex-workers`.
- A Codex turn costs about 30k Codex tokens before the task starts, so give each worker one real task.
- Codex agents in a workflow can edit files by default. Say "read-only" in the prompt unless the stage should edit.

```
/codex-workers find why tests/test_parser.py fails and fix it with the smallest patch
/council is the speedup claimed in the README supported by the benchmark script?
/hybrid audit src/ for unchecked file reads and propose a fix for each
```

## Prose lint hook (Claude Code)

`writing-for-readers/scripts/prose_lint.py` reads the text an agent just wrote to a `.md`, `.tex`, `.rst` or `.txt` file and tells the agent about em dashes, hedges, buzzwords and sentences over 40 words. It never blocks. It skips agent instruction files (`CLAUDE.md`, `AGENTS.md`, `SKILL.md`, `MEMORY.md`) and folders named `.claude`, `memory`, `skills`, `.git`, `.venv` or `node_modules`.

Per project: banned words go in `.claude/rejected-words.txt`, one per line, optionally `phrase -> use instead`; an empty `.claude/prose-lint-off` turns the hook off.

To turn it on, merge this into the `hooks` key of `~/.claude/settings.json`:

```json
"hooks": {"PostToolUse": [{"matcher": "Edit|Write|MultiEdit", "hooks": [{"type": "command",
  "command": "python3 -I \"$HOME/.claude/skills/writing-for-readers/scripts/prose_lint.py\" 2>/dev/null || true", "timeout": 10}]}]}
```

`writing-for-readers/scripts/check_edit.py OLD NEW [--reject words.txt]` compares a document before and after an edit: lost and new numbers, long sentences, doubled words, broken `??` references.
