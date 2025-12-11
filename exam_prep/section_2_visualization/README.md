# Section 2: Visualization (11% of Exam)

> **Exam Weight**: ~7 questions | **Difficulty**: Easy-Medium | **Must Master**: ✅

---

## 📖 Overview

Visualization is CRITICAL for understanding quantum circuits and debugging. This section covers how to **draw circuits** and **visualize quantum states** using Qiskit's visualization tools.

### What You'll Learn

1. **Circuit Visualization**: Different drawing styles, backends, and customization
2. **State Visualization**: Bloch sphere, state vectors, density matrices, Q-sphere
3. **Measurement Results**: Histograms, probability distributions

---

## 🎯 Why Visualization Matters

### 🧠 Conceptual Deep Dive

#### Analogy: The Musical Score
A quantum circuit diagram is remarkably similar to a musical score.
- **Time**: Flows from left to right.
- **Staff Lines**: Each line represents a qubit (like an instrument).
- **Notes**: Gates are the notes played on the instruments.
- **Chords**: Multi-qubit gates (like CNOT) are chords played across instruments.
- **Barriers**: Like measure lines, organizing the music into sections.

#### The "Unseeable" State
Why do we need histograms? Because we can **never** observe a quantum state vector directly.
- If you have a state $\alpha|0\rangle + \beta|1\rangle$, you cannot ask the qubit "What are $\alpha$ and $\beta$?".
- You can only ask "Are you 0 or 1?".
- To "see" the state, we must run the experiment thousands of times (shots) and build a histogram of the results to infer $\alpha$ and $\beta$.

### Visualization Methods Overview

```
"If you can't visualize it, you can't understand it"
                                        - Quantum Debugging Wisdom

Visualization helps you:
✓ Debug circuits (find gate errors)
✓ Understand state evolution
✓ Communicate results to non-experts
✓ Verify algorithm correctness
✓ Detect entanglement visually
```

---

## 🎨 Circuit Visualization

### Basic Circuit Drawing

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

# Default draw (text)
print(qc.draw())
```

**Output**:
```
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 
```

### Drawing Styles (EXAM TESTED!)

**1. Text Style** (default for Jupyter/console)

```python
qc.draw(output='text')  # ASCII art (good for console)
```

**2. Matplotlib Style** (best for reports/papers)

```python
qc.draw(output='mpl')  # High-quality matplotlib figure
```

Visual:
```
┌────────────────────────────┐
│  q₀: ──H────●────M──       │
│            │     │          │
│  q₁: ─────⊕────M──         │
│                             │
│  c: 2/═════════╩╩═         │
└────────────────────────────┘
```

**3. LaTeX Style** (for publications)

```python
qc.draw(output='latex')  # LaTeX circuit diagram
```

**4. LaTeX Source** (raw LaTeX code)

```python
qc.draw(output='latex_source')  # Returns LaTeX string
```

### Customization Options

```python
# Reverse qubit order (q_n on top)
qc.draw(reverse_bits=True)

# Show idle wires
qc.draw(idle_wires=False)  # Hide unused qubits

# Fold long circuits
qc.draw(fold=50)  # Fold after 50 gate columns

# Scale diagram
qc.draw(output='mpl', scale=1.5)  # 150% size

# Custom color scheme
qc.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'})
```

### ⚠️ Exam Traps - Visualization

**Trap 1: Output Parameter is String**
```python
❌ qc.draw(output=mpl)          # WRONG: mpl is not defined
✅ qc.draw(output='mpl')        # CORRECT: String!
❌ qc.draw('mpl')               # WRONG: Positional not supported
✅ qc.draw(output='text')       # CORRECT: Named parameter
```

**Trap 2: Default Output Depends on Context**
```python
# In Jupyter: defaults to 'text'
qc.draw()  # Shows ASCII

# With matplotlib installed: can use 'mpl'
qc.draw(output='mpl')  # Shows figure
```

**Trap 3: plot_histogram vs Sampler Result**
```python
from qiskit.visualization import plot_histogram

# WRONG: Can't plot result object directly
❌ plot_histogram(result)  

# CORRECT: Extract counts first
✅ counts = result[0].data.meas.get_counts()
✅ plot_histogram(counts)
```

**📊 Understanding `counts`**:

**Definition**: `counts` is a Python dictionary that maps measurement outcome strings to the number of times each outcome was observed during circuit execution.

**Structure**:
```python
counts = {'00': 512, '11': 488}  # Example for Bell state with 1000 shots
#          │     │
#          │     └── Number of times this outcome occurred
#          └── Measurement outcome (binary string)
```

**Key Concepts**:
- **Keys**: Binary strings representing measured qubit states (e.g., `'00'`, `'01'`, `'10'`, `'11'`)
- **Values**: Integers showing how many times each state was measured (frequency)
- **Shots**: Total number of circuit executions (sum of all values)
- **Probabilities**: Divide each count by total shots to get probability

**Why It Matters**:
- Quantum measurements are probabilistic → need multiple shots to see distribution
- `counts` reveals the probability distribution of quantum states
- Essential for analyzing algorithm results and verifying circuits

**Accessing Counts**:
```python
# From SamplerV2 result
counts = result[0].data.meas.get_counts()

# Common operations
total_shots = sum(counts.values())           # Total executions
most_common = max(counts, key=counts.get)    # Most frequent result
probability = counts['00'] / total_shots     # Probability of '00'
```

**Example**:
```python
# Bell state: expect 50% |00⟩, 50% |11⟩
counts = {'00': 512, '11': 488}  # 1000 shots

