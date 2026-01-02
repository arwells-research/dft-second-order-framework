import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Toy MD Viability Sampling (Σ₂ ground-truth test) — single file
#
# Track 1: widen gate to boost event rate (cleanest signal)
# Adds:
#  - angdiff + consistent half-width gate convention
#  - rich instrumentation (p_cross, gate_occupancy, p_cross_in_gate, p_adm)
#  - CRN proto vs true comparisons
#  - τ1/τ2 noncommutativity harness
#  - phase coherence order parameter R = |<exp(i phi)>|
#  - linger_steps is now actually honored (>=2)
#  - coupling_mode toggle for a more physical drift-bias variant
#
# Notes:
#  - "Dissipation" remains a labeled proxy (gamma * v^2 dt).
#  - "Maintenance cost" is ∫ u(t)^2 dt where u is control angular-velocity correction.
# ============================================================

# -----------------------------
# Parameters (edit here)
# -----------------------------
dt = 0.02
T = 20.0
N_traj = 500
gamma = 1.0
kT = 1.0

D_phi = 0.1
omega = 1.0

gate_center = np.pi
gate_width = 0.5               # FULL width (Track 1)
gate_half_width = gate_width / 2.0

barrier_high = 0.25
barrier_low = 0.025

feedback_strength = 0.5        # true-regime stabilization gain

# Coupling mode:
#   "impulse"    = original toy saddle kick (keeps your current behavior)
#   "drift_bias" = gate-conditioned drift bias near saddle (more defensible)
coupling_mode = "impulse"

# Impulse region (toy saddle neighborhood)
saddle_band = 0.5

# Drift-bias parameters (only used if coupling_mode="drift_bias")
k_gate = 0.8                   # strength of conditional drift toward saddle
w_gate = 0.5                   # width of localized saddle coupling

# Linger rule: require in-gate at crossing and for the next (linger_steps-1) steps
linger_steps = 2               # >=2 (2 means i and i+1)

# Noncommutativity harness defaults
i_star_frac = 0.50
tau1_phase_shift = 0.6         # Δ (radians)
tau2_x_impulse = 0.25          # δ (position units)

# Reproducibility
BASE_SEED = 12345


# -----------------------------
# Helpers
# -----------------------------
def potential(x):
    return 0.25 * (x**2 - 1)**2

def force(x):
    return - (x**3 - x)

def angdiff(a, b):
    return (a - b + np.pi) % (2*np.pi) - np.pi

def in_gate(phi):
    return abs(angdiff(phi, gate_center)) < gate_half_width

def gate_barrier(phi):
    return barrier_low if in_gate(phi) else barrier_high


# -----------------------------
# Noise pre-generation (CRN)
# -----------------------------
def pregenerate_noise(N, t_steps, seed=BASE_SEED):
    rng = np.random.default_rng(seed)
    z_x = rng.standard_normal((N, t_steps - 1))
    z_phi = rng.standard_normal((N, t_steps - 1))
    s_imp = rng.choice(np.array([-1.0, 1.0]), size=(N, t_steps - 1))
    phi0 = rng.uniform(0.0, 2*np.pi, size=N)
    return {"z_x": z_x, "z_phi": z_phi, "s_imp": s_imp, "phi0": phi0}


