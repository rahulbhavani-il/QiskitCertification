# Section 1: Quantum Operations (16% of Exam)

> **Exam Weight**: ~11 questions | **Difficulty**: Foundation | **Must Master**: ✅✅✅

---

## 📖 Overview

This section covers **single and multi-qubit gate operations** - the fundamental building blocks of all quantum circuits. Understanding these operations is critical for the certification exam and practical quantum programming.

### What You'll Learn

1. **Foundational Concepts**: Qubits, Bloch sphere, global vs relative phase
2. **Single-Qubit Gates**: X, Y, Z, H, S, T, P, RX, RY, RZ + Pauli Class
3. **Multi-Qubit Gates**: CNOT, CZ, SWAP, Toffoli, Fredkin, Bell States
4. **State Preparation**: `initialize()`, `reset()`, `barrier()`

---

## 🎯 Why This Section Matters (Conceptual Foundation)

### 🧠 Conceptual Deep Dive

#### Analogy: The Spinning Coin
- **Classical Bit**: Coin flat on table - either Heads (0) or Tails (1)
- **Qubit (Superposition)**: Coin spinning - both states simultaneously until measured
- **Measurement**: Slapping coin down forces it to choose - you never see the "spinning" state
- **Phase**: Direction coin faces while spinning - affects interference, not probabilities

#### Global Phase vs. Relative Phase
- **Global Phase**: Rotating entire universe by 90° - no one notices. $|ψ⟩ ≡ e^{iθ}|ψ⟩$
- **Relative Phase**: Rotating one component - causes interference! $|0⟩+|1⟩ ≠ |0⟩-|1⟩$

### Visual Overview: The Bloch Sphere

```
                |0⟩ (North Pole)
                 ↑
                 |
            +----+----+
           /     |     \
          /      |      \
         |       |       |  ← Equator: |+⟩, |-⟩, |+i⟩, |-i⟩
          \      |      /
           \     |     /
            +----+----+
                 |
                 ↓
                |1⟩ (South Pole)

• North pole: |0⟩    • South pole: |1⟩
• +X equator: |+⟩    • -X equator: |-⟩
• +Y equator: |+i⟩   • -Y equator: |-i⟩
```

---

## 📋 Topics Covered (Quick Reference)

| Topic | Description | Exam Weight | Priority |
|-------|-------------|-------------|----------|
| **Pauli Gates (X,Y,Z)** | Bit flip, phase flip, combined | High | 🔴 |
| **Hadamard (H)** | Superposition creator | High | 🔴 |
| **Phase Gates (S,T,P)** | Phase rotations | Medium | 🟡 |
| **Rotation Gates (RX,RY,RZ)** | Parameterized rotations | Medium | 🟡 |
| **Pauli Class** | Algebraic Pauli operations | High | 🔴 |
| **CNOT/CX** | Entanglement creator | High | 🔴 |
| **Bell States** | Maximally entangled states | High | 🔴 |
| **CZ, SWAP, Toffoli, Fredkin** | Other multi-qubit gates | Medium | 🟡 |
| **State Preparation** | initialize, reset, barrier | Low | 🟢 |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION 1 LEARNING PATH                       │
├─────────────────────────────────────────────────────────────────┤
│  START HERE                                                      │
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. SINGLE-QUBIT GATES                                        ││
│  │    └─ Pauli X, Y, Z → Hadamard → S, T, P → RX, RY, RZ       ││
│  │    └─ Pauli Class (quantum_info)                            ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 2. MULTI-QUBIT GATES                                         ││
│  │    └─ CNOT → Bell States → CZ → SWAP → Toffoli → Fredkin    ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 3. STATE PREPARATION                                         ││
│  │    └─ initialize() → reset() → barrier()                    ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  COMPLETE: Ready for Quantum Operations exam questions           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 SINGLE-QUBIT GATES

> **LEARNING FLOW**: Each gate follows: Definition → Analogy → Math → Implementation → ⚠️ Trap → 🧠 Mnemonic → ⚡ Quick Check

---

### 🔹 Pauli-X Gate (Bit Flip)

#### 1. Definition
The X gate flips the qubit state: |0⟩ ↔ |1⟩. It's a π rotation around the X-axis of the Bloch sphere.

#### 2. Analogy + Intuition
**Real-World Analogy**: A light switch - flips between ON and OFF states.

**Intuition**: X is the quantum NOT gate. Apply twice and you're back where you started (X² = I).

#### 3. Math + Visual
```
Matrix:          Effect:              Bloch Sphere:
┌     ┐         |0⟩ → |1⟩            π rotation around X-axis
│ 0 1 │         |1⟩ → |0⟩         
│ 1 0 │         X² = I               
└     ┘
```

#### 4. Implementation
```python
qc.x(qubit)  # Apply X gate
```

| Parameter | Type | Description |
|-----------|------|-------------|
| qubit | int/Qubit | Target qubit |

#### 5. ⚠️ Trap Alert
**Trap: X on superposition**
- ❌ **Wrong**: X always changes the state
- ✅ **Correct**: X|+⟩ = |+⟩ (unchanged!), X|-⟩ = |-⟩
- 🔍 **Why**: X swaps amplitudes, but |+⟩ has equal amplitudes

#### 6. 🧠 Mnemonic
> **"X-Men Flip bits"** - X flips between |0⟩ and |1⟩

#### 7. ⚡ Quick Check
**Q: What is X|0⟩?**
<details><summary>Answer</summary>|1⟩</details>

---

### 🔹 Pauli-Y Gate (Combined Flip)

#### 1. Definition
The Y gate combines bit flip and phase flip with complex phases. Y = iXZ.

#### 2. Analogy + Intuition
**Real-World Analogy**: A flip-and-twist move in gymnastics - rotates around Y-axis.

**Intuition**: Y does both X and Z operations with extra i phase factors.

#### 3. Math + Visual
```
Matrix:          Effect:              Relation:
┌      ┐        |0⟩ → i|1⟩           Y = iXZ
│ 0 -i │        |1⟩ → -i|0⟩          Y² = I
│ i  0 │        
└      ┘
```

#### 4. Implementation
```python
qc.y(qubit)  # Apply Y gate
```

#### 5. ⚠️ Trap Alert
**Trap: Y introduces complex phases**
- ❌ **Wrong**: Y just flips like X
- ✅ **Correct**: Y adds i and -i phases (not just ±1)

#### 6. 🧠 Mnemonic
> **"Y = iXZ combo"** - Y combines X and Z with i factor

#### 7. ⚡ Quick Check
**Q: What is the relation Y = ?**
<details><summary>Answer</summary>Y = iXZ</details>

---

### 🔹 Pauli-Z Gate (Phase Flip)

