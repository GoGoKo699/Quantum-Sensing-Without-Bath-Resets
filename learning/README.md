# Learning route

This project asks how repeated measurements can estimate a frequency when every fresh probe meets the same inaccessible quantum environment. Its learning route connects the physical experiment to the proof of an attainable error bound and then to the operations needed to implement it.

The single educational anchor is **Howard M. Wiseman and Gerard J. Milburn, _Quantum Measurement and Control_ (Cambridge University Press, 2010)**. The [anchor and bridge](ANCHOR.md) identifies the relevant sections, translates the notation and assumptions, and explains the additional arguments developed in the repository. Selected sections provide foundations; reading the entire book is not a prerequisite for following this route.

## Follow the scientific story

The [30-milestone map](MILESTONES.md) has two phases:

| Phase | Milestones | What becomes understandable |
|---|---|---|
| Background and preliminaries | M01–M12 | How states, outcome operations, conditional records, open dynamics, estimation and accessible controls combine into the sensing task. |
| Narrative and innovation | M13–M30 | How the tagged recovery preserves the signal, finite stationary structure controls the correlated record, local inversion yields an estimator, and finite controls determine its resource cost. |

Each milestone states a central question, an understanding target, its dependencies, its role in the argument, and exact source pointers. Both phases move from individual ingredients to the complete setting or result. The map describes the project's conceptual structure; the linked scientific files retain the detailed proofs.

The central physical distinction runs through the route. Preparing a new probe leaves the environment's history in place. The proof handles that history through the actual outcome maps. A hidden quantum factor that is preserved perfectly cannot simultaneously reveal its state through those outcomes; the remaining stationary responses form a finite family. On a fixed local calibration interval, the observed response can therefore be converted into a frequency estimate even when its sector is unknown.

## Read at the level you need

- For the complete statement and resource assumptions, start with [Model and results](../science/model_and_results.md).
- For the physical mechanism, follow [Control and resources](../science/control_and_resources.md) alongside the relevant anchor sections.
- For the statistical argument, follow [Finite-memory statistics](../science/finite_memory_statistics.md), using M18–M24 to connect its structural and estimation steps.
- For concrete memory effects, study the [unitary and dissipative examples](../science/examples.md) and their [verification guide](../verification/README.md).
- For the limit of local calibration, read the [global ambiguity example](../science/global_ambiguity.md).

The conclusion retains its physical assumptions: the joint generator is known, the unknown signal acts only on the probe, the calibration interval is local, and the general recovery construction uses ideal controls whose sufficient count grows cubically with the record length. Models already in the required logical form have a fixed-cadence route. These distinctions are part of understanding the result.

[Return to the repository overview](../README.md) · [Scientific reading map](../science/README.md)
