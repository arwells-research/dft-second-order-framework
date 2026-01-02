# Toy MD Viability Sampling as a Σ₂ Diagnostic

**File:** `toy_md_viability_sigma2.py`  
**Status:** Frozen baseline demonstration  
**Purpose:** Empirical grounding of Σ₂ (second-order) viability diagnostics in a minimal stochastic system

---

## 1. Motivation

Second-order organization (Σ₂) is characterized not by changes in first-order dynamics alone, but by **conditional accessibility**: the ability of trajectories to enter and persist within narrow viability-supporting manifolds, often at a nonzero maintenance cost.

This note documents a minimal stochastic toy model designed to demonstrate that Σ₂ diagnostics are **operational** rather than purely conceptual. The goal is not realism, but clarity: to show, in the simplest possible setting, how viability can increase without increasing base crossings, energy injection, or dissipation—while exhibiting path dependence, failure of Markov closure, and ordering sensitivity.

---

## 2. Toy system definition

A schematic overview of the toy system is shown in Fig. 1 (conceptual).

### 2.1 State variables

- **x(t):** overdamped Langevin coordinate in a symmetric double-well potential  
  \[
  V(x) = \tfrac14 (x^2 - 1)^2
  \]

- **φ(t):** angular phase variable undergoing rotation plus diffusion

### 2.2 Dynamics

- **x dynamics (overdamped):**
  \[
  \dot{x} = -\partial_x V(x) + \text{noise} + \text{gate-conditioned coupling}
  \]

- **φ dynamics:**
  \[
  \dot{\phi} = \omega + \sqrt{2D_\phi}\,\eta(t)
  \]
  with an optional weak stabilizing control in the “true” regime.

### 2.3 Phase gate

A narrow **viability gate** is defined near:
\[
\phi \approx \pi
\]

The gate does **not** directly force crossings. Instead, it modulates whether crossings that occur anyway become *admissible* via a temporal persistence (“linger”) requirement.

Abstractly, this gate structure is analogous to **conformational gating in molecular systems**, where energetic input is only productive within specific windows of an internal cycle.

Gate membership is defined via wrapped angular distance with a fixed half-width.

---

## 3. Proto vs true regimes

Two regimes are compared under **common random numbers (CRN)** to reduce variance:

### Proto (passive)
- φ evolves purely by rotation + diffusion
- No control input
- Zero maintenance cost

### True (stabilized)
- Weak feedback nudges φ toward the gate center
- Control input:
  \[
  u(\phi) = -k \sin(\phi - \phi_{\text{gate}})
  \]
- Nonzero maintenance cost:
  \[
  M = \int u(t)^2 \, dt
  \]

Importantly, the base x-dynamics and noise statistics are unchanged.

---

## 4. Admissibility and diagnostics

### 4.1 Crossing events

A **crossing** occurs when x(t) changes sign (between wells).

### 4.2 Admissible trajectories

A trajectory is **admissible** if:
1. A crossing occurs, **and**
2. The crossing occurs while φ is inside the gate, **and**
3. φ remains inside the gate for a minimum number of subsequent steps (“linger”).

This enforces **temporal coherence**, not just instantaneous coincidence.

### 4.3 Measured diagnostics

For each ensemble:

- **p_cross** — probability of any crossing  
- **gate_occupancy** — fraction of time φ spends in gate  
- **p_cross_in_gate** — probability that a crossing occurs while in gate  
- **p_adm** — probability of admissible crossing (cross + linger)  
- **avg_maint** — average maintenance cost  
- **avg_diss (proxy)** — overdamped dissipation proxy  
- **Rφ** — phase coherence order parameter:
  \[
  R_\phi = \left|\langle e^{i\phi} \rangle\right|
  \]

---

## 5. Baseline results (Track 1 settings)

Parameters:
- gate width = 0.5 rad (full width)
- N = 500 trajectories
- CRN shared between proto and true

Representative results:

| Metric | Proto | True | Δ (True − Proto) |
|------|------|------|------------------|
| p_cross | ≈ 0.44 | ≈ 0.45 | ≈ +0.01 |
| gate_occupancy | ≈ 0.08 | ≈ 0.19 | **+0.11** |
| p_cross_in_gate | ≈ 0.04 | ≈ 0.08 | **+0.05** |
| p_adm | ≈ 0.02 | ≈ 0.07 | **+0.04** |
| avg_maint | 0 | > 0 | **nonzero** |
| avg_diss (proxy) | ≈ same | ≈ same | ~0 |

Key observations:

- **Crossing probability remains nearly unchanged.**
- **Dissipation remains nearly unchanged.**
- **Viability increases exclusively via gate-mediated pathways.**
- **Maintenance cost is nonzero only in the stabilized regime.**

Notably, the observed increase in admissible probability satisfies the approximate decomposition:
\[
\Delta p_{\text{adm}} \;\approx\;
\Delta p_{\text{cross-in-gate}} \;\approx\;
p_{\text{cross}} \cdot \Delta(\text{gate occupancy}),
\]
which is a **direct structural prediction of the Σ₂ framework**: viability gains arise from increased conditional accessibility rather than amplification of base dynamics.

---

## 6. Ordering sensitivity (noncommutativity)

Two small interventions are applied at a fixed time:
- **τ₁:** phase shift (φ → φ + Δ)
- **τ₂:** position impulse (x → x + δ)

The order of application is swapped:
- τ₂ ∘ τ₁ vs τ₁ ∘ τ₂

Results:
- Admissible probability differs by order
- Effect persists under CRN
- Magnitude is small but structurally stable

Interpretation:
> Even when first-order state variables are nearly identical, **the order of operations alters future viability**.

Stabilization does not remove ordering sensitivity—it reshapes it.

---

## 7. Phase-diagram behavior and “sweet spot”

Sweeps over feedback strength and phase diffusion show:
- A bounded region of **moderate feedback + low diffusion** where:
  - viability gains are large,
  - maintenance cost is modest,
  - phase coherence Rφ rises sharply.

At higher feedback strengths:
- Viability continues to increase,
- but maintenance cost rises superlinearly.

This illustrates an **organizational closure tradeoff**: viability without brute-force energy injection exists only within a constrained parameter regime.

---

## 8. What this toy does—and does not—claim

**Does show:**
- Σ₂ diagnostics are measurable and operational
- Viability can increase without increasing base crossings or dissipation
- Maintenance cost is necessary for sustained access
- Path dependence and ordering sensitivity are unavoidable

**Does not claim:**
- Physical realism of the coupling mechanism
- Biological or molecular specificity
- Optimality or universality

The model is deliberately minimal and transparent.

---

## 9. Role within the broader framework

This toy serves as a **grounding artifact** for the Σ₂ framework:
- not a foundational proof,
- not a phenomenological model,
- but a concrete demonstration that the proposed diagnostics behave coherently in a controlled setting.

The accompanying theory paper references this toy as an existence proof, not as a central result.

---

## 10. Files

- `toy_md_viability_sigma2.py` — executable simulation  
- `toy_md_viability_sigma2_note.md` — this document