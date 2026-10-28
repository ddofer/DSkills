---
name: codex-workers
description: Claude plans, delegates and integrates; Codex workers do the substantive reading, diagnosis and implementation through the official Codex plugin, so the Claude session spends few tokens. Manual only; start with /codex-workers <task>.
disable-model-invocation: true
argument-hint: "[--write] <what to get done>"
---

Claude keeps the plan, the decisions and the integration. Codex does the long reading, the debugging and the edits in its own session, and returns a short result. The point is to spend Claude tokens on judgment, not on scanning files. Quality comes first: if a step needs Claude's context, do it in Claude.

Task: $ARGUMENTS

## Steps

1. **Scope in Claude.** Read CLAUDE.md or AGENTS.md guidance you already have, and locate the relevant files with a targeted search. Do not rescan the repo or re-check the Codex install each time; `/codex:setup` once per machine is enough.
2. **Split into worker tasks.** One substantive task per worker, with a clear done state. Independent tasks run in parallel; dependent ones run in sequence. If the task is small enough that writing the brief costs more than doing it, do it in Claude.
3. **Launch.** Follow [references/codex-calls.md](references/codex-calls.md): prompt file, run from the repo root, foreground runner inside a background Bash, `--json`, `--write` only for a worker that is meant to edit. Parallel writers must touch disjoint files or use a worktree.
4. **Integrate.** Read each result once. Keep the decisions, evidence and file:line references; drop the narration. Continue a specific worker with its thread id instead of re-sending context.
5. **Verify in proportion to the risk.** Run the targeted test or check the worker named; do not run the full suite unless the change warrants it. Review cycles are for changes that justify them (`/codex:review` or `/codex:adversarial-review`).
6. **Report** to the user in your own words: what was done, what the evidence is, what was left undone. Do not paste the Codex transcript.

## Rules

- One owner of integrated changes: Claude, or one Codex worker with `--write`. Never two writers on one tree.
- Respect the current permission mode and sandbox; Codex defaults to read-only and `--write` only widens it to the workspace.
- Record what helps future work (decisions, file locations, git refs) in the reply or the place the repo keeps such notes. No routine logs or status files.
- If Codex is unavailable or a worker fails twice, do the work in Claude and say so.
