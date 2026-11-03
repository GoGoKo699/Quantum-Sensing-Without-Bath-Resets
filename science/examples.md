# Noncommuting environments and reproducible checks

The first two examples are sensing experiments with a qubit environment whose conditional Hamiltonians do not commute. They use a fixed sensing duration and one probe preparation and readout per round. The environment is carried from one round to the next, including its measurement backaction. Neither example needs rapid recovery pulses. The later examples isolate conserved sectors, an invisible quantum subsystem and transient absorption. A separate calculation checks the general recovery construction on a joint Hamiltonian and two nontrivial Lindblad jumps.

The companion program is [`code/verify_sensing.py`](../code/verify_sensing.py). Its checked output is [`results/sensing_checks.json`](../results/sensing_checks.json). The [statistics theorem](finite_memory_statistics.md) supplies the general local risk guarantee; the examples do not replace that proof.

## 1. A native model with a noncommuting qubit environment

Let $E$ and $P$ both be qubits. Write $X,Y,Z$ for the usual Pauli matrices, with $Y_{01}=-i$. Set

$$
H_0=\frac{X_E}{2},\qquad H_1=\frac{1.3Z_E}{2},\qquad G_P=\frac{Z_P}{2},
$$

and take

$$
H_\omega=H_0\otimes|0\rangle\langle0|
+H_1\otimes|1\rangle\langle1|
+\omega I_E\otimes G_P.
$$

The conditional bath Hamiltonians satisfy $[H_0,H_1]=-0.65iY_E\ne0$. This is already in logical dephasing form. It is not a static classical field model: successive measurements update a quantum environment that evolves under two incompatible rotations.

Fix $t=0.4$ for every sensing round, and define $U_i=e^{-itH_i}$. Prepare the accessible probe in $|+\rangle$, evolve for time $t$, choose $X$ or $Y$ with probability $1/2$, measure it, and record its outcome $y=\pm1$. The environment is not prepared again. Use the complex score

$$
z_{X,y}=2y,\qquad z_{Y,y}=-2iy.
$$

For $\theta=\omega t$, put $A_0=e^{-i\theta/2}U_0$ and $A_1=e^{i\theta/2}U_1$. The conditional bath Kraus operators, before including the setting probability, are

$$
B_{X,y}=\frac{A_0+yA_1}{2},\qquad
B_{Y,y}=\frac{A_0-iyA_1}{2}.
$$

The recorded-outcome instrument is therefore

$$
\mathcal M_{a,y}(\sigma)=\frac12 B_{a,y}\sigma B_{a,y}^\dagger.
$$

The factor $1/2$ is the probability of selecting the measurement setting. Summing all four outcomes and taking their score-weighted sum gives, exactly,

$$
\mathcal T(\sigma)
=\frac{U_0\sigma U_0^\dagger+U_1\sigma U_1^\dagger}{2},
\qquad
\mathcal W_\omega(\sigma)
=e^{-i\theta}U_0\sigma U_1^\dagger.
$$

In particular, the unobserved bath evolution is independent of $\omega$. The sign of the $Y$ score matters: with the stated Pauli convention, $\langle X\rangle-i\langle Y\rangle=2\rho_{01}$.

### Stationary response and absence of an unobserved persistent phase

The stationary bath state is $\tau=I_E/2$, with response

$$
c=\operatorname{Tr}(U_0\tau U_1^\dagger)
=\cos(0.2)\cos(0.26)
=0.9471265187303647.
$$

It is the only stationary state. To see why no other peripheral mode survives, consider the Hilbert–Schmidt triangle inequality for an eigenoperator of the average of two unitary conjugations. Equality at an eigenvalue of modulus one forces the two conjugations to have the same eigenoperator and eigenvalue. On traceless qubit operators, the two conjugations have eigenvalues $\{1,e^{\pm0.4i}\}$ and $\{1,e^{\pm0.52i}\}$. Their only common eigenvalue is $1$, whose respective axes are $X$ and $Z$ and have no nonzero intersection. Thus the only peripheral operator is the identity.

Numerically, the other eigenvalues of $\mathcal T$ are

$$
0.9504946506881592,
\qquad 0.9191927614961873\pm0.3144121326429763i.
$$

The largest nontrivial modulus is $0.97147842072796$. No scheduling skips are needed. Every $N$-round run has exposure exactly $Nt$ and uses $N$ fresh probe preparations and $N$ readouts.

The uniform short-time response condition is explicit here:

$$
\|\mathcal C_t-\operatorname{id}\|_{1\to1}
\le\|U_0-I\|+\|U_1-I\|
=2\sin(0.1)+2\sin(0.13)
<0.459<\frac12,
$$

