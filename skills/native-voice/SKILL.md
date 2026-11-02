---
name: native-voice
description: Rewrites stiff, machine-sounding text the way a blunt, fluent native researcher would, and cuts long headings, titles, captions and figure labels down to size. Use on any draft an LLM wrote or edited (papers, reports, READMEs, slides, figures) before a person sees it, and whenever someone asks whether a sentence "sounds human", calls text stilted, wordy, AI-sounding or slop, or asks to tighten titles, captions or figure text.
---

# Native voice

The test for each sentence: would a good native-speaking researcher, or a blunt PI marking up a student draft, write it this way? If they would say it shorter or more directly, rewrite it. `plain-words` covers word choice and the full list of AI tells; this skill is the read-aloud pass that catches what a checklist misses.

## What to fix

- **Roundabout claims.** Say what the thing does, with the subject doing it. "PTM-Prot embeddings are better inputs for PTM-site probes than ESM-C embeddings" becomes "PTM-Prot's embeddings predict PTM sites better than ESM-C's."
- **Translated-sounding constructions:** nominalizations ("performs the ranking of" → "ranks"), "it is X that", "the fact that", noun stacks, a clause hung off the end to carry a second claim. Split or cut.
- **Committee phrasing:** "is on par with" where "matches" is true; "suits users with labeled sites" where "with labeled sites, use the probe" is meant; "it should be noted that", "serves to", "in order to".
- **Length that carries nothing.** Headings and titles state the point in a few words; drop the method, the subset and the caveats they repeat from the text below. Captions say how to read the figure, not what the axes, legend or panel titles already show. A figure title that repeats its axis label goes.
- **One name per thing** across text, headings, captions and figure labels; a new short name in a heading reads as a new thing.

Direct is not casual. Keep the register and the field's standard terms: no idioms ("in hand", "the bottom line"), no "you" in a paper, no slang swapped in for stiffness.

Keep every number, its comparison, and any limit that changes what the reader believes. Shorter must not mean vaguer or stronger than the evidence: "matches" only for a difference whose interval includes zero; "beats" only for a clear one.

## How

Read the piece aloud in your head, opening sentences and headings first, since skimmers read only those. For each line that a fluent writer would not write, give the rewrite. When asked to review, show a short before/after table of the worst cases; when asked to edit, edit, then check that no number, citation or reference was lost.
