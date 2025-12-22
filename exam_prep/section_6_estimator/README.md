# Section 6: Estimator Primitive & VQE/QAOA

> **Exam Weight**: ~12% (~8 questions) | **Difficulty**: Medium-High | **Must Master**: ✅✅✅

---

## 📖 Overview

**Estimator** is the NEW way (Qiskit 1.0+) to calculate expectation values of quantum observables. This primitive is CRITICAL for variational algorithms like VQE and QAOA!

```
Old Way (Deprecated):              New Way (Qiskit 1.0+):
    execute() + manual calc           Estimator
    backend.run() + pauli ops          
    
❌ DON'T use these anymore!        ✅ Use Estimator Primitive!
```

### What You'll Learn

| Topic | Key Concepts | Exam Focus |
|-------|--------------|------------|
| Estimator Primitive | `StatevectorEstimator`, expectation values | ⚠️ HIGH |
| SparsePauliOp | Observable construction, qubit ordering | ⚠️ HIGH |
| PUB Format | (circuit, observable, params, precision) | ⚠️ HIGH |
| Result Extraction | `.data.evs`, `.data.stds` | ⚠️ HIGH |
| Error Mitigation | ResilienceOptionsV2, ZNE, M3 | MEDIUM |
| VQE Pattern | scipy.optimize, cost function | ⚠️ HIGH |
| QAOA Pattern | MaxCut, cost/mixer layers | MEDIUM |

---

## 📊 Topics Quick Reference

| Topic | API/Pattern | Common Trap | Mnemonic |
|-------|-------------|-------------|----------|
| Estimator | `StatevectorEstimator()` | Adding measurements | "ENM" = Estimator No Measures |
| Observable | `SparsePauliOp('ZZ')` | String qubit order | "TiPO" = Tensor in Pauli Order |
| PUB Format | `[(qc, obs, params, prec)]` | Missing observable | "COPPP" = Circuit Observable Params Precision |
| Result | `result[0].data.evs` | Missing 's' plural | "0-D-EV-S" = [0].data.evs |
| VQE | `scipy.optimize.minimize` | Wrong optimizer | "COBYLA for Quantum" |
| QAOA | `rzz()` + `rx()` layers | Wrong layer order | "CostMix" = Cost then Mixer |

---

## 🛤️ Learning Path

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Estimator     │────▶│   Observables   │────▶│  Result Access  │
│   Primitive     │     │  SparsePauliOp  │     │   .data.evs     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                                               │
         └───────────────────┬───────────────────────────┘
                             ▼
         ┌─────────────────────────────────────┐
         │         Variational Algorithms      │
         │  ┌───────────┐     ┌───────────┐   │
         │  │    VQE    │     │   QAOA    │   │
         │  │  Ground   │     │  MaxCut   │   │
         │  │  Energy   │     │  Graphs   │   │
         │  └───────────┘     └───────────┘   │
         └─────────────────────────────────────┘
```

---

## 🎯 Conceptual Deep Dive

### Measurement vs Expectation Value

| Aspect | Measurement (Sampler) | Expectation Value (Estimator) |
|--------|----------------------|-------------------------------|
| **Output** | Counts dictionary `{'00': 512}` | Real number `⟨O⟩ = 0.73` |
| **Circuit** | Needs `measure()` | NO `measure()` |
| **Returns** | Classical bit strings | Observable average |
| **Use Case** | Get bitstrings, Grover's | Calculate ⟨H⟩ for VQE |
| **Post-processing** | Manual | Automatic |

### 🧠 Mathematical Foundation

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Expectation Value Formula:
⟨O⟩ = ⟨ψ|O|ψ⟩ = Σᵢ λᵢ |⟨φᵢ|ψ⟩|²

Where:
• |ψ⟩ = quantum state (e.g., |+⟩, Bell state)
• O = observable operator (e.g., Z, XX, Hamiltonian)
• λᵢ = eigenvalues of O
• |φᵢ⟩ = eigenstates of O
• |⟨φᵢ|ψ⟩|² = probability of measuring eigenstate |φᵢ⟩

Physical Interpretation:
The expectation value is the weighted average of all possible measurement
outcomes, where weights are the probabilities of each outcome.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 1: Z operator on |+⟩ state

State: |+⟩ = 1/√2(|0⟩ + |1⟩)
Observable: Z = |0⟩⟨0| - |1⟩⟨1|

⟨Z⟩ = ⟨+|Z|+⟩
    = 1/2(⟨0| + ⟨1|) · (|0⟩ - |1⟩)
    = 1/2(1 - 0 + 0 - 1) = 0

Using eigenvalue decomposition:
P(|0⟩) = 1/2 → (+1)·(1/2) = +1/2
P(|1⟩) = 1/2 → (-1)·(1/2) = -1/2
⟨Z⟩ = +1/2 - 1/2 = 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 2: ZZ on Bell state |Φ⁺⟩ = 1/√2(|00⟩ + |11⟩)

ZZ eigenvalues:
|00⟩ → (+1)(+1) = +1
|11⟩ → (-1)(-1) = +1

⟨ZZ⟩ = (+1)·(1/2) + (+1)·(1/2) = 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Variational Principle (VQE Foundation):

For any quantum state |ψ⟩ and Hamiltonian H:
⟨ψ|H|ψ⟩ ≥ E₀

where E₀ is the ground state energy (lowest eigenvalue).

This is why VQE works: minimizing ⟨H⟩ pushes toward ground state!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Visual: Estimator Workflow

```
┌─────────────────────────────────────────────────────┐
│                 Your Circuit                         │
│     ┌───┐                                           │
│ q: ─┤ H ├──■──   (NO measurements needed!)          │
│     └───┘┌─┴─┐                                      │
│ q: ──────┤ X ├──                                    │
│          └───┘                                       │
└─────────────────────────────────────────────────────┘
                    │
               ┌────▼──────┐
               │ Estimator │
               │+ Observable│
               │   (ZZ, XX) │
               └────┬───────┘
                    │
               ┌────▼──────────┐
               │ Expectation   │
               │    Values     │
               │  ⟨ZZ⟩ = 1.0   │
               │  ⟨XX⟩ = 1.0   │
               └───────────────┘
```

---

# 📚 Topic 1: Estimator Primitive

## 1.1 StatevectorEstimator

### 📝 Definition
**StatevectorEstimator** is a local simulator that calculates exact expectation values using statevector simulation. It requires NO measurements in the circuit.

### 🎭 Real-World Analogy
Think of Estimator like a **voting poll analyst**:
- **Sampler** = Actually running an election (count individual votes)
- **Estimator** = Polling expert who calculates the expected outcome without counting every vote
- The analyst uses mathematical models to predict averages, not individual results

### 📐 Visual Representation

```
Sampler:                          Estimator:
┌─────────┐                       ┌─────────┐
│ Circuit │                       │ Circuit │
│ + meas  │                       │ NO meas │
└────┬────┘                       └────┬────┘
     │                                 │
     ▼                                 ▼
┌─────────┐                       ┌────────────┐
│  Counts │                       │ Observable │
│ {'00':5}│                       │   'ZZ'     │
└─────────┘                       └─────┬──────┘
                                       │
                                       ▼
                                  ┌─────────┐
                                  │ ⟨ZZ⟩=1.0│
                                  └─────────┘
