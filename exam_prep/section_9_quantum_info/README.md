# Section 9: Quantum Information

> **Exam Weight**: 3% (~2 Questions) | **Difficulty**: High | **Must Master**: Operator.equiv(), Fidelity range [0,1]

```
┌─────────────────────────────────────────────────────────────────┐
│  🎯 EXAM TRAP #1: T gate is NOT Clifford!                       │
│  ✅ Clifford gates: {H, S, CNOT, X, Y, Z}                       │
│  ❌ T gate makes circuits universal but NOT efficiently         │
│     simulatable                                                  │
│                                                                 │
│  📌 Mnemonic: "HSCP" - H, S, CNOT, Paulis (no T!)              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Overview

Quantum information theory provides the mathematical tools to analyze, verify, and benchmark quantum circuits. This section covers the `qiskit.quantum_info` module for circuit verification, state comparison, and noise characterization.

### What You'll Learn

| Sub-Topic | Key Concept | Exam Trap |
|-----------|-------------|-----------|
| 9.1 Clifford Circuits | Efficiently simulatable gates | T gate is NOT Clifford |
| 9.2 Operator Class | Matrix representation | Use `.equiv()` not `==` for phase-invariant |
| 9.3 Statevector | Pure quantum state vectors | Normalization requirement |
| 9.3.5 DensityMatrix | Mixed quantum states | Superposition ≠ Mixture |
| 9.4 Fidelity Measures | State/process comparison | Always in [0, 1] range |
| 9.5 Quantum Channels | Noise representations | Kraus vs SuperOp vs Choi |
| 9.6 Randomized Benchmarking | SPAM-free gate errors | EPC metric interpretation |

---

## 🧠 Conceptual Deep Dive

### The Quality Control Analogy

```
┌──────────────────────────────────────────────────────────────────┐
│                THE QUALITY CONTROL ANALOGY                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Manufacturing Plant = Quantum Computer                           │
│  Product Blueprint = Ideal Circuit/Gate                           │
│  Actual Product = Noisy Implementation                            │
│  Quality Inspector = Quantum Info Tools                           │
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │  Blueprint  │ vs │  Product    │ = │  Fidelity   │          │
│  │  (Ideal)    │    │  (Actual)   │    │  Score      │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                                                                  │
│  Quality Check Methods:                                          │
│  • Operator.equiv() = "Does it match the blueprint?"             │
│  • state_fidelity() = "How close is the state?"                  │
│  • RB = "What's the average error rate?"                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Why Quantum Info Matters

1. **Verification** - Confirm circuits do what you expect
2. **Benchmarking** - Measure hardware quality
3. **Debugging** - Find where things go wrong
4. **Optimization** - Choose best gate decompositions

---

## 🗺️ Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│               QUANTUM INFO TOOLS MAP                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   STATE TOOLS                    OPERATOR TOOLS                 │
│   ┌──────────────┐              ┌──────────────┐               │
│   │ Statevector  │              │  Operator    │               │
│   │ DensityMatrix│              │  Clifford    │               │
│   └──────────────┘              └──────────────┘               │
│          │                             │                        │
│          ▼                             ▼                        │
│   ┌──────────────┐              ┌──────────────┐               │
│   │state_fidelity│              │   .equiv()   │               │
│   │   (compare)  │              │  (compare)   │               │
│   └──────────────┘              └──────────────┘               │
│                                                                 │
│   NOISE TOOLS                    BENCHMARKING                   │
│   ┌──────────────┐              ┌──────────────┐               │
│   │ Kraus        │              │ StandardRB   │               │
│   │ SuperOp      │              │ (qiskit_exp) │               │
│   │ Choi         │              │              │               │
│   └──────────────┘              └──────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Quick Reference

| Class/Function | Import | Purpose | Returns |
|----------------|--------|---------|---------|
| `Clifford` | `qiskit.quantum_info` | Efficient Clifford simulation | `Clifford` object |
| `Operator` | `qiskit.quantum_info` | Unitary matrix representation | `Operator` object |
| `Statevector` | `qiskit.quantum_info` | Pure state vector | `Statevector` object |
| `DensityMatrix` | `qiskit.quantum_info` | Mixed state representation | `DensityMatrix` object |
| `state_fidelity()` | `qiskit.quantum_info` | Compare states | `float` in [0, 1] |
| `process_fidelity()` | `qiskit.quantum_info` | Compare processes | `float` in [0, 1] |
| `average_gate_fidelity()` | `qiskit.quantum_info` | Gate quality metric | `float` in [0, 1] |
| `Kraus` | `qiskit.quantum_info` | Kraus representation | `Kraus` object |
| `SuperOp` | `qiskit.quantum_info` | Superoperator matrix | `SuperOp` object |
| `Choi` | `qiskit.quantum_info` | Choi matrix | `Choi` object |

---

## 🛤️ Learning Path

```
START
  │
  ▼
┌─────────────────────────────────┐
│ 9.1 Clifford Circuits           │ ← Efficiently simulatable
│     "Which gates are Clifford?" │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.2 Operator Class              │ ← Matrix representation
│     "Circuit to unitary"        │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.3 Statevector                 │ ← Pure states only
│     "Pure quantum states"       │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.3.5 DensityMatrix             │ ← Mixed states & noise
│     "Mixed quantum states"      │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.4 Fidelity Measures           │ ← State/process comparison
│     "How close are they?"       │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.5 Quantum Channels            │ ← Noise modeling
│     "Kraus, SuperOp, Choi"      │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 9.6 Randomized Benchmarking     │ ← Hardware characterization
│     "SPAM-free error rates"     │
└─────────────────────────────────┘
  │
  ▼
 END
```

---

# 📖 TOPIC 9.1: Clifford Circuits

## 9.1.1 Clifford Gate Set

### Definition
The **Clifford group** consists of gates that map Pauli operators to Pauli operators under conjugation. These gates can be efficiently simulated classically using the stabilizer formalism.

**Clifford gates**: {H, S, CNOT, X, Y, Z, S†}

### Analogy
**"The Simulatable Club"** - Clifford gates are like a VIP club of gates that can be simulated efficiently on a classical computer. The T gate is NOT in the club - once you add T, you leave the realm of efficient classical simulation.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIFFORD GATE SET                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✅ IN THE CLUB (Efficiently Simulatable):                      │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌──────┐     │
│  │  H  │ │  S  │ │ S†  │ │  X  │ │  Y  │ │  Z  │ │ CNOT │     │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └──────┘     │
│                                                                 │
│  ❌ NOT IN THE CLUB (Makes circuits universal):                 │
│  ┌─────┐                                                        │
│  │  T  │  ← Adds universality, breaks efficient simulation      │
│  └─────┘                                                        │
│                                                                 │
│  WHY CLIFFORD MATTERS:                                          │
│  • Can simulate millions of qubits classically                  │
│  • Used in randomized benchmarking                              │
│  • Foundation of quantum error correction                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit.quantum_info import Clifford
from qiskit import QuantumCircuit

# Create Clifford from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  # Bell state preparation
cliff = Clifford(qc)

# Check if two Cliffords are equivalent
cliff1 = Clifford(circuit1)
cliff2 = Clifford(circuit2)
print(cliff1 == cliff2)  # Direct comparison works for Clifford

