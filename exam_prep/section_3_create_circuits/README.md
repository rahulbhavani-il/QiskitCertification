# Section 3: Create Circuits (18% of Exam - HIGHEST WEIGHT!)

> **Exam Weight**: ~12 questions | **Difficulty**: Medium | **Must Master**: ✅✅✅

---

## 📖 Overview

This is the **MOST IMPORTANT SECTION** for the certification exam! Understanding circuit creation, composition, and manipulation is absolutely critical.

### What You'll Learn

1. **Circuit Basics**: Creating circuits, properties, registers
2. **Circuit Composition**: `compose()`, `append()`, `tensor()`
3. **Parameterized Circuits**: `Parameter`, `bind_parameters()`
4. **Circuit Library**: Standard gates and pre-built circuits
5. **Classical Control**: Conditional operations with `c_if()`

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

## 📖 Detailed Term Definitions

### 1. Circuit Basics

**Definition**: The foundational concepts for creating and understanding quantum circuits in Qiskit.

**Key Components**:

- **QuantumCircuit**: The primary object representing a quantum computation
  - Contains quantum gates, measurements, and classical operations
  - Created with `QuantumCircuit(n_qubits, n_clbits)`
  - Example: `qc = QuantumCircuit(3, 3)` creates 3 qubits and 3 classical bits

- **Properties**: Measurable characteristics of a circuit
  - `depth()`: The critical path length (longest sequential chain of operations)
  - `size()`: Total count of all gates/operations in the circuit
  - `width()`: Total number of wires (qubits + classical bits)
  - `num_qubits`: Number of quantum bits (property, no parentheses)
  - `num_clbits`: Number of classical bits (property, no parentheses)

- **Registers**: Named collections of qubits or classical bits
  - `QuantumRegister(n, 'name')`: Group of n qubits with a label
  - `ClassicalRegister(n, 'name')`: Group of n classical bits with a label
  - Used for logical organization in complex circuits

**Importance**:
- **Foundation of quantum programming**: Every quantum algorithm starts with circuit creation
- **Exam critical**: Circuit properties (depth, size, width) are frequently tested
- **Organization**: Registers help manage complex multi-qubit systems
- **Debugging**: Understanding properties helps optimize circuit performance

**Example Comparison**:
```python
# Method 1: Simple (no registers)
qc1 = QuantumCircuit(3, 3)

# Method 2: With registers (better organization)
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc2 = QuantumCircuit(qr, cr)

# Both create identical circuits, but qc2 has named components
```

---

### 2. Circuit Composition

**Definition**: Methods for combining multiple quantum circuits into larger, more complex circuits.

**Key Methods**:

#### `compose()`
- **Definition**: Appends one circuit to another sequentially (one after the other)
- **Syntax**: `qc1.compose(qc2, qubits=[...], front=False, inplace=False)`
- **Behavior**: Adds qc2's operations after qc1's operations (by default)
- **Use case**: Building circuits step-by-step, adding layers to existing circuits

#### `append()`
- **Definition**: Adds a single gate or instruction to a circuit
- **Syntax**: `qc.append(gate, qubits, clbits)`
- **Behavior**: Inserts one operation at the end of the circuit
- **Use case**: Adding individual gates, custom gates, or library circuits as single operations

#### `tensor()`
- **Definition**: Combines circuits side-by-side (tensor product, parallel systems)
- **Syntax**: `qc1.tensor(qc2)`
- **Behavior**: Creates a new circuit with qc1's qubits + qc2's qubits (independent systems)
- **Use case**: Combining separate quantum systems that don't interact

**Importance**:
- **Modularity**: Build complex circuits from simple components
- **Reusability**: Create sub-circuits once, use multiple times
- **Exam critical**: Understanding differences between compose/append/tensor is frequently tested
- **Circuit design**: Essential for variational algorithms (VQE, QAOA)

**Key Differences**:

| Feature | `compose()` | `append()` | `tensor()` |
|---------|------------|-----------|-----------|
| **Purpose** | Merge circuits sequentially | Add single operation | Combine independent systems |
| **Qubits** | Can target specific qubits | Targets specified qubits | Adds new qubits |
| **Order** | Sequential (→) | Sequential (→) | Parallel (⊗) |
| **Result** | Operations happen one after another | One gate added to end | Two separate systems combined |
| **Width change** | No change (uses same qubits) | No change | Increases (adds qubits) |

**Visual Comparison**:
```
compose():  [Circuit A]→[Circuit B]  (sequential execution)
append():   [Circuit]→[Gate]         (add one operation)
tensor():   [Circuit A] ⊗ [Circuit B] (parallel systems)
            (separate qubit spaces)
```

**Exam Trap Example**:
```python
qc1 = QuantumCircuit(2)
qc2 = QuantumCircuit(2)
qc1.h([0, 1])
qc2.x([0, 1])

# compose: 2 qubits (H then X on same qubits)
result1 = qc1.compose(qc2)  # width = 2

# tensor: 4 qubits (H on first 2, X on last 2)
result2 = qc1.tensor(qc2)   # width = 4

print(f"compose width: {result1.width()}")  # 2
print(f"tensor width: {result2.width()}")   # 4
```

---

### 3. Parameterized Circuits

