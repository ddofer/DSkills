---
name: council
description: Multi-model deliberation on demand. Brings a Codex perspective next to Claude's for a second opinion, an adversarial critique, independent attempts or a judgment, only where that improves the answer. Works without Workflow. Manual only; start with /council <question or decision>.
disable-model-invocation: true
argument-hint: "<question, decision, draft or diff to deliberate>"
---

Two models with different training see different things. Use that where the answer is uncertain, contested or costly to get wrong, and nowhere else. The council is a step, not a mode: pick the smallest form that resolves the question, then decide in Claude and say why.

Question: $ARGUMENTS

## Forms, smallest first

1. **Second opinion.** One read-only Codex task with the question and the evidence you have. Use for "is this reading right", "what am I missing", a plan check.
2. **Adversarial critique.** Ask one side to refute. For local git changes use `/codex:adversarial-review <focus>`; for a plan or draft, a Codex task told to argue against it with file:line evidence. Use before a risky change or a claim the user will act on.
3. **Independent attempts.** A Claude subagent and a Codex worker get the same brief, blind to each other, in parallel. Compare where they agree and disagree; agreement is weak evidence, a disagreement is the finding. Use for design choices, stuck bugs and ideas.
4. **Judge.** A third voice scores the attempts against stated criteria. Only when you cannot decide from the comparison yourself.

Add agents, extra attempts or a synthesis round only when the previous round left a real disagreement. Do not run the whole task through both models.

## How to run it

- Codex calls: [~/.claude/skills/codex-workers/references/codex-calls.md](../codex-workers/references/codex-calls.md). Read-only unless the user asked for edits. Parallel calls go in one message so they overlap.
- Claude voices: the Agent tool with a fresh subagent and the same brief; give it the evidence, not your conclusion, so it is not anchored.
- Inside a `/hybrid` workflow, a council is one stage: a `parallel()` of a Claude agent and a `codex:codex-rescue` agent, then a Claude stage that compares.

## Synthesis

State in the reply: what each side said in one line, where they disagree, the decision, and the reason. Keep the evidence (file:line, test output) and drop the rest. Record a decision that will matter later where the repo keeps such notes; do not log routine council runs.
