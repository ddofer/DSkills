---
name: council
description: A Codex view next to Claude's - a second opinion, a focused adversarial review, independent attempts or a judge. Use only when the user asks for Codex or a second model, or names /council, including for a reviewer subagent or workflow stage.
argument-hint: "<question, decision, draft or diff to deliberate>"
---

A second model trained differently catches different mistakes. Use it only where the answer is uncertain, contested or costly to get wrong. Pick the smallest form that settles the question, then decide in Claude and say why.

Question: $ARGUMENTS

## Forms, smallest first

1. **Second opinion.** One read-only Codex task with the question and the evidence you have. Use for "is this reading right", "what am I missing", a plan check.
2. **Focused adversarial review.** One read-only Codex worker per concern, told to refute only that concern (Reviews in codex-calls.md). Use before a risky change or a claim the user will act on.
3. **Independent attempts.** A Claude subagent and a Codex worker get the same brief, blind to each other, in parallel. Compare where they agree and disagree; agreement is weak evidence, a disagreement is the finding. Use for design choices, stuck bugs and ideas.
4. **Judge.** A third voice scores the attempts against stated criteria. Only when you cannot decide from the comparison yourself.

Add agents, extra attempts or a synthesis round only when the previous round left a real disagreement. Do not run the whole task through both models.

## How to run it

- Codex calls: [~/.claude/skills/codex-workers/references/codex-calls.md](../codex-workers/references/codex-calls.md). Read-only unless the user asked for edits. Parallel calls go in one message so they overlap.
- Claude voices: the Agent tool with a fresh subagent and the same brief; give it the evidence, not your conclusion, so it is not anchored.
- Inside a `/hybrid` workflow, a council is one stage: a `parallel()` of a Claude agent and a `codex:codex-rescue` agent, then a Claude stage that compares.

## Synthesis

State in the reply: what each side said in one line, where they disagree, the decision, and the reason. Keep the evidence (file:line, test output) and drop the rest. Record a decision that will matter later where the repo keeps such notes; do not log routine council runs.
