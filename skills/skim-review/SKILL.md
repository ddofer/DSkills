---
name: skim-review
description: Final check of a paper or report. Finds strong findings that fell out of the text over rounds of editing, and findings a skimming reviewer would miss. Manual only; start with /skim-review <paper path> [--full].
disable-model-invocation: true
argument-hint: "<paper or report path> [--full]"
---

Two things go wrong late in a paper. Findings get lost: a result from an earlier session never made it in, or an edit cut it. Findings get buried: they are in the text but not where a skimming reader looks. Experienced readers skim first: title, abstract, headings, figures, tables and captions, the first and last paragraph of each section, the conclusion. If the reasons to accept the paper are not in that view, most reviewers never see them.

Target: $ARGUMENTS

## Effort

- **Quick** (default): you do steps 1 to 3 yourself, in one pass. For a short report or a late-stage check.
- **Full** (`--full`, or a paper going to a venue): steps 1 to 3 each go to a fresh subagent that sees only its own input, so it cannot fill gaps from memory. Tell each one only where to look, not what you expect it to find.

## Steps

1. **Findings on disk.** From the results, not the paper: result files, figure scripts, analysis notes, reports, memory. List the strongest findings: new, unexpected, large, decision-changing, or the kind a reviewer would quote. For each: one plain sentence, the key number with its comparison, the source file. Include results that were done after the paper's last big revision.
2. **Skim view.** Run `python3 <this skill's folder>/scripts/skim_view.py <paper>` to extract the skim view (title, abstract, headings, captions, first and last paragraph of each section, conclusion). From that view alone, write down: what the paper found, the two or three reasons to accept it, and what each figure and table shows.
3. **Full read.** From the whole paper: every finding it states, with its number.
4. **Compare** the three lists in Claude:
   - in 1, not in 3: **lost**. Report it with its source. Add it only if the number is in the results; never from memory.
   - in 3, not in 2: **buried**. Move it to where a skimmer looks: the abstract, the contributions, the first or last paragraph of its section. In a report, also a heading that states the claim and the caption's first sentence; in a paper, headings stay short nouns and captions say what is shown (`writing-for-readers/references/paper.md`).
   - in 2, not in 3 or 1: **unsupported**. The skim view promises what the text does not deliver. Narrow it.
   - reasons to accept unclear from 2: rewrite the abstract's last sentence, the introduction's contributions, or the conclusion so they carry them.
5. **Edit.** Propose each change as an exact `old` → `new` replacement with one line on why. Apply them if the user asked for edits; otherwise report them. Change no number. A lost finding that needs a new number goes to the author as a question, not into the text.
6. **Verdict.** End with: is the paper ready? List what was lost, buried or unsupported and what was done about each. Say plainly if a strong finding still has no home. If the prose also needs cleaning (slop, dead ink, coined terms), run `writing-for-readers/references/editing-pass.md` next; this skill does not do it.

Rank findings by what a reader in the field would care about, not by what took the most work. Do not add or extend analyses here.