# Analysis:
# - '00' measured 512 times (51.2%)
# - '11' measured 488 times (48.8%)
# - '01' and '10' not observed (as expected for Bell state)
```

**Memory Aid - Visualization Methods**:
```
Mnemonic: "Text Makes LaTeX, Bloch Visualizes Histograms"
T = Text (console)
M = Matplotlib (figures)
L = LaTeX (papers)
B = Bloch (states)
H = Histogram (results)
```

### 🎓 Exam Question Patterns - Visualization

**Pattern 1: "Which output format for...?"**
```
Console/Terminal → 'text'
Jupyter Notebook → 'mpl' (matplotlib)
Academic Paper → 'latex'
Single Qubit State → plot_bloch_multivector()
Measurement Data → plot_histogram()
```

**Pattern 2: "What does reverse_bits do?"**
```python
# Default: q_0 on top
qc.draw()  
     q_0: ───  ← Top
     q_1: ───  
     q_2: ───  ← Bottom

# Reversed: q_n on top (MSB first)
qc.draw(reverse_bits=True)
     q_2: ───  ← Top (Most Significant)
     q_1: ───
     q_0: ───  ← Bottom (Least Significant)

# USE WHEN: Matching classical bit ordering (big-endian)
```

**Pattern 3: "State vector vs Bloch sphere?"**
```
State Vector: Complex amplitudes [α, β, ...]
Bloch Sphere: Geometric (angles θ, φ)
Use Bloch for: Single qubit only!
Use State Vector for: Any number of qubits
```

### 📊 Quick Decision: Which Visualization?

```
┌─ Need to see circuit structure? ─────────────┐
│  → qc.draw(output='mpl')                     │
└──────────────────────────────────────────────┘

┌─ Need to see quantum state? ─────────────────┐
│  → plot_bloch_multivector(state)  (1 qubit)  │
│  → plot_state_qsphere(state)      (n qubits) │
└──────────────────────────────────────────────┘

┌─ Need to see measurement results? ───────────┐
│  → plot_histogram(counts)                    │
└──────────────────────────────────────────────┘

┌─ Need LaTeX code for paper? ─────────────────┐
│  → qc.draw(output='latex_source')            │
└──────────────────────────────────────────────┘
```

**Example with Options**:

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.barrier()
qc.measure([0,1,2], [0,1,2])

# Professional visualization
qc.draw(
    output='mpl',
    reverse_bits=True,    # MSB on top
    fold=20,              # Fold long circuits
    scale=1.2             # Larger size
)
```

---

## 🌐 State Visualization

### 1. Bloch Sphere (Single Qubit)

**The Bloch Sphere** represents single-qubit states geometrically:

```
         |0⟩ (North Pole)
          ↑
          |
     ┌────+────┐
    /     |     \
   /      |      \
  /       |       \
 |        |        |
  ────────+────────  ← |+⟩, |-⟩, |+i⟩, |-i⟩
 |        |        |
  \       |       /
   \      |      /
    \     |     /
     └────+────┘
          |
          ↓
         |1⟩ (South Pole)

Coordinates:
• θ = polar angle (0 to π)
• φ = azimuthal angle (0 to 2π)

|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
```

**Qiskit Visualization**:

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# Create state
qc = QuantumCircuit(1)
qc.h(0)  # |+⟩ = (|0⟩+|1⟩)/√2

# Get statevector
state = Statevector(qc)

# Plot on Bloch sphere
import matplotlib.pyplot as plt
plot_bloch_multivector(state)
plt.show()  # Display the figure
```

**Common States on Bloch Sphere**:

```
|0⟩:  θ=0,    φ=0     (North pole)
|1⟩:  θ=π,    φ=0     (South pole)
|+⟩:  θ=π/2,  φ=0     (+X axis)
|-⟩:  θ=π/2,  φ=π     (-X axis)
|+i⟩: θ=π/2,  φ=π/2   (+Y axis)
|-i⟩: θ=π/2,  φ=3π/2  (-Y axis)
```

### 2. State Vector Visualization

**Multi-qubit states** can't be shown on single Bloch sphere. Use bar charts:

```python
from qiskit.visualization import plot_state_city

# 2-qubit state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  # Bell state

state = Statevector(qc)

# City plot (3D bars for amplitudes)
import matplotlib.pyplot as plt
plot_state_city(state)
plt.show()  # Display the figure
```

**Visual Output**:
```
         Real             Imaginary
     ┌────┬────┐      ┌────┬────┐
|00⟩ │ ▓▓ │    │  |00⟩│    │    │
|01⟩ │    │    │  |01⟩│    │    │
|10⟩ │    │    │  |10⟩│    │    │
|11⟩ │ ▓▓ │    │  |11⟩│    │    │
     └────┴────┘      └────┴────┘
    
Bell state: (|00⟩+|11⟩)/√2
Real parts: 1/√2 for |00⟩ and |11⟩
Imaginary: all zero
```

---

### 🔍 Key Comparison: `plot_state_city` vs `plot_histogram`

#### 📖 Definitions

**`plot_state_city`**:
A visualization function that displays a quantum state's **complex amplitudes** as 3D bars in a "city skyline" format. It shows both the real and imaginary components of each basis state amplitude, providing complete information about the quantum state before measurement.

```python
from qiskit.visualization import plot_state_city
from qiskit.quantum_info import Statevector

