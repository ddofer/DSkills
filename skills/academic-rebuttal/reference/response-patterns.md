# Response patterns

Fill every `[...]` from supplied evidence or leave it as a visible placeholder.

## Opening summary

> We thank the reviewers for their careful feedback. They recognize [strength 1] (R1, R2) and [strength 2] (R3). The main concerns are (1) [concern], (2) [concern] and (3) [concern]. We address these below with new evidence and concrete revisions.

For a critical review set:

> While the reviewers raise important concerns about [central issue], they also recognize [merit 1] and [merit 2]. We clarify the intended scope, provide the requested evidence where feasible, and list the revisions below.

## Major response

> **C1. Performance under matched compute (R1, R3)**
>
> **Concern.** [Faithful one-sentence paraphrase.]
>
> **Yes, the method remains stronger under matched compute.** With the same data, backbone, tuning budget and FLOPs, it reaches [X ± s] versus [Y ± t] for the strongest baseline over [N] seeds. We will add this to Table 2, put per-seed results in Appendix C, and change "consistently superior" to "superior in the evaluated matched-compute settings."

## Minor comments

> **Minor comments.** We will define [term] at first use (R1), cite [work] (R2), correct Eq. (5) (R2) and expand the implementation details in Appendix D (R3).

## Correcting a misunderstanding

> **The method does not require [assumption]; it requires only [actual assumption].** Section [N] states this, but our presentation may have obscured the distinction. We will revise the paragraph and add [example or derivation].

## Acknowledging a valid limitation

> **We agree that the current evidence does not establish [broad claim].** It supports the narrower claim that [claim] under [conditions]. We will narrow the abstract and conclusion and add this limitation to Section [N].

## Reporting a completed experiment

> **We ran the requested [comparison / ablation / robustness test].** Under matched [data / compute / tuning], our method obtains [result] versus [baseline] over [N] runs. This supports [specific claim]. We will add the setup and result to [location].

## Experiment that cannot be finished reliably

> We agree this experiment would be informative. Doing it reliably requires [reason], and we do not want to report an under-validated result. The current evidence supports [narrow claim]; we will state this scope and add the experiment to the revision plan.

## Novelty

First build a delta table:

| Prior work | Capability or assumption | This paper's difference | Why it matters |
|---|---|---|---|

Then:

> The contribution is not [common component] alone. It is (i) [new formulation], (ii) [new capability or guarantee] and (iii) [new finding]. Work A differs in [distinction]; Work B assumes [assumption].

Don't argue novelty only from an unseen combination of known parts.

## Missing baseline or unfair comparison

> We agree the comparison conditions should match. All methods now use the same [split], [budget], [backbone] and [selection protocol]. Under this protocol, [result]. We will state these controls explicitly.

## Statistical reliability

> We report [metric] over [N] independent runs as mean ± standard deviation, with [interval or test]. The improvement over [baseline] is [value] ([uncertainty]).

Don't claim significance without a valid test.

## Score-text mismatch and process problems

Keep the public response technical. Use a confidential chair note only when the venue offers one: quote only the necessary text, describe the issue factually, cite the venue guideline, explain why it affects fair evaluation, and don't speculate about intent or identity.

> We respectfully ask the chair to consider whether the score matches the review text, which recognizes [positive assessment] and identifies no [fatal issue].