#### 1. Definition
The Z gate adds a -1 phase to |1⟩ while leaving |0⟩ unchanged. π rotation around Z-axis.

#### 2. Analogy + Intuition
**Real-World Analogy**: Invisible ink - changes the "hidden" phase, not the visible bit value.

**Intuition**: Z flips phases in the Hadamard basis: |+⟩ → |-⟩.

#### 3. Math + Visual
```
Matrix:          Effect:              Bloch Sphere:
┌      ┐        |0⟩ → |0⟩            π rotation around Z-axis
│ 1  0 │        |1⟩ → -|1⟩           
│ 0 -1 │        |+⟩ → |-⟩            Z² = I
└      ┘
```

#### 4. Implementation
```python
qc.z(qubit)  # Apply Z gate
```

#### 5. ⚠️ Trap Alert
**Trap: Z on computational basis**
- ❌ **Wrong**: Z flips |0⟩ to something else
- ✅ **Correct**: Z|0⟩ = |0⟩ (unchanged!)
- 🔍 **Why**: Z only adds phase to |1⟩ component

#### 6. 🧠 Mnemonic
> **"Z-Men flip Phase"** - Z changes phase, not bit

#### 7. ⚡ Quick Check
**Q: What is Z|0⟩?**
<details><summary>Answer</summary>|0⟩ (unchanged!)</details>

---

### 🔹 Hadamard Gate (H) - MOST IMPORTANT!

#### 1. Definition
Creates equal superposition from basis states. Self-inverse: H² = I. Appears in 80%+ of quantum algorithms!

#### 2. Analogy + Intuition
**Real-World Analogy**: A fair coin flipper - takes a definite state to 50/50 superposition.

**Intuition**: H is the "superposition creator" - the gateway to quantum parallelism.

#### 3. Math + Visual
```
Matrix:              Effect:              
     ┌       ┐      |0⟩ → |+⟩ = (|0⟩+|1⟩)/√2
1/√2 │ 1  1  │      |1⟩ → |-⟩ = (|0⟩-|1⟩)/√2
     │ 1 -1  │      H² = I (self-inverse)
     └       ┘      

Circuit:  ───H───
```

#### 4. Implementation
```python
qc.h(qubit)  # Create superposition

# Multi-qubit superposition (all 2^n states)
for i in range(n):
    qc.h(i)
```

#### 5. ⚠️ Trap Alert
**Trap: Hadamard conjugation**
- ❌ **Wrong**: HXH = X
- ✅ **Correct**: HXH = Z, HZH = X (swaps X and Z!)
- 🔍 **Why**: Hadamard transforms between X and Z bases

#### 6. 🧠 Mnemonic
> **"Hadamard Makes Plus"** - H|0⟩ = |+⟩

#### 7. ⚡ Quick Check
**Q: What is H|0⟩?**
<details><summary>Answer</summary>|+⟩ = (|0⟩+|1⟩)/√2</details>

---

### 🔹 S Gate (Phase by π/2)

#### 1. Definition
Adds π/2 phase to |1⟩. S² = Z. Also called √Z gate.

#### 2. Analogy + Intuition
**Real-World Analogy**: Quarter turn of a phase dial.

#### 3. Math + Visual
```
Matrix:          Relation:
┌     ┐         S² = Z
│ 1 0 │         S = P(π/2)
│ 0 i │         S† = Sdg
└     ┘
```

#### 4. Implementation
```python
qc.s(qubit)    # S gate
qc.sdg(qubit)  # S† (S-dagger, inverse)
```

#### 5. ⚠️ Trap Alert
**Trap: S squared**
- ❌ **Wrong**: S² = I
- ✅ **Correct**: S² = Z

#### 6. 🧠 Mnemonic
> **"S-Squared equals Z"**

#### 7. ⚡ Quick Check
**Q: What is S²?**
<details><summary>Answer</summary>Z</details>

---

### 🔹 T Gate (Phase by π/4)

#### 1. Definition
Adds π/4 phase to |1⟩. T⁴ = Z, T² = S. Also called √S or π/8 gate.

#### 2. Analogy + Intuition
**Real-World Analogy**: Eighth turn of a phase dial (half of S).

#### 3. Math + Visual
```
Matrix:              Relation:
┌          ┐        T⁴ = Z
│ 1   0    │        T² = S
│ 0  e^iπ/4│        T = P(π/4)
└          ┘
```

#### 4. Implementation
```python
qc.t(qubit)    # T gate
qc.tdg(qubit)  # T† (T-dagger, inverse)
```

#### 5. ⚠️ Trap Alert
**Trap: T powers**
- ❌ **Wrong**: T² = Z
- ✅ **Correct**: T⁴ = Z (T² = S)

#### 6. 🧠 Mnemonic
> **"T-Fourth equals Z"** (T⁴ = Z)

#### 7. ⚡ Quick Check
**Q: What is T²?**
<details><summary>Answer</summary>S</details>

---

### 🔹 P Gate (Arbitrary Phase)

#### 1. Definition
General phase gate P(λ) adding phase e^(iλ) to |1⟩. Generalizes S, T, Z.

#### 2. Analogy + Intuition
**Real-World Analogy**: Adjustable phase dial - set to any angle you want.

#### 3. Math + Visual
```
Matrix:              Special cases:
┌         ┐         P(π/2) = S
│ 1   0   │         P(π/4) = T
│ 0  e^iλ │         P(π) = Z
└         ┘
```

#### 4. Implementation
```python
qc.p(lambda_angle, qubit)  # P(λ) gate
```

| Parameter | Type | Description |
|-----------|------|-------------|
| lambda_angle | float | Phase angle in radians |
| qubit | int | Target qubit |

#### 5. ⚠️ Trap Alert
**Trap: P only affects |1⟩**
- P|0⟩ = |0⟩ (unchanged)
- P|1⟩ = e^(iλ)|1⟩

#### 6. 🧠 Mnemonic
> **"P for Parameterized Phase"**

#### 7. ⚡ Quick Check
**Q: What is P(π)?**
<details><summary>Answer</summary>Z gate</details>

---

### 🔹 Rotation Gates (RX, RY, RZ)

#### 1. Definition
Parameterized rotations by angle θ around X, Y, or Z axis of Bloch sphere.

#### 2. Analogy + Intuition
**Real-World Analogy**: Tilting a globe by angle θ around a specified axis.

**Intuition**: Essential for variational algorithms (VQE, QAOA) where angles are optimized.

