# Section 3: Create Circuits (18% of Exam - HIGHEST WEIGHT!)

> **Exam Weight**: ~12 questions | **Difficulty**: Medium-High | **Must Master**: ✅✅✅

---

## 📖 Overview

This is the **MOST IMPORTANT SECTION** for the certification exam! Understanding circuit creation, composition, and manipulation is absolutely critical. This section covers everything from basic circuit creation to advanced parameterized circuits for variational algorithms.

### What You'll Learn

1. **Circuit Basics**: Creating circuits, properties, registers
2. **Circuit Composition**: `compose()`, `append()`, `tensor()`
3. **Parameterized Circuits**: `Parameter`, `ParameterVector`, `assign_parameters()`
4. **Circuit Library**: Standard gates and pre-built circuits (QFT, ansätze)
5. **Classical Control**: Conditional operations with `c_if()`
6. **Dynamic Circuits**: `if_test()`, `for_loop()`, `while_loop()`, `switch()`

---

## 🧠 Key Quantum Algorithms Overview

Before diving into circuit creation, it's essential to understand the key quantum algorithms that these circuits implement. These algorithms are frequently referenced throughout this section and the exam.

### VQE (Variational Quantum Eigensolver)

**Definition**: A hybrid quantum-classical algorithm for finding the ground state energy of a molecular or physical system. It's the most important near-term algorithm for quantum chemistry.

**How it works**:
1. Prepare a parameterized quantum state (ansatz)
2. Measure the expectation value of the Hamiltonian
3. Classical optimizer adjusts parameters to minimize energy
4. Repeat until convergence

**Circuit Diagram**:
```
     ┌───────────┐┌───────────┐     ┌─┐
q_0: ┤ RY(θ[0]) ├┤ RZ(θ[2]) ├──■──┤M├───
     ├───────────┤├───────────┤┌─┴─┐└╥┘┌─┐
q_1: ┤ RY(θ[1]) ├┤ RZ(θ[3]) ├┤ X ├─╫─┤M├
     └───────────┘└───────────┘└───┘ ║ └╥┘
c: 2/════════════════════════════════╩══╩═
                                     0  1
```
*Typical VQE ansatz: parameterized rotations followed by entangling gates*

**Use Case**: Finding molecular ground state energies (drug discovery, materials science)

---

### QAOA (Quantum Approximate Optimization Algorithm)

**Definition**: A variational algorithm designed to solve combinatorial optimization problems (MaxCut, traveling salesman, portfolio optimization).

**How it works**:
1. Encode problem as a cost Hamiltonian
2. Apply alternating cost (γ) and mixer (β) layers
3. Measure and evaluate cost function
4. Classical optimizer tunes γ and β parameters

**Circuit Diagram**:
```
     ┌───┐┌────────────┐┌────────────┐┌────────────┐┌────────────┐┌─┐
q_0: ┤ H ├┤ RZZ(γ[0]) ├┤ RX(β[0])  ├┤ RZZ(γ[1]) ├┤ RX(β[1])  ├┤M├
     ├───┤├────────────┤├────────────┤├────────────┤├────────────┤├─┤
q_1: ┤ H ├┤ RZZ(γ[0]) ├┤ RX(β[0])  ├┤ RZZ(γ[1]) ├┤ RX(β[1])  ├┤M├
     └───┘└────────────┘└────────────┘└────────────┘└────────────┘└─┘
           └── Layer 1 (p=1) ──┘      └── Layer 2 (p=2) ──┘
```
*QAOA with p=2 layers: cost layer (RZZ) alternates with mixer layer (RX)*

**Use Case**: Optimization problems (logistics, finance, scheduling)

---

### Grover's Algorithm

**Definition**: A quantum search algorithm that provides quadratic speedup for unstructured search problems. Finds a marked item in N items using O(√N) queries instead of O(N).

**How it works**:
1. Initialize uniform superposition (Hadamard on all qubits)
2. Apply Grover iteration √N times:
   - Oracle: marks the solution by flipping its phase
   - Diffusion operator: amplifies marked state amplitude
3. Measure to find solution with high probability

**Circuit Diagram**:
```
     ┌───┐┌─────────┐┌───────────────────┐   ┌─┐
q_0: ┤ H ├┤         ├┤                   ├───┤M├
     ├───┤┤         ├┤                   ├┌─┐└╥┘
q_1: ┤ H ├┤  Oracle ├┤     Diffusion     ├┤M├─╫─
     ├───┤┤         ├┤                   ├└╥┘ ║
q_2: ┤ H ├┤         ├┤                   ├─╫──╫─
     └───┘└─────────┘└───────────────────┘ ║  ║
           └────── Repeat √N times ──────┘
```
*Grover's algorithm: Initialize → (Oracle → Diffusion) × √N → Measure*

**Detailed Grover Iteration**:
```
     ┌───┐     ┌───┐┌───┐     ┌───┐┌───┐
q_0: ┤ Z ├──■──┤ H ├┤ X ├──■──┤ X ├┤ H ├
     └───┘┌─┴─┐├───┤├───┤┌─┴─┐├───┤├───┤
q_1: ─────┤ Z ├┤ H ├┤ X ├┤ Z ├┤ X ├┤ H ├
          └───┘└───┘└───┘└───┘└───┘└───┘
     └─ Oracle ─┘   └──── Diffusion ────┘
```

**Use Case**: Database search, SAT solving, cryptography

---

### QFT (Quantum Fourier Transform)

**Definition**: The quantum analog of the classical Discrete Fourier Transform (DFT). Transforms computational basis states to frequency basis with exponential speedup.

**How it works**:
1. Apply Hadamard to first qubit
2. Apply controlled phase rotations from all other qubits
3. Repeat for each qubit with decreasing rotation angles
4. Swap qubits to correct output ordering

**Circuit Diagram (3-qubit QFT)**:
```
     ┌───┐                                     
q_0: ┤ H ├─■────────■───────────────────────×─
     └───┘ │P(π/2)  │P(π/4) ┌───┐           │ 
q_1: ──────■────────│───────┤ H ├─■─────────┼─
                    │       └───┘ │P(π/2)   │ 
q_2: ───────────────■─────────────■──────┤H├×─
                                         └─┘  
```
*QFT circuit: Hadamards + controlled phase gates + swaps*

**Mathematical Formula**:
$$|j\rangle \xrightarrow{QFT} \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} e^{2\pi ijk/N}|k\rangle$$

**Use Case**: Shor's factoring algorithm, Quantum Phase Estimation, signal processing

---

### What is an Ansatz?

**Definition**: An *ansatz* (plural: *ansätze*) is a parameterized quantum circuit template used as a trial wavefunction in variational algorithms. The term comes from German meaning "initial placement" or "approach."

**Key Characteristics**:
- Contains tunable parameters (rotation angles)
- Structure is fixed, but parameter values are optimized
- Expressibility: ability to represent target states
- Hardware efficiency: should map well to physical qubits

**Common Ansätze in Qiskit**:
| Ansatz | Use Case | Parameters | Structure |
|--------|----------|------------|-----------|
| `RealAmplitudes` | VQE | Real rotations only | RY + CNOT layers |
| `EfficientSU2` | General VQE | Full SU(2) | RY + RZ + CNOT layers |
| `QAOAAnsatz` | QAOA | Cost + mixer | RZZ + RX layers |
| `TwoLocal` | Customizable | User-defined | Configurable rotation + entanglement |

---

## 🎯 Why This Section Matters (Conceptual Foundation)

### 🧠 Conceptual Deep Dive

#### Analogy: The Recipe

Building a `QuantumCircuit` is like writing a recipe:
- **Ingredients**: Qubits and Classical Bits
- **Instructions**: Gates (Hadamard, CNOT, Measure)
- **Cookware**: Registers (QuantumRegister, ClassicalRegister)
- **Cooking Time**: Circuit Depth (longest parallel step)
- **Kitchen Space**: Circuit Width (total wires needed)

#### Key Insight: Depth vs Size

- **Size**: Total number of operations (how much work you do)
- **Depth**: The longest path from input to output (how long it takes)
- *Example*: If 10 friends (qubits) chop 10 onions (gates) simultaneously, **size** = 10, but **depth** = 1

### Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    CIRCUIT CREATION DECISION TREE                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What do you want to create?                                     │
│                                                                  │
│  ├─ Simple circuit ─────────► QuantumCircuit(n, m)              │
│  │                                                               │
│  ├─ Named/organized ────────► Use QuantumRegister/ClassicalReg  │
│  │                                                               │
│  ├─ Combine sequential ─────► compose(qc2)                      │
│  │                                                               │
│  ├─ Combine parallel ───────► tensor(qc2)                       │
│  │                                                               │
│  ├─ Add single gate ────────► append(gate, qubits)              │
│  │                                                               │
│  ├─ Variable rotations ─────► Parameter('θ')                    │
│  │                                                               │
│  ├─ Pre-built algorithm ────► Circuit Library (QFT, etc.)       │
│  │                                                               │
│  └─ Conditional ops ────────► if_test() or c_if()               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Covered (Quick Reference)

| Topic | Description | Exam Weight | Priority |
|-------|-------------|-------------|----------|
| **QuantumCircuit** | Basic circuit creation | High | 🔴 |
| **depth(), size(), width()** | Circuit properties | High | 🔴 |
| **compose()** | Sequential combination | High | 🔴 |
| **tensor()** | Parallel combination | Medium | 🟡 |
| **Parameter** | Parameterized gates | High | 🔴 |
| **assign_parameters()** | Binding values | High | 🔴 |
| **Circuit Library** | QFT, RealAmplitudes | Medium | 🟡 |
| **c_if() / if_test()** | Classical control | Medium | 🟡 |
| **Dynamic circuits** | for_loop, while_loop | Low | 🟢 |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION 3 LEARNING PATH                       │
├─────────────────────────────────────────────────────────────────┤
│  START HERE                                                      │
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. CIRCUIT BASICS                                            ││
│  │    └─ QuantumCircuit creation                               ││
│  │    └─ Properties: depth, size, width, num_qubits            ││
│  │    └─ Registers for organization                            ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 2. CIRCUIT COMPOSITION                                       ││
│  │    └─ compose() for sequential                              ││
│  │    └─ tensor() for parallel                                 ││
│  │    └─ append() for single gates                             ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 3. PARAMETERIZED CIRCUITS                                    ││
│  │    └─ Parameter and ParameterVector                         ││
│  │    └─ assign_parameters() binding                           ││
│  │    └─ VQE/QAOA patterns                                     ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 4. CIRCUIT LIBRARY & CLASSICAL CONTROL                       ││
│  │    └─ Standard gates and circuits                           ││
│  │    └─ c_if() and if_test()                                  ││
│  │    └─ Dynamic circuit operators                             ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  COMPLETE: Ready for Circuit Creation exam questions             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Circuit Basics