**Definition**: Quantum circuits containing symbolic parameters (variables) instead of fixed numerical values, enabling optimization and variational algorithms.

**Key Components**:

#### `Parameter`
- **Definition**: A symbolic variable representing an unbound angle or value
- **Syntax**: `theta = Parameter('θ')`
- **Behavior**: Acts as a placeholder until bound to a concrete value
- **Use case**: Creating flexible circuits for optimization algorithms

#### `ParameterVector`
- **Definition**: An array of multiple parameters
- **Syntax**: `params = ParameterVector('θ', length)`
- **Behavior**: Creates θ[0], θ[1], ..., θ[n-1]
- **Use case**: Managing many parameters efficiently in deep circuits

#### `bind_parameters()` / `assign_parameters()`
- **Definition**: Replace symbolic parameters with numerical values
- **Syntax**: `bound_qc = qc.assign_parameters({theta: 0.5})`
- **Behavior**: Creates a new circuit with parameters replaced by values
- **Difference**: `assign_parameters()` is newer API, `bind_parameters()` is older (deprecated but still works)

**Importance**:
- **Variational algorithms**: Essential for VQE (Variational Quantum Eigensolver) and QAOA
- **Optimization**: Allows classical optimizer to tune quantum circuit parameters
- **Flexibility**: One circuit template can generate infinite variations
- **Industry standard**: Used in all production quantum machine learning and chemistry applications
- **Exam critical**: Parameter binding patterns appear in VQE/QAOA questions

**Workflow Example**:
```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Step 1: Create parameterized circuit
theta = Parameter('θ')
phi = Parameter('φ')

qc = QuantumCircuit(1)
qc.ry(theta, 0)  # Rotation by θ (unbound)
qc.rz(phi, 0)    # Rotation by φ (unbound)

print(qc.parameters)  # {Parameter(θ), Parameter(φ)}

# Step 2: Bind to specific values
bound = qc.assign_parameters({theta: 0.5, phi: 1.2})

print(bound.parameters)  # set() - empty, all bound!

# Step 3: Use in optimization loop (VQE pattern)
import numpy as np
for iteration in range(10):
    values = np.random.random(2)  # Optimizer provides values
    circuit = qc.assign_parameters({theta: values[0], phi: values[1]})
    # Execute circuit, measure energy, update parameters...
```

**Key Differences**:

| Aspect | Parameterized Circuit | Fixed Circuit |
|--------|----------------------|---------------|
| **Flexibility** | Infinite variations from one template | Single fixed computation |
| **Execution** | Must bind before running | Ready to run immediately |
| **Use case** | Optimization, machine learning | Standard algorithms |
| **Memory** | One circuit, many evaluations | Need separate circuit for each variation |

---

### 4. Circuit Library

**Definition**: Pre-built, tested quantum circuits and gates provided by Qiskit for common operations and algorithms.

**Key Components**:

#### Standard Gates
- **Definition**: Single or multi-qubit gates available as objects
- **Examples**: `XGate()`, `HGate()`, `CXGate()`, `CCXGate()` (Toffoli)
- **Usage**: `qc.append(HGate(), [0])`
- **Benefit**: Explicit gate objects for programmatic circuit construction

#### Standard Circuits
- **Definition**: Complex multi-qubit circuits for common algorithms
- **Examples**:
  - `QFT(n)`: Quantum Fourier Transform on n qubits
  - `QAOAAnsatz(problem, reps)`: QAOA circuit for optimization
  - `RealAmplitudes(n, reps)`: Variational ansatz for VQE
  - `EfficientSU2(n, reps)`: Hardware-efficient variational circuit
  - `GroverOperator(oracle)`: Grover search iteration
  - `PauliEvolutionGate(operator, time)`: Hamiltonian time evolution

#### Pre-built Ansätze
- **Definition**: Variational circuit templates with parameterized gates
- **Purpose**: Starting point for VQE, QAOA, and quantum machine learning
- **Benefit**: Proven circuit structures optimized for specific hardware

**Importance**:
- **Saves time**: Don't reinvent the wheel for common operations
- **Tested code**: Library circuits are thoroughly validated
- **Best practices**: Implementations follow quantum computing standards
- **Hardware optimization**: Some circuits (EfficientSU2) designed for real quantum hardware
- **Exam relevant**: Knowing when to use QFT, standard ansätze is tested
- **Research accelerator**: Build complex algorithms faster

**Key Differences**:

| Type | Purpose | Parameterized? | Example |
|------|---------|----------------|---------|
| **Standard Gates** | Basic operations | No | `HGate()`, `CXGate()` |
| **Standard Circuits** | Complete algorithms | Sometimes | `QFT(4)` |
| **Variational Ansätze** | Optimization templates | Yes (always) | `RealAmplitudes(4, reps=3)` |

**Example Comparison**:
```python
from qiskit.circuit.library import QFT, RealAmplitudes, HGate

# Manual QFT (complex, error-prone)
def manual_qft(n):
    qc = QuantumCircuit(n)
    # ... 50+ lines of swap and controlled-rotation gates
    return qc

# Library QFT (simple, correct)
qft = QFT(4)

# Manual ansatz (tedious)
def manual_ansatz(n, depth):
    qc = QuantumCircuit(n)
    # ... many lines of parameterized gates
    return qc

# Library ansatz (one line!)
ansatz = RealAmplitudes(4, reps=3)
print(f"Parameters: {len(ansatz.parameters)}")  # Automatic
```