```

### 💻 Implementation

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create circuit (NO measurements!)
qc = QuantumCircuit(1)
qc.h(0)  # Create |+⟩

# Define observable
observable = SparsePauliOp("Z")

# Create Estimator and run
estimator = StatevectorEstimator()
job = estimator.run([(qc, observable)])  # Note: (circuit, observable) tuple

# Get result
result = job.result()
expectation_value = result[0].data.evs
print(f"⟨Z⟩ = {expectation_value}")  # ≈ 0.0
```

### ⚠️ Exam Trap: Estimator Requires NO Measurements

```python
# ❌ WRONG - Circuit has measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()  # THIS CAUSES ERROR!
estimator.run([(qc, observable)])  # ERROR!

# ✅ CORRECT - No measurements
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO measure() calls
estimator.run([(qc, observable)])  # Works!
```

### 🧠 Mnemonic: "ENM" = Estimator No Measures
> **E**stimator **N**eeds **N**o **M**easures
> 
> Opposite of Sampler: **S**ampler **N**eeds **M**easures (SNM)

### ✅ Quick Check
**Q: What happens if you add `measure_all()` to a circuit before running with Estimator?**

<details>
<summary>Answer</summary>

The Estimator will raise an error or produce incorrect results. Estimator calculates ⟨O⟩ mathematically - it doesn't sample measurement outcomes. Remove all measurement operations before using Estimator.

</details>

---

## 1.2 Hardware Estimator (EstimatorV2)

### 📝 Definition
**EstimatorV2** is the IBM Runtime estimator for real quantum hardware. It includes error mitigation options.

### 🎭 Real-World Analogy
Like upgrading from a **local calculator** to a **cloud supercomputer**:
- StatevectorEstimator = Calculator on your desk (exact, limited size)
- EstimatorV2 = Remote supercomputer (noisy, unlimited scale, needs error correction)

### 💻 Implementation

```python
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator

# Connect to IBM Runtime
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Create hardware Estimator
estimator = Estimator(mode=backend)

# Configure options
estimator.options.resilience_level = 1  # M3 mitigation
estimator.options.default_shots = 4096

# Run (same API!)
job = estimator.run([(qc, observable)])
result = job.result()
evs = result[0].data.evs
stds = result[0].data.stds  # Standard deviations
```

### ⚠️ Exam Trap: evs and stds are PLURAL

```python
# ❌ WRONG - Missing 's'
result[0].data.ev   # AttributeError!
result[0].data.std  # AttributeError!

# ✅ CORRECT - Plural forms
result[0].data.evs   # Expectation values
result[0].data.stds  # Standard deviations
```

### 🧠 Mnemonic: "EVS has S" 
> Expectation **V**alue**S** = **evs** (always plural)
> Standard **D**eviation**S** = **stds** (always plural)

### ✅ Quick Check
**Q: What's the difference between `result[0].data.evs` and `result[0].data.stds`?**

<details>
<summary>Answer</summary>

- `evs` = Expectation values (the calculated ⟨O⟩ values)
- `stds` = Standard deviations (uncertainty/error bars on hardware)

For StatevectorEstimator, `stds` is always 0 (exact simulation). For hardware, `stds` reflects shot noise and errors.

</details>

---

# 📚 Topic 2: SparsePauliOp (Observables)

## 2.1 Basic Observable Construction

### 📝 Definition
**SparsePauliOp** represents quantum observables as sums of Pauli strings. It's how you tell Estimator WHAT to measure.

### 🎭 Real-World Analogy
Think of observables like **survey questions**:
- `SparsePauliOp('Z')` = "Is the qubit pointing up or down?"
- `SparsePauliOp('X')` = "Is the qubit pointing left or right?"
- `SparsePauliOp('ZZ')` = "Are both qubits pointing the same direction?"

### 📐 Visual Representation

```
Single-Qubit Observables:
┌─────────────────────────────────────────────┐
│  'Z' → measures ↑/↓ (computational basis)   │
│  'X' → measures ←/→ (superposition basis)   │
│  'Y' → measures ↻/↺ (phase basis)           │
│  'I' → identity (always 1)                  │
└─────────────────────────────────────────────┘

Multi-Qubit (Tensor Product):
'ZZ' = Z ⊗ Z = Z on qubit 0 AND Z on qubit 1
       ↑   ↑
      q0  q1
```

### 💻 Implementation

```python
from qiskit.quantum_info import SparsePauliOp

# Single Pauli operators
obs_z = SparsePauliOp('Z')     # Z on qubit 0
obs_x = SparsePauliOp('X')     # X on qubit 0

# Multi-qubit tensor products
obs_zz = SparsePauliOp('ZZ')   # Z⊗Z: Z on q0 AND Z on q1
obs_xy = SparsePauliOp('XY')   # X⊗Y: X on q0, Y on q1
obs_iz = SparsePauliOp('IZ')   # I⊗Z: Identity on q0, Z on q1

# Multiple terms (Hamiltonian)
H = SparsePauliOp(['ZZ', 'XX'], [0.5, 0.5])  # 0.5*ZZ + 0.5*XX

# H2 Molecule (EXAM COMMON!)
H2 = SparsePauliOp(
    ["II", "ZI", "IZ", "ZZ", "XX"],
    [-1.05, 0.39, 0.39, -0.01, 0.18]
)
```

### ⚠️ Exam Trap: Pauli String Qubit Ordering

```
STRING: 'ZXY' means:
  ┌───┬───┬───┐
  │ Z │ X │ Y │  → Tensor order (right-to-left in physics)
  └───┴───┴───┘
   q0  q1  q2

NOT visual left-to-right order!

SparsePauliOp('ZXY'):
  Qubit 0: Z (leftmost in string)
  Qubit 1: X 
  Qubit 2: Y (rightmost in string)
```

### 🧠 Mnemonic: "TiPO" = Tensor in Pauli Order
> **T**ensor product order **i**n **P**auli **O**rder
> 
> First character = qubit 0, Second = qubit 1, etc.
> "ZXY" = Z⊗X⊗Y where Z acts on q0

### ✅ Quick Check
**Q: For `SparsePauliOp('XIZ')`, which qubit has the Z operator?**

<details>
<summary>Answer</summary>

**Qubit 2** (the rightmost position in the string)
- 'X' → qubit 0
- 'I' → qubit 1 (identity, does nothing)
- 'Z' → qubit 2

</details>

---

## 2.2 Hamiltonian Construction

### 📝 Definition
A **Hamiltonian** is a sum of weighted Pauli terms representing a physical system's energy operator.

### 💻 Implementation

```python
from qiskit.quantum_info import SparsePauliOp

# Method 1: List of terms with coefficients
H = SparsePauliOp(
    ['ZZ', 'XX', 'YY'],    # Pauli terms
    [1.0, 0.5, 0.5]        # Coefficients
)
# = 1.0*ZZ + 0.5*XX + 0.5*YY

# Method 2: Single term
H_simple = SparsePauliOp('ZZ')  # Just ZZ with coefficient 1.0

# Method 3: Sum of SparsePauliOps
H1 = SparsePauliOp('ZZ', 1.0)
H2 = SparsePauliOp('XX', 0.5)
H_combined = H1 + H2  # ZZ + 0.5*XX

# H2 Molecule Hamiltonian (MEMORIZE for exam!)
H2_molecule = SparsePauliOp(
    ["II", "ZI", "IZ", "ZZ", "XX"],
    [-1.05, 0.39, 0.39, -0.01, 0.18]
)
```

### ⚠️ Exam Trap: Observable Must Be SparsePauliOp

