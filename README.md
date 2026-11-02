# DSkills

Writing, paper-review and Codex skills for Claude Code, Codex and other agents that read the [Agent Skills](https://agentskills.io) format. By Dan Ofer.

| Skill | What it does | How it starts |
|---|---|---|
| `plain-words` | Rewrites text in everyday or standard terms, one idea per sentence, without hedges or AI-sounding filler | On its own, for any text a person will read |
| `writing-for-readers` | Decides what a piece says and in what order: the finding first, every number with a comparison. Has an editing-pass guide and paper rules | On its own, for any text a person will read, or an editing pass |
| `academic-rebuttal` | Triages peer reviews, says whether to rebut or resubmit, ranks the experiments worth running, then drafts or checks the rebuttal | On its own, when you share reviews |
| `sit` | Systematic Inventive Thinking: changes the shape of the existing system first, then asks what the change is good for. For new ideas and stuck problems | On its own, when you ask to brainstorm or think creatively, or `/sit <goal or obstacle>` |
| `idea-audit` | Finds the doubt that decides whether an idea is worth pursuing, and the cheapest check that settles it | `/idea-audit <idea>` |
| `skim-review` | Final check of a paper: finds strong findings that fell out of the text, and findings a skimming reviewer would miss. Ends with a ready-or-not verdict | `/skim-review <paper> [--full]` |
| `results-page` | Builds one self-contained results page from finished analyses, for a reader who decides from that page alone | `/results-page` (in Codex, ask for it by name) |
| `codex-workers` | Claude plans and integrates; Codex does the reading, debugging and edits | `/codex-workers [--write] <task>` (Claude Code only) |
| `council` | Adds a Codex view next to Claude's: a second opinion, a critique, two blind attempts, or a judge | `/council <question>` (Claude Code only) |
| `hybrid` | Runs a Claude Code Workflow in which some stages are Codex agents and the rest are Claude agents | `/hybrid <task>` (Claude Code only) |

## Install

```bash
git clone https://github.com/ddofer/DSkills
DSkills/link.sh
```

`link.sh` links each skill into `~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex and most other agents). It skips a real folder of the same name but replaces a symlink of that name. Rerunning never removes links it made before. A `git pull` then updates every linked skill. Start a new agent session to load them.

Skills marked with a `/` command start only when you type it (in Codex, `$name` instead of `/name`; `agents/openai.yaml` in each of those folders enforces it). To install one skill, copy its folder into `~/.claude/skills` or `~/.agents/skills`. Some skills point to others: copy `plain-words` and `writing-for-readers` together, `results-page` with both, and `council` or `hybrid` with `codex-workers`.

## Codex skills: what to know

`codex-workers`, `council` and `hybrid` run Codex from inside Claude Code.

- They need the official Codex plugin and a logged-in Codex CLI. In Claude Code: `/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex`, then `/codex:setup`.
- They work only in Claude Code, so `link.sh` does not link them into `~/.agents/skills`.
- `hybrid` needs Claude Code's Workflow tool. If your build lacks it, use `/codex-workers` instead.
- Each Codex turn uses about 30k Codex tokens before it starts on the task. Give each worker one real task.
- Codex agents started from a workflow can edit files by default. Say "read-only" in the prompt unless the stage should edit.
- They start only when you type them, so they cost no context until then.

Examples:

```
/codex-workers find why tests/test_parser.py fails and fix it with the smallest patch
/council is the speedup claimed in the README supported by the benchmark script?
/hybrid audit src/ for unchecked file reads and propose a fix for each
```

## Prose lint (Claude Code hook)

`writing-for-readers/scripts/prose_lint.py` checks text an agent writes to a `.md`, `.tex`, `.rst` or `.txt` file.

- It flags em dashes, hedges, buzzwords, sentences over 40 words and similar habits. It never blocks; it tells the agent what it found.
- It skips `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, `MEMORY.md` and anything under a folder named `.claude`, `memory`, `skills`, `.git`, `.venv` or `node_modules`.
- A project can list its own banned words in `.claude/rejected-words.txt`, one per line, optionally `phrase -> use instead`.
- An empty `.claude/prose-lint-off` file turns it off for a project.

To turn it on, merge this into the `hooks` key of `~/.claude/settings.json`:

```json
"hooks": {"PostToolUse": [{"matcher": "Edit|Write|MultiEdit", "hooks": [{"type": "command",
  "command": "python3 -I \"$HOME/.claude/skills/writing-for-readers/scripts/prose_lint.py\" 2>/dev/null || true", "timeout": 10}]}]}
```

`writing-for-readers/scripts/check_edit.py OLD NEW [--reject words.txt]` compares a document's text before and after an edit. It lists lost and new numbers, long sentences, doubled words and broken `??` references.