state = Statevector(qc)  # Get quantum state (no measurements!)
plot_state_city(state)   # Visualize amplitudes as 3D bars
```

**`plot_histogram`**:
A visualization function that displays **measurement outcomes** (counts) as a bar chart. It shows how many times each classical bit string was observed when measuring a quantum circuit multiple times (shots), representing the probability distribution of measurement results.

```python
from qiskit.visualization import plot_histogram

counts = {'00': 512, '11': 488}  # Measurement results from running circuit
plot_histogram(counts)           # Visualize as bar chart
```

---

**EXAM CRITICAL**: These visualizations serve completely different purposes!

| Aspect | `plot_state_city` | `plot_histogram` |
|--------|-------------------|------------------|
| **Input** | `Statevector` object | `counts` dictionary |
| **Shows** | Quantum state amplitudes (α, β) | Measurement outcomes (frequencies) |
| **When to use** | BEFORE measurement | AFTER measurement |
| **Information** | Full quantum information (complex amplitudes) | Classical information only (probabilities) |
| **Phase info** | ✅ Yes (shows real + imaginary parts) | ❌ No (phase lost after measurement) |
| **Reversible?** | ✅ Can reconstruct state | ❌ Cannot recover original state |
| **Data type** | Complex numbers | Integers (counts) |

**Conceptual Difference**:

```
┌─────────────────────────────────────────────────────────────────┐
│                     QUANTUM WORLD                                │
│   plot_state_city shows the "true" quantum state                │
│   • Complex amplitudes: α|00⟩ + β|01⟩ + γ|10⟩ + δ|11⟩           │
│   • Phase information preserved                                  │
│   • Requires Statevector (simulation only!)                      │
│   • You see EVERYTHING about the state                           │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                            MEASUREMENT
                            (collapses state)
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CLASSICAL WORLD                              │
│   plot_histogram shows what we actually observe                 │
│   • Integer counts: {'00': 512, '11': 488}                       │
│   • Phase information LOST forever                               │
│   • Works with real hardware results                             │
│   • You only see PROBABILITIES, not amplitudes                   │
└─────────────────────────────────────────────────────────────────┘
```

**Example - Same Bell State, Different Views**:

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_city, plot_histogram
from qiskit.primitives import StatevectorSampler

# Create Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# VIEW 1: plot_state_city (quantum view)
state = Statevector(qc)
plot_state_city(state)
# Shows: α = 1/√2 for |00⟩, δ = 1/√2 for |11⟩
# You see the EXACT amplitudes (complex numbers)

# VIEW 2: plot_histogram (classical view)
qc.measure_all()
sampler = StatevectorSampler()
counts = sampler.run([qc], shots=1000).result()[0].data.meas.get_counts()
plot_histogram(counts)
# Shows: {'00': ~500, '11': ~500}
# You only see how many times each outcome occurred
```

---

### 🔍 Key Comparison: `Statevector` vs `StatevectorSampler`

#### 📖 Definitions

**`Statevector`**:
A class from `qiskit.quantum_info` that represents the **exact mathematical state** of a quantum system as a vector of complex amplitudes. It provides the complete quantum information including phase, allowing you to know precisely what superposition the qubits are in. This is a simulation tool that cannot be replicated on real quantum hardware (you can never "see" the actual statevector of a physical qubit).

```python
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# Note: NO measurements in the circuit!

state = Statevector(qc)
print(state.data)  # [0.707+0j, 0+0j, 0+0j, 0.707+0j]
# This is the EXACT quantum state: (|00⟩ + |11⟩)/√2
```

**`StatevectorSampler`**:
A primitive class from `qiskit.primitives` that **simulates the measurement process** of a quantum circuit. It uses the underlying statevector to calculate probabilities, then samples from those probabilities to produce measurement counts—mimicking what would happen on real quantum hardware. This is useful for testing code before running on actual quantum computers.

```python
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])  # MUST have measurements!

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
counts = job.result()[0].data.meas.get_counts()
print(counts)  # {'00': 507, '11': 493} (varies each run)
```

---

**EXAM CRITICAL**: These are fundamentally different tools!

| Aspect | `Statevector` | `StatevectorSampler` |
|--------|---------------|----------------------|
| **Import** | `from qiskit.quantum_info import Statevector` | `from qiskit.primitives import StatevectorSampler` |
| **Purpose** | Get exact quantum state amplitudes | Simulate measurement sampling |
| **Output** | Complex amplitude vector [α, β, γ, δ...] | Measurement counts dictionary {'00': 512, '11': 488} |
| **Measurements** | ❌ Circuit must NOT have measurements | ✅ Circuit MUST have measurements |
| **Shots** | N/A (exact calculation) | Uses `shots` parameter |
| **Randomness** | ❌ Deterministic (same result every time) | ✅ Probabilistic (varies with shots) |
| **Information** | Full quantum state (phase included) | Classical outcomes only |
| **Use case** | Understanding state, debugging | Simulating real hardware behavior |

**Conceptual Difference**:

```
┌─────────────────────────────────────────────────────────────────┐
│ Statevector = "What IS the quantum state?"                      │
│   • Mathematical description of the quantum system               │
│   • Returns: [0.707+0j, 0, 0, 0.707+0j]  (exact amplitudes)     │
│   • Like asking "What's inside Schrödinger's box?"               │
│   • ⚠️ Impossible on real hardware! (simulation only)            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ StatevectorSampler = "What would we MEASURE?"                   │
│   • Simulates the act of measuring the quantum system            │
│   • Returns: {'00': 512, '11': 488}  (measurement outcomes)      │
│   • Like asking "What do we see when we open the box?"           │
│   • ✅ Mimics real hardware behavior (useful for testing)        │
└─────────────────────────────────────────────────────────────────┘
```