# Convert back to circuit
equivalent_circuit = cliff.to_circuit()

# Compose Cliffords
composed = cliff1.compose(cliff2)
```

### ⚠️ Trap Alert

**Trap: T gate is Clifford**
- ❌ **Wrong**: T gate is part of the Clifford group
- ✅ **Correct**: T gate is NOT Clifford - it makes circuits universal
- 🔍 **Why it's tricky**: T looks similar to S (both are phase gates)

```python
# ❌ WRONG - This is NOT a Clifford circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)  # T gate breaks Clifford!
# cliff = Clifford(qc)  # This will fail!

# ✅ CORRECT - This IS a Clifford circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)  # S gate is Clifford
cliff = Clifford(qc)  # Works!
```

### 🧠 Mnemonic

**"HSCP - No T"** (H, S, CNOT, Paulis - No T!)
- **H**adamard, **S** phase, **C**NOT, **P**aulis
- T is the "intruder" that breaks efficient simulation

### ⚡ Quick Check

**Q: Is a circuit with {H, CNOT, S, Z} gates efficiently simulatable?**

<details>
<summary>Answer</summary>

**A**: Yes! All these gates are Clifford gates, so the circuit can be efficiently simulated classically using the stabilizer formalism.

</details>

---

# 📖 TOPIC 9.2: Operator Class

## 9.2.1 Creating and Using Operators

### Definition
The `Operator` class represents the full unitary matrix of a quantum operation. It stores a $2^n \times 2^n$ complex matrix for an n-qubit operation.

### Analogy
**"The Full Recipe"** - While a circuit is like cooking instructions (steps), an Operator is the complete mathematical formula showing exactly what transformation happens. It's the "no secrets" view of a quantum operation.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    OPERATOR CLASS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Circuit → Operator                                              │
│  ┌───────────┐     ┌─────────────────────────┐                  │
│  │ ───[H]─── │  →  │ 1/√2 × [1   1]          │                  │
│  └───────────┘     │        [1  -1]          │                  │
│                    └─────────────────────────┘                  │
│                                                                 │
│  2 Qubits → 4×4 Matrix                                          │
│  n Qubits → 2ⁿ × 2ⁿ Matrix                                      │
│                                                                 │
│  KEY METHODS:                                                   │
│  • Operator(circuit)     Create from circuit                    │
│  • op.data               Get numpy matrix                       │
│  • op.equiv(other)       Compare (phase-invariant!)             │
│  • op.compose(other)     Matrix multiplication                  │
│  • op.tensor(other)      Tensor product                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
import numpy as np

# Create from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
op = Operator(qc)

# Get the unitary matrix
print(op.data)  # numpy 4×4 array

# Check if two circuits are equivalent (up to global phase!)
op1 = Operator(circuit1)
op2 = Operator(circuit2)
print(op1.equiv(op2))  # True if same up to global phase

# Compose operators (matrix multiplication)
combined = op1.compose(op2)  # op2 applied first, then op1

# Tensor product
tensor = op1.tensor(op2)  # op1 ⊗ op2
```

### ⚠️ Trap Alert

**Trap: Using == instead of .equiv()**
- ❌ **Wrong**: `op1 == op2` to check circuit equivalence
- ✅ **Correct**: `op1.equiv(op2)` for phase-invariant comparison
- 🔍 **Why it's tricky**: Global phase doesn't affect physics but changes the matrix

```python
from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
import numpy as np

# Two circuits that are equivalent up to global phase
qc1 = QuantumCircuit(1)
qc1.x(0)

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.global_phase = np.pi  # Add global phase

op1 = Operator(qc1)
op2 = Operator(qc2)

# ❌ WRONG - returns False due to global phase
print(op1 == op2)  # False (matrices differ by e^{iπ})

# ✅ CORRECT - returns True (same physics)
print(op1.equiv(op2))  # True!
```

### 🧠 Mnemonic

**"EQUIV for EQUIValent physics"**
- `==` checks matrix equality (strict)
- `.equiv()` checks physical equivalence (ignores global phase)

### ⚡ Quick Check

**Q: What method should you use to check if two circuits implement the same quantum operation?**

<details>
<summary>Answer</summary>

**A**: `Operator.equiv()` - This method compares operators up to a global phase, which is the physically meaningful comparison since global phases don't affect measurement outcomes.

</details>

---

## 9.2.2 Operator Composition

### Definition
Operator composition combines multiple operators using matrix multiplication. `op1.compose(op2)` applies op2 first, then op1.

### Analogy
**"Stacking Functions"** - Just like `f(g(x))` applies g first then f, `op1.compose(op2)` applies op2 to the state first, then op1.

### Implementation

```python
from qiskit.quantum_info import Operator
from qiskit.circuit.library import HGate, XGate

h_op = Operator(HGate())
x_op = Operator(XGate())

# H then X (X applied to result of H)
hx = x_op.compose(h_op)  # h_op first, then x_op

# Equivalent to:
qc = QuantumCircuit(1)
qc.h(0)
qc.x(0)
combined = Operator(qc)

print(hx.equiv(combined))  # True
```

### ⚠️ Trap Alert

**Trap: Compose order is counterintuitive**
- ❌ **Wrong**: `op1.compose(op2)` means "op1 then op2"
- ✅ **Correct**: `op1.compose(op2)` means "op2 first, then op1" (like matrix multiplication)

```python
# ❌ WRONG thinking
# op1.compose(op2) does NOT mean op1 first, then op2

# ✅ CORRECT
# op1.compose(op2) = op1 × op2 = op2 applied first!
```

### 🧠 Mnemonic

**"Compose = Right to Left"** (like matrix multiplication)
- `A.compose(B)` = A × B = B first, then A

### ⚡ Quick Check

**Q: If you want to apply H first then X, what's the correct compose call?**

<details>
<summary>Answer</summary>

**A**: `x_op.compose(h_op)` - The argument (h_op) is applied first, then the method caller (x_op).

</details>

---

# 📖 TOPIC 9.3: Statevector

## 9.3.1 Creating and Using Statevectors

### Definition
The `Statevector` class represents a pure quantum state as a complex vector of length $2^n$ for n qubits. Each element is the amplitude for a computational basis state.

### Analogy
**"The Probability Fingerprint"** - A Statevector is like a unique fingerprint showing exactly how the quantum state is distributed across all possible outcomes. The squared magnitudes give measurement probabilities.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    STATEVECTOR                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  |ψ⟩ = α|0⟩ + β|1⟩  →  Statevector([α, β])                     │
│                                                                 │
│  |00⟩ = [1, 0, 0, 0]     |+⟩ = [1/√2, 1/√2]                    │
│  |01⟩ = [0, 1, 0, 0]     |-⟩ = [1/√2, -1/√2]                   │
│  |10⟩ = [0, 0, 1, 0]     |i⟩ = [1/√2, i/√2]                    │
│  |11⟩ = [0, 0, 0, 1]                                            │
│                                                                 │
│  CONSTRAINT: |α|² + |β|² = 1 (normalization)                    │
│                                                                 │
│  KEY METHODS:                                                   │
│  • Statevector.from_label('0')    Create from label             │
│  • Statevector.from_instruction() Create from circuit           │
│  • sv.probabilities()             Get |amplitude|²              │
│  • sv.evolve(operator)            Apply operator                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit
import numpy as np