> **STRUCTURE**: Foundation of all quantum programming
> **LEARNING FLOW**: Each sub-topic has 7 elements (learn → trap → mnemonic → test)

### Overview

Every quantum algorithm starts with creating a `QuantumCircuit`. Understanding circuit creation, properties, and organization with registers is fundamental to passing the certification.

---

### 🔹 QuantumCircuit Creation

#### 1. Definition

`QuantumCircuit` is the primary object representing a quantum computation. It contains quantum gates, measurements, and classical operations applied to qubits and classical bits.

#### 2. Analogy + Intuition

**Real-World Analogy**: A QuantumCircuit is like a musical score:
- Qubits are instrument lines (staffs)
- Gates are musical notes/instructions
- Time flows left to right
- The conductor (computer) follows the score exactly

**Intuition Builder**: Think of it as writing a recipe that the quantum computer will follow step-by-step.

#### 3. Math + Visual

**Circuit Structure**:
```
     ┌───────────────────────┐
q_0: ┤                       ├  Qubit 0
     │                       │
q_1: ┤  Quantum Operations   ├  Qubit 1
     │                       │
q_2: ┤                       ├  Qubit 2
     └───────────────────────┘
c: 3/═════════════════════════  Classical bits
```

#### 4. Implementation (Basic → Advanced)

**Qiskit Syntax**:
```python
from qiskit import QuantumCircuit
qc = QuantumCircuit(n_qubits, n_clbits)
```

**Basic Example - Simple Creation**:
```python
from qiskit import QuantumCircuit

# Just qubits (no classical bits)
qc = QuantumCircuit(2)

# Qubits + classical bits
qc = QuantumCircuit(2, 2)
```

**Intermediate Example - Using Registers**:
```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

qr = QuantumRegister(3, 'q')    # 3 qubits named 'q'
cr = ClassicalRegister(3, 'c')  # 3 classical bits named 'c'
qc = QuantumCircuit(qr, cr)
```

**Advanced Example - Multiple Registers**:
```python
# Logical organization for complex algorithms
data_qubits = QuantumRegister(4, 'data')
ancilla_qubits = QuantumRegister(2, 'ancilla')
measurements = ClassicalRegister(4, 'meas')
syndrome = ClassicalRegister(2, 'syndrome')

qc = QuantumCircuit(data_qubits, ancilla_qubits, measurements, syndrome)
```

#### 5. ⚠️ Trap Alert

> **LEARN THE TRAP NOW** - Don't let misconceptions form!

**Trap: Arguments Order Matters**
- ❌ **Wrong**: Thinking first arg is classical bits
- ✅ **Correct**: First arg is QUBITS, second is CLASSICAL bits
- 🔍 **Why it's tricky**: Some expect (classical, quantum) order

```python
# ❌ WRONG interpretation
qc = QuantumCircuit(2, 3)  # NOT 2 classical, 3 qubits!

# ✅ CORRECT
qc = QuantumCircuit(2, 3)  # 2 qubits, 3 classical bits
```

#### 6. 🧠 Mnemonic

**"Qubits Come Before Classical" (Q before C)**
- Meaning: In QuantumCircuit(q, c), qubits come first
- Example: `QuantumCircuit(3, 2)` = 3 qubits, 2 classical

#### 7. ⚡ Quick Check

**Q: What does `QuantumCircuit(4, 2)` create?**

<details>
<summary>Answer</summary>

**A**: A circuit with **4 qubits** and **2 classical bits**.

Remember: Q before C - Qubits first, Classical second.
</details>

---

### 🔹 Circuit Properties (EXAM CRITICAL!)

#### 1. Definition

Circuit properties are measurable characteristics that describe a circuit's structure without executing it:
- `depth()`: Critical path length (longest sequential chain)
- `size()`: Total count of all operations
- `width()`: Total number of wires (qubits + classical bits)
- `num_qubits`: Number of quantum bits (property, no parentheses)
- `num_clbits`: Number of classical bits (property, no parentheses)

#### 2. Analogy + Intuition

**Real-World Analogy**: 
- **Depth** = How long a project takes (critical path in project management)
- **Size** = Total work items in the project
- **Width** = How many people/resources needed

**Intuition Builder**: Parallel operations don't add depth! If 10 people do 10 tasks simultaneously, depth=1 but size=10.

#### 3. Math + Visual

**Visual Example**:
```
Circuit:
     ┌───┐          
q_0: ┤ H ├──■───────  Layer 1: H
     └───┘┌─┴─┐      Layer 2: CX(0,1)
q_1: ─────┤ X ├──■──  Layer 3: CX(1,2)
          └───┘┌─┴─┐  Layer 4: Measurement
q_2: ──────────┤ X ├  
               └───┘  

Depth = 4  (longest path)
Size = 6   (1 H + 2 CX + 3 Measure)
Width = 6  (3 qubits + 3 classical bits)
```

#### 4. Implementation

**Qiskit Syntax**:
```python
qc.depth()       # Method - with parentheses
qc.size()        # Method - with parentheses
qc.width()       # Method - with parentheses
qc.num_qubits    # Property - NO parentheses!
qc.num_clbits    # Property - NO parentheses!
qc.count_ops()   # Method - returns dict of gate counts
```

**Example**:
```python
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

print(f"Depth: {qc.depth()}")        # 4
print(f"Size: {qc.size()}")          # 6
print(f"Width: {qc.width()}")        # 6
print(f"Qubits: {qc.num_qubits}")    # 3
print(f"Clbits: {qc.num_clbits}")    # 3
print(f"Ops: {qc.count_ops()}")      # {'h': 1, 'cx': 2, 'measure': 3}
```

**Parallel Operations**:
```python
qc = QuantumCircuit(2)
qc.h(0)  # Layer 1
qc.h(1)  # Also Layer 1 (parallel!)

print(qc.depth())  # Output: 1 (not 2!)
```

#### 5. ⚠️ Trap Alert

**Trap: Method vs Property**
- ❌ **Wrong**: `qc.num_qubits()` with parentheses
- ✅ **Correct**: `qc.num_qubits` without parentheses
- 🔍 **Why it's tricky**: depth() is method, num_qubits is property

```python
# ❌ WRONG
qc.num_qubits()  # TypeError!

# ✅ CORRECT
qc.num_qubits    # Property (no parentheses)
qc.depth()       # Method (with parentheses)
```

**Trap: Measurements Count in Depth and Size**
- ❌ **Wrong**: Thinking measurements don't affect depth
- ✅ **Correct**: Measurements add to both depth AND size

```python
qc = QuantumCircuit(2, 2)
qc.h(0)           # Layer 1
qc.cx(0, 1)       # Layer 2
qc.measure_all()  # Layer 3 (adds to depth!)

print(qc.depth())  # 3 (H → CX → Measure)
print(qc.size())   # 4 (1 H + 1 CX + 2 Measures)
```

#### 6. 🧠 Mnemonic

**"Width = Wires, Depth = Delays, Size = Sum"**
- Width: Count all wires (quantum + classical)
- Depth: Longest path (layers/delays)
- Size: Sum of all gates

**"Methods have Mouths (parentheses), Properties are Plain"**
- `depth()` has parentheses (method)
- `num_qubits` is plain (property)

#### 7. ⚡ Quick Check

**Q: A circuit has H gates on qubits 0,1,2 (parallel), then a barrier, then measure_all(). What is the depth?**

<details>
<summary>Answer</summary>

**A**: **3** (Layer 1: H gates in parallel, Layer 2: barrier, Layer 3: measurements)

Parallel gates on different qubits share the same layer!
</details>

---

## 🔧 Circuit Composition

> **STRUCTURE**: Methods for combining circuits
> **CRITICAL**: compose() vs tensor() is frequently tested!

### Overview

Circuit composition allows you to build complex algorithms from simpler components. The three main methods serve different purposes: `compose()` for sequential, `tensor()` for parallel, and `append()` for single gates.

---

### 🔹 compose() - Sequential Combination

#### 1. Definition

`compose()` appends one circuit's operations after another circuit's operations on the same (or mapped) qubits. The circuits execute sequentially.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like chaining recipes - first make the sauce, then add it to the pasta. Same ingredients (qubits), sequential steps.

**Intuition Builder**: Think "→" arrow - circuit 1 flows INTO circuit 2.

#### 3. Math + Visual

**Visual**:
```
qc1:           qc2:           compose(qc1, qc2):
     ┌───┐         ┌───┐            ┌───┐     ┌───┐
q_0: ┤ H ├──■──    ┤ X ├       q_0: ┤ H ├──■──┤ X ├
     └───┘┌─┴─┐    └───┘            └───┘┌─┴─┐└───┘
q_1: ─────┤ X ├    ──Z──       q_1: ─────┤ X ├──Z──
          └───┘                          └───┘     
```

#### 4. Implementation

**Qiskit Syntax**:
```python
result = qc1.compose(qc2)  # Returns new circuit
```

**Parameters**:
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `other` | QuantumCircuit | Circuit to append | Required |
| `qubits` | list | Target qubits in qc1 | None (same) |
| `clbits` | list | Target classical bits | None |
| `front` | bool | Add to front instead | False |
| `inplace` | bool | Modify qc1 directly | False |

**Basic Example**:
```python
prep = QuantumCircuit(2)
prep.h(0)
prep.cx(0, 1)

algo = QuantumCircuit(2)
algo.x(0)
algo.z(1)

full = prep.compose(algo)  # prep then algo
```

**With Qubit Mapping**:
```python
qc1 = QuantumCircuit(3)
qc2 = QuantumCircuit(2)
qc2.cx(0, 1)

# Apply qc2 to qubits 1,2 of qc1
result = qc1.compose(qc2, qubits=[1, 2])
```

**Front Composition**:
```python
# Add at the beginning instead of end
result = qc1.compose(qc2, front=True)
```

