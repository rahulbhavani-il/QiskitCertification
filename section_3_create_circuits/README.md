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
CIRCUIT CREATION CONCEPTS:
□ QuantumCircuit(n, m) creates n qubits, m classical bits (Q before C!)
□ QuantumCircuit argument order: qubits FIRST, classical bits SECOND
□ QuantumCircuit() with no args creates empty circuit (add registers later)
□ QuantumCircuit can accept multiple registers: QuantumCircuit(qr1, qr2, cr)
□ QuantumRegister for named quantum registers (better organization)
□ ClassicalRegister for named classical registers (measurement storage)
□ Registers have .name and .size attributes
□ Qubits initialized to |0⟩ state by default (cannot specify initial state in constructor)
□ Classical bits initialized to 0 by default
□ Circuit objects are mutable (can add gates after creation)
□ Empty circuit has depth=0, size=0, width=0
□ QuantumCircuit.from_qasm_str() creates circuit from OpenQASM string
□ QuantumCircuit.from_qasm_file() loads circuit from QASM file
□ Circuit names can be set: qc.name = 'my_circuit'
□ Global phase tracked separately: qc.global_phase (doesn't affect measurements)

CIRCUIT PROPERTY CONCEPTS:
□ depth() = longest path through circuit (critical path length)
□ depth() includes ALL operations: gates, measurements, barriers
□ Parallel gates on different qubits share the same depth layer
□ Sequential gates on same qubit increase depth
□ Barrier gates add 0 to depth (they don't affect critical path)
□ size() = total operation count (sum of all gates + measurements)
□ size() includes barriers, measurements, all instructions
□ width() = total number of wires (qubits + classical bits)
□ width() = num_qubits + num_clbits (property calculation)
□ num_qubits is a PROPERTY (no parentheses!) returns int
□ num_clbits is a PROPERTY (no parentheses!) returns int
□ num_parameters returns count of unbound parameters (property)
□ count_ops() returns dict with gate counts: {'h': 2, 'cx': 3}
□ count_ops() does NOT include parameter information
□ Depth calculation: parallel ops = 1 layer, sequential = multiple layers
□ Empty circuit metrics: depth=0, size=0, width=total wires

COMPOSITION CONCEPTS:
□ compose() = sequential combination (gates applied one after another)
□ compose() operates on SAME qubits (width unchanged)
□ compose() default: appends qc2 after qc1 (front=False)
□ compose() with front=True prepends qc2 before qc1
□ compose() with qubits=[...] maps to specific target qubits
□ compose() with clbits=[...] maps classical bits
□ compose() with inplace=True modifies original circuit
□ compose() with inplace=False returns new circuit (default)
□ compose() preserves gate order and dependencies
□ compose() can map smaller circuit to subset of larger circuit
□ tensor() = parallel combination (side-by-side circuits)
□ tensor() ADDS qubits (width increases by qc2.num_qubits)
□ tensor() creates independent subsystems (no interaction)
□ tensor() equivalent to tensor product notation: qc1 ⊗ qc2
□ tensor() qubits from qc2 added after qc1's qubits
□ tensor() classical bits also concatenated
□ append() adds single instruction/gate to circuit
□ append() requires qubit list argument (even for single qubit)
□ append() can add custom gates, barriers, measurements
□ append() preserves instruction order (sequential addition)
□ Composition is associative: (A∘B)∘C = A∘(B∘C)
□ Tensor product is associative: (A⊗B)⊗C = A⊗(B⊗C)

PARAMETERIZED CIRCUIT CONCEPTS:
□ Parameter = symbolic placeholder for gate rotation angles
□ Parameter acts like variable in algebra (unbound value)
□ Parameter has .name attribute (string identifier)
□ Parameter identity matters: Parameter('θ') twice = TWO parameters!
□ Same name ≠ same parameter object (object identity, not string equality)
□ ParameterVector = efficient creation of multiple related parameters
□ ParameterVector creates indexed parameters: θ[0], θ[1], θ[2]...
□ ParameterVector useful for ansätze with many parameters
□ Parameters can appear in mathematical expressions: 2*theta, theta+phi
□ Parameter expressions supported: sin(theta), cos(theta), theta**2
□ Parameters must be bound before circuit execution (no unbound params on hardware)
□ Binding creates new circuit with concrete values (doesn't mutate original)
□ assign_parameters() is modern API (bind_parameters deprecated)
□ Partial binding allowed (bind subset of parameters)
□ qc.parameters returns ParameterView (set-like) of unbound parameters
□ len(qc.parameters) == 0 indicates fully bound circuit
□ Parameters enable variational algorithms (VQE, QAOA)
□ Parameters allow circuit reuse with different values
□ Parameter binding preserves circuit structure
□ Unbound parameters prevent transpilation (transpiler needs concrete angles)

CLASSICAL CONTROL CONCEPTS:
□ c_if() = legacy conditional execution (deprecated but still supported)
□ c_if() syntax: gate.c_if(clbit, value) - gate method first, then condition
□ c_if() operates on classical bit or classical register
□ c_if() register value interpreted as INTEGER (binary representation)
□ c_if() example: cr==3 means binary '11' (both bits set to 1)
□ c_if() condition evaluated at runtime (dynamic decision)
□ if_test() = modern conditional (context manager API)
□ if_test() requires TUPLE syntax: (clbit, value) not clbit, value
□ if_test() supports if-else blocks with 'as else_:' syntax
□ if_test() integrates with expr module for complex conditions
□ if_test() can test individual bits or full registers
□ expr.logic_and(), expr.logic_or() combine conditions
□ expr.equal(), expr.not_equal() for equality testing
□ expr.less(), expr.greater() for comparisons
□ Measurements must happen BEFORE conditionals (condition needs measured value)
□ Conditional gates only execute if condition is true
□ Conditional execution adds to circuit depth (branch taken)
□ Classical bits hold measurement outcomes (0 or 1)
□ Classical registers combine bits into integer values
□ Bit indexing: cr[0] is least significant bit (LSB)
□ Register interpretation: big-endian for bit ordering

DYNAMIC CIRCUIT CONCEPTS:
□ Dynamic circuits = circuits with runtime control flow
□ for_loop() executes block for fixed number of iterations
□ for_loop() syntax: with qc.for_loop(range(n)):
□ for_loop() loop variable can be used in block (parameter)
□ while_loop() executes while condition remains true
□ while_loop() syntax: with qc.while_loop((clbit, value)):
□ while_loop() condition checked at runtime (measurement-based)
□ switch() enables multi-way branching (multiple cases)
□ switch() syntax: with qc.switch(creg) as case:
□ switch() cases can be individual values or ranges
□ switch() default case with case(case.DEFAULT):
□ break_loop() and continue_loop() control loop flow
□ Dynamic circuits require hardware support (not all backends)
□ Dynamic circuits enable adaptive algorithms
□ Dynamic circuits allow feedback (measurement → gate decision)
□ Loop depth calculation includes iterations
□ Nested control flow supported (loops in conditionals)

CIRCUIT LIBRARY CONCEPTS:
□ qiskit.circuit.library contains pre-built circuits
□ QFT = Quantum Fourier Transform (basis of many algorithms)
□ QFT(n) creates n-qubit QFT circuit
□ QFT has do_swaps parameter (bit reversal swaps)
□ RealAmplitudes = VQE ansatz with RY rotations + CNOT entanglement
□ RealAmplitudes(n, reps) has reps repetition layers
□ RealAmplitudes uses only real amplitudes (no complex phase)
□ EfficientSU2 = hardware-efficient ansatz (RY + RZ + CNOT)
□ EfficientSU2 covers full SU(2) single-qubit space
□ EfficientSU2 efficient on hardware (basis gate compatible)
□ TwoLocal = customizable ansatz (rotation + entanglement)
□ TwoLocal(n, rotation, entanglement, reps) fully configurable
□ NLocal generalizes to n-qubit gates (N>2)
□ PauliEvolutionGate implements e^(-iHt) time evolution
□ Library circuits are parameterized (must bind before execution)
□ Library circuits compose with regular circuits
□ Library circuits optimize for specific use cases

TRANSPILER CONCEPTS (6 STAGES):
□ Transpiler = compiler from logical circuit to physical circuit
□ Transpiler has 6 sequential stages (pipeline architecture)
□ Stage 1 - Init: Decomposes high-level gates (3+ qubits)
□ Init stage: Unroll3qOrMore pass breaks down complex gates
□ Init stage ensures max 2-qubit gates for routing
□ Stage 2 - Layout: Maps logical qubits → physical qubits
□ Layout selection critical for circuit performance
□ TrivialLayout: q[i] → physical qubit i (simple, no optimization)
□ VF2Layout: Graph isomorphism for perfect subgraph embedding
□ VF2Layout finds optimal layout when it exists (may be slow)
□ SabreLayout: Heuristic search, best for general use
□ SabreLayout works well on large circuits (scales better)
□ DenseLayout: Places connected qubits on connected hardware qubits
□ Layout affects routing cost (good layout = fewer SWAPs)
□ Stage 3 - Routing: Inserts SWAP gates for non-adjacent qubits
□ Routing needed when 2-qubit gate spans non-connected qubits
□ Each SWAP = 3 CNOT gates (expensive operation!)
□ SabreSwap: Heuristic routing (default, generally good)
□ StochasticSwap: Random search with scoring (alternative)
□ Routing minimizes SWAP count (depth vs gate count tradeoff)
□ Coupling map defines allowed 2-qubit interactions
□ Stage 4 - Translation: Converts gates to hardware basis gates
□ Translation uses BasisTranslator pass
□ Basis gates: hardware-native operations (e.g., ['id','rz','sx','x','cx'])
□ Translation ensures all gates are executable on hardware
□ Some gates decompose into multiple basis gates
□ Stage 5 - Optimization: Reduces circuit depth and gate count
□ Optimization level 0: No optimization (TrivialLayout, minimal passes)
□ Optimization level 1: Light optimization (basic passes)
□ Optimization level 2: Medium optimization (default, balanced)
□ Optimization level 3: Heavy optimization (unitary synthesis, slow)
□ Higher optimization = more compilation time
□ Higher optimization ≠ always better results (diminishing returns)
□ Optimization passes: gate cancellation, commutation analysis, resynthesis
□ Stage 6 - Scheduling: Adds timing information (pulse-level)
□ Scheduling converts to time-domain representation
□ ASAP: As Soon As Possible (minimize idle at start)
□ ALAP: As Late As Possible (minimize idle at end)
□ ALAP better for decoherence (gates execute closer to measurement)
□ Scheduled circuits include Delay instructions
□ Delay instructions represent idle time (no gates)
□ Scheduling aligns gates with hardware constraints
□ Backend object provides: coupling map, basis gates, timing info
□ Transpiler without backend uses generic constraints
□ Transpilation deterministic given same seed (reproducible)
□ PassManager orchestrates all stages (configurable pipeline)
```

### 💻 Code Pattern Checklist
```
CIRCUIT CREATION PATTERNS:
□ from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
□ qc = QuantumCircuit(3) creates 3 qubits, 0 classical bits
□ qc = QuantumCircuit(3, 2) creates 3 qubits, 2 classical bits
□ qc = QuantumCircuit(n_qubits, n_clbits) standard creation pattern
□ qr = QuantumRegister(5, 'q') creates quantum register named 'q'
□ cr = ClassicalRegister(5, 'c') creates classical register named 'c'
□ qc = QuantumCircuit(qr, cr) creates circuit from registers
□ qc = QuantumCircuit(qr1, qr2, cr) multiple registers allowed
□ qc = QuantumCircuit() creates empty circuit
□ qc.add_register(qr) adds register to existing circuit
□ qc.add_register(cr) adds classical register
□ qc.qubits returns list of Qubit objects
□ qc.clbits returns list of Clbit objects
□ qc.qregs returns list of QuantumRegister objects
□ qc.cregs returns list of ClassicalRegister objects
□ qc.name = 'my_circuit' sets circuit name
□ qc.name returns circuit name (string)
□ qc.global_phase = np.pi/4 sets global phase
□ qc.metadata = {'key': 'value'} attaches metadata dict

CIRCUIT PROPERTY PATTERNS:
□ depth_value = qc.depth() returns int (METHOD with parentheses)
□ size_value = qc.size() returns int (METHOD with parentheses)
□ width_value = qc.width() returns int (METHOD with parentheses)
□ num_q = qc.num_qubits returns int (PROPERTY - NO parentheses!)
□ num_c = qc.num_clbits returns int (PROPERTY - NO parentheses!)
□ num_p = qc.num_parameters returns int (PROPERTY - NO parentheses!)
□ ops_dict = qc.count_ops() returns dict {'h': 2, 'cx': 3}
□ total_gates = sum(qc.count_ops().values()) sum all gate counts
□ qc.count_ops().get('cx', 0) safe access (0 if no CNOT)
□ qc.decompose() returns decomposed circuit (breaks down complex gates)
□ qc.decompose().depth() depth after decomposition
□ qc.inverse() returns inverse circuit (reverse order, conjugate gates)
□ qc.copy() creates deep copy of circuit
□ qc.copy(name='new_name') copy with new name
□ qc.clear() removes all instructions (empties circuit)
□ qc.remove_final_measurements() removes measurements at end
□ qc.remove_final_measurements(inplace=False) returns new circuit

GATE APPLICATION PATTERNS:
□ qc.h(0) applies Hadamard to qubit 0
□ qc.h([0, 1, 2]) applies Hadamard to multiple qubits (parallel)
□ qc.cx(0, 1) applies CNOT (control=0, target=1)
□ qc.cx([0, 1], [1, 2]) applies multiple CNOTs: 0→1, 1→2
□ qc.measure(0, 0) measures qubit 0 into classical bit 0
□ qc.measure([0, 1], [0, 1]) measures multiple qubits
□ qc.measure_all() adds measurements for all qubits
□ qc.measure_all(inplace=False) returns new circuit with measurements
□ qc.barrier() adds barrier across all qubits
□ qc.barrier([0, 1]) barrier on specific qubits
□ qc.reset(0) resets qubit 0 to |0⟩
□ qc.reset([0, 1]) resets multiple qubits

COMPOSITION PATTERNS:
□ result = qc1.compose(qc2) sequential composition (qc2 after qc1)
□ result = qc1.compose(qc2, inplace=False) returns NEW circuit (default)
□ qc1.compose(qc2, inplace=True) modifies qc1 directly (no return)
□ qc1.compose(qc2, qubits=[2, 3]) maps qc2 to specific qubits in qc1
□ qc1.compose(qc2, qubits=[2, 3], clbits=[0]) maps quantum and classical
□ qc1.compose(qc2, front=True) prepends qc2 BEFORE qc1
□ qc1.compose(qc2, front=True, inplace=True) prepend and modify
□ result = qc1.tensor(qc2) parallel composition (qc1 ⊗ qc2)
□ result = qc1.tensor(qc2, inplace=False) returns NEW circuit (default)
□ qc1.tensor(qc2, inplace=True) modifies qc1 directly
□ qc.tensor(qc2) adds qc2's qubits after qc1's qubits
□ from qiskit.circuit import Gate, Instruction
□ custom_gate = Gate('mygate', num_qubits=2, params=[])
□ qc.append(custom_gate, [0, 1]) adds custom gate
□ qc.append(HGate(), [0]) adds Hadamard via append
□ qc.append(CXGate(), [0, 1]) adds CNOT via append
□ qc.append(instruction, qargs=[0], cargs=[0]) append with classical args

PARAMETERIZED CIRCUIT PATTERNS:
□ from qiskit.circuit import Parameter, ParameterVector
□ theta = Parameter('θ') creates single parameter
□ phi = Parameter('φ') creates another parameter
□ params = ParameterVector('θ', 5) creates θ[0], θ[1], ..., θ[4]
□ qc.rx(theta, 0) rotation gate with parameter
□ qc.ry(2*theta, 0) parameter in expression
□ qc.rz(theta + phi, 0) combines parameters
□ import numpy as np
□ qc.ry(np.pi*theta, 0) parameter with constant
□ param_set = qc.parameters returns ParameterView (set-like)
□ list(qc.parameters) converts to list
□ len(qc.parameters) counts unbound parameters
□ param_dict = {theta: 0.5, phi: 1.2} binding dictionary
□ bound = qc.assign_parameters(param_dict) binds and returns new circuit
□ bound = qc.assign_parameters({theta: 0.5}) partial binding allowed
□ bound = qc.assign_parameters({params: [0.1, 0.2, 0.3, 0.4, 0.5]}) bind vector
□ bound = qc.assign_parameters([0.1, 0.2], inplace=False) positional binding
□ qc.assign_parameters(values, inplace=True) modifies circuit directly
□ len(bound.parameters) == 0 check if fully bound
□ qc.bind_parameters() DEPRECATED - use assign_parameters()
□ from qiskit.circuit import ParameterExpression
□ expr = 2*theta + np.sin(phi) complex parameter expression
□ qc.ry(expr, 0) use expression as gate parameter

CLASSICAL CONTROL PATTERNS (LEGACY):
□ qc.measure(0, 0) measure first (condition needs measured value)
□ qc.x(1).c_if(cr[0], 1) apply X if classical bit 0 is 1
□ qc.h(0).c_if(cr, 3) apply H if classical register equals 3 (binary '11')
□ qc.cx(0, 1).c_if(cr[1], 0) apply CNOT if bit 1 is 0
□ gate_instruction = qc.x(0).c_if(cr, 1) returns instruction
□ c_if syntax: gate.c_if(classical, value) - gate FIRST, condition second

CLASSICAL CONTROL PATTERNS (MODERN):
□ from qiskit.circuit.classical import expr
□ qc.measure(0, 0) measure first
□ with qc.if_test((cr[0], 1)): uses TUPLE (clbit, value)
□     qc.x(1) applies X inside if block
□ with qc.if_test((cr, 3)): register comparison (cr == 3)
□     qc.h(0) operations in if block
□ with qc.if_test((cr[0], 1)) as else_: if-else syntax
□     qc.x(1) if branch
□ with else_: else block
□     qc.h(1) else branch
□ condition = expr.logic_and(cr[0], cr[1]) create AND condition
□ with qc.if_test(condition): use complex condition
□     qc.x(0)
□ condition = expr.equal(cr, 5) equality test
□ condition = expr.not_equal(cr, 0) inequality test
□ condition = expr.less(cr, 10) less than comparison
□ condition = expr.greater(cr, 2) greater than comparison
□ condition = expr.logic_or(cr[0], cr[1]) OR condition
□ condition = expr.logic_not(cr[0]) NOT condition

DYNAMIC CIRCUIT PATTERNS:
□ with qc.for_loop(range(5)): fixed 5 iterations
□     qc.h(0) operation repeated 5 times
□ with qc.for_loop(range(3)) as i: loop with variable
□     qc.rx(i*0.1, 0) use loop variable
□ qc.measure(0, 0)
□ with qc.while_loop((cr[0], 0)): loop while bit 0 is 0
□     qc.h(0)
□     qc.measure(0, 0) re-measure in loop
□ with qc.switch(cr) as case: switch on register value
□     with case(0): case for value 0
□         qc.x(0)
□     with case(1): case for value 1
□         qc.h(0)
□     with case(case.DEFAULT): default case
□         qc.reset(0)
□ qc.break_loop() exit loop early
□ qc.continue_loop() skip to next iteration

CIRCUIT LIBRARY PATTERNS:
□ from qiskit.circuit.library import QFT, RealAmplitudes, EfficientSU2
□ from qiskit.circuit.library import TwoLocal, NLocal, PauliEvolutionGate
□ qft = QFT(num_qubits=4) create 4-qubit QFT
□ qft = QFT(4, do_swaps=True) QFT with bit reversal swaps (default)
□ qft = QFT(4, do_swaps=False) QFT without swaps
□ qft_inverse = qft.inverse() inverse QFT
□ qc.append(qft, range(4)) append QFT to circuit
□ ansatz = RealAmplitudes(num_qubits=3, reps=2) VQE ansatz
□ ansatz = RealAmplitudes(3, reps=2, entanglement='linear') linear entanglement
□ ansatz = RealAmplitudes(3, reps=2, entanglement='full') full entanglement
□ print(ansatz.num_parameters) check parameter count
□ bound_ansatz = ansatz.assign_parameters([0.1, 0.2, ...]) bind parameters
□ ansatz = EfficientSU2(num_qubits=4, reps=3) hardware-efficient ansatz
□ ansatz = EfficientSU2(4, su2_gates=['ry', 'rz']) custom single-qubit gates
□ ansatz = EfficientSU2(4, entanglement='sca') sca entanglement pattern
□ ansatz = TwoLocal(4, rotation_blocks='ry', entanglement_blocks='cx')
□ ansatz = TwoLocal(4, ['ry', 'rz'], 'cz', reps=2) custom rotation/entangle
□ from qiskit.circuit.library import PauliFeatureMap, ZFeatureMap
□ feature_map = PauliFeatureMap(feature_dimension=2, reps=2)
□ from qiskit.circuit.library import HGate, XGate, CXGate
□ h_gate = HGate()
□ qc.append(h_gate, [0])

TRANSPILER PATTERNS:
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
□ from qiskit.transpiler import PassManager, CouplingMap
□ from qiskit_ibm_runtime import QiskitRuntimeService
□ service = QiskitRuntimeService()
□ backend = service.backend('ibm_brisbane')
□ pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
□ pm = generate_preset_pass_manager(optimization_level=2, backend=backend) default
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend) heavy
□ pm = generate_preset_pass_manager(0, backend) level 0 (no optimization)
□ transpiled = pm.run(qc) transpile circuit
□ transpiled_circuits = pm.run([qc1, qc2, qc3]) batch transpilation
□ pm = generate_preset_pass_manager(2, backend, layout_method='sabre')
□ pm = generate_preset_pass_manager(2, backend, layout_method='vf2')
□ pm = generate_preset_pass_manager(2, backend, layout_method='trivial')
□ pm = generate_preset_pass_manager(2, backend, layout_method='dense')
□ pm = generate_preset_pass_manager(2, backend, routing_method='sabre') default
□ pm = generate_preset_pass_manager(2, backend, routing_method='stochastic')
□ pm = generate_preset_pass_manager(2, backend, scheduling_method='asap')
□ pm = generate_preset_pass_manager(2, backend, scheduling_method='alap') better
□ pm = generate_preset_pass_manager(2, backend, seed_transpiler=42) reproducible
□ pm = generate_preset_pass_manager(2, backend, approximation_degree=0.99)
□ coupling_map = CouplingMap([[0,1], [1,2], [2,3]]) custom coupling
□ pm = generate_preset_pass_manager(2, backend, coupling_map=coupling_map)
□ from qiskit import transpile
□ transpiled = transpile(qc, backend) simple transpile (uses defaults)
□ transpiled = transpile(qc, backend, optimization_level=2)
□ transpiled = transpile(qc, backend, basis_gates=['id','rz','sx','cx'])
□ transpiled = transpile(qc, backend, coupling_map=coupling_map)
□ transpiled = transpile(qc, backend, initial_layout=[0,1,3]) manual layout
□ transpiled.depth() check transpiled depth
□ transpiled.count_ops() check gate counts after transpilation
□ print(transpiled.layout) view qubit layout
```

### ⚠️ Exam Trap Checklist
```
CIRCUIT CREATION TRAPS:
□ TRAP: QuantumCircuit(2, 3) = 2 QUBITS, 3 CLASSICAL BITS!
  → Fix: Arguments are (qubits, classical) not (classical, qubits)
  → Why: Q before C! Quantum first, classical second
□ TRAP: QuantumCircuit(5) creates 5 qubits but 0 classical bits
  → Fix: Add measurements or specify classical: QuantumCircuit(5, 5)
  → Why: Classical bits not auto-created, must be explicit
□ TRAP: Trying to measure without classical bits → ERROR!
  → Fix: Create circuit with classical bits or use measure_all()
  → Why: Measurements need classical bits to store results
□ TRAP: Assuming qubits start in arbitrary states
  → Fix: All qubits initialize to |0⟩ by default
  → Why: Cannot specify initial state in constructor
□ TRAP: Confusing register size with circuit width
  → Fix: width = num_qubits + num_clbits (total wires)
  → Why: Width includes both quantum and classical wires
□ TRAP: Modifying circuit in place without realizing it
  → Fix: Most methods have inplace parameter (default False)
  → Why: qc.compose(qc2) returns new, qc.compose(qc2, inplace=True) modifies

PROPERTY vs METHOD TRAPS:
□ TRAP: qc.num_qubits() with parentheses → AttributeError!
  → Fix: qc.num_qubits (NO parentheses - it's a PROPERTY)
  → Why: Properties accessed without (), methods with ()
□ TRAP: qc.num_clbits() with parentheses → AttributeError!
  → Fix: qc.num_clbits (NO parentheses - it's a PROPERTY)
  → Why: Same as num_qubits - property not method
□ TRAP: qc.depth without parentheses → returns method object
  → Fix: qc.depth() (WITH parentheses - it's a METHOD)
  → Why: Methods need () to execute and return value
□ TRAP: qc.size without parentheses → returns method object
  → Fix: qc.size() (WITH parentheses - it's a METHOD)
  → Why: Methods need () to execute
□ TRAP: qc.width without parentheses → returns method object
  → Fix: qc.width() (WITH parentheses - it's a METHOD)
  → Why: Methods need () to execute
□ TRAP: Mixing up which are properties and which are methods
  → Fix: PROPERTIES: num_qubits, num_clbits, num_parameters (no ())
  → Fix: METHODS: depth(), size(), width(), count_ops() (with ())
  → Why: API design inconsistency - memorize which is which!

DEPTH/SIZE/WIDTH CALCULATION TRAPS:
□ TRAP: qc.depth() excludes measurements (wrong!)
  → Fix: depth() INCLUDES measurements, barriers (all operations)
  → Why: Measurements take time, contribute to critical path
□ TRAP: Parallel gates add depth: H on q[0,1,2] = depth 3
  → Fix: Parallel gates share ONE layer: depth = 1
  → Why: Gates on different qubits execute simultaneously
□ TRAP: Barrier gates add to depth count
  → Fix: Barriers have zero duration (don't add to depth)
  → Why: Barriers are compiler hints, not physical operations
□ TRAP: Empty circuit has non-zero depth
  → Fix: Empty circuit: depth=0, size=0, width=0
  → Why: No operations = zero critical path length
□ TRAP: count_ops() includes parameter information
  → Fix: count_ops() only counts gate types, ignores parameters
  → Why: Returns {'h': 2, 'rx': 3} not parameter values

COMPOSITION TRAPS:
□ TRAP: qc1.compose(qc2) modifies qc1 directly
  → Fix: compose() returns NEW circuit (default inplace=False)
  → Why: Functional programming style - immutable by default
□ TRAP: compose() ADDS qubits (increases width)
  → Fix: compose() uses SAME qubits (width unchanged)
  → Why: Sequential execution on existing qubits
□ TRAP: tensor() uses SAME qubits (width unchanged)
  → Fix: tensor() ADDS qubits (width increases)
  → Why: Parallel composition creates independent subsystems
□ TRAP: compose(qc2, front=False) prepends qc2
  → Fix: front=False APPENDS qc2 after qc1 (default)
  → Why: front=True prepends, front=False appends
□ TRAP: Forgetting to specify target qubits in compose
  → Fix: compose(qc2, qubits=[2,3]) maps to specific qubits
  → Why: Default uses qubits in order [0,1,2,...]
□ TRAP: qc1.tensor(qc2) and qc2.tensor(qc1) are the same
  → Fix: Order matters! qc1⊗qc2 ≠ qc2⊗qc1 (qubit ordering differs)
  → Why: qc1's qubits come first, then qc2's qubits
□ TRAP: Using + operator for composition
  → Fix: Use .compose() method explicitly
  → Why: + operator not defined for QuantumCircuit

APPEND TRAPS:
□ TRAP: qc.append(HGate(), 0) → TypeError!
  → Fix: qc.append(HGate(), [0]) - qubits must be LIST
  → Why: append expects list even for single qubit
□ TRAP: qc.append(CXGate(), [0]) → Wrong number of qubits!
  → Fix: qc.append(CXGate(), [0, 1]) - CNOT needs 2 qubits
  → Why: Gate requires specific number of qubits
□ TRAP: append() returns None (can't chain)
  → Fix: append() modifies circuit in place (returns None)
  → Why: Unlike compose(), append is always in-place
□ TRAP: Using wrong gate import
  → Fix: from qiskit.circuit.library import HGate, CXGate
  → Why: Gates in qiskit.circuit.library, not main qiskit

PARAMETER TRAPS:
□ TRAP: Parameter('θ') twice creates SAME parameter
  → Fix: Parameter('θ') twice creates TWO DIFFERENT parameters!
  → Why: Object identity matters, not string name equality
□ TRAP: Checking parameter equality with == operator
  → Fix: Parameter identity based on object, not name
  → Why: theta1 = Parameter('θ'), theta2 = Parameter('θ') → theta1 ≠ theta2
□ TRAP: Parameters with same name can be bound independently (wrong!)
  → Fix: Each Parameter object needs separate binding
  → Why: assign_parameters uses object as dict key, not name
□ TRAP: bind_parameters() is current API
  → Fix: bind_parameters() is DEPRECATED, use assign_parameters()
  → Why: API modernization, bind_parameters removed in newer versions
□ TRAP: Running circuit with unbound parameters executes anyway
  → Fix: Unbound parameters → ERROR at runtime!
  → Why: Hardware/simulator needs concrete angle values
□ TRAP: len(qc.parameters) counts individual parameters only (wrong!)
  → Fix: len(qc.parameters) counts total unbound parameters
  → Why: ParameterVector elements counted separately
□ TRAP: assign_parameters modifies circuit in place
  → Fix: assign_parameters returns NEW circuit (default inplace=False)
  → Why: Immutable pattern - original circuit unchanged
□ TRAP: Partial binding not allowed
  → Fix: Partial binding IS allowed! Bind subset of parameters
  → Why: Can bind parameters in multiple steps
□ TRAP: ParameterVector('θ', 3) creates single parameter
  → Fix: Creates 3 parameters: θ[0], θ[1], θ[2]
  → Why: Vector notation for indexed parameters
□ TRAP: Forgetting to bind parameters before transpilation
  → Fix: Transpiler requires fully bound circuit (no free parameters)
  → Why: Transpiler needs concrete values for optimization

CLASSICAL CONTROL TRAPS:
□ TRAP: qc.c_if(0, 1).x(1) → Wrong method order!
  → Fix: qc.x(1).c_if(0, 1) - GATE first, CONDITION second
  → Why: c_if is method on gate instruction, not circuit
□ TRAP: if_test without tuple: if_test(clbit, 1)
  → Fix: if_test((clbit, 1)) - needs TUPLE with parentheses
  → Why: API requires tuple for condition specification
□ TRAP: c_if register value interpreted as array
  → Fix: Register value is INTEGER: cr==3 means binary '11'
  → Why: Register bits combined into single integer value
□ TRAP: Not measuring before conditional execution
  → Fix: Must measure BEFORE c_if/if_test
  → Why: Conditional needs measured value to evaluate
□ TRAP: Assuming c_if() is modern API
  → Fix: c_if() is LEGACY (deprecated), if_test() is MODERN
  → Why: Know both for exam! Transition period
□ TRAP: if_test() supports else without special syntax
  → Fix: Need 'as else_:' syntax for else block
  → Why: with qc.if_test((clbit, 1)) as else_:
□ TRAP: Using expr module without import
  → Fix: from qiskit.circuit.classical import expr
  → Why: Complex conditions require expr module
□ TRAP: Bit indexing confusion: cr[0] vs cr[1]
  → Fix: cr[0] is LSB (least significant bit)
  → Why: Little-endian convention in Qiskit
□ TRAP: Conditional gates always execute (wrong!)
  → Fix: Conditional gates only execute if condition TRUE
  → Why: That's the point of conditionals!
□ TRAP: Conditionals don't add to depth
  → Fix: Conditionals DO add to depth (branch evaluation time)
  → Why: Runtime evaluation and potential execution

DYNAMIC CIRCUIT TRAPS:
□ TRAP: for_loop without range: for_loop(5)
  → Fix: for_loop(range(5)) - needs range object
  → Why: Syntax follows Python conventions
□ TRAP: while_loop condition without tuple
  → Fix: while_loop((clbit, value)) - needs TUPLE
  → Why: Same tuple requirement as if_test
□ TRAP: while_loop without measurement in loop body → infinite loop!
  → Fix: Must re-measure inside loop to update condition
  → Why: Condition based on classical bit value
□ TRAP: switch cases overlap or conflict
  → Fix: Each case should be distinct value
  → Why: Switch branches to first matching case
□ TRAP: Using break/continue outside loop context
  → Fix: break_loop() and continue_loop() only valid inside loops
  → Why: Loop control flow only meaningful in loop
□ TRAP: Assuming all backends support dynamic circuits
  → Fix: Dynamic circuits require hardware support (not universal)
  → Why: Feature availability depends on backend capabilities
□ TRAP: Loop variable type confusion
  → Fix: Loop variable in for_loop is Parameter (symbolic)
  → Why: for_loop(range(n)) as i → i is Parameter object

CIRCUIT LIBRARY TRAPS:
□ TRAP: QFT(4) returns transpiled circuit ready to run
  → Fix: Library circuits are LOGICAL (need transpilation)
  → Why: Still need to map to hardware basis gates
□ TRAP: Library circuits have no parameters
  → Fix: Most library circuits (ansätze) are PARAMETERIZED
  → Why: Must bind parameters before execution
□ TRAP: RealAmplitudes covers full unitary space
  → Fix: RealAmplitudes only covers REAL amplitudes (no complex phase)
  → Why: Name says it all - "Real" amplitudes
□ TRAP: EfficientSU2 is most general ansatz
  → Fix: EfficientSU2 is hardware-efficient, not most expressive
  → Why: Optimized for specific hardware, not full SU(2^n)
□ TRAP: Forgetting to check num_parameters for library circuits
  → Fix: ansatz.num_parameters tells you how many values to bind
  → Why: Different reps values change parameter count
□ TRAP: QFT inverse is QFT with different parameters
  → Fix: QFT inverse is CIRCUIT inverse (reverse + conjugate)
  → Why: qft.inverse() gives QFT†

TRANSPILER TRAPS:
□ TRAP: SWAP decomposes to 1 or 2 CNOTs
  → Fix: Each SWAP = 3 CNOT gates (expensive!)
  → Why: SWAP(a,b) = CX(a,b) + CX(b,a) + CX(a,b)
□ TRAP: Transpiler works without backend specification
  → Fix: Transpiler NEEDS backend for realistic results
  → Why: Backend provides coupling map + basis gates
□ TRAP: Optimization level 3 always best
  → Fix: Level 3 takes LONGER, not always better quality
  → Why: Diminishing returns, increased compilation time
□ TRAP: Optimization level 0 uses advanced layout
  → Fix: Level 0 uses TrivialLayout (q[i]→i, no optimization)
  → Why: Level 0 means NO optimization
□ TRAP: Scheduled circuits ready to execute normally
  → Fix: Scheduled circuits have Delay instructions (timing info)
  → Why: Scheduling adds pulse-level timing details
□ TRAP: VF2Layout always succeeds
  → Fix: VF2Layout may FAIL on large circuits (no perfect layout)
  → Why: Graph isomorphism problem can be hard
□ TRAP: ASAP scheduling better than ALAP
  → Fix: ALAP scheduling BETTER for decoherence
  → Why: ALAP minimizes idle time before measurement
□ TRAP: Translation stage handles any gate
  → Fix: Translation requires gates in basis set or decomposable
  → Why: Must specify valid basis gates for hardware
□ TRAP: Routing always finds optimal SWAP insertion
  → Fix: Routing is HEURISTIC (may not be optimal)
  → Why: Optimal routing is NP-hard problem
□ TRAP: Transpilation deterministic without seed
  → Fix: Use seed_transpiler for reproducibility
  → Why: Heuristics have randomness (different runs vary)
□ TRAP: Higher optimization level reduces depth
  → Fix: Level 3 may INCREASE depth in some cases
  → Why: Optimization targets gate count, not always depth
□ TRAP: Layout methods all produce same quality
  → Fix: VF2 best quality, Sabre best scalability, Trivial no optimization
  → Why: Different algorithms, different tradeoffs
□ TRAP: Coupling map optional for transpilation
  → Fix: Coupling map REQUIRED for routing stage
  → Why: Routing needs to know which qubits connect
□ TRAP: Basis gates can be inferred from circuit
  → Fix: Basis gates must be SPECIFIED (from backend or explicit)
  → Why: Transpiler needs to know target gate set
□ TRAP: Init stage only handles 3-qubit gates
  → Fix: Init handles ALL gates with 3+ qubits
  → Why: Unroll3qOrMore breaks down any high-qubit-count gates
□ TRAP: Transpiled circuit has same depth as original
  → Fix: Transpiled circuit usually has GREATER depth (SWAPs added)
  → Why: Routing and decomposition increase operation count

DEPRECATED API TRAPS:
□ TRAP: Using bind_parameters() in modern code
  → Fix: Use assign_parameters() instead
  → Why: bind_parameters() deprecated and removed
□ TRAP: Using qiskit.compiler.transpile from old import
  → Fix: from qiskit import transpile (modern import)
  → Why: Import location changed in recent versions
□ TRAP: Using add_bits() instead of add_register()
  → Fix: Both valid, but add_register() cleaner for multiple bits
  → Why: API provides both options
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
│    Think: "Quantum Questions Come first, Classical second"      │
│    QuantumCircuit(3, 2) = 3 qubits, 2 classical (not reverse!) │
│                                                                  │
│ 📏 "Width=Wires, Depth=Delays, Size=Sum"                        │
│    Width: Total wires (qubits + classical bits counted)         │
│    Depth: Longest path (critical path with delays)              │
│    Size: Sum of all operations (total count)                    │
│    Think: "WDS = Wires, Delays, Sum"                            │
│    width() with (), but num_qubits without ()!                  │
│                                                                  │
│ 🔗 "Compose = Continue, Tensor = Together-separate"              │
│    compose(): Continue on SAME qubits (sequential →)            │
│    tensor(): Together but SEPARATE qubits (parallel ⊗)          │
│    Think: "Compose chains, Tensor pairs"                        │
│    compose doesn't add qubits, tensor does!                     │
│    compose: qc1 then qc2 on same wires                          │
│    tensor: qc1 and qc2 side-by-side (new wires)                 │
│                                                                  │
│ 🔀 "Inplace=True → Changes Original"                             │
│    inplace=False returns NEW circuit (default)                  │
│    inplace=True modifies ORIGINAL circuit                       │
│    Think: "True = Transforms in place"                          │
│    compose/tensor/assign_parameters all have inplace param      │
│                                                                  │
│ 📝 "Parameters are Placeholders (like algebra variables)"        │
│    Like x in algebra - holds spot for real value                │
│    Won't execute until bound (needs concrete value)             │
│    Think: "Parameter = Pending value"                           │
│    Must assign before running on hardware!                      │
│                                                                  │
│ ✍️ "Assign = Attach actual values"                               │
│    assign_parameters() attaches concrete numbers                │
│    Creates runnable circuit (executable)                        │
│    Think: "Assign = Actually Set Specific numbers"              │
│    bind_parameters() is OLD (deprecated!)                       │
│                                                                  │
│ 👄 "Methods have Mouths (), Properties are Plain"                │
│    depth() - mouth (parentheses) = method CALL                  │
│    num_qubits - plain (no parentheses) = property ACCESS        │
│    Think: "Call with (), Access without ()"                     │
│    METHODS: depth(), size(), width(), count_ops()               │
│    PROPERTIES: num_qubits, num_clbits, num_parameters           │
│                                                                  │
│ 🎯 "Gate first, then Condition"                                  │
│    qc.x(1).c_if(0, 1) - gate THEN condition                     │
│    NOT qc.c_if(0, 1).x(1) - wrong order!                        │
│    Think: "Gate Goes first, Condition checks if"                │
│    c_if is method ON the gate instruction                       │
│                                                                  │
│ 📦 "append needs List (even for one)"                            │
│    qc.append(gate, [qubits]) - qubits in LIST always!           │
│    qc.append(HGate(), [0]) not HGate(), 0                       │
│    Think: "append Array (list of qubits)"                       │
│    Single qubit still needs [0] not just 0                      │
│                                                                  │
│ 🔄 "SWAP = 3 CX = Super eXpensive"                               │
│    Each SWAP decomposes to 3 CNOT gates                         │
│    Routing is EXPENSIVE! Minimize SWAPs                          │
│    Think: "SWAP Consumes three CX gates"                        │
│    Good layout reduces SWAPs (critical for performance)         │
│                                                                  │
│ 🔢 "Same Name ≠ Same Parameter (object identity)"                │
│    Parameter('θ') twice = TWO different parameter objects       │
│    Object identity matters, not string name                     │
│    Think: "Twins with same name are still different people"     │
│    Each Parameter() call creates NEW object                     │
│                                                                  │
│ 🎭 "c_if: Gate.Condition (gate first, if second)"               │
│    qc.x(1).c_if(0, 1) - gate method, then condition             │
│    NOT qc.c_if(...).x(...) - backwards!                         │
│    Think: "Do X, Check IF condition"                            │
│    Legacy API but still on exam!                                │
│                                                                  │
│ 🎯 "if_test needs Tuple (parentheses inside)"                    │
│    with qc.if_test((clbit, value)): - TUPLE required!           │
│    Think: "Tuple To test"                                       │
│    if_test((cr[0], 1)) NOT if_test(cr[0], 1)                    │
│    Modern API, replaces c_if()                                  │
│                                                                  │
│ 📏 "Register Value = Integer (not bit array)"                    │
│    cr == 3 means binary '11' (both bits set)                    │
│    Not individual bit values cr[0]=1, cr[1]=1                   │
│    Think: "Register = Right-to-left Integer"                    │
│    cr[0] is LSB (rightmost), cr[1] is next bit                  │
│                                                                  │
│ 🔧 "Measure BEFORE conditional (need value first)"               │
│    Must measure BEFORE c_if/if_test                             │
│    Think: "Measure, then Maybe execute"                         │
│    Condition needs measured value to evaluate                   │
│    No measurement = no condition value = error!                 │
│                                                                  │
│ 🏗️ "6-Stage Pipeline: ILRTOS"                                   │
│    Init → Layout → Routing → Translation → Optimization → Scheduling│
│    "I Love Routing Through Optimized Systems"                   │
│    Think: "Compiler Pipeline = 6 sequential stages"             │
│    Each stage builds on previous (order matters!)               │
│                                                                  │
│ 🔄 "SWAP = 3 CNOTs (remember the cost!)"                         │
│    Each SWAP inserted = 3 CNOT gates                            │
│    Minimize non-adjacent 2-qubit gates!                         │
│    Think: "SWAP = Super Wasteful (3x cost)"                     │
│    Good layout = fewer SWAPs = faster circuit                   │
│                                                                  │
│ 🎚️ "Level 0-3: None → Light → Medium → Heavy"                   │
│    Optimization level: 0=none, 1=light, 2=medium, 3=heavy       │
│    Higher = more optimization BUT slower compilation            │
│    Think: "Higher level = Heavier work"                         │
│    Level 0: TrivialLayout, Level 1+: SabreLayout                │
│    Level 3 doesn't always mean better results!                  │
│                                                                  │
│ ⏰ "ASAP/ALAP = Soon/Late (timing matters)"                      │
│    ASAP: As Soon As Possible (minimize idle at start)           │
│    ALAP: As Late As Possible (minimize idle at end)             │
│    Think: "ALAP = Almost Late = better for decoherence"         │
│    ALAP better: gates execute closer to measurement             │
│    Less time for decoherence to affect results                  │
│                                                                  │
│ 📍 "Layout = Location (which physical qubit?)"                   │
│    Layout maps logical qubits → physical qubits                 │
│    Think: "Layout = Location assignment"                        │
│    TrivialLayout: q[i]→i (simple, no optimization)              │
│    VF2Layout: Perfect graph matching (best but slow)            │
│    SabreLayout: Heuristic (good balance, default)               │
│    DenseLayout: Pack connected qubits together                  │
│                                                                  │
│ 🗺️ "Routing = Road-building (insert SWAPs)"                      │
│    Routing inserts SWAP gates for non-adjacent qubits           │
│    Think: "Routing = Roads between qubits"                      │
│    Needed when 2-qubit gate spans disconnected qubits           │
│    SabreSwap: Heuristic routing (default)                       │
│    StochasticSwap: Random search routing                        │
│                                                                  │
│ 🔀 "Translation = Transform to basis gates"                      │
│    Translation converts all gates to hardware basis             │
│    Think: "Translation = Transform Language"                    │
│    From logical gates → hardware-native gates                   │
│    Basis gates example: ['id','rz','sx','x','cx']               │
│                                                                  │
│ 🎨 "front=True → Prepend (add to front)"                         │
│    compose(qc2, front=True) adds qc2 BEFORE qc1                 │
│    front=False adds qc2 AFTER qc1 (default)                     │
│    Think: "front=True → Front of line"                          │
│    front parameter controls insertion position                  │
│                                                                  │
│ 🔑 "ParameterVector = Parallel Parameters"                       │
│    ParameterVector('θ', 5) creates θ[0] through θ[4]            │
│    Think: "Vector = array of indexed parameters"                │
│    Efficient for ansätze with many parameters                   │
│    All elements are separate Parameter objects                  │
│                                                                  │
│ 📊 "Parallel gates = One depth layer"                            │
│    Gates on different qubits execute simultaneously             │
│    H on q[0,1,2] = depth 1, not 3!                              │
│    Think: "Parallel = Same time = same layer"                   │
│    Sequential gates increase depth                              │
│                                                                  │
│ 🚫 "Barrier = Zero depth (just a hint)"                          │
│    Barrier gates don't add to circuit depth                     │
│    Think: "Barrier = Boundary marker (not an operation)"        │
│    Used for compiler hints, visualization                       │
│    No physical gate, no time cost                               │
│                                                                  │
│ 🔄 "inverse() = Reverse + Conjugate"                             │
│    qc.inverse() reverses order AND conjugates gates             │
│    Think: "inverse = Undo circuit (reverse time)"               │
│    U†: reverse gate order + take gate adjoint                   │
│    Useful for uncomputing, QFT† patterns                        │
│                                                                  │
│ 📚 "Library circuits = Logical (need transpile)"                 │
│    Circuit library gates not hardware-ready yet                 │
│    Think: "Library = blueprint (not built yet)"                 │
│    Must transpile before running on backend                     │
│    QFT, RealAmplitudes, EfficientSU2 all need transpilation     │
│                                                                  │
│ 🎯 "RealAmplitudes = Real only (no complex phase)"               │
│    RealAmplitudes ansatz has only real amplitudes               │
│    Think: "Real = no imaginary part"                            │
│    Uses RY rotations (real), not general rotations              │
│    Less expressive but hardware-efficient                       │
│                                                                  │
│ ⚡ "EfficientSU2 = Efficient for hardware"                        │
│    EfficientSU2 optimized for hardware basis gates              │
│    Think: "Efficient = Easy for hardware"                       │
│    Uses RY + RZ (both in basis sets)                            │
│    Covers full SU(2) single-qubit space                         │
│                                                                  │
│ 🎛️ "TwoLocal = Tunable (rotation + entanglement)"               │
│    TwoLocal lets you customize rotation and entanglement        │
│    Think: "Two = Two types (rotation + entangle)"               │
│    Specify rotation_blocks and entanglement_blocks              │
│    Most flexible ansatz template                                │
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
║  🏗️ CIRCUIT CREATION FUNDAMENTALS                                      ║
║  ├─ BASIC CREATION                                                     ║
║  │  ├─ QuantumCircuit(n_qubits, n_clbits) - Q before C! (trap!)      ║
║  │  ├─ QuantumCircuit(3, 2) = 3 qubits, 2 classical bits              ║
║  │  ├─ QuantumCircuit(qr, cr) - with named registers                  ║
║  │  ├─ qr = QuantumRegister(5, 'q') named quantum register            ║
║  │  ├─ cr = ClassicalRegister(5, 'c') named classical register        ║
║  │  └─ All qubits initialize to |0⟩ (cannot specify initial state)    ║
║  ├─ REGISTER MANAGEMENT                                                ║
║  │  ├─ qc.add_register(qr) adds register to existing circuit          ║
║  │  ├─ qc.qubits returns list of Qubit objects                        ║
║  │  ├─ qc.clbits returns list of Clbit objects                        ║
║  │  ├─ qc.qregs returns list of QuantumRegister objects               ║
║  │  └─ qc.cregs returns list of ClassicalRegister objects             ║
║  └─ CIRCUIT METADATA                                                   ║
║     ├─ qc.name = 'my_circuit' sets circuit name                       ║
║     ├─ qc.global_phase = np.pi/4 sets global phase                    ║
║     └─ qc.metadata = {'key': 'value'} attaches metadata               ║
║                                                                        ║
║  📏 CIRCUIT PROPERTIES & METRICS                                       ║
║  ├─ METHODS (require parentheses!)                                     ║
║  │  ├─ depth() = longest path through circuit (critical path)         ║
║  │  │   └─ Includes measurements, barriers count as 0                 ║
║  │  │   └─ Parallel gates share ONE layer (same depth)                ║
║  │  ├─ size() = total operation count (gates + measurements)          ║
║  │  │   └─ Counts all instructions including barriers                 ║
║  │  ├─ width() = total wires (num_qubits + num_clbits)                ║
║  │  └─ count_ops() = dict of gate types {'h': 2, 'cx': 3}             ║
║  │      └─ Does NOT include parameter values                          ║
║  ├─ PROPERTIES (NO parentheses!)                                       ║
║  │  ├─ num_qubits = qubit count (TRAP: no parentheses!)               ║
║  │  ├─ num_clbits = classical bit count (TRAP: no parentheses!)       ║
║  │  └─ num_parameters = unbound parameter count (property)            ║
║  └─ CIRCUIT MANIPULATION                                               ║
║     ├─ qc.decompose() breaks down complex gates                       ║
║     ├─ qc.inverse() returns circuit inverse (reverse + conjugate)     ║
║     ├─ qc.copy() creates deep copy                                    ║
║     ├─ qc.clear() removes all instructions                            ║
║     └─ qc.remove_final_measurements() removes end measurements        ║
║                                                                        ║
║  🔗 COMPOSITION & COMBINATION                                          ║
║  ├─ COMPOSE (Sequential - SAME qubits)                                 ║
║  │  ├─ result = qc1.compose(qc2) sequential combination               ║
║  │  ├─ qc1.compose(qc2, inplace=True) modifies qc1 directly           ║
║  │  ├─ qc1.compose(qc2, qubits=[2,3]) maps to specific qubits         ║
║  │  ├─ qc1.compose(qc2, front=True) prepends qc2 before qc1           ║
║  │  ├─ Width unchanged (uses existing qubits)                         ║
║  │  └─ TRAP: compose() returns NEW circuit (default inplace=False)    ║
║  ├─ TENSOR (Parallel - ADDS qubits)                                    ║
║  │  ├─ result = qc1.tensor(qc2) parallel combination (qc1 ⊗ qc2)      ║
║  │  ├─ qc1.tensor(qc2, inplace=True) modifies qc1 directly            ║
║  │  ├─ Width increases (adds qc2.num_qubits + qc2.num_clbits)         ║
║  │  ├─ Creates independent subsystems (no interaction)                ║
║  │  └─ qc2's qubits added after qc1's qubits                          ║
║  └─ APPEND (Single operation)                                          ║
║     ├─ qc.append(gate, [qubits]) adds single gate                     ║
║     ├─ TRAP: qubits must be LIST even for single qubit!               ║
║     ├─ qc.append(HGate(), [0]) correct syntax                         ║
║     ├─ qc.append(CXGate(), [0, 1]) two-qubit gate                     ║
║     └─ append() modifies in place (returns None)                      ║
║                                                                        ║
║  🎛️ PARAMETERIZED CIRCUITS                                             ║
║  ├─ PARAMETER CREATION                                                 ║
║  │  ├─ theta = Parameter('θ') creates symbolic parameter              ║
║  │  ├─ params = ParameterVector('θ', n) creates θ[0]...θ[n-1]         ║
║  │  ├─ TRAP: Parameter('θ') twice = TWO different objects!            ║
║  │  └─ Object identity matters, not name equality                     ║
║  ├─ PARAMETER USAGE                                                    ║
║  │  ├─ qc.rx(theta, 0) gate with parameter                            ║
║  │  ├─ qc.ry(2*theta, 0) parameter expressions allowed                ║
║  │  ├─ qc.rz(theta + phi, 0) combine parameters                       ║
║  │  └─ Complex expressions: sin(theta), cos(phi), theta**2            ║
║  ├─ PARAMETER BINDING                                                  ║
║  │  ├─ bound = qc.assign_parameters({theta: 0.5}) bind single         ║
║  │  ├─ bound = qc.assign_parameters({params: [0.1, 0.2, ...]})        ║
║  │  ├─ bound = qc.assign_parameters(values, inplace=False) default    ║
║  │  ├─ Partial binding allowed (bind subset of parameters)            ║
║  │  ├─ TRAP: bind_parameters() is DEPRECATED!                         ║
║  │  └─ Must bind before execution (hardware needs concrete values)    ║
║  └─ PARAMETER INSPECTION                                               ║
║     ├─ qc.parameters returns ParameterView (set-like)                 ║
║     ├─ len(qc.parameters) counts unbound parameters                   ║
║     ├─ len(qc.parameters) == 0 means fully bound                      ║
║     └─ Used for VQE, QAOA, variational algorithms                     ║
║                                                                        ║
║  🔀 CLASSICAL CONTROL (LEGACY c_if)                                    ║
║  ├─ SYNTAX & USAGE                                                     ║
║  │  ├─ qc.x(1).c_if(cr[0], 1) - gate FIRST, condition second          ║
║  │  ├─ TRAP: qc.c_if(0,1).x(1) WRONG ORDER!                           ║
║  │  ├─ qc.h(0).c_if(cr, 3) register comparison (cr==3)                ║
║  │  └─ Must measure BEFORE c_if (condition needs value)               ║
║  ├─ REGISTER INTERPRETATION                                            ║
║  │  ├─ Register value is INTEGER (binary representation)              ║
║  │  ├─ cr==3 means binary '11' (both bits set)                        ║
║  │  ├─ cr[0] is LSB (least significant bit)                           ║
║  │  └─ Little-endian bit ordering                                     ║
║  └─ STATUS                                                             ║
║     ├─ c_if() is LEGACY (deprecated but exam-relevant!)               ║
║     └─ Replaced by modern if_test() API                               ║
║                                                                        ║
║  🔀 CLASSICAL CONTROL (MODERN if_test)                                 ║
║  ├─ BASIC IF                                                           ║
║  │  ├─ from qiskit.circuit.classical import expr                      ║
║  │  ├─ with qc.if_test((cr[0], 1)): - TUPLE required!                 ║
║  │  │      qc.x(1) - operations in if block                           ║
║  │  ├─ TRAP: if_test(cr[0], 1) without tuple → ERROR!                 ║
║  │  └─ with qc.if_test((cr, 3)): register comparison                  ║
║  ├─ IF-ELSE                                                            ║
║  │  ├─ with qc.if_test((cr[0], 1)) as else_:                          ║
║  │  │      qc.x(1) - if branch                                        ║
║  │  ├─ with else_: - else block                                       ║
║  │  │      qc.h(1) - else branch                                      ║
║  │  └─ TRAP: Need 'as else_:' syntax for else block!                  ║
║  └─ COMPLEX CONDITIONS                                                 ║
║     ├─ condition = expr.logic_and(cr[0], cr[1]) AND                   ║
║     ├─ condition = expr.logic_or(cr[0], cr[1]) OR                     ║
║     ├─ condition = expr.logic_not(cr[0]) NOT                          ║
║     ├─ condition = expr.equal(cr, 5) equality                         ║
║     ├─ condition = expr.less(cr, 10) less than                        ║
║     └─ with qc.if_test(condition): use complex condition              ║
║                                                                        ║
║  🔁 DYNAMIC CIRCUITS (Control Flow)                                    ║
║  ├─ FOR LOOPS                                                          ║
║  │  ├─ with qc.for_loop(range(5)): fixed iterations                   ║
║  │  │      qc.h(0) - repeated 5 times                                 ║
║  │  ├─ with qc.for_loop(range(3)) as i: loop variable                 ║
║  │  │      qc.rx(i*0.1, 0) - use loop index                           ║
║  │  └─ TRAP: for_loop(5) wrong! Need range(5)                         ║
║  ├─ WHILE LOOPS                                                        ║
║  │  ├─ with qc.while_loop((cr[0], 0)): - TUPLE required               ║
║  │  │      qc.h(0)                                                    ║
║  │  │      qc.measure(0, 0) - re-measure in loop!                     ║
║  │  └─ TRAP: Must re-measure to update condition                      ║
║  ├─ SWITCH STATEMENTS                                                  ║
║  │  ├─ with qc.switch(cr) as case: multi-way branch                   ║
║  │  │      with case(0): qc.x(0) - case 0                             ║
║  │  │      with case(1): qc.h(0) - case 1                             ║
║  │  │      with case(case.DEFAULT): qc.reset(0) - default             ║
║  │  ├─ qc.break_loop() exit loop early                                ║
║  │  └─ qc.continue_loop() skip to next iteration                      ║
║  └─ CONSTRAINTS                                                        ║
║     ├─ Dynamic circuits require hardware support                      ║
║     ├─ Not all backends support dynamic circuits                      ║
║     └─ Enable adaptive algorithms and feedback                        ║
║                                                                        ║
║  📚 CIRCUIT LIBRARY (Pre-built Circuits)                               ║
║  ├─ QUANTUM FOURIER TRANSFORM                                          ║
║  │  ├─ from qiskit.circuit.library import QFT                         ║
║  │  ├─ qft = QFT(num_qubits=4) create 4-qubit QFT                     ║
║  │  ├─ qft = QFT(4, do_swaps=True) with bit reversal (default)        ║
║  │  ├─ qft_inverse = qft.inverse() inverse QFT (QFT†)                 ║
║  │  └─ qc.append(qft, range(4)) append to circuit                     ║
║  ├─ VQE ANSÄTZE                                                        ║
║  │  ├─ RealAmplitudes(n, reps=k) - real amplitudes only               ║
║  │  │   └─ Uses RY rotations + CNOT entanglement                      ║
║  │  ├─ EfficientSU2(n, reps=k) - hardware-efficient                   ║
║  │  │   └─ Uses RY + RZ rotations (covers full SU(2))                 ║
║  │  ├─ TwoLocal(n, rotation, entanglement, reps) - customizable       ║
║  │  │   └─ Specify rotation and entanglement blocks                   ║
║  │  └─ NLocal - generalizes to N-qubit gates                          ║
║  ├─ FEATURE MAPS                                                       ║
║  │  ├─ PauliFeatureMap(feature_dimension, reps) - Pauli encoding      ║
║  │  └─ ZFeatureMap(feature_dimension, reps) - Z-rotation encoding     ║
║  └─ LIBRARY CIRCUIT PROPERTIES                                         ║
║     ├─ TRAP: Library circuits are LOGICAL (need transpilation!)       ║
║     ├─ Most are parameterized (must bind before execution)            ║
║     ├─ ansatz.num_parameters shows parameter count                    ║
║     ├─ Compose with regular circuits normally                         ║
║     └─ Optimized for specific use cases (VQE, QAOA, etc.)             ║
║                                                                        ║
║  🔧 TRANSPILER PIPELINE (6 Stages: ILRTOS)                             ║
║  ├─ STAGE 1: INIT (Decomposition)                                      ║
║  │  ├─ Decomposes 3+ qubit gates into 2-qubit gates                   ║
║  │  ├─ Unroll3qOrMore pass breaks down complex gates                  ║
║  │  └─ Ensures max 2-qubit gates for routing stage                    ║
║  ├─ STAGE 2: LAYOUT (Logical→Physical Mapping)                         ║
║  │  ├─ Maps logical qubits to physical hardware qubits                ║
║  │  ├─ TrivialLayout: q[i]→i (simple, no optimization)                ║
║  │  ├─ VF2Layout: Perfect graph matching (best but slow/may fail)     ║
║  │  ├─ SabreLayout: Heuristic (default, good balance)                 ║
║  │  ├─ DenseLayout: Pack connected qubits together                    ║
║  │  └─ Good layout → fewer SWAPs → better performance                 ║
║  ├─ STAGE 3: ROUTING (SWAP Insertion)                                  ║
║  │  ├─ Inserts SWAP gates for non-adjacent 2-qubit gates              ║
║  │  ├─ TRAP: Each SWAP = 3 CNOT gates! (expensive!)                   ║
║  │  ├─ SabreSwap: Heuristic routing (default, generally good)         ║
║  │  ├─ StochasticSwap: Random search with scoring (alternative)       ║
║  │  ├─ Routing is NP-hard (heuristics may not be optimal)             ║
║  │  └─ Coupling map defines allowed 2-qubit interactions              ║
║  ├─ STAGE 4: TRANSLATION (Basis Gate Conversion)                       ║
║  │  ├─ Converts all gates to hardware basis gates                     ║
║  │  ├─ BasisTranslator pass handles conversion                        ║
║  │  ├─ Example basis: ['id','rz','sx','x','cx']                       ║
║  │  ├─ Some gates decompose into multiple basis gates                 ║
║  │  └─ Must specify valid basis gates for target hardware             ║
║  ├─ STAGE 5: OPTIMIZATION (Gate Reduction)                             ║
║  │  ├─ Level 0: No optimization (TrivialLayout, minimal passes)       ║
║  │  ├─ Level 1: Light optimization (basic passes)                     ║
║  │  ├─ Level 2: Medium optimization (default, balanced)               ║
║  │  ├─ Level 3: Heavy optimization (unitary synthesis, slow)          ║
║  │  ├─ Higher level = more compilation time                           ║
║  │  ├─ TRAP: Level 3 ≠ always better! (diminishing returns)           ║
║  │  └─ Passes: gate cancellation, commutation, resynthesis            ║
║  ├─ STAGE 6: SCHEDULING (Timing Information)                           ║
║  │  ├─ Adds pulse-level timing to circuit                             ║
║  │  ├─ ASAP: As Soon As Possible (minimize idle at start)             ║
║  │  ├─ ALAP: As Late As Possible (minimize idle before measure)       ║
║  │  ├─ TRAP: ALAP better for decoherence! (gates closer to measure)   ║
║  │  ├─ Scheduled circuits include Delay instructions                  ║
║  │  └─ Delay = idle time (no gates executing)                         ║
║  └─ TRANSPILER USAGE                                                   ║
║     ├─ from qiskit.transpiler.preset_passmanagers import generate_... ║
║     ├─ pm = generate_preset_pass_manager(level, backend)              ║
║     ├─ transpiled = pm.run(qc) execute transpilation                  ║
║     ├─ TRAP: Backend REQUIRED for realistic results!                  ║
║     ├─ Backend provides: coupling map, basis gates, timing            ║
║     ├─ seed_transpiler=42 for reproducibility                         ║
║     └─ Transpiled circuit usually has GREATER depth (SWAPs!)          ║
║                                                                        ║
║  ⚠️⚠️⚠️ TOP 15 EXAM TRAPS - MEMORIZE THESE! ⚠️⚠️⚠️                        ║
║  1.  QuantumCircuit(2,3) = 2 QUBITS, 3 CLASSICAL! (Q before C)        ║
║  2.  num_qubits is PROPERTY (no ()), depth() is METHOD (with ())      ║
║  3.  compose() = SAME qubits, tensor() = ADDS qubits                  ║
║  4.  compose() returns NEW circuit (default inplace=False)            ║
║  5.  qc.append(HGate(), [0]) needs LIST even for single qubit!        ║
║  6.  Parameter('θ') twice creates TWO different parameter objects!    ║
║  7.  qc.x(1).c_if(0,1) NOT qc.c_if(0,1).x(1) - gate FIRST!           ║
║  8.  if_test needs TUPLE: (clbit, value) not clbit, value             ║
║  9.  c_if register value is INTEGER: cr==3 means binary '11'          ║
║  10. Must measure BEFORE conditionals (c_if/if_test need value!)      ║
║  11. SWAP = 3 CNOT gates! (routing is VERY expensive)                 ║
║  12. bind_parameters() DEPRECATED → use assign_parameters()           ║
║  13. Transpiler needs backend for realistic results (coupling + basis)║
║  14. ALAP scheduling better than ASAP (minimize decoherence)          ║
║  15. Parallel gates = ONE depth layer (H on q[0,1,2] = depth 1!)      ║
║                                                                        ║
║  🎯 QUICK DECISION GUIDE                                               ║
║  Combining circuits sequentially? → compose() (same qubits)           ║
║  Combining circuits in parallel? → tensor() (adds qubits)             ║
║  Need symbolic gate angles? → Parameter() and assign_parameters()     ║
║  Legacy conditionals? → gate.c_if(clbit, value)                       ║
║  Modern conditionals? → with qc.if_test((clbit, value)):              ║
║  Need pre-built circuits? → Circuit library (QFT, ansätze)            ║
║  Compiling for hardware? → Transpiler with backend                    ║
║  Checking properties? → Remember: num_qubits (no ()), depth() (with ())║
║                                                                        ║
║  💡 CRITICAL CONCEPT SUMMARY                                           ║
║  ├─ Properties vs Methods: Know which use () and which don't!         ║
║  ├─ compose vs tensor: Same qubits vs adding qubits                   ║
║  ├─ Parameter identity: Object matters, not name string               ║
║  ├─ c_if vs if_test: Legacy vs modern (know both!)                    ║
║  ├─ Transpiler: 6-stage pipeline (ILRTOS mnemonic)                    ║
║  ├─ SWAP cost: 3 CNOTs per SWAP (expensive!)                          ║
║  └─ Circuit library: Logical circuits (transpile before running)      ║
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