#### 3. Math + Visual
```
RX(θ): Rotation θ around X    RY(θ): Rotation θ around Y    RZ(θ): Rotation θ around Z
┌                    ┐        ┌                  ┐          ┌              ┐
│ cos(θ/2) -i·sin(θ/2)│       │ cos(θ/2) -sin(θ/2)│         │e^(-iθ/2)  0  │
│-i·sin(θ/2) cos(θ/2) │       │ sin(θ/2)  cos(θ/2)│         │ 0    e^(iθ/2)│
└                    ┘        └                  ┘          └              ┘

Special cases:
RX(π) = X    RY(π) = Y    RZ(π) = Z
                          RZ(π/2) = S (up to global phase)
```

#### 4. Implementation
```python
qc.rx(theta, qubit)  # Rotation around X
qc.ry(theta, qubit)  # Rotation around Y
qc.rz(theta, qubit)  # Rotation around Z

# Variational ansatz pattern
qc.ry(theta, 0)
qc.rz(phi, 0)
```

#### 5. ⚠️ Trap Alert
**Trap: Half-angle in matrix**
- ❌ **Wrong**: Matrix uses θ directly
- ✅ **Correct**: Matrix uses θ/2 (half-angle formula)

#### 6. 🧠 Mnemonic
> **"R-π equals Pauli"** - RX(π)=X, RY(π)=Y, RZ(π)=Z

#### 7. ⚡ Quick Check
**Q: What is RZ(π/2)?**
<details><summary>Answer</summary>S gate (up to global phase)</details>

---

### 🔹 Pauli Class (`qiskit.quantum_info.Pauli`)

#### 1. Definition
Python class for algebraic manipulation of Pauli operators. **Different from Pauli gates!**

The Pauli group consists of all tensor products of Pauli matrices (I, X, Y, Z) with phases (±1, ±i).

#### 2. Analogy + Intuition
**Real-World Analogy**: Calculator for Pauli math vs. physically applying gates to a circuit.

**Intuition**: Use for checking commutativity, composing operators, analyzing Hamiltonians.

**Why Pauli Operators Matter**:
- **Quantum Error Correction**: Errors are classified as X (bit flip), Z (phase flip), or Y (both)
- **Hamiltonians**: Many quantum systems are expressed as sums of Pauli operators
- **Measurements**: Pauli operators define measurement bases
- **VQE/QAOA**: Cost functions are decomposed into Pauli strings

**Key Properties**:
- Hermitian: P† = P
- Unitary: P†P = I
- Involutory: P² = I (self-inverse)
- Eigenvalues: Always ±1

#### 3. Math + Visual
**Pauli Algebra:**
```
XY = iZ,  YZ = iX,  ZX = iY   (cyclic, positive i)
YX = -iZ, ZY = -iX, XZ = -iY  (anti-cyclic, negative i)
X² = Y² = Z² = I              (self-inverse)
```

**Anticommutation**: Different Paulis anticommute: XZ = -ZX

**X and Z Array Representation**:
| Label | X bit | Z bit |
|-------|-------|-------|
| I | 0 | 0 |
| X | 1 | 0 |
| Y | 1 | 1 |
| Z | 0 | 1 |

#### 4. Implementation
```python
from qiskit.quantum_info import Pauli

# Creating Paulis
p = Pauli('X')           # Single qubit
p = Pauli('XYZ')         # 3-qubit: RIGHT-TO-LEFT! (X on q2, Y on q1, Z on q0)
p = Pauli('iX')          # With phase prefix

# Phase notation (EXAM TIP!):
# ''=+1, 'i'=+i, '-'=-1, '-i'=-i

# Key methods
X, Z = Pauli('X'), Pauli('Z')
X.commutes(Z)            # → False
X.anticommutes(Z)        # → True
(X @ Z).to_label()       # → 'iY' (composition)
X.tensor(Z)              # → Pauli('XZ') (tensor product)
X.expand(2)              # → Pauli('XI') (adds identities)
p.to_matrix()            # → numpy array
p.to_instruction()       # → circuit instruction
p.evolve(gate)           # → Pauli after gate conjugation (U·P·U†)
```

**Attributes**: `.num_qubits`, `.x`, `.z`, `.phase`

#### 5. ⚠️ Trap Alert
**Trap 1: String ordering**
- ❌ **Wrong**: 'XYZ' means X on q0
- ✅ **Correct**: 'XYZ' means X⊗Y⊗Z (X on q2, Y on q1, Z on q0) - RIGHT-TO-LEFT!

**Trap 2: Class vs Gates**
- `Pauli('X')` = algebraic object for calculations
- `qc.x(0)` = applies gate to circuit

#### 6. 🧠 Mnemonic
> **"Pauli Class Calculates, Gates Apply"**

#### 7. ⚡ Quick Check
**Q: What is X @ Z (compose)?**
<details><summary>Answer</summary>iY (XZ = iY)</details>

---

### 📊 Single-Qubit Gates: Consolidated Review

#### Comparison Table

| Gate | Matrix | |0⟩ → | |1⟩ → | Qiskit |
|------|--------|------|------|--------|
| **X** | [[0,1],[1,0]] | \|1⟩ | \|0⟩ | `qc.x(q)` |
| **Y** | [[0,-i],[i,0]] | i\|1⟩ | -i\|0⟩ | `qc.y(q)` |
| **Z** | [[1,0],[0,-1]] | \|0⟩ | -\|1⟩ | `qc.z(q)` |
| **H** | [[1,1],[1,-1]]/√2 | \|+⟩ | \|-⟩ | `qc.h(q)` |
| **S** | [[1,0],[0,i]] | \|0⟩ | i\|1⟩ | `qc.s(q)` |
| **T** | [[1,0],[0,e^(iπ/4)]] | \|0⟩ | e^(iπ/4)\|1⟩ | `qc.t(q)` |

#### Gate Equivalences
```
X = HZH        H = (X+Z)/√2
S² = Z         T⁴ = Z         T² = S
RX(π) = X      RY(π) = Y      RZ(π) = Z
P(π/2) = S     P(π/4) = T     P(π) = Z
```

