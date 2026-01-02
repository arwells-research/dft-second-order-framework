# Orders of Organization

**Document role:** Normative definitions  
**Applies to:** All uses of “order” in this framework  
**Status:** Frozen at MAJOR version v0.x

---

## 1. Purpose

This document defines **first-, second-, and third-order organization** in a way that is:

- categorical (not gradual or scalar),
- independent of scale, complexity, or substrate,
- resistant to collapse or reinterpretation,
- sufficient to classify biological, cognitive, artificial, and physical systems.

These definitions are **structural**, not phenomenological.

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
It reflects the **minimal ontological structure required for persistence of function under admissible perturbation**.

---

### 2.3 Formal definition of order

**Definition (Order):**  
The order of a system is defined by the *lowest-level primitive required to specify persistence of function*.

This definition is **exclusive and exhaustive**.

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

## 5. Third-order organization

### 5.1 Definition

A system is **third order** if and only if:

1. It contains second-order organization, and
2. It represents elements of that organization as objects of cognition or control.

Third order is **representation of organization**.

---

### 5.2 Core properties

Third-order systems exhibit:

- explicit modeling of internal trajectories,
- navigation of organizational space,
- decoupling from immediate drive,
- symbolic manipulation or abstraction,
- meta-stability across contexts.

---

### 5.3 Spatiality of ideas

The experienced spatial arrangement of ideas belongs **exclusively** to third order.

Second-order organization may have space-like structure, but it is not experienced as space.

---

## 6. Order transitions

### 6.1 First → Second

Occurs when:

- persistence or function can no longer be specified by state alone,
- trajectory dependence becomes causally relevant.

This transition does **not** require reflection, representation, or awareness.

---

### 6.2 Second → Third

Occurs when:

- the system represents its own second-order structure,
- internal trajectories become manipulable objects.

This transition is discrete, not gradual.

---

## 7. Mixed-order systems

Real systems may contain multiple orders simultaneously.

Rules:

- Higher order does not eliminate lower order.
- Lower order provides substrate for higher order.
- Classification is based on **what is required**, not what is present.

---

## 8. Classification constraint

A system must be classified by the **highest order required for correct description**.

If second-order structure is required to explain behavior, the system is second order even if first-order descriptions are locally valid.

---

## 9. Prohibitions

The following are forbidden:

- redefining order as complexity or intelligence,
- collapsing second order into subjective or experiential time,
- attributing third-order properties to second-order systems,
- skipping order definitions in downstream work.

---

## 10. Status

These definitions are **foundational**.

Any extension or application must:
- use these definitions verbatim,
- or explicitly declare incompatibility.

No reinterpretation is permitted without a MAJOR version change.