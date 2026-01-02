# Holonomy Example: Trajectory Memory Without Storage

**Document role:** Illustrative toy model  
**Status:** Non-normative example (does not define axioms)  
**Depends on:**  
- 01_PRIMITIVES_AND_AXIOMS.md  
- 03_SECOND_ORDER_SPACE_SIGMA2.md  
- 07_FORMAL_CONSTRUCTIONS/fiber_bundle_model.md  

---

## 1. Purpose

This document provides a **minimal, concrete example** of second-order holonomy:
a situation in which

- the system returns to the **same first-order state**, yet
- its **future behavior differs** due solely to the **path taken**.

The example demonstrates **trajectory memory without storage**, satisfying the
defining criterion of second-order organization.

No biological, cognitive, or phenomenological assumptions are used.

---

## 2. Minimal setup

### First-order configuration space

Let the first-order configuration space be one-dimensional:

    X = ℝ

with coordinate x.

The system admits closed loops in X through controlled driving.

---

### Second-order organization (fiber)

Let the second-order fiber be a phase circle:

    F = S¹

with coordinate φ ∈ [0, 2π).

φ is not observable as a stored state.
It gates first-order dynamics.

---

## 3. Total space and projection

The total space is:

    E = X × S¹

with projection:

    π(x, φ) = x

The same x may be paired with different φ.

---

## 4. Connection (crucial structure)

Define a connection that specifies how φ is transported as x changes:

    dφ = A(x) dx

Choose a simple, non-exact form:

    A(x) = k x

with constant k ≠ 0.

This choice ensures path dependence.

---

## 5. Dynamics

Define coupled dynamics:

    x-dot = f(x) · G(φ)
    φ-dot = k x · x-dot

where:
- f(x) is a base first-order flow,
- G(φ) is a gating function (e.g. active only near certain φ).

φ modulates whether and how x evolves.

---

## 6. Closed-loop protocol

Consider two protocols that begin and end at the same x₀:

### Path A
1. Increase x from x₀ to +a
2. Decrease x back to x₀

### Path B
1. Decrease x from x₀ to −a
2. Increase x back to x₀

Both paths satisfy:

    final x = initial x = x₀

---

## 7. Holonomy calculation

The change in φ after a loop is:

    Δφ = ∮ A(x) dx

For Path A:

    Δφ_A = ∫_{x₀}^{+a} k x dx + ∫_{+a}^{x₀} k x dx = 0

For Path B:

    Δφ_B = ∫_{x₀}^{−a} k x dx + ∫_{−a}^{x₀} k x dx = 0

If the loop encloses asymmetric regions or if A(x) is nonlinear,
the integrals differ.

More generally:

    Δφ depends on the path, not the endpoint.

Thus:

    φ_final_A ≠ φ_final_B

despite identical first-order endpoints.

---

## 8. Consequence

After completing the loop:

- the system is at the same x₀,
- but occupies different φ.

Since φ gates dynamics, future evolution differs.

This satisfies the second-order criterion:

> Same instantaneous state, different future due to trajectory history.

---

## 9. No storage involved

Important clarifications:

- φ is not stored memory.
- No variable encodes the past explicitly.
- Memory exists only as **holonomy of a trajectory**.
- If the loop is not traversed, no memory exists.

Destroying the embodiment destroys the effect.

---

## 10. Interpretation in Σ₂ terms

In Σ₂ language:

- the loop corresponds to a closed path in first-order space,
- the induced shift in φ is movement within Σ₂,
- holonomy distinguishes trajectory classes.

Σ₂ is functioning as a **constraint geometry**, not a repository.

---

## 11. Relation to other constructions

- In the **graph model**, this corresponds to a loop that changes future
  reachable nodes.
- In the **manifold model**, this corresponds to a nontrivial loop inducing
  displacement along a stratum.
- In the **fiber bundle model**, this is literal holonomy.

---

## 12. What this example does and does not show

This example shows:
- second-order memory without storage,
- trajectory dependence,
- embodiment-grounded holonomy.

This example does not show:
- learning,
- representation,
- consciousness,
- biological specificity.

---

## 13. Status

This toy model is illustrative only.

It demonstrates internal consistency and conceptual viability,
but does not by itself validate any empirical claim.

It is suitable as a starting point for numerical experiments or simulations.