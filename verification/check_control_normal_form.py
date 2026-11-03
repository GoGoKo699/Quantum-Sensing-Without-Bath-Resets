"""Finite-dimensional algebra checks for the tagged recovery construction.

These checks compare two independently assembled superoperators.  The
finite-step norms below are Hilbert--Schmidt induced norms, not diamond norms;
the public diamond-norm statement is proved analytically.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm


def superoperator(k: np.ndarray) -> np.ndarray:
    return np.kron(k.conj(), k)


def gksl(h: np.ndarray, jumps: list[np.ndarray]) -> np.ndarray:
    ident = np.eye(h.shape[0], dtype=complex)
    result = -1j * (np.kron(ident, h) - np.kron(h.T, ident))
    for jump in jumps:
        s = jump.conj().T @ jump
        result += superoperator(jump)
        result -= 0.5 * (np.kron(ident, s) + np.kron(s.T, ident))
    return result


def main() -> None:
    rng = np.random.default_rng(20261103)
    de, dp, da = 2, 3, 2
    dphysical, dlogical = de * dp * da, de * 2

    def randmat(n: int, scale: float) -> np.ndarray:
        return scale * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))

    raw_h = randmat(de * dp, 0.13)
    h = (raw_h + raw_h.conj().T) / 2
    jumps = [randmat(de * dp, 0.06) for _ in range(2)]
    eigenvalues = np.array([0.75, -0.65, 0.2])
    g = np.diag(eigenvalues)
    omega = 0.37
    ep = np.eye(dp, dtype=complex)
    el = np.eye(2, dtype=complex)
    gi = [ep[:, 0], ep[:, 1]]
    basis = []
    for i in range(2):
        rest = [p for p in range(dp) if p != i]
        q, _ = np.linalg.qr(randmat(dp - 1, 1.0))
        basis.append(np.column_stack((gi[i], ep[:, rest] @ q)))

    j = np.column_stack([np.kron(gi[i], el[:, i]) for i in range(2)])
    full_j = np.kron(np.eye(de), j)
    recovery = []
    for a in range(dp):
        ra = np.zeros((dp * da, dp * da), dtype=complex)
        for i in range(2):
            ra += np.kron(np.outer(gi[i], basis[i][:, a].conj()), np.outer(el[:, i], el[:, i]))
        recovery.append(ra)
    full_recovery = [np.kron(np.eye(de), ra) for ra in recovery]
    rsuper = sum(superoperator(ra) for ra in full_recovery)
    jsuper = superoperator(full_j)
    dsuper = superoperator(full_j.conj().T)

    physical_h = np.kron(h + omega * np.kron(np.eye(de), g), np.eye(da))
    physical_jumps = [np.kron(jump, np.eye(da)) for jump in jumps]
    physical_generator = gksl(physical_h, physical_jumps)
    projected_generator = dsuper @ rsuper @ physical_generator @ jsuper

    def block(operator: np.ndarray, bra: np.ndarray, ket: np.ndarray) -> np.ndarray:
        return np.einsum("p,epfq,q->ef", bra.conj(), operator.reshape(de, dp, de, dp), ket)

    effective_h = np.zeros((dlogical, dlogical), dtype=complex)
    for i in range(2):
        hii = block(h, gi[i], gi[i]) + omega * eigenvalues[i] * np.eye(de)
        effective_h += np.kron(hii, np.outer(el[:, i], el[:, i]))
    effective_jumps = []
    for jump in jumps:
        for a in range(dp):
            bar = np.zeros((dlogical, dlogical), dtype=complex)
            for i in range(2):
                bij = block(jump, basis[i][:, a], gi[i])
                bar += np.kron(bij, np.outer(el[:, i], el[:, i]))
            effective_jumps.append(bar)
    explicit_generator = gksl(effective_h, effective_jumps)

    completeness_residual = np.linalg.norm(sum(ra.conj().T @ ra for ra in recovery) - np.eye(dp * da))
    code_fixing_residual = np.linalg.norm(rsuper @ jsuper - jsuper)
    generator_residual = np.linalg.norm(projected_generator - explicit_generator)

    # Deliberately use one common basis: this destroys code coherence and must
    # not pass the same code-fixing condition.
    common_recovery = []
    for a in range(dp):
        ra = sum(np.kron(np.outer(gi[i], ep[:, a]), np.outer(el[:, i], el[:, i])) for i in range(2))
        common_recovery.append(ra)
    coherence = np.outer(j[:, 0], j[:, 1].conj())
    common_output = sum(ra @ coherence @ ra.conj().T for ra in common_recovery)

    t = 0.4
    target = expm(t * explicit_generator)
    convergence = []
    for m in (4, 8, 16, 32, 64):
        step = dsuper @ rsuper @ expm((t / m) * physical_generator) @ jsuper
        actual = np.linalg.matrix_power(step, m)
        error = float(np.linalg.norm(actual - target, ord=2))
        convergence.append({"microcycles": m, "hs_induced_error": error, "m_times_error": m * error})

    assert completeness_residual < 1e-12
    assert code_fixing_residual < 1e-12
    assert generator_residual < 1e-12
    assert np.linalg.norm(common_output) < 1e-12
    assert convergence[-1]["hs_induced_error"] < convergence[0]["hs_induced_error"] / 10

    result = {
        "seed": 20261103,
        "dimensions": {"environment": de, "probe": dp, "tag": da},
        "recovery_completeness_residual": float(completeness_residual),
        "code_fixing_residual": float(code_fixing_residual),
        "generator_identity_residual": float(generator_residual),
        "common_basis_code_coherence_output_norm": float(np.linalg.norm(common_output)),
        "finite_recovery_convergence": convergence,
        "norm_note": "Numerical finite-step errors use induced Hilbert--Schmidt norm, not diamond norm.",
    }
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results/control_checks.json")
    destination = parser.parse_args().output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