```python
# ❌ WRONG - String not SparsePauliOp
estimator.run([(qc, 'ZZ')])  # ERROR!

# ❌ WRONG - List not SparsePauliOp  
estimator.run([(qc, ['ZZ', 'XX'])])  # ERROR!

# ✅ CORRECT - SparsePauliOp object
estimator.run([(qc, SparsePauliOp('ZZ'))])
estimator.run([(qc, SparsePauliOp(['ZZ', 'XX']))])
```

### 🧠 Mnemonic: "SPO not String"
> Estimator needs **S**parse**P**auli**O**p, **not** a **String**

### ✅ Quick Check
**Q: How do you create an observable for the Hamiltonian H = 2.0·ZZ - 0.5·XX?**

<details>
<summary>Answer</summary>

```python
H = SparsePauliOp(['ZZ', 'XX'], [2.0, -0.5])
```

</details>

---

# 📚 Topic 3: Estimator PUB Format

## 3.1 PUB Structure

### 📝 Definition
**PUB** (Primitive Unified Block) is the input format for Estimator: `(circuit, observable, parameter_values, precision)`.

### 📐 Visual Representation

```
PUB = (circuit, observable, parameter_values, precision)
        │         │              │               │
        │         │              │               └─ Optional: target precision (float)
        │         │              └─ Optional: list of parameter values
        │         └─ REQUIRED: SparsePauliOp observable
        └─ REQUIRED: QuantumCircuit (NO measurements!)
```

### 💻 Implementation

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

estimator = StatevectorEstimator()
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
obs = SparsePauliOp('ZZ')

# Scenario 1: Basic (circuit, observable)
job = estimator.run([(qc, obs)])

# Scenario 2: With parameter values
theta = Parameter('θ')
qc_param = QuantumCircuit(1)
qc_param.ry(theta, 0)
job = estimator.run([(qc_param, SparsePauliOp('Z'), [0.5])])

# Scenario 3: With precision (hardware)
job = estimator.run([(qc, obs, None, 0.01)])  # precision = 0.01

# Scenario 4: Multiple PUBs
pubs = [(qc, SparsePauliOp('ZZ')), 
        (qc, SparsePauliOp('XX')),
        (qc, SparsePauliOp('YY'))]
job = estimator.run(pubs)
```

### ⚠️ Exam Trap: Missing Observable

```python
# ❌ WRONG - Sampler format (only circuit)
estimator.run([(qc,)])  # Missing observable!

# ❌ WRONG - Parameters must be list
estimator.run([(qc_param, obs, 0.5)])  # 0.5 should be [0.5]

# ✅ CORRECT
estimator.run([(qc, obs)])  # Basic
estimator.run([(qc_param, obs, [0.5])])  # With params
```

### 🧠 Mnemonic: "COPPP" = Circuit Observable Params Precision
> **C**ircuit (required)
> **O**bservable (required) 
> **P**arameters (optional, must be list)
> **P**recision (optional)
>
> Estimator needs **O**bservable, Sampler doesn't!

### ✅ Quick Check
**Q: What's wrong with `estimator.run([(qc, obs, 0.5)])`?**

<details>
<summary>Answer</summary>

The parameter value `0.5` should be wrapped in a list: `[0.5]`. Parameters must always be a list, even for single values.

Correct: `estimator.run([(qc, obs, [0.5])])`

</details>

---

# 📚 Topic 4: Result Extraction

## 4.1 Result Access Chain

### 📝 Definition
Estimator results are accessed via a chain: `result[i].data.evs` for expectation values and `result[i].data.stds` for standard deviations.

### 📐 Visual Representation

```
job.result()
     │
     ▼
result[0]  ─────────────────────────  (First PUB result)
     │
     ├── .data
     │      ├── .evs  ────────────── Expectation values (array)
     │      └── .stds ────────────── Standard deviations (array)
     │
     └── .metadata ───────────────── Additional info

result[1], result[2], ...  ────────── (Additional PUB results)
```

### 💻 Implementation

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]
pubs = [(qc, obs) for obs in observables]

estimator = StatevectorEstimator()
job = estimator.run(pubs)
result = job.result()

# Access each result
for i, label in enumerate(['ZZ', 'XX', 'YY']):
    evs = result[i].data.evs    # Expectation value
    stds = result[i].data.stds  # Standard deviation
    print(f"⟨{label}⟩ = {evs:.3f} ± {stds:.3f}")

# Output for Bell state:
# ⟨ZZ⟩ = 1.000 ± 0.000
# ⟨XX⟩ = 1.000 ± 0.000
# ⟨YY⟩ = -1.000 ± 0.000
```

### ⚠️ Exam Trap: Result Access Mistakes

```python
# ❌ WRONG patterns
result.evs                    # Missing [0] and .data
result[0].evs                 # Missing .data
result[0].data.ev             # Missing 's' (not plural)
result.data.evs               # Missing [0] index

# ✅ CORRECT
result[0].data.evs   # Expectation values
result[0].data.stds  # Standard deviations
```

### 🧠 Mnemonic: "0-D-EV-S" = [0].data.evs
> **[0]** - Index first result
> **.D**ata - Access data object
> **.EV** - Expectation value
> **-S** - Plural 's' at end
>
> "Zero Data EVS"

### ✅ Quick Check
**Q: For `result = job.result()` with 3 PUBs, how do you get the expectation value of the second observable?**

<details>
<summary>Answer</summary>

`result[1].data.evs`

Remember: Python indexing starts at 0, so second = index 1.

</details>

---

# 📚 Topic 5: Error Mitigation (ResilienceOptionsV2)

## 5.1 Resilience Levels

### 📝 Definition
**Resilience levels** control the amount of error mitigation applied to hardware results. Higher levels = more accurate but slower.

### 📐 Visual Representation

```
┌─────────────────────────────────────────────────────────┐
│           ERROR MITIGATION TECHNIQUES                    │
├─────────────────────────────────────────────────────────┤
│  resilience_level = 0   →  NO mitigation (fastest)      │
│                                                          │
│  resilience_level = 1   →  Twirling + M3 Readout        │
│                             (balanced - DEFAULT)         │
│                                                          │
│  resilience_level = 2   →  ZNE + PEC (slowest, best)    │
└─────────────────────────────────────────────────────────┘
```

### 💻 Implementation

```python
from qiskit_ibm_runtime import EstimatorV2 as Estimator

estimator = Estimator(mode=backend)

# Level 0: No mitigation (testing)
estimator.options.resilience_level = 0

# Level 1: M3 mitigation (recommended)
estimator.options.resilience_level = 1

# Level 2: ZNE + PEC (research)
estimator.options.resilience_level = 2
```

### ⚠️ Exam Trap: Level Values

```python
# ❌ WRONG - String not integer
estimator.options.resilience_level = "1"  

# ❌ WRONG - Invalid level
estimator.options.resilience_level = 3  # Only 0, 1, 2 valid

# ✅ CORRECT
estimator.options.resilience_level = 1
```

### 🧠 Mnemonic: "012 = None-M3-ZNE"
> **0** = **N**one
> **1** = **M**3 (M is 1 letter after L)
> **2** = **Z**NE (Z is 2nd from end of alphabet)

### ✅ Quick Check
**Q: Which resilience_level should you use for production runs on hardware?**

<details>
<summary>Answer</summary>

`resilience_level = 1` is recommended for most hardware runs. It provides M3 readout mitigation which balances accuracy and execution time. Level 2 is for research when you need maximum accuracy and can afford longer runtimes.

