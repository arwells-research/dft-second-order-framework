# Primitives and Axioms

This document defines the minimal formal commitments of the Dual-Frame Theory
second-order framework. All subsequent constructions must respect these
primitives, axioms, and prohibitions.

This document is normative for the definition of **Σ₂ (second-order organization)**.

**Scope note (2026):** This repository defines Σ₂ as a formal layer: constraint
geometry over admissible trajectories grounded by embodiment. It does **not**
certify organism-level biology or cognition. Subsequent development of the
sigma-order program treats biological organization as requiring higher-order
closure (provisionally Σ₅+) and cognition as higher still. Any references to
“mind” or cognition in this document are strictly contextual and non-normative.
See `SIGMA_ORDER_SCOPE_CORRECTION_2026.md` for the normative scope statement.

---

## Primitive commitments

### P1. Process is primitive
The fundamental ontological unit is **process**, not state.  
States are **projections** or cross-sections of processes.

### P2. Organization is real
Organization is not epistemic shorthand.  
It has causal efficacy via constraint.

### P3. Constraints are not objects
Constraints do not exist as stored entities.  
They exist as invariances that coherent processes satisfy.

---

## Definition of order

**Order** is defined by the lowest-level primitive required to specify
**persistence** under admissible perturbation.

- **First order:** persistence is fully specified by instantaneous state  
- **Second order:** persistence requires trajectory or path information  
- **Third order:** persistence requires representation of trajectories themselves  

Order is not scale, complexity, hierarchy, or refinement.

This definition applies structurally and does not certify substrate-specific
biological or cognitive sufficiency.

---

## First order (S-frame)

### Definition
A system is first order if and only if its evolution is fully determined
(up to noise) by instantaneous state and external parametric time.

A minimal schematic form is:

    x(t + Δt) = F(x(t), t)

### Characteristics
- State-based
- Markovian given full state
- Time is an external, uniform parameter
- Memory is stored state
- Conservation applies to instantaneous quantities

### Constraint (F1)
No first-order description may depend on history except via encoded state.

---

## Second order (T-frame)

### Definition
A system is second order if two systems may share identical instantaneous
state yet diverge in future evolution due to **unreduced trajectory history**.

Second order is not refined first-order time, delayed state, or hidden state.

---

## Second-order variables

A second-order variable **φ** satisfies:

- φ is not a function of instantaneous state alone
- φ evolves through accumulated process
- φ gates, biases, or conditions first-order dynamics

A minimal schematic form is:

    ẋ = F(x; φ)
    φ̇ = Ω(x, φ)

The introduction of φ does not imply a new physical degree of freedom; it
represents trajectory-conditioned organization.

---

## Second-order space–time analogs

### Axiom (T1)
Any second-order system exhibiting persistence and differentiation must possess:

- a **space-like analog** enabling distinction, compatibility, and adjacency
- a **time-like analog** enabling ordering, irreversibility, and history dependence

These analogs are relational and organizational, not metric or geometric
in the first-order sense.

---

## Second-order constraint space (Σ₂)

### Definition
Σ₂ is the set of admissible second-order trajectories permitted by physical
invariants and embodiment constraints.

Σ₂:
- contains no realized trajectories
- contains no stored forms, memories, or ideas
- is a constraint grammar, not a library or state space

---

## Instantiation

### Definition
Instantiation is the stabilization of a trajectory within Σ₂ through embodiment.

A trajectory does not exist prior to instantiation.

### Axiom (I1)
The existence of Σ₂ must not depend on recurrence.  
Recurrence stabilizes attractors but does not originate them.

---

## Embodiment

### Definition
A body is a first-order system capable of grounding second-order variables by:
- supplying continuous energy flow
- enforcing compatibility constraints
- supporting trajectory persistence against noise and dissipation

### Axiom (E1)
Second-order dynamics are causally inert without embodiment.

---

## Relation to orders of mind (non-normative, archival context)

**Status:** Non-normative contextual note (not part of the Σ₂ formal contract)

Earlier internal versions of this framework introduced terminology such as
“second-order mind” and “third-order mind” to describe structural relationships
between trajectory-conditioned organization and representational access to that
organization.

Subsequent development of the sigma-order program clarifies that:

- organism-level biology requires higher-order closure (provisionally Σ₅+),
- cognition and reflective awareness are treated as higher still,
- therefore this repository does **not** certify any taxonomy of mind or cognition.

These earlier terms are retained only for historical continuity and must not be
interpreted as sufficiency claims.

The archival discussion appears in `05_MIND_2ND_VS_3RD_ORDER.md` and is marked
superseded.

---

## Prohibitions

The following are explicitly forbidden within this framework:

- disembodied repositories of form, memory, or ideas
- collapse of second-order time into refined clock time
- energy creation or violation of conservation laws
- treating constraints as stored or transferable objects
- unembodied second-order causation

---

## Status

These primitives and axioms are foundational for the definition of Σ₂.

Any model, theory, or application that violates them is not compatible
with this framework.

Interpretation of biological or cognitive organization requires higher-order
framework layers beyond Σ₂.
