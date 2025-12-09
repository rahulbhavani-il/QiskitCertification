# Section 1: Quantum Operations (16% of Exam)

> **Exam Weight**: ~11 questions | **Difficulty**: Foundation | **Must Master**: ✅

---

## 📖 Overview

This section covers **single and multi-qubit gate operations** - the fundamental building blocks of all quantum circuits. Understanding these operations is critical for the certification exam and practical quantum programming.

### What You'll Learn

1. **Single-Qubit Gates**: X, Y, Z, H, S, T, P, RX, RY, RZ
2. **Multi-Qubit Gates**: CNOT, CZ, SWAP, Toffoli, Fredkin
3. **State Preparation**: `initialize()`, `reset()`, `barrier()`

---

## 🎯 Conceptual Foundation

### 🧠 Conceptual Deep Dive

#### Analogy: The Spinning Coin
Imagine a coin spinning on a table.
- **Classical Bit**: The coin is either flat on "Heads" (0) or "Tails" (1).
- **Superposition**: While spinning, the coin is in a state of "Heads AND Tails" simultaneously. It has a probability of landing on either.
- **Measurement**: Slapping the coin down forces it to choose a state. You can never see the "spinning" state directly, only the result.
- **Phase**: The direction the coin is facing while spinning (e.g., facing the window vs. the door). This doesn't change the probability of Heads/Tails, but it affects how it interacts with other coins.

#### Global Phase vs. Relative Phase
- **Global Phase**: Rotating the entire universe by 90 degrees. No one notices. Physically irrelevant. $| \psi \rangle \equiv e^{i\theta} | \psi \rangle$.
- **Relative Phase**: Rotating *one* qubit relative to another. This causes **interference** (constructive or destructive) and is the secret sauce of quantum algorithms.

### The Qubit: Building Block of Quantum Computing

A qubit exists in a superposition of states |0⟩ and |1⟩:

```
|ψ⟩ = α|0⟩ + β|1⟩

where |α|² + |β|² = 1 (normalization)
```

**Visual Representation - The Bloch Sphere**:

```
                |0⟩ (North Pole)
                 ↑
                 |
            +----+----+
           /     |     \
          /      |      \
         /       |       \
        /        |        \
       |         |         |  ← Equator: |+⟩, |-⟩, |+i⟩, |-i⟩
        \        |        /
         \       |       /
          \      |      /
           \     |     /
            +----+----+
                 |
                 ↓
                |1⟩ (South Pole)

• North pole: |0⟩ = [1, 0]
• South pole: |1⟩ = [0, 1]
• Equator (+X): |+⟩ = (|0⟩+|1⟩)/√2
• Equator (-X): |-⟩ = (|0⟩-|1⟩)/√2
• Equator (+Y): |+i⟩ = (|0⟩+i|1⟩)/√2
• Equator (-Y): |-i⟩ = (|0⟩-i|1⟩)/√2
```

---

## 🔧 Single-Qubit Gates

### Pauli Gates (X, Y, Z)

**Pauli-X Gate** (Bit Flip / NOT Gate)

```
Matrix:          Effect:          Bloch Sphere:
┌     ┐         |0⟩ → |1⟩         Rotation π around X-axis
│ 0 1 │         |1⟩ → |0⟩         
│ 1 0 │                          |0⟩ ──X──> |1⟩
└     ┘

Qiskit: qc.x(qubit)
```

**Pauli-Z Gate** (Phase Flip)

```
Matrix:          Effect:          Bloch Sphere:
┌      ┐         |0⟩ → |0⟩        Rotation π around Z-axis
│ 1  0 │         |1⟩ → -|1⟩       
│ 0 -1 │         |+⟩ → |-⟩        |+⟩ ──Z──> |-⟩
└      ┘

Qiskit: qc.z(qubit)
```

**Pauli-Y Gate** (Combined Flip)

```
Matrix:          Effect:          Bloch Sphere:
┌      ┐         |0⟩ → i|1⟩       Rotation π around Y-axis
│ 0 -i │         |1⟩ → -i|0⟩      
│ i  0 │                          Y = iXZ
└      ┘

Qiskit: qc.y(qubit)
```

### Hadamard Gate (MOST IMPORTANT!)

**The Superposition Creator**