---

### 5. Classical Control

**Definition**: Techniques for making quantum operations conditional on classical measurement results during circuit execution.

**Key Components**:

#### `c_if()`
- **Definition**: Execute a quantum gate only if a classical bit (or register) has a specific value
- **Syntax**: `qc.gate(qubit).c_if(classical_bit, value)`
- **Behavior**: Gate applies only when condition is true
- **Execution**: Happens during circuit runtime (dynamic decision)

#### Conditional Operations
- **Single bit condition**: `qc.x(1).c_if(0, 1)` - Apply X if classical bit 0 is 1
- **Register condition**: `qc.z(2).c_if(cr, 3)` - Apply Z if classical register equals 3 (binary '11')
- **Multiple conditions**: Chain measurements and conditionals for complex logic

**Importance**:
- **Quantum error correction**: Essential for real-time error syndrome measurement and correction
- **Adaptive algorithms**: Enable circuits that respond to intermediate results
- **Quantum teleportation**: Classic example requiring conditional X and Z gates
- **Real hardware**: Modern quantum computers support dynamic circuits with mid-circuit measurement
- **Exam relevance**: Teleportation and conditional operations appear in certification questions
- **Future of QC**: Dynamic circuits are the foundation of fault-tolerant quantum computing

**How It Works**:
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)

# Step 1: Create superposition and measure
qc.h(0)
qc.measure(0, 0)  # Result stored in classical bit 0

# Step 2: Conditional operation (happens AFTER measurement)
qc.x(1).c_if(0, 1)  # "If c[0]==1, apply X to qubit 1"

# Step 3: Final measurement
qc.measure(1, 1)

# Execution flow:
# - Measure qubit 0 → get 0 or 1 → store in c[0]
# - Check c[0]: if 1, apply X to qubit 1; if 0, do nothing
# - Measure qubit 1 → get final result
```

**Key Differences from Regular Operations**:

| Aspect | Regular Gate | Conditional Gate (c_if) |
|--------|-------------|-------------------------|
| **Execution** | Always executes | Executes only if condition true |
| **Timing** | Before measurement | After measurement |
| **Dependencies** | None | Depends on classical bit value |
| **Hardware** | All devices support | Requires dynamic circuit support |
| **Use case** | Standard algorithms | Error correction, teleportation |

**Common Patterns**:

1. **Quantum Teleportation**:
```python
# Measure Bell pair, conditionally correct
qc.measure([0, 1], [0, 1])
qc.x(2).c_if(1, 1)  # Bit flip correction
qc.z(2).c_if(0, 1)  # Phase flip correction
```

2. **Error Correction**:
```python
# Measure syndrome, conditionally fix error
qc.measure(ancilla, syndrome)
qc.x(data_qubit).c_if(syndrome, 1)  # Correct detected error
```

3. **Adaptive Algorithm**:
```python
# Measure intermediate result, adjust next step
qc.measure(0, 0)
qc.ry(theta, 1).c_if(0, 1)  # Different rotation based on measurement
```

**Modern Alternative**: In Qiskit 1.0+, `c_if()` is being replaced by more powerful control flow:
- `if_test()`: If-else blocks
- `while_loop()`: Loops based on conditions
- `for_loop()`: Counted loops
- These are covered in Section 9 (Dynamic Circuits)

---

## 🔗 Relationships Between Concepts

**How They Work Together**:

1. **Circuit Basics** → Foundation for everything
2. **Circuit Composition** → Combine basic circuits into complex algorithms
3. **Parameterized Circuits** → Make composed circuits flexible for optimization
4. **Circuit Library** → Pre-built components to compose
5. **Classical Control** → Add runtime decision-making to composed circuits

**Typical Workflow**:
```python
# 1. Circuit Basics: Create structure
qc = QuantumCircuit(4, 4)

# 2. Circuit Library: Add pre-built components
from qiskit.circuit.library import QFT
qc.append(QFT(4), range(4))

# 3. Parameterized Circuits: Add variational layer
from qiskit.circuit import Parameter
theta = Parameter('θ')
qc.ry(theta, 0)

# 4. Circuit Composition: Combine with another circuit
prep_circuit = QuantumCircuit(4)
prep_circuit.h(range(4))
full_circuit = prep_circuit.compose(qc)

# 5. Classical Control: Add conditional operations
full_circuit.measure(0, 0)
full_circuit.x(1).c_if(0, 1)

# Now you have a complete, sophisticated quantum algorithm!
```

---

## 🎯 Core Concepts

### 🧠 Conceptual Deep Dive

#### Analogy: The Recipe
Building a `QuantumCircuit` is like writing a recipe.
- **Ingredients**: Qubits and Classical Bits.
- **Instructions**: Gates (Hadamard, CNOT, Measure).
- **Cookware**: Registers (QuantumRegister, ClassicalRegister).
- **Cooking Time**: Circuit Depth (how long the longest parallel step takes).
- **Kitchen Space**: Circuit Width (how many qubits you need).

#### Depth vs. Size
- **Size**: Total number of operations. (How much work you do).
- **Depth**: The longest path from input to output. (How long it takes).
- *Example*: If you have 10 friends (qubits) chopping 10 onions (gates) simultaneously, the **size** is 10, but the **depth** is 1 (since they happen at the same time).

### The QuantumCircuit Object

```python
from qiskit import QuantumCircuit

