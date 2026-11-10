---
name: writing-for-readers
description: Clear writing for a reader who wasn't there. What to say, in what order, in plain sentences with no filler, hedges or invented labels. Use when writing or editing anything a person will read (reports, papers, abstracts, reviews, summaries, tl;drs, captions, slides, emails, status messages, READMEs), for an editing, proofreading or cleanup pass on a draft, when asked to make text plainer, clearer, shorter, de-jargoned or less hedged, or to answer "what does X mean?".
---

# Writing for readers

Your reader wasn't there. Before writing, name who they are and what they will do with the text. Most know the field, not your project, and they skim; a tool's user or a manager may know less.

Write the way you would say it, out loud, to that reader: plainly and bluntly, in words they already know. Colloquial is fine, with contractions, "you" and short plain verbs. Only a paper needs the formal register, and even there the plain verb wins. Skip idioms a non-native reader may not know ("moves the needle").

The rules below are judgment calls with examples, not a ban list. A listed word is fine where it carries meaning ("robust standard errors"), and a rule gives way when following it would make the text harder to read. Notes for yourself or another agent can stay in note form.

- Editing, proofreading or cleaning up an existing paper, report or page: follow [`references/editing-pass.md`](references/editing-pass.md), with the rules below as its checklist.
- Writing or editing a paper: also read [`references/paper.md`](references/paper.md).
- Writing a README, a results report, a review, an email, a status message or slides: also read that form's few lines in [`references/forms.md`](references/forms.md).
- Asked to de-slop or humanize a text: make it clear with the rules below first, then follow the `deslop` skill (its `SKILL.md` is in the folder beside this one).

## Story

- **One message.** Before drafting, write in a sentence or two what the reader should remember. Everything else supports it or goes. Drop side stories; a secondary check or exception gets one main-text sentence, and its detail goes to an appendix.
- **Choose, don't transfer.** Your notes hold more than this reader needs. Give them what they need to believe the message and act on it. Leave the rest in the notes and say where they are. A detail that is true and took work to find still goes if it would not change what this reader believes or does. The pull is to hand over everything you learned; resist it, because the reader can ask. Length follows the reader's use, not how much you know.
- **Each result answers a question the reader already has.** Make the question plain (a clause is enough), give the answer with its number and comparison, then say what it changes. A number without its question reads as a log entry. The question is the reader's, not a defence against an objection nobody raised.
- **Order by the argument, not by when things were run.** Each part raises the question the next one answers. Test: if two paragraphs could swap places unnoticed, the piece is a list, not an argument.

## Order

- **Lead with the finding:** what happened, and how big. Headline the new idea or ability; a comparison leads only when it is the contribution. Open on the problem only if an introduction is needed. A first sentence that could open any piece in the field goes.
- **Headings state the claim** in a report, in a few words ("Cheaper plans sell more", not "Pricing analysis"). They drop the method, the subset and the caveats that the text below repeats. A text of a few paragraphs needs no headings.
- **Summaries and tl;drs** stay high level: findings in words, the number a reader would quote, nulls in words, why each matters. Match the length asked for. End on a plain claim the reader will remember.
- **Ground before use.** A sentence may lean only on what the reader already has: what the field knows, or what an earlier sentence gave them. That covers terms, abbreviations, run and file names, figures, and events from your own working session ("the earlier fix", "option B", "as discussed"). Define each where it first appears in the main text, never first in an appendix.
- **Old before new.** Open a sentence with something the reader has just met and end it on the new thing; the next sentence starts from there. Keep one subject through a paragraph where you can.
- **The skim test.** The title, the headings and the first sentence of each paragraph, read alone and in order, give the whole story.

## Content