**Code Example - Same Circuit, Different Tools**:

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler

# Create Bell state (NO measurements yet)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# ═══════════════════════════════════════════════════════════════
# TOOL 1: Statevector - Get exact quantum state
# ═══════════════════════════════════════════════════════════════
state = Statevector(qc)  # No measurements in circuit!
print(state.data)
# Output: [0.707+0j, 0+0j, 0+0j, 0.707+0j]
#         |00⟩      |01⟩  |10⟩  |11⟩
# → Exact amplitudes, phase information preserved
# → Same result EVERY time (deterministic)

# ═══════════════════════════════════════════════════════════════
# TOOL 2: StatevectorSampler - Simulate measurements
# ═══════════════════════════════════════════════════════════════
qc_measured = qc.copy()
qc_measured.measure_all()  # MUST add measurements!

sampler = StatevectorSampler()
job = sampler.run([qc_measured], shots=1000)
counts = job.result()[0].data.meas.get_counts()
print(counts)
# Output: {'00': 507, '11': 493}  (example - varies each run!)
# → Probabilistic results based on amplitudes
# → Different result each time due to quantum randomness
```

**When to Use Each**:

| Scenario | Use This | Why |
|----------|----------|-----|
| Debug algorithm logic | `Statevector` | See exact state at each step |
| Verify state preparation | `Statevector` | Check amplitudes precisely |
| Test before real hardware | `StatevectorSampler` | Mimics real measurement behavior |
| Analyze measurement statistics | `StatevectorSampler` | Returns counts like real device |
| Get phase information | `Statevector` | Phase is lost in measurement |
| Prepare for production | `StatevectorSampler` | Same API as real backends |

**Common Exam Traps**:

```python
# ❌ TRAP 1: Using Statevector on circuit WITH measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure(0, 0)
state = Statevector(qc)  # ⚠️ Works but gives post-measurement state!

# ✅ CORRECT: Use Statevector BEFORE measurements
qc = QuantumCircuit(2)
qc.h(0)
state = Statevector(qc)  # Clean quantum state

# ❌ TRAP 2: Using StatevectorSampler WITHOUT measurements
qc = QuantumCircuit(2)
qc.h(0)
sampler = StatevectorSampler()
job = sampler.run([qc])  # ⚠️ No measurements = no counts!

# ✅ CORRECT: Always add measurements for Sampler
qc.measure_all()
job = sampler.run([qc], shots=1000)

# ❌ TRAP 3: Expecting same results from StatevectorSampler
counts1 = sampler.run([qc], shots=100).result()[0].data.meas.get_counts()
counts2 = sampler.run([qc], shots=100).result()[0].data.meas.get_counts()
# counts1 ≠ counts2 (different due to randomness!)

# ✅ Statevector always gives same result
state1 = Statevector(qc_no_meas)
state2 = Statevector(qc_no_meas)
# state1 == state2 (always identical)
```

**Memory Aid**:
```
Statevector = "State"       → The quantum state itself (what it IS)
StatevectorSampler = "Sample" → Samples from the state (what we MEASURE)

Think of it like a dice:
- Statevector = Knowing the exact probabilities (1/6 for each face)
- StatevectorSampler = Actually rolling the dice 1000 times
```

---

### 📊 Visualization Compatibility Matrix

**Which visualizations work with which tool?**

| Visualization Function | `Statevector` | `StatevectorSampler` (counts) |
|------------------------|:-------------:|:-----------------------------:|
| `plot_state_city()` | ✅ | ❌ |
| `plot_state_qsphere()` | ✅ | ❌ |
| `plot_bloch_multivector()` | ✅ | ❌ |
| `plot_state_hinton()` | ✅ | ❌ |
| `plot_state_paulivec()` | ✅ | ❌ |
| `plot_histogram()` | ❌ | ✅ |
| `plot_distribution()` | ❌ | ✅ |

---

### 🎨 All Visualizations with `Statevector`

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_state_city,
    plot_state_qsphere,
    plot_bloch_multivector,
    plot_state_hinton,
    plot_state_paulivec
)
import matplotlib.pyplot as plt

# Create Bell state (NO measurements!)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Get the quantum state
state = Statevector(qc)

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 1: City Plot (3D bars for amplitudes)
# ═══════════════════════════════════════════════════════════════
plot_state_city(state, title="City Plot - Bell State")
plt.show()
# Shows: Real and imaginary parts as 3D bars
# Best for: Seeing exact amplitude values
# a) WHEN TO USE: When you need to see the precise numerical values of state amplitudes
# b) WHERE IT HELPS: Debugging algorithms, verifying state preparation, educational demos
# c) PURPOSE: Displays complex amplitudes as 3D bars - real & imaginary parts separately

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 2: Q-Sphere (probability + phase on sphere)
# ═══════════════════════════════════════════════════════════════
plot_state_qsphere(state, title="Q-Sphere - Bell State")
plt.show()
# Shows: Markers on sphere, size = probability, color = phase
# Best for: Multi-qubit states with phase information
# a) WHEN TO USE: When analyzing multi-qubit states where phase relationships matter
# b) WHERE IT HELPS: Understanding superposition patterns, detecting phase errors in algorithms
# c) PURPOSE: Shows probability (marker size) and phase (color) on a spherical surface

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 3: Bloch Multivector (individual qubit Bloch spheres)
# ═══════════════════════════════════════════════════════════════
plot_bloch_multivector(state, title="Bloch Spheres - Bell State")
plt.show()
# Shows: One Bloch sphere per qubit (reduced density matrix)
# Best for: Understanding individual qubit states
# ⚠️ Note: For entangled states, individual qubits appear mixed!
# a) WHEN TO USE: When examining how each qubit behaves independently in a multi-qubit system
# b) WHERE IT HELPS: Detecting entanglement (mixed states), teaching single-qubit rotations
# c) PURPOSE: Visualizes each qubit's reduced state on its own Bloch sphere

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 4: Hinton Diagram (density matrix visualization)
# ═══════════════════════════════════════════════════════════════
plot_state_hinton(state, title="Hinton Diagram - Bell State")
plt.show()
# Shows: Density matrix as squares (size = magnitude, color = sign)
# Best for: Visualizing entanglement and coherences
# a) WHEN TO USE: When analyzing density matrices, entanglement, or mixed states
# b) WHERE IT HELPS: Identifying off-diagonal coherences, spotting decoherence effects
# c) PURPOSE: Displays density matrix elements as squares - size shows magnitude, color shows sign

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 5: Pauli Vector (Pauli basis decomposition)
# ═══════════════════════════════════════════════════════════════
plot_state_paulivec(state, title="Pauli Vector - Bell State")
plt.show()
# Shows: Expectation values of Pauli operators
# Best for: Quantum chemistry, Pauli decomposition analysis
# a) WHEN TO USE: When working with Hamiltonians or Pauli-based decompositions
# b) WHERE IT HELPS: VQE algorithms, quantum chemistry, error analysis via Pauli channels
# c) PURPOSE: Shows expectation values of all Pauli operator combinations (II, IX, IY, IZ, XI, XX, ...)
```