# Most common: n qubits, m classical bits
qc = QuantumCircuit(n_qubits, n_classical_bits)

# Example: 3 qubits, 3 classical bits
qc = QuantumCircuit(3, 3)
```

**Visual Representation**:
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

---

## 🏗️ Circuit Creation Methods

### Method 1: Simple Creation

```python
from qiskit import QuantumCircuit

# Just qubits (no classical bits)
qc = QuantumCircuit(2)

# Qubits + classical bits
qc = QuantumCircuit(2, 2)
```

### Method 2: Using Registers

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Named registers
qr = QuantumRegister(3, 'q')   # 3 qubits named 'q'
cr = ClassicalRegister(3, 'c')  # 3 classical bits named 'c'

qc = QuantumCircuit(qr, cr)
```

**Why use registers?**
- Better organization for complex circuits
- Named registers improve readability
- Multiple registers for logical grouping

### Method 3: Multiple Registers

```python
# Separate logical units
data_qubits = QuantumRegister(4, 'data')
ancilla_qubits = QuantumRegister(2, 'ancilla')
measurements = ClassicalRegister(4, 'meas')
syndrome = ClassicalRegister(2, 'syndrome')

qc = QuantumCircuit(data_qubits, ancilla_qubits, measurements, syndrome)
```

**Visual**:
```
         ┌──────────┐
data_0: ─┤          ├─
data_1: ─┤   Data   ├─
data_2: ─┤  Qubits  ├─
data_3: ─┤          ├─
         └──────────┘
         ┌──────────┐
ancilla_0:┤  Ancilla ├─
ancilla_1:┤  Qubits  ├─
         └──────────┘
meas: 4/═══════════════
syndrome: 2/═══════════
```

---

## 📏 Circuit Properties (EXAM CRITICAL!)

### Essential Properties

```python
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

# EXAM TESTED:
print(f"Depth: {qc.depth()}")        # Critical path length
print(f"Size: {qc.size()}")          # Total gate count
print(f"Width: {qc.width()}")        # Total qubits + classical bits
print(f"Qubits: {qc.num_qubits}")    # Number of qubits
print(f"Clbits: {qc.num_clbits}")    # Number of classical bits
print(f"Operations: {qc.count_ops()}")  # Gate count by type
```

### Understanding Depth vs Size

```
Circuit:
     ┌───┐          
q_0: ┤ H ├──■───────  Layer 1: H
     └───┘┌─┴─┐      Layer 2: CX(0,1)
q_1: ─────┤ X ├──■──  Layer 3: CX(1,2)
          └───┘┌─┴─┐  Layer 4: Measurement
q_2: ──────────┤ X ├  
               └───┘  

Depth = 4  (longest path: q0 → H → CX → wait → M)
Size = 4   (total gates: 1 H + 2 CX + 3 M = 6, but measurements often excluded)
Width = 6  (3 qubits + 3 classical bits)

EXAM TIP: Depth ≠ Size!
- Depth = critical path (sequential operations)
- Size = total operation count
```

**Parallel Operations Don't Add Depth**:

```python
# Two operations in parallel
qc = QuantumCircuit(2)
qc.h(0)  # Layer 1
qc.h(1)  # Also Layer 1 (parallel!)

print(qc.depth())  # Output: 1 (not 2!)
```

### ⚠️ Critical Exam Comparison: compose() vs tensor() vs append()

| Operation | Qubits | Structure | Use Case | Syntax |
|-----------|---------|-----------|----------|--------|
| **compose()** | Same or subset | Sequential (→) | Add steps to existing circuit | `qc1.compose(qc2)` |
| **tensor()** | Independent sets | Parallel (⊗) | Combine separate systems | `qc1.tensor(qc2)` |
| **append()** | Depends on gate | Adds single gate | Add one operation | `qc.append(gate, qubits)` |

**Visual Comparison**:
```
compose():  qc1──┬──  +  ──┬──qc2  =  qc1──┬────┬──qc2
               │           │                  │    │
               │           │                  │    │

tensor():   qc1──┬──  ⊗  qc2──┬──  =  qc1──┬──
               │              │           │
                           qc2──┬──
                                │

append():   qc──┬──  + gate  =  qc──┬──gate──
               │                    │
```

**Exam Trap - compose() with qubit mapping**:
```python
qc1 = QuantumCircuit(2)
qc2 = QuantumCircuit(2)

# WRONG: No qubit mapping specified when overlapping
❌ qc1.compose(qc2)  # Applies qc2 to same qubits

# CORRECT: Explicit qubit mapping
✅ qc1.compose(qc2, qubits=[0, 1])  # Maps qc2's qubits to qc1's [0,1]
✅ qc1.compose(qc2, qubits=[1, 0])  # Swaps the mapping!
```

### 🎓 Exam Question Patterns - Circuit Creation

**Pattern 1: "What is the depth/size/width of this circuit?"**
```python
# MEMORIZE THE ALGORITHM:
qc = QuantumCircuit(3, 3)
qc.h(0)      # Layer 1
qc.h(1)      # Layer 1 (parallel!)
qc.cx(0, 2)  # Layer 2
qc.measure_all()  # Layer 3

Depth = 3    # Longest sequential path
Size = 5     # Total operations (3 H + 1 CX + 3 M, but may exclude M)
Width = 6    # Total wires (3 qubits + 3 classical)
```

