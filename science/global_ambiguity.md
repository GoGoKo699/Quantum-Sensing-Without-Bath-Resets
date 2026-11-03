# A hidden conserved sector can prevent global estimation

Finite environmental memory does not by itself guarantee that a single sensing record identifies an unknown parameter over an arbitrary interval. A conserved hidden label can act as an unknown static offset. The example below gives an exact minimax obstruction under arbitrary probe-side controls, including auxiliary systems and adaptive measurements.

This does not obstruct the calibrated local guarantee in [finite-memory statistics](finite_memory_statistics.md). It explains why the parameter interval in that theorem is chosen to separate the finitely many observable sector branches.

## 1. Model

Let $`E`$ and $`P`$ be qubits, let $`g>0`$ be known, and set

```math
H_\omega=(\omega I_E+g Z_E)\otimes Z_P.
```

The signal generator is the nonscalar probe operator $`G=Z_P`$. The known initial environment state is $`I_E/2`$. No direct environment control is available. The probe may be prepared, controlled, measured, and reset arbitrarily, with noiseless auxiliary systems and classical adaptation.

One may also add any fixed probe-only Lindblad generator $`\mathcal L_P`$:

```math
\mathcal L_\omega(X)
=-i[H_\omega,X]
+(\operatorname{id}_E\otimes\mathcal L_P)(X).
```

For example, $`\mathcal L_P=\gamma\mathcal D[Z_P]`$ with $`\gamma>0`$ gives a genuinely dissipative instance. The argument does not depend on the strength or absence of this added noise.

The projectors onto $`Z_E=+1`$ and $`Z_E=-1`$ are conserved by both the joint dynamics and all accessible controls. Conditional on the first sector, the probe experiences total field $`\omega+g`$; conditional on the second, it experiences $`\omega-g`$.

## 2. Every adaptive record remains a two-component mixture

Fix any protocol, including its classical randomization, settings, stopping rules, ancillas, and final readout. Let $`Q_v`$ be its record distribution when the total probe field is $`v`$ and the same probe noise is present. The unknown parameter does not enter the protocol's control instructions except through observations.

Linearity of each instrument and conservation of the hidden sectors imply, for the complete retained record,

```math
\boxed{
P_\omega=\frac12Q_{\omega+g}+\frac12Q_{\omega-g}.
}
```

This identity holds at every finite horizon and for arbitrary adaptive choices. To see this directly, condition on a complete record prefix. Each branch applies the same accessible instrument selected by that prefix, while its underlying physical generator depends only on its total field. Iterating preserves the two unnormalized sector contributions; summing them at the end yields the mixture above. No independence assumption between successive measurements is used.

A known pure initial environment state $`|+\rangle_E`$ gives the same accessible record law. Its off-diagonal sector terms remain off-diagonal under all permitted operations and vanish when the hidden environment is traced out.

## 3. A risk lower bound independent of exposure

Consider two possible signal values,

```math
\omega_-=-g,
\qquad
\omega_+=g.
```

Their record laws are

```math
P_- =\frac12Q_{-2g}+\frac12Q_0,
\qquad
P_+ =\frac12Q_0+\frac12Q_{2g}.
```

Thus both distributions contain the identical submeasure $`Q_0/2`$, whatever the protocol or exposure. For any estimator $`\widehat\omega`$, including a randomized one, the equal-prior average risk obeys

```math
\begin{aligned}
\frac12\mathbb E_-[(\widehat\omega+g)^2]
+\frac12\mathbb E_+[(\widehat\omega-g)^2]
&\ge\frac14\mathbb E_{Q_0}
\left[(\widehat\omega+g)^2+(\widehat\omega-g)^2\right]\\
&=\frac12\mathbb E_{Q_0}[\widehat\omega^2]
+\frac{g^2}{2}\\
&\ge\frac{g^2}{2}.
\end{aligned}
```

Since the maximum of the two risks is at least their average,

```math
\boxed{
\inf_{\text{accessible protocols},\,\widehat\omega}
\sup_{\omega\in\{-g,g\}}
\mathbb E_\omega[(\widehat\omega-\omega)^2]
\ge\frac{g^2}{2}.
}
```

The lower bound applies to any larger parameter interval containing both values. It already holds for one fixed, known initial environment state, so allowing that state to be unknown cannot remove the obstruction. If an estimator has infinite risk, the inequality is immediate; otherwise all displayed expectations are well-defined.

## 4. Local information and global identification are different

Within a sufficiently narrow parameter interval, the two offset branches can be separated. Repeated probes can then estimate the field within the realized branch. The exact overlap above concerns distinct parameter values separated by $`2g`$ and does not imply a vanishing local Fisher-information rate.

[Mann et al., Section IV](https://arxiv.org/html/2503.07745v2) formulate an SQL question in terms of Fisher-information scaling for hidden Markovian quantum dynamics. The present example is compatible with that local question. Its role here is to establish the necessary scope of an actual uniform MSE statement over one persistent bath realization.

The normal-form protocol handles the remaining quantum dynamics through finitely many observable recurrent sectors. Its estimator uses a fixed local interval on which the corresponding mean curves are distinguishable. [Controls and resources](control_and_resources.md) account for the operations needed to reach that form. Neither more exposure nor more probe-side processing can resolve the exact sector ambiguity in the example without additional information or access.