#### Quick Reference Card
```
┌─────────────────────────────────────────────────────────────────┐
│              SINGLE-QUBIT GATES QUICK REFERENCE                  │
├─────────────────────────────────────────────────────────────────┤
│  PAULI: qc.x(q), qc.y(q), qc.z(q)                               │
│  HADAMARD: qc.h(q)                                               │
│  PHASE: qc.s(q), qc.sdg(q), qc.t(q), qc.tdg(q), qc.p(λ,q)      │
│  ROTATION: qc.rx(θ,q), qc.ry(θ,q), qc.rz(θ,q)                  │
├─────────────────────────────────────────────────────────────────┤
│  MNEMONICS:                                                      │
│  • "X-Men Flip bits, Z-Men flip Phase"                          │
│  • "Hadamard Makes Plus" (H|0⟩ = |+⟩)                           │
│  • "S-Squared, T-Fourth" (S²=Z, T⁴=Z)                           │
├─────────────────────────────────────────────────────────────────┤
│  TRAPS:                                                          │
│  • Z|0⟩ = |0⟩ (unchanged!)                                      │
│  • HXH = Z, HZH = X                                              │
│  • X and Z anticommute (XZ ≠ ZX)                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔗 MULTI-QUBIT GATES

---

### 🔹 CNOT Gate (CX) - MOST CRITICAL!

#### 1. Definition
Controlled-NOT: flips target qubit IF control qubit is |1⟩. Creates entanglement!

#### 2. Analogy + Intuition
**Real-World Analogy**: Conditional switch - "If boss (control) says yes, flip the switch (target)"

**Intuition**: CNOT is the entanglement creator - combines with H to make Bell states.

#### 3. Math + Visual
```
Circuit:          Truth Table:                Matrix (4×4):
q0: ──●──         |00⟩ → |00⟩                ┌         ┐
      │           |01⟩ → |01⟩                │1 0 0 0  │
q1: ──⊕──         |10⟩ → |11⟩ ✓ flip!       │0 1 0 0  │
                  |11⟩ → |10⟩ ✓ flip!       │0 0 0 1  │
Control  Target                              │0 0 1 0  │
                                             └         ┘
```

#### 4. Implementation
```python
qc.cx(control, target)   # CNOT
qc.cnot(control, target) # Alternative name
```

| Parameter | Type | Description |
|-----------|------|-------------|
| control | int | Control qubit (first!) |
| target | int | Target qubit (flipped if control=1) |

#### 5. ⚠️ Trap Alert
**Trap: CNOT direction matters!**
- ❌ **Wrong**: CX(0,1) = CX(1,0)
- ✅ **Correct**: CX(0,1) ≠ CX(1,0) - control and target are different!
- 🔍 **Example**: |10⟩ → CX(0,1) → |11⟩, but CX(1,0) → |10⟩ (no change)

#### 6. 🧠 Mnemonic
> **"Control BEFORE Target"** - first parameter is control

#### 7. ⚡ Quick Check
**Q: What is CX|10⟩ (control=q0)?**
<details><summary>Answer</summary>|11⟩ (target flipped because control is 1)</details>

---

### 🔹 Bell States (All Four)

#### 1. Definition
Four maximally entangled 2-qubit states. Measuring one qubit instantly determines the other.

#### 2. Analogy + Intuition
**Real-World Analogy**: Telepathically linked coins - flip one and you know what the other is!

**Intuition**: Bell states are the "most quantum" 2-qubit states - maximum entanglement.

#### 3. Math + Visual
```
|Φ⁺⟩ = (|00⟩+|11⟩)/√2    |Φ⁻⟩ = (|00⟩-|11⟩)/√2
|Ψ⁺⟩ = (|01⟩+|10⟩)/√2    |Ψ⁻⟩ = (|01⟩-|10⟩)/√2
```

**Phi (Φ) states**: Same bits (00, 11) - correlated
**Psi (Ψ) states**: Different bits (01, 10) - anti-correlated

#### 4. Implementation
```python
# |Φ⁺⟩ (most common)
qc.h(0)
qc.cx(0, 1)

# |Φ⁻⟩
qc.x(0)
qc.h(0)
qc.cx(0, 1)

# |Ψ⁺⟩
qc.h(0)
qc.cx(0, 1)
qc.x(1)

# |Ψ⁻⟩
qc.x(0)
qc.h(0)
qc.cx(0, 1)
qc.x(1)
```

#### 5. ⚠️ Trap Alert
**Trap: Phi vs Psi**
- Φ states: same bits (00/11) - like "twins"
- Ψ states: different bits (01/10) - like "opposites"

#### 6. 🧠 Mnemonic
> **"Phi = same, Psi = different"** (Φ: 00/11, Ψ: 01/10)

#### 7. ⚡ Quick Check
**Q: How many gates for Bell state |Φ⁺⟩?**
<details><summary>Answer</summary>2 (one H + one CX)</details>

---

### 🔹 CZ Gate (Controlled-Z)

#### 1. Definition
Adds -1 phase to |11⟩ state. **Symmetric**: CZ(0,1) = CZ(1,0)!

#### 2. Analogy + Intuition
**Real-World Analogy**: Mutual agreement penalty - both must be |1⟩ for the phase flip.

#### 3. Math + Visual
```
Circuit:          Matrix:                Effect:
q0: ──●──         ┌         ┐           Only |11⟩ → -|11⟩
      │           │1 0 0  0 │           All others unchanged
q1: ──●──         │0 1 0  0 │           
                  │0 0 1  0 │           CZ = H·CX·H (on target)
                  │0 0 0 -1 │           
                  └         ┘           
```

#### 4. Implementation
```python
qc.cz(qubit1, qubit2)  # Order doesn't matter!
```

#### 5. ⚠️ Trap Alert
**Trap: CZ is symmetric**
- ❌ **Wrong**: CZ(0,1) ≠ CZ(1,0) like CNOT
- ✅ **Correct**: CZ(0,1) = CZ(1,0) - symmetric gate!

#### 6. 🧠 Mnemonic
> **"CZ is Symmetric"**

#### 7. ⚡ Quick Check
**Q: Is CZ(0,1) = CZ(1,0)?**
<details><summary>Answer</summary>Yes! CZ is symmetric</details>

---

### 🔹 SWAP Gate

#### 1. Definition
Exchanges the states of two qubits: |01⟩ ↔ |10⟩.

#### 2. Analogy + Intuition
**Real-World Analogy**: Swapping contents of two glasses.

#### 3. Math + Visual
```
Circuit:          Effect:               Decomposition:
q0: ──×──         |01⟩ ↔ |10⟩          SWAP = CX(a,b)·CX(b,a)·CX(a,b)
      │           |00⟩, |11⟩ unchanged       (3 CNOTs)
q1: ──×──         
```

#### 4. Implementation
```python
qc.swap(qubit1, qubit2)
```

#### 5. ⚠️ Trap Alert
**Trap: SWAP decomposition**
- SWAP requires **3 CNOTs** to decompose (expensive on hardware!)

#### 6. 🧠 Mnemonic
> **"Three CNOTs to SWAP"**

#### 7. ⚡ Quick Check
**Q: How many CNOTs to implement SWAP?**
<details><summary>Answer</summary>3</details>

---

### 🔹 Toffoli Gate (CCX)

#### 1. Definition
Double-controlled NOT: flips target if BOTH controls are |1⟩.

#### 2. Analogy + Intuition
**Real-World Analogy**: Two-key safe - both keys (controls) needed to unlock (flip target).

**Intuition**: Implements classical AND gate in quantum circuits.

#### 3. Math + Visual
```
Circuit:          Effect:
q0: ──●──         Flips q2 IF both q0 AND q1 are |1⟩
      │           