**Pattern 2: "Compose vs Tensor?"**
```
Same qubits, sequential? → compose()
Different qubits, parallel? → tensor()
Adding one gate? → append()
```

**Pattern 3: "Parameter binding"**
```python
theta = Parameter('θ')
qc.ry(theta, 0)

# Single value:
bound = qc.assign_parameters({theta: 0.5})

# Multiple values (returns list):
bound_list = [qc.assign_parameters({theta: val}) for val in [0, 0.5, 1]]
```

**Pattern 4: "Circuit properties without running**
```python
# BEFORE execution (just by analyzing circuit):
qc.depth()       # Critical path length
qc.size()        # Gate count
qc.num_qubits    # Qubit count (property, no ())
qc.count_ops()   # Dict of operations

# ⚠️ TRAP: num_qubits is PROPERTY, depth() is METHOD!
✅ qc.num_qubits     # No parentheses
✅ qc.depth()        # With parentheses
```

### 🧠 Memory Aids - Circuit Creation

**"Width = Wires, Depth = Delays, Size = Sum"**
- Width: Count all wires (quantum + classical)
- Depth: Longest path (layers)
- Size: Count all gates

**"Compose = Continue, Tensor = Together"**
- Compose: Continue the circuit (sequential)
- Tensor: Bring circuits together (parallel)

**"Parameters are Placeholders"**
- Parameter: Symbolic (like 'θ')
- assign_parameters: Make it concrete (θ = 0.5)
- bind_parameters: Older name (deprecated)

---

## 🧩 Circuit Composition

### compose() - The Flexible Merger

```python
from qiskit import QuantumCircuit

# Create sub-circuits
prep = QuantumCircuit(2)
prep.h(0)
prep.cx(0, 1)

algo = QuantumCircuit(2)
algo.x(0)
algo.z(1)

# Compose them
full_circuit = prep.compose(algo)
```

**Visual**:
```
prep:          algo:          full_circuit:
     ┌───┐         ┌───┐            ┌───┐     ┌───┐
q_0: ┤ H ├──■──    ┤ X ├       q_0: ┤ H ├──■──┤ X ├
     └───┘┌─┴─┐    └───┘            └───┘┌─┴─┐└───┘
q_1: ─────┤ X ├    ──■──       q_1: ─────┤ X ├──■──
          └───┘      │                   └───┘  │
                   ┌─┴─┐                      ┌─┴─┐
                   ┤ Z ├                      ┤ Z ├
                   └───┘                      └───┘
```

**Key Parameters**:

```python
# Add to end (default)
qc1.compose(qc2)

# Add in front
qc1.compose(qc2, front=True)

# Target specific qubits
qc1.compose(qc2, qubits=[2, 3])  # Apply qc2 to qubits 2,3 of qc1

# In-place modification
qc1.compose(qc2, inplace=True)
```

### append() - Add Gates/Circuits

```python
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

qc = QuantumCircuit(3)
qc.h([0, 1, 2])

# Append a gate
qc.append(QFT(3), [0, 1, 2])  # Add QFT to qubits 0,1,2
```

### tensor() - Combine Side-by-Side

```python
# Create circuits for different systems
system1 = QuantumCircuit(2)
system1.h(0)
system1.cx(0, 1)

system2 = QuantumCircuit(2)
system2.x([0, 1])

# Tensor product (side-by-side, not sequential!)
combined = system1.tensor(system2)
```

**Visual**:
```
system1:         system2:         combined (tensor):
     ┌───┐            ┌───┐            ┌───┐          
q_0: ┤ H ├──■──  q_0: ┤ X ├       q_0: ┤ H ├──■───────
     └───┘┌─┴─┐       └───┘            └───┘┌─┴─┐     
q_1: ─────┤ X ├  q_1: ┤ X ├       q_1: ─────┤ X ├─────
          └───┘       └───┘                 └───┘     
                                         ┌───┐          
                                    q_2: ┤ X ├─────────
                                         └───┘          
                                         ┌───┐          
                                    q_3: ┤ X ├─────────
                                         └───┘          

tensor: 4 qubits total (system1 ⊗ system2)
```

---

## 🎛️ Parameterized Circuits (VQE/QAOA ESSENTIAL!)

### Creating Parameters

```python
from qiskit import QuantumCircuit, Parameter
import numpy as np

# Define parameters
theta = Parameter('θ')
phi = Parameter('φ')

# Use in circuit
qc = QuantumCircuit(1)
qc.ry(theta, 0)  # Parameterized rotation
qc.rz(phi, 0)
```

**Visual**:
```
     ┌────────┐┌───────┐
q_0: ┤ Ry(θ) ├┤ Rz(φ) ├
     └────────┘└───────┘

Parameters: θ, φ (unbound)
```

### Binding Parameters

```python
# Bind specific values
bound_circuit = qc.assign_parameters({theta: np.pi/4, phi: np.pi/2})

# OR using bind_parameters (older API, still works)
bound_circuit = qc.bind_parameters({theta: np.pi/4, phi: np.pi/2})
```

