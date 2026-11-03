# Scientific account

The probe is repeatedly prepared and measured, while the same inaccessible environment persists. The scientific question is whether this finite memory can force local estimation to converge more slowly than shot-noise order. Under the stated ideal-control model, the answer is no: a concrete protocol attains squared risk at most $`C/N`$. Its general finite implementation pays a growing recovery cost, and a global frequency ambiguity shows why the local calibration promise is necessary.

## Reading route

| Page | Question answered |
|---|---|
| [Model and results](model_and_results.md) | What is known, what is estimated, which operations are allowed, and what does the precision theorem guarantee? |
| [Control and resources](control_and_resources.md) | How does conditional recovery preserve the signal, and how many finite recoveries are sufficient? |
| [Finite-memory statistics](finite_memory_statistics.md) | Why can nonergodic quantum memory leave only finitely many observable stationary responses, and how does that yield a uniform finite-sample risk bound? |
| [Examples](examples.md) | How do the construction and correlations appear in a noncommuting qubit bath, including a dissipative model? |
| [Global ambiguity](global_ambiguity.md) | Why can a wide frequency interval remain unidentifiable under every accessible control strategy? |

## How the proofs fit together

The control proof supplies an effective instrument whose averaged environmental channel is exactly independent of frequency. Every stationary sector retains a nonzero phase response for a sufficiently short, fixed interrogation. The statistics proof gives a finite-sector covariance bound and constructs a nearest-arc estimator. The finite-control estimate then transfers its bounded squared risk to an actual finite sequence of recoveries.

The statistical proof is self-contained in finite dimension. It reconstructs the established stationary-algebra and absorption ingredients with explicit attribution. It includes arbitrary initial environmental states, transient support, stationary coherences, and sector probabilities that may be arbitrarily small. A Fisher-information bound is not used as a substitute for an attainable-risk proof.

For native block-diagonal probe dynamics, the exact instrument is already available and the recovery approximation is unnecessary. This gives the fixed-cadence corollary. The separate global counterexample supplies a boundary of the inference task; it does not contradict the local theorem.

See [Related work](../references/related_work.md) for the comparison to metrological QEC, quantum Markov estimation, and trajectory-mixture results. See [Verification](../verification/README.md) for the finite checks and their relationship to the analytical claims.
