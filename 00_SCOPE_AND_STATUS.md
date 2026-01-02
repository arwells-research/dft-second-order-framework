# Scope and Status

**Repository:** dft-second-order-framework  
**Document role:** Boundary definition and change-control  
**Applies to:** All files in this repository unless explicitly stated otherwise

---

## 1. Purpose of this document

This document defines:

- the **scope** of the second-order framework,
- the **status** of its components,
- the rules governing **change, extension, and revision**,
- and the criteria for **compatibility** and **incompatibility** with the framework.

Its purpose is to prevent silent drift, category collapse, or retroactive reinterpretation as the framework evolves.

This document is normative.

---

## 2. Scope

### 2.1 What is in scope

This repository is scoped to the following:

- ontological primitives (process, constraint, embodiment)
- definitions of first-, second-, and third-order organization
- formal properties of second-order constraint space (Σ₂)
- admissible formalisms for Σ₂ (graph, manifold, fiber bundle)
- rules for instantiation, grounding, and recurrence
- explicit prohibitions on disallowed interpretations

The scope is **foundational** and **pre-empirical**, with minimal operational grounding used strictly to demonstrate diagnostic feasibility rather than empirical claims.

---

### 2.2 What is explicitly out of scope

The following are **out of scope** and must not be added to this repository:

- empirical biological claims
- neuroscience data analysis or fitting
- AI architectures or benchmarks
- device designs or engineering schematics
- claims of consciousness, sentience, or phenomenology beyond order definitions
- metaphysical assertions not grounded in the axioms
- new physical forces, energies, or fields

Any work involving these must live in **separate repositories** and depend on this one by reference.

---

## 3. Status of framework components

### 3.1 Frozen components (contractual)

The following are considered **frozen** at a given MAJOR version:

- primitive commitments (P1–P3, as defined in `01_PRIMITIVES_AND_AXIOMS.md`)
- definition of order
- distinction between first, second, and third order
- prohibition of disembodied repositories
- requirement of embodiment for causal efficacy
- non-collapse of second-order time into first-order time
- conservation applied at the trajectory level

These constitute the **framework contract**.

Changes to these require a **MAJOR version increment**.

---

### 3.2 Stable but extensible components

The following are stable but may be extended compatibly:

- formal representations of Σ₂
- choice of mathematical language (graph, manifold, bundle)
- toy models demonstrating properties
- clarifications of terminology
- additional prohibitions derived from axioms

Extensions must not contradict frozen components.

These changes require a **MINOR version increment**.

---

### 3.3 Provisional components

The following may evolve without breaking compatibility:

- illustrative examples
- explanatory text
- ordering or presentation of documents
- non-normative commentary

These changes require a **PATCH version increment**.

---

## 4. Versioning rules

This repository uses **semantic versioning**:

- **MAJOR (X.0.0):** breaking changes to axioms or definitions
- **MINOR (0.Y.0):** additive, compatible extensions
- **PATCH (0.0.Z):** clarifications, typo fixes, rewording only

Silent modification of axioms is forbidden.

---

## 5. Compatibility definition

A model, theory, or application is **compatible** with this framework if and only if:

1. It respects all frozen axioms.
2. It does not reify second-order constraint space into a repository, store, or latent state variable, whether explicit or implicit.
3. It does not treat second-order time as refined clock time.
4. It requires embodiment for second-order causal efficacy.
5. It does not violate conservation laws.
6. It does not attribute independent causal power to uninstantiated constraints.

Failure on any point constitutes incompatibility.

---

## 6. Criteria for revision

Revisions to frozen components may occur only if:

- a formal contradiction is identified within the framework, or
- an extension leads to unavoidable inconsistency, or
- an explicit decision is made to abandon backward compatibility.

Empirical disagreement alone is not sufficient grounds for revision, since this repository is pre-empirical.

---

## 7. Falsifiability and limits

This framework is constrained but not directly falsifiable in isolation, as it specifies organizational criteria rather than empirical predictions.

It may be indirectly challenged if:

- no embodiment can be found that realizes second-order variables as defined,
- all candidate realizations collapse to first-order descriptions without loss,
- or the second-order distinction provides no explanatory or organizational advantage in any downstream domain.

Such outcomes motivate reassessment but do not automatically falsify the framework.

---

## 8. Relationship to downstream repositories

Downstream repositories must:

- specify the version of this framework they depend on,
- state any additional assumptions explicitly,
- and refrain from modifying foundational definitions locally.

This repository is a **dependency**, not a workspace.

---

## 9. Status summary

At version **v0.2.0**, this framework is:

- internally consistent
- ontologically minimal
- formally constrained
- pre-empirical in scope
- operationally grounded via a minimal diagnostic toy
- suitable as a foundation for modeling, simulation, and experiment design

It is not complete, but it is stable.

Further work proceeds by **extension**, not revision, unless explicitly versioned otherwise.