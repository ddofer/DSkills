---
name: plain-words
description: Clear sentences in plain words. The actor is the subject, each sentence makes one point, and nothing is filler, hedge, invented label or AI slop. Use for any text a person will read, when asked to make text plainer, clearer, shorter, de-jargoned, humanized, less hedged or less AI-sounding, or to answer "what does X mean?".
---

# Plain words

Write the way you would say it, out loud, to a smart colleague who wasn't in the project: plainly and bluntly, in words they already know. Colloquial is fine. Define a word once, where it first appears, if they might not know it.

The rules below are judgment calls with examples, not a ban list: a listed word is fine where it carries meaning ("robust standard errors"), and a rule gives way when following it would make a sentence harder to read. Notes for yourself or another agent can stay in note form.

For what to say and in what order, see `writing-for-readers`. To clean up a whole draft, run `writing-for-readers/references/editing-pass.md` with this skill as its checklist.

## Sentences

- **Who did what.** The actor is the subject and its action is the verb. An action hidden in a noun makes the reader rebuild the sentence: "An evaluation of both models was performed following the completion of training" becomes "After training, we evaluated both models." Use the passive only when the actor does not matter.
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

- **Say it the ordinary way.** Use what someone outside the project would call it, or the field's standard term ("odds ratio", "95% interval"). Never a name you invented: a project nickname ("the dial", "bucket B"), or a phrase built on the spot from abstract nouns ("the training-completion boundary" for "when training ends"). Test: would the reader say it this way themselves?
- **Name the specific thing.** A word the reader can neither picture nor check tells them nothing. "Performance improved" becomes "accuracy rose from 71% to 74%"; "several factors" become the factors; "studies show" becomes the study; "is associated with" becomes the relationship, unless a correlation is all you have.
- **Every "this", "it" and "they" points at one noun** the reader has just read. If two nouns could fit, or the pointer stands for a whole paragraph, repeat the noun: "This shows" becomes "This drop shows".
- **No metaphor standing in for a measurement:** "raises the odds", not "pays", "lifts" or "flattens", unless that word is the measured quantity. A figure of speech must survive being read literally; "a backbone that fuels the landscape" does not.
- **Match the word to what was measured.** A broader word overstates ("grows" for "concentrates"). Say "significant" or "passes correction" only when the analysis computed it.
- **Shorter when just as clear:** "cheaper plans sell more", not "a negative association between price point and conversion probability"; "use", not "utilize"; "we kept only finished runs", not "we did not include runs that did not finish".
- **One name per thing, everywhere:** text, headings, tables, figure labels and captions. Three names read as three things. When two measures cover one idea, give each its own name every time. The same estimate has the same value everywhere.

## Filler

Each of these sounds like content and adds none. The test for any phrase, sentence, column, footnote or label: what does the reader know after it that they did not know before? If nothing, cut it; don't shorten it.

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

## Cut

- **Process talk.** How the work was governed is not a finding: gates, pass rules, what was fixed in advance, preregistration, who decided what and when. Give the result and what it is compared with. Keep a process sentence only when it changes how to read a number ("we chose the recipe by looking at these test scores").
- **Edit history.** Outside a changelog, describe the thing as it is, not how it changed: "now uses a hash map instead of the old loop" becomes "uses a hash map".
- **Text only the writer needs:** file names, variables, job ids, internal section labels, notes for the next agent, provenance bookkeeping, chat leftovers ("Here is the revised version", "Let me know if…"). Move sources to a sources list; delete the rest.

## Keep

- **What each number is.** Plain is not vaguer, and rewording never changes a number. Check each plain phrase against the source. A corrected estimate is not the raw measurement: "the halves correlate 0.57, which implies 0.73 for all the data", not "the halves agree at 0.73". Put the technical name in a footnote.
- The user's own terms.
- A defined term that saves real space, defined once where it first appears.

Done when you have read it as an outsider and changed every word you would have to ask about.
