#!/usr/bin/env python3
"""
oscillator_phase_gate_demo.py

Minimal numerical instantiation of the Σ₂ toy system:
- phase-gated dynamics
- noncommutativity (T1)
- same x, different future (T3)

Dependencies: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters (dimensionless)
# -----------------------------
alpha = 1.0      # baseline relaxation
beta = 3.0       # gated drive
gamma = 0.5      # gated saturation
omega = 2 * np.pi
sigma = 0.2      # gate width
phi0 = 0.0       # gate center

dt = 0.001
T = 3.0          # simulation duration
steps = int(T / dt)

noise_x = 0.0
noise_phi = 0.0

# transformation magnitudes
DELTA_PHI = 0.6
DELTA_X = 0.6

# -----------------------------
# Helper functions
# -----------------------------
def wrap(phi):
    return (phi + np.pi) % (2 * np.pi) - np.pi

def gate(phi):
    d = wrap(phi - phi0)
    return np.exp(-(d ** 2) / (2 * sigma ** 2))

def simulate(x0, phi0_init):
    x = x0
    phi = phi0_init
    xs = np.zeros(steps)
    phis = np.zeros(steps)

    for i in range(steps):
        g = gate(phi)
        dx = -alpha * x + g * (beta - gamma * x)
        dphi = omega

        x += dx * dt + noise_x * np.random.randn()
        phi = wrap(phi + dphi * dt + noise_phi * np.random.randn())

        xs[i] = x
        phis[i] = phi

    return xs, phis

# -----------------------------
# Test T1: Noncommutativity
# -----------------------------
x0 = 0.0
phi_init = -1.0  # chosen so phase shift can move system into gate

# τ2 ∘ τ1
phi_A = wrap(phi_init + DELTA_PHI)
x_A = x0 + DELTA_X
xs_A, _ = simulate(x_A, phi_A)

# τ1 ∘ τ2
phi_B = wrap(phi_init)
x_B = x0 + DELTA_X
xs_B, _ = simulate(x_B, wrap(phi_B + DELTA_PHI))

out_A = xs_A[-1]
out_B = xs_B[-1]

print("T1 Noncommutativity Test")
print(f"Outcome(τ2 ∘ τ1) = {out_A:.3f}")
print(f"Outcome(τ1 ∘ τ2) = {out_B:.3f}")
print("PASS" if abs(out_A - out_B) > 0.1 else "FAIL")

# -----------------------------
# Test T3: Same x, different future
# -----------------------------
phi_A = -0.2
phi_B = +0.2

xs1, _ = simulate(x0, phi_A)
xs2, _ = simulate(x0, phi_B)

diff = abs(xs1[-1] - xs2[-1])

print("\nT3 Same x, Different Future Test")
print(f"x_final(history A) = {xs1[-1]:.3f}")
print(f"x_final(history B) = {xs2[-1]:.3f}")
print("PASS" if diff > 0.1 else "FAIL")

# -----------------------------
# Visualization
# -----------------------------
t = np.linspace(0, T, steps)

plt.figure(figsize=(10, 4))
plt.plot(t, xs1, label="History A (φ = -0.2)")
plt.plot(t, xs2, label="History B (φ = +0.2)")
plt.xlabel("time")
plt.ylabel("x")
plt.title("T3: Same x, Different Future")
plt.legend()
plt.tight_layout()
plt.show()