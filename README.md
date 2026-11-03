# Quantum Sensing Without Bath Resets

Can a finite, inaccessible environment prevent repeated sensing from attaining shot-noise precision when the environment is never reset?

For a known finite-dimensional joint Lindblad model, with an unknown frequency acting only on the probe, an explicit protocol gives local-uniform mean-squared error

$$
\sup_{\omega\in I,\rho_E}
\mathbb E[(\widehat\omega_N-\omega)^2]
\le\frac{C}{N}.
$$

The initial environmental state is arbitrary and unknown. The environment can have several stationary sectors, noiseless quantum subsystems, and noncommuting dynamics. It is neither directly controlled nor re-prepared. The calibration interval $I$ is fixed as $N$ grows, and the exposure never exceeds $Nt$ for a fixed sensing duration $t$.

The general construction uses ideal local recoveries at an increasing rate. Their sufficient count is $O(N^3)$, plus $O(N)$ probe preparations and readouts. A model whose dynamics are already diagonal on the accessible logical qubit needs no intermediate recovery and permits a fixed prepare-and-measure cadence.

## Results and their scope

| Result | Operational consequence | Essential scope |
|---|---|---|
| [General local precision theorem](science/model_and_results.md#3-general-local-precision-theorem) | Squared risk at most $C/N$ without an environmental reset or equilibration assumption | Known finite joint Lindblad model; probe-only signal; ideal controls; fixed local interval |
| [Finite recovery implementation](science/control_and_resources.md#5-a-uniform-finite-recovery-bound) | The complete correlated record is approximated accurately enough to preserve the risk bound | Sufficient $O(N^3)$ recovery/reset uses and $O(N^2)$ recovery rate |
| [Native dephasing corollary](science/model_and_results.md#4-a-fixed-cadence-subclass) | Fixed-cadence preparation and quadrature readout suffice | Logical diagonality; environmental blocks can be noncommuting |
| [Global ambiguity](science/global_ambiguity.md) | Some wide intervals have a positive risk floor at every exposure | A conserved hidden frequency shift; the obstruction holds even with a known bath state |

The precision statement is an attainable upper bound. It does not assert that shot-noise order is optimal in every model, or that the general protocol has fixed hardware throughput.

## How the mechanism works

A two-state ancillary tag preserves the probe signal while recovery restricts the effective logical noise to dephasing. The averaged hidden-environment transition then becomes exactly independent of the unknown frequency. Its stationary quantum degrees of freedom that are perfectly preserved cannot be revealed by any compatible measurement outcome. Only finitely many stationary response curves remain visible.

Each curve carries a nonzero copy of the same signal phase. A local calibration interval separates the curves, and projecting the empirical complex quadrature mean onto their union gives an explicit estimator. Harmonic absorption effects control its variance for the actual correlated record, including initial transients and coherences.

The channel structure and Zeno control principles are inherited mathematical ingredients. [Related work](references/related_work.md) credits them and explains the distinction from the general prepare-and-measure conjecture of Mann, Cao, Laflamme and Zhou.

## Read the science

Start with the [scientific overview](science/README.md), or follow the proof in this order:

1. [Model, exact theorems, resources, and physical interpretation](science/model_and_results.md).
2. [Conditional recovery, effective generator, and finite-control bound](science/control_and_resources.md).
3. [Stationary algebra, absorption effects, finite-sample variance, and estimator](science/finite_memory_statistics.md).
4. [Noncommuting examples and numerical checks](science/examples.md).
5. [The global identifiability obstruction](science/global_ambiguity.md).

The [related-work account](references/related_work.md) and [bibliography](references/references.bib) identify the sources and the limits of the comparison.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) describes the deterministic algebra and moment checks, seeded trajectory diagnostics, expected outputs, and their limits. The simulations retain the conditional bath state between probe observations. They do not reset it to create independent samples.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