```
Matrix:                Effect:              Circuit:
     ┌       ┐         |0⟩ → (|0⟩+|1⟩)/√2   ───H───
1/√2 │ 1  1  │         |1⟩ → (|0⟩-|1⟩)/√2   
     │ 1 -1  │         
     └       ┘         Creates equal superposition!

Qiskit: qc.h(qubit)

KEY PROPERTY: H·H = I (Hadamard is self-inverse)
EXAM TIP: Appears in 80%+ of quantum algorithms!
```

**Visual Effect**:

```
Before H:               After H:
  |0⟩                   (|0⟩+|1⟩)/√2 = |+⟩
   ↓                         ↓
   •                         •
   |                        /|\
   |                       / | \
  100%                   50%  50%
  at |0⟩               |0⟩  |1⟩
```

### Phase Gates (S, T, P)

**S Gate** (Phase by π/2)

```
Matrix:          Relation:        Circuit:
┌     ┐         S² = Z            ───S───
│ 1 0 │         S† = S†           
│ 0 i │                           
└     ┘         

Qiskit: qc.s(qubit) or qc.sdg(qubit) for S†
```

**T Gate** (Phase by π/4)

```
Matrix:              Relation:        Circuit:
┌          ┐         T⁴ = Z           ───T───
│ 1   0    │         T² = S           
│ 0  e^(iπ/4) │      T† = T†          
└          ┘         

Qiskit: qc.t(qubit) or qc.tdg(qubit) for T†
```

**P Gate** (Arbitrary Phase)

```
Matrix:          Parameter:       Circuit:
┌         ┐      λ = phase angle   ───P(λ)───
│ 1   0   │      
│ 0  e^iλ │      λ=π/2 → S
└         ┘      λ=π/4 → T
                 λ=π → Z

Qiskit: qc.p(lambda, qubit)
```

### Rotation Gates (RX, RY, RZ)

**Parameterized rotations around Bloch sphere axes**

```
RX(θ):                   RY(θ):                   RZ(θ):
┌              ┐         ┌              ┐         ┌            ┐
│ cos(θ/2)  -i·sin(θ/2)│ │ cos(θ/2) -sin(θ/2)│   │ e^(-iθ/2)  0    │
│-i·sin(θ/2) cos(θ/2) │ │ sin(θ/2)  cos(θ/2)│   │  0      e^(iθ/2)│
└              ┘         └              ┘         └            ┘

Rotate θ radians         Rotate θ radians         Rotate θ radians
around X-axis            around Y-axis            around Z-axis

Special cases:           Special cases:           Special cases:
RX(π) = X               RY(π) = Y                RZ(π) = Z
RX(π/2) = √X            RY(π/2) = creates        RZ(π/2) = S
                        superposition

Qiskit: qc.rx(theta, qubit)  |  qc.ry(theta, qubit)  |  qc.rz(theta, qubit)
```

**Usage Pattern**:

```python
# Variational quantum algorithms (VQE, QAOA)
from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(1)
theta = np.pi/4  # Parameter to optimize

# Common variational ansatz pattern
qc.ry(theta, 0)  # Y rotation
qc.rz(theta, 0)  # Z rotation
```

---

## 🔗 Multi-Qubit Gates

### CNOT Gate (Controlled-NOT) - MOST CRITICAL!

**Creates entanglement between qubits**

```
Circuit:          Matrix (4×4):              Truth Table:
                  ┌         ┐               |q0,q1⟩ → |q0, q1⊕q0⟩
q0: ──●──         │1 0 0 0  │               
      │           │0 1 0 0  │               |00⟩ → |00⟩
q1: ──⊕──         │0 0 0 1  │               |01⟩ → |01⟩
                  │0 0 1 0  │               |10⟩ → |11⟩ ✓ flip!
Control  Target   └         ┘               |11⟩ → |10⟩ ✓ flip!

Qiskit: qc.cx(control, target)  or  qc.cnot(control, target)

EXAM TIP: CNOT flips target IF control is |1⟩
```

**Creating Bell States (Maximally Entangled)**:

