# Orders of Organization

**Document role:** Normative definitions (Σ₂ structural layer only)  
**Applies to:** All uses of “order” in this framework  
**Status:** Frozen at MAJOR version v0.x

---

## 1. Purpose

This document defines **first-, second-, and third-order organization** in a way that is:

- categorical (not gradual or scalar),
- independent of scale, complexity, or substrate,
- resistant to collapse or reinterpretation,
- sufficient to classify **ordering-relevance regimes and representational requirements**
  across physical, engineered, and biological **subsystems and motifs**.

These definitions are **structural**, not phenomenological.

**Scope note (2026):** This repository defines the Σ₂ structural layer only.
While biological and cognitive systems may contain Σ₂-type phenomena, organism-level
biology and cognition require higher-order closure beyond Σ₂ (provisionally Σ₅+).
Accordingly, this document does not certify organism-level biological or cognitive
classification. See `SIGMA_ORDER_SCOPE_CORRECTION_2026.md` for the normative scope statement.

---

## 2. What “order” means in this framework

### 2.1 Order is not scale

Order does **not** refer to:

- size (micro vs. macro),
- number of components,
- computational complexity,
- evolutionary advancement,
- degree of sophistication or intelligence.

A small system may be higher order than a large one.

---

### 2.2 Order is not descriptive convenience

Order is not an epistemic label or modeling choice.  
It reflects the **minimal ontological structure required for persistence of function
under admissible perturbation**.

---

### 2.3 Formal definition of order

**Definition (Order):**  
The order of a system is defined by the *lowest-level primitive required to specify
persistence of function*.

This definition is **exclusive and exhaustive**.

This definition applies structurally and does not certify biological or cognitive
sufficiency at the Σ₂ layer.

---

## 3. First-order organization (S-frame)

### 3.1 Definition

A system is **first order** if and only if:

1. Its future evolution is fully determined by its instantaneous state.
2. Time enters only as an external, parametric index.
3. All functional memory is representable as stored state.

Formally, a complete description exists of the form:

    x(t + Δt) = F(x(t), t)

where all causally relevant history is encoded in x(t).

---

### 3.2 Characteristic properties

First-order systems exhibit:

- state-based causation,
- Markovian evolution (given full state),
- immediate interaction,
- local causality,
- continuous dissipation,
- conservation applied to instantaneous quantities.

---

### 3.3 What first order cannot do

First-order systems cannot:

- distinguish histories that share identical states,
- deploy energy conditionally on trajectory class,
- exhibit intrinsic memory without stored state,
- gate dynamics based on past path rather than present configuration.

Any system that appears to do so requires higher order.

---

## 4. Second-order organization (T-frame)

### 4.1 Definition

A system is **second order** if and only if:

1. Two instances may share identical instantaneous state.
2. Their future evolution differs due to unreduced trajectory history.
3. That history cannot be represented as stored state without loss of function.

This criterion is decisive.

---

### 4.2 Core distinguishing feature

Second order is defined by **trajectory dependence**, not by extended duration or refined timing.

Second-order systems respond to:

    (state, path)

not to state alone.

---

### 4.3 Formal minimal structure

Second-order organization minimally requires:

- at least one second-order variable φ,
- whose evolution depends on accumulated process,
- and which gates, biases, or conditions first-order dynamics.

Minimal schematic:

    x-dot = F(x; φ)
    φ-dot = Ω(x, φ)

This form is illustrative, not restrictive.

---

### 4.4 Second-order time (Τ₂)

Second-order “time” is not clock time.

It consists of:

- ordering of transformations,
- irreversible accumulation of constraint,
- trajectory-sensitive organization.

Second-order time:

- need not be monotonic,
- need not be global,
- need not map injectively to first-order time.

---

### 4.5 Second-order space (Σ₂ analog)

Second-order systems necessarily instantiate a **space-like analog** enabling:

- differentiation of possibilities,
- compatibility and incompatibility,
- competition among trajectories,
- basin structure and selection.

This space is:

- relational, not metric,
- topological, not extended,
- implicit and unrepresented at second order.

---

### 4.6 What second order is not

Second order is not:

- slower first-order dynamics,
- finer-grained clocking,
- extended memory buffers,
- analog state storage,
- disembodied temporal or organizational fields.

Any such interpretation is incompatible.

---

## 5. Third-order organization (structural definition only)

**Status:** Structural definition provided for completeness only.  
**Non-normative at the Σ₂ layer.**

### 5.1 Definition

A system is **third order** if and only if:

1. It contains second-order organization, and
2. It represents elements of that organization as objects of internal control,
   manipulation, or reasoning.

Third order is **representation of organization**, not merely organization itself.

This definition establishes structural relationships between orders but does
not certify biological or cognitive classification within this repository.

---

### 5.2 Core properties (structural)

Third-order systems exhibit:

- internal representation of trajectory-conditioned organization,
- manipulation of organizational structure as objects,
- decoupling from immediate trajectory enforcement.

These properties are defined structurally and do not imply any specific substrate.

---

## 6. Order transitions

### 6.1 First → Second

Occurs when:

- persistence or function can no longer be specified by state alone,
- trajectory dependence becomes causally relevant.

This transition does **not** require representation, awareness, or cognition.

---

### 6.2 Second → Third

Occurs when:

- organizational structure itself becomes internally manipulable.

This definition is structural and does not certify organism-level biological or cognitive transitions within this repository.

---

## 7. Mixed-order systems

Real systems may contain multiple orders simultaneously.

Rules:

- Higher order does not eliminate lower order.
- Lower order provides substrate for higher order.
- Classification is based on **what is required**, not what is present.

---

## 8. Classification constraint

A system must be classified by the **highest order required for correct structural description of its persistence and organization**.

This classification rule applies structurally and does not imply organism-level biological or cognitive sufficiency within the Σ₂ layer.

---

## 9. Prohibitions

The following are forbidden:

- redefining order as complexity or intelligence,
- collapsing second order into refined clock time,
- treating second-order structure as stored representation,
- attributing higher-order sufficiency without explicit structural justification,
- skipping order definitions in downstream work.

---

## 10. Status

These definitions are **foundational for the Σ₂ structural layer**.

Any extension or application must:

- use these definitions verbatim, or
- explicitly declare incompatibility.

Interpretation of organism-level biology or cognition requires higher-order
framework layers beyond Σ₂.