#### 5. ⚠️ Trap Alert

**Trap: Width Unchanged**
- ❌ **Wrong**: Expecting compose to add qubits
- ✅ **Correct**: compose uses SAME qubits (width unchanged)

```python
qc1 = QuantumCircuit(2)
qc2 = QuantumCircuit(2)

result = qc1.compose(qc2)
print(result.num_qubits)  # 2 (not 4!)
```

**Trap: Default is NOT inplace**
- ❌ **Wrong**: `qc1.compose(qc2)` modifies qc1
- ✅ **Correct**: Returns NEW circuit; use `inplace=True` to modify

```python
# ❌ This doesn't modify qc1!
qc1.compose(qc2)

# ✅ Either capture return value or use inplace
result = qc1.compose(qc2)
# OR
qc1.compose(qc2, inplace=True)
```

#### 6. 🧠 Mnemonic

**"Compose = Continue"**
- Meaning: Continue the same circuit with more operations
- Same qubits, sequential execution

#### 7. ⚡ Quick Check

**Q: After `qc1.compose(qc2)` where both have 3 qubits, how many qubits in result?**

<details>
<summary>Answer</summary>

**A**: **3 qubits**

compose() is sequential on the SAME qubits - it doesn't add new ones.
</details>

---

### 🔹 tensor() - Parallel Combination

#### 1. Definition

`tensor()` combines two circuits side-by-side as independent systems. Creates a tensor product of the two circuits, adding new qubits.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like having two separate cooking stations working independently - different ingredients, same kitchen, parallel execution.

**Intuition Builder**: Think "⊗" symbol - two separate systems combined.

#### 3. Math + Visual

**Visual**:
```
qc1:         qc2:         tensor(qc1, qc2):
     ┌───┐       ┌───┐         ┌───┐          
q_0: ┤ H ├──■──  ┤ X ├    q_0: ┤ H ├──■───────
     └───┘┌─┴─┐  └───┘         └───┘┌─┴─┐     
q_1: ─────┤ X ├  ──X──    q_1: ─────┤ X ├─────
          └───┘                     └───┘     
                              q_2: ┤ X ├───────
                                   └───┘          
                              q_3: ──X─────────

Width: 2 ⊗ 2 = 4 qubits
```

#### 4. Implementation

**Qiskit Syntax**:
```python
result = qc1.tensor(qc2)  # Returns new circuit with combined qubits
```

**Example**:
```python
system1 = QuantumCircuit(2)
system1.h(0)
system1.cx(0, 1)

system2 = QuantumCircuit(2)
system2.x([0, 1])

combined = system1.tensor(system2)
print(combined.num_qubits)  # 4
```

#### 5. ⚠️ Trap Alert

**Trap: tensor() ADDS Qubits**
- ❌ **Wrong**: Confusing tensor with compose
- ✅ **Correct**: tensor creates NEW qubits for the second circuit

```python
qc1 = QuantumCircuit(2)  # 2 qubits
qc2 = QuantumCircuit(3)  # 3 qubits

result = qc1.tensor(qc2)
print(result.num_qubits)  # 5 (2 + 3)
```

#### 6. 🧠 Mnemonic

**"Tensor = Together but separate"**
- Meaning: Two independent systems combined
- New qubits added, parallel systems

#### 7. ⚡ Quick Check

**Q: qc1 has 2 qubits, qc2 has 3 qubits. What is `qc1.tensor(qc2).num_qubits`?**

<details>
<summary>Answer</summary>

**A**: **5 qubits**

tensor() creates a tensor product: 2 + 3 = 5 qubits total.
</details>

---

### 🔹 append() - Add Single Operation

#### 1. Definition

`append()` adds a single gate or instruction to the end of a circuit on specified qubits.

#### 2. Implementation

```python
from qiskit.circuit.library import HGate, CXGate, QFT

qc = QuantumCircuit(4)

# Append single gate
qc.append(HGate(), [0])

# Append multi-qubit gate
qc.append(CXGate(), [0, 1])

# Append circuit as single operation
qc.append(QFT(3), [0, 1, 2])
```

#### 3. ⚠️ Trap Alert

**Trap: append needs list for qubits**
```python
# ❌ WRONG
qc.append(HGate(), 0)  # Error! Needs list

# ✅ CORRECT
qc.append(HGate(), [0])  # List of qubits
```

---

## 📊 Circuit Composition - Consolidated Review

### Comparison Table

| Feature | `compose()` | `tensor()` | `append()` |
|---------|------------|-----------|-----------|
| **Purpose** | Sequential combination | Parallel combination | Add single operation |
| **Qubits** | Same (or mapped) | Independent sets | Specified qubits |
| **Width Change** | No | Yes (adds) | No |
| **Structure** | qc1 → qc2 | qc1 ⊗ qc2 | qc + gate |
| **Returns** | New circuit | New circuit | None (modifies) |

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ CIRCUIT COMPOSITION - QUICK REFERENCE                           │
├─────────────────────────────────────────────────────────────────┤
│ compose(qc2)           - Append qc2 after (sequential →)        │
│ compose(qc2, front=True) - Prepend qc2 before                   │
│ compose(qc2, qubits=[1,2]) - Map to specific qubits             │
│ tensor(qc2)            - Combine side-by-side (parallel ⊗)      │
│ append(gate, [qubits]) - Add single operation                   │
├─────────────────────────────────────────────────────────────────┤
│ DECISION GUIDE:                                                 │
│ • Same qubits, sequential? → compose()                          │
│ • Different qubits, parallel? → tensor()                        │
│ • Adding one gate? → append()                                   │
├─────────────────────────────────────────────────────────────────┤
│ WIDTH CHANGE:                                                   │
│ • compose: NO (uses same qubits)                                │
│ • tensor: YES (adds qubits)                                     │
│ • append: NO (uses existing qubits)                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Parameterized Circuits

> **STRUCTURE**: Essential for VQE, QAOA, and quantum machine learning
> **CRITICAL**: Parameter binding is frequently tested!

### Overview

Parameterized circuits contain symbolic parameters instead of fixed values. This enables variational algorithms where a classical optimizer tunes the quantum circuit parameters.

---

### 🔹 Parameter Class

#### 1. Definition

`Parameter` is a symbolic variable representing an unbound angle or value. It acts as a placeholder until bound to a concrete numerical value.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like a variable in algebra - θ represents "some angle" until you substitute a specific value.

**Intuition Builder**: Parameters make your circuit a "template" that can be instantiated with different values without rebuilding.

#### 3. Math + Visual

**Visual**:
```
Parameterized:              Bound (θ=π/4):
     ┌────────┐                  ┌──────────┐
q_0: ┤ Ry(θ)  ├             q_0: ┤ Ry(π/4)  ├
     └────────┘                  └──────────┘
```

#### 4. Implementation

**Qiskit Syntax**:
```python
from qiskit.circuit import Parameter

theta = Parameter('θ')
qc.ry(theta, 0)
```

**Basic Example**:
```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

theta = Parameter('θ')
phi = Parameter('φ')

qc = QuantumCircuit(1)
qc.ry(theta, 0)
qc.rz(phi, 0)

print(qc.parameters)  # {Parameter(θ), Parameter(φ)}
```

**ParameterVector for Multiple Parameters**:
```python
from qiskit.circuit import ParameterVector

params = ParameterVector('θ', 4)  # Creates θ[0], θ[1], θ[2], θ[3]

qc = QuantumCircuit(4)
for i in range(4):
    qc.ry(params[i], i)
```

#### 5. ⚠️ Trap Alert

**Trap: Parameters Must Be Unique**
- ❌ **Wrong**: Creating two Parameters with same name
- ✅ **Correct**: Each Parameter object is unique by identity

```python
# ❌ WRONG - Creates two different parameters!
theta1 = Parameter('θ')
theta2 = Parameter('θ')  # Different object!

# ✅ CORRECT - Reuse same parameter
theta = Parameter('θ')
qc.ry(theta, 0)
qc.rz(theta, 1)  # Same theta used twice
```

#### 6. 🧠 Mnemonic

**"Parameters are Placeholders"**
- Meaning: Like 'x' in math - holds a spot for a real value
- Won't execute until bound

#### 7. ⚡ Quick Check

**Q: What does `qc.parameters` return for a circuit with unbound Parameters?**

<details>
<summary>Answer</summary>

**A**: A set of all unbound Parameter objects in the circuit.

```python
qc.parameters  # {Parameter(θ), Parameter(φ)}
```
</details>

---

### 🔹 assign_parameters() - Binding Values

#### 1. Definition

`assign_parameters()` replaces symbolic parameters with numerical values, creating an executable circuit.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like "find and replace" - substitute all θ's with 0.5.

#### 3. Implementation

**Qiskit Syntax**:
```python
bound_circuit = qc.assign_parameters({theta: value})
```

**Single Value**:
```python
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.ry(theta, 0)

# Bind to π/4
bound = qc.assign_parameters({theta: np.pi/4})
print(bound.parameters)  # set() - empty, all bound!
```

**Multiple Values**:
```python
params = ParameterVector('θ', 3)
qc = QuantumCircuit(3)
for i in range(3):
    qc.ry(params[i], i)

# Bind all at once
values = [0.1, 0.2, 0.3]
bound = qc.assign_parameters({params: values})
```

**Partial Binding**:
```python
theta = Parameter('θ')
phi = Parameter('φ')

qc = QuantumCircuit(1)
qc.ry(theta, 0)
qc.rz(phi, 0)

# Bind only theta
partial = qc.assign_parameters({theta: 0.5})
print(partial.parameters)  # {Parameter(φ)} - phi still unbound
```

#### 4. ⚠️ Trap Alert

**Trap: bind_parameters vs assign_parameters**
- ❌ **Wrong**: Using `bind_parameters()` (deprecated)
- ✅ **Correct**: Use `assign_parameters()` (modern API)

```python
# ⚠️ OLD (deprecated but may appear in exam)
bound = qc.bind_parameters({theta: 0.5})

# ✅ MODERN
bound = qc.assign_parameters({theta: 0.5})
```

**Trap: Must Bind Before Execution**
- ❌ **Wrong**: Running circuit with unbound parameters
- ✅ **Correct**: Bind all parameters before sending to backend