# Create from label
sv = Statevector.from_label('00')  # |00⟩ state
sv_plus = Statevector.from_label('+')  # |+⟩ state

# Create from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
bell_state = Statevector.from_instruction(qc)

# Get the state vector
print(bell_state.data)  # numpy array

# Get probabilities
probs = bell_state.probabilities()
print(probs)  # [0.5, 0, 0, 0.5] for Bell state

# Evolve with operator
from qiskit.quantum_info import Operator
x_op = Operator.from_label('X')
evolved = sv.evolve(x_op)
```

### ⚠️ Trap Alert

**Trap: Forgetting normalization**
- ❌ **Wrong**: `Statevector([1, 1])` is a valid quantum state
- ✅ **Correct**: `Statevector([1/np.sqrt(2), 1/np.sqrt(2)])` is normalized
- 🔍 **Why it's tricky**: Qiskit may normalize automatically, but conceptually wrong

```python
import numpy as np
from qiskit.quantum_info import Statevector

# ❌ CONCEPTUALLY WRONG (not normalized)
sv_wrong = Statevector([1, 1])  # Qiskit normalizes, but input is wrong

# ✅ CORRECT (properly normalized)
sv_correct = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])

# Check normalization
print(np.sum(np.abs(sv_correct.data)**2))  # Should be 1.0
```

### 🧠 Mnemonic

**"Amplitudes Squared Sum to One"**
- $\sum_i |a_i|^2 = 1$ always for valid quantum states

### ⚡ Quick Check

**Q: What does `Statevector.from_label('+')` return?**

<details>
<summary>Answer</summary>

**A**: The |+⟩ state = $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ represented as `Statevector([1/√2, 1/√2])` or approximately `[0.707, 0.707]`.

</details>

---

# 📖 TOPIC 9.3.5: DensityMatrix

## 9.3.5.1 Creating and Using DensityMatrix

### Definition
The `DensityMatrix` class represents a **mixed quantum state** using a density matrix $\rho$. Unlike Statevector (pure states only), DensityMatrix can represent:
- Pure states: $\rho = |\psi\rangle\langle\psi|$
- Mixed states: $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ (statistical mixture)

### Analogy
**"The Complete Picture vs The Snapshot"**
- **Statevector** = A perfect photograph of a single quantum state
- **DensityMatrix** = A blurry photo that could be a mixture of different states (classical uncertainty + quantum uncertainty)

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│              STATEVECTOR vs DENSITYMATRIX                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PURE STATE (both work):                                        │
│  |0⟩ → Statevector([1, 0])                                      │
│      → DensityMatrix([[1, 0],                                   │
│                       [0, 0]])                                  │
│                                                                 │
│  MIXED STATE (only DensityMatrix):                              │
│  50% |0⟩ + 50% |1⟩ (classical mixture)                          │
│      → DensityMatrix([[0.5, 0],                                 │
│                       [0, 0.5]])  # Maximally mixed             │
│                                                                 │
│  KEY DIFFERENCE:                                                │
│  • Pure state: Tr(ρ²) = 1                                       │
│  • Mixed state: Tr(ρ²) < 1                                      │
│                                                                 │
│  WHEN TO USE WHICH:                                             │
│  • Statevector: Ideal simulation, no noise                      │
│  • DensityMatrix: Noise simulation, open systems                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit.quantum_info import DensityMatrix, Statevector
from qiskit import QuantumCircuit
import numpy as np

# Create from label
rho = DensityMatrix.from_label('0')  # |0⟩⟨0|

# Create from Statevector
sv = Statevector.from_label('+')
rho_plus = DensityMatrix(sv)  # |+⟩⟨+|

# Create from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
rho_bell = DensityMatrix.from_instruction(qc)

# Get the density matrix
print(rho_bell.data)  # numpy 4×4 array

# Get probabilities
probs = rho_bell.probabilities()

# Check purity (pure state = 1, mixed < 1)
purity = rho_bell.purity()
print(f"Purity: {purity}")  # 1.0 for pure state

# Create maximally mixed state
mixed = DensityMatrix(np.eye(2) / 2)  # I/2
print(f"Mixed state purity: {mixed.purity()}")  # 0.5

# Evolve through a channel (noise!)
from qiskit.quantum_info import Kraus
rho_noisy = rho.evolve(noise_channel)
```

### ⚠️ Trap Alert

**Trap: Confusing Superposition with Classical Mixture**
- ❌ **Wrong**: `Statevector` can represent a 50/50 classical mixture of |0⟩ and |1⟩
- ✅ **Correct**: Only `DensityMatrix` can represent classical mixtures (mixed states)
- 🔍 **Why it's tricky**: The notation "50% |0⟩ + 50% |1⟩" is ambiguous!

**Two COMPLETELY Different Meanings**:

1. **Quantum Superposition** (Pure State - use Statevector):
  - |+⟩ = (|0⟩ + |1⟩)/√2
  - Coherent quantum state with interference
  - Can see interference patterns (e.g., H|+⟩ = |0⟩)
  - Purity = 1.0

2. **Classical Mixture** (Mixed State - use DensityMatrix):
  - 50% probability of |0⟩ OR 50% probability of |1⟩
  - Classical uncertainty (like a coin flip)
  - NO interference - just statistical randomness
  - Purity = 0.5

**The Key Difference**:
```python
# SUPERPOSITION (pure, coherent)
|+⟩ = (|0⟩ + |1⟩)/√2  ← Plus sign means INTERFERENCE
ρ = |+⟩⟨+| = [[0.5, 0.5],   ← Off-diagonal terms!
          [0.5, 0.5]]

# MIXTURE (mixed, incoherent)
ρ = 0.5|0⟩⟨0| + 0.5|1⟩⟨1| = [[0.5, 0],    ← NO off-diagonal!
                    [0, 0.5]]
```

**Physical Example**:
- **Superposition**: Photon in |H⟩+|V⟩ state (both polarizations AT ONCE)
- **Mixture**: Photon that's either |H⟩ OR |V⟩ (you just don't know which)

**Mnemonic**: "Off-diagonal = Quantum Magic" - If the density matrix has non-zero off-diagonal elements, you have superposition. If all off-diagonal elements are zero, you have a classical mixture.

```python
from qiskit.quantum_info import Statevector, DensityMatrix
import numpy as np

# |+⟩ = superposition (PURE state)
plus = Statevector.from_label('+')  
# This is NOT a 50/50 mixture of |0⟩ and |1⟩!
# It's a coherent superposition with interference

# 50/50 MIXTURE of |0⟩ and |1⟩ (MIXED state)
# Must use DensityMatrix!
mixed = DensityMatrix(np.array([[0.5, 0], [0, 0.5]]))

# Check the difference
print(f"|+⟩ purity: {DensityMatrix(plus).purity()}")  # 1.0 (pure)
print(f"Mixture purity: {mixed.purity()}")  # 0.5 (mixed)
```

### 🧠 Mnemonic

