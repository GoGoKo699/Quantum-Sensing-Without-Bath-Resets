# Related work and attribution

The scientific claim is the [controlled local precision theorem](../science/model_and_results.md): a known finite hidden-environment Lindblad model with a probe-only nontrivial signal admits an explicit estimator with uniform local mean-squared error $O(1/N)$, without environmental reset or an ergodicity assumption. The general implementation uses a sufficient $O(N^3)$ ideal recovery count. A native logical-dephasing subclass works at a fixed prepare/readout cadence.

The proof combines established channel structure and metrological control ideas. Its contribution depends on the guarantee that every output-visible stationary sector retains a signal response, together with a local inversion that handles the unknown realized sector. The channel decomposition, absorption construction, and Zeno principle have prior sources.

## Educational foundation

Howard M. Wiseman and Gerard J. Milburn, [*Quantum Measurement and Control*](https://doi.org/10.1017/CBO9780511813948), Cambridge University Press (2010), is the single educational anchor. Its measurement, estimation, open-system and control topics support the [learning bridge](../learning/ANCHOR.md). The specialized structural results and this project's particular risk and resource proofs are identified separately below.

## Closest metrology result

**[MCLZ25]** Zachary Mann, Ningping Cao, Raymond Laflamme, and Sisi Zhou, [*Quantum Error-Corrected Non-Markovian Metrology*](https://doi.org/10.1103/wfyl-wtz3), PRX Quantum **6**, 030321 (2025); [arXiv:2503.07745v2](https://arxiv.org/html/2503.07745v2).

Section IV studies repeated sensing without resetting the hidden environment. Theorem 10 proves SQL achievability for an interaction diagonal in a common environmental basis, using a logical-dephasing recovery. The general dissipative prepare-and-measure claim is left as a conjecture, with numerical evidence. We inherit the finite joint-Lindblad setting and the idea of imposing logical diagonality. The [conditional recovery](../science/control_and_resources.md#4-relation-to-the-earlier-dephasing-reduction) used here is derived explicitly and differs in how it treats leakage coherences.

Our theorem allows noncommuting environmental blocks and arbitrary recurrent sectors, and supplies actual local-uniform MSE. It permits intermediate recovery, so it does not settle their conjecture for plain prepare-and-measure experiments. The fixed-cadence corollary is restricted to models already having the required logical block structure.

## Quantum Markov estimation

**[GK15]** Mădălin Guţă and Jukka Kiukas, [*Equivalence classes and local asymptotic normality in system identification for quantum Markov chains*](https://doi.org/10.1007/s00220-014-2253-0), Communications in Mathematical Physics **335** (2015); [primary manuscript](https://arxiv.org/pdf/1402.3535).

This work characterizes stationary-output identifiability and local asymptotic normality for ergodic quantum Markov chains. The phase and internal-unitary gauge identifies dynamical directions with no output information. It supplies the appropriate conceptual comparison for an asymptotic information rate. The present protocol instead establishes an observable signal in every stationary sector and gives a particular classical estimator, including reducible hidden dynamics and arbitrary initial states.

**[GKG26]** Federico Girotti, Jukka Kiukas, and Mădălin Guţă, [*Asymptotic statistical theory of irreducible quantum Markov chains*](https://arxiv.org/html/2603.20761v1), arXiv:2603.20761v1 (2026).

This extends the primitive-chain theory to irreducible periodic dynamics, with an orbifold of identifiable parameters and Gaussian-mixture limit models. Our proof does not claim to replace or generalize that full asymptotic theory. It uses a parameter-independent averaged instrument, a finite-sector nonvanishing condition supplied by the control construction, and a direct second-moment argument. The result needed here is an attainable risk bound under the accessible measurement, rather than a complete local statistical equivalence theorem.

## Stationary structure, absorption, and trajectory mixtures

| Source | Ingredient used here | Where it enters |
|---|---|---|
| **[CP16]** Carbone and Pautrat, [*Irreducible decompositions and stationary states of quantum channels*](https://arxiv.org/abs/1507.08404), Reports on Mathematical Physics **77**, 293–313 (2016) | Recurrent supports and the full stationary-state structure; see Sections 5–7. | [Statistics, Lemmas 2–4](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support). The required finite-dimensional algebra argument is proved there. |
| **[CG21]** Carbone and Girotti, [*Absorption in Invariant Domains for Semigroups of Quantum Channels*](https://doi.org/10.1007/s00023-021-01016-5), Annales Henri Poincaré **22**, 2497–2530 (2021) | Positive harmonic absorption effects and their connection to fixed points; Proposition 6 and Section 4. | [Statistics, Lemma 5](../science/finite_memory_statistics.md#3-absorption-effects-and-an-auxiliary-sector-label). |
| **[CGH22]** Carbone, Girotti, and Melchor Hernandez, [*On a Generalized Central Limit Theorem and Large Deviations for Homogeneous Open Quantum Walks*](https://doi.org/10.1007/s10955-022-02938-y), Journal of Statistical Physics **188**, 8 (2022) | Recurrent-sector output statistics and absorption-weighted record mixtures; Lemmas 4.2–4.3, Theorem 4.4, and the multiple-Kraus extension in Remark 4.6. | The auxiliary sector law and the interpretation of correlated empirical means. |

These results already explain why a finite quantum trajectory may have a mixture of asymptotic responses. The [finite-sample proof](../science/finite_memory_statistics.md#4-a-finite-sample-second-moment-bound) specializes that structure to bounded complex scores and obtains the bound needed for local estimation. It directly controls second moments, including arbitrary transient initial states and arbitrarily small sector weights. It does not infer risk convergence from a central-limit theorem alone.

## Effective control and its finite cost

**[BFNPY20]** Daniel Burgarth, Paolo Facchi, Hiromichi Nakazato, Saverio Pascazio, and Kazuya Yuasa, [*Quantum Zeno Dynamics from General Quantum Operations*](https://quantum-journal.org/papers/q-2020-07-06-289/), Quantum **4**, 289 (2020), provides the general effective-dynamics background. The [finite recovery proof](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound) uses an elementary Taylor remainder and channel telescoping for the particular idempotent recovery. The bound controls the complete correlated record, including its hidden-system output, and transfers a bounded squared-loss guarantee.

**[ST26]** Shravan Shravan and Tyler G. Thurtell, [*Heisenberg-limited metrology in the presence of non-Markovian noise with finite control rates*](https://arxiv.org/abs/2607.12913), arXiv:2607.12913 (2026), connects non-Markovian Heisenberg-limited protocols with Zeno dynamics and analyzes finite-rate measurement, active-recovery, and dynamical-decoupling constructions. The abstract establishes that finite-rate Zeno analysis in non-Markovian metrology is prior work. We make no claim of novelty for that general subject or of an optimal frequency exponent. The comparison to this preprint is limited to its primary abstract because full-text retrieval was unavailable; no detailed theorem-level exclusion is asserted.

## Nearby collision-model projects

The author's [Noise-Rate-Activated-Sensing](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/e4c8a7d4f15c3b35dda1507caf7e411502b9b100/science/microscopic_global_precision.md) and [Markovian-Resolution-Limit](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b/science/global_contact_precision.md) investigate fresh collision partners and the role of control/contact resources. Their microscopic preparation resets the noise partner for each collision. The present task reuses one finite hidden environment and retains the resulting correlations. The common resource-accounting concerns do not identify these statistical experiments.

## Scope of the comparison

The cited exact models and proof dependencies determine the comparison. This is a bounded primary-literature review through 3 November 2026, not a certification of priority. The full mathematical argument required for the claimed risk bound is included in the scientific files. The local calibration interval, the general protocol's growing recovery rate, the known-generator assumption, and the distinction from the no-intermediate-recovery conjecture remain part of the result.

Structured citation data are in [references.bib](references.bib).
