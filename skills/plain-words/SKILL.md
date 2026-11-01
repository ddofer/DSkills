---
name: plain-words
description: Plain words, one idea per sentence, no stacked qualifiers, hedges or AI slop. Use for any text a person will read, when asked to make text plainer, de-jargoned, humanized, less hedged or less AI-sounding, or to answer "what does X mean?".
---

# Plain words

Write for a smart colleague who wasn't in the project. Use words they already know, or define a word once, in plain words, where it first appears. This skill covers words and sentences; for what to say and in what order, see `writing-for-readers`. To clean up a whole existing draft, run `writing-for-readers/references/editing-pass.md` with this skill as its checklist.

## Rules

- **One idea per sentence.** Judge by meaning, not punctuation. Split where the reader would have to hold two claims at once; keep a tight pair together ("X rises while Y stays flat"). Prefer the active voice: "we compared", "users finish".
- **No telescoping.** Don't make the reader hold a growing chain of qualifiers before the point arrives: noun and hyphen stacks ("a past-win-rate-plus-text recommender"), "which… where… that…" chains, brackets inside or beside brackets. Name the thing, then say what happened to it. Give each qualifier its own sentence, or drop it if the reader doesn't need it.
  - Before: "The redesigned flow's Q3 mobile returning-user median checkout time fell 12%."
  - After: "We looked at returning customers on phones, July to September. With the new checkout, half of them finished in a time 12% shorter than before."
- **Say it the ordinary way.** Use what someone outside the project would call it, or the field's standard term ("odds ratio", "95% interval"), never one you invented. Name a method or baseline by what it is, not by a nickname.
- **No metaphor standing in for a measurement:** "raises the odds", not "pays", "lifts" or "flattens", unless that word is the measured quantity.
- **Match the word to what was measured.** A broader word overstates ("grows" for "concentrates"). Say "significant" or "passes correction" only when the analysis computed it.
- **Shorter when just as clear:** "edgier answers win more", not "a positive association between transgression intensity and selection probability"; "use", not "utilize".
- **One name per thing, everywhere:** text, tables, figure labels and captions. Three names read as three things. When two measures cover one idea, give each its own name every time. The same estimate has the same value everywhere.

## AI slop

- **Hedges:** "it seems possible", "to our knowledge", "slightly", "about", "close to", repeated disclaimers. Next to a number, let the number say it: "moves slightly away" becomes "moves from +0.31 to +0.28"; "is not clear (−3.8; −8.7 to 1.0)" becomes "is −3.8 points (−8.7 to +1.0)". Keep "about" on a rounded number when the source has no exact one. A null stated once in words ("no clear effect") is a finding, not a hedge.
- **Defensive setups.** Start with the action: "To check that X does not carry Y, we added Z" becomes "We added Z". Cut asides that answer an objection nobody raised ("so this cell is not a test"). Keep the purpose of a control when the reader needs it to read the result.
- **Announce, then say.** "Removing them is expected to lower the estimate. It lowers it to 1.2" becomes "Removing them lowers the estimate to 1.2". Same for colon reveals ("The key finding is clear: …") and "notably", "importantly", "crucially".
- **Slogans and fragments:** "Same data. Different questions." Write a plain sentence.
- **Rhythm standing in for content.** A contrast nobody raised ("not X, but Y" when no one claimed X), a list padded to three, a rhetorical question before the answer, a paragraph opened with "Moreover", "Furthermore", "Overall" or "In conclusion". Each sounds like an argument without adding one. Say the claim; let the order of sentences carry the connection.
- **Buzzwords where an ordinary word exists:** "leverage", "robust", "nuanced", "landscape", "delve", "showcase", "key" as an adjective. Use the ordinary word or the measured quantity.
- **Orphaned "also", "further", "another"** left after an edit removed what they pointed back to.
- **Em dashes in prose.** Use a comma or a new sentence.

## Cut

- **Coined labels** ("the dial", "end fifths", "main set"). Replace each with what it measures.
- **Text only the writer needs:** file names, variables, job ids, internal section labels, notes for the next agent, provenance bookkeeping. Move sources to a sources list; delete the rest.
- **Pet terms, found by counting.** In a long piece, list the most frequent 1–3-word phrases (lowercase, plurals folded, stop words dropped). Rename each one a reader in the field wouldn't use, everywhere at once.
- **Labels seeded by notes.** Project notes, memory and glossaries spread coined labels into later writing. When you replace one, fix it at the source too, and list the old name as one to avoid.

## Keep

- **What each number is.** Plain is not vaguer, and rewording never changes a number. Check each plain phrase against the source. A corrected estimate is not the raw measurement: "the halves correlate 0.57, which implies 0.73 for all the data", not "the halves agree at 0.73". Put the technical name in a footnote.
- The user's own terms.
- A defined term that saves real space, defined once where it first appears.

Done when you have read it as an outsider and changed every word you would have to ask about.