**After binding**:
```
     ┌──────────┐┌──────────┐
q_0: ┤ Ry(π/4) ├┤ Rz(π/2) ├
     └──────────┘└──────────┘

Parameters: None (all bound)
```

### Parameter Vectors (Multiple Parameters)

```python
from qiskit.circuit import ParameterVector

# Create vector of parameters
params = ParameterVector('θ', 3)  # θ[0], θ[1], θ[2]

qc = QuantumCircuit(3)
for i in range(3):
    qc.ry(params[i], i)

# Bind all at once
values = [np.pi/4, np.pi/3, np.pi/2]
bound_qc = qc.assign_parameters({params: values})
```

**VQE/QAOA Pattern**:

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

def create_ansatz(n_qubits, depth):
    """Variational ansatz with parameters"""
    qc = QuantumCircuit(n_qubits)
    
    params = []
    for d in range(depth):
        # Rotation layer
        for i in range(n_qubits):
            theta = Parameter(f'θ_{d}_{i}')
            qc.ry(theta, i)
            params.append(theta)
        
        # Entangling layer
        for i in range(n_qubits-1):
            qc.cx(i, i+1)
    
    return qc, params

ansatz, params = create_ansatz(3, 2)
print(f"Parameters: {len(params)}")  # 6 parameters

# Optimize these in VQE...
```

---

## 📚 Circuit Library (Pre-Built Circuits)

### Standard Gates

```python
from qiskit.circuit.library import (
    XGate, ZGate, HGate, CXGate, CCXGate,
    RXGate, RYGate, RZGate
)

qc = QuantumCircuit(3)

# Add library gates
qc.append(HGate(), [0])
qc.append(CXGate(), [0, 1])
qc.append(CCXGate(), [0, 1, 2])  # Toffoli
```

### Standard Circuits

```python
from qiskit.circuit.library import (
    QFT,           # Quantum Fourier Transform
    QAOAAnsatz,    # QAOA circuit
    RealAmplitudes, # Variational ansatz
    EfficientSU2,  # Hardware-efficient ansatz
    PauliEvolutionGate  # Hamiltonian evolution
)

# Quantum Fourier Transform
qc = QuantumCircuit(4)
qc.append(QFT(4), range(4))

# QAOA for MaxCut
from qiskit_optimization import QuadraticProgram
# ... (define problem)
qaoa = QAOAAAnsatz(problem, reps=2)
```

### Commonly Used Library Circuits

| Circuit | Purpose | Usage |
|---------|---------|-------|
| `QFT(n)` | Quantum Fourier Transform | Shor's, Phase Estimation |
| `RealAmplitudes(n, reps)` | Variational ansatz | VQE, QAOA |
| `EfficientSU2(n, reps)` | Hardware-efficient ansatz | VQE on real hardware |
| `QAOAAnsatz(problem, reps)` | QAOA circuit | Optimization problems |
| `GroverOperator(oracle)` | Grover's iteration | Search algorithms |

---

## 🎮 Classical Control (c_if)

### Conditional Gate Execution

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)

# Measure qubit 0
qc.h(0)
qc.measure(0, 0)

# Apply X to qubit 1 IF classical bit 0 is 1
qc.x(1).c_if(0, 1)  # or qc.x(1).c_if(qc.clbits[0], 1)

qc.measure(1, 1)
```

**Visual**:
```
     ┌───┐┌─┐        
q_0: ┤ H ├┤M├────────
     └───┘└╥┘  ┌───┐ 
q_1: ──────╫───┤ X ├─  ← X applied if c[0] == 1
           ║   └─╥─┘ 
           ║  ┌──╨──┐
c: 2/══════╩══╡     ╞
           0  └─────┘
```

### Multiple Classical Bits

```python
qc = QuantumCircuit(3, 3)

# Measure qubits 0 and 1
qc.measure([0, 1], [0, 1])

# Apply Z to qubit 2 IF both c[0] and c[1] are 1
# (requires creating a ClassicalRegister)
from qiskit import ClassicalRegister

cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

qc.measure([0, 1], [0, 1])
qc.z(2).c_if(cr, 3)  # cr == 3 means '11' in binary
```

---

## ✅ Exam Quick Reference

### Must Memorize

```python
# Circuit creation
qc = QuantumCircuit(n_qubits, n_clbits)

# Properties (TESTED!)
qc.depth()       # Critical path length
qc.size()        # Total gate count
qc.width()       # Qubits + classical bits
qc.num_qubits    # Number of qubits
qc.num_clbits    # Number of classical bits
qc.count_ops()   # Dict of gate counts

# Composition
qc1.compose(qc2)              # Append qc2 to qc1
qc1.compose(qc2, front=True)  # Prepend qc2
qc1.tensor(qc2)               # Side-by-side (tensor product)

# Parameters
from qiskit.circuit import Parameter
theta = Parameter('θ')
qc.ry(theta, 0)
bound = qc.assign_parameters({theta: value})

# Classical control
qc.x(1).c_if(classical_bit, value)
```

### Common Exam Questions

**Q1: What's the difference between depth() and size()?**
- `depth()`: Critical path (longest sequential chain)
- `size()`: Total gate count

**Q2: How to compose two circuits sequentially?**
```python
full = qc1.compose(qc2)  # qc1 then qc2
```

