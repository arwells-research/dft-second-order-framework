# Graph Construction of Σ₂

**Document role:** Discrete formal construction  
**Status:** Stable (extensions allowed via MINOR versions)  
**Depends on:**  
- 01_PRIMITIVES_AND_AXIOMS.md  
- 02_ORDERS_OF_ORGANIZATION.md  
- 03_SECOND_ORDER_SPACE_SIGMA2.md  

---

## 1. Purpose

This document provides a **graph-theoretic construction** of the second-order
constraint space Σ₂.

The graph construction is a **discrete reduction** of the canonical fiber-bundle
model. It is especially useful for:

- computational modeling,
- finite-state abstractions,
- control and planning problems,
- comparison with empirical dynamical data.

This construction is a **representation**, not an ontological claim that Σ₂ “is”
a graph.

---

## 2. Core idea

Σ₂ is represented as a **graph of admissible organizational types**, where:

- nodes represent equivalence classes of second-order organization,
- edges represent admissible transitions under constraints,
- paths represent second-order trajectories.

Instantaneous first-order states are not nodes.

---

## 3. Nodes: organizational equivalence classes

### Definition (Node)

A node v ∈ V represents an **equivalence class of second-order organization**
defined by indistinguishability with respect to:

- gating behavior,
- trajectory response,
- functional outcomes under admissible perturbations.

Nodes do **not** represent stored patterns or states.

They represent **ways of being organized over time**.

---

## 4. Edges: admissible transitions

### Definition (Edge)

A directed edge e = (vᵢ → vⱼ) exists if and only if:

- there exists an embodiment,
- and a viable process,
- that can transform organization vᵢ into vⱼ
- without violating constraints.

Edges represent **possibility**, not guarantee.

---

### Edge labels (optional)

Edges may be labeled with:

- triggering conditions,
- required interventions,
- energy thresholds,
- control actions.

Labels are constraints, not causes.

---

## 5. Graph structure

The graph is defined as:

    G₂ = (V, E)

with:
- V: set of organizational equivalence classes,
- E ⊆ V × V: admissible transitions.

The graph may be:
- directed or undirected,
- cyclic,
- disconnected.

Disconnected components correspond to **organizationally incompatible regimes**.

---

## 6. Trajectories as paths

### Definition (Second-order trajectory)

A second-order trajectory is a **path** in G₂:

    γ = (v₀ → v₁ → … → vₙ)

Two trajectories may:
- pass through the same nodes,
- differ in ordering,
- differ in repetition,
- differ in looping structure.

Trajectory identity is path identity, not node identity.

---

## 7. Space-like analog in the graph

The graph provides a **space-like analog** via:

- adjacency (local compatibility),
- separation (incompatibility),
- connectivity (reachability),
- components (organizational domains).

No metric is assumed.

If a metric is introduced (e.g. edge cost), it is derived and embodiment-dependent.

---

## 8. Time-like analog in the graph

The **ordering of edges** provides a time-like analog:

- paths are ordered sequences,
- cycles encode recurrence,
- irreversible transitions break symmetry.

Graph time is **topological**, not parametric.

---

## 9. Holonomy in the graph

### Definition (Graph holonomy)

Holonomy occurs when:

- a closed path exists starting and ending at the same node,
- traversal of the loop alters future admissible transitions.

Formally:
- same node,
- different reachable subgraph after loop traversal.

This encodes **trajectory memory** without stored state.

---

## 10. Capacity without storage

In the graph model, capacity is characterized by:

- number of distinguishable nodes,
- number of non-equivalent cycles,
- depth of reachable subgraphs,
- robustness of paths under perturbation.

Capacity is structural, not representational.

---

## 11. Relation to first-order dynamics

The graph does **not** replace first-order dynamics.

Instead:
- first-order dynamics realize transitions,
- the graph constrains which transitions are admissible.

The graph abstracts **organizational possibilities**, not physical motion.

---

## 12. Reduction from the fiber bundle model

The graph model can be obtained by:

- partitioning fiber space into equivalence classes,
- collapsing continuous regions into nodes,
- encoding admissible transports as edges.

Thus:

    fiber bundle → stratified manifold → graph

---

## 13. Prohibited interpretations

This graph must not be interpreted as:

- a state transition diagram of stored memory,
- a symbolic rule system,
- a repository of behaviors,
- a computational program.

It is a **constraint graph**, not an instruction set.

---

## 14. Status

This graph construction is a valid representation of Σ₂
when discrete abstraction is appropriate.

Any use of this model must:

- justify the equivalence-class definition,
- preserve trajectory primacy,
- avoid reifying nodes as stored states.

Compatibility requires adherence to these constraints.