where $\mathcal C_t(\sigma)=U_0\sigma U_1^\dagger$. This bound applies to every initial bath state, including a pure state.

### The records retain measurable memory

Write $S_N=\sum_{n=1}^N Z_n$ and $\mu=c e^{-i\omega t}$. At a stationary start, the lag-one complex covariance is

$$
\mathbb E[(Z_1-\mu)(Z_2-\mu)^*]
=0.09773424623363502.
$$

It is nonzero. Treating the records as independent would give the wrong variance coefficient. For the exact channel, let $\Pi(X)=\tau\operatorname{Tr}X$, and let $\overline{\mathcal W}$ denote conjugation of the scalar scores in the instrument sum. The geometric covariance sum gives

$$
v_\infty
=4-|\mu|^2
+2\operatorname{Re}\operatorname{Tr}\!\left[
\overline{\mathcal W}
(I-\mathcal T+\Pi)^{-1}(I-\Pi)
\mathcal W(\tau)
\right].
$$

Here

$$
v_\infty=3.372015250314819,
\qquad
v_{\mathrm{iid}}=4-|\mu|^2=3.1029513575177.
$$

The finite-length moments are computed by exact operator recursion, without sampling or replacing the bath by $\tau$ after a round:

| $N$ | $\mathbb E\lvert S_N-N\mu\rvert^2/N$, stationary start | Same quantity, initial $\lvert{+y}\rangle$ bath |
|---:|---:|---:|
| 64 | 3.32197511 | 3.32197511 |
| 256 | 3.35828625 | 3.35828625 |
| 1,024 | 3.36858219 | 3.36858219 |
| 4,096 | 3.37115699 | 3.37115699 |
| 16,384 | 3.37180072 | 3.37180072 |

The near equality of these two second moments is a property of this example, not an assumption in the theorem. The nonstationary start does have a finite mean transient. The program reports that bias separately.

### An estimator that uses only the record

For the calibrated interval $I=[-0.8,0.8]$, project $\overline Z_N=S_N/N$ onto the arc

$$
\{c e^{-i\omega t}:\omega\in I\}.
$$

The script considers angle representatives and endpoints explicitly, so it also handles observations outside the arc and a zero empirical mean. It never uses the true bath state to estimate $\omega$.

The following simulation uses $\omega=0.27$, initial bath $|{+y}\rangle$, 2,048 independent experimental runs and a fixed random seed. Within a run, the same bath is updated by the selected Kraus operator after every outcome. The uncertainty is the empirical standard error across runs, not a confidence interval or a theorem bound.

| $N$ | Empirical MSE | Standard error of MSE | $N\times\mathrm{MSE}$ |
|---:|---:|---:|---:|
| 128 | 0.11200928 | 0.00329347 | 14.33719 |
| 512 | 0.03011436 | 0.00097482 | 15.41855 |
| 2,048 | 0.00756817 | 0.00024059 | 15.49961 |
| 8,192 | 0.00186755 | 0.00005641 | 15.29899 |

An independent covariance-resolvent calculation for the tangent score

$$
r(z)=-\frac{\operatorname{Im}(e^{i\omega t}z)}{tc}
$$

gives the linearized local estimator variance coefficient $15.80923114$. The finite-run estimates are consistent with that scale. The local-uniform $O(1/N)$ guarantee follows from the theorem, rather than from fitting this table.

## 2. A dissipative variant at the same fixed cadence

Keep the Hamiltonian above and add the joint Lindblad jump

$$
L=\sqrt{\gamma}\,Y_E\otimes I_P,
\qquad\gamma=0.2.
$$

The bath is still never reset by the protocol. Its physical noise now includes continuous dissipation. The environment operators $X$, $Y$ and $Z$ have no common diagonal basis.

The population generators and the coherence generator are

$$
\mathcal K_i(\sigma)
=-i[H_i,\sigma]+\gamma(Y\sigma Y-\sigma),
$$

$$
\mathcal M_{01}(\sigma)
=-i(H_0\sigma-\sigma H_1)+\gamma(Y\sigma Y-\sigma).
$$

Consequently,

$$
\mathcal T=\frac{e^{t\mathcal K_0}+e^{t\mathcal K_1}}2,
\qquad
\mathcal C_t=e^{t\mathcal M_{01}},
\qquad
\mu=e^{-i\omega t}\operatorname{Tr}\mathcal C_t(I/2).
$$

These relations are checked against the full $EP$ Lindblad superoperator, followed by the actual probe projection and partial trace. They are not used to generate that independent full-system calculation.

