#!/usr/bin/env python3
"""Run the finite scientific checks; optionally omit trajectory diagnostics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-monte-carlo", action="store_true",
                        help="Run every deterministic check, omitting seeded trajectory diagnostics.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sensing = [sys.executable, str(root / "code/verify_sensing.py")]
    if args.skip_monte_carlo:
        sensing.append("--skip-monte-carlo")
    commands = [
        ("finite-memory instrument, moments, and estimator", sensing),
        ("three-level probe conditional recovery", [sys.executable,
         str(root / "verification/check_control_normal_form.py")]),
    ]
    for name, command in commands:
        result = subprocess.run(command, cwd=root, text=True, capture_output=True)
        if result.returncode:
            sys.stdout.write(result.stdout)
            sys.stderr.write(result.stderr)
            raise SystemExit(result.returncode)
        print(f"PASS: {name}")
    for name in ("sensing_checks.json", "control_checks.json"):
        path = root / "results" / name
        json.loads(path.read_text())
        print(f"Report: results/{name}")
    print("Finite checks complete. General risk and resource bounds are proved in science/.")


if __name__ == "__main__":
    main()