</details>

---

## 5.2 ZNE (Zero Noise Extrapolation)

### 📝 Definition
**ZNE** amplifies circuit noise at multiple levels and extrapolates back to zero noise.

### 📐 Visual Representation

```
                Expectation Value
                    ^
                    │     * (1x noise)
                    │         * (3x noise)
                    │             * (5x noise)
                    │
       Zero-noise ──┼────────────────────────────
       estimate     │ ↑ Extrapolate backward
                    │
                    └──────────────────────────────> Noise Level
                        1x    3x    5x
                        
Gate Folding: U → UU†U → UU†UU†U (adds noise while preserving logic)
```

### 💻 Implementation

```python
from qiskit_ibm_runtime import EstimatorV2 as Estimator

estimator = Estimator(mode=backend)

# Enable ZNE
estimator.options.resilience.zne_mitigation = True

# Configure ZNE
estimator.options.resilience.zne.noise_factors = (1, 3, 5)
estimator.options.resilience.zne.extrapolator = "exponential"
estimator.options.resilience.zne.amplifier = "gate_folding"
```

### ZNE Parameters (MEMORIZE!)

| Parameter | Values | Description |
|-----------|--------|-------------|
| **noise_factors** | `(1, 3, 5)` default | Scaling factors for noise amplification |
| **extrapolator** | `"linear"`, `"exponential"`, `"polynomial"`, `"double_exponential"` | Method to extrapolate to zero noise |
| **amplifier** | `"gate_folding"`, `"local_folding"` | How to amplify circuit noise |

### 🧠 Mnemonic: "ZNE = Zero via Noise Expansion"
> Run at multiple noise levels, extrapolate to **Z**ero

### ✅ Quick Check
**Q: What does gate folding do in ZNE?**

<details>
<summary>Answer</summary>

Gate folding adds noise while preserving circuit logic:
- 1x: U
- 3x: U U† U (adds 2 more gates)
- 5x: U U† U U† U (adds 4 more gates)

The extra gates increase noise proportionally, allowing extrapolation to zero noise.

</details>

---

## 5.3 Twirling Defaults (Sampler vs Estimator)

### 📝 Definition
**Twirling** randomizes errors to make them easier to mitigate. Estimator and Sampler have DIFFERENT defaults!

### ⚠️ Exam Trap: Different Defaults

| Option | Sampler Default | Estimator Default |
|--------|-----------------|-------------------|
| `enable_gates` | `False` | `False` |
| `enable_measure` | `False` ⚠️ | `True` ⚠️ |
| `num_randomizations` | `32` | `32` |
| `strategy` | `"active-accum"` | `"active-accum"` |

**Why the difference?**
- **Estimator**: Averages over many shots → measurement twirling helps
- **Sampler**: Returns individual counts → measurement twirling changes outcomes

### 💻 Implementation

```python
from qiskit_ibm_runtime import EstimatorV2 as Estimator

estimator = Estimator(mode=backend)

# Configure twirling
estimator.options.twirling.enable_gates = True
estimator.options.twirling.enable_measure = True    # DEFAULT for Estimator!
estimator.options.twirling.num_randomizations = 32
estimator.options.twirling.strategy = "active-accum"
```

### 🧠 Mnemonic: "Estimator Expects Twirling"
> **E**stimator has **E**nable_measure=True by default

### ✅ Quick Check
**Q: Does Estimator have `enable_measure` twirling on by default?**

<details>
<summary>Answer</summary>

**Yes!** Unlike Sampler (which defaults to False), Estimator has `enable_measure = True` by default because it averages over shots and benefits from measurement error twirling.

</details>

---

## 5.4 Dynamical Decoupling (DD)

### 📝 Definition
**Dynamical Decoupling** inserts pulse sequences during idle times to suppress decoherence.

### 💻 Implementation

```python
from qiskit_ibm_runtime import EstimatorV2 as Estimator

estimator = Estimator(mode=backend)

# Enable DD
estimator.options.dynamical_decoupling.enable = True
estimator.options.dynamical_decoupling.sequence_type = "XY4"  # Best protection
```

### DD Sequence Types

| Sequence | Gates | Protection |
|----------|-------|------------|
| `"X"` | X pulses | Basic |
| `"XpXm"` | X, -X | Better |
| `"XY4"` | X, Y, X, Y | Best |

### 🧠 Mnemonic: "XY4 for Quality"
> **XY4** = Best **Q**uality protection

---

# 📚 Topic 6: VQE Pattern

## 6.1 VQE Algorithm

### 📝 Definition
**VQE** (Variational Quantum Eigensolver) is a hybrid quantum-classical algorithm to find the ground state energy of a Hamiltonian.

### 🎭 Real-World Analogy
VQE is like **tuning a guitar** blindfolded:
- You have a target sound (ground state)
- You adjust tuning knobs (parameters θ)
- A friend tells you "closer" or "further" (⟨H⟩ value)
- You keep adjusting until the sound is perfect (minimum energy)

### 📐 Visual Representation

```
┌────────────────────────────────────────────────────────────┐
│                    VQE LOOP                                 │
│                                                             │
│    ┌──────────────┐                                        │
│    │   Quantum    │ ← Parameters θ                         │
│    │   Ansatz     │                                        │
│    │   |ψ(θ)⟩     │                                        │
│    └──────┬───────┘                                        │
│           │                                                 │
│           ▼                                                 │
│    ┌──────────────┐                                        │
│    │  Estimator   │ → ⟨H⟩ = ⟨ψ(θ)|H|ψ(θ)⟩                 │
│    └──────┬───────┘                                        │
│           │                                                 │
│           ▼                                                 │
│    ┌──────────────┐                                        │
│    │  Classical   │                                        │
│    │  Optimizer   │ → New θ (minimize ⟨H⟩)                 │
│    │   COBYLA     │                                        │
│    └──────┬───────┘                                        │
│           │                                                 │
│           └────────────→ Repeat until converged            │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

### 💻 Implementation

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize
import numpy as np

# 1. Define Hamiltonian
H = SparsePauliOp(['ZZ', 'ZI', 'IZ'], [1.0, -1.0, -1.0])

# 2. Create parameterized ansatz
theta = Parameter('θ')
phi = Parameter('φ')

ansatz = QuantumCircuit(2)
ansatz.ry(theta, 0)
ansatz.ry(phi, 1)
ansatz.cx(0, 1)

# 3. Define cost function
estimator = StatevectorEstimator()

def cost_function(params):
    qc = ansatz.assign_parameters(params)
    job = estimator.run([(qc, H)])
    return job.result()[0].data.evs

# 4. Optimize with COBYLA
initial_params = [0.0, 0.0]
result = minimize(cost_function, initial_params, method='COBYLA')

# 5. Results
print(f"Ground state energy: {result.fun:.6f}")
print(f"Optimal parameters: {result.x}")
```

### ⚠️ Exam Trap: COBYLA is Gradient-Free

```python
# VQE typically uses gradient-free optimizers:
# - COBYLA (most common on exam!)
# - SLSQP
# - Nelder-Mead

# These work well with noisy quantum functions

result = minimize(cost, params, method='COBYLA')  # ✅ EXAM ANSWER
result = minimize(cost, params, method='BFGS')     # Gradient-based (less common)
```

### 🧠 Mnemonic: "COBYLA for Quantum"
> **C**onstrained **O**ptimization **BY** **L**inear **A**pproximation
> 
> Gradient-free = Good for noisy quantum functions