```
Circuit:                    State Evolution:
     ┌───┐                  
q0: ─┤ H ├──●──             |00⟩ ──H⊗I──> (|0⟩+|1⟩)|0⟩/√2
     └───┘  │                     ──CX──> (|00⟩+|11⟩)/√2 = |Φ⁺⟩
q1: ────────⊕──             
                            Bell State |Φ⁺⟩ (EPR pair)
Qiskit:                     Perfect correlation: measure q0→q1 same result!
qc.h(0)
qc.cx(0, 1)

**Other Three Bell States**:

|Φ⁻⟩ Circuit:                State Evolution:
     ┌───┐     ┌───┐
q0: ─┤ H ├──●──┤ Z ├──      |00⟩ ──H⊗I──> (|0⟩+|1⟩)|0⟩/√2
     └───┘  │  └───┘             ──CX──> (|00⟩+|11⟩)/√2
q1: ────────⊕─────────           ──Z──> (|00⟩-|11⟩)/√2 = |Φ⁻⟩

Qiskit:                     Bell State |Φ⁻⟩ (phase flip)
qc.h(0)                     Anti-correlation in phase
qc.cx(0, 1)
qc.z(0)

|Ψ⁺⟩ Circuit:                State Evolution:
     ┌───┐
q0: ─┤ H ├──●─────────      |00⟩ ──H⊗I──> (|0⟩+|1⟩)|0⟩/√2
     └───┘  │                    ──CX──> (|00⟩+|11⟩)/√2
            │  ┌───┐             ──X──> (|01⟩+|10⟩)/√2 = |Ψ⁺⟩
q1: ────────⊕──┤ X ├──
               └───┘
Qiskit:                     Bell State |Ψ⁺⟩ (bit flip)
qc.h(0)                     Perfect anti-correlation: if q0=0 then q1=1
qc.cx(0, 1)
qc.x(1)

|Ψ⁻⟩ Circuit:                State Evolution:
     ┌───┐     ┌───┐
q0: ─┤ H ├──●──┤ Z ├──      |00⟩ ──H⊗I──> (|0⟩+|1⟩)|0⟩/√2
     └───┘  │  └───┘             ──CX──> (|00⟩+|11⟩)/√2
            │  ┌───┐             ──X──> (|01⟩+|10⟩)/√2
q1: ────────⊕──┤ X ├──           ──Z──> (|01⟩-|10⟩)/√2 = |Ψ⁻⟩
               └───┘
Qiskit:                     Bell State |Ψ⁻⟩ (bit + phase flip)
qc.h(0)                     Anti-correlation with phase
qc.cx(0, 1)
qc.x(1)
qc.z(0)

EXAM ESSENTIAL: Know all four Bell states by heart!
```



### Controlled-Z Gate (CZ)

```
Circuit:          Matrix:                Effect:
                  ┌         ┐           Adds -1 phase to |11⟩
q0: ──●──         │1 0 0  0 │           
      │           │0 1 0  0 │           Symmetric: CZ(0,1) = CZ(1,0)
q1: ──●──         │0 0 1  0 │           
                  │0 0 0 -1 │           
                  └         ┘           

Qiskit: qc.cz(control, target)

Relation: CZ = H·CNOT·H (on target)
```

### SWAP Gate

```
Circuit:          Matrix:                Effect:
                  ┌         ┐           Exchanges qubit states
q0: ──×──         │1 0 0 0  │           
      │           │0 0 1 0  │           |01⟩ ↔ |10⟩
q1: ──×──         │0 1 0 0  │           
                  │0 0 0 1  │           
                  └         ┘           

Qiskit: qc.swap(qubit1, qubit2)

Decomposition: SWAP = CX(a,b)·CX(b,a)·CX(a,b)
```

### Toffoli Gate (CCNOT / CCX)

**3-qubit gate: Double-controlled NOT**

```
Circuit:          Effect:
                  
q0: ──●──         Flips q2 IF both q0 AND q1 are |1⟩
      │           
q1: ──●──         |110⟩ → |111⟩
      │           |111⟩ → |110⟩
q2: ──⊕──         All others unchanged

Qiskit: qc.ccx(control1, control2, target)  or  qc.toffoli(...)

USE CASE: Classical logic in quantum circuits (AND gate)
```

---

## 🎨 State Preparation

### Initialize State

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)

# Prepare custom state
state = [1/2, 1/2, 1/2, 1/2]  # Equal superposition
qc.initialize(state, [0, 1])

