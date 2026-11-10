---
name: native-voice
description: Rewrites stiff, machine-sounding text the way a blunt, fluent native researcher would, and cuts long headings, titles, captions and figure labels down to size. Use on any draft an LLM wrote or edited (papers, reports, READMEs, slides, figures) before a person sees it, and whenever someone asks whether a sentence "sounds human", calls text stilted, wordy, AI-sounding or slop, asks to de-slop or humanize it, or asks to tighten titles, captions or figure text.
---

# Native voice

The test for each sentence: would a good native-speaking researcher, or a blunt PI marking up a student draft, write it this way? If they would say it shorter or more directly, rewrite it. `plain-words` holds the rules; this skill is the read-aloud pass that catches what a checklist misses.

## What to fix

- **Roundabout claims.** The sentence is correct, but nobody would say it: the actor is not the subject, or the action sits in a noun. "PTM-Prot embeddings are better inputs for PTM-site probes than ESM-C embeddings" becomes "PTM-Prot's embeddings predict PTM sites better than ESM-C's." The same goes for "performs the ranking of" (ranks), "it is X that", "the fact that", and a clause hung off the end to carry a second claim.
- **Committee phrasing:** "is on par with" where "matches" is true; "suits users with labeled sites" where "with labeled sites, use the probe" is meant; "it should be noted that", "serves to", "in order to"; "stands as", "serves as" or "boasts" for "is" or "has".
- **Words that don't go together.** A phrase no one in the field has said aloud ("benefit landscape", "improvement trajectory", "compute resource" for a GPU). Say what the thing is.
- **Length that carries nothing.** Headings and titles state the point in a few words; drop the method, the subset and the caveats they repeat from the text below. Captions say how to read the figure, not what the axes, legend or panel titles already show. A figure title that repeats its axis label goes. A shortened heading or label keeps the name the text uses.

Blunt and colloquial is fine, and usually better: contractions, "you", short plain verbs. Only a paper needs the formal register, and even there the plain verb wins. Keep the field's standard terms, and skip idioms a non-native reader may not know ("in hand", "moves the needle").

Keep every number, its comparison, and any limit that changes what the reader believes. Shorter must not mean vaguer or stronger than the evidence: "matches" only for a difference whose interval includes zero; "beats" only for a clear one.

## How

Read the piece aloud in your head, opening sentences and headings first, since skimmers read only those. For each line that a fluent writer would not write, give the rewrite. When asked to review, show a short before/after table of the worst cases; when asked to edit, edit, then check that no number, citation or reference was lost.

## Removing AI tells, when asked

When the user asks to de-slop or humanize a text, or says it must not read as machine-written, apply the rules above and `plain-words` first, then go through [`references/ai-tells.md`](references/ai-tells.md). Never trade clarity for a tell.
