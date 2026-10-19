---
name: results-page
description: Turn a set of finished, verified analyses into one self-contained results page for a cold reader (a PI deciding whether to invest).
disable-model-invocation: true
---

The reader is **cold**: they know the field, not the project, and decide from this page alone. Every step serves them.

## Steps

1. **Catalogue.** Have a subagent list every finding across the analyses (and earlier ones the current draft dropped). For each: one plain sentence, the key number with its comparison and interval, the cohort, the source file, its status (registered / exploratory / withdrawn), and whether the draft has it and, if not, why. Done when every analysis on disk is accounted for as main, supplement or dropped-with-reason, and withdrawn results are excluded.
2. **Facts.** Have a subagent collect the data, model, training and test-set facts the page needs, each with its source; anything it cannot trace is marked unverified and stays off the page. Done when every number in the data and model sections has a source.
3. **Draft in pitch order** (see the `finding-unknowns:pitch-packager` skill):
   - bottom line (what we made / learned / why it is worth more work);
   - a worked example figure, chosen by a stated rule, with the rule and the hit rate in the caption;
   - what is new (one claim per item);
   - what was tested in advance versus explored;
   - the problem and the bet;
   - what we built (diagram, data, models);
   - how we tested (every baseline, readout and measure defined in tables, with chance levels);
   - findings grouped in parts, each heading a claim;
   - uses and limits;
   - benchmarks, with pending cells left blank;
   - what an expert will ask;
   - departures from the plan;
   - what we do not claim;
   - what exists and what it cost;
   - next steps and a recommendation;
   - glossary.
   
   Done when every catalogued main finding sits in a section.
4. **Figures.** One script draws every figure from the results files and writes every plotted value with its source to a numbers file (see `tufte-data-viz`). A figure stays only if a sentence cannot say it. Done when the script reruns cleanly and every figure has a caption whose first sentence is the finding.
5. **Verify.** Run two independent subagents on the draft:
   - a **number check**: every number and causal word against its source, flagging overstatement;
   - a **cold-reader audit**: every term listed with where it is first used and where it is defined, plus sentences that stumble and what a PI would still miss.
   
   Apply every item or state why not. Repeat until both return only nitpicks.
6. **Publish** the page, commit its source with the figure script, and report the link, what changed, and anything left unverified.

## Rules

- Define each term, acronym, model and dataset in plain words where it first appears, including in the opening box, which comes before the definitions.
- Say plainly when the main hypothesis failed.
- Prose follows `writing-for-readers` and `plain-words`.
