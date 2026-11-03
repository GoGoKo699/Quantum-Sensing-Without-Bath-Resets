# Local precision with an environment that is never reset

Repeated sensing ordinarily combines fresh preparations with repeated observations. A persistent environment changes that experiment: resetting the probe does not erase the environment's history, and successive observations can remain correlated. This project asks whether a finite inaccessible environment can prevent a local frequency estimate from attaining mean-squared error proportional to the inverse sensing exposure.

The answer proved here is an achievability statement under ideal local control. Every model in the class below admits a finite protocol with local-uniform squared risk at most $C/N$ after at most $N$ sensing intervals of a fixed duration. The environment can have several stationary sectors and noiseless internal subsystems. Its initial state is arbitrary and need not be known. The general implementation uses a number of ideal recovery operations that grows cubically with $N$. A native dephasing subclass attains the same risk order using a fixed prepare-and-measure cadence.

## 1. Physical model

Let $E$ be an inaccessible environment and $P$ an accessible probe, both finite dimensional. Between interventions, their joint density operator obeys

$$
\frac{d\rho}{dt}=\mathcal L_\omega(\rho),
\qquad
\mathcal L_\omega(\rho)
=-i[H+\omega I_E\otimes G,\rho]
+\sum_{k=1}^{r}\left(
L_k\rho L_k^\dagger-
\frac12\{L_k^\dagger L_k,\rho\}
\right).
$$

The Hermitian matrices $H$ and $G$, the jump operators $L_k$, and the dimensions are known. The sole unknown model parameter is the real frequency $\omega$. The probe signal generator $G$ has at least two distinct eigenvalues. All these operators are bounded because the spaces are finite dimensional. The jump operators can act jointly on $E$ and $P$; no commutation or detailed-balance assumption is imposed.

This is a time-homogeneous Markovian embedding of the probe's memory. The reduced probe dynamics can be non-Markovian. The model permits an additional Markovian reservoir implicit in the Lindblad terms; access to its emitted degrees of freedom is not assumed. It does not describe every possible infinite-memory or time-dependent noise process.

Initially the environment is in an arbitrary density operator $\rho_E$, independent of the frequency and unknown to the estimator. The accessible probe and auxiliary systems can be initialized independently. An arbitrary pre-existing probe state can be discarded locally at the start, preserving the environmental marginal.

### Allowed operations

The experimenter can prepare and measure the probe, use noiseless finite-dimensional auxiliaries, and apply parameter-independent local completely positive trace-preserving operations on those accessible systems. These operations are ideal and instantaneous in the sensing-exposure account. They never act directly on $E$.

The environment is never replaced or re-prepared. It nevertheless evolves, and conditioning on probe outcomes changes its conditional state. Local recovery may also change its later evolution through the coupling. These ordinary indirect effects are retained in the exact instrument probabilities.

Fresh initialization and reset of accessible systems are charged separately below. The protocol does not require storing unmeasured output probes between sensing intervals. Only a finite accessible workspace is needed at any instant; classical outcomes are retained for the estimator.

## 2. Estimation task and resources

Choose a reference frequency $\omega_0$. A calibration promise restricts the unknown parameter to a fixed interval

$$
I=[\omega_0-r_I,\omega_0+r_I],\qquad r_I>0.
$$

The interval is determined from the known model and stays fixed as the number of sensing slots increases. It is therefore larger than a shrinking asymptotic neighborhood. Its width can be small and model dependent.

For an estimator $\widehat\omega_N$ with values in $I$, define the worst-case risk

$$
\mathcal R_N(I)
=\sup_{\omega\in I}\sup_{\rho_E\in\mathcal D(\mathcal H_E)}
\mathbb E_{\omega,\rho_E}
\left[(\widehat\omega_N-\omega)^2\right].
$$

The expectation includes every quantum outcome and the protocol's classical randomization. The estimator has no access to $\rho_E$.

There are $N$ scheduling slots. Each active slot contains a sensing interval of duration $t$, chosen once from the model. A skipped slot is an instantaneous classical decision, with no physical waiting period. Thus the sensing exposure obeys

$$
T_{\mathrm{used}}\le Nt=:T_N
$$

