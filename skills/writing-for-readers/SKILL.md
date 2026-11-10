---
name: writing-for-readers
description: What a piece of writing says and in what order, for a reader who wasn't there. Use when writing or editing anything a person will read (reports, papers, abstracts, reviews, summaries, tl;drs, captions, slides, emails, status messages, READMEs), or for an editing, proofreading or cleanup pass on a draft.
---

# Writing for readers

Your reader wasn't there. Before writing, name who they are and what they will do with the text. Most know the field, not your project, and they skim; a tool's user or a manager may know less. For word choice and sentences, apply `plain-words`.

- Editing, proofreading or cleaning up an existing paper, report or page: follow [`references/editing-pass.md`](references/editing-pass.md), with the rules below as its checklist.
- Writing or editing a paper: also read [`references/paper.md`](references/paper.md).
- Writing a README, a results report, a review, an email, a status message or slides: also read that form's few lines in [`references/forms.md`](references/forms.md).

## Story

- **One message.** Before drafting, write in a sentence or two what the reader should remember. Everything else supports it or goes. Drop side stories; a secondary check or exception gets one main-text sentence, and its detail goes to an appendix.
- **Choose, don't transfer.** Your notes hold more than this reader needs. Give them what they need to believe the message and act on it. Leave the rest in the notes and say where they are. A detail that is true and took work to find still goes if it would not change what this reader believes or does. The pull is to hand over everything you learned; resist it, because the reader can ask. Length follows the reader's use, not how much you know.
- **Each result answers a question the reader already has.** Make the question plain (a clause is enough), give the answer with its number and comparison, then say what it changes. A number without its question reads as a log entry. The question is the reader's, not a defence against an objection nobody raised.
- **Order by the argument, not by when things were run.** Each part raises the question the next one answers. Test: if two paragraphs could swap places unnoticed, the piece is a list, not an argument.

## Order

- **Lead with the finding:** what happened, and how big. Headline the new idea or ability; a comparison leads only when it is the contribution. Open on the problem only if an introduction is needed. A first sentence that could open any piece in the field goes.
- **Headings state the claim** in a report ("Cheaper plans sell more", not "Pricing analysis"). A text of a few paragraphs needs no headings.
- **Summaries and tl;drs** stay high level: findings in words, the number a reader would quote, nulls in words, why each matters. Match the length asked for. End on a plain claim the reader will remember.
- **Ground before use.** A sentence may lean only on what the reader already has: what the field knows, or what an earlier sentence gave them. That covers terms, abbreviations, run and file names, figures, and events from your own working session ("the earlier fix", "option B", "as discussed"). Define each where it first appears in the main text, never first in an appendix.
- **Old before new.** Open a sentence with something the reader has just met and end it on the new thing; the next sentence starts from there. Keep one subject through a paragraph where you can.
- **The skim test.** The title, the headings and the first sentence of each paragraph, read alone and in order, give the whole story.

## Content

- **Words first, then the one number.** State each finding in words, then give the number a reader would quote and what to compare it with: "25.6% accuracy (chance is 10%)". Say how big a finding is, even when small. Intervals, p-values, per-group values and second estimates go where a reader checks them, in the results or a table, not in an abstract, summary, message or caption. The exception is one that changes the reading: an interval that includes zero, a small denominator, a subgroup that goes the other way. Say that one, in words or as a number, wherever the claim stands alone. Without the interval, the words carry its certainty: "a clear gain", "cannot be told from zero". Where an exact figure adds nothing for this reader, words are better: "about twice as fast", "on most tasks", "no clear difference".
- **Show one real example** per finding. Keep case studies, surprises and checked negative results.
- **Explain a method once, where it first shows up:** one line on how; why only where the reader would otherwise ask or be misled. Disclose exclusions that define the population or denominator; don't defend routine choices.
- **No content warnings or notes on your own process** unless the venue or the user asks for them. If a threshold or subset was picked after seeing the results, state the rule plainly, once.
- **State a limit or counterpoint once, beside the claim it limits**, and only if it changes what the reader should believe. Keep conditions that define the result ("in 2024 only"). A single near-miss under a robustness check does not demote a headline; a reversal does.
- **Narrow an overclaim instead of hedging it:** keep the firm part, drop the shaky part.
- **Asked to choose, choose.** "Use A unless X", not "both have merits; it depends on your needs".
- **Don't sabotage the finding.** Concede nothing beyond what the data show. If a check weakens a story, propose fixing or extending the analysis before hedging or dropping it; don't change the analysis yourself.
- **No dense blocks.** A paragraph makes one point and can be read once, at speed. Split a paragraph that stacks findings or conditions; a run of numbers goes in a table or a list. Bullets are fine when the items are parallel; a chain of reasoning stays a paragraph.
- **Compare like with like.** Numbers from different datasets or people get their own sentence or table. Never set them side by side as if one caused the other.
- **Everything must justify itself.** Every word, sentence, paragraph, list item, section, table column, figure panel and caption clause must change what the reader believes or how they read something. Ask of each: what would the reader lose without it? If nothing, cut it; don't compress it.
- **Say each thing once.** A number lives in a table or the text, not both; in the main text or the appendix, not both. Prose beside a table says in words what the table shows, with at most the one number that carries the claim; it does not read the table back. A finding is stated in full once; the abstract, introduction and summary repeat only its key number. Cover each subject in one place: the data, then its caveat, then the model, not the data, the model, then back to the data.
- **Add nothing that isn't in the sources.** Never invent a citation or a result; leave a marked placeholder for the author.

## Figures and tables

- Each panel makes one point the text cannot make as well. Make the metric, the better direction and the baselines obvious.
- Real names, not codes; the simplest chart; titled axes; one label scheme, matching the caption and text. Put a direct label next to the series it names.
- Decode every colour, marker, error bar and abbreviation in the figure or its caption, and give the units.
- Show all subsets, or state the rule that picked them.
- In a report, the figure title says what is shown. The caption says how to read it and does not repeat the methods.

## Before you hand it over

Read it as the reader. Could it be half as long? Cut whole points first, then every sentence the reader would not miss. Does each number say "compared with what"? Then run `plain-words`. Change no number. If something is missing or two numbers disagree, tell the author instead of filling the gap.

For a long piece, or one that decides something, hand it to a fresh reader who was told nothing (a subagent). Ask them to restate the main finding, and to mark every word they had to guess and every place they thought "why am I told this?" (context is missing) or "so what?" (the conclusion is missing). Fix those.
