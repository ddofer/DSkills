# Calling Codex from Claude Code

Shared by `/codex-workers`, `/hybrid` and `/council`. Checked against Codex plugin 1.0.6 and Codex CLI 0.165 (2026-10-28). If a flag below is rejected, run `node "$CODEX" --help` and `codex exec --help` once and update this file.

## The runtime

The official plugin ships a job runner, `codex-companion.mjs`. It starts Codex through the shared app-server, records the job so `/codex:status`, `/codex:result` and `/codex:cancel` see it, and cleans up at session end. Prefer it over bare `codex exec` except for the one case noted under Follow-ups.

Resolve its path once per session (`${CLAUDE_PLUGIN_ROOT}` is only set inside the plugin's own commands):

```bash
CODEX=$(ls -d ~/.claude/plugins/cache/openai-codex/codex/*/scripts/codex-companion.mjs | sort -V | tail -1)
```

If the glob is empty, Codex is not installed as a plugin: tell the user to run `/codex:setup` and stop.

## One task

```bash
cd <repo root> && node "$CODEX" task --json --prompt-file scratch/codex/<name>.md
```

- **Run from the repo root.** Jobs are keyed on the git root of the current directory.
- **Prompt in a file** under a gitignored `scratch/` (or the session scratchpad); delete it when the worker is done. Never pass the prompt as one quoted argument: the runner re-splits a single argument into flags, so any `--word` inside the prompt becomes an option.
- **`--json`** returns `{status, threadId, rawOutput, touchedFiles}`; `rawOutput` is Codex's final message. Without it you get the rendered message only.
- **`--write`** gives Codex a workspace-write sandbox. Leave it off for reading, diagnosis, research and review.
- **`--model` / `--effort`**: leave unset. The user's Codex config is the default and is the stronger choice.
- Run the call **foreground inside a Claude Bash with `run_in_background: true`**. Claude is then notified when it ends. Do not use the runner's own `--background`: it detaches and nothing tells Claude when it finishes.
- A Codex turn costs about 30k Codex tokens before the task starts, so give each worker one substantive task, not a series of trivial ones.

## Parallel workers

Launch each task as its own background Bash in the same message. They run concurrently; each completion arrives as a notification. Rules:

- Parallel workers are read-only, or edit disjoint files. Two writers on one tree conflict.
- For parallel edits of overlapping files use `codex exec --worktree` (raw CLI) or, inside a Workflow, `isolation: 'worktree'`, and let one owner merge.
- Three or four at once is plenty: each result still has to be read and integrated.

## Follow-ups

`node "$CODEX" task --resume-last` continues the newest task thread of this repo, so it cannot target one of several workers. For a specific worker, use its `threadId` from the `--json` result:

```bash
codex exec resume <threadId> -c 'sandbox_mode="read-only"' -o scratch/codex/<name>.md "<delta instruction only>"
```

Send only what changed; the thread already holds the context. `resume` has no `-s` flag and defaults to workspace-write, so the `-c` override is what keeps a read-only worker read-only; drop it only for a worker that is meant to edit. `-o` writes the final message to a file; `resume` does not accept `--color`.

## Prompt contract

Codex works best as an operator: a compact, block-structured prompt that states the job, what done looks like, and how to answer. Template (drop blocks you do not need):

```
<task>What to do, where, and the relevant failure or context. One task per run.</task>
<done>What must be true at the end (tests named, files touched, question answered).</done>
<output_contract>At most N lines. Facts first, then inferences marked as such. Cite file:line. No restating of the task.</output_contract>
<follow_through>Proceed without asking unless a step is destructive or needs a secret.</follow_through>
<scope>Only edit <files>. No unrelated refactors. Do not commit.</scope>
<verify>Run <targeted test>; report the exact command and result.</verify>
```

Codex reads `AGENTS.md`, not `CLAUDE.md`. In a repo with only `CLAUDE.md`, say in `<task>` to read it first.

## Reviews

For a review of local git changes use the plugin's own commands, which already carry the review contract: `/codex:review` (plain) or `/codex:adversarial-review <focus>` (challenges the design). Both are read-only.

## Failures

- Runner missing or Codex unauthenticated: send the user to `/codex:setup`; do not improvise another auth path.
- A task that returns nothing or fails: read its log under `/codex:status <job-id>`, retry once with a tighter prompt, then do the work in Claude and say that Codex did not deliver it.