### ✅ Quick Check
**Q: Why does VQE use COBYLA instead of gradient-based optimizers like BFGS?**

<details>
<summary>Answer</summary>

COBYLA is **gradient-free**, which means it doesn't need to compute derivatives. Quantum circuits on real hardware are noisy, making gradient estimation unreliable. Gradient-free methods like COBYLA are more robust to noise.

</details>

---

## 6.2 VQE Components

### 📝 Definition
VQE has four main components: Ansatz, Hamiltonian, Estimator, and Classical Optimizer.

### 💻 Implementation Details

```python
# ANSATZ: Parameterized quantum circuit
# Common ansatze (exam may test names):
# - RealAmplitudes (RY + CNOT)
# - EfficientSU2 (rotation + entangling)
# - TwoLocal (flexible layers)

from qiskit.circuit import ParameterVector

params = ParameterVector('θ', 4)
ansatz = QuantumCircuit(2)
ansatz.ry(params[0], 0)
ansatz.ry(params[1], 1)
ansatz.cx(0, 1)
ansatz.ry(params[2], 0)
ansatz.ry(params[3], 1)

# HAMILTONIAN: Energy operator
# H2 molecule is common exam example
H2 = SparsePauliOp(
    ["II", "ZI", "IZ", "ZZ", "XX"],
    [-1.05, 0.39, 0.39, -0.01, 0.18]
)

# OPTIMIZER: Classical minimization
# COBYLA: No gradients needed (noisy-friendly)
# SLSQP: Can handle constraints
# Nelder-Mead: Simplex method

from scipy.optimize import minimize
result = minimize(cost, initial, method='COBYLA', options={'maxiter': 100})
```

### ⚠️ Exam Trap: assign_parameters() Required

```python
# ❌ WRONG - Can't run parameterized circuit directly
job = estimator.run([(ansatz, H)])  # Has unbound parameters!

# ✅ CORRECT - Bind parameters first
bound_circuit = ansatz.assign_parameters([0.5, 1.2, 0.3, 0.8])
job = estimator.run([(bound_circuit, H)])
```

### 🧠 Mnemonic: "AHEO" for VQE Components
> **A**nsatz (parameterized circuit)
> **H**amiltonian (energy operator)
> **E**stimator (calculates ⟨H⟩)
> **O**ptimizer (minimizes energy)

### ✅ Quick Check
**Q: What do you need to do before running a parameterized circuit with Estimator?**

<details>
<summary>Answer</summary>

Call `assign_parameters()` to bind the parameter values:
```python
bound_qc = qc.assign_parameters([value1, value2, ...])
```

You cannot run a circuit with unbound Parameters through Estimator.

</details>

---

# 📚 Topic 7: QAOA Pattern

## 7.1 QAOA Algorithm

### 📝 Definition
**QAOA** (Quantum Approximate Optimization Algorithm) is a variational algorithm for combinatorial optimization problems like MaxCut.

### 🎭 Real-World Analogy
QAOA is like **solving a maze with two helpers**:
- **Cost layer** (γ): A guide who knows where the exit is but can only whisper hints
- **Mixer layer** (β): An explorer who tries different paths
- Together they iteratively narrow down to the best path

### 📐 Visual Representation

```
QAOA Circuit Structure (p layers):

|+⟩ ─┤ Cost(γ₁) ├─┤ Mixer(β₁) ├─┤ Cost(γ₂) ├─┤ Mixer(β₂) ├─ ... ─┤ Measure ├
     └───────────┘ └───────────┘ └───────────┘ └───────────┘

Cost Layer:                    Mixer Layer:
┌─────────────────┐           ┌─────────────────┐
│  rzz(2γ, i, j)  │           │   rx(2β, i)     │
│  for each edge  │           │  for each qubit │
└─────────────────┘           └─────────────────┘
```

### 💻 Implementation (MaxCut)

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# MaxCut on triangle: 3 nodes, edges (0,1), (0,2), (1,2)
H_cost = SparsePauliOp(['ZZI', 'ZIZ', 'IZZ'], [1.0, 1.0, 1.0])

gamma = Parameter('γ')
beta = Parameter('β')

def qaoa_circuit(p=1):
    qc = QuantumCircuit(3)
    
    # Initial state: |+++⟩
    qc.h([0, 1, 2])
    
    for _ in range(p):
        # Cost layer (problem-specific)
        qc.rzz(2*gamma, 0, 1)  # Edge (0,1)
        qc.rzz(2*gamma, 0, 2)  # Edge (0,2)
        qc.rzz(2*gamma, 1, 2)  # Edge (1,2)
        
        # Mixer layer (standard)
        qc.rx(2*beta, 0)
        qc.rx(2*beta, 1)
        qc.rx(2*beta, 2)
    
    return qc

# Optimize
estimator = StatevectorEstimator()
qc = qaoa_circuit(p=1)

def qaoa_cost(params):
    bound = qc.assign_parameters(params)
    job = estimator.run([(bound, H_cost)])
    return job.result()[0].data.evs

result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')
print(f"Optimal γ={result.x[0]:.4f}, β={result.x[1]:.4f}")
```

### ⚠️ Exam Trap: Cost Before Mixer

```python
# ❌ WRONG - Mixer before Cost
qc.rx(2*beta, 0)      # Mixer first
qc.rzz(2*gamma, 0, 1) # Cost second

# ✅ CORRECT - Cost then Mixer
qc.rzz(2*gamma, 0, 1) # Cost first
qc.rx(2*beta, 0)      # Mixer second
```

### 🧠 Mnemonic: "CostMix" = Cost then Mixer
> **Cost** layer first (problem encoding)
> **Mix**er layer second (solution exploration)
>
> Also: "γ comes before β in Greek alphabet"

### ✅ Quick Check
**Q: In QAOA, what gates are used for the cost layer vs mixer layer?**

<details>
<summary>Answer</summary>

- **Cost layer**: `rzz(2γ, i, j)` for each edge in the graph (problem-specific)
- **Mixer layer**: `rx(2β, i)` for each qubit (standard exploration)

Parameters: γ (gamma) for cost, β (beta) for mixer.

</details>

---

## 7.2 QAOA Parameters

### 📝 Definition
QAOA uses 2p parameters: p gamma values (γ) for cost layers and p beta values (β) for mixer layers.

### 💻 Implementation

```python
# p layers = 2p parameters total
# Layer 1: γ₁, β₁
# Layer 2: γ₂, β₂
# ...
# Layer p: γₚ, βₚ

from qiskit.circuit import ParameterVector

def qaoa_circuit_multi_layer(p):
    gammas = ParameterVector('γ', p)
    betas = ParameterVector('β', p)
    
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    
    for layer in range(p):
        # Cost with γ[layer]
        qc.rzz(2*gammas[layer], 0, 1)
        qc.rzz(2*gammas[layer], 0, 2)
        qc.rzz(2*gammas[layer], 1, 2)
        
        # Mixer with β[layer]
        qc.rx(2*betas[layer], 0)
        qc.rx(2*betas[layer], 1)
        qc.rx(2*betas[layer], 2)
    
    return qc, gammas, betas