- **Words first, then the one number.** State each finding in words, then give the number a reader would quote and what to compare it with: "25.6% accuracy (chance is 10%)". Say how big a finding is, even when small. Intervals, p-values, per-group values and second estimates go where a reader checks them, in the results or a table, not in an abstract, summary, message or caption. The exception is one that changes the reading: an interval that includes zero, a small denominator, a subgroup that goes the other way. Say that one, in words or as a number, wherever the claim stands alone. Without the interval, the words carry its certainty: "a clear gain", "cannot be told from zero". Where an exact figure adds nothing for this reader, words are better: "about twice as fast", "on most tasks", "no clear difference".
- **Show one real example** per finding. Keep case studies, surprises and checked negative results.
- **Explain a method once, where it first shows up:** one line on how; why only where the reader would otherwise ask or be misled. Disclose exclusions that define the population or denominator; don't defend routine choices.
- **State a limit or counterpoint once, beside the claim it limits**, and only if it changes what the reader should believe. Keep conditions that define the result ("in 2024 only"). A single near-miss under a robustness check does not demote a headline; a reversal does.
- **Narrow an overclaim instead of hedging it:** keep the firm part, drop the shaky part.
- **Asked to choose, choose.** "Use A unless X", not "both have merits; it depends on your needs".
- **Don't sabotage the finding.** Concede nothing beyond what the data show. If a check weakens a story, propose fixing or extending the analysis before hedging or dropping it; don't change the analysis yourself.
- **No dense blocks.** A paragraph makes one point and can be read once, at speed. Split a paragraph that stacks findings or conditions; a run of numbers goes in a table or a list. Bullets are fine when the items are parallel; a chain of reasoning stays a paragraph.
- **Compare like with like.** Numbers from different datasets or people get their own sentence or table. Never set them side by side as if one caused the other.
- **Everything must justify itself.** Every word, sentence, paragraph, list item, section, table column, figure panel, footnote and caption clause must change what the reader believes or how they read something. Ask of each: what would the reader lose without it? If nothing, cut it; don't compress it.
- **Say each thing once.** A number lives in a table or the text, not both; in the main text or the appendix, not both. Prose beside a table says in words what the table shows, with at most the one number that carries the claim; it does not read the table back. A finding is stated in full once; the abstract, introduction and summary repeat only its key number. Cover each subject in one place: the data, then its caveat, then the model, not the data, the model, then back to the data.
- **Add nothing that isn't in the sources.** Never invent a citation or a result; leave a marked placeholder for the author.

## Sentences

- **Who did what.** The actor is the subject and its action is the verb. An action hidden in a noun makes the reader rebuild the sentence: "An evaluation of both models was performed following the completion of training" becomes "After training, we evaluated both models." The same goes for "performs the ranking of" (ranks), "it is X that" and "the fact that". Use the passive only when the actor does not matter.
- **One idea per sentence.** Judge by meaning, not punctuation. Split where the reader would have to hold two claims at once; keep a tight pair together ("X rises while Y stays flat").
- **Point first.** Put the point in the main clause and reach its verb within a few words. Reasons, conditions and exceptions follow, or get their own sentence. End on the new or important word.
  - Before: "Given that the two stores ran the same promotion and differ only in page layout, the fact that their weekly sales matched in 10 of 12 weeks means the layout does not matter."
  - After: "The layout does not matter. The two stores differ only in layout, and their weekly sales matched in 10 of 12 weeks."
- **No telescoping.** Don't make the reader hold a growing chain of qualifiers before the point arrives: noun and hyphen stacks ("a click-history-plus-text ranking model"), "which… where… that…" chains, brackets inside or beside brackets. Name the thing, then say what happened to it. Give each qualifier its own sentence, or drop it if the reader doesn't need it.
  - Before: "The redesigned flow's Q3 mobile returning-user median checkout time fell 12%."
  - After: "We looked at returning customers on phones, July to September. With the new checkout, half of them finished in a time 12% shorter than before."
- **Parallel things in parallel form.** Compared items get the same words in the same order: "the new page gains 3 points; the old page loses 1", not "the new page gains 3 points. For the old page there was a 1-point drop."
- **Short is not compressed.** Cut ideas, not the small words that connect them. Keep the articles, the verbs and the "because". No note form; no arrow, slash or "+" standing in for a verb; no abbreviation the reader was never given. Test: can it be read aloud as a sentence?
  - Before: "small → large model: gain +0.02 → +0.10 (rerun spread ±0.005, so real)."
  - After: "The gain rises from +0.02 for the small model to +0.10 for the large one. Repeat runs differ by only ±0.005."

## Words

- **Say it the ordinary way.** Use what someone outside the project would call it, or the field's standard term ("odds ratio", "95% interval"). Never a name you invented: a project nickname ("the dial", "bucket B"), or a phrase built on the spot from abstract nouns ("the training-completion boundary" for "when training ends", "compute resource" for a GPU). Test: would the reader say it this way themselves?
- **Name the specific thing.** A word the reader can neither picture nor check tells them nothing. "Performance improved" becomes "accuracy rose from 71% to 74%"; "several factors" become the factors; "studies show" becomes the study; "is associated with" becomes the relationship, unless a correlation is all you have.
- **Every "this", "it" and "they" points at one noun** the reader has just read. If two nouns could fit, or the pointer stands for a whole paragraph, repeat the noun: "This shows" becomes "This drop shows".
- **No metaphor standing in for a measurement:** "raises the odds", not "pays", "lifts" or "flattens", unless that word is the measured quantity. A figure of speech must survive being read literally; "a backbone that fuels the landscape" does not.
- **Match the word to what was measured.** A broader word overstates ("grows" for "concentrates"). Say "significant" or "passes correction" only when the analysis computed it; "matches" only for a difference whose interval includes zero; "beats" only for a clear one. Rewording never changes a number, and a corrected estimate is not the raw measurement: "the halves correlate 0.57, which implies 0.73 for all the data", not "the halves agree at 0.73".
- **Shorter when just as clear:** "cheaper plans sell more", not "a negative association between price point and conversion probability"; "use", not "utilize"; "matches", not "is on par with"; "is" or "has", not "serves as" or "boasts"; "we kept only finished runs", not "we did not include runs that did not finish".
- **One name per thing, everywhere:** text, headings, tables, figure labels and captions. Three names read as three things. When two measures cover one idea, give each its own name every time. The same estimate has the same value everywhere. Keep the user's own terms, and a defined term that saves real space.