# PURPOSE:
# 1. Create arbitrary quantum states directly
# 2. Useful for algorithm initialization (e.g., VQE, QAOA)
# 3. Automatically normalizes if |state| ≠ 1
# 4. EXAM NOTE: Adds gates behind the scenes to create this state
```

### Reset Qubit

```python
qc = QuantumCircuit(1)
qc.x(0)        # |1⟩
qc.reset(0)    # Back to |0⟩ (measurement + conditional X)

# PURPOSE:
# 1. Reuse qubits mid-circuit (important for limited hardware)
# 2. Reset to ground state |0⟩ regardless of current state
# 3. Enables qubit recycling in long computations
# 4. Implemented via measurement + conditional X flip
```

### Barrier

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.barrier()   # ┈┈┈┈┈┈┈┈ (visual separator)
qc.cx(0, 1)

# PURPOSE: 
# 1. Visual clarity in circuit diagrams
# 2. Prevents transpiler optimization across barrier
# 3. No effect on quantum state!
```

---

## 📊 Common Patterns & Exam Tips

### Pattern 1: Creating Superposition

```python
# Single qubit superposition
qc.h(0)  # |0⟩ → |+⟩ = (|0⟩+|1⟩)/√2

# Multi-qubit superposition (all 2^n states)
for i in range(n):
    qc.h(i)
# Result: (|00...0⟩ + |00...1⟩ + ... + |11...1⟩) / √(2^n)
```

### Pattern 2: Entanglement

```python
# Bell state (2-qubit entanglement)
qc.h(0)
qc.cx(0, 1)  # |Φ⁺⟩ = (|00⟩+|11⟩)/√2

# GHZ state (n-qubit entanglement)
qc.h(0)
for i in range(n-1):
    qc.cx(i, i+1)
# Result: (|00...0⟩ + |11...1⟩) / √2
```

### Pattern 3: Phase Kickback

```python
# Used in algorithms (Deutsch-Jozsa, Grover, etc)
qc.h(0)        # Control in superposition
qc.x(1)        # Target
qc.h(1)        # Target in |-⟩
qc.cx(0, 1)    # Phase kickback to control!
```

---

## ✅ Exam Quick Reference

### Must Memorize

| Gate | Matrix | Effect on |0⟩ | Effect on |1⟩ | Qiskit |
|------|--------|------------|------------|--------|
| X | [[0,1],[1,0]] | |1⟩ | |0⟩ | `qc.x(q)` |
| Z | [[1,0],[0,-1]] | |0⟩ | -|1⟩ | `qc.z(q)` |
| H | [[1,1],[1,-1]]/√2 | (|0⟩+|1⟩)/√2 | (|0⟩-|1⟩)/√2 | `qc.h(q)` |
| S | [[1,0],[0,i]] | |0⟩ | i|1⟩ | `qc.s(q)` |
| T | [[1,0],[0,e^(iπ/4)]] | |0⟩ | e^(iπ/4)|1⟩ | `qc.t(q)` |
| CX | 4×4 | |00⟩,|01⟩ unchanged | |10⟩→|11⟩, |11⟩→|10⟩ | `qc.cx(c,t)` |

### 🎓 Exam Question Patterns (MEMORIZE THESE!)

**Pattern 1: "What does this circuit produce?"**
```python
qc.h(0); qc.cx(0,1)  → Bell state (|00⟩+|11⟩)/√2
qc.h(0); qc.h(1)     → Product state (|00⟩+|01⟩+|10⟩+|11⟩)/2
qc.x(0); qc.h(0)     → |-⟩ = (|0⟩-|1⟩)/√2
```

**Pattern 2: "Which gates commute?"**
```python
✅ X and X (same gate): X² = I
✅ Z on different qubits: Z₀Z₁ = Z₁Z₀
❌ X and Z: XZ ≠ ZX (they anticommute!)
❌ H and S: HS ≠ SH
```

**Pattern 3: "What is the matrix of...?"**
- If unsure, apply to basis states: Gate|0⟩ and Gate|1⟩
- X: swaps components → [[0,1],[1,0]]
- Z: adds minus to |1⟩ → [[1,0],[0,-1]]
- H: creates superposition → [[1,1],[1,-1]]/√2

**Pattern 4: "How many gates needed for...?"**
```python
Bell state: 2 gates (H + CX)
GHZ state (n qubits): n gates (1 H + n-1 CX)
SWAP: 3 gates (3 CNOTs)
Toffoli: 6 CX gates (hardware decomposition)
```