```python
# ❌ ERROR - can't execute unbound circuit
# sampler.run([qc])  # Has unbound θ!

# ✅ CORRECT
bound_qc = qc.assign_parameters({theta: 0.5})
sampler.run([bound_qc])
```

#### 5. 🧠 Mnemonic

**"Assign = Attach values"**
- Meaning: Attach concrete numbers to parameter symbols
- Creates runnable circuit

#### 6. ⚡ Quick Check

**Q: What is `len(qc.parameters)` after binding ALL parameters?**

<details>
<summary>Answer</summary>

**A**: **0** (empty set)

When all parameters are bound, `qc.parameters` returns an empty set.
</details>

---

### 🔹 ParameterExpression (Advanced)

#### 1. Definition

`ParameterExpression` allows mathematical operations on parameters, creating expressions like `2*θ` or `θ + φ`.

#### 2. Theoretical Background

**What is a ParameterExpression?**

A `ParameterExpression` represents a **symbolic mathematical expression** involving one or more `Parameter` objects. Unlike a simple `Parameter` (which is just a symbolic placeholder), a `ParameterExpression` can represent complex mathematical relationships like `2*θ + sin(φ)` or `θ²/π`.

**Why This Matters for Quantum Computing:**

1. **Variational Algorithms (VQE, QAOA)**: Optimization algorithms often require computing **gradients** of parameterized quantum circuits. ParameterExpression enables automatic differentiation through symbolic manipulation.

2. **Parameter Shifts**: The parameter-shift rule for computing quantum gradients requires evaluating circuits at shifted parameter values. `subs()` enables this efficiently.

3. **Hardware Calibration**: Real quantum hardware may require transformations of logical parameters to physical pulse parameters.

4. **Circuit Optimization**: Transpilers can simplify expressions like `θ - θ` to `0` before circuit execution.

**Mathematical Foundation:**

ParameterExpression implements a **symbolic algebra system** where:
- Operations like `+`, `-`, `*`, `/`, `**` create new expressions
- Functions like `sin()`, `cos()`, `exp()` extend the expression tree
- The `gradient()` method computes **symbolic derivatives** using calculus rules:
  - Product rule: $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$
  - Chain rule: $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

#### 3. ParameterExpression Methods

| Method | Description | Example |
|--------|-------------|---------|
| `gradient(param)` | Compute symbolic derivative with respect to param | `expr.gradient(theta)` |
| `subs(param_dict)` | Substitute parameters with new values or expressions | `expr.subs({theta: phi})` |
| `bind(param_dict)` | Bind parameters to numerical values (returns `ParameterExpression`) | `expr.bind({theta: 0.5})` |
| `is_real()` | Check if expression is real-valued | `expr.is_real()` |
| `numeric()` | Convert fully-bound expression to number | `bound_expr.numeric()` |
| `sympify()` | Convert to SymPy expression for advanced manipulation | `expr.sympify()` |
| `parameters` | Set of unbound Parameter objects in expression | `expr.parameters` |

#### 4. Mathematical Functions on Parameters

```python
from qiskit.circuit import Parameter
import numpy as np

theta = Parameter('θ')
phi = Parameter('φ')

# Arithmetic operations (return ParameterExpression)
expr1 = 2 * theta              # Scalar multiplication
expr2 = theta + phi            # Addition
expr3 = theta - phi            # Subtraction
expr4 = theta * phi            # Multiplication
expr5 = theta / 2              # Division
expr6 = theta ** 2             # Exponentiation

# Mathematical functions (from qiskit.circuit)
sin_expr = theta.sin()         # sin(θ)
cos_expr = theta.cos()         # cos(θ)
tan_expr = theta.tan()         # tan(θ)
exp_expr = theta.exp()         # e^θ
log_expr = theta.log()         # ln(θ)
abs_expr = abs(theta)          # |θ|

# Complex expressions for ansätze
rotation_angle = np.pi * theta / 4 + phi.sin()
```

#### 5. Implementation

```python
from qiskit.circuit import Parameter
import numpy as np

theta = Parameter('θ')

qc = QuantumCircuit(2)
qc.rx(theta, 0)           # θ
qc.rx(2 * theta, 1)       # 2θ
qc.rx(theta + np.pi/4, 0) # θ + π/4

# All can be bound with one value
bound = qc.assign_parameters({theta: 0.5})
```

#### 6. Gradient Computation (Essential for VQE!)

**Theoretical Foundation - Parameter Shift Rule:**

For parameterized quantum gates $U(\theta)$, the gradient of expectation values can be computed using the **parameter-shift rule**:

$$\frac{\partial}{\partial\theta}\langle\psi|U^\dagger(\theta) O U(\theta)|\psi\rangle = \frac{1}{2}\left[\langle O \rangle_{\theta+\frac{\pi}{2}} - \langle O \rangle_{\theta-\frac{\pi}{2}}\right]$$

This requires evaluating circuits at shifted parameter values, which `subs()` enables.

```python
from qiskit.circuit import Parameter

# Define parameter and expression
theta = Parameter('θ')
expr = theta ** 2 + 2 * theta  # f(θ) = θ² + 2θ

# Compute gradient symbolically: d/dθ = 2θ + 2
gradient = expr.gradient(theta)
print(f"Expression: {expr}")           # θ² + 2*θ
print(f"Gradient: {gradient}")          # 2*θ + 2

# For parameter shift rule implementation
import numpy as np
shift = np.pi / 2
shifted_plus = expr.subs({theta: theta + shift})   # (θ + π/2)² + 2(θ + π/2)
shifted_minus = expr.subs({theta: theta - shift})  # (θ - π/2)² + 2(θ - π/2)
```

#### 7. Parameter Substitution with subs()

```python
from qiskit.circuit import Parameter

theta = Parameter('θ')
phi = Parameter('φ')

# Original expression
expr = 2 * theta + theta.sin()

# Substitute theta with phi (returns new ParameterExpression)
new_expr = expr.subs({theta: phi})
print(f"After substitution: {new_expr}")  # 2*φ + sin(φ)

# Substitute with numeric value
numeric_expr = expr.subs({theta: 0.5})
print(f"Numerical: {numeric_expr.numeric()}")  # 1.479...

# Substitute with another expression
complex_sub = expr.subs({theta: 2 * phi})
print(f"Complex substitution: {complex_sub}")  # 4*φ + sin(2*φ)
```

#### 8. ⚠️ Trap Alert - ParameterExpression

```python
from qiskit.circuit import Parameter

theta = Parameter('θ')

# TRAP 1: subs() vs assign_parameters() vs bind()
expr = 2 * theta
# subs() - substitutes in expression (returns ParameterExpression)
new_expr = expr.subs({theta: 0.5})  # Returns ParameterExpression

# assign_parameters() - use on QuantumCircuit
# bind() - use on ParameterExpression (same as subs with numeric)

# TRAP 2: Checking if fully bound
expr = theta + 1
print(len(expr.parameters))  # 1 (has unbound theta)
bound = expr.bind({theta: 0.5})
print(len(bound.parameters))  # 0 (fully bound)

# TRAP 3: Getting numeric value
# WRONG: numeric() on unbound expression
# ❌ expr.numeric()  # Error!

# CORRECT: First bind, then numeric
bound_expr = expr.bind({theta: 0.5})
value = bound_expr.numeric()  # Returns 1.5

# TRAP 4: gradient() returns expression, not number
grad = expr.gradient(theta)  # Returns ParameterExpression (value: 1)
grad_value = grad.numeric()  # Now get the number
```

---

## 📊 Parameterized Circuits - Consolidated Review

### VQE Pattern (EXAM CRITICAL!)

```python
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
import numpy as np

def create_vqe_ansatz(n_qubits, depth):
    """Hardware-efficient VQE ansatz"""
    qc = QuantumCircuit(n_qubits)
    params = ParameterVector('θ', n_qubits * depth * 2)
    idx = 0
    
    for d in range(depth):
        # Rotation layer
        for i in range(n_qubits):
            qc.ry(params[idx], i)
            idx += 1
        for i in range(n_qubits):
            qc.rz(params[idx], i)
            idx += 1
        # Entangling layer
        for i in range(n_qubits-1):
            qc.cx(i, i+1)
    
    return qc

# Usage
ansatz = create_vqe_ansatz(3, 2)
print(f"Parameters: {len(ansatz.parameters)}")  # 12
```

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ PARAMETERIZED CIRCUITS - QUICK REFERENCE                        │
├─────────────────────────────────────────────────────────────────┤
│ CREATION:                                                       │
│ theta = Parameter('θ')                                          │
│ params = ParameterVector('θ', n)  # Creates θ[0]...θ[n-1]       │
├─────────────────────────────────────────────────────────────────┤
│ BINDING:                                                        │
│ bound = qc.assign_parameters({theta: 0.5})                      │
│ bound = qc.assign_parameters({params: [0.1, 0.2, 0.3]})         │
├─────────────────────────────────────────────────────────────────┤
│ CHECKING:                                                       │
│ qc.parameters          # Set of unbound parameters              │
│ len(qc.parameters)     # Number of unbound parameters           │
├─────────────────────────────────────────────────────────────────┤
│ EXAM TRAPS:                                                     │
│ • Use assign_parameters() not bind_parameters()                 │
│ • Must bind ALL parameters before execution                     │
│ • Same Parameter object = same parameter (not same name)        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Circuit Library

> **STRUCTURE**: Pre-built circuits and gates for common operations

### Overview

Qiskit's circuit library provides tested, optimized implementations of common gates and algorithms. Using library components saves time and reduces errors.

---

### 🔹 Standard Gates

#### 1. Definition

The circuit library contains all standard quantum gates as classes that can be instantiated and appended to circuits.

#### 2. Implementation

```python
from qiskit.circuit.library import (
    XGate, YGate, ZGate, HGate,
    CXGate, CZGate, CCXGate,  # Toffoli
    RXGate, RYGate, RZGate,
    SwapGate
)

qc = QuantumCircuit(3)
qc.append(HGate(), [0])
qc.append(CXGate(), [0, 1])
qc.append(CCXGate(), [0, 1, 2])  # Toffoli
```

---

### 🔹 Standard Circuits

| Circuit | Purpose | Parameters |
|---------|---------|------------|
| `QFT(n)` | Quantum Fourier Transform | n qubits |
| `RealAmplitudes(n, reps)` | VQE ansatz (RY + CNOT) | n qubits, reps layers |
| `EfficientSU2(n, reps)` | Hardware-efficient ansatz | n qubits, reps layers |
| `TwoLocal(n, rotation, entanglement)` | Custom ansatz | Flexible structure |