# -----------------------------
# Trajectory simulation (instrumented)
# -----------------------------
def simulate_trajectory_from_noise(j, regime, noise, intervention=None):
    t_steps = int(T / dt)
    x = np.zeros(t_steps, dtype=float)
    phi = np.zeros(t_steps, dtype=float)

    diss = np.zeros(t_steps - 1, dtype=float)     # proxy
    maint = np.zeros(t_steps - 1, dtype=float)    # u^2 dt

    x[0] = -1.0
    phi[0] = float(noise["phi0"][j])

    crossed = False
    admissible = False
    cross_in_gate = False
    i_cross = None
    phi_cross = None

    # Intervention timing/order
    if intervention is not None:
        i_star = int(intervention["i_star"])
        order = intervention["order"]
        dphi_shift = float(intervention["delta_phi"])
        dx_impulse = float(intervention["delta_x"])
    else:
        i_star = None
        order = None
        dphi_shift = 0.0
        dx_impulse = 0.0

    for i in range(1, t_steps):
        # Apply intervention(s) at i_star BEFORE integrating step i (state-level)
        if (i_star is not None) and (i == i_star):
            if order == "tau2_then_tau1":
                x[i - 1] += dx_impulse
                phi[i - 1] = (phi[i - 1] + dphi_shift) % (2*np.pi)
            elif order == "tau1_then_tau2":
                phi[i - 1] = (phi[i - 1] + dphi_shift) % (2*np.pi)
                x[i - 1] += dx_impulse
            else:
                raise ValueError(f"Unknown intervention order: {order}")

        # --- x dynamics ---
        F = force(x[i - 1])

        if coupling_mode == "impulse":
            barrier = gate_barrier(phi[i - 1])
            if abs(x[i - 1]) < saddle_band:
                F += noise["s_imp"][j, i - 1] * barrier

        elif coupling_mode == "drift_bias":
            # Gate-conditioned drift toward saddle (x->0), localized near saddle
            if abs(x[i - 1]) < saddle_band and in_gate(phi[i - 1]):
                F += -k_gate * x[i - 1] * np.exp(-(x[i - 1] ** 2) / (w_gate ** 2))

        else:
            raise ValueError(f"Unknown coupling_mode: {coupling_mode}")

        dx = (F / gamma) * dt + np.sqrt(2 * kT * dt / gamma) * noise["z_x"][j, i - 1]
        x[i] = x[i - 1] + dx

        # --- phi dynamics ---
        dphi = omega * dt + np.sqrt(2 * D_phi * dt) * noise["z_phi"][j, i - 1]

        if regime == "true":
            phase_error = angdiff(phi[i - 1], gate_center)
            u = -feedback_strength * np.sin(phase_error)
            dphi += u * dt
            maint[i - 1] = (u * u) * dt

        phi[i] = (phi[i - 1] + dphi) % (2*np.pi)

        # --- dissipation proxy ---
        v_sq = (dx / dt) ** 2
        diss[i - 1] = gamma * v_sq * dt

        # --- crossing detection ---
        if (not crossed) and (np.sign(x[i]) != np.sign(x[i - 1])):
            crossed = True
            i_cross = i
            phi_cross = float(phi[i])
            cross_in_gate = bool(in_gate(phi[i]))

    # Linger check honoring linger_steps (>=2)
    if crossed and (i_cross is not None):
        ok = True
        if i_cross + (linger_steps - 1) < t_steps:
            for k in range(linger_steps):
                if not in_gate(phi[i_cross + k]):
                    ok = False
                    break
            admissible = ok
        else:
            admissible = False

    # Gate occupancy + coherence R for this trajectory
    gate_mask = np.abs(((phi - gate_center + np.pi) % (2*np.pi)) - np.pi) < gate_half_width
    gate_occ = float(np.mean(gate_mask))

    # Trajectory-level coherence: R_traj = |mean_t exp(i phi(t))|
    R_traj = float(np.abs(np.mean(np.exp(1j * phi))))

    return {
        "crossed": crossed,
        "admissible": admissible,
        "cross_in_gate": cross_in_gate,
        "i_cross": i_cross,
        "phi_cross": phi_cross,
        "gate_occupancy": gate_occ,
        "R_traj": R_traj,
        "diss_proxy": float(np.mean(diss)),
        "maint_cost": float(np.sum(maint)),
    }


# -----------------------------
# Ensemble runner
# -----------------------------
def run_ensemble(regime, noise, intervention=None):
    N = noise["phi0"].shape[0]

    crossed_ct = 0
    cross_in_gate_ct = 0
    admissible_ct = 0

    gate_occ_sum = 0.0
    R_sum = 0.0
    diss_sum = 0.0
    maint_sum = 0.0

    crossing_phases_adm = []

    for j in range(N):
        out = simulate_trajectory_from_noise(j, regime, noise, intervention=intervention)

        crossed_ct += int(out["crossed"])
        cross_in_gate_ct += int(out["cross_in_gate"])
        admissible_ct += int(out["admissible"])

        gate_occ_sum += out["gate_occupancy"]
        R_sum += out["R_traj"]
        diss_sum += out["diss_proxy"]
        maint_sum += out["maint_cost"]

        if out["admissible"] and (out["phi_cross"] is not None):
            crossing_phases_adm.append(out["phi_cross"] % (2*np.pi))

    return {
        "p_cross": crossed_ct / N,
        "p_cross_in_gate": cross_in_gate_ct / N,
        "p_adm": admissible_ct / N,
        "gate_occupancy": gate_occ_sum / N,
        "R_phi": R_sum / N,
        "avg_diss_proxy": diss_sum / N,
        "avg_maint": maint_sum / N,
        "admissible_cross_phases": crossing_phases_adm,
    }