**Visual Summary of Statevector Visualizations**:

```
┌─────────────────────────────────────────────────────────────────┐
│ plot_state_city()           │ plot_state_qsphere()             │
│ ┌────────────┐              │         ○                        │
│ │ ▓▓   ▓▓    │ Real         │       ●   ●                      │
│ │            │              │     ○       ○                    │
│ │            │ Imag         │       ●   ●   (sphere with       │
│ └────────────┘              │         ○      markers)          │
│ 3D bars for amplitudes      │ Probability + phase on sphere    │
├─────────────────────────────┼──────────────────────────────────┤
│ plot_bloch_multivector()    │ plot_state_hinton()              │
│   ↗                ↗        │ ┌──┬──┬──┬──┐                    │
│  ●                ●         │ │▓▓│  │  │▓▓│                    │
│ ↙                ↙          │ │  │  │  │  │                    │
│ Qubit 0        Qubit 1      │ │  │  │  │  │                    │
│ Individual Bloch spheres    │ │▓▓│  │  │▓▓│                    │
│                             │ └──┴──┴──┴──┘                    │
│                             │ Density matrix squares           │
├─────────────────────────────┴──────────────────────────────────┤
│ plot_state_paulivec()                                          │
│ ┌────┬────┬────┬────┬────┬────┬────┬────┐                      │
│ │ II │ IX │ IY │ IZ │ XI │ XX │ XY │... │                      │
│ │ ▓▓ │    │    │    │    │ ▓▓ │    │    │                      │
│ └────┴────┴────┴────┴────┴────┴────┴────┘                      │
│ Pauli operator expectation values                              │
└─────────────────────────────────────────────────────────────────┘
```

---

### 📈 All Visualizations with `StatevectorSampler`

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram, plot_distribution
import matplotlib.pyplot as plt

# Create Bell state WITH measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # MUST have measurements!

# Run the sampler
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
counts = job.result()[0].data.meas.get_counts()

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 1: Histogram (measurement counts)
# ═══════════════════════════════════════════════════════════════
plot_histogram(counts, title="Histogram - Bell State Measurements")
plt.show()
# Shows: Bar chart with raw counts
# Best for: Seeing exact number of occurrences

# ═══════════════════════════════════════════════════════════════
# VISUALIZATION 2: Distribution (normalized probabilities)
# ═══════════════════════════════════════════════════════════════
plot_distribution(counts, title="Distribution - Bell State Probabilities")
plt.show()
# Shows: Normalized probability bars (sum to 1)
# Best for: Comparing relative probabilities

# ═══════════════════════════════════════════════════════════════
# Advanced: Histogram with options
# ═══════════════════════════════════════════════════════════════
plot_histogram(
    counts,
    title="Bell State Results",
    figsize=(10, 6),
    color='steelblue',
    bar_labels=True,      # Show values on bars
    sort='value_desc'     # Sort by frequency (descending)
)
plt.show()

# ═══════════════════════════════════════════════════════════════
# Advanced: Compare multiple runs
# ═══════════════════════════════════════════════════════════════
job1 = sampler.run([qc], shots=100)
job2 = sampler.run([qc], shots=1000)
job3 = sampler.run([qc], shots=10000)

counts1 = job1.result()[0].data.meas.get_counts()
counts2 = job2.result()[0].data.meas.get_counts()
counts3 = job3.result()[0].data.meas.get_counts()