**"DM for Dirty/Mixed, SV for Single/Pure"**
- **D**ensity**M**atrix = **D**irty/**M**ixed states (noise, decoherence)
- **S**tate**V**ector = **S**ingle/**V**irgin pure states (ideal)

### ⚡ Quick Check

**Q: Can Statevector represent a 50% |0⟩ + 50% |1⟩ classical mixture?**

<details>
<summary>Answer</summary>

**A**: No! Statevector can only represent pure states. A classical mixture requires DensityMatrix. Note: |+⟩ = (|0⟩+|1⟩)/√2 is NOT a mixture - it's a coherent superposition (pure state).

</details>

---

# 📖 TOPIC 9.4: Fidelity Measures

## 9.4.1 State Fidelity

### Definition
**State fidelity** measures how close two quantum states are. For pure states, it's the squared overlap: $F = |\langle\psi|\phi\rangle|^2$. Always in range [0, 1] where 1 means identical.

### Analogy
**"Similarity Score"** - Fidelity is like a similarity percentage between two quantum states. 1.0 = identical twins, 0.5 = random, 0.0 = complete opposites.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                    FIDELITY SCALE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  0.0 ─────────── 0.5 ─────────── 0.9 ── 0.99 ── 1.0            │
│   │               │               │       │      │              │
│   ▼               ▼               ▼       ▼      ▼              │
│  Orthogonal   Random/No      Good    Excellent  Perfect         │
│  (opposite)   correlation   quality   quality   match           │
│                                                                 │
│  FIDELITY FORMULA (pure states):                                │
│  F(|ψ⟩, |φ⟩) = |⟨ψ|φ⟩|²                                        │
│                                                                 │
│  ALWAYS: 0 ≤ F ≤ 1                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Fidelity Interpretation Guide

| Fidelity | Quality | Interpretation |
|----------|---------|----------------|
| 0.99+ | Excellent | High-quality gate/state |
| 0.95-0.99 | Good | Acceptable for most applications |
| 0.90-0.95 | Moderate | May need error mitigation |
| < 0.90 | Poor | Significant noise present |
| 0.5 | Random | No correlation (for qubits) |
| 0.0 | Orthogonal | Completely different states |

### Implementation

```python
from qiskit.quantum_info import state_fidelity, Statevector

# Compare two states
state1 = Statevector.from_label('0')
state2 = Statevector.from_label('+')

fid = state_fidelity(state1, state2)
print(f"Fidelity: {fid}")  # 0.5 (|⟨0|+⟩|² = 0.5)

# Identical states
same_fid = state_fidelity(state1, state1)
print(f"Same state fidelity: {same_fid}")  # 1.0

# Orthogonal states
state3 = Statevector.from_label('1')
ortho_fid = state_fidelity(state1, state3)
print(f"Orthogonal fidelity: {ortho_fid}")  # 0.0
```

### ⚠️ Trap Alert

**Trap: Thinking fidelity can exceed 1**
- ❌ **Wrong**: "High fidelity might be 1.5 or 2.0"
- ✅ **Correct**: Fidelity is ALWAYS in [0, 1]
- 🔍 **Why it's tricky**: Other metrics (like SNR) can exceed 1

```python
from qiskit.quantum_info import state_fidelity, Statevector

state1 = Statevector.from_label('0')
state2 = Statevector.from_label('+')

fid = state_fidelity(state1, state2)

# Fidelity is ALWAYS between 0 and 1
assert 0 <= fid <= 1, "Fidelity must be in [0, 1]!"
```

### 🧠 Mnemonic

**"Fidelity = Faithful to [0,1]"**
- **F**idelity is **F**aithfully between 0 and 1, always

### ⚡ Quick Check

**Q: What is the fidelity between |0⟩ and |1⟩?**

<details>
<summary>Answer</summary>

**A**: 0.0 - They are orthogonal states with zero overlap: $|\langle 0|1\rangle|^2 = 0$

</details>

---

## 9.4.2 Process and Average Gate Fidelity

### Definition
- **Process fidelity**: Compares quantum channels/processes
- **Average gate fidelity**: Average fidelity over all possible input states (more practical)

### Implementation

```python
from qiskit.quantum_info import process_fidelity, average_gate_fidelity
from qiskit.quantum_info import Operator

# Compare ideal vs noisy operation
ideal_gate = Operator.from_label('X')
noisy_gate = Operator(noisy_circuit)

# Process fidelity
proc_fid = process_fidelity(noisy_gate, ideal_gate)

# Average gate fidelity (standard metric)
avg_fid = average_gate_fidelity(noisy_gate, ideal_gate)

print(f"Process fidelity: {proc_fid}")
print(f"Average gate fidelity: {avg_fid}")
```

### 🧠 Mnemonic

**"AGF = Average over All inputs"**
- Average Gate Fidelity averages over all possible input states

### ⚡ Quick Check

**Q: Which fidelity measure is the standard for reporting gate quality?**

<details>
<summary>Answer</summary>

**A**: Average gate fidelity - It's the standard metric because it averages performance over all possible input states, giving a more practical measure of gate quality.

</details>

---

# 📖 TOPIC 9.5: Quantum Channels

## 9.5.1 Channel Representations

### Definition
A **quantum channel** describes how a quantum state evolves, including noise effects. Qiskit provides three representations:
- **Kraus**: Sum of operators $\rho \to \sum_k K_k \rho K_k^\dagger$
- **SuperOp**: Superoperator matrix on vectorized density matrix
- **Choi**: Choi matrix representation (useful for tomography)

### Analogy
**"Three Views of the Same Noise"** - Like describing weather as temperature/humidity/pressure (different but equivalent), Kraus/SuperOp/Choi are different ways to represent the same quantum noise process.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│              QUANTUM CHANNEL REPRESENTATIONS                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ALL DESCRIBE THE SAME NOISE PROCESS!                           │
│                                                                 │
│  KRAUS: ρ → Σₖ Kₖ ρ Kₖ†                                         │
│         Sum of "error operators" acting on state                │
│                                                                 │
│  SUPEROP: vec(ρ) → S × vec(ρ)                                   │
│           Matrix acting on vectorized density matrix            │
│                                                                 │
│  CHOI: J = (I ⊗ Λ)(|Φ⁺⟩⟨Φ⁺|)                                   │
│        Channel applied to half of maximally entangled state     │
│                                                                 │
│  CONVERSIONS:                                                   │
│  Kraus ←→ SuperOp ←→ Choi                                       │
│  (All equivalent, use what's convenient)                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Common Noise Channels

| Channel | Effect | Use Case |
|---------|--------|----------|
| **Depolarizing** | Random Pauli errors | General noise model |
| **Amplitude Damping** | Energy relaxation (T1) | Models spontaneous emission |
| **Phase Damping** | Dephasing (T2) | Loss of coherence |
| **Bit Flip** | X errors with probability p | Simple error model |
| **Phase Flip** | Z errors with probability p | Simple error model |

### Implementation

```python
from qiskit.quantum_info import Kraus, SuperOp, Choi
import numpy as np

# Create depolarizing channel
def depolarizing_kraus(p):
    """Depolarizing channel with error probability p."""
    I = np.eye(2)
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    
    kraus_ops = [
        np.sqrt(1 - 3*p/4) * I,
        np.sqrt(p/4) * X,
        np.sqrt(p/4) * Y,
        np.sqrt(p/4) * Z
    ]
    return Kraus(kraus_ops)

channel = depolarizing_kraus(0.1)

# Convert between representations
superop = SuperOp(channel)
choi = Choi(channel)

# Apply channel to state
from qiskit.quantum_info import DensityMatrix
rho = DensityMatrix.from_label('0')
rho_noisy = rho.evolve(channel)
```

### ⚠️ Trap Alert

**Trap: Confusing when to use which representation**
- **Kraus**: Best for understanding physics (sum of errors)
- **SuperOp**: Best for mathematical manipulation
- **Choi**: Best for tomography and complete positivity checks

### 🧠 Mnemonic

**"KSC = Know, Solve, Check"**
- **K**raus: Know the physics
- **S**uperOp: Solve mathematically
- **C**hoi: Check properties (like complete positivity)

### ⚡ Quick Check

**Q: What does a depolarizing channel do to a quantum state?**

<details>
<summary>Answer</summary>

**A**: A depolarizing channel applies random Pauli errors (X, Y, Z) with some probability p, effectively "mixing" the state towards the maximally mixed state. With probability (1-p) the state is unchanged, and with probability p it gets a random Pauli error.

</details>

---

# 📖 TOPIC 9.6: Randomized Benchmarking

## 9.6.1 RB Protocol

### Definition
**Randomized Benchmarking (RB)** measures average gate error rates by applying random sequences of Clifford gates and measuring fidelity decay. It's SPAM-free (independent of state preparation and measurement errors).

### Analogy
**"Stress Test for Gates"** - RB is like a stress test for quantum gates. Apply many random operations, then undo them all - if gates are perfect, you get back to start. The error rate tells you how much "drift" accumulates.

### Math/Visual

```
┌─────────────────────────────────────────────────────────────────┐
│              RANDOMIZED BENCHMARKING PROTOCOL                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  STEP 1: Prepare |0⟩                                            │
│          │                                                      │
│  STEP 2: Apply random Cliffords: C₁ → C₂ → ... → Cₘ            │
│          │                                                      │
│  STEP 3: Apply inverse: C_inv = (Cₘ...C₂C₁)⁻¹                  │
│          │                                                      │
│  STEP 4: Measure (should return |0⟩ if no errors)              │
│          │                                                      │
│  STEP 5: Repeat for different sequence lengths m               │
│          │                                                      │
│  STEP 6: Fit exponential decay → extract EPC                   │
│                                                                 │
│  DECAY CURVE:                                                   │
│  F(m) = A × p^m + B                                             │
│  where p = 1 - EPC × (d-1)/d                                    │
│                                                                 │
│  EPC = Error Per Clifford (what we want!)                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit_experiments.library import StandardRB
from qiskit_ibm_runtime import QiskitRuntimeService

# Setup backend
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Create RB experiment
rb_exp = StandardRB(
    physical_qubits=[0],           # Which qubit(s)
    lengths=[1, 10, 20, 50, 100],  # Sequence lengths
    num_samples=10,                # Circuits per length
    seed=42
)

# Run experiment
rb_data = rb_exp.run(backend).block_for_results()

# Extract Error Per Clifford
epc = rb_data.analysis_results('EPC').value
print(f"Error per Clifford: {epc:.4f}")

# Typical good values: EPC ≈ 0.001 - 0.01
```

### Interpreting RB Results

| Metric | Meaning | Good Values |
|--------|---------|-------------|
| **EPC** | Error per Clifford | < 0.01 (1%) |
| **Average Gate Fidelity** | 1 - EPC × (d-1)/d | > 0.99 |
| **Decay Rate (p)** | How fast fidelity drops | Close to 1 |

### ⚠️ Trap Alert

**Trap: RB measures state preparation errors**
- ❌ **Wrong**: RB includes SPAM (state prep and measurement) errors
- ✅ **Correct**: RB is SPAM-free - it isolates gate errors
- 🔍 **Why it's tricky**: The inverse operation cancels SPAM effects

```
# RB is SPAM-FREE because:
# |0⟩ → C₁...Cₘ → C_inv → |0⟩
#  ↑                        ↑
#  SPAM errors here      and here CANCEL OUT!
```

### 🧠 Mnemonic

**"RB = Really 'Bout Gates (not SPAM)"**
- RB measures gate errors only, not state prep or measurement

### ⚡ Quick Check

**Q: Why is randomized benchmarking considered SPAM-free?**

<details>
<summary>Answer</summary>

**A**: RB is SPAM-free because the random Clifford sequence is followed by its inverse, so the ideal outcome is always the initial state. This means state preparation errors at the start and measurement errors at the end affect all sequences equally and cancel out when fitting the exponential decay curve. Only gate errors accumulate with sequence length.

</details>

---

# 📖 Topic Consolidated Review

## Static vs Instance Methods Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                QUANTUM INFO COMPARISON                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLASS         │ PURPOSE              │ KEY METHOD              │
│  ─────────────────────────────────────────────────────────────  │
│  Clifford      │ Efficient simulation │ Clifford(circuit)       │
│  Operator      │ Full unitary matrix  │ op.equiv(other)         │
│  Statevector   │ Pure state vector    │ sv.probabilities()      │
│  DensityMatrix │ Mixed states         │ dm.evolve(channel)      │
│                                                                 │
│  FIDELITY FUNCTIONS:                                            │
│  state_fidelity(s1, s2)      → Compare states                   │
│  process_fidelity(c1, c2)    → Compare processes                │
│  average_gate_fidelity(c, t) → Standard gate metric             │
│                                                                 │
│  CHANNEL REPRESENTATIONS:                                       │
│  Kraus   → Physics intuition (sum of operators)                 │
│  SuperOp → Mathematical manipulation                            │
│  Choi    → Tomography and property checks                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Key Comparisons

| Aspect | Clifford | Operator | Statevector |
|--------|----------|----------|-------------|
| **Represents** | Clifford circuits | Any unitary | Pure states |
| **Storage** | Efficient (stabilizer) | Full matrix | Full vector |
| **Scalability** | Millions of qubits | ~15 qubits | ~30 qubits |
| **Comparison** | `==` works | Use `.equiv()` | Use `state_fidelity()` |

---

# ⚠️ Master Trap List

## Trap 1: T Gate is Clifford (CRITICAL!)

```python
# ❌ WRONG - T gate is NOT Clifford
qc = QuantumCircuit(1)
qc.t(0)
cliff = Clifford(qc)  # FAILS!

# ✅ CORRECT - S gate IS Clifford
qc = QuantumCircuit(1)
qc.s(0)
cliff = Clifford(qc)  # Works!
```

**Mnemonic**: "HSCP - No T!" (H, S, CNOT, Paulis)

---

## Trap 2: Using == Instead of .equiv() for Operators

```python
from qiskit.quantum_info import Operator
import numpy as np

# Circuits equivalent up to global phase
op1 = Operator(circuit1)
op2 = Operator(circuit2)

# ❌ WRONG - False due to global phase
print(op1 == op2)  # False

# ✅ CORRECT - True (same physics)
print(op1.equiv(op2))  # True
```

**Mnemonic**: "EQUIV for EQUIValent physics"

---

## Trap 3: Fidelity Can Exceed 1

```python
# ❌ WRONG - Fidelity is always in [0, 1]
# There is no fidelity > 1!

# ✅ CORRECT
fid = state_fidelity(state1, state2)
assert 0 <= fid <= 1  # Always true!
```

**Mnemonic**: "Fidelity = Faithful to [0,1]"

---

## Trap 4: RB Measures SPAM Errors

```python
# ❌ WRONG - RB does NOT measure SPAM errors
# It's specifically designed to be SPAM-free!

# ✅ CORRECT - RB isolates GATE errors only
# The inverse operation cancels SPAM effects
```

**Mnemonic**: "RB = Really 'Bout Gates (not SPAM)"

---

## Trap 5: Compose Order Confusion

```python
# ❌ WRONG thinking: op1.compose(op2) = op1 first
# This is NOT how compose works!

# ✅ CORRECT: op1.compose(op2) = op2 first, then op1
# Like matrix multiplication: A × B means B first
```

**Mnemonic**: "Compose = Right to Left"

---

## Trap 6: Superposition = Mixture (CRITICAL!)

```python
from qiskit.quantum_info import Statevector, DensityMatrix
import numpy as np

# |+⟩ = superposition (PURE state with interference)
plus = Statevector.from_label('+')
# ❌ WRONG - This is NOT a 50/50 mixture!

# 50/50 MIXTURE (no interference, classical randomness)
mixed = DensityMatrix(np.array([[0.5, 0], [0, 0.5]]))

# The difference: PURITY
print(DensityMatrix(plus).purity())  # 1.0 (pure)
print(mixed.purity())                 # 0.5 (mixed)

# ❌ WRONG - Using Statevector for mixed states
# Statevector CANNOT represent classical mixtures!

# ✅ CORRECT - Use DensityMatrix for mixed states
```

**Mnemonic**: "DM for Dirty/Mixed, SV for Single/Pure"

---

# 🧠 All Mnemonics Summary

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **HSCP - No T!** | Clifford gates: H, S, CNOT, Paulis (NOT T) |
| 2 | **EQUIV for EQUIValent** | Use .equiv() not == for operators |
| 3 | **Fidelity = Faithful to [0,1]** | Fidelity always between 0 and 1 |
| 4 | **RB = Really 'Bout Gates** | RB is SPAM-free (gate errors only) |
| 5 | **Compose = Right to Left** | op1.compose(op2) applies op2 first |
| 6 | **KSC = Know, Solve, Check** | Kraus/SuperOp/Choi usage |
| 7 | **AGF = Average over All** | Average Gate Fidelity averages all inputs |
| 8 | **Amplitudes Squared Sum to One** | Statevector normalization |
| 9 | **DM for Dirty/Mixed, SV for Single/Pure** | When to use DensityMatrix vs Statevector |

---

# 📝 Practice Exam

## Question 1: Clifford Gates

**Which gate is NOT in the Clifford group?**

A) H (Hadamard)  
B) S (Phase)  
C) T (π/8)  
D) CNOT  

<details>
<summary>Answer</summary>

**C) T (π/8)**

The T gate is NOT Clifford. Clifford gates are {H, S, S†, CNOT, X, Y, Z}. The T gate makes circuits universal but breaks efficient simulation.

**Mnemonic**: "HSCP - No T!"
</details>

---

## Question 2: Operator Equivalence

**What method checks if two operators are equivalent up to global phase?**

A) `op1 == op2`  
B) `op1.equiv(op2)`  
C) `op1.equal(op2)`  
D) `op1.compare(op2)`  

<details>
<summary>Answer</summary>

**B) `op1.equiv(op2)`**

The `.equiv()` method compares operators ignoring global phase, which is the physically meaningful comparison.

**Mnemonic**: "EQUIV for EQUIValent physics"
</details>

---

## Question 3: Fidelity Range

**What is the range of state fidelity?**

A) [-1, 1]  
B) [0, 1]  
C) [0, ∞)  
D) (-∞, ∞)  

<details>
<summary>Answer</summary>

**B) [0, 1]**

Fidelity is always between 0 (orthogonal states) and 1 (identical states).

**Mnemonic**: "Fidelity = Faithful to [0,1]"
</details>

---

## Question 4: Randomized Benchmarking

**What does RB measure?**

A) State preparation errors  
B) Measurement errors  
C) Gate errors (SPAM-free)  
D) All of the above  

<details>
<summary>Answer</summary>

**C) Gate errors (SPAM-free)**

RB is specifically designed to measure gate errors independent of state preparation and measurement errors. The inverse operation in the protocol cancels SPAM effects.

**Mnemonic**: "RB = Really 'Bout Gates (not SPAM)"
</details>

---

## Question 5: Compose Order

**What does `x_op.compose(h_op)` represent?**

A) X gate then H gate  
B) H gate then X gate  
C) X and H applied simultaneously  
D) Tensor product of X and H  

<details>
<summary>Answer</summary>

**B) H gate then X gate**

`.compose()` works like matrix multiplication - the argument (h_op) is applied first, then the method caller (x_op).

**Mnemonic**: "Compose = Right to Left"
</details>

---

## Question 6: State Fidelity Calculation

**What is `state_fidelity(|0⟩, |+⟩)`?**

A) 0.0  
B) 0.5  
C) 0.707  
D) 1.0  

<details>
<summary>Answer</summary>

**B) 0.5**

|+⟩ = (|0⟩ + |1⟩)/√2, so:
$F = |\langle 0|+\rangle|^2 = |1/\sqrt{2}|^2 = 0.5$

</details>

---

## Question 7: Channel Representations

**Which representation is best for understanding the physics of a noise channel?**

A) Kraus  
B) SuperOp  
C) Choi  
D) All equivalent  

<details>
<summary>Answer</summary>

**A) Kraus**

Kraus representation shows the channel as a sum of "error operators," making the physics intuitive. SuperOp is better for math, Choi is better for tomography.

**Mnemonic**: "KSC = Know (Kraus), Solve (SuperOp), Check (Choi)"
</details>

---

## Question 8: EPC Interpretation

**An EPC of 0.005 means:**

A) 0.5% error per Clifford gate  
B) 5% error per Clifford gate  
C) 50% error per Clifford gate  
D) Cannot determine  

<details>
<summary>Answer</summary>

**A) 0.5% error per Clifford gate**

EPC = 0.005 = 0.5% error rate. This is a good value for modern quantum hardware.

</details>

---

## Question 9: Statevector vs DensityMatrix

**Can `Statevector` represent a 50% |0⟩ + 50% |1⟩ classical mixture?**

A) Yes, using `Statevector([0.5, 0.5])`  
B) Yes, using `Statevector.from_label('+')`  
C) No, only `DensityMatrix` can represent mixed states  
D) Yes, using `Statevector([1, 1])`  

<details>
<summary>Answer</summary>

**C) No, only `DensityMatrix` can represent mixed states**

Statevector can only represent pure states. A classical mixture requires DensityMatrix. Note: |+⟩ is a coherent superposition (pure), NOT a classical mixture!

**Key**: Superposition ≠ Mixture
- Superposition (|+⟩): Pure state, purity = 1
- Mixture (50% |0⟩ + 50% |1⟩): Mixed state, purity = 0.5

**Mnemonic**: "DM for Dirty/Mixed, SV for Single/Pure"
</details>

---

### Part B: Code Analysis (3-5 minutes each)

**Q10**: What does this code output?
```python
from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
import numpy as np

qc1 = QuantumCircuit(1)
qc1.h(0)

qc2 = QuantumCircuit(1)
qc2.h(0)
qc2.global_phase = np.pi

op1 = Operator(qc1)
op2 = Operator(qc2)

print(op1 == op2)
print(op1.equiv(op2))
```

<details>
<summary>Answer</summary>

**Output**:
```
False
True
```

**Step-by-step**:
1. Both circuits apply H gate
2. qc2 has an additional global phase of π
3. `==` compares matrices exactly → Different due to phase → `False`
4. `.equiv()` ignores global phase → Same physics → `True`

**Topic**: Operator Class
**Trap tested**: Using == instead of .equiv()
</details>

---

**Q11**: What is the purity of each state?
```python
from qiskit.quantum_info import Statevector, DensityMatrix
import numpy as np

# State A: |+⟩
sv_plus = Statevector.from_label('+')
dm_plus = DensityMatrix(sv_plus)

# State B: I/2 (maximally mixed)
dm_mixed = DensityMatrix(np.eye(2) / 2)

print(f"A: {dm_plus.purity()}")
print(f"B: {dm_mixed.purity()}")
```

<details>
<summary>Answer</summary>

**Output**:
```
A: 1.0
B: 0.5
```

**Step-by-step**:
1. |+⟩ is a PURE state (superposition, not mixture)
2. Pure states have purity = Tr(ρ²) = 1
3. Maximally mixed state I/2 has purity = 0.5 for 1 qubit
4. General: purity = 1/d for maximally mixed (d = dimension)

**Topic**: Statevector vs DensityMatrix
**Trap tested**: Superposition ≠ Mixture
</details>

---

**Q12**: Does this code raise an error?
```python
from qiskit.quantum_info import Clifford
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.t(0)  # T gate
qc.cx(0, 1)

cliff = Clifford(qc)
```

<details>
<summary>Answer</summary>

**Output**: `QiskitError` - Circuit contains non-Clifford gate

**Explanation**:
1. H gate → Clifford ✅
2. T gate → NOT Clifford ❌
3. CNOT → Clifford ✅
4. Clifford() constructor fails because T gate is present

**Topic**: Clifford Circuits
**Trap tested**: T gate is NOT Clifford
**Mnemonic**: "HSCP - No T!"
</details>

---

**Q13**: What fidelity value will this print?
```python
from qiskit.quantum_info import state_fidelity, Statevector

state_0 = Statevector.from_label('0')
state_1 = Statevector.from_label('1')

fid = state_fidelity(state_0, state_1)
print(fid)
```

<details>
<summary>Answer</summary>

**Output**: `0.0`

**Explanation**:
- |0⟩ and |1⟩ are orthogonal states
- Fidelity = |⟨0|1⟩|² = |0|² = 0
- Orthogonal states always have fidelity 0

**Topic**: Fidelity Measures
</details>

---

**Q14**: What is the result of this compose operation?
```python
from qiskit.quantum_info import Operator
from qiskit.circuit.library import HGate, ZGate

h_op = Operator(HGate())
z_op = Operator(ZGate())

# Apply H first, then Z
result = z_op.compose(h_op)

# Check equivalence with circuit
from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
circuit_op = Operator(qc)

print(result.equiv(circuit_op))
```

<details>
<summary>Answer</summary>

**Output**: `True`

**Explanation**:
1. `z_op.compose(h_op)` means: apply h_op first, then z_op
2. This is like matrix multiplication: Z × H
3. The circuit qc applies H then Z → same operation
4. `.equiv()` confirms they're equivalent

**Topic**: Operator Composition
**Trap tested**: Compose order (right to left)
**Mnemonic**: "Compose = Right to Left"
</details>

---

### Part C: Scenario-Based (5-7 minutes each)

**Q15**: You need to verify that your custom gate decomposition is correct. The original gate is a Toffoli (CCX), and you've decomposed it into a circuit using only single-qubit gates and CNOTs. How do you verify equivalence?

<details>
<summary>Answer</summary>

**Approach**:
1. Create Operator from both circuits
2. Use `.equiv()` for phase-invariant comparison
3. Don't use `==` (global phase may differ)

**Implementation**:
```python
from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit
from qiskit.circuit.library import CCXGate

# Original Toffoli
qc_original = QuantumCircuit(3)
qc_original.ccx(0, 1, 2)

# Your decomposition (example)
qc_decomposed = QuantumCircuit(3)
# ... your decomposition gates here ...

# Verify
op_original = Operator(qc_original)
op_decomposed = Operator(qc_decomposed)

if op_original.equiv(op_decomposed):
    print("✅ Decomposition is correct!")
else:
    print("❌ Decomposition differs from original")
```

**Topics combined**: Operator class, equiv() method
</details>

---

**Q16**: You're running a quantum algorithm on noisy hardware and want to characterize the gate errors. You need a metric that is independent of state preparation and measurement errors. Which technique and metric should you use?

<details>
<summary>Answer</summary>

**Approach**:
1. Use Randomized Benchmarking (RB)
2. RB is SPAM-free (independent of state prep and measurement)
3. Extract Error Per Clifford (EPC) metric

**Implementation**:
```python
from qiskit_experiments.library import StandardRB
from qiskit_ibm_runtime import QiskitRuntimeService

# Setup
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Create RB experiment
rb_exp = StandardRB(
    physical_qubits=[0],
    lengths=[1, 10, 20, 50, 100],
    num_samples=10,
    seed=42
)

# Run and extract EPC
rb_data = rb_exp.run(backend).block_for_results()
epc = rb_data.analysis_results('EPC').value
print(f"Error per Clifford: {epc}")

# Interpretation: EPC < 0.01 (1%) is good
```

**Topics combined**: Randomized Benchmarking, EPC metric
**Key insight**: RB uses inverse operation to cancel SPAM effects
</details>

---

**Q17**: You need to model decoherence on a quantum state. The state |+⟩ should lose its coherence over time and approach the maximally mixed state. Which quantum_info classes should you use?

<details>
<summary>Answer</summary>

**Approach**:
1. Cannot use Statevector (pure states only)
2. Must use DensityMatrix (can represent mixed states)
3. Use quantum channels (Kraus/SuperOp) to model noise

**Implementation**:
```python
from qiskit.quantum_info import DensityMatrix, Statevector
import numpy as np

# Start with |+⟩ as DensityMatrix
sv_plus = Statevector.from_label('+')
rho = DensityMatrix(sv_plus)
print(f"Initial purity: {rho.purity()}")  # 1.0

# Create dephasing channel (phase damping)
def dephasing_channel(p):
    """Phase damping with probability p."""
    K0 = np.array([[1, 0], [0, np.sqrt(1-p)]])
    K1 = np.array([[0, 0], [0, np.sqrt(p)]])
    return [K0, K1]

from qiskit.quantum_info import Kraus

# Apply increasing dephasing
for p in [0.0, 0.3, 0.6, 1.0]:
    channel = Kraus(dephasing_channel(p))
    rho_noisy = rho.evolve(channel)
    print(f"p={p}: purity={rho_noisy.purity():.3f}")

# At p=1.0, state approaches maximally mixed
```

**Topics combined**: DensityMatrix, Kraus channels, purity
**Key insight**: Statevector cannot represent decoherence
</details>

---

### Score Yourself

| Section | Total Qs | Your Score | Percentage |
|---------|----------|------------|------------|
| Part A (Quick Fire) | 9 | /9 | % |
| Part B (Code Analysis) | 5 | /5 | % |
| Part C (Scenarios) | 3 | /3 | % |
| **TOTAL** | **17** | **/17** | **%** |

