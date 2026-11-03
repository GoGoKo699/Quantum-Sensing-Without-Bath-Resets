# Statistical estimation with a finite hidden environment

A finite environment can retain information indefinitely. Consequently, repeated measurements of a probe need not produce independent samples, and their empirical mean need not approach one deterministic value. The result proved here accommodates that possibility. The empirical mean approaches one of finitely many sector responses, each of which rotates with the signal at the same known angular speed. A fixed local calibration interval makes these responses distinguishable and gives an estimator with mean-squared error of order $1/N$.

The proof permits an arbitrary initial environmental state, transient population, coherences between recurrent sectors and noiseless quantum subsystems. It uses no measurement or reset of the environment. The [control construction](control_and_resources.md) supplies the required measurement instrument for the general Lindblad model. The [global ambiguity example](global_ambiguity.md) explains why the calibration interval is a substantive part of the result.

## 1. Instrument and estimator theorem

Let $\mathcal H_E$ be finite dimensional. One round is described by a finite instrument

$$
\{\mathcal M_{\omega,z}:z\in\mathcal Z\},
\qquad
\mathcal S=\sum_{z\in\mathcal Z}\mathcal M_{\omega,z},
$$

where every $\mathcal M_{\omega,z}$ is completely positive and $\mathcal S$ is trace preserving. The observed score $z$ is a complex number; distinct recorded outcomes with the same score may be combined. Set

$$
R=\max_{z\in\mathcal Z}|z|,
\qquad
\mathcal W_\omega=\sum_z z\,\mathcal M_{\omega,z}.
$$

The channel $\mathcal S$ is the environmental evolution obtained when the recorded outcome is ignored. It is assumed to be independent of $\omega$. Starting from an arbitrary density operator $\rho$, the probability of a record is

$$
p_{\omega,\rho}(z_1,\ldots,z_N)
=
\operatorname{Tr}\!\left[
\mathcal M_{\omega,z_N}\cdots
\mathcal M_{\omega,z_1}(\rho)
\right].
$$

No factorization of this probability into independent rounds is assumed.

**Theorem 1 — local mean-squared error from a finite hidden instrument.**
Suppose the following conditions hold:

1. $\mathcal S$ is a finite-dimensional, parameter-independent channel whose only eigenvalue on the unit circle is $1$.
2. There are a known nonzero real number $\kappa$ and a known linear functional $\ell$ such that, for every operator $X$,

   $$
   \operatorname{Tr}\mathcal W_\omega(X)
   =e^{-i\kappa\omega}\ell(X).
   $$

3. $\ell(\sigma)\ne0$ for every stationary density operator $\sigma$ of $\mathcal S$.

For every reference value $\omega_0$, there is a known interval
$I=[\omega_0-r,\omega_0+r]$ with $r>0$, independent of $N$, and an estimator using only the recorded scores such that

$$
\sup_{\omega\in I}\ \sup_{\rho\in\mathcal D(\mathcal H_E)}
\mathbb E_{\omega,\rho}
\left[(\widehat\omega_N-\omega)^2\right]
\le \frac{C_I}{N}.
$$

The constant depends on the instrument, the chosen interval and its finite-dimensional spectral data. It is independent of $N$, $\omega\in I$ and the initial state $\rho$. No uniform bound over all environmental dimensions, mixing times or noise models is asserted.

The proof below constructs the estimator and a finite constant. A weaker nonvanishing assumption on one representative of each central stationary sector would suffice. The stated condition is convenient for the sensing application, where a short sensing interval supplies a uniform lower bound for all environmental states.

### How the sensing experiment supplies these assumptions

In the dephasing normal form, a fresh logical $|+\rangle$ probe gives an environmental coherence map $\mathcal C_t$ and population channels $\mathcal E_0,\mathcal E_1$. Write

$$
\mathcal T=\frac{\mathcal E_0+\mathcal E_1}{2},
\qquad
\kappa=(g_0-g_1)t.
$$