**Q3: How to create parameterized circuit?**
```python
from qiskit.circuit import Parameter
theta = Parameter('θ')
qc.ry(theta, 0)
```

**Q4: How to do conditional operations?**
```python
qc.x(qubit).c_if(classical_bit, value)
```

---

## 🎯 Practice Examples

### Example 1: Build VQE Ansatz

```python
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
import numpy as np

def vqe_ansatz(n_qubits, depth):
    """Hardware-efficient ansatz"""
    qc = QuantumCircuit(n_qubits)
    
    # Parameters
    params = ParameterVector('θ', n_qubits * depth * 2)
    idx = 0
    
    for d in range(depth):
        # Y rotations
        for i in range(n_qubits):
            qc.ry(params[idx], i)
            idx += 1
        
        # Z rotations
        for i in range(n_qubits):
            qc.rz(params[idx], i)
            idx += 1
        
        # Entangling
        for i in range(n_qubits-1):
            qc.cx(i, i+1)
    
    return qc

ansatz = vqe_ansatz(3, 2)
print(ansatz.draw())
print(f"Depth: {ansatz.depth()}")
print(f"Parameters: {len(ansatz.parameters)}")
```

### Example 2: Conditional Teleportation

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3)

# Entangle qubits 1 and 2
qc.h(1)
qc.cx(1, 2)

# Bell measurement on qubits 0 and 1
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])

# Conditional corrections on qubit 2
qc.x(2).c_if(qc.clbits[1], 1)  # If c[1]==1, apply X
qc.z(2).c_if(qc.clbits[0], 1)  # If c[0]==1, apply Z

qc.measure(2, 2)
```

### Example 3: Multi-Register Organization

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Define registers
data = QuantumRegister(4, 'data')
ancilla = QuantumRegister(1, 'anc')
meas = ClassicalRegister(4, 'meas')
syndrome = ClassicalRegister(1, 'syn')

qc = QuantumCircuit(data, ancilla, meas, syndrome)

# Operate on specific registers
qc.h(data)  # Hadamard on all data qubits
qc.x(ancilla[0])

# Measure to specific classical registers
qc.measure(data, meas)
qc.measure(ancilla, syndrome)

print(qc.draw())
```

---

## 🚀 Complete Walkthrough: VQE from Scratch (Covers ALL Exam Sections!)

This comprehensive example implements a simplified VQE (Variational Quantum Eigensolver) to find the ground state energy of a simple Hamiltonian. It systematically covers concepts from **ALL 8 exam sections**.

### Problem Statement
Find the minimum eigenvalue of the Hamiltonian: $H = 0.5 \cdot Z_0Z_1 + 0.3 \cdot X_0 + 0.2 \cdot X_1$

---

### Step 1: Create the Circuit (Section 3 - Circuit Basics & Composition)

```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector

# Create registers for organization (Section 3.1: Registers)
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')

# Create parameterized ansatz circuit (Section 3.3: Parameters)
theta = ParameterVector('θ', 4)

ansatz = QuantumCircuit(qr, cr)

# Layer 1: Single-qubit rotations (Section 1: Quantum Operations - RY gates)
ansatz.ry(theta[0], qr[0])
ansatz.ry(theta[1], qr[1])

# Entanglement layer (Section 1: Multi-qubit gates - CNOT)
ansatz.cx(qr[0], qr[1])

# Layer 2: More rotations
ansatz.ry(theta[2], qr[0])
ansatz.ry(theta[3], qr[1])

# Add barrier for visual clarity (Section 1: barrier())
ansatz.barrier()

# Check circuit properties (Section 3.1: Circuit Properties)
print(f"Circuit depth: {ansatz.depth()}")     # Critical path length
print(f"Circuit size: {ansatz.size()}")       # Total gates
print(f"Number of qubits: {ansatz.num_qubits}")
print(f"Parameters: {ansatz.parameters}")

# Visualize the ansatz (Section 2: Visualization)
print(ansatz.draw())
```

**Expected Output**:
```
Circuit depth: 4
Circuit size: 5
Number of qubits: 2
Parameters: ParameterView([ParameterVectorElement(θ[0]), ...])

     ┌──────────┐          ░ 
q_0: ┤ Ry(θ[0]) ├──■───────░─┤ Ry(θ[2]) ├
     ├──────────┤┌─┴─┐     ░ ├──────────┤
q_1: ┤ Ry(θ[1]) ├┤ X ├─────░─┤ Ry(θ[3]) ├
     └──────────┘└───┘     ░ └──────────┘
```

---

### Step 2: Define the Hamiltonian Observable (Section 6 - Estimator)

```python
from qiskit.quantum_info import SparsePauliOp

# Define Hamiltonian: H = 0.5*ZZ + 0.3*X0 + 0.2*X1 (Section 6: Observables)
# SparsePauliOp uses little-endian: rightmost = qubit 0
hamiltonian = SparsePauliOp.from_list([
    ('ZZ', 0.5),   # Z on both qubits (correlation term)
    ('XI', 0.3),   # X on qubit 0 (I on qubit 1)
    ('IX', 0.2),   # X on qubit 1 (I on qubit 0)
])

print(f"Hamiltonian: {hamiltonian}")
print(f"Number of Pauli terms: {len(hamiltonian)}")
```

