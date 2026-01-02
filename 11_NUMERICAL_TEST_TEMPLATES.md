# Numerical Test Templates for Σ₂ Relevance

**Document role:** Practical evaluation templates (non-axiomatic)  
**Status:** Stable (extend with additional tests and domains)  
**Depends on:**  
- 02_ORDERS_OF_ORGANIZATION.md  
- 03_SECOND_ORDER_SPACE_SIGMA2.md  
- 07_FORMAL_CONSTRUCTIONS/fiber_bundle_model.md  
- 07_FORMAL_CONSTRUCTIONS/graph_model.md  
- 07_FORMAL_CONSTRUCTIONS/manifold_model.md  
- 10_PROTO_SECOND_ORDER_SYSTEMS.md  

---

## 1. Purpose

This document defines **numerical test templates** for detecting Σ₂ relevance
(order-relevant organization) in simulated or analyzed systems.

The templates are designed to:

- be substrate-agnostic (molecules, circuits, neural motifs, devices),
- avoid biology-specific assumptions,
- produce clear pass/fail signals aligned with Σ₂ definitions,
- connect directly to admissibility and noncommutativity criteria.

These are *programmatic tests* for whether a candidate model exhibits:
- proto-second-order behavior, or
- true second-order behavior.

---

## 2. Core observables and evaluation structure

Every test should specify:

- **Embodiment class E:** noise model, constraints, throughput regime
- **Transformations τ:** admissible operations / perturbations / driving segments
- **Outcome:** a robust measurable quantity (σ proxy or behavior proxy)
- **Robustness:** repeatability under perturbations allowed by E

Minimal decision rule:

- **Σ₂ relevance** if noncommutativity or holonomy is robustly demonstrated
  (03, Sections 13–14).

---

## 3. Template T1 — Noncommutativity test (τ ordering)

### Goal
Demonstrate that ordering of two admissible transformations matters:

    Outcome(τ₂ ∘ τ₁) ≠ Outcome(τ₁ ∘ τ₂)

### Setup
- Choose a model with state x(t)
- Define two admissible transformations τ₁, τ₂
  (e.g., pulses, binding events, control actions, parameter toggles)

### Procedure
1. Initialize at x₀ under embodiment E
2. Apply τ₂ ∘ τ₁ and measure Outcome A
3. Reset to x₀ (or equivalence class) and apply τ₁ ∘ τ₂ and measure Outcome B
4. Repeat under noise samples in E

### Pass condition
- A and B differ beyond a predefined tolerance
- Difference persists under allowed perturbations (robustness)

### Classification
- **Proto-second-order** if the effect exists but washes out quickly
- **Second-order** if it persists as a stabilized organizational difference

---

## 4. Template T2 — Holonomy test (loop in X)

### Goal
Demonstrate that a closed loop in first-order configuration returns to the same
x but changes organizational mode:

    start: (x₀, σ₀)
    loop in x
    end:   (x₀, σ₁), σ₁ ≠ σ₀

### Setup
- Choose a model with controllable loop-driving in X
- Identify an internal organizational proxy for σ
  (e.g., basin ID, phase estimate, mode occupancy, switching propensity)

### Procedure
1. Start at x₀
2. Drive x around a closed loop protocol L (parameter cycle, control schedule)
3. Return to x₀
4. Measure σ proxy before and after

### Pass condition
- Same x equivalence class at start and end
- σ proxy shifts reliably, affecting future evolution

---

## 5. Template T3 — “Same x, different future” divergence

### Goal
Demonstrate that identical instantaneous states can lead to different futures
due solely to history:

    x(t₀) identical
    future evolution differs

### Setup
- Generate two histories H₁ and H₂ that converge to the same x(t₀)
- Let the system evolve forward without further intervention

### Procedure
1. Construct H₁ and H₂ leading to identical x(t₀)
2. From t₀ onward, run the same dynamics
3. Compare time series statistics or final outcomes

### Pass condition
- Divergence persists beyond transient noise
- Difference is reproducible across trials

This is the practical form of Σ₂ relevance.

---

## 6. Template T4 — Failed Markov closure (compression barrier)

### Goal
Demonstrate that no finite-dimensional state closure captures outcomes under the
allowed perturbation class without loss.

This is the strongest defense against “just augment the state.”

### Setup
- Choose an observable Y(t) of interest
- Fit candidate Markov models of increasing order/dimension to predict Y(t+Δ)

### Procedure
1. Build model family M(k): k-dimensional state closures
2. Train/predict under a distribution of trajectories and perturbations
3. Evaluate generalization error vs k

### Pass condition (qualitative)
- Error does not collapse below threshold for any reasonable finite k
- Predictive sufficiency requires path-dependent functionals or exploding state

This indicates genuine trajectory-native organization.

---

## 7. Template T5 — Basin graph extraction (graph Σ₂)

### Goal
Construct a graph G₂ of organizational classes from simulation data and test for
order relevance via loops and reachability changes.

### Setup
- Identify metastable regions (basins) in state space
- Cluster trajectories into basin sequences

### Procedure
1. Generate trajectories under E
2. Identify basins and transitions
3. Build directed graph G₂ = (V,E)
4. Test noncommutativity and holonomy as:
   - different reachable sets after loops
   - ordering-dependent transitions between basins

### Pass condition
- Presence of nontrivial cycles with differing downstream reachability
- Robustness under perturbations

---

## 8. Template T6 — Manifold regime identification (continuous Σ₂)

### Goal
Identify continuous organizational coordinates and stratification boundaries
consistent with manifold Σ₂ representation.

### Setup
- Use dimensionality reduction on trajectory features (not instantaneous x only)
- Identify regime strata and boundary crossings

### Procedure
1. Construct trajectory descriptors (windowed features, phase features, cycle stats)
2. Embed descriptors into low-dimensional coordinates
3. Identify strata and transitions
4. Test whether transitions are ordering-dependent

### Pass condition
- Clear regime separation with ordering-dependent crossing behavior
- Trajectory features outperform state-only features in predicting outcomes

---

## 9. Embodiment specification checklist (required)

Every numerical test must state:

- noise class and amplitude
- dissipation / throughput regime
- coupling constraints
- reset protocol (how “same x” is defined)
- outcome definition and tolerance threshold
- number of trials / robustness criterion

Without this, results are not interpretable in Σ₂ terms.

---

## 10. Minimal recommended pipeline (for any candidate system)

To evaluate a candidate model efficiently:

1. **T1 (Noncommutativity)** — fastest signal
2. **T3 (Same x, different future)** — confirm
3. **T2 (Holonomy loop)** — strongest interpretation
4. **T5/T6 (Graph/Manifold extraction)** — structural visualization
5. **T4 (Failed Markov closure)** — hardest, most decisive

Stop early if no noncommutativity is found.

---

## 11. Status

These templates operationalize Σ₂ relevance without committing to substrate or
domain.

They:
- encode the admissibility and order criteria directly,
- support numerical and empirical adaptation,
- and provide a disciplined path from theory to test.

Extensions should preserve:
- embodiment indexing,
- robustness requirements,
- and the noncommutativity/holonomy hallmark.