Choose an $X$ or $Y$ measurement with equal probability. For its binary outcome $y$, use score $2y$ for an $X$ measurement and $-2iy$ for a $Y$ measurement. With this sign convention,

$$
\mathbb E[Z\mid\rho]
=e^{-i\kappa\omega}\operatorname{Tr}\mathcal C_t(\rho).
$$

The averaged channel is $\mathcal T$, exactly independent of the signal. The map $\mathcal C_t$ is not required to be a channel. Since $\mathcal C_0=\operatorname{id}$ and it is continuous in $t$, one may fix $t>0$ sufficiently small that

$$
\|\mathcal C_t-\operatorname{id}\|_{1\to1}<\frac12.
$$

It then follows that

$$
\left|\operatorname{Tr}\mathcal C_t(\rho)-1\right|<\frac12
$$

for every density operator $\rho$. In particular, the coherence response cannot vanish.

For a channel $\mathcal T$ with nontrivial peripheral eigenvalues, use a classical scheduling coin. With probability $1/2$, perform the sensing round. With probability $1/2$, perform no interaction and record score $0$. The skipped slot has zero duration. The resulting instrument has

$$
\mathcal M_{\omega,0}=\frac12\operatorname{id},
\qquad
\mathcal S=\frac{\operatorname{id}+\mathcal T}{2},
\qquad
\ell(X)=\frac12\operatorname{Tr}\mathcal C_t(X).
$$

Each of $N$ slots uses at most the fixed sensing duration $t$, so the total exposure is at most $Nt$ on every record. No environmental evolution interval is discarded without being charged.

For every channel eigenvalue $\lambda$ with $|\lambda|\le1$, the corresponding eigenvalue of $\mathcal S$ is $(1+\lambda)/2$. Its modulus is $1$ only when $\lambda=1$. Thus this scheduling choice supplies condition 1. A native experiment whose averaged channel already satisfies condition 1 can use every slot for sensing, with $\ell(X)=\operatorname{Tr}\mathcal C_t(X)$.

## 2. Stationary structure on its actual support