**Interpretation**:
- 90-100%: Ready for Section 9 exam questions
- 75-89%: Review weak areas, focus on traps
- Below 75%: Re-study this section

---

# 💡 Key Takeaways

1. **MEMORIZE**: T gate is NOT Clifford (HSCP - No T!)
2. **Operator comparison**: Use `.equiv()` not `==` for phase-invariant comparison
3. **Fidelity**: Always in [0, 1], 1 is perfect
4. **RB**: SPAM-free gate error measurement
5. **Compose order**: `op1.compose(op2)` = op2 first, then op1
6. **Channel representations**: Kraus (physics), SuperOp (math), Choi (tomography)
7. **Statevector vs DensityMatrix**: SV = pure states only, DM = pure + mixed
8. **Average gate fidelity**: Standard metric for gate quality

---

## ✅ Concept Mastery Checklist

- [ ] I can explain what makes a gate "Clifford" in one sentence
- [ ] I understand why Clifford circuits are efficiently simulatable
- [ ] I know the difference between Statevector and DensityMatrix
- [ ] I can explain what fidelity measures and its range
- [ ] I understand why RB is SPAM-free
- [ ] I can describe the three quantum channel representations

## ✅ Code Mastery Checklist

- [ ] I can create a `Clifford` object from a circuit
- [ ] I can use `Operator.equiv()` for phase-invariant comparison
- [ ] I can create Statevector using `from_label()` and `from_instruction()`
- [ ] I can create DensityMatrix and check purity
- [ ] I can calculate state fidelity using `state_fidelity()`
- [ ] I can use `compose()` correctly (understanding the order)