**Example - QFT**:
```python
from qiskit.circuit.library import QFT

# QFT on 4 qubits
qft = QFT(4)
print(qft.draw())

# Inverse QFT
iqft = QFT(4, inverse=True)
```

**Example - VQE Ansätze**:
```python
from qiskit.circuit.library import RealAmplitudes, EfficientSU2

# VQE ansatz
ansatz = RealAmplitudes(num_qubits=4, reps=2)
print(f"Parameters: {ansatz.num_parameters}")

# Hardware-efficient
hea = EfficientSU2(num_qubits=4, reps=2)
```

---

### 🔹 Boolean Oracle Construction

```python
from qiskit.circuit.library import PhaseOracle
from qiskit.circuit import QuantumCircuit

# From truth table string
# '1' marks solutions, '0' marks non-solutions
oracle = PhaseOracle('0011')  # |10⟩ and |11⟩ are solutions

# From DIMACS CNF file
# oracle = PhaseOracle.from_dimacs_file('formula.cnf')
```

---

## 🔧 Classical Control

> **STRUCTURE**: Conditional operations based on measurement results

### Overview

Classical control enables quantum circuits to make decisions based on mid-circuit measurement results. This is essential for quantum error correction, teleportation, and adaptive algorithms.

---

### 🔹 c_if() - Legacy Conditional

#### 1. Definition

`c_if()` makes a gate conditional on a classical bit or register value. The gate only executes if the condition is met.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like an "if" statement in programming - do X only if condition Y is true.

#### 3. Implementation

```python
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure(0, 0)

# Apply X to qubit 1 IF classical bit 0 equals 1
qc.x(1).c_if(0, 1)

qc.measure(1, 1)
```

**With Register**:
```python
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

# cr value is interpreted as integer
# cr == 3 means binary '11' (both bits = 1)
qc.z(2).c_if(cr, 3)
```

#### 4. ⚠️ Trap Alert

**Trap: c_if applies to GATE, not qubit**
```python
# ❌ WRONG ORDER
# qc.c_if(0, 1).x(1)  # Error!

# ✅ CORRECT
qc.x(1).c_if(0, 1)  # Gate first, then condition
```

**Trap: Register Value is Integer**
```python
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

# cr == 3 means binary '11' (both bits = 1)
# NOT individual bit values!
qc.z(2).c_if(cr, 3)
```

#### 5. 🧠 Mnemonic

**"Gate.c_if" - Gate first, Condition second**

---

### 🔹 if_test() - Modern Conditional (Qiskit 1.0+)

#### 1. Definition

`if_test()` is the modern context manager for conditional execution, supporting if-else blocks and multiple gates.

#### 2. Implementation

**Basic If**:
```python
qc = QuantumCircuit(2, 1)
qc.h(0)
qc.measure(0, 0)

with qc.if_test((qc.clbits[0], 1)):  # If c[0] == 1
    qc.x(1)
```

**If-Else**:
```python
with qc.if_test((qc.clbits[0], 1)) as else_:
    qc.x(1)      # If c[0] == 1
with else_:
    qc.z(1)      # Else (c[0] == 0)
```

**Multi-Bit Conditioning**:
```python
from qiskit import QuantumCircuit, ClassicalRegister

cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

qc.h([0, 1])
qc.measure([0, 1], [0, 1])

# Condition on entire register value
with qc.if_test((cr, 3)):  # cr == 3 means '11' in binary
    qc.x(2)
```

#### 3. Classical Expressions with expr Module

```python
from qiskit import QuantumCircuit, ClassicalRegister
from qiskit.circuit.classical import expr

cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

qc.h([0, 1])
qc.measure([0, 1], [0, 1])

# AND condition: c[0] AND c[1]
condition = expr.logic_and(cr[0], cr[1])
with qc.if_test(condition):
    qc.x(2)

# OR condition: c[0] OR c[1]
condition_or = expr.logic_or(cr[0], cr[1])

# Comparison: cr >= 2
condition_gte = expr.greater_equal(cr, 2)
```

#### 4. c_if vs if_test Comparison

| Feature | c_if() (Legacy) | if_test() (Modern) |
|---------|-----------------|---------------------|
| Syntax | `gate.c_if(bit, val)` | `with qc.if_test((bit, val)):` |
| Else clause | ❌ Not supported | ✅ `as else_:` |
| Multiple gates | One gate per call | Block of gates |
| Complex conditions | ❌ Limited | ✅ `expr` module |
| Nesting | ⚠️ Awkward | ✅ Clean nesting |
| Deprecation | ⚠️ Deprecated | ✅ Recommended |

#### 5. ⚠️ Trap Alert

**Trap: Tuple Syntax Required**
```python
# ❌ WRONG
# with qc.if_test(qc.clbits[0], 1):  # Missing tuple!

# ✅ CORRECT
with qc.if_test((qc.clbits[0], 1)):  # Tuple: (bit, value)
    qc.x(1)
```

**Trap: Measurements must happen BEFORE c_if/if_test**
```python
qc.h(0)
qc.measure(0, 0)  # Must measure first!
qc.x(1).c_if(0, 1)  # Then conditional
```

---

## 🔧 Dynamic Circuits

> **STRUCTURE**: Advanced control flow for quantum algorithms

### Overview

Dynamic circuits enable runtime control flow including loops and multi-way branching. These are supported on IBM Quantum hardware.

---

### 🔹 Dynamic Circuit Operators

| Operator | Use Case | Syntax |
|----------|----------|--------|
| `if_test()` | Binary decision | `with qc.if_test((clbit, value)):` |
| `for_loop()` | Fixed iterations | `with qc.for_loop(range(n)):` |
| `while_loop()` | Condition-based | `with qc.while_loop((clbit, value)):` |
| `switch()` | Multi-way branch | `with qc.switch(creg) as case:` |

### for_loop Example

```python
qc = QuantumCircuit(1, 1)

with qc.for_loop(range(3)):
    qc.h(0)  # Apply H three times
```

### while_loop Example

```python
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

with qc.while_loop((qc.clbits[0], 1)):  # While c[0] == 1
    qc.x(0)
    qc.measure(0, 0)
```

### switch Example

```python
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

with qc.switch(cr) as case:
    with case(0):
        qc.x(0)
    with case(1):
        qc.x(1)
    with case(2):
        qc.x(2)
    with case(case.DEFAULT):
        qc.id(0)  # No operation
```

---

## 🔧 Transpiler (Reference)

> **STRUCTURE**: Converting circuits for hardware execution

### Overview

The transpiler converts abstract circuits to hardware-executable form. Understanding the 6-stage pipeline helps optimize circuits for real quantum computers.

### Theoretical Background

**Why Do We Need Transpilation?**

Real quantum hardware has significant **constraints**:

1. **Limited Connectivity**: Qubits aren't all connected to each other. A typical 5-qubit chip might have connectivity like `0-1-2-3-4` (linear), meaning qubit 0 can only directly interact with qubit 1.

2. **Basis Gates**: Hardware only implements a small set of gates natively (e.g., `{CX, ID, RZ, SX, X}` for IBM hardware). All other gates must be decomposed.

3. **Gate Errors**: Each gate has error rates; minimizing gate count reduces total error

4. **Decoherence**: Operations must complete before qubits lose quantum information

**The Transpiler's Job:**

The transpiler solves a **constrained optimization problem**: find the equivalent circuit that:
- Uses only available gates (basis gates)
- Respects qubit connectivity (coupling map)
- Minimizes circuit depth and gate count
- Optionally includes timing information (scheduling)

**Mathematical Foundation:**

Any quantum operation can be decomposed into a universal gate set. The **Solovay-Kitaev theorem** guarantees that any single-qubit gate can be approximated to precision $\epsilon$ using $O(\log^c(1/\epsilon))$ gates from a finite universal set.

### The 6 Transpiler Stages

The Qiskit transpiler processes circuits through **6 sequential stages**:

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────┐   ┌──────────────┐   ┌────────────┐
│   INIT   │ → │  LAYOUT  │ → │ ROUTING  │ → │ TRANSLATION │ → │ OPTIMIZATION │ → │ SCHEDULING │
└──────────┘   └──────────┘   └──────────┘   └─────────────┘   └──────────────┘   └────────────┘
     │              │              │               │                  │                  │
     ▼              ▼              ▼               ▼                  ▼                  ▼
 Decompose     Map logical    Insert SWAP     Convert to       Reduce gate        Add timing
 multi-qubit   to physical    gates for       basis gates      count and          and delay
 gates         qubits         connectivity                     depth              instructions
```

| Stage | Purpose | Key Operations |
|-------|---------|----------------|
| **1. Init** | Prepare circuit for mapping | Unroll 3+ qubit gates, high-level synthesis |
| **2. Layout** | Map logical qubits → physical qubits | Analyze connectivity, assign positions |
| **3. Routing** | Ensure 2-qubit gates respect connectivity | Insert SWAP gates where needed |
| **4. Translation** | Convert to hardware basis gates | Replace gates with native equivalents |
| **5. Optimization** | Minimize circuit depth/gates | Merge gates, cancel redundancies |
| **6. Scheduling** | Add timing information | Compute delays, align operations |

### Stage Details

#### Stage 1: Init
```python
# Init stage decomposes gates that can't be directly mapped
# Example: 3-qubit gates → 2-qubit gates
from qiskit.transpiler.passes import Unroll3qOrMore, HighLevelSynthesis

# A CCX (Toffoli) gate decomposes to ~6 CNOT gates
```

#### Stage 2: Layout (Physical Qubit Assignment)

**Layout Problem:**
Given logical qubits `q0, q1, q2` and physical qubits `0, 1, 2, 3, 4` with limited connectivity, find the best mapping.

| Layout Method | Strategy | Best For |
|---------------|----------|----------|
| **TrivialLayout** | q[i] → physical[i] | Testing, simple circuits |
| **VF2Layout** | Graph isomorphism search | Finding perfect layouts when possible |
| **DenseLayout** | Pack qubits in high-connectivity region | Circuits with many 2-qubit gates |
| **SabreLayout** | Heuristic forward-backward passes | General use, large circuits |

```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Different layout methods
pm_trivial = generate_preset_pass_manager(
    optimization_level=1,
    backend=backend,
    layout_method='trivial'  # Direct mapping
)