The stationary-sector decomposition used here is standard finite-dimensional channel theory. It is developed, in particular, by Carbone and Pautrat and is reviewed with its output-statistics consequences by Carbone, Girotti and Hernandez. We give the argument required for this experiment, including the support restriction that is necessary when no globally faithful stationary state exists. [References 1 and 3](#references)

### Lemma 2 — convergence to the stationary projection

There is a completely positive, trace-preserving projection $\Pi$ and constants $M<\infty$, $0<q<1$ such that

$$
\Pi=\lim_{n\to\infty}\mathcal S^n,
\qquad
\|\mathcal S^n-\Pi\|_{1\to1}\le Mq^n.
$$

Moreover,

$$
\Pi^2=\Pi,
\qquad
\mathcal S\Pi=\Pi\mathcal S=\Pi,
\qquad
\operatorname{ran}\Pi=\ker(\mathcal S-\operatorname{id}).
$$

**Proof.**
A channel is power bounded: its powers have diamond norm $1$ and hence induced trace norm at most $1$. Its eigenvalues have modulus at most $1$, and a Jordan block associated with an eigenvalue of modulus $1$ must be trivial, since a nontrivial such block would give polynomially growing powers. By assumption, the only peripheral eigenvalue is $1$. Finite-dimensional Jordan decomposition therefore gives the stated limit and exponential remainder, after choosing $q$ larger than the moduli of all remaining eigenvalues and absorbing their finite polynomial factors into $M$. The limit is a channel because complete positivity and trace preservation are closed in finite dimension. The projection identities follow from the spectral decomposition. $\square$

Define the recurrent support $\mathcal R$ to be the span of the supports of all stationary states, and let $P_{\mathcal R}$ be its orthogonal projector. A finite sum of stationary states can be chosen to have support exactly $\mathcal R$. After normalization, it gives a stationary state $\sigma_{\mathcal R}$ that is strictly positive on $\mathcal R$.

The subspace $\mathcal R$ is invariant under every Kraus operator of $\mathcal S$. Indeed, if
$\mathcal S(X)=\sum_\alpha K_\alpha X K_\alpha^\dagger$, then
$\mathcal S(\sigma_{\mathcal R})=\sigma_{\mathcal R}$. For any
$v\perp\mathcal R$,

$$
0=\sum_\alpha
\langle K_\alpha^\dagger v,\sigma_{\mathcal R}K_\alpha^\dagger v\rangle.
$$

Each term is nonnegative. Faithfulness on $\mathcal R$ implies
$P_{\mathcal R}K_\alpha^\dagger v=0$, equivalently
$K_\alpha\mathcal R\subseteq\mathcal R$.
Consequently, the restriction $\mathcal S_{\mathcal R}$ is a channel on $\mathcal R$.

### Lemma 3 — fixed algebra and noiseless factors

There is a finite orthogonal decomposition

$$
\mathcal R=
\bigoplus_{j=1}^{s}
\left(\mathcal H_{A_j}\otimes\mathcal H_{B_j}\right)
$$

such that

$$
\operatorname{Fix}(\mathcal S_{\mathcal R}^*)
=
\bigoplus_{j=1}^{s}
\left(\mathcal B(\mathcal H_{A_j})\otimes I_{B_j}\right),
$$

and, on each diagonal block,

$$
\mathcal S_{\mathcal R}
\big|_{A_jB_j}
=\operatorname{id}_{A_j}\otimes\mathcal S_j.
$$

Each $\mathcal S_j$ has a unique stationary state $\tau_j$, which is faithful on $\mathcal H_{B_j}$. The complete stationary operator space is

$$
\operatorname{Fix}(\mathcal S)
=
\left\{
\bigoplus_{j=1}^{s}X_j\otimes\tau_j:
X_j\in\mathcal B(\mathcal H_{A_j})
\right\},
$$

with zero support outside $\mathcal R$.

**Proof.**
The dual map $\mathcal S_{\mathcal R}^*$ is unital and has the faithful invariant state $\sigma_{\mathcal R}$. If $X$ is fixed, the Schwarz inequality gives

$$
\mathcal S_{\mathcal R}^*(X^\dagger X)-X^\dagger X\ge0.
$$

Its expectation in $\sigma_{\mathcal R}$ is zero by stationarity. Faithfulness makes the positive difference zero. Applying the same reasoning to $XX^\dagger$ shows that $X$ is in the multiplicative domain of $\mathcal S_{\mathcal R}^*$. Thus products and adjoints of fixed operators are fixed, and the fixed space is a finite-dimensional unital $C^*$-algebra.

In a Stinespring representation
$V\psi=\sum_\alpha K_\alpha\psi\otimes|\alpha\rangle$,
the multiplicative-domain equality for a fixed $X$ implies

$$
(X\otimes I)V=VX.
$$

Therefore $XK_\alpha=K_\alpha X$ for every Kraus operator of the restricted channel. The finite-dimensional representation of a $C^*$-algebra yields the displayed direct sum. Its commutant is
$\bigoplus_j(I_{A_j}\otimes\mathcal B(\mathcal H_{B_j}))$.
Hence every Kraus operator has the form

$$
K_\alpha\big|_{\mathcal R}
=\bigoplus_j I_{A_j}\otimes K_{\alpha,j},
$$

which proves the channel factorization.

The fixed algebra of $\mathcal S_j^*$ consists only of scalar multiples of the identity; otherwise the displayed fixed algebra would be larger. The fixed spaces of a finite linear map and its adjoint have the same dimension. Hence the stationary operator space of $\mathcal S_j$ is one dimensional. It contains a density operator, so that density operator is unique. Tracing a faithful stationary state on the full recurrent support over $\mathcal H_{A_j}$ supplies a faithful stationary state on $\mathcal H_{B_j}$, proving the claimed faithfulness.

The operators $X_j\otimes\tau_j$ are stationary. Their total dimension equals the dimension of the dual fixed algebra, so they exhaust the stationary space on $\mathcal R$. Finally, $\Pi$ sends a positive input to a stationary positive operator, which by definition is supported in $\mathcal R$. Since arbitrary operators are linear combinations of positive operators, $\operatorname{ran}\Pi$ is supported there as well. Lemma 2 then excludes additional stationary operators involving the transient complement. $\square$

The factors $\mathcal H_{A_j}$ can carry undisturbed quantum information. Their dimensions need not be one. The index $j$ labels the finitely many central blocks, rather than an arbitrarily selected basis of a noiseless subsystem.

### Lemma 4 — every compatible outcome is invisible to a noiseless factor

For every $\omega$, $z$ and recurrent block $j$,

$$
\mathcal M_{\omega,z}\big|_{A_jB_j}
=\operatorname{id}_{A_j}\otimes\mathcal M_{\omega,z}^{(j)}.
$$

In particular, the stationary output distribution on that block is independent of the state on $\mathcal H_{A_j}$.

**Proof.**
Combine Kraus operators for all the completely positive maps
$\mathcal M_{\omega,z}$. Together they form a Kraus representation of the same channel $\mathcal S$. The invariant-support argument and the multiplicative-domain argument in Lemma 3 apply to this representation. Every one of these Kraus operators therefore preserves $\mathcal R$ and commutes, on $\mathcal R$, with the full fixed algebra. It must have the form
$\bigoplus_j I_{A_j}\otimes K_{\omega,z,\alpha,j}$.
Summing the Kraus terms for a fixed outcome gives the claimed factorization.
For a stationary input $\nu_j\otimes\tau_j$, the trace of any outcome is consequently
$\operatorname{Tr}\mathcal M_{\omega,z}^{(j)}(\tau_j)$, independent of $\nu_j$. $\square$

This conclusion holds for each instrument in the parameterized family, even if its individual outcome maps depend on $\omega$. The fixed algebra and its decomposition depend only on the common averaged channel $\mathcal S$.

Choose any density operator $\nu_j$ on $\mathcal H_{A_j}$ and define

$$
a_j=\ell(\nu_j\otimes\tau_j),
\qquad
m_j(\omega)=e^{-i\kappa\omega}a_j.
$$

Lemma 4 and the first-moment identity make $a_j$ independent of the chosen $\nu_j$. Condition 3 makes every $a_j$ nonzero. The finitely many functions $m_j$ are the stationary sector responses.

## 3. Absorption effects and an auxiliary sector label

Let $P_j$ denote the projection onto $\mathcal H_{A_j}\otimes\mathcal H_{B_j}$, extended by zero outside $\mathcal R$. Define

$$
F_j=\Pi^*(P_j).
$$

These are the usual absorption effects associated with recurrent enclosures. Their general theory is developed by Carbone and Girotti; the required finite-dimensional properties follow directly here. [Reference 2](#references)

### Lemma 5 — positive harmonic effects

The effects satisfy

$$
0\le F_j\le I,
\qquad
\mathcal S^*(F_j)=F_j,
\qquad
\sum_jF_j=I.
$$

On the recurrent support, $F_j$ restricts to $P_j$.

**Proof.**
Positivity and the upper bound follow because $\Pi^*$ is unital and completely positive. Harmonicity follows from $\Pi\mathcal S=\Pi$.
For any operator $X$, $\Pi(X)$ is supported in $\mathcal R$, so

$$
\operatorname{Tr}\!\left[
\left(\sum_jF_j\right)X
\right]
=
\operatorname{Tr}[P_{\mathcal R}\Pi(X)]
=\operatorname{Tr}\Pi(X)
=\operatorname{Tr}X.
$$

This proves the sum identity. On $\mathcal R$, the channel preserves the trace in each central block. Thus
$\operatorname{Tr}[P_j\Pi(X)]=\operatorname{Tr}(P_jX)$
for $X$ supported in $\mathcal R$, which proves the restriction property. $\square$

For every finite record, introduce the nonnegative numbers

$$
\mathbb P_{\omega,\rho}
(J=j,Z_1=z_1,\ldots,Z_N=z_N)
=
\operatorname{Tr}\!\left[
F_j\mathcal M_{\omega,z_N}\cdots
\mathcal M_{\omega,z_1}(\rho)
\right].
$$

They sum to the observed record law. Summing over a final outcome preserves each prefix probability because $\mathcal S^*(F_j)=F_j$. They therefore define a consistent joint probability model with an auxiliary label $J$. Its marginal weight is

$$
\mathbb P_{\omega,\rho}(J=j)=\operatorname{Tr}(F_j\rho).
$$

The label is a mathematical device. The experiment does not observe it, and the estimator does not require its value or its probability. In particular, this construction does not replace the initial environmental state by a physical measurement or a known mixture. Transient population and initial coherences remain in the exact record probabilities above.

## 4. A finite-sample second-moment bound

The key cancellation is

$$
\operatorname{Tr}\!\left[
F_j\mathcal W_\omega\Pi(X)
\right]
=
m_j(\omega)\operatorname{Tr}[F_j\Pi(X)]
$$

for every operator $X$. To see this, write the stationary operator
$\Pi(X)=\bigoplus_k X_k\otimes\tau_k$.
Lemma 4 says that the outcome map acts as the identity on each $X_k$. The restriction of $F_j$ picks out block $j$, and the remaining trace is its stationary score mean.

Define the centered insertion maps

$$
\mathcal Q_j
=\sum_z(z-m_j)\mathcal M_{\omega,z}
=\mathcal W_\omega-m_j\mathcal S
$$

and

$$
\overline{\mathcal Q}_j
=\sum_z(\overline z-\overline{m_j})\mathcal M_{\omega,z}.
$$

The overline in the second notation conjugates the scalar scores; it does not conjugate the matrices or take the adjoint of the map. The cancellation gives

$$
\operatorname{Tr}[F_j\mathcal Q_j\Pi(X)]
=
\operatorname{Tr}[F_j\overline{\mathcal Q}_j\Pi(X)]
=0.
$$

All these maps have uniform finite induced trace norms. Indeed, every outcome map is completely positive and trace nonincreasing, so
$\|\mathcal M_{\omega,z}\|_{1\to1}\le1$.
Also $|m_j|\le R$ because it is the mean of scores bounded by $R$ in a normalized stationary state. If $b=|\mathcal Z|$, a sufficient bound is

$$
B:=
\sup_{\omega,j}
\max\{\|\mathcal Q_j\|_{1\to1},
\|\overline{\mathcal Q}_j\|_{1\to1}\}
\le2bR.
$$

### Proposition 6 — concentration around the unobserved sector response

For every $N$, $\omega$ and initial environmental state,

$$
\mathbb E_{\omega,\rho}
\left[
\left|\frac1N\sum_{n=1}^{N}Z_n-m_J(\omega)\right|^2
\right]
\le \frac{C_{\rm stat}}{N},
$$

where one may take

$$
C_{\rm stat}
=4R^2+\frac{2sB^2M}{1-q}.
$$

Here $s$ is the number of central recurrent blocks and $M,q$ are from Lemma 2.

**Proof.**
For $1\le i<k\le N$, summing the instrument expression over all unretained outcomes gives

$$
\begin{aligned}
&\mathbb E\!\left[
{\bf1}_{\{J=j\}}
(Z_i-m_j)(Z_k-m_j)^*
\right]\\
&\quad=
\operatorname{Tr}\!\left[
F_j\overline{\mathcal Q}_j
\mathcal S^{k-i-1}\mathcal Q_j
\mathcal S^{i-1}(\rho)
\right].
\end{aligned}
$$

The occurrences of $\mathcal S$ after round $k$ disappear by harmonicity of $F_j$. Insert
$\mathcal S^{k-i-1}=\Pi+(\mathcal S^{k-i-1}-\Pi)$.
The term with $\Pi$ vanishes by the preceding cancellation. Since
$\|F_j\|_\infty\le1$ and $\|\mathcal S^{i-1}(\rho)\|_1=1$,

$$
\left|
\mathbb E\!\left[
{\bf1}_{\{J=j\}}
(Z_i-m_j)(Z_k-m_j)^*
\right]
\right|
\le B^2Mq^{k-i-1}.
$$

For the diagonal terms, $|Z_i-m_J|\le2R$ gives

$$
\sum_j
\mathbb E\!\left[
{\bf1}_{\{J=j\}}|Z_i-m_j|^2
\right]
\le4R^2.
$$

Expand the squared modulus of the sum, use the covariance bound and sum over the central blocks:

$$
\begin{aligned}
\mathbb E\left|
\sum_{n=1}^{N}(Z_n-m_J)
\right|^2
&\le4R^2N
+2sB^2M\sum_{i<k}q^{k-i-1}\\
&\le
\left(4R^2+\frac{2sB^2M}{1-q}\right)N.
\end{aligned}
$$

Dividing by $N^2$ proves the result. $\square$

No conditional probability was divided by $\mathbb P(J=j)$. Thus the bound remains uniform when some sectors have arbitrarily small probability or are absent. The argument also starts at the actual first measurement; it requires neither a stationary initial state nor an unrecorded equilibration period.

General asymptotic Gaussian-mixture theorems for finite instruments are available in the literature. The direct second-moment argument is used here because it gives the finite-$N$ bound and initial-state uniformity needed by the estimation theorem, without transferring a convergence-in-distribution statement into a risk guarantee. [Reference 3](#references)

## 5. A calibrated interval and an explicit estimator

Keep one copy of each distinct amplitude among the finite set $\{a_j\}$. Equal amplitudes give the same response curve and require no distinction. Define

$$
a_{\min}=\min_j|a_j|>0,
\qquad
a_{\max}=\max_j|a_j|.
$$

If there is more than one distinct amplitude, also define

$$
\delta=\min_{a_j\ne a_k}|a_j-a_k|>0.
$$

Choose a fixed radius $r>0$ such that

$$
|\kappa|r\le\frac{\pi}{4},
\qquad
|\kappa|r\le\frac{\delta}{4a_{\max}}
$$

when $\delta$ is present. The second condition is unnecessary if every amplitude is identical. If the model is specified only on a bounded parameter interval, choose $r$ so that $I=[\omega_0-r,\omega_0+r]$ lies inside it.

For each distinct amplitude, define its response arc

$$
\mathcal A_j=
\{a_je^{-i\kappa\omega}:\omega\in I\}.
$$

Different arcs are separated by at least $\delta/2$. Indeed, every point on the $j$th arc is within $a_{\max}|\kappa|r$ of
$a_je^{-i\kappa\omega_0}$, while the distinct center points are separated by at least $\delta$.

On one arc, the chord bound gives

$$
|a_je^{-i\kappa\omega}
-a_je^{-i\kappa\omega'}|
\ge
\frac{2a_{\min}|\kappa|}{\pi}
|\omega-\omega'|.
$$

This follows from $2|\sin(u/2)|\ge2|u|/\pi$ for $|u|\le\pi$; our choice of interval guarantees that range. Across two distinct arcs,
$|\omega-\omega'|\le2r$ and the arc separation is at least $\delta/2$. Consequently, for all sector indices and all $\omega,\omega'\in I$,

$$
|\omega-\omega'|
\le K_I
|m_j(\omega)-m_k(\omega')|,
$$

where a valid finite inverse-Lipschitz constant is

$$
K_I=
\max\left\{
\frac{\pi}{2a_{\min}|\kappa|},
\frac{4r}{\delta}
\right\}.
$$

The second entry is omitted when there is one distinct amplitude.

Given
$\overline Z_N=N^{-1}\sum_nZ_n$, define

$$
(\widehat j,\widehat\omega_N)
\in
\underset{j,\ \omega'\in I}{\operatorname{argmin}}
\left|\overline Z_N-a_je^{-i\kappa\omega'}\right|.
$$

Choose a fixed deterministic rule for ties. The minimization is over finitely many known compact circular arcs, so a minimizer exists. Operationally, project the empirical complex mean onto each arc and retain the closest candidate. This rule uses the known amplitudes, the calibration interval and the classical measurement record. It does not use the hidden label or initial state.

For the actual auxiliary label $J$, the minimizing property and the inverse-Lipschitz inequality imply

$$
\begin{aligned}
|\widehat\omega_N-\omega|
&\le K_I
|m_{\widehat j}(\widehat\omega_N)-m_J(\omega)|\\
&\le2K_I|\overline Z_N-m_J(\omega)|.
\end{aligned}
$$

Proposition 6 now gives

$$
\sup_{\omega\in I,\rho}
\mathbb E_{\omega,\rho}
\left[(\widehat\omega_N-\omega)^2\right]
\le
\frac{4K_I^2C_{\rm stat}}{N},
$$

proving Theorem 1.

For fixed sensing duration $t$ and exposure ceiling $T_N=Nt$, this is an $O(T_N^{-1})$ squared-risk bound. Both $t$ and the interval $I$ are chosen once from the model and remain fixed as $N$ grows. The constants may deteriorate when the environmental channel develops very slow modes or two distinct sector responses become nearly indistinguishable.

## 6. What the theorem establishes

The proof establishes an attainable local-uniform mean-squared error. It makes no inference from an inverse Fisher-information bound, unbiasedness assumption or independence approximation. It accommodates arbitrary initial environmental states through the exact absorption-effect construction.

The theorem does not guarantee an estimator on every wide parameter interval. If distinct physical sectors produce exactly the same output at different parameter values, global identification can fail. The finite local calibration interval separates the response arcs relevant to this estimator.

The statistics theorem also does not supply its physical instrument for free. A native phase-covariant model may meet its assumptions at a fixed measurement cadence. For the general Lindblad model, the recovery construction and its finite control schedule must be charged as described in [control and resources](control_and_resources.md).

## References

1. R. Carbone and Y. Pautrat, *Irreducible decompositions and stationary states of quantum channels*, Reports on Mathematical Physics **77**, 293–313 (2016), [arXiv:1507.08404](https://arxiv.org/abs/1507.08404). Sections 5–7 develop recurrent supports and the stationary-state decomposition. The finite-dimensional argument used here is reconstructed in Lemmas 2–4.
2. R. Carbone and F. Girotti, *Absorption in Invariant Domains for Semigroups of Quantum Channels*, Annales Henri Poincaré **22**, 2497–2530 (2021), [doi:10.1007/s00023-021-01016-5](https://doi.org/10.1007/s00023-021-01016-5). Proposition 6 describes absorption operators; Section 4, including Theorem 22, relates them to fixed points when the recurrent support is attractive.
3. R. Carbone, F. Girotti and A. Melchor Hernandez, *On a Generalized Central Limit Theorem and Large Deviations for Homogeneous Open Quantum Walks*, Journal of Statistical Physics **188**, 8 (2022), [doi:10.1007/s10955-022-02938-y](https://doi.org/10.1007/s10955-022-02938-y). Section 4 gives the central recurrent decomposition; Lemmas 4.2–4.3 identify sector statistics and the absorption-weighted record mixture. Theorem 4.4 gives the general Gaussian-mixture limit, and Remark 4.6 extends the result to outcome maps with multiple Kraus operators.
