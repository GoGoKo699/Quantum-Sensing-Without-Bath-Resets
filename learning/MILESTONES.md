# Milestones: sensing with a persistent quantum environment

This map develops the question, construction, proof and limits of estimating a probe frequency while one inaccessible environment persists throughout the experiment. It has exactly 30 milestones. Each is a conceptual understanding target with a route to the authoritative scientific account.

The sole educational anchor is Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control* (Cambridge University Press, 2010), abbreviated **WM** below. Section numbers refer to that edition and were checked against the publisher's [official contents](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf); the [publisher record](https://www.cambridge.org/core/books/quantum-measurement-and-control/F78F445CD9AF00B10593405E9BAC6B9F) identifies the book. The anchor supplies measurement, estimation, open-system and control foundations. The repository supplies the particular derivations and identifies research dependencies where the argument goes beyond those foundations. References to research papers are attribution and proof pointers, not additional educational anchors.

## Structure and scope

| Phase | Milestones | Progression |
|---|---|---|
| Background and preliminaries | M01–M12 | States and individual outcomes become instruments, correlated records and open dynamics; estimation and control then combine into the precise sensing task. |
| Narrative and innovation | M13–M30 | A local recovery produces the required instrument; stationary structure, absorption and concentration produce an estimator; finite controls, examples and an impossibility result establish its physical scope. |

The 12/18 allocation reflects the project's two demands: a physical entry through measurement and control, followed by a longer argument connecting hidden quantum memory to attainable statistical risk. The endpoints of both phases integrate their preceding ingredients. The map covers the project's conceptual structure; detailed algebra and neighboring specialist topics remain in the linked scientific sources.

Dependencies refer to earlier milestone IDs. Sources distinguish **WM** foundations from the repository's **research account**. The [scientific entrypoint](../science/README.md) provides a direct route to complete statements and proofs.

## Phase I — Background and preliminaries (M01–M12)

### M01 — State descriptions when the bath is hidden