pm_vf2 = generate_preset_pass_manager(
    optimization_level=1,
    backend=backend,
    layout_method='vf2'  # Graph isomorphism
)

pm_sabre = generate_preset_pass_manager(
    optimization_level=1,
    backend=backend,
    layout_method='sabre'  # Heuristic (default for level 1+)
)
```

#### Stage 3: Routing (SWAP Insertion)

**The Routing Problem:**

When two qubits need to interact but aren't physically connected, we must route them closer using SWAP gates.

**Critical Fact:** A SWAP gate decomposes to **3 CNOT gates**!

```
SWAP =  ──■──     ──■──     ──■──
         │         │         │
       ──X──  =  ──X──     ──X──     ──■──
                          ──■──     ──X──
                           │
                          ──X──
```

```python
from qiskit.transpiler.passes import SabreSwap, StochasticSwap

# Routing strategies
pm_sabre_swap = generate_preset_pass_manager(
    optimization_level=2,
    backend=backend,
    routing_method='sabre'  # Heuristic, good quality
)

pm_stochastic = generate_preset_pass_manager(
    optimization_level=2,
    backend=backend,
    routing_method='stochastic'  # Random search
)
```

#### Stage 4: Translation (Basis Gate Conversion)

```python
# IBM basis gates: {CX, ID, RZ, SX, X}
# All gates must be translated to this set

# Example: H gate → RZ(-π/2) · SX · RZ(-π/2)
#          T gate → RZ(π/4)
#          S gate → RZ(π/2)
```

#### Stage 5: Optimization

| Optimization Level | Description | Use Case |
|-------------------|-------------|----------|
| **0** | No optimization | Debugging, exact circuit preservation |
| **1** | Light optimization | Quick compilation, 1q gate merging |
| **2** | Medium optimization | Production use, commutative cancellation |
| **3** | Heavy optimization | Final deployment, unitary synthesis |

```python
# Optimization level comparison
pm_0 = generate_preset_pass_manager(optimization_level=0, backend=backend)
pm_1 = generate_preset_pass_manager(optimization_level=1, backend=backend)
pm_2 = generate_preset_pass_manager(optimization_level=2, backend=backend)
pm_3 = generate_preset_pass_manager(optimization_level=3, backend=backend)

# Level 3 techniques:
# - UnitarySynthesis: Optimal gate decomposition
# - ConsolidateBlocks: Merge gate sequences
# - CommutativeCancellation: Use commutation rules
# - CXCancellation: Remove adjacent CNOTs
```

#### Stage 6: Scheduling

```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# ASAP = As Soon As Possible (minimize idle time at start)
# ALAP = As Late As Possible (minimize idle time at end)

pm_asap = generate_preset_pass_manager(
    optimization_level=2,
    backend=backend,
    scheduling_method='asap'
)

pm_alap = generate_preset_pass_manager(
    optimization_level=2,
    backend=backend,
    scheduling_method='alap'  # Better for decoherence
)

# Scheduled circuit includes Delay instructions
scheduled = pm_alap.run(circuit)
```

### Complete Transpilation Example

```python
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

# Create abstract circuit
qc = QuantumCircuit(3)
qc.h([0, 1, 2])
qc.cx(0, 2)  # Non-adjacent qubits!
qc.cx(1, 2)

# Get backend
backend = FakeManilaV2()
print(f"Backend coupling map: {backend.coupling_map}")
# Manila: 0-1-2-3-4 (linear)

# Transpile with different optimization levels
for opt_level in range(4):
    pm = generate_preset_pass_manager(
        optimization_level=opt_level,
        backend=backend
    )
    transpiled = pm.run(qc)
    print(f"Level {opt_level}: depth={transpiled.depth()}, "
          f"size={transpiled.size()}, "
          f"CNOTs={transpiled.count_ops().get('cx', 0)}")
```

### Key Transpiler Passes Reference

| Pass | Stage | Purpose |
|------|-------|---------|
| `Unroll3qOrMore` | Init | Decompose >2-qubit gates |
| `HighLevelSynthesis` | Init | Synthesize high-level objects |
| `VF2Layout` | Layout | Perfect layout via graph isomorphism |
| `SabreLayout` | Layout | Heuristic layout finding |
| `DenseLayout` | Layout | Pack into connected region |
| `TrivialLayout` | Layout | Identity mapping |
| `SabreSwap` | Routing | Heuristic SWAP insertion |
| `StochasticSwap` | Routing | Random search for routing |
| `BasisTranslator` | Translation | Convert to basis gates |
| `Optimize1qGatesDecomposition` | Optimization | Merge single-qubit gates |
| `CXCancellation` | Optimization | Remove CX pairs |
| `CommutativeCancellation` | Optimization | Use gate commutation |
| `ALAPScheduleAnalysis` | Scheduling | As Late As Possible |
| `PadDelay` | Scheduling | Insert delay instructions |

### ⚠️ Exam Traps - Transpilation

```python
# TRAP 1: SWAP = 3 CNOTs (not 2!)
# Each SWAP inserted adds 3 CNOT gates

# TRAP 2: Optimization level affects layout/routing too
# Level 0: TrivialLayout, no routing optimization
# Level 1+: SabreLayout, better routing

# TRAP 3: Higher optimization ≠ always better
# Level 3 takes longer, may not help simple circuits

# TRAP 4: Backend required for realistic transpilation
# Without backend, transpiler doesn't know constraints
transpiled = pm.run(circuit)  # ✅ With backend
# qiskit.transpile(circuit)   # ⚠️ Legacy, no backend = limited

