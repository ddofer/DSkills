---
name: academic-rebuttal
description: Plans and writes academic rebuttals and responses to reviewers in two stages: triage the reviews and rank the experiments worth running, then draft the response once results are in. Use when the user shares peer reviews, reviewer scores or a rebuttal deadline, asks whether to rebut or resubmit, or wants a rebuttal or response letter drafted or checked.
---

# Academic rebuttal

Resolve the few doubts that decide acceptance, within the time left. Don't answer every sentence.

**Two stages.** Stage 1 triages and plans. Stage 2 drafts, once the author supplies results or confirms no new experiment will run. Results may arrive piecemeal: integrate what is done, mark what failed or is partial, and say whether more experiments are worth the time left. If the author asks for a draft from existing evidence only, write it and mark every unsupported claim. To check an existing draft, apply Stage 2's rules to it and list what fails.

**Never invent** results, reviewer quotes or intent, citations, or manuscript locations. Never present planned work as done, hide a negative result, or promise that a future experiment will succeed. Use visible placeholders instead: `[RESULT NEEDED]`, `[SETTING NEEDED]`, `[MANUSCRIPT LOCATION NEEDED]`, `[VENUE RULE NEEDS VERIFICATION]`, `[AUTHOR CONFIRMATION NEEDED]`.

## Inputs

Stage 1 needs the abstract, every review with its score and confidence, the venue and score scale, and the deadline. Useful: the manuscript, word limit, venue policy on new experiments, compute and author time. Stage 2 also needs each completed result with its settings, number of runs and uncertainty, plus the changes and claim narrowings the authors accept.

## Stage 1: Triage and plan

1. **Rebut or resubmit?** Find the score scale and the borderline; if unknown, say the call is provisional. Classify:
   - **Promising**: at least one reviewer above borderline, concerns answerable within the deadline, no fatal flaw. Invest in targeted experiments.
   - **Borderline**: scores near the line, fixable concerns, one decisive experiment could move it. Run only fast, high-value work; log resubmission changes in parallel.
   - **Low return**: all scores below borderline, no advocate, several reviewers doubt the core premise, or the fix needs a redesign. Say so in calibrated words (never "certain rejection"). Offer a short rebuttal that corrects factual errors, then a resubmission plan ([reference/resubmission.md](reference/resubmission.md)).
2. **Split** every review into atomic concerns (C1, C2, …), one doubt each.
3. **Find the underlying concern** behind each: the decision-relevant doubt, the evidence that would settle it, and your confidence in that reading. When two readings are plausible, show both, prefer evidence and wording that hold under both, and ask the author before spending scarce time.
4. **Label** each concern: severity (fatal, major, moderate, minor), sharedness (all, several, one reviewer, chair), decision impact (high, medium, low; a major concern from one low-confidence outlier can matter less than a moderate one several reviewers share), and how it will be answered (new experiment, new analysis, existing evidence, clarification, correction, claim narrowing, defer).
5. **Rank the work.** P0 must do now (fatal or shared major concern, feasible, interpretable even if negative). P1 if time permits. P2 nice to have. P3 defer to revision. DO NOT RUN: misses the underlying concern, duplicates evidence, lacks controls, or would eat the whole period. Prefer experiments that answer several concerns at once. Never recommend an experiment just to look responsive.

**First reply** (done when every atomic concern appears in the matrix and every proposed experiment has a priority):

- viability call, with the strongest positive and negative signals and any assumptions;
- claim map from the abstract (problem, contribution, novelty, main result, scope), flagging claims broader than the evidence;
- concern matrix: `ID | Reviewer | Surface comment | Underlying concern | Alternative reading | Confidence | Severity | Shared | Impact | Answer by`;
- experiment plan: `Priority | Concern IDs | Question | Experiment | Why it changes the decision | Minimum protocol (baselines, controls, metric, seeds) | Result that would support the claim | Time/cost | What a negative result means | Fallback wording`;
- what to answer with existing evidence or clarification only;
- a time budget when the deadline is known, with nothing spent on P2 before P0 is secured;
- this template for the author's results: `Experiment ID / Concerns / Status / Protocol / Baselines / Metric / Runs / Result / Uncertainty / Surprises / Claim supported / Claim not supported / Preferred paper change`.

## Stage 2: Integrate results and draft

1. **Validate each result:** does it answer the underlying concern, under matched conditions, with enough runs? Call it positive, negative, mixed or inconclusive. Never turn an inconclusive result into a positive claim. A negative result can still help by supporting a narrower, credible claim.
2. **Update each concern** to resolved, partly resolved, unresolved, resolved by clarification, conceded and narrowed, or deferred.
3. **Draft for the neutral area chair**, not the reviewer:
   - open with a short summary: strengths the reviewers named (never invented), then the two or three main concerns;
   - order by decision weight: fatal and shared major concerns first, minor comments grouped at the end;
   - merge shared concerns instead of repeating one answer per reviewer, unless the venue needs one reply per reviewer; then answer what is left reviewer by reviewer;
   - write each response as **direct answer → evidence → revision**, with the answer in the first sentence and the exact paper change last.
   Patterns for common cases (misunderstanding, valid limitation, novelty, unfair comparison, statistics, score-text mismatch, chair notes): [reference/response-patterns.md](reference/response-patterns.md).
4. **Fit the limit.** Cut in this order: repeated thanks, repeated quotes, background, adjectives, duplicate answers, low-impact minor comments, detail not needed to read the evidence. Never cut direct answers, key numbers, controls, uncertainty, claim narrowing, unresolved limitations or promised changes. Report the final word or character count.

Done when every concern has a status, every claim in the draft points to a supplied result or manuscript location, and the paper revision list is concrete.

**Tone:** calm and auditable. "We agree", "we clarify", "our presentation may have obscured". Never question a reviewer's competence or motives, or press for a score change.