# More layers = more parameters = potentially better solutions
qc_p1, _, _ = qaoa_circuit_multi_layer(p=1)  # 2 parameters
qc_p2, _, _ = qaoa_circuit_multi_layer(p=2)  # 4 parameters
qc_p3, _, _ = qaoa_circuit_multi_layer(p=3)  # 6 parameters
```

### ✅ Quick Check
**Q: How many parameters does a QAOA circuit with p=3 layers have?**

<details>
<summary>Answer</summary>

**6 parameters**: 3 gamma values (γ₁, γ₂, γ₃) + 3 beta values (β₁, β₂, β₃)

Formula: 2p parameters for p layers.

</details>

---

# 🔄 Consolidated Review: Estimator vs Sampler

## Comparison Table

| Aspect | Sampler | Estimator |
|--------|---------|-----------|
| **Purpose** | Get measurement counts | Calculate ⟨O⟩ |
| **Output** | `{'00': 512, '11': 488}` | `0.732` |
| **Circuit** | NEEDS `measure()` | NO `measure()` |
| **PUB Format** | `[(circuit,)]` | `[(circuit, observable)]` |
| **Result Access** | `.data.meas.get_counts()` | `.data.evs` |
| **Use Case** | Grover's, sampling | VQE, QAOA |
| **Twirling Default** | `enable_measure=False` | `enable_measure=True` |

## Quick Reference

```python
# SAMPLER
from qiskit.primitives import StatevectorSampler
sampler = StatevectorSampler()
qc.measure_all()  # REQUIRED!
job = sampler.run([(qc,)])  # No observable
counts = job.result()[0].data.meas.get_counts()

# ESTIMATOR
from qiskit.primitives import StatevectorEstimator
estimator = StatevectorEstimator()
# NO measure!
job = estimator.run([(qc, SparsePauliOp('ZZ'))])  # WITH observable
evs = job.result()[0].data.evs
```

---

# ⚠️ Master Trap List

| # | Trap | Wrong | Correct | Mnemonic |
|---|------|-------|---------|----------|
| 1 | Estimator needs measurements | `qc.measure_all()` then run | No measurements | "ENM" |
| 2 | Observable must be SparsePauliOp | `'ZZ'` string | `SparsePauliOp('ZZ')` | "SPO not String" |
| 3 | Pauli string qubit order | Left-to-right visual | Tensor product order | "TiPO" |
| 4 | PUB missing observable | `[(qc,)]` | `[(qc, obs)]` | "COPPP" |
| 5 | Result access missing .data | `result[0].evs` | `result[0].data.evs` | "0-D-EV-S" |
| 6 | evs/stds singular | `.ev`, `.std` | `.evs`, `.stds` | "EVS has S" |
| 7 | Parameters not in list | `(qc, obs, 0.5)` | `(qc, obs, [0.5])` | "Params in List" |
| 8 | Twirling defaults differ | Same for both | Estimator has `enable_measure=True` | "Estimator Expects" |
| 9 | QAOA layer order | Mixer then Cost | Cost then Mixer | "CostMix" |
| 10 | Wrong optimizer for VQE | Gradient-based | COBYLA (gradient-free) | "COBYLA for Quantum" |
| 11 | Unbound parameters | Run parameterized directly | `assign_parameters()` first | "Bind Before Run" |
| 12 | resilience_level as string | `"1"` | `1` (integer) | "Levels are Integers" |

---

# 📝 Practice Exam Questions

## Question 1
**What is the correct way to calculate the expectation value of ZZ on a Bell state?**

A. 
```python
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
estimator.run([(qc, 'ZZ')])
```

B.
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
estimator.run([(qc, SparsePauliOp('ZZ'))])
```

C.
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
estimator.run([(qc,)])
```

D.
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
sampler.run([(qc, SparsePauliOp('ZZ'))])
```

<details>
<summary>Answer</summary>

**B** is correct.
- A: Has measurements AND string instead of SparsePauliOp
- B: ✅ No measurements, SparsePauliOp observable, correct PUB format
- C: Missing observable (that's Sampler format)
- D: Uses Sampler with observable (wrong primitive)

</details>

---

## Question 2
**How do you access the expectation value from an Estimator result?**

A. `result.evs`
B. `result[0].evs`
C. `result[0].data.evs`
D. `result[0].data.ev`

<details>
<summary>Answer</summary>

**C** is correct.
- A: Missing index and .data
- B: Missing .data
- C: ✅ Correct chain: [0].data.evs
- D: Missing 's' (it's plural: evs not ev)

</details>

---

## Question 3
**For SparsePauliOp('XIZ'), which qubit has the X operator?**

A. Qubit 0
B. Qubit 1
C. Qubit 2
D. All qubits

<details>
<summary>Answer</summary>

**A** is correct.

In Pauli string 'XIZ':
- Position 0 (leftmost) = X → acts on qubit 0
- Position 1 = I → identity on qubit 1
- Position 2 (rightmost) = Z → acts on qubit 2

</details>

---

## Question 4
**What optimizer is most commonly used with VQE for noisy quantum functions?**

A. BFGS
B. Adam
C. COBYLA
D. Newton-CG

<details>
<summary>Answer</summary>

**C** is correct.

COBYLA is gradient-free, making it ideal for noisy quantum functions. Gradient-based methods (BFGS, Adam, Newton-CG) require reliable gradient estimates, which are difficult with quantum noise.

</details>

---

## Question 5
**In QAOA, what is the correct order of operations per layer?**

A. Mixer layer, then Cost layer
B. Cost layer, then Mixer layer
C. Cost layer only
D. Mixer layer only

<details>
<summary>Answer</summary>

**B** is correct.

QAOA structure: Initial state → [Cost(γ) → Mixer(β)] × p layers

Cost layer uses `rzz()` for edges, Mixer layer uses `rx()` for all qubits.

</details>

---

## Question 6
**What is the default twirling setting difference between Sampler and Estimator?**

A. Both have `enable_measure=True`
B. Both have `enable_measure=False`
C. Sampler=False, Estimator=True
D. Sampler=True, Estimator=False

<details>
<summary>Answer</summary>

**C** is correct.

- Sampler: `enable_measure=False` (preserves individual count outcomes)
- Estimator: `enable_measure=True` (helps average out measurement errors)

</details>

---

## Question 7
**Which resilience_level enables ZNE (Zero Noise Extrapolation)?**

A. 0
B. 1
C. 2
D. 3

<details>
<summary>Answer</summary>

**C** is correct.

- Level 0: No mitigation
- Level 1: M3 readout mitigation + twirling
- Level 2: ZNE + PEC (maximum mitigation)
- Level 3: Invalid

</details>

---

### Part B: Code Analysis (3-5 minutes each)

**Q8**: What's wrong with this code and what will happen?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()  # Added measurements

estimator = StatevectorEstimator()
obs = SparsePauliOp('ZZ')
job = estimator.run([(qc, obs)])
result = job.result()
print(result[0].data.evs)
```

<details>
<summary>Answer</summary>

**Problem**: Circuit has measurements but Estimator requires circuits WITHOUT measurements.

**What happens**: This will raise an error or produce incorrect results. Estimator calculates expectation values mathematically - it doesn't use measurement outcomes.

**Fix**: Remove `qc.measure_all()`

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO measurements for Estimator!
```

**Mnemonic**: "ENM" = Estimator No Measures
</details>

---

**Q9**: What does this code print?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  # Bell state

observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]
pubs = [(qc, obs) for obs in observables]

estimator = StatevectorEstimator()
job = estimator.run(pubs)
result = job.result()

print(result[0].data.evs)
print(result[1].data.evs)
print(result[2].data.evs)
```

<details>
<summary>Answer</summary>

**Output**:
```
1.0
1.0
-1.0
```

**Explanation**:
For the Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2:
- ⟨ZZ⟩ = +1 (both qubits correlated in Z basis)
- ⟨XX⟩ = +1 (both qubits correlated in X basis)
- ⟨YY⟩ = -1 (anti-correlated in Y basis)

This is a famous property of Bell states!
</details>

---

**Q10**: Fix this code to extract the expectation value:
```python
result = job.result()

# These all fail - why?
# evs = result.data.evs
# evs = result[0].evs
# evs = result[0].data.ev
```

<details>
<summary>Answer</summary>

**All three are wrong because:**
1. `result.data.evs` - Missing `[0]` index
2. `result[0].evs` - Missing `.data`
3. `result[0].data.ev` - Missing 's' (plural)

**Correct**:
```python
evs = result[0].data.evs
```

**Mnemonic**: "0-D-EV-S" = [0].data.evs
</details>

---

**Q11**: What's the output of this code?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(1)
qc.h(0)  # |+⟩ state

estimator = StatevectorEstimator()
job = estimator.run([(qc, SparsePauliOp('Z'))])
result = job.result()

print(result[0].data.evs)
print(result[0].data.stds)
```

<details>
<summary>Answer</summary>

**Output**:
```
0.0
0.0
```

**Explanation**:
- |+⟩ = (|0⟩ + |1⟩)/√2
- ⟨Z⟩ = (+1)(0.5) + (-1)(0.5) = 0
- stds = 0 for StatevectorEstimator (exact simulation, no shot noise)

On hardware, stds would be non-zero due to finite shots.
</details>

---

**Q12**: What's wrong with this PUB format?
```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.ry(theta, 0)

estimator = StatevectorEstimator()
job = estimator.run([(qc, SparsePauliOp('Z'), 0.5)])  # param value
```

<details>
<summary>Answer</summary>

**Problem**: Parameter value `0.5` must be wrapped in a list.

**Wrong**: `(qc, SparsePauliOp('Z'), 0.5)`
**Correct**: `(qc, SparsePauliOp('Z'), [0.5])`

Parameters must always be in list format, even for single values:
```python
job = estimator.run([(qc, SparsePauliOp('Z'), [0.5])])
```

**Mnemonic**: "Params in List"
</details>

---

### Part C: Scenario-Based (5-7 minutes each)

**Q13**: You're implementing VQE to find the ground state energy of a simple Hamiltonian H = ZZ + 0.5·XX. Write complete code including the cost function and optimization.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# 1. Define Hamiltonian
H = SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])

