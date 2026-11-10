# Forms

What each kind of reader needs first, and what to leave out. The rules in `SKILL.md` still apply. For a paper see `paper.md`; for a rebuttal use `academic-rebuttal`.

## README

The reader asks, in this order: what is this, is it for me, how do I run it?

- Open with what the thing does and who it is for, in a sentence or two a newcomer understands.
- Next, the shortest command that works, ready to paste, and what it prints or writes.
- Then what the user needs before that command works (install, data, access), the inputs and outputs, and the options people really use.
- Research code adds the commands that train and evaluate, where the weights are, and a results table with the exact command behind each row.
- Steps are numbered and start with a verb. Put the condition before the action ("On the login node, run…"). Examples use real names, not `foo`.
- Then the limits and traps a user will hit.
- Leave out the history, the design rationale, the tour of the code, how each check works inside and anything `--help` prints. Link to them. A small tool's README fits one screen.
- Done when a newcomer could run the first command from this page alone, and you have run every command on it.

## Results report or artifact

The reader decides something from this page: whether to believe the result and what to do next.

- Open with the bottom line in two or three sentences: what we learned, how sure we are, what we recommend.
- Then, in a long report, the findings as a numbered list, each a claim with its number and comparison.
- Then the evidence, one section per finding. The heading is the claim; one figure or table carries it, and the prose gives only the number a reader would quote. Define a term in a clause where it is first used, not in a glossary ahead of the result.
- Then what the data are, how things were measured, the limits that change what to believe, next steps and, in a long report, a short glossary.
- Leave out the order things were done in, dead ends (unless knowing one saves the reader the same trip), checks that changed nothing, and file paths. Sources go in a list at the end.
- A section of a report is short: its claim, the evidence, what it means.

## Review of a paper, proposal, plan or pull request

An editor or area chair decides from it, and the author acts on it.

- Open with what the work claims, in your own words, each claim tied to where the work states it. Then your verdict and the one or two reasons that decide it.
- Then the major concerns, most serious first, and few: a long unranked list buries the one that decides. Each says what is wrong, where (section, figure, line), why it matters for the claim, and what would settle it. "Not novel" names the earlier work and the overlap.
- Before calling anything missing, search the text, figures, tables, appendix and supplement. Check every citation and every number you quote.
- Ask for an experiment only when a stated claim depends on it, and name the claim. Mark the rest optional. Say what you could not assess.
- Then minor points as a short list that does not affect the verdict.
- Judge the claims against the evidence shown. Don't ask for a different paper. A limit of scope the authors state is not a fault; a flaw that undoes the central claim is one, stated or not. A score follows from the text: every low score has a stated major fault.
- Praise only what is specifically good. A bold label on each of several parallel points helps the reader here.
- Check the venue's rule on LLM use before drafting. Many require that the assessment is the reviewer's own and that LLM help is disclosed; then the agent edits a person's assessment and does not write one.

## Status note, email, handoff, pull-request text, reply at the end of a task

The reader was not watching. They want the outcome, then what they must do. If they were in the conversation, skip what they already know: give the answer, then only the facts they lack.

- First sentence: the outcome (done, partly done, blocked) and the one result that matters.
- Then what the reader must decide or do, each with the options, how hard each is, and your recommendation.
- Then what changed, how it was checked, what was not checked, and what is left. Every "done" names its check.
- Aim for a minute's reading, about 150 words. The full account and its tables stay in the notes. Give a path or link the reader can open; don't append them. Never cut to fit a failed or skipped check, a decision the reader owes, or a risk.
- Leave out the story of how you got there, the restated request and closing offers. Use only names the reader already has: no labels or run names coined during the work.
- Paths, commands and job ids the reader will need go in one block at the end.

## Slides

- One message per slide. The title is that message as a sentence; the body is its evidence, usually one figure.
- Cut whatever you will not talk about.
