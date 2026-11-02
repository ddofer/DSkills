---
name: idea-audit
description: Checks whether a proposed idea, hypothesis, design or solution is worth pursuing. Looks at the mechanism, the assumptions, what already exists, and the one check that would settle it. Manual only; start with /idea-audit <idea>.
disable-model-invocation: true
argument-hint: "<the idea, proposal or design to audit>"
---

Idea: $ARGUMENTS

## Steps

1. **State the idea** in one paragraph: what changes, what gain is expected, by what mechanism, and compared with what. Mark each part as known, assumed or predicted. If the comparison is missing, that is the first finding.
2. **Find the weaknesses that matter.** Usually one or two of: an existing thing that already does this; a mechanism that does not hold; a confound or leak that would fake the gain; a cost that outweighs it; a side effect. Skip edge cases that would not change the decision.
3. **Repair what can be repaired** while keeping the promising part: a narrower claim, a simpler version, a different implementation. If the fix needs a new design, offer `/sit`. Do not rescue a premise that has no support.
4. **Name the check.** For each doubt left: the comparison, experiment, prototype or literature search that would settle it, and its cost. Look things up when a claim of novelty or feasibility matters and the tools are there; never assert originality from memory.
5. **Verdict,** in words: what is promising, what is doubtful, what to do next and why. No scores. Depth follows the stakes: a lunch idea gets a paragraph, a grant idea gets the checks run.

## Subagents

A prior-art search or a feasibility check that needs real reading goes to a fresh agent with the idea and the question, not your opinion. Before a big commitment, offer `/council` for a second model's case against it. Reconcile disagreements yourself.
