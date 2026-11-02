# Editing pass

An editing, proofreading or cleanup pass on an existing paper, report, page or summary. For a caption, message or short summary, skip the readers and apply `SKILL.md` and `plain-words` directly.

## Ground rules

- **Clear wins only.** Change text where the change plainly helps the reader. If unsure, leave it.
- **Edit depth follows the request.** "Proofread" or "light edits" means small in-place fixes; "rewrite" or "make it better" allows rewording. When the scope is unclear, edit in place.
- **Never change a number or the substance of a claim.** Fix generated text and figures in their generator, not in the output.
- **Keep the author's decisions.** Build a do-not-touch list from the user's instructions and memory (venue, framing, lead finding, sections they kept on purpose) and don't re-argue it.
- **On a minor point, cut an inaccurate clause rather than add a long correction.** A material error goes to the author in your report.
- **Add no hedge, caveat or warning while fixing something else.** When a claim is wrong, narrow it and list the change in your report.

## Steps

1. **Readers.** For a proofread or light edit, use one reader (the cutter) or none. For a rewrite or a paper, brief up to five fresh agents, one role each:
   - a cold reader (the PI or target reader), told nothing about the conclusions: restate each headline finding with its comparison and conditions from the main text alone;
   - a co-author: what is wrong, missing or unclear;
   - an area chair or editor: novelty, story, and the likely verdict, without nitpicks;
   - a cutter: dead ink, repeats, AI slop, coined terms;
   - a number checker: every number and method statement against its source (results file, code).

   Give every reader except the cold reader the do-not-touch list, so they don't propose undoing it. Ask them to judge findings as analyses (known mechanism? artifact? does it change a conclusion?), not only whether a number traces.
2. **Readers propose exact replacements:** an `old` string copied verbatim from the source file, a `new` string, and one line on why. A cut names the duplicate or reason.
3. **One editor per file merges.** Combine overlapping proposals. Reject any that deletes a finding, changes a number, removes a definition the text still needs, adds a hedge, or undoes a do-not-touch item.
4. **Integrate.** Save the current built text first (for example `pdftotext main.pdf old.txt`). Apply the accepted replacements, regenerate figures and tables from their scripts, rebuild.
5. **Check.** Run `python3 <this skill's folder>/scripts/check_edit.py old.txt new.txt [--reject words.txt]` on the built text before and after. The rejected-word list is the project's `.claude/rejected-words.txt`, if it keeps one. Check venue limits (abstract words, pages). Look at every figure at the size it will be read (paper column, page width) for clipped or overlapping labels and illegible text.
6. **Report** the changes by file, the material corrections, and anything left for the author.

## Done when

- every lost number in the check output is a deliberate cut, and every new number traces to a source;
- every sentence over 40 words is split, or keeping it is the clearer choice;
- every doubled word, `??` and rejected-word hit is fixed or is correct as written;
- venue limits are met and every figure is legible at its printed size;
- the cold reader's restatement of each headline matches the paper's, with its comparison and conditions;
- every number-checker discrepancy is fixed or reported to the author.