plot_histogram(
    [counts1, counts2, counts3],
    legend=['100 shots', '1000 shots', '10000 shots'],
    title="Effect of Shot Count on Results"
)
plt.show()
```

**Visual Summary of StatevectorSampler Visualizations**:

```
┌─────────────────────────────────────────────────────────────────┐
│ plot_histogram(counts)                                          │
│                                                                  │
│  500 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  400 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  300 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  200 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  100 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│    0 ┼──────────────────────────────────                        │
│           00      01      10      11                            │
│                                                                  │
│  Shows: Raw counts (integers)                                   │
├─────────────────────────────────────────────────────────────────┤
│ plot_distribution(counts)                                       │
│                                                                  │
│  0.5 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  0.4 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  0.3 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  0.2 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│  0.1 ┤      ▓▓▓▓                    ▓▓▓▓                        │
│    0 ┼──────────────────────────────────                        │
│           00      01      10      11                            │
│                                                                  │
│  Shows: Normalized probabilities (0 to 1)                       │
└─────────────────────────────────────────────────────────────────┘
```

---

### ❌ Common Errors: Wrong Visualization + Wrong Tool

```python
# ═══════════════════════════════════════════════════════════════
# ERROR 1: Using Statevector visualizations with counts
# ═══════════════════════════════════════════════════════════════
counts = {'00': 500, '11': 500}

plot_state_city(counts)        # ❌ TypeError! Expects Statevector
plot_state_qsphere(counts)     # ❌ TypeError! Expects Statevector
plot_bloch_multivector(counts) # ❌ TypeError! Expects Statevector

# ═══════════════════════════════════════════════════════════════
# ERROR 2: Using histogram visualizations with Statevector
# ═══════════════════════════════════════════════════════════════
state = Statevector(qc)

plot_histogram(state)          # ❌ TypeError! Expects dict
plot_distribution(state)       # ❌ TypeError! Expects dict

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: Match visualization to data type
# ═══════════════════════════════════════════════════════════════

# For Statevector → Use state visualizations
state = Statevector(qc)
plot_state_city(state)         # ✅ Correct!
plot_bloch_multivector(state)  # ✅ Correct!

# For counts → Use histogram visualizations
counts = sampler.run([qc_with_meas]).result()[0].data.meas.get_counts()
plot_histogram(counts)         # ✅ Correct!
plot_distribution(counts)      # ✅ Correct!
```

---

### 🎯 Quick Reference: Choosing the Right Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│ QUESTION: What do you have?                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Statevector (no measurements)          counts dict (measured)   │
│         │                                       │                │
│         ▼                                       ▼                │
│ ┌───────────────────┐                 ┌───────────────────┐     │
│ │ State Visualizations│               │ Result Visualizations│  │
│ ├───────────────────┤                 ├───────────────────┤     │
│ │ • plot_state_city │                 │ • plot_histogram  │     │
│ │ • plot_state_qsphere│               │ • plot_distribution│    │
│ │ • plot_bloch_multivector│           │                   │     │
│ │ • plot_state_hinton│                │                   │     │
│ │ • plot_state_paulivec│              │                   │     │
│ └───────────────────┘                 └───────────────────┘     │
│                                                                  │
│ REMEMBER:                                                        │
│ • Statevector = Quantum info (complex amplitudes, phase)        │
│ • counts = Classical info (integers, no phase)                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Why This Matters**:
- **plot_state_city**: Useful for understanding algorithms, debugging, teaching
  - ⚠️ Only works in simulation (can't get Statevector from real hardware!)
- **plot_histogram**: Useful for real experiments, validating results
  - ✅ Works with both simulators AND real quantum hardware

**Exam Trap**:
```python
# ❌ WRONG: Can't use plot_state_city with measurement counts
plot_state_city(counts)  # ERROR! Expects Statevector

# ❌ WRONG: Can't use plot_histogram with Statevector
plot_histogram(state)    # ERROR! Expects dictionary

# ✅ CORRECT usage:
plot_state_city(Statevector(qc))   # Quantum state
plot_histogram(counts)              # Classical counts
```

---

### 3. Probability Distribution

```python
from qiskit.visualization import plot_state_qsphere

# Q-sphere: Shows probabilities on sphere
plot_state_qsphere(state)
```

**Q-Sphere Visualization**:
```
     Sphere with basis states marked:
     • Marker size ∝ probability
     • Color = phase
     • Position = basis state

     Example: Bell state
     • |00⟩: large marker at one position
     • |11⟩: large marker at opposite position
     • |01⟩, |10⟩: no markers (probability = 0)
```

### 4. Density Matrix (Mixed States)

```python
from qiskit.visualization import plot_state_hinton

# Hinton diagram: Visualize density matrix
state = Statevector(qc)
plot_state_hinton(state)
```

**Hinton Plot**:
```
     |00⟩ |01⟩ |10⟩ |11⟩
|00⟩  ▓         
|01⟩            
|10⟩            
|11⟩            ▓

Square size = matrix element magnitude
White = positive, Black = negative
```

---

## 📊 Measurement Visualization

### Histogram (Classical Results)

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Circuit with measurement
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

# Run and get counts
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.meas.get_counts()

# Visualize results
plot_histogram(counts)
```

**Histogram Output**:
```
      Measurement Counts
      
 500 ┤           ▓▓▓
     │           ▓▓▓
 400 ┤           ▓▓▓
     │           ▓▓▓
 300 ┤           ▓▓▓      ▓▓▓
     │           ▓▓▓      ▓▓▓
 200 ┤           ▓▓▓      ▓▓▓
     │           ▓▓▓      ▓▓▓
 100 ┤           ▓▓▓      ▓▓▓
     │           ▓▓▓      ▓▓▓
   0 ┼───────────────────────
         00   01   10   11
         
Bell state: ~50% |00⟩, ~50% |11⟩
(Perfect correlation)
```

