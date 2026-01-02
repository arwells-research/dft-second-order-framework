# Toy System: Oscillator With Phase-Gated Dynamics

**Document role:** Concrete toy model for T1–T3 tests  
**Status:** Non-normative example  
**Depends on:**  
- 03_SECOND_ORDER_SPACE_SIGMA2.md  
- 07_FORMAL_CONSTRUCTIONS/fiber_bundle_model.md  
- 11_NUMERICAL_TEST_TEMPLATES.md  

---

## 1. Purpose

This toy system provides a minimal dynamical model that exhibits:

- phase-gated action,
- noncommutativity of transformations,
- "same x, different future" behavior,

without invoking biology or domain-specific mechanisms.

It is intended to be used directly with numerical templates:
- T1 (noncommutativity),
- T2 (holonomy loop),
- T3 (same x, different future divergence).

---

## 2. State variables and embodiment class

### First-order state (S-frame)

Let the first-order state be:

    x(t) ∈ ℝ

interpretable as a generic amplitude, concentration, voltage, or coordinate.

### Second-order organizational variable (Σ₂ fiber)

Let the organizational variable be a phase:

    φ(t) ∈ S¹  (identified modulo 2π)

φ is not treated as a stored "memory"; it is an organizational coordinate that
gates S-frame dynamics.

### Embodiment class E (qualitative)

E is characterized by:
- continuous energy throughput supporting sustained oscillation,
- bounded noise on φ and x,
- dissipation that prevents unbounded growth.

---

## 3. Dynamics

### 3.1 Phase evolution (oscillator core)

Let φ evolve approximately uniformly with noise:

    φ-dot = ω + ξ(t)

where:
- ω > 0 is nominal angular frequency,
- ξ(t) is bounded or stochastic noise (e.g., Gaussian white noise).

This makes φ a persistent, winding variable.

---

### 3.2 Phase gate

Define a smooth phase gate G(φ) that is near 1 only in a narrow window.

One convenient form:

    G(φ) = exp( - d(φ, φ0)^2 / (2σ^2) )

where:
- φ0 is the gate center,
- σ (small) sets the gate width,
- d(φ, φ0) is wrapped distance on S¹ (shortest angular distance).

Interpretation:
- most of the cycle, G(φ) ≈ 0
- near φ ≈ φ0, G(φ) ≈ 1

---

### 3.3 S-frame dynamics with gated actuation

Define:

    x-dot = -α x + G(φ) * ( β - γ x ) + η(t)

where:
- α > 0 is baseline relaxation,
- β > 0 is gated drive amplitude,
- γ ≥ 0 is gated damping/saturation term,
- η(t) is noise (bounded or stochastic).

Interpretation:
- x decays most of the time
- x receives structured "kicks" only during gate windows
- the timing of those kicks depends on φ

This is the minimal "nothing happens until the right phase" mechanism.

---

## 4. Σ₂ interpretation (bundle view)

- Base space X: instantaneous x
- Fiber F: phase circle S¹
- Total space: (x, φ)
- Organizational mode σ corresponds to φ (and possibly gate-lock regime)

Order relevance arises because:
- trajectories with identical x but different φ diverge
- sequences of transformations that shift φ relative to the gate yield different outcomes

---

## 5. Two admissible transformations (for T1 noncommutativity)

Define two admissible transformations (control interventions):

### τ₁: Phase perturbation (retiming)
Instantly shift phase:

    φ ← φ + Δ

(with wrap-around)

This models a small retiming pulse.

### τ₂: Amplitude perturbation (state push)
Instantly shift x:

    x ← x + δ

This models a brief input impulse.

Both are admissible under E for small Δ, δ.

---

## 6. Noncommutativity demonstration (T1)

Consider starting from the same (x0, φ0*) at time t0.

Apply the two transformations within a short time window such that:
- τ₁ changes whether τ₂ lands inside the gate window.

Then generically:

    Outcome(τ₂ ∘ τ₁) ≠ Outcome(τ₁ ∘ τ₂)

Example intuition:
- If τ₁ advances φ so the system enters the gate, then τ₂ is amplified by G(φ).
- If τ₂ is applied before τ₁, it may occur outside the gate and decay away.

Outcome can be defined as:
- x(t0 + T) after one cycle,
- or integrated work proxy ∫ G(φ(t)) x(t) dt over a window,
- or probability of crossing a threshold x > x_thr.

---

## 7. "Same x, different future" (T3)

Construct two histories H₁ and H₂ that arrive at:

    x(t0) = x0

but with different phase:

    φ(t0) = φA  vs  φB

Then future x evolution differs because the next gated drive occurs at different times.

This satisfies:
- identical first-order state,
- divergent future due to trajectory variable.

---

## 8. Holonomy-style loop protocol (T2)

Define a closed-loop control protocol in the (externally controlled) parameters:

- temporarily modulate ω or φ0 (gate center),
- then return them to baseline.

Even if x is returned to x0 at the end of the protocol, φ may accumulate a net
shift relative to the gate schedule, producing a persistent change in subsequent
responses.

In practice:
- run a parameter cycle P(t) that returns ω and φ0 to original values,
- verify x returns to same equivalence class,
- measure that the system is now in a different phase relation state (σ proxy),
- confirm different future outcomes under identical forcing.

---

## 9. Proto-second-order vs second-order behavior in this toy

- **Proto-second-order regime:** gate is narrow but noise is large enough that φ
  rapidly dephases; ordering effects exist but wash out quickly.

- **Second-order regime:** φ remains sufficiently coherent (or is actively stabilized)
  such that ordering effects persist robustly across cycles.

This toy therefore supports both regimes by parameter choice.

---

## 10. Suggested parameter defaults (dimensionless)

For quick numerical exploration (arbitrary units):

- α = 1.0
- β = 3.0
- γ = 0.5
- ω = 2π (one unit period)
- σ = 0.2 (narrow gate)
- φ0 = 0
- η, ξ: start at 0 then add noise gradually

---

## 11. Status

This toy system provides a minimal, domain-agnostic demonstration of:

- phase-gated causal efficacy,
- noncommutativity of transformations,
- and trajectory-dependent outcomes.

It is suitable as the first numerical testbed for Σ₂ relevance.