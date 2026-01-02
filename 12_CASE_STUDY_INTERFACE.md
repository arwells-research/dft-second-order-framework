# Case Study Interface for Σ₂ Framework

**Document role:** Interface specification (domain-agnostic)  
**Status:** Stable (normative for downstream case studies)  
**Depends on:**  
- 03_SECOND_ORDER_SPACE_SIGMA2.md  
- 10_PROTO_SECOND_ORDER_SYSTEMS.md  
- 11_NUMERICAL_TEST_TEMPLATES.md  

---

## 1. Purpose

This document defines a **formal interface** for applying the Σ₂ framework to
external systems (empirical, simulated, or engineered) **without modifying the
core theory**.

It specifies:
- what a case study must declare,
- how external dynamics map onto Σ₂ primitives,
- how numerical or empirical tests relate to admissibility and order relevance,
- how results are classified.

This document is **domain-agnostic**.  
EEG, molecular simulations, oscillator models, AI systems, or devices must all
enter the framework through this interface.

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

Any Σ₂ case study must explicitly declare the following elements.

### 3.1 Embodiment class E

The embodiment class E defines the **viability regime** under which trajectories
are admissible.

At minimum, E must specify:
- noise class and amplitude bounds,
- dissipation / throughput regime,
- coupling constraints (what interactions are possible),
- resource limits (time, energy, structure),
- boundary conditions (environmental or experimental).

E must be stated **before** any analysis.

---

### 3.2 First-order variables X

The case study must define:
- the first-order configuration variables \(x(t)\),
- what constitutes an instantaneous state,
- how equivalence of x is determined (exact, coarse-grained, tolerance-based).

First-order completeness must be addressed explicitly:
- either justified,
- or acknowledged as approximate.

---

### 3.3 Organizational proxy (σ observable)

The case study must identify one or more **organizational proxies** corresponding
to σ in Σ₂ language.

σ proxies may be:
- phase estimates,
- basin identifiers,
- coordination patterns,
- mode occupancies,
- relational statistics,
- trajectory-derived features.

Important:
- σ proxies are **observables**, not assumed internal states.
- The proxy must be justified as organizationally relevant.

---

## 4. Transformations τ (process identification)

The case study must define what counts as an **admissible transformation τ**.

Examples:
- control pulses,
- binding/unbinding events,
- parameter excursions,
- stimulus timing changes,
- protocol segments.

Each τ must be:
- admissible under E,
- composable with other τ,
- well-defined in time/order.

Transformations must be named and documented.

---

## 5. Outcome definition

The case study must define **Outcome** clearly.

Outcomes may include:
- final-state statistics,
- trajectory-class identity,
- basin reachability,
- threshold-crossing probability,
- performance metrics.

Outcome definitions must:
- be robust to small perturbations,
- reflect organizational consequences,
- not collapse trivially to instantaneous state.

---

## 6. Mapping to Σ₂ numerical templates

Each case study must state which Σ₂ templates are exercised:

- **T1:** Noncommutativity (ordering sensitivity)
- **T2:** Holonomy (loop-induced organizational change)
- **T3:** Same x, different future
- **T4:** Failed Markov closure
- **T5/T6:** Graph or manifold extraction (optional)

At least one of T1–T3 must be meaningfully addressed to claim Σ₂ relevance.

---

## 7. Robustness and admissibility check

For any claimed effect, the case study must demonstrate:
- persistence under perturbations allowed by E,
- non-fragility (effect does not vanish immediately),
- repeatability across trials or realizations.

This establishes:
\[
\mathrm{Adm}(\gamma; E) = 1
\]
for the relevant trajectory class.

---

## 8. Order classification rule

Based on results, the system must be classified as one of:

- **First-order:**  
  No noncommutativity or trajectory dependence beyond state.

- **Proto-second-order:**  
  Noncommutativity or holonomy exists but σ is weakly stabilized and fragile.

- **Second-order:**  
  σ is persistently stabilized and influences future admissibility robustly.

Classification must be justified explicitly.

---

## 9. Prohibited shortcuts and failure modes

The following invalidate a Σ₂ case study:

- implicit embodiment assumptions,
- post hoc selection of σ proxies,
- defining τ after observing outcomes,
- conflating prediction accuracy with organization,
- treating σ as stored representation.

These are considered category errors.

---

## 10. Relation to core framework

This interface:
- preserves trajectory primacy,
- enforces embodiment indexing,
- operationalizes admissibility,
- and prevents collapse of Σ₂ into state augmentation.

No case study may override core definitions.

---

## 11. Usage pattern

Recommended structure for downstream case studies:

1. Declare E  
2. Define X and σ proxy  
3. Identify τ  
4. Define Outcome  
5. Apply T1–T4 tests  
6. Evaluate robustness  
7. Classify order  
8. State limitations

This pattern must be followed.

---

## 12. Status

This document completes the **conceptual interface layer** of the Σ₂ framework.

It enables:
- disciplined application to real systems,
- comparison across domains,
- cumulative scientific progress.

Downstream work that does not conform to this interface
is not considered Σ₂-grounded.