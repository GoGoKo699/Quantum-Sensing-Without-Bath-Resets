# Textbook anchor: quantum measurement and control

The sole textbook anchor is **Howard M. Wiseman and Gerard J. Milburn, _Quantum Measurement and Control_ (Cambridge University Press, 2010)**. Its measurement, estimation, open-system, and control topics provide the starting language for this project. The repository then develops the additional arguments needed when one inaccessible quantum environment persists throughout the experiment.

## 1. Selected source and what was verified

The edition used here is dated 2010 in the publisher's frontmatter; its hardback ISBN is **9780521804424**. Official sources are the [Cambridge book record](https://www.cambridge.org/core/books/quantum-measurement-and-control/F78F445CD9AF00B10593405E9BAC6B9F), the [book DOI](https://doi.org/10.1017/CBO9780511813948), and the [publisher's frontmatter and contents PDF](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf).

The reading locations below were verified against that frontmatter and contents. Full chapter text was not available for this guide. Page numbers are the book's printed page numbers, and topic descriptions are paraphrased. The displayed equations below use repository notation and derivations; no textbook equation numbers are assigned to them.

## 2. Verified reading locations and their role

| Book location | Foundational topic | Connection to this project |
|---|---|---|
| Chapter 1, §§1.3–1.4; starting pp. 27 and 32 | Operators for measurement outcomes and the general measurement framework | An outcome supplies both a probability and an updated hidden state. See the [instrument definition](../science/finite_memory_statistics.md#1-instrument-and-estimator-theorem). |
| Chapter 2, §§2.1–2.2; starting pp. 51 and 54 | Precision of parameter estimates and Fisher information | Establishes the estimation setting. The project separately constructs an estimator and proves its actual squared-risk bound. |
| Chapter 3, §§3.2 and 3.6; starting pp. 99 and 119 | Markov master equations and Lindblad positivity | The [physical model](../science/model_and_results.md#1-physical-model) assigns a Lindblad generator to the joint environment and probe. |
| Chapter 4; starting p. 148 | Conditional quantum trajectories | The [examples](../science/examples.md) carry the conditional bath state through successive probe observations. |
| Chapter 6, §§6.3 and 6.5; starting pp. 278 and 308 | General classical and quantum state-based control | Provides context for conditioning on a record. Here the estimator cannot assume the unknown initial bath state is available. |
| Chapter 7, §§7.4–7.7; starting pp. 353, 362, 368, and 375 | Error correction and continuous-control formulations | The [tagged recovery](../science/control_and_resources.md#2-a-tagged-code-and-its-exact-recovery) preserves a signal while changing the logical form of the noise. |

This is a topic map, with the additional mathematical work identified below. In particular, a Fisher-information calculation, a trajectory description, or a formal rapid-control limit alone does not supply the repository's finite-sample guarantee.

## 3. Notation and the physical assumptions

The central distinction is between the accessible sensor and the inaccessible memory. The following symbols are used in the scientific files.

| Symbol | Meaning here |
|---|---|
| $E$ | The finite environment retained throughout the experiment. |
| $P$ | The physical probe that can be prepared, measured, and reset. |
| $A$ | An accessible noiseless tag used by the general control construction. |
| $Q$, or $L$ in the control note | The encoded logical qubit carried by $P$ and $A$. |
| $\rho_E$, $\sigma$ | An initial bath state or a bath state conditioned on a measurement record. |
| $\omega$, $G$ | The unknown scalar frequency and its known probe generator. |
| $\mathcal L_\omega$ | The physical joint Lindblad generator on $EP$. |
| $\mathcal M_{\omega,z}$ | A completely positive outcome map acting on the bath, with its outcome probability included. |
| $\mathcal T$, $\mathcal S$ | The bath channels obtained by ignoring outcomes, before and after optional scheduling randomization. |
| $Z_n$ | A complex numerical score for the $n$th slot; it is not a Pauli operator. |
| $N$, $t$, $T_N=Nt$ | Number of scheduling slots, fixed active-interrogation duration, and hard exposure ceiling. |

The noise generator and dimensions are known; the scalar $\omega$ and initial state $\rho_E$ are unknown. The initial bath state is independent of $\omega$. The signal acts only on the probe, and $G$ has distinct eigenvalues. The dynamics is Markovian on the enlarged system $EP$; it can retain memory after reduction to the probe. Joint jump operators may also represent an additional Markovian reservoir whose outputs are unavailable. These assumptions are stated precisely in [Model and results](../science/model_and_results.md).

Accessible preparations, measurements, and recoveries are ideal and instantaneous in the exposure account. Their number is counted separately. Direct bath control and reset are unavailable. Probe measurements still change the conditional bath state, and accessible recovery can affect its subsequent evolution through the coupling. The theorem includes these indirect effects.

Two conventions prevent common notation errors. First, the factors named $A_j$ in the stationary decomposition below belong to the hidden environment; they are not copies of the accessible tag $A$. Second, the off-diagonal transfer $\mathcal C_t$ is a linear map on bath operators and need not be a quantum channel.

## 4. What the project adds to the textbook foundations

### A persistent bath changes the repeated experiment

Fresh probe preparation removes the probe's previous state. It does not remove the bath state left by earlier interactions and observations. Consequently, the next measurement can depend on the previous record even though its probe was freshly prepared. The relevant stochastic object is the entire correlated record from one persistent bath realization.

The [native qubit example](../science/examples.md#1-a-native-model-with-a-noncommuting-qubit-environment) makes this distinction concrete: the bath undergoes two noncommuting rotations conditioned on the probe basis, and successive scores have nonzero covariance. The [global ambiguity example](../science/global_ambiguity.md) shows a different possibility: a conserved hidden sector can act as a static unknown frequency shift.

### Outcome maps keep the hidden state and probability together

For an outcome with score $z$, the operator $\mathcal M_{\omega,z}(\sigma)$ is an unnormalized bath state. Its trace is the outcome probability; dividing by that trace gives the conditional state when the probability is nonzero. Setting choices and scheduling-coin probabilities are included in the appropriate maps. For a full record,

$$
p_{\omega,\rho_E}(z_1,\ldots,z_N)
=\operatorname{Tr}\!\left[
\mathcal M_{\omega,z_N}\cdots
\mathcal M_{\omega,z_1}(\rho_E)
\right].
$$

This expression retains the physical backaction between rounds. Summing over outcomes gives a trace-preserving map, while keeping them gives a quantum instrument. The [statistics setup](../science/finite_memory_statistics.md#1-instrument-and-estimator-theorem) uses this exact description without a product-distribution assumption.

### Control leaves a signal phase in every stationary response

The general construction encodes two distinct eigenstates of $G$ with an accessible tag. Its recovery makes the logical Hamiltonian and jumps diagonal in the same logical basis. Environmental blocks remain quantum and can fail to commute. This control objective preserves a usable signal; it does not require correcting the entire noise.

Let $\mathcal K_0,\mathcal K_1$ be the resulting bath population generators and $\kappa=(g_0-g_1)t$. A logical superposition followed by a random $X$ or $Y$ readout gives

$$
\mathcal T=\frac{e^{t\mathcal K_0}+e^{t\mathcal K_1}}{2},
\qquad
\mathbb E[Z\mid\sigma]
=e^{-i\kappa\omega}\operatorname{Tr}\mathcal C_t(\sigma).
$$

The score is $2y$ for an $X$ outcome $y=\pm1$ and $-2iy$ for a $Y$ outcome. Thus the two measured quadratures encode one complex phase response. The averaged bath channel $\mathcal T$ is exactly independent of $\omega$ in this effective model.

At $t=0$, $\mathcal C_t$ is the identity. A sufficiently short but fixed positive $t$ keeps its trace response near $1$ for every bath state. This supplies a nonzero response in every stationary sector, including sectors that the experimenter does not know are occupied. The [effective-generator derivation](../science/control_and_resources.md#3-exact-form-of-the-effective-generator) proves these claims.

### Stationary memory can include an invisible quantum factor

A bath channel may have many stationary states. When needed, a fair zero-duration skip produces $\mathcal S=(\operatorname{id}+\mathcal T)/2$, removing nontrivial peripheral eigenvalues while retaining stationary states. The limit $\Pi=\lim_n\mathcal S^n$ then exists.

On the span $\mathcal R$ of stationary-state supports, the fixed algebra yields finitely many central blocks,

$$
\mathcal R=\bigoplus_j
\left(\mathcal H_{A_j}\otimes\mathcal H_{B_j}\right).
$$

Stationary operators have blocks $X_j\otimes\tau_j$. The factor $A_j$ can retain arbitrary quantum information, while $\tau_j$ is the unique stationary state of the remaining factor. Every outcome map compatible with the same averaged channel acts as the identity on $A_j$. Therefore its unknown state cannot create a continuum of stationary output responses: only finitely many central-sector responses remain visible.

This is a specialized channel-structure argument, reconstructed in [Statistics, Lemmas 2–4](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support). Restricting to the actual recurrent support is necessary because a stationary state need not be faithful on the whole bath.

### Harmonic absorption handles unknown starts without measuring a sector

Let $P_j$ project onto a central recurrent block. Define the absorption effect

$$
F_j=\Pi^*(P_j),
\qquad
\mathcal S^*(F_j)=F_j,
\qquad
\sum_jF_j=I.
$$

These positive effects assign sector weights while including initially transient population. More precisely,

$$
\mathbb P(J=j,z_1,\ldots,z_N)
=\operatorname{Tr}\!\left[
F_j\mathcal M_{\omega,z_N}\cdots
\mathcal M_{\omega,z_1}(\rho_E)
\right]
$$

defines a consistent auxiliary joint law. Summing over $j$ recovers the actual observed record. The label $J$ is used in the proof; no sector measurement is performed, and the estimator never receives it. The [absorption argument](../science/finite_memory_statistics.md#3-absorption-effects-and-an-auxiliary-sector-label) preserves initial coherences and avoids division by possibly tiny sector weights.

### A local inverse turns correlated-score concentration into risk

The stationary score responses are finitely many known curves,

$$
m_j(\omega)=a_je^{-i\kappa\omega},
\qquad a_j\ne0.
$$

The finite-sample proof first establishes

$$
\mathbb E\left|\overline Z_N-m_J(\omega)\right|^2
\le\frac{C_{\rm stat}}{N},
\qquad
\overline Z_N=\frac1N\sum_{n=1}^{N}Z_n.
$$

It does so by summing covariances after subtracting the stationary projection. On a sufficiently small, fixed calibration interval, distinct response arcs are separated and their parameter inverse has a finite Lipschitz constant $K_I$. Projection of $\overline Z_N$ onto the known arcs then gives

$$
\mathbb E[(\widehat\omega_N-\omega)^2]
\le\frac{4K_I^2C_{\rm stat}}{N}.
$$

This is a bound on a specified estimator's actual loss, uniform over the unknown bath state. [Statistics, Sections 4–5](../science/finite_memory_statistics.md#4-a-finite-sample-second-moment-bound) contain the covariance and inverse arguments. The interval does not shrink with $N$, but its width depends on the known model. The global ambiguity proof explains why an arbitrary wide interval cannot be promised.

### Finite recovery transfers the whole experiment and charges its cost

The effective generator arises from a rapid-recovery limit. The physical theorem implements it with finitely many recovery cycles. If each active interrogation uses $m$ cycles, the complete output-channel error obeys

$$
\epsilon_{N,m}
\le\frac{Nt^2\Lambda^2}{m}e^{\Lambda t/m},
$$

where $\Lambda$ bounds the physical generator in diamond norm on the calibration interval. The comparison retains the conditional bath and the complete classical record, so it applies despite memory. Taking $m=O(N^2)$ makes record total variation $O(1/N)$. Because the estimator is clipped to a bounded interval, that record error changes squared risk by only $O(1/N)$.

The resulting sufficient cost is $O(N^3)$ recovery/reset uses, an $O(N^2)$ recovery rate, and another $O(N)$ preparations and readouts. This is an explicit ideal-control resource account, with no claim of optimality or bounded recovery throughput. Models already in the required logical form need no intermediate recovery and admit a fixed cadence. See [Control and resources, Sections 5–8](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound).

## 5. Research dependencies and proof locations

The book provides the foundations identified above. Specialized papers supply established structure used in the research argument; the scientific files include the particular proofs required here.

| Ingredient | Research dependency | Repository proof or application |
|---|---|---|
| Logical dephasing through tagged metrological control | [Mann, Cao, Laflamme, and Zhou (2025)](https://doi.org/10.1103/wfyl-wtz3) | [Control, Sections 2–4](../science/control_and_resources.md#2-a-tagged-code-and-its-exact-recovery); the paired recovery is derived explicitly. |
| Recurrent supports and stationary channel structure | [Carbone and Pautrat (2016)](https://arxiv.org/abs/1507.08404) | [Statistics, Lemmas 2–4](../science/finite_memory_statistics.md#2-stationary-structure-on-its-actual-support). |
| Harmonic absorption and sector mixtures | [Carbone and Girotti (2021)](https://doi.org/10.1007/s00023-021-01016-5); [Carbone, Girotti, and Melchor Hernandez (2022)](https://doi.org/10.1007/s10955-022-02938-y) | [Statistics, Sections 3–4](../science/finite_memory_statistics.md#3-absorption-effects-and-an-auxiliary-sector-label), followed by a direct finite-sample covariance bound. |
| Effective dynamics under frequent quantum operations | [Burgarth et al. (2020)](https://quantum-journal.org/papers/q-2020-07-06-289/) | [Control, Sections 5–6](../science/control_and_resources.md#5-a-uniform-finite-recovery-bound), including complete-record and bounded-loss transfer. |

The local inverse construction and global ambiguity example are proved in the repository. They should be assessed from their displayed assumptions and arguments. The [related-work account](../references/related_work.md) details the inherited ingredients and the comparison boundaries, including the distinction between this controlled theorem and the general conjecture for sensing without intermediate recovery.