# TRAP 5: Scheduled circuits have Delay instructions
# These are for timing, not gates
```

---

## ⚠️ MASTER TRAP LIST

> **ALL traps from ALL topics** - review before exam!

### Trap Summary Table

| # | Topic | Trap Name | ❌ Wrong | ✅ Correct |
|---|-------|-----------|----------|-----------|
| 1 | Creation | Arg order | Classical first | Qubits first |
| 2 | Properties | Method vs Property | `num_qubits()` | `num_qubits` |
| 3 | Properties | Measurements | Don't affect depth | Add to depth and size |
| 4 | compose | Width change | Expecting more qubits | Same qubit count |
| 5 | compose | inplace | `qc1.compose(qc2)` modifies | Returns new circuit |
| 6 | tensor | Width same | Same qubits | Adds new qubits |
| 7 | Parameter | Same name = same | `Parameter('θ')` twice | Different objects |
| 8 | Binding | bind_parameters | Old API | assign_parameters |
| 9 | Binding | Unbound execution | Can run unbound | Must bind first |
| 10 | c_if | Order | `c_if().gate()` | `gate().c_if()` |
| 11 | if_test | Tuple | Missing parentheses | `(clbit, value)` |
| 12 | append | List | `append(gate, 0)` | `append(gate, [0])` |
| 13 | Transpiler | SWAP cost | SWAP = 1 gate | SWAP = 3 CNOTs |

---

## 📝 PRACTICE EXAM

### Part A: Quick Fire (1 minute each)

**Q1**: What does `QuantumCircuit(3, 2)` create?
<details>
<summary>Answer</summary>

**A**: 3 qubits, 2 classical bits (Q before C)
</details>

**Q2**: Method or Property? `qc.num_qubits`
<details>
<summary>Answer</summary>

**A**: Property (no parentheses needed)
</details>

**Q3**: `qc1.compose(qc2)` - does qc1 change?
<details>
<summary>Answer</summary>

**A**: No - returns new circuit. Use `inplace=True` to modify qc1.
</details>

**Q4**: qc1 has 2 qubits, qc2 has 3. What is `qc1.tensor(qc2).num_qubits`?
<details>
<summary>Answer</summary>

**A**: 5 (tensor ADDS qubits: 2 + 3 = 5)
</details>

**Q5**: How to check if a circuit has unbound parameters?
<details>
<summary>Answer</summary>

**A**: `len(qc.parameters) > 0` or `bool(qc.parameters)`
</details>

**Q6**: What's wrong with `qc.append(HGate(), 0)`?
<details>
<summary>Answer</summary>

**A**: Qubit must be in a list: `qc.append(HGate(), [0])`
</details>

### Part B: Code Analysis (2 minutes each)

**Q7**: What's wrong with this code?
```python
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure(0, 0)
qc.c_if(0, 1).x(1)
```
<details>
<summary>Answer</summary>

**A**: Wrong order! `c_if()` must come AFTER the gate.

**Fix**: `qc.x(1).c_if(0, 1)`
</details>

**Q8**: What does this return?
```python
qc1 = QuantumCircuit(2)
qc2 = QuantumCircuit(2)
result = qc1.compose(qc2)
print(result.num_qubits)
```
<details>
<summary>Answer</summary>

**A**: **2** (compose uses same qubits, doesn't add new ones)
</details>

**Q9**: What's the depth of this circuit?
```python
qc = QuantumCircuit(3)
qc.h([0, 1, 2])  # H on all 3 qubits
qc.cx(0, 1)
qc.cx(1, 2)
```
<details>
<summary>Answer</summary>

**A**: **3** (Layer 1: 3 parallel H gates, Layer 2: CX(0,1), Layer 3: CX(1,2))

Parallel gates share the same layer!
</details>

**Q10**: Will this code work?
```python
theta = Parameter('θ')
phi = Parameter('θ')  # Same name!
qc.ry(theta, 0)
qc.rz(phi, 0)
qc.assign_parameters({theta: 0.5})
```
<details>
<summary>Answer</summary>

**A**: The circuit will have TWO different parameters (phi is still unbound!).
Same **name** ≠ same **parameter**. Each Parameter() creates a new object.
</details>

### Part C: Scenario Questions (3 minutes each)

**Q11**: You need to combine two subcircuits where one runs AFTER the other on the SAME qubits. Which method?
<details>
<summary>Answer</summary>

**A**: `compose()` - for sequential combination on same qubits
</details>

**Q12**: You're building a VQE ansatz with 4 qubits and need 8 rotation parameters. What's the most efficient approach?
<details>
<summary>Answer</summary>

**A**: Use `ParameterVector('θ', 8)` to create all 8 parameters at once:
```python
params = ParameterVector('θ', 8)
```
</details>

**Q13**: The transpiler inserted too many SWAP gates. What can you do?
<details>
<summary>Answer</summary>

**A**: 
1. Use a better layout method (e.g., `SabreLayout`)
2. Increase optimization level
3. Design circuit to minimize non-adjacent 2-qubit gates
Remember: Each SWAP = 3 CNOTs!
</details>

---

## ✅ Key Takeaways

### 📚 Concept Checklist
```
□ QuantumCircuit(n, m) creates n qubits, m classical bits (Q before C!)
□ QuantumRegister/ClassicalRegister for named, organized circuits
□ depth() = longest path (critical path), includes measurements
□ size() = total operation count (gates + measurements)
□ width() = total wires (qubits + classical bits)
□ num_qubits is a PROPERTY (no parentheses)
□ Parallel gates on different qubits share the same depth layer
□ compose() = sequential combination (same qubits, width unchanged)
□ tensor() = parallel combination (adds new qubits, width increases)
□ append() = add single gate/operation to circuit
□ Parameter = symbolic placeholder for rotation angles
□ ParameterVector = efficient creation of multiple parameters
□ Parameters must be bound before circuit execution
□ c_if() = legacy conditional (gate.c_if syntax)
□ if_test() = modern conditional (context manager with tuple)
□ Dynamic circuits: for_loop, while_loop, switch for runtime control
□ Circuit Library: QFT, RealAmplitudes, EfficientSU2, TwoLocal
□ VQE ansatz = parameterized circuit + classical optimizer
□ QAOA = alternating cost (γ) and mixer (β) layers
□ Transpiler 6 stages: Init→Layout→Routing→Translation→Optimization→Scheduling
□ SWAP = 3 CNOTs (routing is expensive!)
```

### 💻 Code Pattern Checklist
```
□ qc = QuantumCircuit(n_qubits, n_clbits) creates circuit
□ qc = QuantumCircuit(qr, cr) creates circuit with named registers
□ qr = QuantumRegister(n, 'name') creates named quantum register
□ cr = ClassicalRegister(n, 'name') creates named classical register
□ qc.depth() returns critical path length (method with parentheses)
□ qc.size() returns total operation count (method with parentheses)
□ qc.width() returns total wire count (method with parentheses)
□ qc.num_qubits returns qubit count (PROPERTY - no parentheses!)
□ qc.num_clbits returns classical bit count (PROPERTY - no parentheses!)
□ qc.count_ops() returns dict of gate counts {'h': 1, 'cx': 2}
□ result = qc1.compose(qc2) combines sequentially (returns new circuit)
□ qc1.compose(qc2, inplace=True) modifies qc1 directly
□ qc1.compose(qc2, qubits=[1,2]) maps to specific qubits
□ qc1.compose(qc2, front=True) prepends instead of appends
□ result = qc1.tensor(qc2) combines in parallel (adds qubits)
□ qc.append(gate, [qubits]) adds single operation (LIST required!)
□ theta = Parameter('θ') creates symbolic parameter
□ params = ParameterVector('θ', n) creates θ[0]...θ[n-1]
□ bound = qc.assign_parameters({param: value}) binds parameters
□ bound = qc.assign_parameters({params: [v0, v1, v2]}) binds vector
□ qc.parameters returns set of unbound parameters
□ len(qc.parameters) == 0 means all parameters bound
□ qc.x(1).c_if(clbit, value) applies X conditionally
□ with qc.if_test((clbit, value)): block applies conditionally
□ with qc.if_test((clbit, value)) as else_: enables if-else
□ from qiskit.circuit.library import QFT, RealAmplitudes, EfficientSU2
□ QFT(n) creates n-qubit Quantum Fourier Transform
□ RealAmplitudes(n, reps=k) creates VQE ansatz with k layers
□ EfficientSU2(n, reps=k) creates hardware-efficient ansatz
```

### ⚠️ Exam Trap Checklist
```
□ TRAP: QuantumCircuit(2, 3) = 2 qubits, 3 classical (NOT 2 classical, 3 qubits!)
□ TRAP: qc.num_qubits() with parentheses → ERROR! It's a property
□ TRAP: qc.depth() returns int including measurements (they add depth!)
□ TRAP: Parallel gates share layer: H on q0,q1,q2 = depth 1, not 3
□ TRAP: qc1.compose(qc2) does NOT modify qc1 (returns new circuit)
□ TRAP: compose() keeps same width (doesn't add qubits)
□ TRAP: tensor() ADDS qubits (increases width)
□ TRAP: qc.append(HGate(), 0) → ERROR! Must be list: [0]
□ TRAP: Parameter('θ') twice creates TWO different parameters!
□ TRAP: Same name ≠ same parameter (object identity matters)
□ TRAP: bind_parameters() is DEPRECATED → use assign_parameters()
□ TRAP: Running circuit with unbound parameters → ERROR!
□ TRAP: qc.c_if(0, 1).x(1) → WRONG ORDER! Use qc.x(1).c_if(0, 1)
□ TRAP: if_test without tuple: if_test(clbit, 1) → ERROR!
  → Use: if_test((clbit, 1)) with parentheses for tuple
□ TRAP: c_if register value is INTEGER: cr==3 means binary '11'
□ TRAP: SWAP decomposes to 3 CNOTs (not 1 or 2!)
□ TRAP: Higher optimization level ≠ always better (may be slower)
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 3 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🔤 "Q before C"                                                  │
│    QuantumCircuit(Qubits, Classical)                            │
│    First argument = qubits, second = classical bits             │
│                                                                  │
│ 📏 "Width=Wires, Depth=Delays, Size=Sum"                        │
│    Width: Total wires (qubits + classical bits)                 │
│    Depth: Longest path (critical path with delays)              │
│    Size: Sum of all operations                                  │
│                                                                  │
│ 🔗 "Compose = Continue, Tensor = Together"                       │
│    compose(): Continue on SAME qubits (sequential →)            │
│    tensor(): Together but SEPARATE qubits (parallel ⊗)          │
│                                                                  │
│ 📝 "Parameters are Placeholders"                                 │
│    Like x in algebra - holds spot for real value                │
│    Won't execute until bound                                    │
│                                                                  │
│ ✍️ "Assign = Attach values"                                      │
│    assign_parameters() attaches concrete numbers                │
│    Creates runnable circuit                                     │
│                                                                  │
│ 👄 "Methods have Mouths (parentheses), Properties are Plain"     │
│    depth() - mouth (parentheses) = method                       │
│    num_qubits - plain (no parentheses) = property               │
│                                                                  │
│ 🎯 "Gate first, then Condition"                                  │
│    qc.x(1).c_if(0, 1) - NOT qc.c_if(0, 1).x(1)                 │
│                                                                  │
│ 📦 "append needs List"                                           │
│    qc.append(gate, [qubits]) - qubits in list!                  │
│                                                                  │
│ 🔄 "SWAP = 3 CX"                                                 │
│    Each SWAP decomposes to 3 CNOTs                              │
│    Routing is EXPENSIVE!                                        │
│                                                                  │
│ 🔢 "Same Name ≠ Same Parameter"                                  │
│    Parameter('θ') twice = TWO different parameters              │
│    Object identity matters, not string name                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 3: CREATE CIRCUITS - ONE-PAGE SUMMARY                     ║
║              (18% of Exam - HIGHEST WEIGHT! ~12 Questions)            ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🏗️ CIRCUIT CREATION                                                   ║
║  ├─ QuantumCircuit(n_qubits, n_clbits) - Q before C!                  ║
║  ├─ QuantumCircuit(qr, cr) - with named registers                     ║
║  └─ QuantumRegister(n, 'name'), ClassicalRegister(n, 'name')          ║
║                                                                        ║
║  📏 CIRCUIT PROPERTIES                                                 ║
║  ├─ depth() = longest path (METHOD with parentheses)                  ║
║  ├─ size() = total operations (METHOD with parentheses)               ║
║  ├─ width() = total wires (METHOD with parentheses)                   ║
║  ├─ num_qubits = qubit count (PROPERTY - NO parentheses!)             ║
║  └─ count_ops() = gate counts dict {'h': 1, 'cx': 2}                  ║
║                                                                        ║
║  🔗 COMPOSITION METHODS                                                ║
║  ├─ compose(qc2) = sequential, SAME qubits (width unchanged)          ║
║  │   └─ front=True, inplace=True, qubits=[...] options                ║
║  ├─ tensor(qc2) = parallel, ADDS qubits (width increases)             ║
║  └─ append(gate, [qubits]) = single operation (LIST required!)        ║
║                                                                        ║
║  🎛️ PARAMETERIZED CIRCUITS                                             ║
║  ├─ theta = Parameter('θ') creates symbolic variable                  ║
║  ├─ params = ParameterVector('θ', n) creates θ[0]...θ[n-1]            ║
║  ├─ qc.assign_parameters({theta: 0.5}) binds value                    ║
║  ├─ qc.parameters returns set of unbound parameters                   ║
║  └─ len(qc.parameters) == 0 when fully bound                          ║
║                                                                        ║
║  📚 CIRCUIT LIBRARY                                                    ║
║  ├─ QFT(n) - Quantum Fourier Transform                                ║
║  ├─ RealAmplitudes(n, reps) - VQE ansatz (RY + CNOT)                  ║
║  ├─ EfficientSU2(n, reps) - Hardware-efficient (RY + RZ + CNOT)       ║
║  └─ TwoLocal(n, rotation, entanglement) - Customizable ansatz         ║
║                                                                        ║
║  🔀 CLASSICAL CONTROL                                                  ║
║  ├─ qc.x(1).c_if(clbit, value) - legacy conditional                   ║
║  ├─ with qc.if_test((clbit, value)): - modern (TUPLE required!)       ║
║  └─ for_loop, while_loop, switch - dynamic circuits                   ║
║                                                                        ║
║  ⚠️ TOP 5 EXAM TRAPS                                                   ║
║  1. QuantumCircuit(2, 3) = 2 qubits, 3 classical (Q before C!)        ║
║  2. num_qubits is PROPERTY (no parentheses), depth() is METHOD        ║
║  3. compose() = same qubits, tensor() = adds qubits                   ║
║  4. Parameter('θ') twice = TWO different parameters!                  ║
║  5. qc.x(1).c_if(0,1) NOT qc.c_if(0,1).x(1) - gate first!            ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 🎮 Complete VQE Walkthrough (Integration Example)

> This section demonstrates ALL exam topics in a single cohesive example!

### Step 1: Create Parameterized Ansatz (Section 3.3)

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
import numpy as np

# Create circuit with registers (Section 3.1: Circuit creation)
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
ansatz = QuantumCircuit(qr, cr)

# Create parameters for VQE (Section 3.3: Parameterized circuits)
theta = ParameterVector('θ', 4)  # 4 parameters

# Build hardware-efficient ansatz
ansatz.ry(theta[0], 0)
ansatz.ry(theta[1], 1)
ansatz.cx(0, 1)
ansatz.ry(theta[2], 0)
ansatz.ry(theta[3], 1)

print(f"Ansatz has {ansatz.num_parameters} parameters")
print(f"Parameter names: {ansatz.parameters}")
print(f"Depth: {ansatz.depth()}, Size: {ansatz.size()}")
print(ansatz.draw())
```

### Step 2: Create Hamiltonian (Section 6 - Quantum Info)

```python
from qiskit.quantum_info import SparsePauliOp

# H₂ molecule Hamiltonian (simplified) (Section 9: SparsePauliOp)
hamiltonian = SparsePauliOp.from_list([
    ("II", -1.0523),  # Constant term
    ("ZI", 0.3979),   # Z on qubit 0
    ("IZ", -0.3979),  # Z on qubit 1
    ("ZZ", -0.0112),  # ZZ interaction
    ("XX", 0.1809),   # XX interaction
])

print(f"Hamiltonian: {hamiltonian}")
```

### Step 3: Use Circuit Library (Section 3.4)

```python
from qiskit.circuit.library import EfficientSU2, TwoLocal

# Use library ansatz (Section 3.4: CircuitLibrary)
library_ansatz = EfficientSU2(
    num_qubits=2,
    reps=2,
    entanglement='linear'
)

print(f"Library ansatz parameters: {library_ansatz.num_parameters}")
print(library_ansatz.decompose().draw())

# Compose with initialization (Section 3.2: compose)
init_circuit = QuantumCircuit(2)
init_circuit.h([0, 1])

full_circuit = init_circuit.compose(library_ansatz)
print("\nComposed Circuit (init + ansatz):")
print(full_circuit.draw())
```

### Step 4: Export to OpenQASM (Section 8)

```python
# Export circuit to OpenQASM (Section 8: QASM export)
qasm_string = ansatz.qasm()
print("OpenQASM 2.0 Export:")
print(qasm_string[:300] + "...")  # First 300 characters

# Import from QASM (Section 8: STATIC method - EXAM TRAP!)
# CORRECT: QuantumCircuit.from_qasm_str(string)
# WRONG:   qc.from_qasm_str(string)
reconstructed = QuantumCircuit.from_qasm_str(qasm_string)
print("\nReconstructed from QASM:")
print(reconstructed.draw())
```

### Step 5: Transpile for Backend (Section 4)

```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

# Use fake backend for demonstration (Section 4: Backends)
backend = FakeManilaV2()

# Generate pass manager (Section 4: Transpilation)
pm = generate_preset_pass_manager(
    optimization_level=2,  # 0-3, higher = more optimization
    backend=backend
)

# Bind parameters before transpilation (Section 3.3: assign_parameters)
initial_params = np.random.random(ansatz.num_parameters) * np.pi

bound_circuit = ansatz.assign_parameters(
    {theta[i]: initial_params[i] for i in range(len(theta))}
)
bound_circuit.measure(qr, cr)  # Add measurements

# Transpile (Section 4: transpile)
transpiled = pm.run(bound_circuit)

print(f"Original depth: {bound_circuit.depth()}")
print(f"Transpiled depth: {transpiled.depth()}")
```

### Step 6: Run with Sampler (Section 5)

```python
from qiskit.primitives import StatevectorSampler

# Use local sampler for testing (Section 5: Sampler)
sampler = StatevectorSampler()

# Create measurement circuit
measure_circuit = ansatz.copy()
measure_circuit.measure(qr, cr)

# Bind and run (Section 5: PUB format)
bound_measure = measure_circuit.assign_parameters(
    {theta[i]: initial_params[i] for i in range(len(theta))}
)

job = sampler.run([bound_measure], shots=1024)
result = job.result()

# Extract counts (Section 7: Result Extraction - MEMORIZE THIS!)
counts = result[0].data.c.get_counts()  # 'c' is our classical register name
print(f"Measurement counts: {counts}")

# Alternative methods (Section 7)
bitstrings = result[0].data.c.get_bitstrings()
print(f"First 10 bitstrings: {bitstrings[:10]}")

int_counts = result[0].data.c.get_int_counts()
print(f"Integer counts: {int_counts}")
```

### Step 7: Run with Estimator (Section 6)

```python
from qiskit.primitives import StatevectorEstimator

# Use Estimator for expectation values (Section 6: Estimator)
estimator = StatevectorEstimator()

# Note: Estimator circuits should NOT have measurements!
ansatz_no_measure = ansatz.copy()

# Bind parameters
bound_ansatz = ansatz_no_measure.assign_parameters(
    {theta[i]: initial_params[i] for i in range(len(theta))}
)

# Run Estimator (Section 6: PUB format with observable)
job = estimator.run([(bound_ansatz, hamiltonian)])
result = job.result()

# Extract expectation value (Section 7: Result Extraction - MEMORIZE!)
energy = result[0].data.evs  # Expectation value
std = result[0].data.stds    # Standard deviation (if available)

print(f"Energy (expectation value): {energy}")
```

### Step 8: Visualize Results (Section 2)

```python
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector

# Plot measurement histogram (Section 2: Histogram visualization)
# plot_histogram(counts)  # Uncomment in Jupyter

# Get statevector for visualization (Section 2: State visualization)
sv = Statevector(bound_ansatz)
print(f"State vector: {sv}")

# Circuit visualization styles (Section 2: Drawing styles)
print("\nText style:")
print(ansatz.draw(output='text'))

# For Jupyter: ansatz.draw(output='mpl')  # Matplotlib style
```

### Step 9: Complete VQE Optimization Loop

```python
from scipy.optimize import minimize

def vqe_cost_function(params, ansatz, hamiltonian, estimator):
    """
    Cost function for VQE - evaluates energy at given parameters.
    
    Concepts used:
    - Section 3.3: assign_parameters() to bind values
    - Section 6: Estimator to calculate expectation value
    - Section 7: result[0].data.evs to extract result
    """
    # Bind parameters (Section 3.3)
    param_dict = {ansatz.parameters[i]: params[i] for i in range(len(params))}
    bound_circuit = ansatz.assign_parameters(param_dict)
    
    # Run Estimator (Section 6)
    job = estimator.run([(bound_circuit, hamiltonian)])
    result = job.result()
    
    # Extract energy (Section 7)
    energy = float(result[0].data.evs)
    
    return energy

# Initialize estimator and parameters
estimator = StatevectorEstimator()
initial_params = np.random.random(ansatz.num_parameters) * 2 * np.pi

print("Starting VQE optimization...")

# Run classical optimizer (scipy integration)
result = minimize(
    vqe_cost_function,
    initial_params,
    args=(ansatz, hamiltonian, estimator),
    method='COBYLA',
    options={'maxiter': 100}
)

print(f"\n=== VQE RESULTS ===")
print(f"Optimal parameters: {result.x}")
print(f"Ground state energy: {result.fun:.6f}")
print(f"Optimization converged: {result.success}")
```

### Step 10: Add Classical Control (Section 3.5)

```python
# Demonstrate conditional operations (Section 3.5: Classical Control)
teleportation = QuantumCircuit(3, 2)

# Prepare Bell pair (qubits 1-2)
teleportation.h(1)
teleportation.cx(1, 2)
teleportation.barrier()

# Prepare state to teleport (qubit 0)
teleportation.h(0)
teleportation.barrier()

# Bell measurement (qubits 0-1)
teleportation.cx(0, 1)
teleportation.h(0)
teleportation.measure([0, 1], [0, 1])
teleportation.barrier()

# Conditional corrections (Section 3.5: c_if)
teleportation.x(2).c_if(teleportation.clbits[1], 1)  # If c[1]==1, apply X
teleportation.z(2).c_if(teleportation.clbits[0], 1)  # If c[0]==1, apply Z

print("Quantum Teleportation with Classical Control:")
print(teleportation.draw())
```

### 📋 Summary: Concepts Covered by Section

| Section | Concepts Demonstrated |
|---------|----------------------|
| **Section 1** | H, RY, CX gates, barrier(), state preparation |
| **Section 2** | draw(), plot_histogram(), Statevector visualization |
| **Section 3** | QuantumCircuit, registers, depth(), size(), compose(), Parameter, assign_parameters(), c_if() |
| **Section 4** | Backend selection, transpile(), pass managers, optimization levels |
| **Section 5** | StatevectorSampler, run(), shots, PUB format |
| **Section 6** | StatevectorEstimator, SparsePauliOp, expectation values, VQE pattern |
| **Section 7** | result[0].data.c.get_counts(), result[0].data.evs, bitstrings |
| **Section 8** | qasm(), QuantumCircuit.from_qasm_str() (STATIC method!) |

---

## 📁 Files in This Section

| File | Description | Key Topics |
|------|-------------|------------|
| `circuit_basics.ipynb` | Circuit creation CODE LAB | QuantumCircuit, properties, registers |
| `circuit_composition.ipynb` | Composition CODE LAB | compose, tensor, append |
| `parameterized_circuits.ipynb` | Parameters CODE LAB | Parameter, assign_parameters, VQE |
| `circuit_library.ipynb` | Library CODE LAB | Standard gates, QFT, ansätze |
| `classical_control.ipynb` | Control CODE LAB | c_if, conditional operations |
| `dynamic_circuits.ipynb` | Dynamic CODE LAB | if_test, for_loop, while_loop |

---

## 🔗 Next Steps

1. ✅ Complete all CODE LAB notebooks in this section
2. ✅ Master depth vs size calculations
3. ✅ Build parameterized VQE ansätze from scratch
4. ✅ Practice compose vs tensor decisions
5. → Move to **Section 4 (Run Circuits)** to execute on backends

**This is the HIGHEST weighted section (18%) - invest extra time here!** 🚀🎯

---

*Last Updated: 2025*