## ✅ Trap Avoidance Checklist

- [ ] I know T gate is NOT Clifford (won't confuse with S)
- [ ] I will use `.equiv()` not `==` for operator comparison
- [ ] I know fidelity is ALWAYS in [0, 1]
- [ ] I understand compose order is "right to left"
- [ ] I know superposition ≠ mixture (|+⟩ is pure, not mixed)
- [ ] I know RB measures gate errors only (SPAM-free)

## 🧠 Mnemonic Recall

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 9 MNEMONICS - FINAL REVIEW                              │
├─────────────────────────────────────────────────────────────────┤
│ • "HSCP - No T!" - Clifford gates (no T gate!)                  │
│ • "EQUIV for EQUIValent" - Use .equiv() not ==                  │
│ • "Fidelity = Faithful to [0,1]" - Range always 0-1             │
│ • "RB = Really 'Bout Gates" - SPAM-free                         │
│ • "Compose = Right to Left" - Like matrix multiplication        │
│ • "KSC = Know, Solve, Check" - Kraus/SuperOp/Choi               │
│ • "AGF = Average over All" - Average gate fidelity              │
│ • "Amplitudes Squared Sum to One" - Normalization               │
│ • "DM for Dirty/Mixed, SV for Single/Pure" - State types        │
└─────────────────────────────────────────────────────────────────┘
```

## 📋 One-Page Summary

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 9: QUANTUM INFORMATION - EXAM READY SUMMARY             │
├─────────────────────────────────────────────────────────────────┤
│ MAIN TOPICS:                                                    │
│ 1. Clifford Circuits: Efficiently simulatable ({H,S,CNOT,P})    │
│ 2. Operator Class: Full unitary matrix representation           │
│ 3. Statevector/DensityMatrix: Pure vs mixed state handling      │
│ 4. Fidelity Measures: State/process comparison [0,1]            │
│ 5. Quantum Channels: Kraus/SuperOp/Choi representations         │
│ 6. Randomized Benchmarking: SPAM-free error measurement         │
├─────────────────────────────────────────────────────────────────┤
│ MUST-REMEMBER CODE:                                             │
│ • Clifford(circuit) - Create Clifford (fails if T gate!)        │
│ • op1.equiv(op2) - Phase-invariant comparison                   │
│ • Statevector.from_label('+') - Create |+⟩ state                │
│ • DensityMatrix(sv).purity() - Check if pure (=1) or mixed (<1) │
│ • state_fidelity(s1, s2) - Compare states [0,1]                 │
│ • x_op.compose(h_op) - H first, then X (right to left!)         │
├─────────────────────────────────────────────────────────────────┤
│ TOP 3 TRAPS:                                                    │
│ 1. T gate is NOT Clifford - "HSCP - No T!"                      │
│ 2. Use .equiv() not == - "EQUIV for EQUIValent"                 │
│ 3. Superposition ≠ Mixture - "DM for Dirty/Mixed"               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 Files in This Section

| File | Description | Lines |
|------|-------------|-------|
| [README.md](./README.md) | This file - concepts, traps, mnemonics | ~1770 |
| [quantum_info_advanced.ipynb](./quantum_info_advanced.ipynb) | Code laboratory - APIs, verification, challenges | 28 cells |
| [quantum_info_advanced_OLD.ipynb](./quantum_info_advanced_OLD.ipynb) | Backup of original notebook | 23 cells |
| [README_OLD.md](./README_OLD.md) | Backup of original README | ~438 |

---

## 🚀 Next Steps

1. **Run the notebook**: Execute all cells in [quantum_info_advanced.ipynb](./quantum_info_advanced.ipynb)
2. **Complete challenges**: Test yourself with the 3 code challenges
3. **Take practice exam**: Score yourself on all 17 questions above
4. **Review weak areas**: Focus on any topics where you scored < 80%
5. **Move to next section**: Proceed to Section 1 (Quantum Operations) for gate fundamentals

---

## 🔗 Related Sections

- **Section 1**: Single/Multi-qubit gates (building blocks for Clifford)
- **Section 4**: Running circuits (needed before benchmarking)
- **Section 7**: Results interpretation (fidelity from experiments)

---

## 📚 Additional Resources

- [Qiskit Quantum Information API](https://docs.quantum.ibm.com/api/qiskit/quantum_info)
- [Qiskit Experiments Documentation](https://qiskit-community.github.io/qiskit-experiments/)
- Notebook: [quantum_info_advanced.ipynb](./quantum_info_advanced.ipynb)

---

**Remember the #1 Exam Trap**:
```python
# ❌ T gate is NOT Clifford!
# ✅ Clifford = {H, S, CNOT, X, Y, Z}
```

🎯 **Exam Success Tip**: Write "HSCP - No T!" on your scratch paper!

---

*Last Updated: December 2025*