## Filler

Each of these sounds like content and adds none.

- **Hedges:** "it seems possible", "to our knowledge", "slightly", "about", "close to", repeated disclaimers. Next to a number, let the number say it: "moves slightly away" becomes "moves from +0.31 to +0.28"; "is not clear (−3.8; −8.7 to 1.0)" becomes "is −3.8 points (−8.7 to +1.0)". Keep "about" on a number you rounded. A null stated once in words ("no clear effect") is a finding, not a hedge.
- **Defensive setups.** Start with the action: "To check that X does not carry Y, we added Z" becomes "We added Z". Cut asides that answer an objection nobody raised ("so this cell is not a test"). Keep the purpose of a control when the reader needs it to read the result.
- **Announce, then say.** "Removing them is expected to lower the estimate. It lowers it to 1.2" becomes "Removing them lowers the estimate to 1.2". Same for colon reveals ("The key finding is clear: …"), signposts ("It is worth noting that", "Let's break this down") and "notably", "importantly", "crucially".
- **Verdicts and sales talk:** "the results reveal a nuanced picture", "plays a pivotal role", "these results are promising", "a powerful, seamless pipeline". Say what was found or what the thing does, and how big or how fast; the reader will judge.
- **Trailing "-ing" comments:** ", underscoring the importance of…", ", highlighting…", ", making it ideal for…". The tail restates or inflates the main clause. Cut it. A real consequence gets its own sentence and its evidence.
- **Recaps.** A closing sentence or paragraph that repeats what was just said ("Overall, …", "In summary, …"). Stop after the last new thing.
- **Rhythm standing in for content.** A contrast nobody raised ("not X, but Y" when no one claimed X; a reflexive "not only"), a list padded to three, a rhetorical question before the answer, a paragraph opened with "Moreover" or "Furthermore". State the central contrast once. Let the order of sentences carry the connection, and write "because", "so" or "but" where the reader could not guess the link.
- **Slogans, fragments and staccato:** "Same data. Different questions." Write a plain sentence, and join short sentences that make one argument.
- **Buzzwords and intensifiers:** "leverage", "robust", "nuanced", "landscape", "delve", "showcase"; "very", "highly", "extremely". Use the ordinary word or the measured quantity.
- **Orphaned "also", "further", "another"** left after an edit removed what they pointed back to.
- **Em dashes in prose.** Use a comma or a new sentence.
- **Process talk.** How the work was governed is not a finding: gates, pass rules, what was fixed in advance, preregistration, who decided what and when, content warnings, notes on your own process. Give the result and what it is compared with. Keep a process sentence only when it changes how to read a number ("we chose the recipe by looking at these test scores", a threshold picked after seeing the results), and state it once.
- **Edit history.** Outside a changelog, describe the thing as it is, not how it changed: "now uses a hash map instead of the old loop" becomes "uses a hash map".
- **Text only the writer needs:** file names, variables, job ids, internal section labels, notes for the next agent, provenance bookkeeping, chat leftovers ("Here is the revised version", "Let me know if…"). Move sources to a sources list; delete the rest.

## Figures and tables

- Each panel makes one point the text cannot make as well. Make the metric, the better direction and the baselines obvious.
- Real names, not codes; the simplest chart; titled axes; one label scheme, matching the caption and text. Put a direct label next to the series it names.
- Decode every colour, marker, error bar and abbreviation in the figure or its caption, and give the units.
- Show all subsets, or state the rule that picked them.
- In a report, the figure title says what is shown. The caption says how to read it. It does not repeat the methods, or what the axes, legend and panel titles already show. A figure title that repeats its axis label goes.

## Before you hand it over

Read it as the reader, aloud in your head, headings and opening sentences first. Would a blunt, fluent researcher say each line this way? Could the piece be half as long? Cut whole points first, then every sentence the reader would not miss. Does each number say "compared with what"? Change no number. If something is missing or two numbers disagree, tell the author instead of filling the gap.

For a long piece, or one that decides something, hand it to a fresh reader who was told nothing (a subagent). Ask them to restate the main finding, and to mark every word they had to guess and every place they thought "why am I told this?" (context is missing) or "so what?" (the conclusion is missing). Fix those.