# 2. Create parameterized ansatz
theta = Parameter('θ')
phi = Parameter('φ')
ansatz = QuantumCircuit(2)
ansatz.ry(theta, 0)
ansatz.ry(phi, 1)
ansatz.cx(0, 1)

# 3. Define cost function
estimator = StatevectorEstimator()

def cost_function(params):
    # Bind parameters
    bound_circuit = ansatz.assign_parameters(params)
    # Calculate expectation value
    job = estimator.run([(bound_circuit, H)])
    result = job.result()
    return result[0].data.evs

# 4. Optimize with COBYLA
initial_params = [0.0, 0.0]
result = minimize(
    cost_function, 
    initial_params, 
    method='COBYLA',  # Gradient-free!
    options={'maxiter': 100}
)

# 5. Print results
print(f"Ground state energy: {result.fun:.6f}")
print(f"Optimal parameters: θ={result.x[0]:.4f}, φ={result.x[1]:.4f}")
```

**Key points**:
- No measurements in ansatz circuit
- Use SparsePauliOp for Hamiltonian
- Bind parameters with assign_parameters()
- COBYLA is gradient-free (works with noisy functions)
</details>

---

**Q14**: Write code to measure all three Pauli observables (X, Y, Z) on a single qubit in the |+⟩ state and print their expectation values.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create |+⟩ state (NO measurements!)
qc = QuantumCircuit(1)
qc.h(0)

# Define observables
observables = {
    'X': SparsePauliOp('X'),
    'Y': SparsePauliOp('Y'),
    'Z': SparsePauliOp('Z')
}

# Create PUBs
pubs = [(qc, obs) for obs in observables.values()]

# Run Estimator
estimator = StatevectorEstimator()
job = estimator.run(pubs)
result = job.result()

# Print results
for i, name in enumerate(['X', 'Y', 'Z']):
    evs = result[i].data.evs
    print(f"⟨{name}⟩ = {evs:.4f}")

# Expected output:
# ⟨X⟩ = 1.0000  (|+⟩ is eigenstate of X with eigenvalue +1)
# ⟨Y⟩ = 0.0000  (equal superposition)
# ⟨Z⟩ = 0.0000  (equal superposition)
```

**Key insight**: |+⟩ is an eigenstate of X with eigenvalue +1, explaining ⟨X⟩ = 1.
</details>

---

**Q15**: Implement a simple QAOA circuit for MaxCut on a triangle graph (3 nodes, all pairs connected). Include cost and mixer layers.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# Parameters
gamma = Parameter('γ')
beta = Parameter('β')

# Build QAOA circuit (1 layer)
qc = QuantumCircuit(3)

# Initial state: |+++⟩
qc.h([0, 1, 2])

# Cost layer (rzz for each edge)
# Triangle: edges (0,1), (0,2), (1,2)
qc.rzz(2*gamma, 0, 1)  # Edge 0-1
qc.rzz(2*gamma, 0, 2)  # Edge 0-2
qc.rzz(2*gamma, 1, 2)  # Edge 1-2

# Mixer layer (rx on each qubit)
qc.rx(2*beta, 0)
qc.rx(2*beta, 1)
qc.rx(2*beta, 2)

# Cost Hamiltonian for MaxCut
# H = Σ(1 - ZᵢZⱼ)/2 for each edge
# Simplified: just use ZZ terms
H_cost = SparsePauliOp(['ZZI', 'ZIZ', 'IZZ'], [0.5, 0.5, 0.5])

# Optimize
estimator = StatevectorEstimator()

def qaoa_cost(params):
    bound = qc.assign_parameters(params)
    job = estimator.run([(bound, H_cost)])
    return job.result()[0].data.evs

