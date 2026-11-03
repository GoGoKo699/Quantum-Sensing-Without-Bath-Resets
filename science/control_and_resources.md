# Controls, effective dynamics, and finite resources

The sensing protocol uses a two-state label on an accessible noiseless ancilla to preserve a nonzero signal while converting the uncontrolled dynamics into a block-diagonal logical form. The hidden environment may still evolve quantum mechanically and retain correlations between experiments. A finite sequence of recoveries approximates this form in the diamond norm, which controls the complete retained measurement record and the resulting estimation risk.

The statistical argument is in [finite-memory statistics](finite_memory_statistics.md). The [examples](examples.md) include a model that already has the required form and therefore needs no recovery during an interrogation. [Global ambiguity](global_ambiguity.md) explains why the parameter interval must satisfy a local identifiability condition.

## 1. Physical model and control assumptions

Let $`E`$ and $`P`$ be finite-dimensional systems. Only $`P`$ and an auxiliary system $`A`$ are controlled. During a sensing interval, the joint generator is

```math
\mathcal L_\omega(X)
=-i[H+\omega I_E\otimes G,X]
+\sum_{j=1}^{r}\left(
L_jXL_j^\dagger-\frac12\{L_j^\dagger L_j,X\}
\right).
```

Here $`H,L_j,G`$ are known, $`G`$ is not scalar, and $`\omega`$ is unknown. The operators act trivially on the noiseless ancilla. The initial environment state can be arbitrary and unknown. The protocol never directly measures, prepares, or resets $`E`$.

Known preparation, measurement, unitary gates, and CPTP recovery maps on $`PA`$ are ideal and have zero duration in this model. Their number is counted below. The finite-horizon construction does not impose a bound independent of the horizon on their rate. Noise or positive-duration dynamics during these controls would require a separate implementation analysis.

