---
name: writing-for-readers
description: Decides what a piece of writing says and in what order, so a reader who wasn't there can act on it — finding first, every number with a comparison, limits stated once. Use when writing or editing anything a person will read (reports, summaries, paper sections, captions, slides, emails, Slack updates, READMEs), or when asked to make writing clearer, shorter, less hedged or readable on its own.
---

# Writing for readers

Your reader wasn't there. They know the field, not your project, and they skim. Every sentence should tell them something they need. For word choice, apply `plain-words`.

## What good looks like

- **Lead with the finding:** what happened, and how big. In a summary, one line per finding. Match the length asked for: "a few lines" means a few lines.
- **Headings state the claim.** "Edgier answers win more", not "Selection analysis". In a long piece, open with a numbered list of findings.
- **Give every number something to compare with:** "1.2× the odds of an episode without it", "25.6% (chance is 10%)".
- **Show one real example** per finding.
- **Explain a method once, where it first shows up:** one line on how, one on why this way. A long piece ends with a short glossary.
- **Say limits once, plainly, beside the claim they limit.** Keep conditions that define the result ("in 2024 only"). Say what a result rests on (which measure, a small n, what was held fixed) and whether the work is exploratory.
- **Say how big an effect is, even when small** ("adds about 0.3% to the fit").
- **Don't sabotage the finding.** Don't add contrasts nobody asked for unless they change what the reader should believe. Give an exception one sentence and move its detail to an appendix. If a check weakens a story, fix or extend the analysis before hedging or dropping it.
- **Compare like with like.** Numbers from different datasets or people get their own sentence or table. Never set them side by side as if one caused the other.
- **Figures:** the title states the finding; the caption says how to read it.

## Before you hand it over

Read it as the reader. For each sentence:

1. Would they miss it? If not, cut it: repeats, throat-clearing, restating a figure, trivial counts.
2. Does each number say "compared with what"?
3. Then run the `plain-words` check, including on the draft's own pet words.

Keep every finding and number that matters, and change none. If something is missing (a baseline, an example) or two numbers disagree, tell the author instead of filling the gap.

## Before → after

| Before | After |
|---|---|
| "Arm B1 serves mean edginess 1.62" | "A recommender that always picks its top-scored episode averages 1.62 on the edginess scale; people pick 1.21" |
| "It seems possible this is the strongest effect, though we cannot yet say." | "This is the strongest effect we measured." |
| "(see results/phase94.csv; n=142 and 97 in the smallest cells)" | (cut) |