### 🧠 Mnemonics for Perfect Recall

**"X-Men Flip, Z-Men Phase"**
- X flips between |0⟩ and |1⟩
- Z adds phase (minus sign) to |1⟩

**"Hadamard Makes Plus"**
- H|0⟩ = |+⟩ (plus state)
- H|1⟩ = |-⟩ (minus state)

**"Phase Powers: S-Squared, T-Forth"**
- S² = Z (S twice is Z)
- T⁴ = Z (T four times is Z)

**"Control BEFORE Target"**
- CX(control, target) - control is FIRST parameter
- CX(0, 1) means: q0 controls, q1 is flipped

**"Barriers Block, Reset Returns"**
- barrier() = visual only, blocks optimization
- reset() = active operation, returns to |0⟩

### Gate Equivalences

```
X = HZH
H = (X+Z)/√2
S² = Z
T⁴ = Z
RX(π) = X
RY(π) = Y
RZ(π) = Z
SWAP = CX(a,b)·CX(b,a)·CX(a,b)
```

### Critical Exam Facts

1. ✅ H creates superposition: |0⟩ → |+⟩ = (|0⟩+|1⟩)/√2
2. ✅ CNOT creates entanglement: H(q0) + CX(q0,q1) = Bell state
3. ✅ X flips |0⟩↔|1⟩, Z adds phase -1 to |1⟩
4. ✅ Phase gates (S,T,P) don't change populations, only phases
5. ✅ Rotation gates are parameterized: RY(θ), RZ(φ)
6. ✅ Toffoli = double-controlled X (AND gate in quantum)
7. ✅ `barrier()` prevents optimization, doesn't change state
8. ✅ `reset()` returns qubit to |0⟩ (measurement + conditional flip)

### ⚠️ Common Exam Traps

**Trap 1: Gate Commutativity**

**Definition**:
- **Commutative operations**: Order doesn't matter → `AB = BA`
- **Non-commutative operations**: Order matters → `AB ≠ BA`

**Visual Explanation**:
```
Commutative (Order doesn't matter):
  Gate A → Gate B  =  Gate B → Gate A
     |0⟩ → A → B       |0⟩ → B → A
          ↓                  ↓
      Same Result        Same Result

Non-Commutative (Order matters!):
  Gate A → Gate B  ≠  Gate B → Gate A
     |0⟩ → A → B       |0⟩ → B → A
          ↓                  ↓
    Different Result   Different Result
```

**Decision Tree - Do Gates Commute?**
```
                    Two Gates (A and B)
                           |
                 ┌─────────┴─────────┐
                 │                   │
          Same Qubit?          Different Qubits?
                 │                   │
         ┌───────┴────────┐          │
         │                │          └──> ✓ Always Commute
    Same Gate?    Different Gates?
         │                │
         │                │
    ✓ Commute      Check if matrices
    (X·X = I)      multiply same way
                         |
                   ┌─────┴─────┐
                   │           │
              ✓ Commute    ✗ Don't Commute
              (Z·S = S·Z)  (X·Z ≠ Z·X)
```

**Examples**:

```python
# ✅ COMMUTATIVE Examples:

# 1. Same gate (idempotent or self-inverse)
qc.x(0); qc.x(0)  ==  I  # X² = I (cancel out)
qc.h(0); qc.h(0)  ==  I  # H² = I (self-inverse)

# 2. Different qubits (always commute)
qc.z(0); qc.z(1)  ==  qc.z(1); qc.z(0)  # No interaction
qc.x(0); qc.h(1)  ==  qc.h(1); qc.x(0)  # Operate independently

# 3. Diagonal gates (phase gates commute with each other)
qc.z(0); qc.s(0)  ==  qc.s(0); qc.z(0)  # Both diagonal
qc.s(0); qc.t(0)  ==  qc.t(0); qc.s(0)  # Both phase gates

# ❌ NON-COMMUTATIVE Examples:

# 1. Pauli X and Z (anticommute)
qc.x(0); qc.z(0)  ≠  qc.z(0); qc.x(0)  # XZ = -ZX (phase difference!)

# 2. Hadamard with phase gates
qc.h(0); qc.s(0)  ≠  qc.s(0); qc.h(0)  # HS ≠ SH

# 3. Rotations around different axes
qc.rx(π/4, 0); qc.ry(π/4, 0)  ≠  qc.ry(π/4, 0); qc.rx(π/4, 0)
```

