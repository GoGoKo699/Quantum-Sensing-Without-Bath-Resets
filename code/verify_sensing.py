#!/usr/bin/env python3
"""Reproducible checks for sensing with a finite, unreset quantum environment.

Run from any working directory. The report is written to results/sensing_checks.json.
Exact finite-dimensional checks are assertions; Monte Carlo is diagnostic evidence.
Column vectorization, E tensor P tensor A ordering, and the usual Pauli Y are used.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)
PROJ = [np.diag([1.0, 0.0]), np.diag([0.0, 1.0])]
SEED = 20261103
TOL = 3e-11


def vec(a):
    return np.asarray(a).reshape(-1, order="F")


def unvec(a, d):
    return np.asarray(a).reshape((d, d), order="F")


def trace_row(d):
    return vec(np.eye(d)).conj()


def super_kraus(kraus):
    return sum(np.kron(k.conj(), k) for k in kraus)


def lindblad_super(h, jumps):
    d = h.shape[0]
    eye = np.eye(d)
    result = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    for jump in jumps:
        jj = jump.conj().T @ jump
        result += np.kron(jump.conj(), jump)
        result -= (np.kron(eye, jj) + np.kron(jj.T, eye)) / 2
    return result


def normalized_choi(channel, d):
    """Input tensor output convention; normalized Choi has trace one."""
    result = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            unit = np.zeros((d, d), dtype=complex)
            unit[i, j] = 1
            result += np.kron(unit, unvec(channel @ vec(unit), d)) / d
    return (result + result.conj().T) / 2


def kraus_from_super(channel, d):
    values, vectors = np.linalg.eigh(normalized_choi(channel, d))
    assert values.min() > -TOL, "instrument branch is not completely positive"
    return [np.sqrt(d * value) * unvec(vectors[:, i], d)
            for i, value in enumerate(values) if value > 1e-13]


def close(actual, expected, name, tolerance=TOL):
    error = float(np.linalg.norm(np.asarray(actual) - np.asarray(expected)))
    if error > tolerance:
        raise AssertionError(f"{name}: error {error:.3g} > {tolerance:.3g}")
    return error


def scalar_complex(z):
    return {"real": float(np.real(z)), "imag": float(np.imag(z))}


def native_unitaries(t=0.4):
    return expm(-1j * t * X / 2), expm(-1j * t * 1.3 * Z / 2)


def native_instrument(omega, t=0.4, sector_shift=0.0):
    u0, u1 = native_unitaries(t)
    theta = (omega + sector_shift) * t
    a0 = np.exp(-1j * theta / 2) * u0
    a1 = np.exp(1j * theta / 2) * u1
    branches = []
    for setting, coefficient in (("X", 1), ("Y", -1j)):
        for outcome in (1, -1):
            # 1/sqrt(2) is the classical setting probability, not a Born factor.
            k = (a0 + outcome * coefficient * a1) / (2 * np.sqrt(2))
            score = 2 * outcome if setting == "X" else -2j * outcome
            branches.append((setting, outcome, score, k))
    return branches


def instrument_maps(branches):
    maps = [np.kron(k.conj(), k) for _, _, _, k in branches]
    scores = [z for _, _, z, _ in branches]
    s = sum(maps)
    w = sum(z * m for z, m in zip(scores, maps))
    wbar = sum(np.conj(z) * m for z, m in zip(scores, maps))
    v2 = sum(abs(z) ** 2 * m for z, m in zip(scores, maps))
    return s, w, wbar, v2


def moment_path(branches, rho, checkpoints, effect=None):
    """Exact first and second moments, retaining the hidden environment state.

    a = sum_word score(word) rho_word and b = sum |score(word)|^2 rho_word.
    These are unnormalized operator sums, so conditional state normalization is
    neither performed nor approximated here.
    """
    s, w, wbar, v2 = instrument_maps(branches)
    d = rho.shape[0]
    tr = trace_row(d) if effect is None else vec(effect).conj()
    state = vec(rho)
    a = np.zeros_like(state)
    abar = np.zeros_like(state)
    b = np.zeros_like(state)
    wanted = set(checkpoints)
    result = {}
    for n in range(1, max(wanted) + 1):
        state, a, abar, b = (
            s @ state,
            s @ a + w @ state,
            s @ abar + wbar @ state,
            s @ b + wbar @ a + w @ abar + v2 @ state,
        )
        if n in wanted:
            result[n] = (complex(tr @ a), float(np.real(tr @ b)))
    return result


def enumerate_words(branches, rho, n):
    """Independent, direct tree enumeration for small n."""
    paths = [(0j, rho)]
    for _ in range(n):
        paths = [
            (score + z, k @ state @ k.conj().T)
            for score, state in paths
            for _, _, z, k in branches
        ]
    probabilities = np.array([np.trace(state).real for _, state in paths])
    scores = np.array([score for score, _ in paths])
    return {
        "mean": np.sum(probabilities * scores),
        "second": np.sum(probabilities * abs(scores) ** 2),
        "probabilities": probabilities,
    }


def centered_second(mean, second, n, mu, mass=1.0):
    return float(second - 2 * np.real(n * np.conj(mu) * mean) + n * n * abs(mu) ** 2 * mass)


def native_exact_checks():
    t, omega = 0.4, 0.27
    u0, u1 = native_unitaries(t)
    branches = native_instrument(omega, t)
    s, w, wbar, v2 = instrument_maps(branches)
    tau = I2 / 2
    tr = trace_row(2)
    c = np.trace(u1.conj().T @ u0) / 2
    mu = c * np.exp(-1j * omega * t)
    errors = {}
    errors["analytic_c"] = close(c, np.cos(0.2) * np.cos(0.26), "analytic c")
    errors["kraus_completeness"] = close(
        sum(k.conj().T @ k for _, _, _, k in branches), I2, "Kraus completeness"
    )
    expected_s = (np.kron(u0.conj(), u0) + np.kron(u1.conj(), u1)) / 2
    errors["averaged_channel"] = close(s, expected_s, "averaged hidden channel")
    errors["score_map_sign"] = close(
        w, np.exp(-1j * omega * t) * np.kron(u1.conj(), u0), "complex score map"
    )
    errors["second_score_map"] = close(v2, 4 * s, "second score map")
    errors["stationarity"] = close(s @ vec(tau), vec(tau), "stationarity")
    errors["parameter_independence"] = max(
        close(instrument_maps(native_instrument(q, t))[0], s, "parameter independence")
        for q in (-0.9, 0, 0.83)
    )

    # Compare every branch with a full EP Hamiltonian and a partial trace.
    h = np.kron(X / 2, PROJ[0]) + np.kron(1.3 * Z / 2, PROJ[1])
    h += omega * np.kron(I2, Z / 2)
    joint_u = expm(-1j * t * h)
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    rho = (I2 + 0.21 * X - 0.36 * Y + 0.47 * Z) / 2
    joint = joint_u @ np.kron(rho, np.outer(plus, plus.conj())) @ joint_u.conj().T
    full_errors = []
    for setting, outcome, _, k in branches:
        ket = np.array([1, outcome if setting == "X" else 1j * outcome]) / np.sqrt(2)
        projection = np.kron(I2, np.outer(ket, ket.conj()))
        post = projection @ joint @ projection / 2
        bath = np.einsum("apbp->ab", post.reshape(2, 2, 2, 2))
        full_errors.append(close(bath, k @ rho @ k.conj().T, "full EP branch"))
    errors["full_unitary_partial_trace"] = max(full_errors)

    enumeration = enumerate_words(branches, rho, 5)
    path_five = moment_path(branches, rho, [5])[5]
    errors["enumerated_mass"] = close(enumeration["probabilities"].sum(), 1, "word mass")
    errors["enumerated_first_moment"] = close(enumeration["mean"], path_five[0], "word mean")
    errors["enumerated_second_moment"] = close(enumeration["second"], path_five[1], "word variance")

    eigenvalues = np.linalg.eigvals(s)
    peripheral = np.sum(abs(eigenvalues - 1) < 1e-10)
    radius = max(abs(q) for q in eigenvalues if abs(q - 1) > 1e-10)
    assert peripheral == 1 and radius < 1 - 1e-3
    projector = np.outer(vec(tau), tr)
    reduced_resolvent = np.linalg.solve(np.eye(4) - s + projector, np.eye(4) - projector)
    covariance_sum = tr @ wbar @ reduced_resolvent @ w @ vec(tau)
    asymptotic_variance = float(4 - abs(mu) ** 2 + 2 * np.real(covariance_sum))
    tangent_scores = [-np.imag(np.exp(1j * omega * t) * z) / (t * c.real)
                      for _, _, z, _ in branches]
    outcome_maps = [np.kron(k.conj(), k) for _, _, _, k in branches]
    tangent_map = sum(a * m for a, m in zip(tangent_scores, outcome_maps))
    tangent_second_map = sum(a**2 * m for a, m in zip(tangent_scores, outcome_maps))
    tangent_variance = float(np.real(tr @ tangent_second_map @ vec(tau)
                            + 2 * tr @ tangent_map @ reduced_resolvent @ tangent_map @ vec(tau)))
    first_covariance = tr @ wbar @ w @ vec(tau) - abs(mu) ** 2
    assert abs(first_covariance) > 1e-3, "example must have genuine memory correlations"
    checkpoints = [64, 256, 1024, 4096, 16384]
    stationary_moments = moment_path(branches, tau, checkpoints)
    nonstationary = moment_path(branches, (I2 + Y) / 2, checkpoints)
    moment_rows = []
    for n in checkpoints:
        m, second = stationary_moments[n]
        var = centered_second(m, second, n, mu)
        m_ns, second_ns = nonstationary[n]
        moment_rows.append({
            "N": n,
            "stationary_variance_over_N": var / n,
            "nonstationary_centered_second_over_N": centered_second(m_ns, second_ns, n, mu) / n,
            "nonstationary_mean_bias": scalar_complex(m_ns / n - mu),
        })
    assert abs(moment_rows[-1]["stationary_variance_over_N"] - asymptotic_variance) < 0.01
    return {
        "parameters": {"t": t, "omega": omega, "H0_X_coefficient": 0.5, "H1_Z_coefficient": 0.65},
        "commutator_frobenius_norm": float(np.linalg.norm((X / 2) @ (1.3 * Z / 2) - (1.3 * Z / 2) @ (X / 2))),
        "coherence_c": scalar_complex(c),
        "uniform_coherence_distance_bound": float(2 * np.sin(0.1) + 2 * np.sin(0.13)),
        "hidden_channel_eigenvalues": [scalar_complex(q) for q in eigenvalues],
        "nontrivial_spectral_radius": float(radius),
        "lag_one_complex_covariance": scalar_complex(first_covariance),
        "iid_complex_variance": float(4 - abs(mu) ** 2),
        "asymptotic_complex_variance": asymptotic_variance,
        "linearized_local_estimator_variance_coefficient": tangent_variance,
        "finite_N_exact_moments": moment_rows,
        "residuals": errors,
    }


def dissipative_instrument(omega, t=0.4, gamma=0.2):
    """Build outcome maps from a full EP Lindblad evolution, not block formulas."""
    h = np.kron(X / 2, PROJ[0]) + np.kron(1.3 * Z / 2, PROJ[1])
    h += omega * np.kron(I2, Z / 2)
    full = expm(t * lindblad_super(h, [np.sqrt(gamma) * np.kron(Y, I2)]))
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    branches = []
    for setting in ("X", "Y"):
        for outcome in (1, -1):
            ket = np.array([1, outcome if setting == "X" else 1j * outcome]) / np.sqrt(2)
            projection = np.kron(I2, np.outer(ket, ket.conj()))
            branch_map = np.zeros((4, 4), dtype=complex)
            for column in range(4):
                unit = unvec(np.eye(4)[:, column], 2)
                joint = unvec(full @ vec(np.kron(unit, np.outer(plus, plus.conj()))), 4)
                post = projection @ joint @ projection / 2
                branch_map[:, column] = vec(np.einsum("apbp->ab", post.reshape(2, 2, 2, 2)))
            score = 2 * outcome if setting == "X" else -2j * outcome
            for k in kraus_from_super(branch_map, 2):
                branches.append((setting, outcome, score, k))
    return branches


def dissipative_native_checks():
    t, omega, gamma = 0.4, 0.27, 0.2
    tau = I2 / 2
    branches = dissipative_instrument(omega, t, gamma)
    s, w, wbar, v2 = instrument_maps(branches)
    k0 = lindblad_super(X / 2, [np.sqrt(gamma) * Y])
    k1 = lindblad_super(1.3 * Z / 2, [np.sqrt(gamma) * Y])
    expected_s = (expm(t * k0) + expm(t * k1)) / 2
    offdiagonal_generator = -1j * (np.kron(I2, X / 2) - np.kron((1.3 * Z / 2).T, I2))
    offdiagonal_generator += gamma * (np.kron(Y.conj(), Y) - np.eye(4))
    coherence = expm(t * offdiagonal_generator)
    tr = trace_row(2)
    c = tr @ coherence @ vec(tau)
    mu = c * np.exp(-1j * omega * t)
    # Tr C(rho)=Tr(F rho), where F is the transpose of the row functional.
    # ||F-I|| bounds |Tr C(rho)-1| for every initial bath state.
    f = unvec(tr @ coherence, 2).T
    coherence_response_bound = float(np.linalg.norm(f - I2, ord=2))
    analytic_response_bound = float(t * np.linalg.norm(X / 2 - 1.3 * Z / 2, ord=2))
    assert coherence_response_bound < 0.5
    assert analytic_response_bound < 0.5
    errors = {
        "full_lindblad_vs_population_blocks": close(s, expected_s, "dissipative population blocks"),
        "full_lindblad_vs_coherence_block": close(w, np.exp(-1j * omega * t) * coherence, "dissipative coherence block"),
        "stationarity": close(s @ vec(tau), vec(tau), "dissipative stationarity"),
        "trace_preservation": close(tr @ s, tr, "dissipative hidden TP"),
        "second_score_map": close(v2, 4 * s, "dissipative second score map"),
        "parameter_independence": close(instrument_maps(dissipative_instrument(-0.61, t, gamma))[0], s,
                                        "dissipative parameter independence"),
    }
    # Multiple Kraus terms per observed outcome are intentionally unobserved.
    # Summing the direct Kraus tree is still the physical outcome moment.
    rho = (I2 + Y) / 2
    enumeration = enumerate_words(branches, rho, 3)
    exact_three = moment_path(branches, rho, [3])[3]
    errors["enumerated_first_moment"] = close(enumeration["mean"], exact_three[0], "dissipative enumerated mean")
    errors["enumerated_second_moment"] = close(enumeration["second"], exact_three[1], "dissipative enumerated variance")
    projector = np.outer(vec(tau), tr)
    reduced_resolvent = np.linalg.solve(np.eye(4) - s + projector, np.eye(4) - projector)
    variance = float(4 - abs(mu)**2 + 2 * np.real(tr @ wbar @ reduced_resolvent @ w @ vec(tau)))
    eigenvalues = np.linalg.eigvals(s)
    radius = max(abs(q) for q in eigenvalues if abs(q - 1) > 1e-10)
    assert sum(abs(eigenvalues - 1) < 1e-10) == 1 and radius < 1 - 1e-3
    checkpoints = [64, 256, 1024, 4096]
    moments = moment_path(branches, tau, checkpoints)
    rows = [{"N": n, "stationary_variance_over_N": centered_second(*moments[n], n, mu) / n}
            for n in checkpoints]
    assert abs(rows[-1]["stationary_variance_over_N"] - variance) < 0.01
    return {"parameters": {"t": t, "omega": omega, "gamma": gamma},
            "coherence_c": scalar_complex(c),
            "uniform_response_distance_bound": coherence_response_bound,
            "analytic_uniform_response_distance_bound": analytic_response_bound,
            "hidden_channel_eigenvalues": [scalar_complex(q) for q in eigenvalues],
            "nontrivial_spectral_radius": float(radius),
            "iid_complex_variance": float(4 - abs(mu)**2),
            "asymptotic_complex_variance": variance,
            "finite_N_exact_moments": rows, "residuals": errors}


def nearest_arc_estimator(z, coefficients, t, interval):
    """Exact nearest point on a finite union of short circular arcs.

    Each arc is c_j exp(-i t omega) on the supplied interval. The additional
    angle representatives handle the branch cut of Arg, including boundary data.
    """
    z = np.asarray(z)
    coefficients = np.asarray(coefficients)
    raw = -np.angle(z[:, None] / coefficients[None, :]) / t
    candidates = raw[:, :, None] + (2 * np.pi / t) * np.arange(-1, 2)[None, None, :]
    candidates = np.clip(candidates, interval[0], interval[1])
    points = coefficients[None, :, None] * np.exp(-1j * t * candidates)
    distances = abs(z[:, None, None] - points) ** 2
    selected = np.argmin(distances.reshape(len(z), -1), axis=1)
    return candidates.reshape(len(z), -1)[np.arange(len(z)), selected]


def estimator_checks():
    c = np.cos(0.2) * np.cos(0.26)
    coefficients = np.array([c, c * np.exp(-0.36j)])
    truths = np.tile(np.array([-0.2, -0.13, 0.0, 0.07, 0.2]), 2)
    signals = np.repeat(coefficients, 5) * np.exp(-0.4j * truths)
    estimates = nearest_arc_estimator(signals, coefficients, 0.4, (-0.2, 0.2))
    error = close(estimates, truths, "noiseless finite-arc inversion")
    zero_result = nearest_arc_estimator(np.array([0j]), coefficients, 0.4, (-0.2, 0.2))
    assert np.all(np.isfinite(zero_result)) and np.all(abs(zero_result) <= 0.2)
    return {"noiseless_arc_inversion_residual": error, "zero_empirical_mean_estimate": float(zero_result[0])}


def simulate_records(omega, shifts, coefficients, interval, checkpoints, trajectories, seed):
    """Pure-state quantum trajectories: the bath is carried between every round."""
    rng = np.random.default_rng(seed)
    t = 0.4
    u0, u1 = native_unitaries(t)
    shifts = np.broadcast_to(shifts, (trajectories,))
    phases = (omega + shifts) * t
    p0 = np.exp(-0.5j * phases)[:, None]
    p1 = np.exp(0.5j * phases)[:, None]
    state = np.tile(np.array([1, 1j]) / np.sqrt(2), (trajectories, 1))
    score = np.zeros(trajectories, dtype=complex)
    rows = []
    max_norm_error = 0.0
    wanted = set(checkpoints)
    for n in range(1, max(wanted) + 1):
        use_y = rng.integers(0, 2, trajectories).astype(bool)
        setting_coefficient = np.where(use_y, -1j, 1)[:, None]
        arm0 = p0 * (state @ u0.T)
        arm1 = p1 * (state @ u1.T)
        plus = (arm0 + setting_coefficient * arm1) / 2
        minus = (arm0 - setting_coefficient * arm1) / 2
        probability_plus = np.sum(abs(plus) ** 2, axis=1)
        probability_minus = np.sum(abs(minus) ** 2, axis=1)
        max_norm_error = max(max_norm_error, float(np.max(abs(probability_plus + probability_minus - 1))))
        positive = rng.random(trajectories) < probability_plus
        probability = np.where(positive, probability_plus, probability_minus)
        state = np.where(positive[:, None], plus, minus) / np.sqrt(probability[:, None])
        outcome = np.where(positive, 1, -1)
        score += np.where(use_y, -2j * outcome, 2 * outcome)
        if n in wanted:
            estimate = nearest_arc_estimator(score / n, coefficients, t, interval)
            squared_error = (estimate - omega) ** 2
            c = np.cos(0.2) * np.cos(0.26)
            sector_mean = c * np.exp(-1j * phases)
            centered_score = abs(score / n - sector_mean) ** 2
            rows.append({
                "N": n,
                "mse": float(np.mean(squared_error)),
                "mse_standard_error": float(np.std(squared_error, ddof=1) / np.sqrt(trajectories)),
                "N_times_mse": float(n * np.mean(squared_error)),
                "N_times_sector_centered_score_second": float(n * np.mean(centered_score)),
                "empirical_score_mean": scalar_complex(np.mean(score / n)),
            })
    return {"seed": seed, "trajectories": trajectories, "omega": omega, "interval": list(interval),
            "max_probability_normalization_error": max_norm_error, "rows": rows}


def reducible_and_noiseless_checks():
    t, omega, probability, shift = 0.4, 0.07, 0.35, 0.9
    tau = I2 / 2
    c = np.cos(0.2) * np.cos(0.26)
    mus = [c * np.exp(-1j * t * (omega + s)) for s in (0, shift)]
    checkpoints = [64, 256, 1024, 4096, 16384]
    moments = [moment_path(native_instrument(omega, t, s), tau, checkpoints) for s in (0, shift)]
    weights = [probability, 1 - probability]
    rows = []
    for n in checkpoints:
        mean = sum(p * m[n][0] for p, m in zip(weights, moments))
        second = sum(p * m[n][1] for p, m in zip(weights, moments))
        sector_centered = sum(p * centered_second(m[n][0], m[n][1], n, mu)
                              for p, m, mu in zip(weights, moments, mus))
        rows.append({"N": n, "ordinary_mean_variance": float((second - abs(mean) ** 2) / n**2),
                     "N_times_sector_centered_mean_second": float(sector_centered / n)})
    variance_floor = probability * (1 - probability) * abs(mus[0] - mus[1]) ** 2
    assert variance_floor > 0.01
    assert abs(rows[-1]["ordinary_mean_variance"] - variance_floor) < 0.002

    # A conserved sector can initially be coherent. No outcome distinguishes it
    # from its dephasing, because all instrument Kraus operators are block diagonal.
    b0 = native_instrument(omega, t, 0)
    b1 = native_instrument(omega, t, shift)
    block_branches = [(setting, y, z, np.kron(PROJ[0], k0) + np.kron(PROJ[1], k1))
                      for (setting, y, z, k0), (_, _, _, k1) in zip(b0, b1)]
    sector_ket = np.sqrt(np.array(weights))
    coherent_rho = np.kron(np.outer(sector_ket, sector_ket), tau)
    incoherent_rho = np.kron(np.diag(weights), tau)
    central_error = close(enumerate_words(block_branches, coherent_rho, 4)["probabilities"],
                          enumerate_words(block_branches, incoherent_rho, 4)["probabilities"],
                          "coherent conserved sectors")

    # Noiseless factor A tensor mixing factor B. Two orthogonal entangled states
    # with the same B marginal must have exactly the same entire record law.
    spectator = [(setting, y, z, np.kron(I2, k)) for setting, y, z, k in b0]
    bell_plus = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    bell_minus = np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)
    spectator_error = close(
        enumerate_words(spectator, np.outer(bell_plus, bell_plus.conj()), 4)["probabilities"],
        enumerate_words(spectator, np.outer(bell_minus, bell_minus.conj()), 4)["probabilities"],
        "noiseless spectator invisibility",
    )
    return {"sector_weight": probability, "sector_hamiltonian_shift": shift,
            "sector_coefficients": [scalar_complex(c * np.exp(-1j * t * s)) for s in (0, shift)],
            "ordinary_mean_variance_limit": float(variance_floor), "exact_moment_rows": rows,
            "coherent_sector_record_residual": central_error,
            "noiseless_spectator_record_residual": spectator_error}


def transient_absorption_checks():
    """A three-state hidden instrument independently tests harmonic-effect labels.

    State order is transient, recurrent 0, recurrent 1. This is a finite-instrument
    statistics example, not an additional continuous-time sensing realization.
    """
    absorption, p, omega, t = 0.23, 0.35, 0.07, 0.4
    q = 1 - absorption
    amplitudes = np.array([0.85 * np.exp(0.2j), 0.9, 0.9 * np.exp(-0.36j)])
    means = amplitudes * np.exp(-1j * omega * t)
    transitions = []
    for destination, source, probability in ((0, 0, q), (1, 0, absorption * p),
                                             (2, 0, absorption * (1 - p)), (1, 1, 1), (2, 2, 1)):
        k = np.zeros((3, 3), dtype=complex)
        k[destination, source] = np.sqrt(probability)
        transitions.append((destination, k))
    branches = []
    for setting in ("X", "Y"):
        for outcome in (1, -1):
            score = 2 * outcome if setting == "X" else -2j * outcome
            for destination, k in transitions:
                quadrature = means[destination].real if setting == "X" else -means[destination].imag
                joint_probability = (1 + outcome * quadrature) / 4
                branches.append((setting, outcome, score, np.sqrt(joint_probability) * k))
    s, _, _, _ = instrument_maps(branches)
    effects = [np.diag([p, 1, 0]), np.diag([1 - p, 0, 1])]
    rho = np.diag([1.0, 0, 0])
    errors = {"harmonic_absorption_effects": max(
        close(s.conj().T @ vec(effect), vec(effect), "harmonic absorption effect") for effect in effects),
        "effects_sum_to_identity": close(sum(effects), np.eye(3), "absorption partition")}
    checkpoints = [16, 64, 256, 1024, 4096]
    weighted = [moment_path(branches, rho, checkpoints, effect) for effect in effects]
    rows = []
    for n in checkpoints:
        total = 0.0
        for j, weight in enumerate((p, 1 - p)):
            mean, second = weighted[j][n]
            analytic_mean = weight * (n * means[j + 1] + (means[0] - means[j + 1]) * q * (1 - q**n) / (1 - q))
            close(mean, analytic_mean, "absorption-weighted first moment", tolerance=2e-8)
            total += centered_second(mean, second, n, means[j + 1], mass=weight)
        rows.append({"N": n, "N_times_absorption_weighted_centered_mean_second": total / n})
    expected_limit = 4 - 0.9**2
    assert abs(rows[-1]["N_times_absorption_weighted_centered_mean_second"] - expected_limit) < 0.005
    return {"absorption_probability_per_round": absorption, "sector_0_absorption_weight": p,
            "initial_state": "entirely transient", "expected_large_N_limit": expected_limit,
            "finite_N_rows": rows, "residuals": errors}


def recovery_normal_form_checks():
    omega, duration = 0.37, 0.6
    h_ep = (0.43 * np.kron(X, X) + 0.29 * np.kron(Z, Y)
            + 0.31 * np.kron(Y, Z) + 0.17 * np.kron(Z, I2) + 0.11 * np.kron(I2, X))
    jumps_ep = [np.sqrt(0.19) * (np.kron(X, LOWER) + 0.3 * np.kron(Z, Z)),
                np.sqrt(0.13) * (np.kron(LOWER, Y) + 0.2 * np.kron(I2, X))]
    h_full = np.kron(h_ep + omega * np.kron(I2, Z / 2), I2)
    jumps_full = [np.kron(jump, I2) for jump in jumps_ep]
    l_full = lindblad_super(h_full, jumps_full)

    # Physical order E,P,A and logical order E,L.
    embedding = np.zeros((8, 4), dtype=complex)
    for e in range(2):
        for i in range(2):
            embedding[4 * e + 3 * i, 2 * e + i] = 1
    r0 = np.diag([1.0, 0, 0, 1.0]).astype(complex)
    r1 = np.zeros((4, 4), dtype=complex)
    r1[0, 2] = r1[3, 1] = 1
    recovery = super_kraus([np.kron(I2, r) for r in (r0, r1)])
    encode = np.kron(embedding.conj(), embedding)
    decode = np.kron(embedding.T, embedding.conj().T)
    errors = {
        "recovery_trace_preservation": close(r0.conj().T @ r0 + r1.conj().T @ r1, np.eye(4), "recovery TP"),
        "recovery_idempotence": close(recovery @ recovery, recovery, "recovery idempotence"),
        "code_fixed": close(recovery @ encode, encode, "code fixed"),
    }

    # Independently construct the claimed normal form from physical matrix elements.
    h_blocks = h_ep.reshape(2, 2, 2, 2)
    h_eff = sum(np.kron(h_blocks[:, i, :, i], PROJ[i]) for i in range(2))
    h_eff += omega * np.kron(I2, Z / 2)
    jumps_eff = []
    for jump in jumps_ep:
        blocks = jump.reshape(2, 2, 2, 2)
        for syndrome in range(2):
            branch0 = blocks[:, syndrome, :, 0]
            branch1 = blocks[:, 1 - syndrome, :, 1]
            jumps_eff.append(np.kron(branch0, PROJ[0]) + np.kron(branch1, PROJ[1]))
    l_eff = lindblad_super(h_eff, jumps_eff)
    errors["full_vs_normal_form_generator"] = close(
        decode @ recovery @ l_full @ encode, l_eff, "recovered generator normal form"
    )
    errors["effective_generator_trace_preservation"] = close(trace_row(4) @ l_eff, np.zeros(16), "effective generator TP")
    ideal = expm(duration * l_eff)
    ideal_choi = normalized_choi(ideal, 4)
    assert np.linalg.eigvalsh(ideal_choi).min() > -TOL
    rows = []
    for pulses in (4, 8, 16, 32, 64):
        delta = duration / pulses
        one_step = decode @ recovery @ expm(delta * l_full) @ encode
        finite = np.linalg.matrix_power(one_step, pulses)
        finite_choi = normalized_choi(finite, 4)
        tp_error = close(trace_row(4) @ finite, trace_row(4), "finite recovery TP")
        minimum_eigenvalue = float(np.linalg.eigvalsh(finite_choi).min())
        assert minimum_eigenvalue > -TOL
        rows.append({"recoveries": pulses, "spacing": delta,
                     "superoperator_frobenius_error": float(np.linalg.norm(finite - ideal)),
                     "normalized_choi_trace_distance": float(np.sum(abs(np.linalg.eigvalsh(finite_choi - ideal_choi))) / 2),
                     "minimum_normalized_choi_eigenvalue": minimum_eigenvalue,
                     "trace_preservation_residual": tp_error})
    assert rows[-1]["superoperator_frobenius_error"] < rows[0]["superoperator_frobenius_error"] / 8
    return {"omega": omega, "fixed_total_exposure": duration, "residuals": errors,
            "finite_recovery_rows": rows,
            "interpretation": "Finite-dimensional convergence check, not a proof of a uniform diamond-norm bound."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results" / "sensing_checks.json")
    parser.add_argument("--skip-monte-carlo", "--skip-mc", action="store_true", help="Run deterministic checks only.")
    args = parser.parse_args()
    report = {
        "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "seed": SEED,
        "status": "all deterministic assertions passed",
        "native_noncommuting_example": native_exact_checks(),
        "native_dissipative_example": dissipative_native_checks(),
        "reducible_and_noiseless_examples": reducible_and_noiseless_checks(),
        "transient_absorption_example": transient_absorption_checks(),
        "finite_recovery_normal_form": recovery_normal_form_checks(),
        "estimator_checks": estimator_checks(),
    }
    if not args.skip_monte_carlo:
        c = np.cos(0.2) * np.cos(0.26)
        checkpoints = [128, 512, 2048, 8192]
        report["native_monte_carlo"] = simulate_records(
            omega=0.27, shifts=0, coefficients=[c], interval=(-0.8, 0.8),
            checkpoints=checkpoints, trajectories=2048, seed=SEED,
        )
        rng = np.random.default_rng(SEED + 1)
        shifts = np.where(rng.random(1024) < 0.35, 0, 0.9)
        report["reducible_monte_carlo"] = simulate_records(
            omega=0.07, shifts=shifts, coefficients=[c, c * np.exp(-0.36j)], interval=(-0.2, 0.2),
            checkpoints=checkpoints, trajectories=1024, seed=SEED + 2,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{report['status']}; report: {args.output}")
    native = report["native_noncommuting_example"]
    print(f"Native c={native['coherence_c']['real']:.9f}; asymptotic score variance={native['asymptotic_complex_variance']:.9f}")
    if "native_monte_carlo" in report:
        print("Native N*MSE:", [round(row["N_times_mse"], 6) for row in report["native_monte_carlo"]["rows"]])


if __name__ == "__main__":
    main()