on every record. If a fixed laboratory stopping time $T_N$ is required, unused time can be placed after the observations and ignored. No freezing of the environment during a positive-duration skip is assumed.

The resource $T_N$ excludes ideal operation duration. The number and rate of recoveries are consequently part of the result, rather than an implicit constant hidden in the exposure scaling. The theorem does not impose an efficient classical calibration algorithm or dimension-uniform constants.

## 3. General local precision theorem

**Theorem A — controlled local estimation without environmental resets.**
For every finite-dimensional model in Section 1 and every reference value $\omega_0$, there are known constants $t>0$, $r_I>0$, $a>0$, and $C<\infty$, independent of $N$, with the following property. For every integer $N\ge1$, an explicit protocol and estimator satisfy

$$
\mathcal R_N(I)\le \frac{C}{N},
\qquad
T_{\mathrm{used}}\le Nt.
$$

The protocol uses at most $N$ sensing rounds, a noiseless two-state logical tag, and at most

$$
N\lceil aN^2\rceil=O(N^3)
$$

recovery cycles, each using one accessible reset. There are also $O(N)$ probe/tag preparations and readouts. One recovery can be implemented with a resettable register of dimension $d_P=\dim\mathcal H_P$. The required recovery rate is $O(N^2)$ for fixed $t$. The environment is untouched by direct controls throughout the protocol.

There is no irreducibility, uniqueness-of-stationary-state, or initial-equilibration hypothesis. Constants may depend on the known generator, the chosen eigenvalue separation of $G$, the fixed interval, environmental dimension, spectral relaxation rates and separation of distinct stationary responses.

This is a guaranteed shot-noise-order upper bound on squared risk. Some models permit faster estimation. The result supplies neither a matching lower bound for every model nor a guarantee of fixed-rate control hardware.

### Proof and construction

Choose signal eigenvectors $|g_0\rangle,|g_1\rangle$ with $g_0\ne g_1$, and encode a logical qubit as

$$
|i\rangle_Q\longmapsto |g_i\rangle_P|i\rangle_A.
$$

A conditional recovery preserves this logical signal and converts the effective generator to one whose Hamiltonian and jumps are diagonal in $Q$. Their environmental blocks can remain noncommuting. The exact reduction, its finite implementation and its resource cost are proved in [Control and resources](control_and_resources.md).

In this effective model, prepare a fresh logical $|+\rangle$, evolve for time $t$, and randomly measure $X$ or $Y$. With binary result $y$, record $Z=2y$ for $X$ and $Z=-2iy$ for $Y$. The environmental population generators $\mathcal K_0,\mathcal K_1$ give the averaged environmental channel

$$
\mathcal T=\frac{e^{t\mathcal K_0}+e^{t\mathcal K_1}}{2},
$$

which is exactly independent of $\omega$. The score has conditional expectation

$$
\mathbb E[Z\mid\sigma]
=e^{-i\omega(g_0-g_1)t}
\operatorname{Tr}\mathcal C_t(\sigma).
$$

Here $\mathcal C_0=\operatorname{id}$. Fix $t$ sufficiently small that its response is within $1/2$ of $1$ for every environmental density operator. This guarantees a nonzero signal response in every stationary sector.

If needed, an independent scheduling coin replaces the averaged channel by $\mathcal S=(\operatorname{id}+\mathcal T)/2$. All peripheral eigenvalues except $1$ then lie strictly inside the unit disk. The channel can still have many stationary states. Its recurrent fixed algebra decomposes them into finitely many central sectors and noiseless quantum factors. Every outcome map compatible with $\mathcal S$ acts as the identity on those noiseless factors, so their arbitrary quantum states cannot create a continuum of different stationary output means.

Let $m_j(\omega)=a_j e^{-i\omega(g_0-g_1)t}$ be the finitely many stationary score responses. The amplitudes $a_j$ are known and nonzero. Positive harmonic absorption effects define an auxiliary sector label $J$ in the exact record law, without an environmental measurement. A direct covariance calculation gives

$$
\mathbb E\left|\frac1N\sum_{n=1}^{N}Z_n-m_J(\omega)\right|^2
\le\frac{C_{\mathrm{stat}}}{N}
$$