**Commutativity Table** (same qubit):

| Gates | Commute? | Reason |
|-------|----------|--------|
| X, X | ✅ Yes | X² = I |
| Z, Z | ✅ Yes | Z² = I |
| H, H | ✅ Yes | H² = I |
| Z, S | ✅ Yes | Both diagonal (phase gates) |
| S, T | ✅ Yes | Both diagonal (phase gates) |
| **X, Z** | ❌ **No** | **XZ = -ZX (anticommute)** |
| **X, Y** | ❌ **No** | **XY = iZ** |
| **Y, Z** | ❌ **No** | **YZ = iX** |
| **H, S** | ❌ **No** | **HS ≠ SH** |
| **H, X** | ❌ **No** | **HXH = Z** |

**Mathematical Test**:
```
Two gates A and B commute if:
  AB = BA  (or equivalently, [A,B] = AB - BA = 0)

Example - X and Z don't commute:
  XZ|0⟩ = X|0⟩ = |1⟩
  ZX|0⟩ = Z|1⟩ = -|1⟩
  → XZ ≠ ZX (differ by minus sign)
```

**Trap 2: CNOT Direction Matters**
```python
qc.cx(0, 1)  ≠  qc.cx(1, 0)  # Control ≠ Target
# |10⟩ ─CX(0,1)→ |11⟩  BUT  |10⟩ ─CX(1,0)→ |10⟩ (no change!)
```

**Trap 3: Phase Gate Powers**
```python
S² = Z   # NOT S² = I
T⁴ = Z   # NOT T² = Z (that's S!)
S†·S = I  # Inverse cancels
```

**Trap 4: Initialize vs Reset**
```python
qc.initialize([1, 0], 0)  # Sets to |0⟩, but adds many gates
qc.reset(0)                # Also sets to |0⟩, but uses measurement
# initialize() = synthesis, reset() = active reset
```

---

## 🔍 Practice Questions

### Q1: What is the result of applying H then X then H to |0⟩?

<details>
<summary>Click for answer</summary>

**Answer**: |1⟩

**Explanation**:
- H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2
- X|+⟩ = X(|0⟩+|1⟩)/√2 = (|1⟩+|0⟩)/√2 = |+⟩
- H|+⟩ = |0⟩

Wait, that's wrong! Let me recalculate:
- H|0⟩ = (|0⟩+|1⟩)/√2
- X flips: (|1⟩+|0⟩)/√2 = (|0⟩+|1⟩)/√2
- H again: H·H = I, so back to... actually:

Actually: HXH = Z (this is a gate equivalence!)
So HXH|0⟩ = Z|0⟩ = |0⟩

**Correct Answer: |0⟩** ✓
</details>

### Q2: How many CNOT gates are needed to create a Bell state?

<details>
<summary>Click for answer</summary>

**Answer**: 1 CNOT gate (plus 1 Hadamard)

```python
qc.h(0)     # Create superposition
qc.cx(0,1)  # Create entanglement → Bell state |Φ⁺⟩
```
</details>

### Q3: What's the difference between X and Z gates?

<details>
<summary>Click for answer</summary>

- **X gate**: Bit flip - exchanges |0⟩↔|1⟩ (rotation around X-axis)
- **Z gate**: Phase flip - keeps |0⟩, adds -1 phase to |1⟩ (rotation around Z-axis)

On computational basis: X changes populations, Z changes phases
On superposition: X: |+⟩→|+⟩, |-⟩→|-⟩ vs Z: |+⟩→|-⟩, |-⟩→|+⟩
</details>

---

## 📁 Files in This Section

1. **`single_qubit_gates.py`** - X, Y, Z, H, S, T, P, RX, RY, RZ implementations
2. **`multi_qubit_gates.py`** - CNOT, CZ, SWAP, Toffoli, Bell states
3. **`state_preparation.py`** - initialize(), reset(), barrier()

---

## 🎯 Next Steps

1. Run each Python file to see gates in action
2. Memorize the gate matrices (X, Z, H, S, T)
3. Practice creating Bell states and GHZ states
4. Understand Bloch sphere rotations
5. Move to Section 2 (Visualization) to see these gates visually

**Master this section = Foundation for entire certification!** 🚀