Both population semigroups have $I/2$ as their unique stationary state. For example, the Bloch generator for $H_0=X/2$ has eigenvalues $-2\gamma$ and $-\gamma\pm i\sqrt{1-\gamma^2}$. For $H_1=1.3Z/2$, replace $1$ under the square root by $1.3^2$. The Hilbert–Schmidt dissipation identity is $\frac{d}{dt}\|A(t)\|_2^2=-\gamma\|[Y,A(t)]\|_2^2$. Equality over an interval would require the evolving traceless operator to remain proportional to $Y$, which either Hamiltonian immediately rotates away from that axis. Each evolution therefore strictly contracts the traceless subspace over a positive time, and their average has no other peripheral mode. The numerical values at $t=0.4$ are:

| Quantity | Value |
|---|---:|
| $c=\operatorname{Tr}\mathcal C_t(I/2)$ | 0.9498276886303852 |
| Largest nontrivial eigenvalue modulus of $\mathcal T$ | 0.898101036745804 |
| Uniform response-distance bound $\lVert F-I\rVert$, $\operatorname{Tr}\mathcal C_t(\sigma)=\operatorname{Tr}(F\sigma)$ | 0.3009281898036875 |
| Analytic uniform response-distance bound $t\lVert H_0-H_1\rVert$ | 0.3280243893371345 |
| Independent-record complex variance | 3.09782736191106 |
| Actual asymptotic complex variance | 3.1486084591514087 |
| Exact $\mathbb E\lvert S_N-N\mu\rvert^2/N$ at $N=4,096$ | 3.1489120302335323 |

The uniform nonvanishing response also has an analytic proof. A coherence map is an off-diagonal corner of a block-preserving channel and satisfies $\|\mathcal C_s(A)\|_1\le\|A\|_1$. This follows by applying trace-norm contraction of the full channel to the Hermitian block matrix with off-diagonal entries $A$ and $A^\dagger$. Moreover,

$$
\frac{d}{ds}\operatorname{Tr}\mathcal C_s(\sigma)
=-i\operatorname{Tr}[(H_0-H_1)\mathcal C_s(\sigma)].
$$

Integrating yields $|\operatorname{Tr}\mathcal C_t(\sigma)-1|\le t\|H_0-H_1\|<1/2$ for every density operator $\sigma$. The numerical bound on $F-I$ is tighter and provides a separate check. The estimator uses the same single-arc construction with this model's value of $c$. Every round again uses exposure $t$, one preparation and one readout. Rapid recovery and zero-duration skips are unnecessary in this variant.

## 3. Conserved sectors: why ordinary mixing is insufficient

Add a conserved classical sector $s\in\{0,1\}$ to the environment and use the first model with conditional signal shifts $\kappa_0=0$ and $\kappa_1=0.9$. Equivalently, the Hamiltonian in sector $s$ is $H_{\omega+\kappa_s}$. The two stationary responses are

$$
c_0=c,
\qquad c_1=c e^{-0.36i}.
$$

For initial sector weights $p=0.35$ and $1-p=0.65$, the empirical score mean does not concentrate around one deterministic mean. Its ordinary variance converges to

$$
p(1-p)|c_0-c_1|^2
=0.026164168620822964.
$$

In contrast, centering around the hidden sector response gives a second moment of order $1/N$. At $N=16,384$, the exact ordinary mean variance is $0.0263699670$, while

$$
N\,\mathbb E\bigl|\overline Z_N-c_J e^{-i\omega t}\bigr|^2
=3.37180074.
$$

The auxiliary sector label $J$ is used in the analysis only. An operational estimator projects onto the union of the two known arcs over $I=[-0.2,0.2]$. The arc centers are separated by phase $0.36$, and each arc has half-width $0.08$, so they are disjoint. The script also simulates this estimator without providing the sector label to it. At $N=8,192$, 1,024 runs give MSE $0.00196500$ and $N\times\mathrm{MSE}=16.09726$.

An initial coherent superposition of the two sectors gives exactly the same record probabilities as its sector-dephased state in this example. The instrument is block diagonal and the final trace removes the cross blocks. Direct enumeration checks this identity for all four-round records. This equality is specific to the conserved direct-sum example; the theorem treats general initial coherences with harmonic absorption effects.

## 4. Noiseless factors and transient absorption

Two further checks target assumptions that a primitive-bath calculation alone cannot test.

**An invisible noiseless factor.** Take $E=A\otimes B$, let the first example act on $B$, and let every bath instrument Kraus operator act as $I_A\otimes K$. The orthogonal Bell states $|\Phi^+\rangle$ and $|\Phi^-\rangle$ have the same $B$ marginal and hence exactly the same entire output law. The script enumerates every four-round outcome record and obtains zero discrepancy. This tests an actual quantum noiseless factor, rather than replacing it by a chosen classical basis.