q1: ──●──         |110⟩ → |111⟩
      │           |111⟩ → |110⟩
q2: ──⊕──         All others unchanged
```

#### 4. Implementation
```python
qc.ccx(control1, control2, target)
qc.toffoli(control1, control2, target)  # Alternative
```

#### 5. ⚠️ Trap Alert
**Trap: Toffoli decomposition**
- Toffoli decomposes to **6 CNOTs** on hardware (very expensive!)

#### 6. 🧠 Mnemonic
> **"Toffoli = quantum AND"**

#### 7. ⚡ Quick Check
**Q: What classical gate does Toffoli implement?**
<details><summary>Answer</summary>AND gate</details>

---

### � Fredkin Gate (CSWAP)

#### 1. Definition
Controlled-SWAP: swaps two target qubits if control qubit is |1⟩.

#### 2. Analogy + Intuition
**Real-World Analogy**: A railway switch controlled by a signal - if signal is ON, trains swap tracks.

**Intuition**: Conditionally swaps two qubits based on a third control qubit.

#### 3. Math + Visual
```
Circuit:          Effect:
q0: ──●──         IF control=|1⟩: swap q1 ↔ q2
      │           
q1: ──×──         |1,1,0⟩ → |1,0,1⟩ (swapped)
      │           |0,1,0⟩ → |0,1,0⟩ (unchanged)
q2: ──×──         
```

#### 4. Implementation
```python
qc.cswap(control, target1, target2)
qc.fredkin(control, target1, target2)  # Alternative
```

| Parameter | Type | Description |
|-----------|------|-------------|
| control | int | Control qubit |
| target1 | int | First swap target |
| target2 | int | Second swap target |

#### 5. ⚠️ Trap Alert
**Trap: Fredkin is expensive**
- Fredkin decomposes to **8+ gates** on hardware

#### 6. 🧠 Mnemonic
> **"Fredkin = Controlled SWAP"** (CSWAP)

#### 7. ⚡ Quick Check
**Q: What does Fredkin do if control is |0⟩?**
<details><summary>Answer</summary>Nothing - targets remain unchanged</details>

---

### �📊 Multi-Qubit Gates: Consolidated Review

#### Comparison Table

| Gate | Effect | Symmetric? | Qiskit |
|------|--------|-----------|--------|
| **CNOT/CX** | Flip target if control=1 | No | `qc.cx(c,t)` |
| **CZ** | Phase flip if both=1 | **Yes** | `qc.cz(q1,q2)` |
| **SWAP** | Exchange qubits | Yes | `qc.swap(q1,q2)` |
| **Toffoli** | Flip if both controls=1 | No | `qc.ccx(c1,c2,t)` |
| **Fredkin** | SWAP if control=1 | No | `qc.cswap(c,t1,t2)` |

#### Gate Costs (CNOT decomposition)
```
Bell state:  2 gates (1 H + 1 CX)
GHZ (n):     n gates (1 H + n-1 CX)
SWAP:        3 CNOTs
Toffoli:     6 CNOTs
Fredkin:     8+ gates
```

#### Quick Reference Card
```
┌─────────────────────────────────────────────────────────────────┐
│              MULTI-QUBIT GATES QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────────┤
│  CNOT: qc.cx(control, target) - creates entanglement!           │
│  CZ: qc.cz(q1, q2) - symmetric!                                 │
│  SWAP: qc.swap(q1, q2) - costs 3 CNOTs                          │
│  Toffoli: qc.ccx(c1, c2, target) - costs 6 CNOTs                │
│  Fredkin: qc.cswap(c, t1, t2) - controlled SWAP (8+ gates)      │
├─────────────────────────────────────────────────────────────────┤
│  BELL STATES:                                                    │
│  • |Φ⁺⟩: H(0), CX(0,1)     • |Φ⁻⟩: X(0), H(0), CX(0,1)        │
│  • |Ψ⁺⟩: H(0), CX(0,1), X(1)  • |Ψ⁻⟩: X(0), H(0), CX(0,1), X(1)│
├─────────────────────────────────────────────────────────────────┤
│  MNEMONICS:                                                      │
│  • "Control BEFORE Target"                                       │
│  • "Phi=same, Psi=different"                                    │
│  • "CZ is Symmetric"                                             │
│  • "Three CNOTs to SWAP"                                         │
│  • "Fredkin = Controlled SWAP"                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎨 STATE PREPARATION

---

### 🔹 initialize()

#### 1. Definition
Prepares an arbitrary quantum state from a given amplitude vector.

#### 2. Analogy + Intuition
**Real-World Analogy**: Setting the starting positions of dancers on stage before the show.

**Intuition**: Useful for algorithm initialization, but expensive (adds many gates).

#### 3. Implementation
```python
qc.initialize(state_vector, qubits)

# Examples
qc.initialize([1, 0], 0)           # |0⟩
qc.initialize([0, 1], 0)           # |1⟩
qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0)  # |+⟩
qc.initialize([0.5, 0.5, 0.5, 0.5], [0, 1])     # Equal superposition
```

#### 4. ⚠️ Trap Alert
**Trap: initialize() is expensive**
- ❌ **Wrong**: initialize() is a simple operation
- ✅ **Correct**: initialize() adds MANY gates for decomposition/synthesis

#### 5. 🧠 Mnemonic
> **"Initialize = Synthesize"** (adds many gates)

#### 6. ⚡ Quick Check
**Q: Does initialize() add gates?**
<details><summary>Answer</summary>Yes, many gates for synthesis!</details>

---

### 🔹 reset()

#### 1. Definition
Returns qubit to |0⟩ state via measurement + conditional flip.

#### 2. Analogy + Intuition
**Real-World Analogy**: Reset button - forces system back to starting state.

**Intuition**: Active operation (unlike initialize). Useful for qubit recycling.

#### 3. Implementation
```python
qc.reset(qubit)

# Example: Reset mid-circuit
qc.x(0)       # |1⟩
qc.reset(0)   # Back to |0⟩
```

#### 4. ⚠️ Trap Alert
**Trap: reset() vs initialize()**
- `reset()` = measurement + conditional flip (active reset)
- `initialize()` = gate synthesis (no measurement)

#### 5. 🧠 Mnemonic
> **"Reset Returns to Zero"**

#### 6. ⚡ Quick Check
**Q: What state does reset() produce?**
<details><summary>Answer</summary>|0⟩</details>

---

### 🔹 barrier()

#### 1. Definition
Visual separator that prevents transpiler optimization across it. **NO quantum effect!**

