---
name: writing-for-readers
description: Use when writing or editing anything a person will read — reports, summaries, paper sections, figure captions, slides, emails, Slack updates, READMEs — or when asked to make writing clearer, plainer, shorter, less jargony, less hedged, or readable on its own.
---

# Writing for readers

Your reader wasn't there. They know the field, not your project, and they skim. Every sentence should tell them something they need, in words they already know.

## What good looks like

- **Lead with the finding.** What happened, and how big. In a summary, one line per finding. Match the length asked for: "a few lines" means a few lines.
- **One idea per sentence.** Plain, conversational, active: "users finish…", "we compared…".
- **Call things what they are.** Use the reader's words for things, and exact terms where they're the right word. Say what happened in plain words ("picks edgier episodes than people do"), not with labels you coined along the way or metaphors. One name per thing, everywhere, figures included.
- **Name groups by what they measure, in words the reader already has:** "the third who favour transgression most", "heavy / light Sci-Fi fans". Not a coined adjective ("the boldest third") or a technical label ("the high-appetite tercile").
- **Name a procedure by what it actually does.** A loose everyday word can mislead: "a random pick" suggests pure chance, when the model picks each item as often as it predicts. Say "picks drawn from the model's probabilities" and define it once.
- **Explain a term or method once, where it first shows up:** "its best guess (the item it scores highest)".
- **Give every number something to compare with:** "1.2× the odds of an episode without it", "25.6% (chance is 10%)".
- **Show one real example** per finding.
- **Say limits once, plainly.** No hedges ("it seems possible", "to our knowledge"). Keep conditions that define the result ("in 2024 only").
- **Don't paper over.** Say how big an effect is in plain terms, even when small ("adds about 0.3% to the fit"). Say what a result rests on: which measure, a small n, "with transgression held fixed". Say whether the work is exploratory. Say each of these once, beside the claim it limits, not only in small print.
- **Don't sabotage the finding either.** One limit, beside the claim, is enough. Don't add contrasts nobody asked for (a raw count that "disagrees" with an adjusted estimate, a subgroup where it is weaker) unless they change what the reader should believe. If a check weakens a story, fix or extend the analysis (estimate each grade freely, add the missing control) before dropping or hedging the story.
- **Plain words must keep what the number is.** When a technical term gives way to plain words, check the plain claim against the source. A corrected estimate is not the raw measurement: "the halves correlate 0.57, which implies 0.73 for all the data", not "the halves agree at 0.73". Put the technical name in the footnote.
- **Compare like with like.** Numbers from different datasets or people each get their own sentence or table. Never set them side by side as if one caused the other.
- **Figures:** the title states the finding; the caption says how to read it.

## Before you hand it over

Read it as the reader. For each sentence:

1. Would they miss it? If not, cut it: repeats, throat-clearing, restating a figure, trivial counts.
2. Is it only for you? Cut file paths, run IDs, TODOs, notes-to-self.
3. Would they stumble on a word? Swap it or define it. When editing, that includes the draft's own pet words: an edit is the time to fix them.
4. Does each number say "compared with what"?

Keep every finding and number that matters, and don't change any. If something's missing (a baseline, an example) or two numbers disagree, tell the author instead of filling the gap.

## Before → after

| Before | After |
|---|---|
| "Arm B1 serves mean edginess 1.62" | "A recommender that always picks its top-scored episode averages 1.62 on the edginess scale; people pick 1.21" |
| "It seems possible this is the strongest effect, though we cannot yet say." | "This is the strongest effect we measured." |
| "the low-appetite tercile" / "the tamest third" | "the third who favour transgression least" |
| "a random pick weighted by its scores" | "picks drawn from the model's probabilities (an answer it gives 30% is picked 30% of the time)" |
| "Knowing the player doesn't remove the overshoot; it serves bold players more" | "Knowing the player, the model still picks more transgressive answers than people do, most of all for players who favour transgression most" |
| "(see results/phase94.csv; n=142 and 97 in the smallest cells)" | (cut) |
