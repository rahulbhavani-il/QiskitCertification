# Section 5: Sampler Primitive (12% of Exam)

> **Exam Weight**: ~8 questions | **Difficulty**: Medium-High | **Must Master**: ✅✅✅

---

## 📖 Overview

**Sampler** is the NEW way (Qiskit 1.0+) to get measurement statistics from quantum circuits. Understanding Sampler is ABSOLUTELY CRITICAL for the certification exam!

```
Old Way (Deprecated):              New Way (Qiskit 1.0+):
    execute()                          Sampler
    Aer.get_backend()                  
    backend.run()   
❌ DON'T use these anymore!        ✅ Use Sampler Primitive!
```

### What You'll Learn

- Get measurement statistics (counts, probabilities)
- SamplerV2 API and PUB (Primitive Unified Blocs) format
- Multi-circuit execution
- Result extraction patterns

---

## 🎯 Core Concepts

### What are Primitives?

**Primitives** are high-level computational building blocks that provide a simplified interface for running quantum computations.

```
Primitives = Simplified quantum execution interface

Why Primitives?
✓ Hardware-agnostic (same code for simulator/hardware)
✓ Auto-transpilation
✓ Error mitigation built-in
✓ Cleaner, more Pythonic API
✓ Future-proof (IBM's long-term direction)

Two Core Primitives:
• Sampler  → Measurement outcomes (bitstrings, counts)
• Estimator → Expectation values (observables)
```

### 🧠 Analogy: The Loaded Die

Using a `Sampler` is like rolling a loaded die to figure out its bias:
- **Circuit**: The manufacturing process of the die
- **Shots**: How many times you roll it (e.g., 1000 times)
- **Quasi-Probabilities**: Mathematical correction for error mitigation

### Visual: Sampler Workflow

```
┌─────────────────────────────────────────────────────┐
│                 Your Circuit                         │
│     ┌───┐                                           │
│ q: ─┤ H ├──■────M                                   │
│     └───┘┌─┴─┐  │                                   │
│ q: ──────┤ X ├──M                                   │
│          └───┘                                       │
└─────────────────────────────────────────────────────┘
                    │
               ┌────▼─────┐
               │ Sampler  │
               └────┬─────┘
                    │
               ┌────▼────────┐
               │ Measurement │
               │   Counts    │
               │ {'00':512,  │
               │  '11':512}  │
               └─────────────┘
```

---

## 📊 Using the Sampler Primitive

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler  # For simulation

# Create circuit with measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # MUST add measurements for Sampler!

# Create Sampler
sampler = StatevectorSampler()

# Run circuit
job = sampler.run([qc], shots=1024)

# Get results
result = job.result()
counts = result[0].data.meas.get_counts()

print(counts)  # {'00': 512, '11': 512}
```

### Sampler with Real Hardware

```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Connect to IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibmq_qasm_simulator')

# Create Sampler with backend
sampler = Sampler(backend=backend)

# Run circuit
job = sampler.run([qc], shots=1024)

# Results
result = job.result()
counts = result[0].data.meas.get_counts()
```

### Multiple Circuits with Sampler

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create multiple circuits
qc1 = QuantumCircuit(2, 2)
qc1.h([0, 1])
qc1.measure([0,1], [0,1])

qc2 = QuantumCircuit(2, 2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0,1], [0,1])

# Run all at once
sampler = StatevectorSampler()
job = sampler.run([qc1, qc2], shots=1024)

# Get results for each
results = job.result()

counts1 = results[0].data.meas.get_counts()
counts2 = results[1].data.meas.get_counts()

print(f"Circuit 1: {counts1}")  # Uniform: ~25% each
print(f"Circuit 2: {counts2}")  # Bell: ~50% |00⟩, ~50% |11⟩
```

### PUB Format (Primitive Unified Blocs)

**EXAM CRITICAL**: Correct PUB syntax!

```python
# PUB = (circuit, parameter_values, shots)

# Single circuit, no parameters
pub = (qc,)  # ← Note trailing comma!

# With parameter values
from qiskit.circuit import Parameter
theta = Parameter('θ')
qc_param = QuantumCircuit(1)
qc_param.ry(theta, 0)

pub = (qc_param, [0.5])  # θ = 0.5

# With custom shots
pub = (qc, None, 2048)  # 2048 shots for this circuit

# Multiple parameter sets
pubs = [
    (qc_param, [0.0]),
    (qc_param, [0.5]),
    (qc_param, [1.0])
]
job = sampler.run(pubs)
```

