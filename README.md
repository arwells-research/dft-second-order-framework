# Dual-Frame Theory: Second-Order Framework

**Status:** Foundational / Axiomatic (with operational grounding)  
**Version:** v0.2.1  
**Scope:** Conceptual kernel + minimal operational demonstration  
**Audience:** Researchers in theoretical biology, complex systems, dynamical systems, foundations of cognition, and foundational AI

---

## Purpose

This repository defines the foundational framework for **second-order organization** within Dual-Frame Theory (DFT).

It formalizes:

- what is meant by **first-, second-, and third-order organization**
- how second-order structure differs categorically from first-order spacetime dynamics
- how second-order constraint spaces (**Σ₂**) exist **without acting as repositories**
- how embodiment grounds second-order organization without mysticism or reductionism
- how **admissible trajectories** replace instantaneous state sufficiency when ordering matters


## Sigma-order scope correction (2026)

This repository defines **Σ₂** as a *formal* layer: **constraint geometry over admissible trajectories** with ordering relevance, grounded by embodiment and operational diagnostics.

**Update:** Subsequent development of the sigma-order program clarifies that **biological organization is not modeled at Σ₂**. While biological systems can exhibit **Σ₂-type phenomena** (trajectory gating, ordering dependence, holonomy-like path effects) at the level of components and motifs, **full biological organization requires higher-order closure** (provisionally treated as **Σ₅+** in the current program).

Accordingly:

- Σ₂ is treated here as a **necessary lower layer**, not a sufficient model of biology or cognition.
- Any mentions of biology, cognition, or AI in this repository are **illustrative** and must be read as **component-level / motif-level**, not as claims of organism-level sufficiency.

For the normative statement of this correction, see `SIGMA_ORDER_SCOPE_CORRECTION_2026.md`.

In addition to the formal framework, this repository includes a **minimal operational grounding artifact** demonstrating that Σ₂ diagnostics are measurable and behave as predicted in a controlled stochastic system.

This repository is **not** an application, dataset, or domain-specific model. It exists to preserve **conceptual invariants** and **diagnostic criteria** so downstream work does not drift, collapse categories, or smuggle in hidden state.

---

## What this repository is

- A formal contract of **definitions, axioms, and prohibitions**
- A shared dependency for future theoretical and applied work
- A constraint layer that later models must satisfy
- A boundary-setting document (what is allowed vs. forbidden)
- A reference implementation demonstrating operational detectability of Σ₂ organization

---

## What this repository is not

- Not a biological model
- Not a neuroscience data analysis
- Not an AI architecture
- Not a metaphysical proposal
- Not a theory of consciousness per se
- Not a claim of new physical forces or energy sources

All applications, simulations, and empirical studies must live in **separate repositories** and explicitly reference this framework.

---

## Core commitments

This framework is built on the following non-negotiable commitments:

1. Process precedes state  
2. Organization is real and causally effective  
3. Constraints are real but not objects  
4. Second order is not refined first-order time  
5. No disembodied repositories of form, memory, or ideas  
6. Embodiment is required for causal efficacy  
7. Conservation laws are respected **at the trajectory level**

Violating any of these invalidates compatibility.

---

## Structure of the framework

- **First order (S-frame):** state evolution indexed by parametric time
- **Second order (Σ₂ / T-frame):** geometry of admissible trajectories with ordering relevance
- **Third order:** representation *of* second-order structure itself

Only first-order dynamics admit complete instantaneous-state closure in principle.

---

## Repository layout

    dft-second-order-framework/
    ├── README.md
    ├── 00_SCOPE_AND_STATUS.md
    ├── 01_PRIMITIVES_AND_AXIOMS.md
    ├── 02_ORDERS_OF_ORGANIZATION.md
    ├── 03_SECOND_ORDER_SPACE_SIGMA2.md
    ├── 04_EMBODIMENT_AND_INSTANTIATION.md
    ├── 05_MIND_2ND_VS_3RD_ORDER.md
    ├── 06_SHARED_STRUCTURE_NO_REPOSITORIES.md
    ├── 07_FORMAL_CONSTRUCTIONS/
    │   ├── fiber_bundle_model.md
    │   ├── graph_model.md
    │   ├── holonomy_example.md
    │   └── manifold_model.md
    ├── 08_TOY_MODELS/
    │   ├── fig_sigma2_toy_schematic.pdf
    │   ├── fig_sigma2_toy_schematic.png
    │   ├── fig_sigma2_toy_schematic.py
    │   ├── oscillator_phase_gate.md
    │   ├── oscillator_phase_gate_demo.py
    │   ├── toy_md_viability_sigma2.py
    │   └── toy_md_viability_sigma2_note.md
    ├── second_order_organization_admissible_trajectories.tex
    ├── docs
    │   └── position
    │       ├── POSITION_RELATION_TO_BIOLOGICAL_COMPUTATIONALISM.md
    │       └── POSITION_RELATION_TO_ENACTIVISM_AND_DYNAMICAL_SYSTEMS.md
    ├── make_paper.sh
    ├── LICENSE
    └── PAPER_LICENSE.md

Only files that are **structurally locked** or **diagnostically definitive** should live here.

---

## The paper

The theoretical framework is developed in:

**Second-Order Organization as Constraint Geometry Over Admissible Trajectories**

The paper includes:
- the formal definition of Σ₂
- the proto → true second-order boundary
- operational hallmarks (noncommutativity, holonomy, failed Markov closure)
- a minimal stochastic grounding example

---

## Build the paper

Run:

    ./make_paper.sh

Output:

    build/second_order_organization_admissible_trajectories.pdf

---

## Versioning discipline

- **MAJOR** version changes break axioms or definitions
- **MINOR** versions add compatible structure or diagnostics
- **PATCH** versions clarify language only

Axioms may not be silently edited.

---

## Position notes (contextual, non-formal)

This repository includes a small set of **position notes** under `docs/position/` that clarify how the Σ₂ framework relates to adjacent theoretical traditions.

These documents are:
- **not part of the Σ₂ formalism**,  
- **not required to use or apply the framework**,  
- **not normative or prescriptive**.

They exist solely to prevent category errors and to support accurate cross-framework interpretation.

Current position notes include:
- `POSITION_RELATION_TO_BIOLOGICAL_COMPUTATIONALISM.md`
- `POSITION_RELATION_TO_ENACTIVISM_AND_DYNAMICAL_SYSTEMS.md`

No definitions, axioms, or commitments originate in these documents.

---

## License

All written material and figures are released under **CC BY 4.0**.

Reuse is permitted with attribution. No solicitation or endorsement is implied.

---

## Citation

If you use this work, please cite it as:

> Wells, A. R. (2026). *Second-Order Organization as Constraint Geometry Over Admissible Trajectories*. Dual-Frame Research Group. Zenodo. https://doi.org/10.5281/zenodo.18124930

This work is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.
