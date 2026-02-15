# Σ₂ Case Study Interface (Domain-Agnostic)

**Document role:** Interface contract for downstream case studies  
**Status:** Normative (interface only; does not introduce new axioms)  
**Applies to:** Any empirical, computational, or engineered case study claiming Σ₂ relevance

---

## 1. Purpose

This document defines the **case study interface** for Σ₂.

It specifies:

- what a case study must declare,
- what diagnostics must be evaluated,
- what constitutes Σ₂ consistency,
- what artifacts must be provided,
- how embodiment is specified,
- how ordering relevance is tested,
- how results are classified.

This document is **domain-agnostic**.  
EEG, molecular simulations, oscillator models, AI systems, or devices must all
enter the framework through this interface.

**Scope note:** Domain mentions in this document (e.g., EEG, molecular simulation, AI) are **illustrative only**. This repository does not contain or endorse domain analyses; it defines the Σ₂ interface and diagnostic contracts that downstream case-study repositories must satisfy.

---

## 2. Scope and constraints

This interface:
- does **not** introduce new axioms,
- does **not** privilege any domain,
- does **not** assume biology, cognition, or semantics.

It exists to prevent:
- ad hoc interpretations,
- domain-specific drift,
- conflation of modeling convenience with ontology.

All downstream case studies must adhere to this interface to be considered
Σ₂-consistent.

---

## 3. Required declarations (minimal schema)

Any Σ₂ case study must explicitly declare the following:

1. **System description**
   - What is the system?
   - What are its controllable variables?
   - What are the relevant degrees of freedom?

2. **Embodiment E**
   - Noise sources and magnitudes
   - Dissipation regimes
   - Coupling constraints
   - Resource limits
   - Environmental interactions

3. **Candidate organizational coordinate(s)**
   - What σ-like coordinates are hypothesized?
   - How are they measured or inferred?

4. **Admissibility predicate**
   - How is Adm(γ;E) defined?
   - What constitutes a viable trajectory?

5. **Interventions**
   - What transformations are applied?
   - What counts as admissible perturbation?

6. **Diagnostics**
   - What Σ₂ diagnostics are computed?
   - What controls are included?

---

## 4. Required diagnostics

A case study must evaluate, at minimum:

- **Ordering relevance / noncommutativity** (τ₂∘τ₁ ≠ τ₁∘τ₂)
- **Holonomy-like effects** (closed loops altering future admissibility)
- **Failed Markov closure** (state-sufficient modeling fails under admissible perturbations)

Optional (recommended):

- stability/robustness of σ under perturbation,
- maintenance costs (if claiming true second order).

---

## 5. Controls

All case studies must include:

- negative controls (first-order matched baselines),
- perturbation tests under common random numbers (where applicable),
- ablation of gating structures,
- sensitivity to embodiment parameters.

---

## 6. Classification outputs

Each case study must report:

- whether Σ₂ ordering relevance is present,
- whether effects persist under admissible perturbations,
- whether σ stabilization is present (proto vs true),
- and whether any claim exceeds Σ₂ scope.

---

## 7. Artifact requirements

A case study must provide:

- code and parameters sufficient to reproduce diagnostics,
- fixed seeds and provenance hashes where applicable,
- logs of interventions and outcomes,
- raw data needed to recompute diagnostics.

---

## 8. Status

This interface is intended to remain stable.

Changes must be:

- explicit,
- versioned,
- and backward-compatible where possible.

No domain claims or sufficiency claims are permitted in this document.