**Common PUB Mistakes**:

```python
❌ WRONG: sampler.run([circuit])  # Missing tuple!
✅ RIGHT: sampler.run([(circuit,)])

❌ WRONG: sampler.run((circuit))  # Missing comma (not a tuple!)
✅ RIGHT: sampler.run([(circuit,)])

❌ WRONG: sampler.run([(circuit, [0.5])])  # List instead of tuple
✅ RIGHT: sampler.run([(circuit, [0.5])])  # This is actually OK!
```

### ⚠️ EXAM CRITICAL: PUB Format Complete Reference

| Scenario | PUB Format | Example |
|----------|------------|----------|
| Single circuit, no params | `[(circuit,)]` | `sampler.run([(qc,)])` |
| Single circuit with params | `[(circuit, params)]` | `sampler.run([(qc, [0.5, 1.2])])` |
| Multiple circuits | `[(qc1,), (qc2,)]` | `sampler.run([(qc1,), (qc2,)])` |
| Custom shots per circuit | `[(circuit, None, shots)]` | `sampler.run([(qc, None, 2048)])` |
| Everything custom | `[(circuit, params, shots)]` | `sampler.run([(qc, [0.5], 4096)])` |

**Memory Aid: "Tuple in List"**
- **Outer**: List `[...]` of PUBs (even if just one)
- **Inner**: Tuple `(...)` for each PUB (note trailing comma!)
- **Order**: `(circuit, parameters, shots)` - remember CPS!

**Trap: Trailing Comma**
```python
(circuit)    # NOT a tuple! Just a circuit in parentheses
(circuit,)   # Tuple with one element ✓
```

**Trap: Sampler REQUIRES measurements**
```python
qc = QuantumCircuit(1)
qc.h(0)
# ❌ sampler.run([(qc,)])  # ERROR! No measurements

qc.measure_all()
# ✅ sampler.run([(qc,)])  # OK!
```

### 🎓 Exam Question Patterns - Sampler

**Pattern 1: "What's the correct PUB format?"**
```python
# Look for these WRONG patterns:
❌ sampler.run(qc)              # Not wrapped
❌ sampler.run([qc])            # Not tuple
❌ sampler.run((qc))            # Missing comma
❌ sampler.run([(qc)])          # Still missing comma

# CORRECT:
✅ sampler.run([(qc,)])         # Tuple in list!
```

**Pattern 2: "How to access counts?"**
```python
# Chain of attributes (MEMORIZE!):
result[0].data.meas.get_counts()
   ↑       ↑    ↑       ↑
   │       │    │       └─ Method to call
   │       │    └───────── Measurement register name
   │       └───────────── Data attribute
   └─────────────────── Index (which circuit)
```

**Pattern 3: "Sampler vs Estimator?"**
```
## Explain the difference:
Sampler → Measurement outcomes (bitstrings)
Estimator → Expectation values (observables)

Sampler needs: measure() in circuit
Estimator needs: Observable (no measure!)
```

### ✅ Pre-Flight Checklist - Using Sampler

```
□ Circuit has measure() or measure_all()?
□ Using tuple format: [(circuit,)]?
□ Accessing results: result[0].data.meas.get_counts()?
□ Handling multiple circuits: result[i] for each?
□ Shots parameter: Default 1024, or custom in PUB?
```

### Extracting Results from Sampler

```python
result = job.result()

# For each PUB/circuit:
pub_result = result[0]

# Get counts (dict)
counts = pub_result.data.meas.get_counts()
# {'00': 502, '11': 498}

# Get bit array (raw measurements)
bitarray = pub_result.data.meas
# BitArray with shape (shots, n_bits)

# Metadata
metadata = pub_result.metadata
print(f"Shots: {metadata['shots']}")
```

---

## 🔄 Sampler vs Estimator: When to Use?

```
┌────────────────────────────────────────────┐
│         Use Sampler When:                   │
├────────────────────────────────────────────┤
│ • You want measurement counts              │
│ • Need to sample output distribution       │
│ • Testing classical output                 │
│ • Debugging circuits                       │
│ • Grover's algorithm (find marked state)   │
│ • Quantum Machine Learning classification  │
└────────────────────────────────────────────┘

EXAM TIP:
- Counts/Probabilities → Sampler (Section 5)
- Expectation values → Estimator (Section 6)
```