result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')
print(f"Optimal γ={result.x[0]:.4f}, β={result.x[1]:.4f}")
print(f"Cost value: {result.fun:.4f}")
```

**Key structure**:
1. Initial |+++⟩ superposition
2. Cost layer (γ): `rzz()` for each edge
3. Mixer layer (β): `rx()` for each qubit
4. Order: Cost THEN Mixer ("CostMix")
</details>

---

### Score Yourself

| Section | Total Qs | Your Score | Percentage |
|---------|----------|------------|------------|
| Part A (Quick Fire) | 7 | /7 | % |
| Part B (Code Analysis) | 5 | /5 | % |
| Part C (Scenarios) | 3 | /3 | % |
| **TOTAL** | **15** | **/15** | **%** |

**Interpretation**:
- 90-100%: Ready for Section 6 exam questions
- 75-89%: Review result access patterns and PUB format
- Below 75%: Re-study Estimator basics and VQE pattern

---

# 🎯 Key Takeaways

## Concept Mastery Checklist

```
□ I understand the difference: Sampler=counts, Estimator=expectation values
□ I know Estimator circuits MUST NOT have measurements ("ENM")
□ I understand SparsePauliOp qubit ordering (leftmost = qubit 0)
□ I know PUB format: (circuit, observable, params, precision)
□ I understand expectation value formula: ⟨O⟩ = ⟨ψ|O|ψ⟩
□ I know VQE minimizes ⟨H⟩ to find ground state energy
□ I know QAOA structure: Cost layer then Mixer layer
□ I understand resilience levels: 0=none, 1=M3, 2=ZNE
□ I know twirling defaults differ: Estimator has enable_measure=True
```

## Code Mastery Checklist

```
□ I can write result[0].data.evs from memory (plural!)
□ I can write result[0].data.stds from memory (plural!)
□ I can create SparsePauliOp: SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])
□ I can create Estimator PUB: [(circuit, SparsePauliOp('ZZ'))]
□ I can bind parameters: circuit.assign_parameters([value1, value2])
□ I can implement VQE cost function with scipy.optimize.minimize
□ I can build QAOA circuit: H gates → rzz (cost) → rx (mixer)
□ I can iterate multiple PUB results: for i in range(len(result))
□ I can set resilience: estimator.options.resilience_level = 1
```

## Trap Avoidance Checklist

```
□ I won't add measurements to Estimator circuits ("ENM")
□ I won't use string for observable: SparsePauliOp('ZZ') not 'ZZ'
□ I won't forget .data: result[0].data.evs not result[0].evs
□ I won't use singular: evs/stds not ev/std
□ I won't forget list for params: [0.5] not 0.5
□ I won't use Sampler PUB format: [(qc, obs)] not [(qc,)]
□ I won't forget assign_parameters() before running
□ I won't use gradient optimizers with VQE: COBYLA not BFGS
□ I won't reverse QAOA order: Cost then Mixer, not Mixer then Cost
```

## Mnemonic Recall Box

```
┌─────────────────────────────────────────────────────────────────┐
│  "ENM" = Estimator No Measures                                  │
│  → Estimator circuits have NO measurement gates                 │
│                                                                  │
│  "TiPO" = Tensor in Pauli Order                                 │
│  → 'XIZ': X on q0, I on q1, Z on q2 (left to right)            │
│                                                                  │
│  "0-D-EV-S" = [0].data.evs                                      │
│  → Result access chain (plural s!)                              │
│                                                                  │
│  "COPPP" = Circuit Observable Params Precision                  │
│  → Estimator PUB format                                         │
│                                                                  │
│  "COBYLA for Quantum"                                           │
│  → Gradient-free optimizer for noisy VQE                        │
│                                                                  │
│  "CostMix" = Cost then Mixer                                    │
│  → QAOA layer order (γ before β)                                │
│                                                                  │
│  "012 = None-M3-ZNE"                                            │
│  → resilience_level values                                      │
└─────────────────────────────────────────────────────────────────┘
```

## One-Page Summary Box

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                      ESTIMATOR QUICK REFERENCE                                │
├──────────────────────────────────────────────────────────────────────────────┤
│  BASIC USAGE                                                                  │
│  ───────────                                                                 │
│  from qiskit.primitives import StatevectorEstimator                          │
│  from qiskit.quantum_info import SparsePauliOp                               │
│                                                                               │
│  qc = QuantumCircuit(2)  # NO measurements!                                  │
│  qc.h(0); qc.cx(0, 1)                                                        │
│  obs = SparsePauliOp('ZZ')                                                   │
│                                                                               │
│  estimator = StatevectorEstimator()                                          │
│  job = estimator.run([(qc, obs)])                                            │
│  evs = job.result()[0].data.evs                                              │
│                                                                               │
│  SPARSEPAULI STRING ORDER                                                     │
│  ────────────────────────                                                    │
│  SparsePauliOp('XIZ') = X⊗I⊗Z                                                │
│    Position 0 (X) → qubit 0                                                  │
│    Position 1 (I) → qubit 1                                                  │
│    Position 2 (Z) → qubit 2                                                  │
│                                                                               │
│  PUB FORMATS                                                                  │
│  ───────────                                                                 │
│  Basic:      [(circuit, observable)]                                         │
│  With params: [(circuit, observable, [param_values])]                        │
│  Full:       [(circuit, observable, [params], precision)]                    │
│                                                                               │
│  VQE PATTERN                                                                  │
│  ───────────                                                                 │
│  1. H = SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])  # Hamiltonian               │
│  2. ansatz = parameterized circuit (NO measurements)                         │
│  3. def cost(p): return estimator.run([(ansatz.assign_parameters(p), H)])   │
│  4. result = minimize(cost, initial, method='COBYLA')                        │
│                                                                               │
│  QAOA PATTERN                                                                 │
│  ────────────                                                                │
│  1. qc.h(all)           # Initial superposition                              │
│  2. qc.rzz(2γ, i, j)    # Cost layer (for each edge)                        │
│  3. qc.rx(2β, i)        # Mixer layer (for each qubit)                      │
│  4. minimize(qaoa_cost, [γ₀, β₀], method='COBYLA')                          │
├──────────────────────────────────────────────────────────────────────────────┤
│  ⚠️ TOP EXAM TRAPS                                                            │
│  ──────────────────                                                          │
│  ❌ qc.measure_all() with Estimator        # No measurements!                 │
│  ❌ estimator.run([(qc, 'ZZ')])            # SparsePauliOp not string!        │
│  ❌ result[0].evs                          # Missing .data!                   │
│  ❌ result[0].data.ev                      # Missing 's' (plural)!            │
│  ❌ (qc, obs, 0.5)                         # Params must be [0.5]!            │
│  ✅ result[0].data.evs                     # CORRECT                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Files in This Section

| File | Purpose | Key Content |
|------|---------|-------------|
| [README.md](README.md) | Complete learning guide | Theory, 12 traps, 15 practice questions, checklists |
| [estimator_primitive.ipynb](estimator_primitive.ipynb) | CODE LABORATORY | Estimator APIs, SparsePauliOp, result extraction |
| [vqe_pattern.ipynb](vqe_pattern.ipynb) | VQE & QAOA Lab | VQE implementation, QAOA MaxCut, optimization |
| [README_OLD.md](README_OLD.md) | Backup | Previous version for reference |

---

## ➡️ Next Steps

1. **Complete the notebooks**: Run all cells in both notebooks
2. **Practice SparsePauliOp**: Create 5 different Hamiltonians
3. **Implement VQE**: Write from scratch without looking at notes
4. **Build QAOA**: Create circuits for different graph sizes
5. **Take Practice Exam**: Score at least 90% on the 15-question exam above
6. **Review Section 7**: Continue to [Section 7: Result Extraction](../section_7_results/README.md) for advanced result processing

---

## 🔗 Related Sections

- **Section 5**: Sampler primitive (counts vs expectation values)
- **Section 7**: Result extraction patterns
- **Section 9**: Quantum info (SparsePauliOp, Operator)

---

## 📚 Additional Resources

- Qiskit Primitives Guide: [docs.quantum.ibm.com/guides/primitives](https://docs.quantum.ibm.com/guides/primitives)
- VQE Tutorial: [learning.quantum.ibm.com](https://learning.quantum.ibm.com)
- QAOA Tutorial: [qiskit-community.github.io](https://qiskit-community.github.io/qiskit-optimization/)
- Error Mitigation: [docs.quantum.ibm.com/guides/error-mitigation](https://docs.quantum.ibm.com/guides/error-mitigation)

---

**Estimator, VQE, and QAOA are CRITICAL for the exam!** 🚀⚡

---

*Last Updated: 2025-01-15 | Qiskit Version: 1.x | Exam Weight: ~12%*