#### 2. Analogy + Intuition
**Real-World Analogy**: "Do Not Cross" tape - visual marker, not a physical barrier.

**Intuition**: Use for debugging, visualization, and controlling optimization.

#### 3. Implementation
```python
qc.barrier()           # All qubits
qc.barrier([0, 1])     # Specific qubits

# Example
qc.h(0)
qc.barrier()   # ┈┈┈┈┈ visual line
qc.cx(0, 1)
```

#### 4. ⚠️ Trap Alert
**Trap: barrier() has no quantum effect!**
- ❌ **Wrong**: barrier() does something to the quantum state
- ✅ **Correct**: barrier() is ONLY visual + blocks optimization

#### 5. 🧠 Mnemonic
> **"Barriers Block optimization, not qubits"**

#### 6. ⚡ Quick Check
**Q: Does barrier() change quantum state?**
<details><summary>Answer</summary>No! Only visual/optimization effect</details>

---

### 📊 State Preparation: Consolidated Review

| Method | Purpose | Implementation | Qiskit |
|--------|---------|----------------|--------|
| **initialize()** | Set arbitrary state | Gate synthesis | `qc.initialize(state, qubits)` |
| **reset()** | Return to \|0⟩ | Measurement + flip | `qc.reset(qubit)` |
| **barrier()** | Visual separator | No quantum effect | `qc.barrier()` |

---

## 📚 END-OF-README: COMPREHENSIVE REVIEW

---

## ⚠️ MASTER TRAP LIST

| Topic | Trap | ❌ Wrong | ✅ Correct |
|-------|------|----------|-----------|
| **Z gate** | Z on \|0⟩ | Z flips \|0⟩ | Z\|0⟩ = \|0⟩ (unchanged) |
| **Hadamard** | HXH | HXH = X | HXH = Z |
| **S gate** | S² | S² = I | S² = Z |
| **T gate** | T powers | T² = Z | T⁴ = Z (T² = S) |
| **CNOT** | Direction | CX(0,1) = CX(1,0) | Order matters! |
| **CZ** | Symmetry | CZ asymmetric | CZ(0,1) = CZ(1,0) |
| **Commutativity** | X and Z | XZ = ZX | XZ = -ZX (anticommute) |
| **Pauli string** | Order | 'XYZ' = X on q0 | RIGHT-TO-LEFT! |
| **barrier()** | Effect | Changes state | No quantum effect |
| **initialize()** | Cost | Simple | Expensive (many gates) |

---

## 📝 PRACTICE EXAM

### Part A: Quick Fire (10 questions)

1. **What is X|0⟩?**
<details><summary>Answer</summary>|1⟩</details>

2. **What is Z|0⟩?**
<details><summary>Answer</summary>|0⟩ (unchanged!)</details>

3. **What is H|0⟩?**
<details><summary>Answer</summary>|+⟩ = (|0⟩+|1⟩)/√2</details>

4. **What is S²?**
<details><summary>Answer</summary>Z</details>

5. **What is T⁴?**
<details><summary>Answer</summary>Z</details>

6. **Do X and Z commute?**
<details><summary>Answer</summary>No, they anticommute (XZ = -ZX)</details>

7. **How many CNOTs for a Bell state?**
<details><summary>Answer</summary>1 (plus 1 Hadamard)</details>

8. **Is CZ symmetric?**
<details><summary>Answer</summary>Yes, CZ(0,1) = CZ(1,0)</details>

9. **How many CNOTs to decompose SWAP?**
<details><summary>Answer</summary>3</details>

10. **Does barrier() affect quantum state?**
<details><summary>Answer</summary>No, only visualization/optimization</details>

### Part B: Code Analysis

**Q1: What state does this produce?**
```python
qc.h(0)
qc.cx(0, 1)
```
<details><summary>Answer</summary>Bell state |Φ⁺⟩ = (|00⟩+|11⟩)/√2</details>

**Q2: What is the result of HXH|0⟩?**
<details><summary>Answer</summary>|0⟩ (because HXH = Z, and Z|0⟩ = |0⟩)</details>

**Q3: What does this Pauli code return?**
```python
from qiskit.quantum_info import Pauli
(Pauli('X') @ Pauli('Z')).to_label()
```
<details><summary>Answer</summary>'iY' (XZ = iY)</details>

### Part C: Real-World Scenarios (3 Questions)

**Q4**: You need to prepare the Bell state |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2 for a quantum teleportation protocol. Write the gate sequence and explain why each gate is needed.

<details>
<summary>Answer</summary>

**A**: The gate sequence for |Ψ⁻⟩:
```python
qc = QuantumCircuit(2)
qc.x(0)       # Step 1: Start with |10⟩
qc.h(0)       # Step 2: Create superposition (|00⟩ - |10⟩)/√2
qc.cx(0, 1)   # Step 3: Entangle to get (|01⟩ - |10⟩)/√2
qc.x(1)       # Step 4: NOT needed for |Ψ⁻⟩ (this was in the original pattern)
```

Wait - let me recalculate. The correct sequence:
```python
qc = QuantumCircuit(2)
qc.h(0)       # |00⟩ → (|0⟩+|1⟩)|0⟩/√2 = (|00⟩+|10⟩)/√2
qc.cx(0, 1)   # → (|00⟩+|11⟩)/√2 = |Φ⁺⟩
qc.x(1)       # → (|01⟩+|10⟩)/√2 = |Ψ⁺⟩
qc.z(0)       # → (|01⟩-|10⟩)/√2 = |Ψ⁻⟩
```

**Explanation:**
1. H creates superposition on control qubit
2. CNOT creates entanglement (same bits: 00/11)
3. X(1) switches to different bits (01/10) → converts Φ to Ψ
4. Z(0) adds the minus sign between terms

**Alternative (fewer gates):**
```python
qc.x(0)       # |10⟩
qc.h(0)       # (|0⟩-|1⟩)|0⟩/√2 = (|00⟩-|10⟩)/√2
qc.cx(0, 1)   # (|00⟩-|11⟩)/√2 = |Φ⁻⟩
qc.x(1)       # (|01⟩-|10⟩)/√2 = |Ψ⁻⟩
```
</details>

**Q5**: A colleague claims that applying HZH to a qubit is equivalent to applying X. They test it on |0⟩ and get |0⟩ in both cases, concluding they're wrong. Explain what's happening.

<details>
<summary>Answer</summary>

**A**: The colleague made a critical error - HZH IS equal to X!

**The confusion:**
```
HZH|0⟩ = ?

Step by step:
1. H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2
2. Z|+⟩ = (|0⟩-|1⟩)/√2 = |-⟩
3. H|-⟩ = |1⟩

So HZH|0⟩ = |1⟩ = X|0⟩ ✓
```