---

## 💡 Practical Patterns

### Pattern 1: Circuit Debugging with Sampler

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Suspected buggy circuit
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)  # Intended GHZ state
qc.measure([0,1,2], [0,1,2])

# Sample to verify
sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
counts = job.result()[0].data.meas.get_counts()

print(counts)
# Expected: {'000': ~500, '111': ~500}
# If different, there's a bug!
```

### Pattern 2: Multi-Circuit Comparison

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create variations
circuits = []
for n_layers in [1, 2, 3, 4]:
    qc = QuantumCircuit(3, 3)
    for _ in range(n_layers):
        qc.h([0, 1, 2])
        qc.cx(0, 1)
        qc.cx(1, 2)
    qc.measure([0,1,2], [0,1,2])
    circuits.append(qc)

# Run all
sampler = StatevectorSampler()
job = sampler.run(circuits, shots=1024)
results = job.result()

# Analyze
for i, result in enumerate(results):
    counts = result.data.meas.get_counts()
    print(f"Layers {i+1}: {counts}")
```

### Pattern 3: Probability Distribution Analysis

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create superposition
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.h(1)
qc.measure([0, 1], [0, 1])

# Sample
sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=4096)
counts = job.result()[0].data.meas.get_counts()

# Convert to probabilities
total = sum(counts.values())
probs = {state: count/total for state, count in counts.items()}

print("Probability distribution:")
for state, prob in sorted(probs.items()):
    print(f"|{state}⟩: {prob:.3f}")
# Expected: ~0.25 for each of |00⟩, |01⟩, |10⟩, |11⟩
```

---

## 🎯 Practice Problems

### Problem 1: Measure GHZ State

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create GHZ
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

# Sample
sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
counts = job.result()[0].data.meas.get_counts()

print(counts)
# Expected: {'000': ~500, '111': ~500}
```

### Problem 2: W-State Verification

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
import math

# Create W-state: (|100⟩ + |010⟩ + |001⟩)/√3
qc = QuantumCircuit(3, 3)
qc.ry(2*math.acos(math.sqrt(1/3)), 0)
qc.ch(0, 1)
qc.x(0)
qc.ccx(0, 1, 2)
qc.x(0)
qc.measure([0, 1, 2], [0, 1, 2])

# Sample
sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=3000)
counts = job.result()[0].data.meas.get_counts()

print(counts)
# Expected: roughly equal distribution among |001⟩, |010⟩, |100⟩
```

### Problem 3: Parameterized Circuit Sweep

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
import numpy as np

# Parameterized circuit
theta = Parameter('θ')
qc = QuantumCircuit(1, 1)
qc.ry(theta, 0)
qc.measure(0, 0)

# Sweep parameter
sampler = StatevectorSampler()
angles = np.linspace(0, np.pi, 5)

pubs = [(qc, [angle]) for angle in angles]
job = sampler.run(pubs, shots=1024)
results = job.result()

print("Parameter sweep results:")
for i, angle in enumerate(angles):
    counts = results[i].data.meas.get_counts()
    prob_1 = counts.get('1', 0) / 1024
    print(f"θ = {angle:.3f}: P(|1⟩) = {prob_1:.3f}")
```

---

## 📁 Files in This Section

**Section 5 - Sampler**:
1. **`sampler_primitive.ipynb`** - Complete Sampler tutorial with examples

---

## 🎓 Key Takeaways

```
✅ Sampler = measurement counts and probabilities
✅ PUB format: [(circuit,)] with trailing comma!
✅ Sampler REQUIRES measurements in circuit
✅ result[0].data.meas.get_counts() for results
✅ StatevectorSampler for simulation, SamplerV2 for hardware
✅ Multiple circuits can be run simultaneously
✅ 12% of exam - MASTER THIS!
```

---

## 🔗 Next Steps

1. Practice PUB format thoroughly
2. Master result extraction patterns
3. Try multi-circuit execution
4. Debug circuits using Sampler
5. Move to **Section 6 (Estimator)** for expectation values
6. Then **Section 7 (Results)** for advanced result processing

**Sampler is essential for the exam - know it inside out!** 🚀📊