---

### Step 3: Use Circuit Library Ansatz (Section 3.4 - Circuit Library)

```python
from qiskit.circuit.library import RealAmplitudes, EfficientSU2

# Alternative: Use pre-built ansatz from library (Section 3.4)
library_ansatz = RealAmplitudes(num_qubits=2, reps=2, entanglement='linear')

print("Library Ansatz (RealAmplitudes):")
print(library_ansatz.draw())
print(f"Parameters: {library_ansatz.num_parameters}")

# Compose circuits together (Section 3.2: compose())
# Initial state preparation + ansatz
init_circuit = QuantumCircuit(2)
init_circuit.h([0, 1])  # Start in superposition (Section 1: H gate)

full_circuit = init_circuit.compose(library_ansatz)
print("\nComposed Circuit (init + ansatz):")
print(full_circuit.draw())
```

---

### Step 4: Export to OpenQASM (Section 8 - OpenQASM)

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

---

### Step 5: Transpile for Backend (Section 4 - Run Circuits)

```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

# Use fake backend for demonstration (Section 4: Backends)
backend = FakeManilaV2()

# Generate pass manager (Section 4: Transpilation)
pm = generate_preset_pass_manager(
    optimization_level=2,  # 0-3, higher = more optimization
    backend=backend
)

# Bind parameters before transpilation (Section 3.3: assign_parameters)
import numpy as np
initial_params = np.random.random(ansatz.num_parameters) * np.pi

bound_circuit = ansatz.assign_parameters(
    {theta[i]: initial_params[i] for i in range(len(theta))}
)
bound_circuit.measure(qr, cr)  # Add measurements

# Transpile (Section 4: transpile)
transpiled = pm.run(bound_circuit)

print(f"Original depth: {bound_circuit.depth()}")
print(f"Transpiled depth: {transpiled.depth()}")
print(f"Transpiled circuit (first 20 lines):")
print('\n'.join(str(transpiled.draw()).split('\n')[:20]))
```

---

### Step 6: Run with Sampler (Section 5 - Sampler Primitive)

```python
from qiskit_ibm_runtime import SamplerV2 as Sampler
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

---

### Step 7: Run with Estimator (Section 6 - Estimator Primitive)

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

---

### Step 8: Visualize Results (Section 2 - Visualization)

```python
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector

# Plot measurement histogram (Section 2: Histogram visualization)
# plot_histogram(counts)  # Uncomment in Jupyter

# Get statevector for visualization (Section 2: State visualization)
sv = Statevector(bound_ansatz)
print(f"State vector: {sv}")

# Plot Bloch sphere (Section 2: Bloch sphere)
# plot_bloch_multivector(sv)  # Uncomment in Jupyter

# Circuit visualization styles (Section 2: Drawing styles)
print("\nText style:")
print(ansatz.draw(output='text'))

# For Jupyter: ansatz.draw(output='mpl')  # Matplotlib style
# For LaTeX:   ansatz.draw(output='latex')
```

---

### Step 9: Complete VQE Optimization Loop (Sections 3, 5, 6, 7 Combined)

```python
from scipy.optimize import minimize
import numpy as np

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
print(f"Initial parameters: {initial_params}")

# Run classical optimizer (scipy integration)
result = minimize(
    vqe_cost_function,
    initial_params,
    args=(ansatz, hamiltonian, estimator),
    method='COBYLA',
    options={'maxiter': 100, 'disp': True}
)

print(f"\n=== VQE RESULTS ===")
print(f"Optimal parameters: {result.x}")
print(f"Ground state energy: {result.fun:.6f}")
print(f"Optimization converged: {result.success}")
print(f"Number of iterations: {result.nfev}")

# Verify with exact diagonalization
import numpy as np
H_matrix = hamiltonian.to_matrix()
eigenvalues = np.linalg.eigvalsh(H_matrix)
print(f"\nExact ground state energy: {min(eigenvalues):.6f}")
print(f"VQE error: {abs(result.fun - min(eigenvalues)):.6f}")
```

---

### Step 10: Add Classical Control (Section 3.5 - c_if Operations)

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

---

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

1. **`circuit_basics.ipynb`** - Circuit creation, properties, registers
2. **`circuit_composition.ipynb`** - compose(), append(), tensor()
3. **`parameterized_circuits.ipynb`** - Parameters, binding, VQE patterns
4. **`circuit_library.ipynb`** - Standard gates, QFT, ansätze
5. **`classical_control.ipynb`** - c_if(), conditional operations

---

## 🎓 Key Takeaways

```
✅ QuantumCircuit(n, m) creates n qubits, m classical bits
✅ depth() = critical path, size() = total gates
✅ compose() appends circuits sequentially
✅ tensor() combines circuits side-by-side
✅ Parameter() creates parameterized gates
✅ assign_parameters() binds parameter values
✅ c_if() does conditional operations
✅ This section is 18% of exam - MASTER IT!
```

---

## 🔗 Next Steps

1. Practice creating circuits all 5 ways
2. Understand depth vs size deeply
3. Master compose() and tensor()
4. Build parameterized ansätze for VQE
5. Implement conditional operations
6. Move to **Section 4 (Run Circuits)** to execute on backends

**This is the HIGHEST weighted section - invest time here!** 🚀🎯