### Multiple Histogram Comparison

```python
from qiskit.visualization import plot_histogram

# Compare different circuits
counts1 = {'00': 500, '11': 500}  # Bell state
counts2 = {'00': 250, '01': 250, '10': 250, '11': 250}  # Uniform

plot_histogram([counts1, counts2], legend=['Bell', 'Uniform'])
```

---

## 🎨 Advanced Visualization Options

### Custom Plot Styling

```python
from qiskit.visualization import plot_histogram

counts = {'00': 480, '01': 20, '10': 15, '11': 485}

plot_histogram(
    counts,
    title='Bell State Measurements',
    figsize=(10, 6),
    color='midnightblue',
    bar_labels=True,  # Show count values on bars
    sort='value'      # Sort by frequency
)
```

### Saving Figures

```python
# Circuit diagram
qc.draw(output='mpl', filename='my_circuit.png')

# State visualization
from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(state, filename='bloch.png')

# Histogram
plot_histogram(counts, filename='results.png')
```

---

## 📋 Visualization Function Reference

### Circuit Drawing

| Function | Output | Best For |
|----------|--------|----------|
| `qc.draw()` | Text | Console, terminal |
| `qc.draw('mpl')` | Matplotlib | Reports, presentations |
| `qc.draw('latex')` | LaTeX | Publications, papers |
| `qc.draw('text')` | ASCII | Documentation |

### State Visualization

| Function | Input | Visualizes | Best For |
|----------|-------|------------|----------|
| `plot_bloch_multivector()` | Statevector | Bloch spheres | 1-3 qubits |
| `plot_state_city()` | Statevector | 3D bars | Amplitudes (real/imag) |
| `plot_state_qsphere()` | Statevector | Sphere with markers | Probabilities + phase |
| `plot_state_hinton()` | Statevector | Density matrix | Entanglement, mixed states |
| `plot_state_paulivec()` | Statevector | Pauli decomposition | Quantum chemistry |

### Measurement Results

| Function | Input | Visualizes | Best For |
|----------|-------|------------|----------|
| `plot_histogram()` | Dict | Bar chart | Measurement counts |
| `plot_distribution()` | Dict | Probability bars | Normalized results |

---

## ✅ Exam Tips

### Must Know for Certification

1. **Default drawing**: `qc.draw()` → text output
2. **Matplotlib**: `qc.draw('mpl')` → high-quality figure
3. **Reverse bits**: `reverse_bits=True` puts MSB on top
4. **Bloch sphere**: `plot_bloch_multivector()` for single qubits
5. **Histogram**: `plot_histogram(counts)` for measurement results
6. **Fold circuits**: `fold=N` wraps long circuits after N columns
7. **State vector**: Use `Statevector(qc)` before visualization
8. **Multiple plots**: Pass list to `plot_histogram([counts1, counts2])`

### Common Exam Questions

**Q: How do you draw a circuit in matplotlib format?**
```python
qc.draw(output='mpl')  # or qc.draw('mpl')
```

**Q: How to visualize a single-qubit state on Bloch sphere?**
```python
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

state = Statevector(qc)
plot_bloch_multivector(state)
```

**Q: How to create a histogram from measurement counts?**
```python
from qiskit.visualization import plot_histogram
plot_histogram(counts)
```

**Q: What parameter shows qubits in reverse order?**
```python
qc.draw(reverse_bits=True)  # MSB on top
```

---

## 🎯 Practice Examples

### Example 1: Visualize Bell State

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city

# Create Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Draw circuit
print(qc.draw())

# Get state
state = Statevector(qc)

# Visualize on Bloch spheres (2 qubits = 2 spheres)
plot_bloch_multivector(state)

# 3D city plot
plot_state_city(state)
```

### Example 2: Compare Algorithm Results

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Algorithm 1: Superposition
qc1 = QuantumCircuit(2, 2)
qc1.h([0, 1])
qc1.measure([0,1], [0,1])

# Algorithm 2: Entanglement
qc2 = QuantumCircuit(2, 2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0,1], [0,1])

# Run both
sampler = StatevectorSampler()
job1 = sampler.run([qc1], shots=1000)
job2 = sampler.run([qc2], shots=1000)

counts1 = job1.result()[0].data.meas.get_counts()
counts2 = job2.result()[0].data.meas.get_counts()

# Compare
plot_histogram([counts1, counts2], legend=['Superposition', 'Entangled'])
```

---

### 📖 Key Concepts: Superposition vs Entanglement

#### **Superposition**

**Definition**: Superposition is the quantum mechanical principle where a single qubit exists in **multiple states simultaneously** until measured. A qubit in superposition is not in state |0⟩ OR |1⟩, but in a combination of BOTH at the same time.

**Mathematical Form**:
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

Where $|\alpha|^2 + |\beta|^2 = 1$ (probabilities must sum to 1)

**Key Characteristics**:
- Applies to a **single qubit** (or independent qubits)
- Created using **Hadamard gate (H)**: `qc.h(0)`
- Upon measurement, collapses to ONE definite state
- Probabilities determined by amplitudes α and β

