# Reproducing the scientific checks

The analytical proofs establish the general local-uniform risk bound and the finite-control resource estimate. The calculations here test the physical instrument, independently assembled generators, exact finite-record moments, and the behavior of explicit examples. They do not certify the theorem for all dimensions or replace a diamond-norm proof by a numerical matrix norm.

## Run the complete suite

The recorded run uses Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

This runs all deterministic assertions and the seeded trajectory diagnostics, writing:

- [`results/sensing_checks.json`](../results/sensing_checks.json).
- [`results/control_checks.json`](../results/control_checks.json).

The complete run took approximately six seconds in the checked environment. Runtime depends on the machine and numerical libraries. Small floating-point changes across platforms are expected; the deterministic comparisons use tolerances and independent constructions.

To run every deterministic assertion without trajectory sampling:

```bash
python3 verification/run_all.py --skip-monte-carlo
```

The quick command replaces `results/sensing_checks.json` with a deterministic-only report. To retain the committed full report, run an individual program with a separate output path:

```bash
python3 code/verify_sensing.py --skip-monte-carlo --output /tmp/sensing_checks.json
python3 verification/check_control_normal_form.py --output /tmp/control_checks.json
```

## What is checked

| Check | Independent comparison or expected behavior | Scientific purpose |
|---|---|---|
| Native unitary instrument | Kraus outcome maps versus full joint evolution, probe projection and partial trace | Detects basis, setting-probability and quadrature-sign mistakes |
| Dissipative instrument | Block evolution versus an independently assembled full joint Lindblad superoperator | Checks the native fixed-cadence model with noncommuting bath operators |
| Complete record moments | Operator moment recursion versus enumeration of every short outcome word | Verifies that correlations and conditional bath evolution are retained |
| Stationary covariance | Finite-length moments versus a covariance-resolvent calculation | Demonstrates the measurable memory correction to the independent-sample variance |
| Local estimator | Exact noiseless arc inversion and seeded trajectories with the bath carried between rounds | Checks implementation of the stated estimator; sampling is diagnostic |
| Conserved sectors | Ordinary variance floor versus sector-centered second moments; coherent versus dephased sector starts | Distinguishes persistent sector uncertainty from within-sector fluctuations |
| Noiseless factor | Every enumerated record for two orthogonal Bell states with the same noisy-factor marginal | Checks output invisibility of a preserved quantum factor |
| Transient absorption | Harmonic effects and weighted moments versus an analytic geometric-transient formula | Checks the treatment of an entirely transient initial state without dividing by sector weights |
| Generic recovery | Direct full-system generator/recovery/decoding versus the derived GKLS blocks | Checks the control normal form beyond native dephasing |
| Three-level probe recovery | Independently chosen branch complement bases, code fixation and the incorrect common-basis countercheck | Tests the basis dependence that a qubit-only example could conceal |

The programs use fixed seeds. The estimator receives the classical record and model calibration; it is not supplied the unknown bath state or conserved-sector label. Distinct simulated runs are initialized separately to estimate ensemble risk, while the environment remains unreset throughout each run.

## Representative checked values

The native unitary model has stationary coherence $c=0.9471265187303647$. Its actual asymptotic complex-score variance is $3.372015250314819$, whereas treating observations as independent gives $3.1029513575177$. The dissipative variant has coherence $0.9498276886303852$ and actual variance $3.1486084591514087$.

The generic qubit recovery generator agrees with the independently assembled compressed generator to approximately $1.1\times10^{-16}$. The three-level probe calculation has generator discrepancy approximately $2.8\times10^{-16}$ and recovery-completeness discrepancy approximately $4.2\times10^{-16}$. These numbers are numerical residuals for the specified models.

The seeded unitary example gives $N\times\mathrm{MSE}\approx15.30$ at $N=8192$, consistent with the independently computed local variance scale. Monte Carlo rows have empirical standard errors and are never used as pass/fail thresholds. They demonstrate the behavior of the implementation; the [finite-memory proof](../science/finite_memory_statistics.md) establishes the general risk bound.

## Norm and scope distinctions

The finite-recovery reports include superoperator Frobenius or induced Hilbert–Schmidt errors and normalized Choi trace distances. None is labeled a diamond norm. The [control proof](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound) establishes the reference-stable diamond bound analytically, then controls the full retained record and bounded estimation loss.

The transient example is an abstract finite instrument. It tests the statistics argument and is not presented as another continuous-time Lindblad realization. Finite numerical checks do not establish uniform constants over all bath dimensions, an optimal recovery count, global identifiability, or noisy-control performance.
