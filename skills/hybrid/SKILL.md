---
name: hybrid
description: Runs a Claude Code Workflow in which some stages are Codex agents and the rest are Claude agents. Claude decomposes the task, assigns each stage to the model that fits, and integrates. Manual only; start with /hybrid <task>.
disable-model-invocation: true
argument-hint: "<task to orchestrate>"
---

Typing `/hybrid` is the user's opt-in to the Workflow tool for this task. It does not turn ultracode on globally. Use the native Workflow tool; do not build another orchestrator, and do not fall back to a different framework if Workflow is unavailable: say so and offer `/codex-workers` instead.

Task: $ARGUMENTS

## Steps

1. **Scout inline.** Find the work list first (files, modules, diff, questions) with what you already know and targeted searches. The orchestration needs the list; the task does not need to be fully understood before the list exists.
2. **Allocate.** For each stage decide which model runs it:
   - Codex stage: long reading, debugging, implementing a bounded change, an independent second opinion.
   - Claude stage: anything that needs this session's context, judgment over several results, synthesis, the final integration.
   - Both, through a council step, only where a judgment is worth a second perspective (design choice, risky fix, contested finding). Do not run every stage through both models.
   Prefer the stronger model when unsure. Leave model and effort unset unless you have a reason.
3. **Write the script.** Load the `workflow-authoring` skill for the API. Default to `pipeline()`; use a barrier only when a stage needs all prior results. Codex stages run as
   `agent(prompt, { agentType: 'codex:codex-rescue' })`, which forwards to the official plugin runtime. Put `--wait` in that prompt: without it the rescue agent may start a long task in the background and return before Codex finishes. Check that the stage returned Codex's answer before a later stage uses it. Say "read-only" in that prompt unless the stage must edit; the rescue agent defaults to write access. Do not pass `schema` to a Codex stage; parse the text in a later Claude stage if structure is needed. Parallel stages that edit need `isolation: 'worktree'` or disjoint files, and one Claude stage merges.
   The call recipe and prompt contract for Codex are in [~/.claude/skills/codex-workers/references/codex-calls.md](../codex-workers/references/codex-calls.md).
4. **Run and read.** Read the journal if a result is empty before diagnosing. Resume with `resumeFromRunId` after an edit instead of rerunning everything.
5. **Integrate and verify.** One owner for the integrated change. Targeted tests sized to the risk; no full-suite reruns by habit.
6. **Report** what each stage found, which model did it, and what is unverified.

## Rules

- Spawn agents only where they pay for themselves: a stage that one model can finish in a few tool calls is not a stage.
- Concise handoffs: give a stage the file list and the done state, not the conversation.
- No new registries, caches, MCP servers or wrappers around Workflow.
