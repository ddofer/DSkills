# Agent skills

Dan Ofer's writing and research skills for Claude Code, Codex and other agents that read the [Agent Skills](https://agentskills.io) format.

| Skill | What it does | How it starts |
|---|---|---|
| `plain-words` | Rewrites text in everyday or standard terms, one idea per sentence | Automatically, on any text a person will read |
| `writing-for-readers` | Puts the finding first and gives every number a comparison | Automatically, on any text a person will read |
| `results-page` | Builds one results page from finished analyses, for a reader new to the project | Only when you type `/results-page` (in Claude Code) |
| `academic-rebuttal` | Triages peer reviews, ranks experiments, then drafts the rebuttal | Automatically, when you share reviews |
| `codex-workers` | Claude plans and integrates; Codex workers (official Codex plugin) do the reading, debugging and edits | Only `/codex-workers <task>` (Claude Code only) |
| `hybrid` | Claude Code's native Workflow orchestration with Codex agents as stages next to Claude agents | Only `/hybrid <task>` (Claude Code only) |
| `council` | A Codex perspective next to Claude's: second opinion, critique, independent attempts, judge | Only `/council <question>` (Claude Code only) |

## Install

On a machine that mounts `/storage`, link the skills into your own home folder:

```bash
/storage/users/ddofer/agent-skills/link.sh
```

This links each skill into `~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex and most other agents). It never replaces a real folder: if you already have your own copy of a skill, move it aside and rerun. Edits here then reach every linked machine and user at once. Start a new agent session to pick them up.

Without `/storage`, copy a skill folder into one of those two folders; `hybrid` and `council` also need `codex-workers`, whose reference file they read.

## Edit

Each skill is one folder with a `SKILL.md`. Keep it short: an agent reads the `description` line in every session and the rest only when the skill starts. Commit each change here.

## Codex skills

`codex-workers`, `hybrid` and `council` need the official Codex plugin in Claude Code (`/plugin marketplace add openai/codex-plugin-cc`, `/plugin install codex@openai-codex`, then `/codex:setup`) and a logged-in Codex CLI. They are manual-only (`disable-model-invocation: true`), so they cost no context until typed. The call recipe they share is `skills/codex-workers/references/codex-calls.md`. Examples:

```
/codex-workers find why plm/tests/hf/test_vocab_row_init.py fails and fix it with the smallest patch
/hybrid audit plm/hf/ for places that read CANON_TOKEN_IDS and propose a fix per site
/council is the PTM-aware LLR correction (claim B16) stated correctly in paper/main.tex?
```

