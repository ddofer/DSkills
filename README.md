# Agent skills

Dan Ofer's writing and research skills for Claude Code, Codex and other agents that read the [Agent Skills](https://agentskills.io) format.

| Skill | What it does | How it starts |
|---|---|---|
| `plain-words` | Rewrites text in everyday or standard terms, one idea per sentence | Automatically, on any text a person will read |
| `writing-for-readers` | Puts the finding first and gives every number a comparison | Automatically, on any text a person will read |
| `results-page` | Builds one results page from finished analyses, for a reader new to the project | Only when you type `/results-page` (in Claude Code) |
| `academic-rebuttal` | Triages peer reviews, ranks experiments, then drafts the rebuttal | Automatically, when you share reviews |

## Install

On a machine that mounts `/storage`, link the skills into your own home folder:

```bash
/storage/users/ddofer/agent-skills/link.sh
```

This links each skill into `~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex and most other agents). It never replaces a real folder: if you already have your own copy of a skill, move it aside and rerun. Edits here then reach every linked machine and user at once. Start a new agent session to pick them up.

Without `/storage`, copy a skill folder into one of those two folders.

## Edit

Each skill is one folder with a `SKILL.md`. Keep it short: an agent reads the `description` line in every session and the rest only when the skill starts. Commit each change here.