- **Central question:** What information is contained in a joint state, and what remains accessible when the environment cannot be measured?
- **Understanding target:** Distinguish the joint probe–environment state, its reduced states, and correlations; explain why local probe preparation preserves the environmental marginal.
- **Dependencies and story role:** Starting point; establishes the objects on which every later operation acts.
- **Conceptual connection:** Partial tracing turns the physical access restriction into the mathematical distinction between the controlled probe and hidden memory.
- **Sources:** WM Appendix A.1–A.2; [Model, §1 and allowed operations](../science/model_and_results.md#1-physical-model).

### M02 — An outcome has both a probability and a state update

- **Central question:** Why does specifying measurement probabilities alone leave a repeated sensing experiment incomplete?
- **Understanding target:** Distinguish an outcome effect from the operation that produces the conditional output state; relate both to a physical measurement.
- **Dependencies and story role:** M01; introduces the elementary event from which a measurement record is built.
- **Conceptual connection:** Measurement backaction on the hidden environment affects future observations even when only the probe is read out.
- **Sources:** WM §§1.3–1.4; [Statistics, §1: instrument and record probability](../science/finite_memory_statistics.md#1-instrument-and-estimator-theorem).

### M03 — From outcome operations to an averaged channel

- **Central question:** How do the recorded and ignored versions of one measurement fit into one description?
- **Understanding target:** Explain a finite instrument as completely positive outcome maps whose sum is trace preserving; distinguish its score-weighted map from its averaged channel.
- **Dependencies and story role:** M02; combines individual outcomes into the complete description of one sensing round.
- **Conceptual connection:** The protocol keeps parameter information in the score while arranging for the averaged hidden transition to be parameter independent.
- **Sources:** WM §1.4; [Statistics, §1: definitions of the instrument, channel and score map](../science/finite_memory_statistics.md#1-instrument-and-estimator-theorem).

### M04 — Conditional trajectories and correlated records

- **Central question:** What changes when the next probe meets the same environment?
- **Understanding target:** Explain how successive outcome maps form a record probability and update a conditional hidden state; distinguish that record from independent samples.
- **Dependencies and story role:** M01–M03; extends one round to an experiment with memory.
- **Conceptual connection:** Measurement-conditioned evolution supplies the physical interpretation of the channel products used later in covariance calculations.
- **Sources:** WM Chapter 4, especially §§4.1–4.2, and §6.5; [Statistics, §1: finite-record law](../science/finite_memory_statistics.md#1-instrument-and-estimator-theorem); [Examples, §1: retained memory](../science/examples.md#the-records-retain-measurable-memory).

### M05 — Joint Markov dynamics can contain probe memory

- **Central question:** How can a time-independent Lindblad equation describe an experiment whose probe observations retain history?
- **Understanding target:** Identify Hamiltonian and jump contributions on the joint system; distinguish a finite Markovian embedding from a Markovian description of the probe alone.
- **Dependencies and story role:** M01 and M04; connects the record description to continuous physical evolution between interventions.
- **Conceptual connection:** The hidden environment carries memory even though the enlarged evolution has a time-homogeneous generator.
- **Sources:** WM §3.6; [Model, §1](../science/model_and_results.md#1-physical-model); [Control, §1](../science/control_and_resources.md#1-physical-model-and-control-assumptions).

### M06 — A frequency becomes a measurable phase

- **Central question:** How can two probe levels and two quadrature measurements reveal an unknown frequency?
- **Understanding target:** Connect eigenvalue separation, interrogation duration and relative phase; explain why randomized X/Y readout supplies a complex response and why its sign convention matters.
- **Dependencies and story role:** M02, M03 and M05; identifies the elementary signal-bearing observable.
- **Conceptual connection:** The same rotating complex response survives the later recovery construction and becomes the estimator's input.
- **Sources:** WM §§2.1–2.2; [Examples, §1: physical instrument and score](../science/examples.md#1-a-native-model-with-a-noncommuting-qubit-environment).

### M07 — Precision is a property of a specified estimation task

- **Central question:** What does an attainable frequency-error guarantee require beyond a local information quantity?
- **Understanding target:** Distinguish an estimator's mean-squared error, a uniform parameter interval, and Fisher-information bounds; recognize the unknown initial bath state as a nuisance that the estimator cannot use.
- **Dependencies and story role:** M04 and M06; turns observable sensitivity into an operational inference criterion.
- **Conceptual connection:** The project proves a risk bound for a concrete estimator across a fixed local interval and every initial hidden state.
- **Sources:** WM §§2.1–2.2; [Model, §2](../science/model_and_results.md#2-estimation-task-and-resources); [Statistics, §6](../science/finite_memory_statistics.md#6-what-the-theorem-establishes).

### M08 — Accessible controls and the physical resource boundary

- **Central question:** Which interventions are available when the probe is controlled but its environment is not?
- **Understanding target:** Separate local preparation, measurement, ancillas and recovery from direct environmental access; distinguish sensing exposure from the number and duration assumptions of controls.
- **Dependencies and story role:** M01, M05 and M07; establishes the operational rules under which precision is assessed.
- **Conceptual connection:** A useful error bound must be paired with the operations and idealizations that produce it.
- **Sources:** WM §§6.3 and 6.5; [Model, §§1–2](../science/model_and_results.md#allowed-operations); [Control, §1](../science/control_and_resources.md#1-physical-model-and-control-assumptions).

### M09 — Recovery can preserve coherence without removing all noise

- **Central question:** What must a recovery preserve if a logical superposition is to remain useful for sensing?
- **Understanding target:** Distinguish preservation of the encoded state from complete noise correction; explain why an unobserved recovery record must not reveal the logical branch.
- **Dependencies and story role:** M02, M06 and M08; supplies the control principle needed by the project's tagged code.
- **Conceptual connection:** The recovery retains a nonzero signal and imposes logical diagonality while allowing substantial environmental noise to remain.
- **Sources:** WM §§7.4–7.7; [Control, §2 and physical realization](../science/control_and_resources.md#2-a-tagged-code-and-its-exact-recovery).

### M10 — Stationary states do not imply complete forgetting

- **Central question:** What can a finite channel preserve after its decaying modes disappear?
- **Understanding target:** Distinguish stationary states, transient modes and unit-modulus eigenmodes; understand why multiple stationary states prevent an assumption of one universal limiting response.
- **Dependencies and story role:** M03–M05; introduces the asymptotic channel language required for persistent memory.
- **Conceptual connection:** The proof must classify observable stationary information instead of assuming that the bath relaxes to a unique state.
- **Sources:** WM §3.11 for the state/observable pictures; research account: [Statistics, §2, Lemmas 2–3](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support); [structural attribution, CP16](../references/related_work.md#stationary-structure-absorption-and-trajectory-mixtures).

### M11 — Operational error must survive composition

- **Central question:** What approximation notion remains useful when a sensing step is embedded in a longer correlated experiment?
- **Understanding target:** Explain why an error bound must allow an untouched reference and later processing; connect channel distance to the distribution of a retained record and then to bounded loss.
- **Dependencies and story role:** M03, M04, M07 and M08; prepares the passage from an effective dynamics to finite physical controls.
- **Conceptual connection:** The diamond-norm estimate controls an implemented estimator without assuming independent rounds or continuity of Fisher information.
- **Sources:** WM §1.4 for the general operation framework; research derivation: [Control, §§5–6](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound).

### M12 — The complete sensing question

- **Central question:** Which combination of access, memory, precision and resources does this project address?
- **Understanding target:** Assemble the known generator, probe-only unknown signal, arbitrary initial bath, fixed calibration interval, hard exposure ceiling and separately counted controls into one estimation task.
- **Dependencies and story role:** M01–M11; integrates the background into the framework used by the scientific theorem.
- **Conceptual connection:** Persistent memory raises both a precision problem and an identifiability problem; the result must state which is solved under which resources.
- **Sources:** WM §§2.1–2.2 and 6.5 as the estimation/control connection; [Model, §§1–3](../science/model_and_results.md#3-general-local-precision-theorem); [Related work: closest metrology result](../references/related_work.md#closest-metrology-result).

## Phase II — Narrative and innovation (M13–M30)

### M13 — A two-state tag retains the signal

- **Central question:** Why encode two signal eigenvectors with orthogonal ancillary labels?
- **Understanding target:** Explain how the code retains their eigenvalue separation and makes compressed probe operators diagonal in the logical label.
- **Dependencies and story role:** M06, M08–M09 and M12; begins the construction with its smallest physical component.
- **Conceptual connection:** A noiseless auxiliary label converts the allowed local-control framework into a useful sensing code.
- **Sources:** WM §7.4; [Control, §2: encoding isometry](../science/control_and_resources.md#2-a-tagged-code-and-its-exact-recovery); [inherited metrological construction, MCLZ25](../references/related_work.md#closest-metrology-result).

### M14 — The exact conditional reset

- **Central question:** How can resetting the probe preserve a superposition of the tagged codewords?
- **Understanding target:** Explain the branch-dependent bases, the common recovery index, and the controlled decode–reset–encode realization; identify why a single common probe basis would fail.
- **Dependencies and story role:** M09 and M13; turns the encoding idea into a fully specified CPTP recovery.
- **Conceptual connection:** The information discarded in a reset determines which encoded coherence survives.
- **Sources:** WM §§1.4 and 7.4; [Control, §2, including physical realization](../science/control_and_resources.md#physical-realization).

### M15 — The recovery produces a legitimate effective generator

- **Central question:** What evolution remains when the same recovery is applied frequently?
- **Understanding target:** Connect the physical Hamiltonian and jump matrix elements to diagonal logical blocks; understand why the resulting generator is explicitly Lindblad rather than only a formal projection.
- **Dependencies and story role:** M05 and M14; converts the recovery into a dynamical normal form.
- **Conceptual connection:** The logical label is constrained while noncommuting environmental dynamics remain fully present.
- **Sources:** WM §§3.6 and 7.5–7.7; [Control, §3](../science/control_and_resources.md#3-exact-form-of-the-effective-generator); [effective-control attribution](../references/related_work.md#effective-control-and-its-finite-cost).

### M16 — Signal in the response, parameter independence in the bath transition

- **Central question:** How does the normal form separate the unknown phase from the averaged environmental evolution?
- **Understanding target:** Distinguish population channels from the coherence transfer map; connect random X/Y readout to the response $e^{-i\omega\Delta g t}\operatorname{Tr}\mathcal C_t(\sigma)$ and to a parameter-independent averaged channel.
- **Dependencies and story role:** M03, M06 and M15; supplies the precise instrument used by the statistics theorem.
- **Conceptual connection:** Conditional outcomes reveal the signal while their ignored sum gives one common hidden channel for every parameter value.
- **Sources:** [Control, §3: population and coherence blocks](../science/control_and_resources.md#population-and-coherence-blocks); [Statistics, §1: sensing instrument](../science/finite_memory_statistics.md#how-the-sensing-experiment-supplies-these-assumptions).

### M17 — Nonzero response and a harmless scheduling choice

- **Central question:** How can one fixed interrogation time work for every initial bath state and every stationary sector?
- **Understanding target:** Explain the uniform short-time response bound and why mixing an active round with a zero-duration skip removes nontrivial peripheral eigenvalues without resetting the bath.
- **Dependencies and story role:** M08, M10 and M16; verifies the two physical inputs needed by the general statistical argument.
- **Conceptual connection:** A short sensing interval preserves signal visibility; classical scheduling simplifies channel asymptotics while retaining a hard exposure budget.
- **Sources:** [Control, §3: duration choice](../science/control_and_resources.md#choosing-a-fixed-duration-with-nonzero-response) and [§7](../science/control_and_resources.md#7-lazy-slots-and-a-hard-exposure-budget); [Statistics, §1](../science/finite_memory_statistics.md#how-the-sensing-experiment-supplies-these-assumptions).

### M18 — Restricting to the actual recurrent support

- **Central question:** How can stationary analysis proceed when no full-rank stationary state exists on the entire environment?
- **Understanding target:** Identify the support spanned by stationary states, its Kraus invariance and the faithful stationary state on that support; distinguish this mathematical restriction from physically preparing the bath.
- **Dependencies and story role:** M10 and M17; establishes the correct domain for the stationary algebra proof.
- **Conceptual connection:** Transient states are retained in the experiment even though the persistent structure is analyzed on a smaller invariant support.
- **Sources:** [Statistics, §2, Lemmas 2–3](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support); [research dependencies CP16 and CG21](../references/related_work.md#stationary-structure-absorption-and-trajectory-mixtures).

### M19 — Persistent information has classical and quantum parts

- **Central question:** What does the fixed algebra say about all stationary environmental states?
- **Understanding target:** Distinguish finitely many central sectors, their noiseless quantum factors and their unique noisy-factor stationary states; explain why a basis choice inside a noiseless factor is not a new classical sector.
- **Dependencies and story role:** M18; resolves the form of all persistent information, including stationary coherences.
- **Conceptual connection:** The channel's algebraic decomposition replaces an unjustified assumption of a unique bath equilibrium.
- **Sources:** [Statistics, §2, Lemma 3](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support); [research dependency CP16](../references/related_work.md#stationary-structure-absorption-and-trajectory-mixtures).

### M20 — Perfectly preserved quantum information is invisible to the record

- **Central question:** Why can an unknown noiseless subsystem not create a continuum of different stationary score means?
- **Understanding target:** Explain how every outcome's Kraus operators refine the same averaged channel and therefore act trivially on its noiseless factors within each recurrent block; identify the resulting finite set of sector amplitudes.
- **Dependencies and story role:** M03, M16 and M19; turns stationary quantum structure into a finite observable classification.
- **Conceptual connection:** Information preserved perfectly by the averaged channel cannot simultaneously leak through a compatible measurement outcome.
- **Sources:** [Statistics, §2, Lemma 4 and sector responses](../science/finite_memory_statistics.md#lemma-4--every-compatible-outcome-is-invisible-to-a-noiseless-factor); [Examples, §4](../science/examples.md#4-noiseless-factors-and-transient-absorption).

### M21 — Harmonic effects account for eventual absorption

- **Central question:** How can recurrent-sector weights be defined for an arbitrary initial state, including transient population?
- **Understanding target:** Explain the positive effects obtained by pulling recurrent projections back through the stationary channel projection; understand their harmonicity and why they sum to the identity.
- **Dependencies and story role:** M18–M20; extends the stationary-sector description to the full initial-state space.
- **Conceptual connection:** Conserved observable weights connect transient evolution with persistent sector responses.
- **Sources:** WM §3.11 for the dual picture; [Statistics, §3, Lemma 5](../science/finite_memory_statistics.md#3-absorption-effects-and-an-auxiliary-sector-label); [research dependency CG21, Proposition 6](../references/related_work.md#stationary-structure-absorption-and-trajectory-mixtures).

### M22 — A sector label can be used without being measured

- **Central question:** How can the proof reason about a hidden sector without changing the experiment?
- **Understanding target:** Explain the exact joint probability law formed from a record and an absorption effect; distinguish its mathematical auxiliary label from a physical bath measurement or an assumed initial mixture.
- **Dependencies and story role:** M04 and M21; connects channel structure to the actual stochastic record.
- **Conceptual connection:** Harmonicity makes the auxiliary-label laws consistent while their marginal remains the original correlated experiment.
- **Sources:** [Statistics, §3: auxiliary sector law](../science/finite_memory_statistics.md#3-absorption-effects-and-an-auxiliary-sector-label); [research dependency CGH22, Lemmas 4.2–4.3](../references/related_work.md#stationary-structure-absorption-and-trajectory-mixtures).

### M23 — Correlations are summable after the correct centering

- **Central question:** What replaces the independent-sample variance calculation when the bath retains a sector indefinitely?
- **Understanding target:** Explain sector-centered score insertions, cancellation of the stationary projection, and the geometric remainder; recognize why no division by a possibly tiny sector weight is needed.
- **Dependencies and story role:** M10, M20 and M22; produces a finite-sample second-moment bound uniform in the initial bath state.
- **Conceptual connection:** Persistent sector uncertainty survives, while fluctuations around the realized sector response shrink with the record length.
- **Sources:** [Statistics, §4, Proposition 6](../science/finite_memory_statistics.md#4-a-finite-sample-second-moment-bound); [Examples, §3](../science/examples.md#3-conserved-sectors-why-ordinary-mixing-is-insufficient).

### M24 — Local calibration converts concentration into an estimator

- **Central question:** How can a frequency be estimated when the response sector is itself unknown?
- **Understanding target:** Explain why finitely many nonzero rotating amplitudes define separable arcs on a sufficiently small fixed interval; connect nearest-arc projection and inverse Lipschitz control to uniform mean-squared error.
- **Dependencies and story role:** M07, M20 and M23; completes the ideal statistical achievability proof.
- **Conceptual connection:** Geometric identifiability turns concentration around an unobserved response into an estimator using only the observed record.
- **Sources:** WM §§2.1–2.2 for the estimation setting; [Statistics, §5](../science/finite_memory_statistics.md#5-a-calibrated-interval-and-an-explicit-estimator).

### M25 — One finite interrogation approximates the normal form

- **Central question:** How accurately does a finite sequence of physical recoveries reproduce the effective sensing evolution?
- **Understanding target:** Connect the matching first-order generators to the second-order microcycle remainder; explain channel telescoping across one interrogation and uniformity over the parameter interval and hidden input.
- **Dependencies and story role:** M11, M14–M15 and M24; begins the implementation step after establishing the ideal estimator.
- **Conceptual connection:** A quantitative finite-control bound replaces reliance on an inaccessible infinite-recovery limit.
- **Sources:** [Control, §5](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound); [effective-control attribution, BFNPY20 and ST26](../references/related_work.md#effective-control-and-its-finite-cost).

### M26 — The full record carries a finite resource guarantee

- **Central question:** Which control schedule keeps implementation error below the estimator's statistical error?
- **Understanding target:** Combine record-channel telescoping with bounded-loss transfer; explain why a sufficient quadratic number of recoveries per round gives a cubic total count and preserves the $1/N$ squared-risk bound.
- **Dependencies and story role:** M07–M08, M11, M24 and M25; assembles the implemented general theorem with its resource cost.
- **Conceptual connection:** Statistical precision and control accuracy must be budgeted together across the same persistent bath realization.
- **Sources:** [Control, §§5–7](../science/control_and_resources.md#the-complete-retained-record); [Model, Theorem A](../science/model_and_results.md#3-general-local-precision-theorem).

### M27 — A native subclass removes the growing recovery cost

- **Central question:** When does the physical experiment already possess the required logical block structure?
- **Understanding target:** Identify native block-diagonal dynamics and explain how noncommuting bath Hamiltonians, including the dissipative example, still support the same estimator at fixed active cadence.
- **Dependencies and story role:** M05, M16–M17 and M26; separates a physically simpler regime from the general sufficient construction.
- **Conceptual connection:** Logical diagonality constrains the accessible probe; it does not require all environmental operators to share an eigenbasis.
- **Sources:** [Model, Corollary B](../science/model_and_results.md#4-a-fixed-cadence-subclass); [Control, §8](../science/control_and_resources.md#8-native-block-diagonal-dynamics-need-no-rapid-recovery); [Examples, §§1–2](../science/examples.md#1-a-native-model-with-a-noncommuting-qubit-environment).

### M28 — Examples probe distinct parts of the argument

- **Central question:** Which checks distinguish quantum memory, conserved sectors, noiseless factors and transient absorption?
- **Understanding target:** Relate each example to its corresponding proof assumption; distinguish exact finite checks, stochastic diagnostics and the analytical theorem, including their different error norms.
- **Dependencies and story role:** M19–M23 and M25–M27; integrates evidence across the mechanisms required for generality.
- **Conceptual connection:** A single mixing example cannot test the structural features that make the theorem independent of an equilibrium assumption.
- **Sources:** [Examples, §§3–6](../science/examples.md#3-conserved-sectors-why-ordinary-mixing-is-insufficient); [Statistics, §§2–4](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support); [Control, §5](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound).

### M29 — Global ambiguity survives arbitrary accessible control

- **Central question:** Why can unlimited observations still fail to identify a frequency over a wide interval?
- **Understanding target:** Explain the conserved hidden offset, the common transcript subdistribution for two separated frequencies, and its nonzero minimax-risk lower bound under adaptive probe-side protocols.
- **Dependencies and story role:** M07–M08, M22 and M24; establishes the boundary that the calibrated local theorem does not cross.
- **Conceptual connection:** Local response inversion and global parameter identification are distinct tasks even when the bath state is known initially.
- **Sources:** WM §§2.1–2.2 as estimation background; [Global ambiguity, §§1–4](../science/global_ambiguity.md#1-model); [Model, §5](../science/model_and_results.md#5-global-identification-can-fail).

### M30 — The complete contribution and its limits

- **Central question:** What does the combined construction establish about sensing with finite persistent memory?
- **Understanding target:** Connect the signal-preserving recovery, invisible noiseless factors, absorption-weighted concentration, local estimator and finite control schedule; distinguish inherited ingredients, the combined guarantee, the native subclass and the global obstruction.
- **Dependencies and story role:** M13–M29; synthesizes the entire scientific narrative and its physical meaning.
- **Conceptual connection:** Finite memory need not be erased for calibrated sensing, but that conclusion retains its known-model, ideal-control, local-identifiability and resource assumptions. Fixed-rate general control and plain prepare-and-measure universality remain outside the established result.
- **Sources:** [Model, §§3–6](../science/model_and_results.md#3-general-local-precision-theorem); [Statistics, §6](../science/finite_memory_statistics.md#6-what-the-theorem-establishes); [Control, §9](../science/control_and_resources.md#9-what-is-and-is-not-established); [Related work](../references/related_work.md).
