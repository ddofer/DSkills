---
name: writing-for-readers
description: What a piece of writing says and in what order, for a reader who wasn't there. Use when writing or editing anything a person will read (reports, papers, abstracts, summaries, tl;drs, captions, slides, emails, READMEs), or for an editing, proofreading or cleanup pass on a draft.
---

# Writing for readers

Your reader wasn't there. They know the field, not your project, and they skim. For word choice, apply `plain-words`.

- Editing, proofreading or cleaning up an existing paper, report or page: follow [`references/editing-pass.md`](references/editing-pass.md), with the rules below as its checklist.
- Writing or editing a paper: also read [`references/paper.md`](references/paper.md).

## Order

- **Lead with the finding:** what happened, and how big. Headline the new idea or ability; a comparison leads only when it is the contribution. Open on the problem only if an introduction is needed; never a generic one. Don't narrate project history or a log of what was run.
- **Headings state the claim** in a report ("Cheaper plans sell more", not "Pricing analysis"); a long report opens with a numbered list of findings.
- **Summaries and tl;drs** stay high level: findings in words, the number a reader would quote, nulls in words, why each matters. Match the length asked for. End on a plain claim the reader will remember.
- **Emails and handoffs** are a short decision list: what to do, how hard each fix is, which option needs least manual work.
- **The main text stands alone.** Define every term and comparator where it first appears there, never first in an appendix. A long report ends with a short glossary.

## Content

- **Give every number something to compare with:** "25.6% accuracy (chance is 10%)".
- **Say how big a finding is, even when small.**
- **Show one real example** per finding. Keep case studies, surprises and checked negative results.
- **Explain a method once, where it first shows up:** one line on how; why only where the reader would otherwise ask or be misled. Disclose exclusions that define the population or denominator; don't defend routine choices.
- **No content warnings or notes on your own process** unless the venue or the user asks for them. If a threshold or subset was picked after seeing the results, state the rule plainly, once.
- **State a limit once, beside the claim it limits**, and only if it changes what the reader should believe. Keep conditions that define the result ("in 2024 only"). A single near-miss under a robustness check does not demote a headline; a reversal does.
- **Narrow an overclaim instead of hedging it:** keep the firm part, drop the shaky part.
- **Don't sabotage the finding.** Concede nothing beyond what the data show. Add no contrast nobody asked for unless it changes what the reader should believe. If a check weakens a story, propose fixing or extending the analysis before hedging or dropping it; don't change the analysis yourself.
- **No dense blocks.** A paragraph makes one point and can be read once, at speed. Split a paragraph that stacks findings or conditions; a run of numbers goes in a table or a list. Bullets are fine when the items are parallel.
- **One story.** Drop side stories. Secondary checks and exceptions get one main-text sentence; their detail goes to an appendix.
- **Compare like with like.** Numbers from different datasets or people get their own sentence or table. Never set them side by side as if one caused the other.
- **Everything must justify itself.** Every word, sentence, paragraph, list item, section, table column, figure panel and caption clause must change what the reader believes or how they read something. Ask of each: what would the reader lose without it? If nothing, cut it; don't compress it.
- **Say each thing once.** A number lives in a table or the text, not both; in the main text or the appendix, not both. A finding is stated in full once; the abstract, introduction and summary repeat only its key number.
- **Add nothing that isn't in the sources.** Never invent a citation or a result; leave a marked placeholder for the author.

## Figures and tables

- Each panel makes one point the text cannot make as well. Make the metric, the better direction and the baselines obvious.
- Real names, not codes; the simplest chart; titled axes; one label scheme, matching the caption and text. Put a direct label next to the series it names.
- Show all subsets, or state the rule that picked them.
- In a report, the figure title says what is shown. The caption says how to read it and does not repeat the methods.

## Before you hand it over

Read it as the reader. For each sentence: would they miss it? Does each number say "compared with what"? Then run `plain-words`. Change no number. If something is missing or two numbers disagree, tell the author instead of filling the gap.