def print_summary(label, res):
    print(
        f"{label}: "
        f"p_cross={res['p_cross']:.3f}, "
        f"gate_occ={res['gate_occupancy']:.3f}, "
        f"R_phi={res['R_phi']:.3f}, "
        f"p_cross_in_gate={res['p_cross_in_gate']:.3f}, "
        f"p_adm={res['p_adm']:.3f}, "
        f"avg_diss(proxy)={res['avg_diss_proxy']:.3f}, "
        f"avg_maint={res['avg_maint']:.4f}"
    )


# -----------------------------
# τ1/τ2 Noncommutativity harness
# -----------------------------
def noncommutativity_experiment(noise, regime):
    t_steps = int(T / dt)
    i_star = int(i_star_frac * (t_steps - 1))

    A = {
        "order": "tau2_then_tau1",
        "i_star": i_star,
        "delta_phi": tau1_phase_shift,
        "delta_x": tau2_x_impulse,
    }
    B = {
        "order": "tau1_then_tau2",
        "i_star": i_star,
        "delta_phi": tau1_phase_shift,
        "delta_x": tau2_x_impulse,
    }

    res_A = run_ensemble(regime, noise, intervention=A)
    res_B = run_ensemble(regime, noise, intervention=B)

    d_p_adm = res_A["p_adm"] - res_B["p_adm"]
    d_p_cig = res_A["p_cross_in_gate"] - res_B["p_cross_in_gate"]

    return res_A, res_B, d_p_adm, d_p_cig


# -----------------------------
# Main
# -----------------------------
def main():
    t_steps = int(T / dt)
    noise = pregenerate_noise(N_traj, t_steps, seed=BASE_SEED)

    print(f"\n[coupling_mode={coupling_mode}] gate_width={gate_width} linger_steps={linger_steps} N={N_traj}")

    proto = run_ensemble("proto", noise, intervention=None)
    true = run_ensemble("true", noise, intervention=None)

    print("\n=== Baseline (CRN-shared) ===")
    print_summary("Proto", proto)
    print_summary("True ", true)

    print("\nUplift (True - Proto):")
    print(f"  Δp_cross         = {true['p_cross'] - proto['p_cross']:+.4f}")
    print(f"  Δgate_occupancy  = {true['gate_occupancy'] - proto['gate_occupancy']:+.4f}")
    print(f"  ΔR_phi           = {true['R_phi'] - proto['R_phi']:+.4f}")
    print(f"  Δp_cross_in_gate = {true['p_cross_in_gate'] - proto['p_cross_in_gate']:+.4f}")
    print(f"  Δp_adm           = {true['p_adm'] - proto['p_adm']:+.4f}")
    print(f"  Δavg_maint       = {true['avg_maint'] - proto['avg_maint']:+.4f}")

    print("\n=== Noncommutativity (τ2∘τ1 vs τ1∘τ2) ===")
    resA_p, resB_p, dp_adm_p, dp_cig_p = noncommutativity_experiment(noise, "proto")
    print("\nProto:")
    print_summary(" τ2∘τ1", resA_p)
    print_summary(" τ1∘τ2", resB_p)
    print(f"  Δp_adm (τ2∘τ1 - τ1∘τ2) = {dp_adm_p:+.4f}")
    print(f"  Δp_cross_in_gate       = {dp_cig_p:+.4f}")

    resA_t, resB_t, dp_adm_t, dp_cig_t = noncommutativity_experiment(noise, "true")
    print("\nTrue:")
    print_summary(" τ2∘τ1", resA_t)
    print_summary(" τ1∘τ2", resB_t)
    print(f"  Δp_adm (τ2∘τ1 - τ1∘τ2) = {dp_adm_t:+.4f}")
    print(f"  Δp_cross_in_gate       = {dp_cig_t:+.4f}")

    # Visualization: admissible crossing phase histograms
    bins = np.linspace(0, 2*np.pi, 30)

    fig, axs = plt.subplots(1, 2, figsize=(11, 4))
    axs[0].hist(proto["admissible_cross_phases"], bins=bins, alpha=0.75)
    axs[0].axvline(gate_center, linestyle="--")
    axs[0].set_title("Proto: admissible crossing phases")
    axs[0].set_xlim(0, 2*np.pi)

    axs[1].hist(true["admissible_cross_phases"], bins=bins, alpha=0.75)
    axs[1].axvline(gate_center, linestyle="--")
    axs[1].set_title("True: admissible crossing phases")
    axs[1].set_xlim(0, 2*np.pi)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()