The noise and interaction are independent of $`\omega`$; the signal acts only on the probe. These assumptions match the probe-only signal case of [Mann et al., PRX Quantum **6**, 030321 (2025)](https://doi.org/10.1103/wfyl-wtz3). No bath output is supplied to the estimator.

## 2. A tagged code and its exact recovery

Choose normalized eigenvectors of $`G`$ with distinct eigenvalues,

```math
G|g_i\rangle=g_i|g_i\rangle,
\qquad i\in\{0,1\},
\qquad \Delta g=g_0-g_1\ne0.
```

An auxiliary qubit has orthonormal states $`|0\rangle_A,|1\rangle_A`$. Define the isometry $`J:\mathbb C^2_L\to\mathcal H_P\otimes\mathcal H_A`$ by

```math
J|i\rangle_L=|g_i\rangle_P|i\rangle_A.
```

For each label $`i`$, independently choose an orthonormal basis $`\{|e_a^i\rangle\}_{a=0}^{d_P-1}`$ of the probe with $`|e_0^i\rangle=|g_i\rangle`$. The recovery has Kraus operators

```math
R_a=\sum_{i=0}^{1}
|g_i\rangle\langle e_a^i|_P\otimes|i\rangle\langle i|_A,
\qquad
\mathcal R(X)=\sum_{a=0}^{d_P-1}R_aXR_a^\dagger.
```

The label-dependent bases are essential. They give

```math
\sum_aR_a^\dagger R_a=I_{PA},
\qquad
R_aJ=\delta_{a0}J.
```

Every output is supported on the code. Consequently $`\mathcal R`$ is CPTP, $`\mathcal R^2=\mathcal R`$, and

```math
\mathcal R(JXJ^\dagger)=JXJ^\dagger
```

for every logical operator $`X`$, including $`|0\rangle\langle1|`$. Replacing both bases by one common probe basis would generally erase this coherence: the corresponding coefficient on that operator would be $`\langle g_1|g_0\rangle=0`$.

### Physical realization

Choose known unitaries $`U_i`$ with $`U_i|a\rangle=|e_a^i\rangle`$. Apply the controlled decoding unitary

```math
V=\sum_i U_i^\dagger\otimes|i\rangle\langle i|_A.
```

Reset the decoded probe to $`|0\rangle`$, then apply $`V^\dagger`$. A reset can be realized by swapping the probe with a fresh dimension-$`d_P`$ register $`D`$ in $`|0\rangle_D`$ and discarding $`D`$. On the relevant input basis, the resulting isometry is

```math
|e_a^i\rangle_P|i\rangle_A|0\rangle_D
\longmapsto
|g_i\rangle_P|i\rangle_A|a\rangle_D.
```

Tracing out $`D`$ gives precisely $`\mathcal R`$. The discarded register carries the recovery index $`a`$; it is not part of the sensing record. No operation in this implementation acts directly on $`E`$. The fixed controlled unitaries and the reset are charged each time the recovery is used.

## 3. Exact form of the effective generator

Write $`\mathcal J(X)=(I_E\otimes J)X(I_E\otimes J^\dagger)`$ for encoding. Let $`\mathcal D`$ decode operators supported on the code. Although this decoder is only defined on code-supported operators, the composite $`\mathcal D\circ(\operatorname{id}_E\otimes\mathcal R)`$ is a CPTP map on the full physical input space. The effective logical generator is

```math
\mathcal A_\omega
=\mathcal D\circ(\operatorname{id}_E\otimes\mathcal R)
\circ(\mathcal L_\omega\otimes\operatorname{id}_A)
\circ\mathcal J.
```

It is useful to derive its Lindblad form rather than infer complete positivity from a formal projection. Define operators on the hidden environment by

```math
H_i=\langle g_i|H|g_i\rangle_P,
\qquad
B_{j,a}^{i}=\langle e_a^i|L_j|g_i\rangle_P,
\qquad
S_i=\sum_{j,a}(B_{j,a}^{i})^\dagger B_{j,a}^{i}.
```

Completeness of each probe basis gives

```math
S_i=\sum_j\langle g_i|L_j^\dagger L_j|g_i\rangle_P.
```

The effective Hamiltonian and jumps are

```math
\overline H_\omega
=\sum_{i=0}^{1}(H_i+\omega g_iI_E)\otimes|i\rangle\langle i|_L,
\qquad
\overline L_{j,a}
=\sum_{i=0}^{1}B_{j,a}^{i}\otimes|i\rangle\langle i|_L.
```

Therefore

```math
\mathcal A_\omega(X)
=-i[\overline H_\omega,X]
+\sum_{j,a}\mathcal D[\overline L_{j,a}](X),
\qquad
\mathcal D[B](X)=BXB^\dagger-\tfrac12\{B^\dagger B,X\}.
```

To check the formula, apply the physical generator to an encoded operator. In the Hamiltonian and anticommutator terms, the identity $`R_aJ=\delta_{a0}J`$ leaves only the code projection on the other side. Each jump term retains every $`a`$, producing $`\overline L_{j,a}X\overline L_{j,a}^\dagger`$. The displayed identity for $`S_i`$ supplies the corresponding anticommutator. This proves the full generator equality on arbitrary operators, including operators entangled with an external reference.

All logical operators in this generator are diagonal in the same two-state basis. The environment blocks $`H_i,B_{j,a}^{i}`$ need not commute. Noise is retained; only its action on the logical label has been restricted.

### Population and coherence blocks

For a block $`X\otimes|i\rangle\langle k|`$,

```math
\mathcal A_\omega(X\otimes|i\rangle\langle k|)
=\left[\mathcal A_{ik}(X)-i\omega(g_i-g_k)X\right]
\otimes|i\rangle\langle k|,
```

where

```math
\mathcal A_{ik}(X)
=-i(H_iX-XH_k)
+\sum_{j,a}B_{j,a}^{i}X(B_{j,a}^{k})^\dagger
-\frac12(S_iX+XS_k).
```

Each $`K_i=\mathcal A_{ii}`$ is a Lindblad generator on $`E`$. The off-diagonal transfer

```math
C_t=e^{t\mathcal A_{01}}
```

is a linear map; it need not be a quantum channel. If the logical state is prepared as $`|+\rangle_L`$, evolution for time $`t`$ gives blocks

```math
\frac12
\begin{pmatrix}
e^{tK_0}(\sigma)&e^{-i\omega\Delta g t}C_t(\sigma)\\
e^{i\omega\Delta g t}C_t(\sigma)^\dagger&e^{tK_1}(\sigma)
\end{pmatrix}.
```

Consequently the unconditioned hidden channel after logical readout and preparation of the next probe is

```math
T=\frac12\left(e^{tK_0}+e^{tK_1}\right),
```

which is exactly independent of $`\omega`$. The parameter remains as the scalar phase multiplying the coherence block. This separation is the input to [finite-memory statistics](finite_memory_statistics.md).

### Choosing a fixed duration with nonzero response

A conservative duration can be selected directly from the known matrices. Define

```math
\beta=\|H_0\|_\infty+\|H_1\|_\infty
+\sum_{j,a}\|B_{j,a}^{0}\|_\infty\|B_{j,a}^{1}\|_\infty
+\frac12(\|S_0\|_\infty+\|S_1\|_\infty).
```

Left and right multiplication bounds give $`\|\mathcal A_{01}\|_{1\to1}\le\beta`$, hence

```math
\|C_t-\operatorname{id}\|_{1\to1}\le e^{\beta t}-1.
```

For $`\beta>0`$, taking $`t=\log(4/3)/\beta`$ makes this at most $`1/3`$. If $`\beta=0`$, the coherence map is the identity and any positive fixed duration suffices. Thus every density operator $`\sigma`$ satisfies $`|\operatorname{Tr}C_t(\sigma)-1|<1/2`$. This is a sufficient choice; a model-specific response estimate can permit a larger duration, as in the examples. The duration is fixed before choosing the local calibration interval or the number of rounds.

## 4. Relation to the earlier dephasing reduction

[Mann et al., Sections III B and IV A](https://arxiv.org/html/2503.07745v2) use codewords with orthogonal ancillary supports to make compressed probe operators diagonal. Their Eq. (44), applied to leakage outside the code, returns each ancillary-support branch to its codeword. That construction and its use in metrology are inherited ingredients.

The recovery above pairs the $`a`$-th basis modes of the two labels, so it can preserve coherence between those leakage modes. It is a different CPTP recovery; its off-diagonal coefficients are derived explicitly in Section 3. Our eigenstate code needs only a two-state tag because it aims to retain a nonzero signal and obtain diagonal logical dynamics, without correcting the entire noise. The later statistical result treats noncommuting hidden blocks and general recurrent sectors. It does not prove the narrower conjecture about plain prepare-and-measure experiments with no intermediate recovery.

Frequent quantum operations and their effective dynamics belong to established quantum Zeno theory; see [Burgarth et al., Quantum **4**, 289 (2020)](https://quantum-journal.org/papers/q-2020-07-06-289/). The elementary bound below makes the required finite-horizon error and recovery count explicit for this projection.

Finite-rate controls in non-Markovian metrology are also studied by [Shravan and Thurtell, arXiv:2607.12913 (2026)](https://arxiv.org/abs/2607.12913), whose stated results connect Heisenberg-limited protocols with the Zeno effect and compare measurement, active-recovery, and dynamical-decoupling constructions through their quantum Fisher information. The bound below serves a specific purpose: it controls the entire correlated sensing record and transfers a bounded-loss estimation guarantee to a finite sequence of recoveries. It makes no claim to optimize control-frequency dependence.

## 5. A uniform finite-recovery bound

Fix a compact parameter interval $`I`$. Choose a finite constant $`\Lambda`$ satisfying

```math
\sup_{\omega\in I}\|\mathcal L_\omega\|_\diamond\le\Lambda.
```

One sufficient choice is

```math
\Lambda
=2\|H\|_\infty
+2\sup_{\omega\in I}|\omega|\,\|G\|_\infty
+2\sum_j\|L_j\|_\infty^2.
```

Identity extensions do not alter the diamond norm. Encoding and the full composite $`\mathcal D\circ(\operatorname{id}_E\otimes\mathcal R)`$ are channels, so $`\|\mathcal A_\omega\|_\diamond\le\Lambda`$. These same channels contract the Taylor remainder below. One physical microcycle of duration $`h`$, viewed as a channel on $`EL`$, is

```math
F_{\omega,h}
=\mathcal D\circ(\operatorname{id}_E\otimes\mathcal R)
\circ e^{h(\mathcal L_\omega\otimes\operatorname{id}_A)}
\circ\mathcal J.
```

It is CPTP, and its first-order expansion is $`I+h\mathcal A_\omega`$. For any bounded superoperator $`B`$,

```math
\|e^{hB}-I-hB\|_\diamond
\le e^{h\|B\|_\diamond}-1-h\|B\|_\diamond
\le\frac{h^2\|B\|_\diamond^2}{2}e^{h\|B\|_\diamond}.
```

Apply this to the physical and effective generators. The two remainders give

```math
\boxed{
\|F_{\omega,h}-e^{h\mathcal A_\omega}\|_\diamond
\le h^2\Lambda^2e^{h\Lambda}.
}
```

For $`m`$ equal microcycles with $`h=t/m`$, telescoping through channels of diamond norm one yields

```math
\boxed{
\|F_{\omega,t/m}^{\,m}-e^{t\mathcal A_\omega}\|_\diamond
\le\frac{t^2\Lambda^2}{m}e^{\Lambda t/m}.
}
```

These bounds are uniform over $`\omega\in I`$, every initial state of the hidden environment, and arbitrary external reference systems. They do not require a stationary, full-rank, or mixing environment state.

### The complete retained record

A sensing instrument is the CPTP map that appends its classical setting and outcome to a record while retaining its conditional environment output. Preparation and measurement compose with each interrogation channel without increasing its diamond-norm error. The same is true when the setting choices or later operations are controlled by an already retained classical record.

For a protocol with at most $`N`$ active interrogations, replacing every ideal interrogation by its $`m`$-microcycle implementation therefore changes the complete output channel by at most

```math
\epsilon_{N,m}
\le\frac{N t^2\Lambda^2}{m}e^{\Lambda t/m}.
```

The output here includes the complete sensing record: sampling coins, measurement settings, and all retained outcomes. It may also include the final hidden system and an untouched reference. The recovery registers specified in Section 2 are discarded. This channel comparison does not replace the actual correlated record by independent samples.

## 6. Recoveries sufficient for the statistical risk

Let the parameter interval have diameter $`B_I`$. The estimator in [finite-memory statistics](finite_memory_statistics.md) takes values in that interval and has ideal risk at most $`C_{\rm ideal}/N`$, where

```math
C_{\rm ideal}=4K_I^2C_{\rm stat}.
```

Here $`C_{\rm stat}`$ is the mean-score concentration constant and $`K_I`$ is the inverse-curve constant used there. The estimator's squared loss lies in $`[0,B_I^2]`$.

An unhalved diamond error $`\epsilon_{N,m}`$ gives total variation at most $`\epsilon_{N,m}/2`$ for the retained classical record. Applying the same estimator to the physical record changes its risk by at most $`B_I^2\epsilon_{N,m}/2`$. Set

```math
c_0=t^2\Lambda^2e^{\Lambda t},
\qquad
m_N=\max\{1,\lceil c_0N^2\rceil\}.
```

Then $`\epsilon_{N,m_N}\le1/N`$, and

```math
\boxed{
\sup_{\omega\in I,\,\rho_E}
\mathbb E_{\omega,\rho_E}
[(\widehat\omega-\omega)^2]
\le\frac{C_{\rm ideal}+B_I^2/2}{N}
=\frac{4K_I^2C_{\rm stat}+B_I^2/2}{N}.
}
```

No continuity claim about Fisher information is used. The proof compares the actual loss of a specified estimator.

For fixed physical model and fixed interrogation duration, the number of recoveries within interrogations is at most $`Nm_N=O(N^3)`$, the spacing within an active interrogation is $`t/m_N=O(N^{-2})`$, and a dimension-$`d_P`$ reset register can be reused between recoveries. The same count applies to its initialization or replacement uses. There are additionally $`O(N)`$ probe/tag preparations and logical readouts, including the resets needed to start each active interrogation. The bound is sufficient; it is not a lower bound or an optimized control cost.

## 7. Lazy slots and a hard exposure budget

The statistics proof uses the channel $`S=(I+T)/2`$ to remove nontrivial peripheral eigenvalues. This has a direct protocol interpretation. Predraw $`N`$ independent fair coins. For an active coin, perform one duration-$`t`$ interrogation and retain its setting and outcome. For an inactive coin, append the prescribed zero score and perform no physical evolution or operation.

An inactive slot has zero elapsed duration in the ideal control model. It does not hold the bath fixed for a positive waiting time. The active experiments can be run consecutively after the coins are drawn; inserting the known zero scores is classical record processing. The environment evolves continuously throughout every actual interrogation.

For every coin realization,

```math
T_{\rm exposure}=t\times\#\{\text{active slots}\}\le Nt,
\qquad
N_{\rm recovery}\le Nm_N.
```

The finite-control comparison remains valid after retaining all coins. The resulting $`O(1/N)`$ risk is therefore an $`O(1/T_{\rm budget})`$ achievability result under the hard budget $`T_{\rm budget}=Nt`$. A positive lower bound on gate, measurement, or reset duration is not included in this exposure convention.

## 8. Native block-diagonal dynamics need no rapid recovery

A useful subclass already has the effective form on two probe eigenstates. It is sufficient that the physical Hamiltonian and every jump reduce the two sectors:

```math
H=\sum_{i=0}^{1}H_i\otimes|g_i\rangle\langle g_i|\ \oplus\ H_{\rm rest},
\qquad
L_j=\sum_{i=0}^{1}B_j^{i}\otimes|g_i\rangle\langle g_i|\ \oplus\ L_{j,\rm rest}.
```

On their span, the signal is diagonal and populations are preserved. The hidden blocks may be noncommuting. Preparing the probe superposition, allowing duration-$`t`$ evolution, and measuring its two quadratures implements the required instrument exactly. The auxiliary tag and the intermediate recoveries can be omitted.

For this subclass, at most $`N`$ probe preparations, measurements, and ordinary probe resets suffice, with active measurements separated by the fixed time $`t`$. The [noncommuting bath example](examples.md) illustrates this case. The general theorem's cubic sufficient recovery count is unnecessary here.

## 9. What is and is not established

The result guarantees standard-quantum-limit order in exposure for a calibrated fixed local interval, uniformly over the initial hidden state. Some models allow better precision, so this is not a universal lower bound on estimation error. The general construction uses ideal controls at a rate that increases with the horizon. A universal theorem with fixed recovery throughput, noisy controls, a bounded supply of fresh auxiliary states, or no intervention during each probe's evolution is not established by this argument.
