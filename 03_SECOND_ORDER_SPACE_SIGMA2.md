# Second-Order Space Σ₂

**Document role:** Core formal definition  
**Status:** Frozen (no breaking changes without MAJOR version bump)  
**Depends on:**  
- 00_SCOPE_AND_STATUS.md  
- 01_PRIMITIVES_AND_AXIOMS.md  
- 02_ORDERS_OF_ORGANIZATION.md  
- 04_EMBODIMENT_AND_INSTANTIATION.md  

---

## 1. Purpose

This document defines **Σ₂**, the second-order organizational space.

Σ₂ is not a physical space, a state space, or a repository.  
It is a **constraint space over admissible trajectories**, made explicit when
trajectory structure itself becomes causally relevant.

---

## 2. Core definition

### Definition (Second-order space Σ₂)

Σ₂ is the space of **organizational possibilities** defined by the set of
trajectories that are *admissible* under a given embodiment.

Formally, for an embodiment class E:

    Σ₂(E) = { γ | Adm(γ; E) = 1 }

Σ₂ is therefore:
- embodiment-indexed,
- trajectory-native,
- independent of any particular representation.

---

## 3. What Σ₂ is not

Σ₂ must not be interpreted as:

- a hidden spatial dimension,
- a parallel spacetime,
- a storage medium,
- a repository of forms,
- a symbolic or representational space.

Σ₂ constrains **what can happen**, not **what is stored**.

---

## 4. Relationship to first-order dynamics

First-order dynamics operate on instantaneous configurations x(t).
They are local in time.

Second-order organization arises when:

- future behavior depends on **trajectory history**, and
- this dependence cannot be eliminated by any instantaneous state description
  available within the embodiment.

Σ₂ hosts this dependency explicitly.

---

## 5. Continuity principle (proto-geometric pressure)

Second-order organization does not emerge abruptly.

First-order dynamics already encode **latent geometric structure** via:
- invariants,
- symmetries,
- variational principles,
- phase relations,
- stability manifolds.

Σ₂ represents the **explicit completion** of this latent geometry when
trajectory structure becomes dynamically relevant.

---

## 6. Space-like analog in Σ₂

Σ₂ admits a **space-like analog** through:

- compatibility relations between organizational modes,
- neighborhoods of similar admissible trajectories,
- separation between incompatible regimes,
- connected components corresponding to organizational domains.

No metric is assumed or required.

---

## 7. Time-like analog in Σ₂

Σ₂ admits a **time-like analog** through:

- ordering of transformations,
- composition of trajectory segments,
- irreversibility of certain compositions.

Time in Σ₂ is not a parameter but an **ordering structure** over processes.

---

## 8. Representational freedom

Σ₂ may be represented as:

- a fiber bundle over first-order configuration space,
- a stratified manifold of organizational modes,
- a graph of organizational equivalence classes,
- a process algebra or path groupoid.

No representation is privileged.

---

## 9. Trajectory primacy

In Σ₂:

- points (if defined) are secondary,
- trajectories and their composition are primary.

Two systems in the same instantaneous first-order state may occupy different
locations in Σ₂ due solely to different histories.

---

## 10. Capacity without storage

Σ₂ supports **organizational capacity** without memory storage.

Capacity arises from:
- number of admissible trajectory classes,
- noncommutativity of transformations,
- robustness of organizational modes,
- presence of holonomy.

No symbols, states, or representations are stored.

---

## 11. Embodiment requirement

Σ₂ has causal efficacy only through embodiment.

Without an embodiment E:
- Σ₂ is not instantiated,
- admissibility is undefined,
- organization has no physical effect.

Σ₂ is not disembodied.

---

## 12. Admissibility predicate Adm(γ; E)

### 12.1 Definition

Let γ be a candidate trajectory and E an embodiment class.

Define:

    Adm(γ; E) ∈ {0, 1}

where:
- Adm(γ; E) = 1 if γ is viable under embodiment E,
- Adm(γ; E) = 0 otherwise.

Then:

    Σ₂(E) = { γ : Adm(γ; E) = 1 }

Σ₂ is explicitly **embodiment-indexed**.

---

### 12.2 What counts as a trajectory γ

A trajectory γ may be represented as:
- a lifted curve (x(t), σ(t)),
- a path on an organizational manifold,
- a path in a graph of organizational classes,
- a composable sequence of transformations.

The admissibility predicate is representation-agnostic.

---

### 12.3 Embodiment class E

An embodiment class E minimally specifies:
- energetic throughput regime,
- dissipation and noise bounds,
- coupling constraints,
- structural persistence limits,
- resource availability,
- boundary conditions.

E defines what “viable” means.

---

### 12.4 Minimal admissibility axioms

**A1. Physical consistency**  
If γ violates fixed physical invariants required by E, then Adm(γ; E) = 0.

**A2. Embodiment dependence**  
Admissibility is indexed by E; the same γ may be admissible under one E and not another.

**A3. Perturbation robustness**  
Admissible trajectories are not immediately destroyed by small perturbations within E’s noise class.

**A4. Local composition closure**  
If γ₁ and γ₂ are admissible and composable under E, their composition is admissible
unless a constraint boundary is crossed.

---

### 12.5 Practical qualitative evaluation

In practice, Adm(γ; E) = 1 if γ:
- remains within viability bounds,
- can be sustained or repeated for a characteristic timescale of E,
- produces consistent organizational outcomes rather than random drift.

---

## 13. Noncommutativity as order-relevance criterion

### 13.1 Transformations

Let τ denote an admissible transformation under embodiment E.

Transformations compose as:

    τ₂ ∘ τ₁

meaning “do τ₁, then τ₂.”

---

### 13.2 Noncommutativity criterion

A system exhibits **order-relevant organization** if there exist admissible
transformations τ₁ and τ₂ such that:

    Adm(τ₂ ∘ τ₁; E) = 1
    Adm(τ₁ ∘ τ₂; E) = 1

but:

    Outcome(τ₂ ∘ τ₁) ≠ Outcome(τ₁ ∘ τ₂)

Outcome may be defined at the level of:
- organizational mode σ,
- basin identity,
- reachable subgraph structure,
- or robust first-order behavior.

Noncommutativity indicates that **ordering matters** beyond instantaneous state.

---

## 14. Holonomy criterion

### Definition (Holonomy)

A system exhibits holonomy if there exists an admissible closed loop of
transformations or a closed loop in first-order configuration space such that:

    start: (x₀, σ₀)
    loop in x
    end:   (x₀, σ₁), with σ₁ ≠ σ₀

This is **trajectory memory without storage**.

---

## 15. Proto-second-order vs second-order

- **Proto-second-order:** noncommutativity exists, but organizational modes are
  weakly stabilized and easily erased by noise or dissipation.

- **Second-order:** noncommutativity exists and organizational modes are
  persistently stabilized, producing robust history-dependent divergence.

This distinction is structural, not biological.

---

## 16. Minimal experimental template

To test for Σ₂ relevance under embodiment E:

1. Identify two admissible transformations τ₁, τ₂  
2. Verify both compositions are admissible  
3. Compare outcomes of τ₂ ∘ τ₁ vs τ₁ ∘ τ₂  
4. Demonstrate robustness under perturbations allowed by E  

Success establishes order relevance.

---

## 17. Status

Σ₂ is defined as a **constraint geometry over admissible trajectories**.

It:
- introduces no new physics,
- violates no conservation laws,
- requires embodiment,
- and makes explicit the organizational structure implicit in complex first-order dynamics.

Downstream models must respect:
- trajectory primacy,
- embodiment indexing,
- and the noncommutativity and holonomy criteria.