**Example**:
```python
qc = QuantumCircuit(2)
qc.h(0)  # Qubit 0 in superposition: (|0⟩ + |1⟩)/√2
qc.h(1)  # Qubit 1 in superposition: (|0⟩ + |1⟩)/√2
# Each qubit is INDEPENDENTLY in superposition
# Combined state: (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2
# Measurement results: ~25% for each of 00, 01, 10, 11
```

---

#### **Entanglement**

**Definition**: Entanglement is a quantum phenomenon where two or more qubits become **correlated** such that the quantum state of one qubit **cannot be described independently** of the others. Measuring one instantly determines the state of the other(s), regardless of distance.

**Mathematical Form** (Bell State):
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**Key Characteristics**:
- Requires **multiple qubits** (minimum 2)
- Created using **H gate + CNOT**: `qc.h(0); qc.cx(0, 1)`
- Qubits are **correlated** — measuring one affects the other
- Individual qubits appear "mixed" when viewed alone
- "Spooky action at a distance" — Einstein's famous description

**Example**:
```python
qc = QuantumCircuit(2)
qc.h(0)       # Put qubit 0 in superposition
qc.cx(0, 1)   # Entangle qubit 0 and qubit 1
# Combined state: (|00⟩ + |11⟩)/√2 (Bell state)
# Measurement results: ~50% for 00, ~50% for 11
# NEVER see 01 or 10 — qubits are perfectly correlated!
```

---

#### **🔍 Key Differences: Superposition vs Entanglement**

| Aspect | Superposition | Entanglement |
|--------|---------------|--------------|
| **Applies to** | Single qubit (or independent qubits) | Multiple qubits (minimum 2) |
| **Definition** | One qubit in multiple states at once | Multiple qubits with correlated states |
| **Independence** | Qubits are independent | Qubits cannot be described independently |
| **Creation** | H gate alone: `qc.h(0)` | H + CNOT: `qc.h(0); qc.cx(0,1)` |
| **Measurement correlation** | Independent outcomes | Correlated outcomes |
| **Example state** | $(|0\rangle + |1\rangle)/\sqrt{2}$ | $(|00\rangle + |11\rangle)/\sqrt{2}$ |
| **Possible outcomes** | All combinations (00, 01, 10, 11) | Only correlated pairs (00, 11) |
| **Histogram pattern** | 4 equal bars (uniform) | 2 bars only (correlated) |

**Visual Comparison**:

```
SUPERPOSITION (2 independent qubits):         ENTANGLEMENT (2 correlated qubits):
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│  qc.h(0)                        │           │  qc.h(0)                        │
│  qc.h(1)                        │           │  qc.cx(0, 1)                    │
│                                 │           │                                 │
│  Histogram:                     │           │  Histogram:                     │
│   25%  25%  25%  25%            │           │   50%              50%          │
│   ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓            │           │   ▓▓▓▓▓▓            ▓▓▓▓▓▓      │
│   00   01   10   11             │           │   00   01   10   11             │
│                                 │           │         (none) (none)           │
│  Each qubit decides             │           │  Qubits decide                  │
│  INDEPENDENTLY                  │           │  TOGETHER                       │
└─────────────────────────────────┘           └─────────────────────────────────┘
```

**Conceptual Analogy**:

```
SUPERPOSITION = Flipping 2 independent coins
  • Each coin is heads AND tails until you look
  • Looking at coin 1 tells you nothing about coin 2
  • All 4 outcomes equally likely: HH, HT, TH, TT

ENTANGLEMENT = Two magic coins that are linked
  • Both coins are in superposition together
  • If coin 1 shows heads, coin 2 MUST show heads
  • If coin 1 shows tails, coin 2 MUST show tails
  • Only 2 outcomes possible: HH or TT
  • "Looking" at one instantly determines the other
```

**Why This Matters for the Exam**:
- Superposition enables **quantum parallelism** — process multiple states at once
- Entanglement enables **quantum teleportation**, **superdense coding**, and **quantum error correction**
- Both are required for **quantum advantage** over classical computers
- Exam questions often test whether you can distinguish superposition from entanglement based on measurement outcomes

---

### Example 3: Custom Circuit Visualization

```python
from qiskit import QuantumCircuit

# Create complex circuit
qc = QuantumCircuit(4, 4)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)
qc.barrier()
qc.measure(range(4), range(4))

# Professional styling
qc.draw(
    output='mpl',
    reverse_bits=True,     # MSB on top
    fold=25,               # Fold after 25 columns
    scale=1.3,             # 130% size
    idle_wires=False,      # Hide idle wires
    style={
        'backgroundcolor': '#FFFFFF',
        'linecolor': '#000000',
        'textcolor': '#000000'
    },
    filename='ghz_circuit.png'
)
```

---

## 📁 Files in This Section

1. **`circuit_visualization.py`** - All circuit drawing methods and styles
2. **`state_visualization.py`** - Bloch sphere, state vector, Q-sphere plots

---

## 🎓 Key Takeaways

```
✓ qc.draw() is your debugging friend
✓ Bloch sphere for single qubits
✓ Histograms for measurement results
✓ plot_state_city() for multi-qubit amplitudes
✓ Visualization catches bugs faster than print statements!
```

---

## 🔗 Next Steps

1. Practice drawing circuits with different styles
2. Visualize states at each step of an algorithm
3. Use histograms to verify algorithm correctness
4. Move to **Section 3 (Circuit Creation)** to build complex circuits

**Remember: Visualization is not just for pretty pictures - it's for understanding!** 🎨✨