uniformly over the actual initial environmental state. The calculation includes transient population and initial coherences, and never divides by a sector probability.

On a sufficiently small fixed interval $I$, distinct response arcs are separated and their inverse in $\omega$ is Lipschitz. Projecting the empirical complex mean onto their union therefore produces an estimator with risk at most $C_0/N$. The full stationary-algebra, absorption, covariance and inversion arguments are given in [Finite-memory statistics](finite_memory_statistics.md).

Finally, replace the ideal effective evolution in each active round by $m_N=\lceil aN^2\rceil$ finite recovery cycles. Their complete measurement-record distribution differs from the ideal distribution by at most $C_1/N$ in total variation. Because the estimator is clipped to $I$, its squared loss is bounded by the squared diameter of $I$. The resulting risk changes by at most another constant divided by $N$. This proves Theorem A with a finite number of controls for each $N$. $\square$

## 4. A fixed-cadence subclass

**Corollary B — native logical dephasing.**
Suppose an accessible qubit already has joint operators of the form

$$
H=\sum_{i=0}^{1}H_i\otimes|i\rangle\langle i|,
\qquad
L_k=\sum_{i=0}^{1}A_k^i\otimes|i\rangle\langle i|,
\qquad
G=\sum_{i=0}^{1}g_i|i\rangle\langle i|,
\quad g_0\ne g_1.
$$

No commutation among the environmental matrices is required. Then there is a fixed duration $t$ and a fixed local interval for which fresh preparation, evolution, and random $X/Y$ readout attain $\mathcal R_N(I)\le C/N$ with no intermediate recovery. The number of probe preparations and readouts is $O(N)$, and the intervention cadence stays fixed.

**Proof.** The block structure gives the exact population/coherence decomposition used in Theorem A. The finite-instrument estimator applies directly, without the approximation step. The same zero-duration scheduling coin can remove peripheral periodicity when needed; every active interrogation still has duration $t$. $\square$

The [examples](examples.md) include noncommuting environmental Hamiltonians and a dissipative variant. This subclass is defined by diagonality on the accessible qubit. It does not require a common environmental eigenbasis.

## 5. Global identification can fail

The local calibration promise cannot be removed throughout the model class. A static environmental qubit can add a hidden shift $+g$ or $-g$ to the probe frequency. With the known initial mixture $I_E/2$, every accessible protocol has transcript law

$$
P_\omega=\frac12Q_{\omega+g}+\frac12Q_{\omega-g}.
$$

The two parameter values $-g$ and $+g$ share the same subdistribution $Q_0/2$ for every duration and every allowed control strategy. Their minimax squared risk is at least $g^2/2$. The [global ambiguity proof](global_ambiguity.md) includes arbitrary probe-only adaptive controls and auxiliaries.

The obstruction concerns unrestricted global consistency. It coexists with the local guarantee, because a calibrated interval can separate aliases. It also shows why an information-rate calculation at one parameter value is insufficient to establish global estimation.

## 6. Physical interpretation and attribution

Finite memory need not lose its initial state to allow local sensing. What matters for this protocol is the structure of the persistent information that remains visible in the output. The average environmental transition is parameter independent; perfectly preserved quantum factors are invisible to each compatible outcome. The remaining finite sector responses all retain the same signal phase, so local calibration converts correlated observations into a precision guarantee.

The statistical argument uses standard fixed-point and absorption structure. The metrological control idea builds on the logical-dephasing construction of Mann, Cao, Laflamme and Zhou. Their environment-diagonal SQL analysis and their broader prepare-and-measure conjecture are distinct from the controlled theorem stated here. The exact relationship to those sources, quantum Markov estimation theory and finite-rate control work is described in [Related work](../references/related_work.md).

The central scope is explicit: finite known Markovian embedding, a probe-only unknown signal, ideal accessible controls, a fixed local calibration interval, and separately counted recovery resources. Unknown noise generators, infinite hidden memory, finite-duration noisy controls, global ambiguity removal, and an optimal recovery count require additional analysis.

Continue with [Control and resources](control_and_resources.md), then [Finite-memory statistics](finite_memory_statistics.md).
