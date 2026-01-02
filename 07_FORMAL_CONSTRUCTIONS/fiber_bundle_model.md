# Fiber Bundle Construction of Σ₂

**Document role:** Canonical formal construction  
**Status:** Stable (extensions allowed via MINOR versions)  
**Depends on:** 01_PRIMITIVES_AND_AXIOMS.md, 03_SECOND_ORDER_SPACE_SIGMA2.md

---

## 1. Purpose

This document provides a **canonical mathematical construction** of the
second-order constraint space Σ₂ using the language of **fiber bundles**.

This construction is preferred because it:

- enforces embodiment explicitly,
- cleanly separates first- and second-order structure,
- supports trajectory-dependent memory via holonomy,
- avoids reification of constraints or storage metaphors.

This is a **representation**, not an ontological claim that nature “is” a bundle.

---

## 2. Base space: first-order configuration (S-frame)

Let **X** denote the first-order configuration space.

X may be:
- continuous (e.g. ℝⁿ-valued state variables),
- discrete,
- hybrid.

Elements x ∈ X fully specify instantaneous first-order state.

Time at this level is parametric and external.

---

## 3. Fiber: second-order organization

For each x ∈ X, define a fiber:

    Σ₂,x = π⁻¹(x)

Σ₂,x is the set of admissible second-order organizations compatible with x.

Properties of the fiber:
- contains no realized trajectories,
- contains no stored memory,
- contains only admissible organizational possibilities.

Globally, Σ₂ corresponds to the **typical fiber** F.

---

## 4. Total space

Define the total space:

    E = { (x, σ) | x ∈ X, σ ∈ Σ₂,x }

E is not itself Σ₂.
Σ₂ is represented by the fiber structure across E.

---

## 5. Projection and embodiment

The projection map:

    π : E → X

forgets second-order organization.

Embodiment is represented by:
- restriction of accessible fibers,
- restriction of admissible transitions,
- viability constraints on (x, σ).

There is no second-order causation without projection to X.

---

## 6. Connection: transport of second-order structure

To define how second-order organization evolves as x changes,
introduce a **connection** on the bundle.

Intuitively, the connection specifies:

- how σ is transported when x evolves,
- what it means for σ to remain “the same” across different x.

Formally, the connection defines a horizontal distribution in TE,
allowing curves in X to lift to curves in E.

---

## 7. Dynamics

A minimal coupled dynamics takes the form:

    x-dot = F(x; σ)
    σ-dot = Ω(x, σ)

Key properties:
- σ gates or biases x dynamics,
- σ evolution depends on accumulated process,
- σ is not reducible to stored state.

This satisfies the second-order criterion.

---

## 8. Holonomy and trajectory memory

### Definition (Holonomy)

Given a closed loop γ in X, parallel transport via the connection
may induce a nontrivial transformation of σ.

That is:

- start at (x₀, σ₀),
- traverse a closed path in X,
- return to x₀ with σ₁ ≠ σ₀.

This difference is **holonomy**.

---

### Interpretation

Holonomy realizes:

- same instantaneous state,
- different second-order organization,
- different future behavior.

Memory is therefore:
- a property of trajectories,
- not a stored variable.

---

## 9. Capacity without storage

In this construction, “capacity” is not bit storage.

Instead, it is characterized by:
- number of distinguishable holonomy classes,
- robustness of σ separation under noise,
- stability of σ under perturbation,
- richness of admissible loops in X.

All capacity measures are embodiment-dependent.

---

## 10. Relation to other constructions

### Graph reduction

If fibers are discretized into equivalence classes and transitions
are restricted, the bundle reduces to a **constraint graph**.

---

### Manifold reduction

If fibers vary smoothly and are locally Euclidean,
the bundle induces a **stratified manifold** structure on Σ₂.

---

## 11. Prohibited interpretations

This construction must not be interpreted as:

- a hidden state space storing information,
- a parallel spacetime,
- a repository of forms,
- a disembodied temporal field.

σ is organizational, not representational.

---

## 12. Status

This fiber bundle construction is the **canonical formal model**
for Σ₂ within this framework.

Downstream work may:
- specialize X or F,
- specify concrete connections,
- introduce noise or control.

Downstream work may not:
- reinterpret σ as stored memory,
- detach Σ₂ from embodiment,
- collapse σ into x.

Compatibility requires adherence to these constraints.