**Where did they go wrong?**
They likely tested X|0⟩ = |1⟩, but then measured and got "0" sometimes due to statistical error, OR they accidentally ran the wrong code.

**Key identity to memorize:**
- HXH = Z (Hadamard transforms X to Z)
- HZH = X (Hadamard transforms Z to X)
- HYH = -Y (Y gets a sign flip)

This is called "Hadamard conjugation" and is fundamental for understanding basis changes!
</details>

**Q6**: You're implementing a VQE ansatz and need parameterized rotations. Someone suggests using RX(θ)·RY(φ)·RZ(ψ) on each qubit. Another person says RY(θ)·RZ(φ) is sufficient. Who is correct and why?

<details>
<summary>Answer</summary>

**A**: **RY(θ)·RZ(φ) is sufficient** for reaching any single-qubit state (up to global phase).

**Explanation:**

Any single-qubit unitary can be decomposed as:
$$U = e^{i\alpha} R_Z(\beta) R_Y(\gamma) R_Z(\delta)$$

This is the ZYZ Euler decomposition. Equivalently, RY·RZ can reach any point on the Bloch sphere:

```
RZ(φ): Rotation around Z-axis (changes longitude)
RY(θ): Rotation around Y-axis (changes latitude)

Combined: Can reach any point on sphere!
```

**Why not RX·RY·RZ?**
- It works, but it's redundant (3 parameters for 2 degrees of freedom)
- More gates = more error on real hardware
- Wastes optimizer iterations on unnecessary parameters

**Hardware-efficient alternative:**
```python
# Efficient single-qubit rotation
qc.ry(theta, qubit)  # Latitude
qc.rz(phi, qubit)    # Longitude
```

**The lesson:** In VQE/QAOA, fewer parameters = faster convergence and less noise. Use minimal sufficient parameterization!
</details>

---

## ✅ Key Takeaways

### 📚 Concept Checklist
```
□ Qubit exists in superposition until measured (spinning coin analogy)
□ Global phase (e^iθ|ψ⟩) is unobservable - affects nothing
□ Relative phase (|0⟩+e^iθ|1⟩) matters - causes interference
□ Bloch sphere: |0⟩ at North pole, |1⟩ at South pole
□ Equator states: |+⟩, |-⟩ (X-basis), |+i⟩, |-i⟩ (Y-basis)
□ Pauli gates: X=bit flip, Z=phase flip, Y=iXZ (both)
□ Hadamard creates superposition: H|0⟩=|+⟩, H|1⟩=|-⟩
□ H is self-inverse: H²=I
□ Hadamard conjugation: HXH=Z, HZH=X
□ S²=Z, T⁴=Z, T²=S (phase gate hierarchy)
□ Rotation gates use HALF-ANGLE in matrix: cos(θ/2), sin(θ/2)
□ RX(π)=X, RY(π)=Y, RZ(π)=Z (up to global phase)
□ CNOT creates entanglement - THE key 2-qubit gate
□ CNOT direction matters: CX(control, target) - order is critical!
□ CZ is symmetric: CZ(0,1)=CZ(1,0)
□ Bell states: Φ=same bits (00/11), Ψ=different bits (01/10)
□ Bell state |Φ⁺⟩ = H + CNOT (just 2 gates!)
□ SWAP = 3 CNOTs (expensive!)
□ Toffoli = 6 CNOTs (very expensive!)
□ Fredkin = controlled SWAP (swaps if control=1)
□ Pauli operators anticommute: XZ = -ZX
□ barrier() has NO quantum effect - visual only
```

### 💻 Code Pattern Checklist
```
□ qc.x(qubit) applies Pauli-X (bit flip)
□ qc.y(qubit) applies Pauli-Y (bit + phase flip with i factors)
□ qc.z(qubit) applies Pauli-Z (phase flip)
□ qc.h(qubit) applies Hadamard (creates superposition)
□ qc.s(qubit) applies S gate (π/2 phase)
□ qc.sdg(qubit) applies S† (S-dagger, inverse of S)
□ qc.t(qubit) applies T gate (π/4 phase)
□ qc.tdg(qubit) applies T† (T-dagger, inverse of T)
□ qc.p(lambda, qubit) applies P(λ) phase gate
□ qc.rx(theta, qubit) rotates around X-axis by theta
□ qc.ry(theta, qubit) rotates around Y-axis by theta
□ qc.rz(theta, qubit) rotates around Z-axis by theta
□ qc.cx(control, target) applies CNOT (control FIRST!)
□ qc.cz(q1, q2) applies CZ (order doesn't matter)
□ qc.swap(q1, q2) swaps two qubits
□ qc.ccx(c1, c2, target) applies Toffoli (AND gate)
□ qc.cswap(control, t1, t2) applies Fredkin (controlled SWAP)
□ qc.initialize(state_vector, qubits) prepares arbitrary state
□ qc.reset(qubit) resets qubit to |0⟩
□ qc.barrier() adds visual separator (no quantum effect)
□ from qiskit.quantum_info import Pauli
□ p = Pauli('X') creates Pauli object
□ p = Pauli('XYZ') creates multi-qubit Pauli (RIGHT-TO-LEFT order!)
□ p1.commutes(p2) checks if operators commute
□ p1.anticommutes(p2) checks if operators anticommute
□ (p1 @ p2).to_label() computes composition and returns label
□ p.to_matrix() converts Pauli to numpy matrix
□ p.to_instruction() converts Pauli to circuit instruction
```