**An initially transient environment.** A separate three-state finite-instrument example has a transient state $t$ and two absorbing states $0,1$. In each round, $t$ survives with probability $q=0.77$; otherwise it is absorbed into $0$ or $1$ with probabilities $p=0.35$ and $1-p$. The instrument first makes this hidden transition and then produces an $X/Y$ score with mean $m_x=a_x e^{-i\omega t}$ in the destination state, using

$$
a_t=0.85e^{0.2i},\qquad a_0=0.9,\qquad a_1=0.9e^{-0.36i}.
$$

For state order $(t,0,1)$, the harmonic effects are

$$
F_0=\operatorname{diag}(p,1,0),\qquad
F_1=\operatorname{diag}(1-p,0,1).
$$

The initial state is entirely transient. Without normalizing by either absorption weight, exact operator moments agree with the analytic identity

$$
\mathbb E[\mathbf1_{\{J=j\}}S_N]
=p_j\left[Nm_j+(m_t-m_j)\frac{q(1-q^N)}{1-q}\right].
$$

The absorption-weighted centered second moment divided by $N$ approaches $4-0.9^2=3.19$. This is an independent test of the theorem's statistical construction, including its finite initial transient. It is presented as a discrete instrument example, not as an additional physical Lindblad realization.

## 5. Finite recovery on a generic joint Lindblad model

The recovery calculation uses $E,P,A$ qubits, the tagged logical basis $|0_L\rangle=|0_P0_A\rangle$, $|1_L\rangle=|1_P1_A\rangle$, and

$$
\begin{aligned}
H_{EP}={}&0.43X_E\otimes X_P+0.29Z_E\otimes Y_P
+0.31Y_E\otimes Z_P\\
&+0.17Z_E\otimes I_P+0.11I_E\otimes X_P,\\
L_1={}&\sqrt{0.19}\left(X_E\otimes\sigma^-_P+0.3Z_E\otimes Z_P\right),\\
L_2={}&\sqrt{0.13}\left(\sigma^-_E\otimes Y_P+0.2I_E\otimes X_P\right).
\end{aligned}
$$

The signal is $\omega I_E\otimes Z_P/2$, with $\omega=0.37$. On $P\otimes A$, recovery has Kraus operators

$$
R_0=|00\rangle\langle00|+|11\rangle\langle11|,
\qquad
R_1=|00\rangle\langle10|+|11\rangle\langle01|.
$$

The program verifies trace preservation, idempotence and exact fixation of the code. It constructs the generator in two independent ways: by applying the full physical generator, recovery and decoding to arbitrary logical operators; and by taking the claimed branch Hamiltonian and jump matrix elements. Their superoperator discrepancy is $1.13\times10^{-16}$.

At total exposure $0.6$, the finite channel is obtained by exact physical evolution for a spacing $\delta$, recovery, and repetition. The following errors compare it with the limiting logical semigroup:

| Recoveries | Spacing $\delta$ | Superoperator Frobenius error | Normalized Choi trace distance |
|---:|---:|---:|---:|
| 4 | 0.15 | 0.13768582 | 0.02893840 |
| 8 | 0.075 | 0.06963561 | 0.01466112 |
| 16 | 0.0375 | 0.03503176 | 0.00738231 |
| 32 | 0.01875 | 0.01757139 | 0.00370457 |
| 64 | 0.009375 | 0.00879983 | 0.00185570 |

The errors scale consistently with first order in $\delta$. These are finite-dimensional diagnostic norms; the normalized Choi trace distance is not being identified with the diamond norm. The analytical control argument in [control and resources](control_and_resources.md) supplies the process-level bound and the $O(N^3)$ recovery count for the general finite-control protocol. The native examples in Sections 1–2 require no such recoveries.

## 6. Reproduction and scope of the checks

The run was verified with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. From the repository root:

```bash
python -m pip install -r requirements.txt
python code/verify_sensing.py
```

The output path defaults to `results/sensing_checks.json`. Use `--skip-monte-carlo` (or `--skip-mc`) for deterministic checks alone or `--output PATH` to keep a separate report. No network access is needed to run the calculation after the dependencies are installed.

The deterministic assertions check physical branch probabilities and partial traces, Kraus completeness, the complex-score sign, exact signal independence of the averaged bath map, stationary response, finite-word moments, covariance sums, conserved-sector coherence, noiseless-factor invisibility, transient absorption, noiseless arc inversion, and the finite recovery normal form. Monte Carlo rows are reported as reproducible diagnostics and are not used as pass/fail gates. This avoids mistaking a favorable stochastic sample for proof of the claimed scaling.