### ⚠️ Exam Trap Checklist
```
□ TRAP: Z|0⟩ = |0⟩ (unchanged!) NOT |1⟩
  → Z only adds phase to |1⟩ component
□ TRAP: X|+⟩ = |+⟩ (unchanged!) because amplitudes are equal
□ TRAP: HXH = Z (NOT X!) and HZH = X
  → Hadamard swaps X and Z bases
□ TRAP: S² = Z (NOT I!) and T⁴ = Z (NOT T² = Z!)
  → T² = S, T⁴ = Z, S² = Z
□ TRAP: CX(0,1) ≠ CX(1,0) - direction matters!
  → First parameter is control, second is target
□ TRAP: CZ IS symmetric: CZ(0,1) = CZ(1,0)
  → Unlike CNOT, CZ doesn't care about order
□ TRAP: X and Z anticommute: XZ = -ZX (NOT XZ = ZX!)
  → Different Paulis anticommute, same Paulis commute
□ TRAP: Pauli('XYZ') means X⊗Y⊗Z (X on q2, Y on q1, Z on q0)
  → RIGHT-TO-LEFT reading! Not left-to-right!
□ TRAP: barrier() has NO quantum effect!
  → Only visual separator and optimization blocker
□ TRAP: initialize() is expensive - adds many gates
  → Not a simple single gate operation
□ TRAP: Y adds complex phases: Y|0⟩ = i|1⟩ (not just |1⟩)
  → Y = iXZ has the i factor
□ TRAP: Rotation matrices use θ/2 (half-angle!)
  → RX(π) uses cos(π/2) and sin(π/2) in matrix
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 1 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🔄 "X-Men Flip bits, Z-Men flip Phase"                          │
│    X: |0⟩↔|1⟩ (bit flip)                                        │
│    Z: adds -1 to |1⟩ (phase flip)                               │
│                                                                  │
│ ➕ "Hadamard Makes Plus"                                         │
│    H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2                                    │
│    H|1⟩ = |-⟩ = (|0⟩-|1⟩)/√2                                    │
│                                                                  │
│ 2️⃣ "S-Squared equals Z"                                          │
│    S² = Z (two S gates = one Z)                                 │
│                                                                  │
│ 4️⃣ "T-Fourth equals Z"                                           │
│    T⁴ = Z (T² = S, so T⁴ = S² = Z)                              │
│                                                                  │
│ ⬅️ "Control BEFORE Target"                                       │
│    qc.cx(control, target) - first arg is control!               │
│                                                                  │
│ 🔀 "CZ is Symmetric"                                             │
│    CZ(0,1) = CZ(1,0) - order doesn't matter                     │
│                                                                  │
│ 👯 "Phi = same, Psi = different"                                 │
│    Φ states: |00⟩, |11⟩ (same bits)                             │
│    Ψ states: |01⟩, |10⟩ (different bits)                        │
│                                                                  │
│ 3️⃣ "Three CNOTs to SWAP"                                         │
│    SWAP = CX(a,b)·CX(b,a)·CX(a,b)                               │
│                                                                  │
│ 🧮 "R-π equals Pauli"                                            │
│    RX(π)=X, RY(π)=Y, RZ(π)=Z (up to global phase)               │
│                                                                  │
│ 📊 "Pauli Class Calculates, Gates Apply"                         │
│    Pauli('X') for algebra, qc.x() for circuits                  │
│                                                                  │
│ 🚧 "Barriers Block optimization, not qubits"                     │
│    barrier() = visual only, no quantum effect                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 1: QUANTUM OPERATIONS - ONE-PAGE SUMMARY                  ║
║                (16% of Exam - ~11 Questions)                          ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  📐 SINGLE-QUBIT GATES                                                 ║
║  ├─ Paulis: qc.x() = bit flip, qc.z() = phase flip, qc.y() = iXZ     ║
║  ├─ Hadamard: qc.h() creates superposition (H|0⟩ = |+⟩)              ║
║  ├─ Phase: qc.s() = π/2, qc.t() = π/4, qc.p(λ) = custom             ║
║  ├─ Rotation: qc.rx(θ), qc.ry(θ), qc.rz(θ)                          ║
║  └─ Inverses: qc.sdg() = S†, qc.tdg() = T†                           ║
║                                                                        ║
║  🔗 MULTI-QUBIT GATES                                                  ║
║  ├─ CNOT: qc.cx(control, target) - creates entanglement!             ║
║  ├─ CZ: qc.cz(q1, q2) - symmetric (order doesn't matter)             ║
║  ├─ SWAP: qc.swap(q1, q2) - costs 3 CNOTs                            ║
║  ├─ Toffoli: qc.ccx(c1, c2, target) - costs 6 CNOTs                  ║
║  └─ Fredkin: qc.cswap(c, t1, t2) - controlled SWAP                   ║
║                                                                        ║
║  💕 BELL STATES (memorize these!)                                      ║
║  ├─ |Φ⁺⟩: qc.h(0); qc.cx(0,1) → (|00⟩+|11⟩)/√2                       ║
║  ├─ |Φ⁻⟩: qc.x(0); qc.h(0); qc.cx(0,1) → (|00⟩-|11⟩)/√2              ║
║  ├─ |Ψ⁺⟩: qc.h(0); qc.cx(0,1); qc.x(1) → (|01⟩+|10⟩)/√2              ║
║  └─ |Ψ⁻⟩: qc.x(0); qc.h(0); qc.cx(0,1); qc.x(1) → (|01⟩-|10⟩)/√2     ║
║                                                                        ║
║  🎯 STATE PREPARATION                                                  ║
║  ├─ qc.initialize(state_vector, qubits) - expensive (many gates)     ║
║  ├─ qc.reset(qubit) - returns to |0⟩                                 ║
║  └─ qc.barrier() - visual only, NO quantum effect                    ║
║                                                                        ║
║  🧮 PAULI CLASS (qiskit.quantum_info)                                  ║
║  ├─ Pauli('X'), Pauli('XYZ') - RIGHT-TO-LEFT order!                  ║
║  ├─ p1.commutes(p2), p1.anticommutes(p2) - check relations           ║
║  └─ (p1 @ p2).to_label() - composition → 'iY' for XZ                 ║
║                                                                        ║
║  📊 KEY IDENTITIES                                                     ║
║  ├─ H² = I (self-inverse)                                             ║
║  ├─ HXH = Z, HZH = X (Hadamard conjugation)                          ║
║  ├─ S² = Z, T⁴ = Z, T² = S                                           ║
║  ├─ XZ = -ZX (anticommute), XX = I (self-inverse)                    ║
║  └─ Y = iXZ                                                           ║
║                                                                        ║
║  ⚠️ TOP 5 EXAM TRAPS                                                   ║
║  1. Z|0⟩ = |0⟩ (unchanged!) - Z only affects |1⟩                     ║
║  2. CX(control, target) - control comes FIRST!                       ║
║  3. Pauli('XYZ') = X⊗Y⊗Z - RIGHT-TO-LEFT (X on q2!)                  ║
║  4. barrier() has NO quantum effect                                   ║
║  5. S² = Z (not I), T⁴ = Z (not T² = Z)                              ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 📁 Files in This Section

| File | Description |
|------|-------------|
| `single_qubit_gates.ipynb` | Code lab: X, Y, Z, H, S, T, P, RX, RY, RZ, Pauli class |
| `multi_qubit_gates.ipynb` | Code lab: CNOT, CZ, SWAP, Toffoli, Bell states |
| `state_preparation.ipynb` | Code lab: initialize(), reset(), barrier() |

---

## 🎯 Next Steps

1. ✅ Run each notebook to see gates in action
2. ✅ Memorize gate matrices (X, Z, H, S, T)
3. ✅ Practice creating Bell states and GHZ states
4. ✅ Understand Bloch sphere rotations
5. → Move to **Section 2 (Visualization)** to see these gates visually

**Master this section = Foundation for entire certification!** 🚀

---

*Last Updated: December 2025*
