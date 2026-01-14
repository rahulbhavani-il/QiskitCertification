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

## ✅ Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS:
□ Estimator returns expectation values ⟨O⟩, Sampler returns counts/bitstrings
□ Estimator circuits MUST NOT have measurements ("ENM" - Estimator No Measures)
□ SparsePauliOp uses leftmost = qubit 0 ordering (opposite of bitstring convention)
□ PUB format: (circuit, observable, params, precision) for Estimator
□ Expectation value: ⟨O⟩ = ⟨ψ|O|ψ⟩ = sum of eigenvalues weighted by probabilities
□ VQE (Variational Quantum Eigensolver) minimizes ⟨H⟩ to find ground state energy
□ QAOA (Quantum Approximate Optimization) structure: Cost layer then Mixer layer
□ Resilience levels: 0=none (ideal), 1=M3 mitigation, 2=M3+ZNE
□ Twirling defaults: Estimator has enable_gates=True, enable_measure=True (both ON)
□ Gradient-free optimizers (COBYLA, SPSA) work best with noisy quantum hardware
□ Observable apply_layout() remaps qubits after transpilation
□ Multiple observables can share same circuit in single PUB
□ Result structure: result[0].data.evs (plural!) and result[0].data.stds

CONSTRAINTS & LIMITATIONS:
□ Estimator will ERROR if circuit contains any measurement gates (not just ignore)
□ Observable must match circuit qubit count (3-qubit circuit needs 3-character Pauli)
□ Maximum 300 PUBs per job submission in runtime (exceeding causes error)
□ precision parameter must be positive float (0 or negative causes ValueError)
□ Parameter binding must match circuit's num_parameters exactly
□ Cannot use ClassicalRegister with Estimator (no classical bits allowed)
□ SparsePauliOp coefficients must be real numbers (complex not supported for expectation)
□ Observable qubits cannot exceed circuit qubits (padding with 'I' if needed)
□ Each observable in list must have same number of qubits
□ Precision target is best-effort, not guaranteed (hardware limitations)
□ Session expires after 5 minutes idle (jobs fail if session closed)
□ Resilience level 2 significantly increases runtime (5-10x slower than level 0)

KEY DEFINITIONS:
□ Expectation value: Average measurement outcome ⟨ψ|O|ψ⟩ for observable O
□ Observable: Hermitian operator whose expectation value is computed
□ SparsePauliOp: Sparse representation of Pauli strings with coefficients
□ Pauli string: Tensor product of Pauli operators (I, X, Y, Z)
□ PUB (Primitive Unified Bloc): Tuple (circuit, observable, parameters, precision)
□ DataBin: Container holding evs (expectation values) and stds (standard deviations)
□ Hamiltonian: Energy operator whose ground state VQE finds
□ Ansatz: Parameterized quantum circuit (trial wavefunction)
□ Cost function: Objective to minimize, typically ⟨H⟩ in VQE
□ Resilience: Error mitigation techniques (M3, ZNE) to reduce noise impact
□ M3 mitigation: Matrix-free Measurement Mitigation
□ ZNE: Zero Noise Extrapolation - extrapolates to zero-noise limit
□ Twirling: Randomized compilation converting coherent to stochastic noise
□ apply_layout: Method to remap observable qubits after circuit transpilation

ARCHITECTURE & WORKFLOW:
□ Estimator uses V2 interface: run() returns Job, result() returns PrimitiveResult
□ StatevectorEstimator simulates ideal quantum computer (no noise)
□ EstimatorV2 connects to IBM Quantum hardware or noisy simulators
□ Runtime primitives batch-optimize multiple circuits for efficiency
□ Primitive options persist across multiple run() calls on same instance
□ Job queuing: jobs wait in QUEUED state until resources available
□ Results persist in cloud for 7 days after completion (then deleted)
□ Estimator internally samples and averages to estimate ⟨O⟩
□ Higher precision targets increase sampling shots automatically
□ Observable decomposition: complex observables split into Pauli basis

VQE & QAOA SPECIFICS:
□ VQE alternates: quantum (expectation) → classical (optimization) → repeat
□ QAOA structure: initial state (H gates) → Cost layer → Mixer layer → measure expectation
□ Cost layer encodes problem: phase gates implementing problem Hamiltonian
□ Mixer layer maintains superposition: typically X rotations on all qubits
□ QAOA parameter order: (γ, β) where γ = cost angle, β = mixer angle
□ VQE convergence depends on ansatz expressiveness and optimizer choice
□ COBYLA: Constrained Optimization BY Linear Approximation (gradient-free)
□ SPSA: Simultaneous Perturbation Stochastic Approximation (handles noise well)
□ Gradient-based optimizers (BFGS, L-BFGS-B) fail on noisy hardware

VERSION-SPECIFIC:
□ V1 Estimator deprecated: use V2 (EstimatorV2, not Estimator)
□ Old execute() removed in Qiskit 1.0 - use primitives exclusively
□ qiskit-ibm-runtime separate package required for hardware access
□ StatevectorEstimator in qiskit.primitives (local), EstimatorV2 in qiskit_ibm_runtime
□ SparsePauliOp replaces older Operator types in primitive workflows
```

### 💻 Code Pattern Checklist
```
ESSENTIAL IMPORTS:
□ from qiskit.primitives import StatevectorEstimator  # ideal/local simulation
□ from qiskit_ibm_runtime import EstimatorV2  # hardware/runtime
□ from qiskit_ibm_runtime import QiskitRuntimeService  # backend access
□ from qiskit.quantum_info import SparsePauliOp  # observable creation
□ from qiskit import QuantumCircuit  # circuit creation
□ from qiskit.circuit import Parameter  # parameterized circuits
□ from scipy.optimize import minimize  # VQE optimization
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

ESTIMATOR INITIALIZATION:
□ estimator = StatevectorEstimator()  # no arguments, local ideal sim
□ service = QiskitRuntimeService(); backend = service.backend("ibm_brisbane")
□ estimator = EstimatorV2(mode=backend)  # runtime with specific backend
□ estimator = EstimatorV2(mode=backend, options=options_dict)  # with options
□ estimator = StatevectorEstimator(default_precision=0.01)  # custom precision
□ estimator = StatevectorEstimator(seed=42)  # reproducible simulation

OBSERVABLE CREATION:
□ obs = SparsePauliOp('Z')  # single qubit, single Pauli
□ obs = SparsePauliOp('ZZ')  # two qubits, Z⊗Z tensor product
□ obs = SparsePauliOp('XIZ')  # three qubits, X⊗I⊗Z (leftmost=q0)
□ obs = SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])  # weighted sum: 1.0*ZZ + 0.5*XX
□ obs = SparsePauliOp.from_list([('ZZ', 1.0), ('XX', 0.5)])  # alternative syntax
□ obs = SparsePauliOp(['ZI', 'IZ'], [0.5, 0.5])  # sum of single-qubit terms
□ H = SparsePauliOp(['ZZ', 'ZI', 'IZ', 'XX'], [1.0, -0.5, -0.5, 0.3])  # Hamiltonian
□ obs = SparsePauliOp('I' * n_qubits)  # identity (returns 1.0)
□ coeff, pauli_list = obs.coeffs, obs.paulis  # extract components

CIRCUIT PREPARATION (NO MEASUREMENTS!):
□ qc = QuantumCircuit(2)  # NO ClassicalRegister, NO measurements
□ qc.h(0); qc.cx(0, 1)  # quantum operations only
□ assert qc.num_clbits == 0, "Estimator requires no classical bits!"
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.ry(theta, 0); qc.rz(phi, 1)  # parameterized circuit
□ # DO NOT add qc.measure_all() or qc.measure() - ERROR!

BASIC RUN PATTERNS:
□ job = estimator.run([(qc, obs)])  # single circuit-observable pair
□ result = job.result()  # blocking call, waits for completion
□ ev = result[0].data.evs[0]  # extract first expectation value (note: evs is array!)
□ std = result[0].data.stds[0]  # extract first standard deviation
□ evs = result[0].data.evs  # all expectation values (if multiple observables)
□ stds = result[0].data.stds  # all standard deviations

PARAMETERIZED CIRCUITS:
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.ry(theta, 0); qc.rz(phi, 1)  # add parameterized gates
□ job = estimator.run([(qc, obs, [0.5, 1.2])])  # bind [θ=0.5, φ=1.2]
□ job = estimator.run([(qc, obs, [0.5, 1.2], 0.01)])  # with precision target
□ job = estimator.run([(qc, obs, None, 0.01)])  # no params, custom precision
□ bound_qc = qc.assign_parameters([0.5, 1.2])  # pre-bind parameters
□ job = estimator.run([(bound_qc, obs)])  # run pre-bound circuit
□ param_values = [[0, 0], [0, π/2], [π/2, 0], [π/2, π/2]]
□ jobs = [estimator.run([(qc, obs, vals)]) for vals in param_values]  # sweep

MULTIPLE PUBS:
□ job = estimator.run([(qc1, obs1), (qc2, obs2), (qc3, obs3)])  # batch submission
□ result[0].data.evs  # qc1 expectation values
□ result[1].data.evs  # qc2 expectation values
□ result[2].data.evs  # qc3 expectation values
□ for i, pub_result in enumerate(result):  # iterate all
□     evs = pub_result.data.evs
□ all_evs = [r.data.evs for r in result]  # list comprehension

MULTIPLE OBSERVABLES (SAME CIRCUIT):
□ observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]
□ job = estimator.run([(qc, observables)])  # single PUB, multiple observables
□ evs = result[0].data.evs  # array: [⟨ZZ⟩, ⟨XX⟩, ⟨YY⟩]
□ stds = result[0].data.stds  # array: [σ_ZZ, σ_XX, σ_YY]
□ for obs, ev, std in zip(observables, evs, stds):  # iterate results

RESULT EXTRACTION (FULL CHAIN):
□ result = job.result()  # PrimitiveResult object
□ pub_result = result[0]  # PubResult for first PUB
□ data_bin = pub_result.data  # DataBin container
□ evs = data_bin.evs  # numpy array of expectation values (PLURAL!)
□ stds = data_bin.stds  # numpy array of standard deviations (PLURAL!)
□ metadata = pub_result.metadata  # access metadata
□ num_obs = len(evs)  # number of observables in this PUB

TRANSPILATION & LAYOUT:
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
□ qc_transpiled = pm.run(qc)  # transpile circuit
□ layout = qc_transpiled.layout  # extract layout information
□ obs_remapped = obs.apply_layout(layout)  # remap observable to match
□ job = estimator.run([(qc_transpiled, obs_remapped)])  # run with remapped obs

OPTIONS CONFIGURATION:
□ options = estimator.options  # get current options
□ estimator.options.default_precision = 0.01  # set precision target
□ options.resilience_level = 0  # no mitigation (ideal/debug)
□ options.resilience_level = 1  # enable M3 mitigation
□ options.resilience_level = 2  # enable M3 + ZNE (slower but better)
□ options.twirling.enable_gates = True  # gate twirling (default ON for Estimator)
□ options.twirling.enable_measure = True  # measurement twirling (default ON)
□ options.twirling.num_randomizations = 32  # set twirling rounds
□ options.dynamical_decoupling.enable = True  # enable DD
□ options.dynamical_decoupling.sequence_type = 'XY4'  # DD sequence
□ options.optimization_level = 3  # transpiler optimization (0-3)

VQE PATTERN (COMPLETE):
□ H = SparsePauliOp(['ZZ', 'ZI', 'IZ', 'XX'], [1.0, -0.5, -0.5, 0.3])  # Hamiltonian
□ ansatz = QuantumCircuit(2)  # NO measurements!
□ theta = Parameter('θ'); phi = Parameter('φ')
□ ansatz.ry(theta, 0); ansatz.ry(phi, 1); ansatz.cx(0, 1)
□ def cost_function(params):
□     bound_circuit = ansatz.assign_parameters(params)
□     job = estimator.run([(bound_circuit, H)])
□     return job.result()[0].data.evs[0]  # minimize this!
□ initial_params = [0.0, 0.0]
□ result = minimize(cost_function, initial_params, method='COBYLA')
□ optimal_energy = result.fun
□ optimal_params = result.x

QAOA PATTERN (COMPLETE):
□ def qaoa_circuit(gamma, beta, n_qubits):
□     qc = QuantumCircuit(n_qubits)
□     qc.h(range(n_qubits))  # initial superposition
□     # Cost layer (problem-specific)
□     for i in range(n_qubits-1):
□         qc.rzz(2*gamma, i, i+1)  # cost Hamiltonian
□     # Mixer layer
□     for i in range(n_qubits):
□         qc.rx(2*beta, i)  # mixer Hamiltonian
□     return qc  # NO measurements!
□ cost_hamiltonian = SparsePauliOp(['ZZ', 'ZI', 'IZ'], [1.0, 0.5, 0.5])
□ def qaoa_cost(params):
□     gamma, beta = params
□     qc = qaoa_circuit(gamma, beta, 2)
□     job = estimator.run([(qc, cost_hamiltonian)])
□     return job.result()[0].data.evs[0]
□ result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')

JOB MANAGEMENT:
□ job_id = job.job_id()  # get job ID for later retrieval
□ status = job.status()  # check job status (QUEUED, RUNNING, DONE, ERROR)
□ result = job.result()  # wait for completion (blocking)
□ job = service.job(job_id)  # retrieve old job by ID
□ job.cancel()  # cancel queued/running job
□ job.wait_for_final_state()  # blocking wait without retrieving result

ERROR HANDLING:
□ try: result = job.result()
□ except Exception as e: print(f"Job failed: {e}")
□ if job.status() == 'ERROR': print(job.error_message())
□ assert qc.num_clbits == 0, "Estimator requires no classical bits!"
□ if any(isinstance(inst.operation, Measure) for inst in qc.data):
□     raise ValueError("Estimator circuits must not have measurements")
```

### ⚠️ Exam Trap Checklist
```
MEASUREMENT TRAPS:
□ TRAP: Adding measurements to Estimator circuit
  → Estimator circuits MUST NOT have measure() or measure_all()
  → "ENM" = Estimator No Measures - will ERROR not warn
□ TRAP: Adding ClassicalRegister thinking it's optional
  → Estimator forbids classical bits entirely: qc.num_clbits must be 0
□ TRAP: Using measure_all() before removing it
  → Cannot undo measure_all() easily; rebuild circuit without measurements
□ TRAP: Thinking Estimator ignores measurements
  → Estimator will ERROR, not ignore measurements
□ TRAP: Confusing Estimator/Sampler measurement requirements
  → Sampler REQUIRES measurements, Estimator FORBIDS them

OBSERVABLE TRAPS:
□ TRAP: Using string for observable instead of SparsePauliOp
  → estimator.run([(qc, 'ZZ')]) is WRONG
  → Use: estimator.run([(qc, SparsePauliOp('ZZ'))])
□ TRAP: Observable qubit count mismatch
  → 3-qubit circuit needs 3-character Pauli: 'ZZZ' not 'ZZ'
□ TRAP: Wrong SparsePauliOp coefficient format
  → SparsePauliOp(['ZZ', 'XX'], 1.0) is WRONG (single value for list)
  → Use: SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5]) with list of coefficients
□ TRAP: Forgetting apply_layout() after transpilation
  → Observable qubits must match transpiled circuit layout
  → Use: obs.apply_layout(transpiled.layout)
□ TRAP: Using complex coefficients in SparsePauliOp
  → Expectation values must be real; complex coefficients cause issues
□ TRAP: Assuming identity observable gives 0
  → SparsePauliOp('III') gives ⟨I⟩ = 1.0 not 0

RESULT EXTRACTION TRAPS:
□ TRAP: Missing .data in result chain
  → result[0].evs is WRONG
  → Use: result[0].data.evs (always need .data!)
□ TRAP: Using singular ev/std instead of plural evs/stds
  → result[0].data.ev is WRONG (no such attribute)
  → Use: result[0].data.evs (plural with s!)
□ TRAP: Forgetting array indexing for single value
  → result[0].data.evs is array, not scalar
  → For single observable: ev = result[0].data.evs[0]
□ TRAP: Confusing evs with counts
  → evs is array of floats (expectation values), not dict like counts
□ TRAP: Expecting integer results
  → Expectation values are floats: -1.0 ≤ ⟨O⟩ ≤ 1.0 for single Pauli
□ TRAP: Not checking result length
  → len(result[0].data.evs) equals number of observables
□ TRAP: Mixing up result indices
  → result[i] for i-th PUB, result[0].data.evs[j] for j-th observable in first PUB

PARAMETER BINDING TRAPS:
□ TRAP: Passing parameter as single value instead of list
  → [(qc, obs, 0.5)] is WRONG
  → Use: [(qc, obs, [0.5])] with list brackets (even for one param!)
□ TRAP: Wrong number of parameter values
  → If circuit has 2 params, must provide exactly 2 values
□ TRAP: Parameter order confusion
  → Values bind in order parameters were created
□ TRAP: Using None for parameters when circuit has parameters
  → None means "no parameters", not "default values"
□ TRAP: Forgetting assign_parameters() in VQE loop
  → Must bind before each run: bound = ansatz.assign_parameters(params)
□ TRAP: Modifying circuit parameters after binding
  → assign_parameters() creates new circuit; original unchanged

PUB FORMAT TRAPS:
□ TRAP: Using Sampler PUB format for Estimator
  → [(qc,)] is Sampler format (missing observable)
  → Use: [(qc, obs)] for Estimator (observable required!)
□ TRAP: Wrong PUB tuple order
  → Order is (circuit, observable, params, precision), not (circuit, params, obs)
□ TRAP: Passing precision as second argument
  → [(qc, 0.01)] is WRONG (0.01 interpreted as observable)
  → Use: [(qc, obs, None, 0.01)]
□ TRAP: Using dict instead of tuple for PUB
  → Cannot use {'circuit': qc, 'observable': obs}, must use (qc, obs)
□ TRAP: Missing observable in single-element tuple
  → [(qc)] is incomplete for Estimator; need [(qc, obs)]

OPTIMIZER TRAPS:
□ TRAP: Using gradient-based optimizers with noisy hardware
  → BFGS, L-BFGS-B require gradients (bad for noise)
  → Use: COBYLA, SPSA (gradient-free)
□ TRAP: Wrong method name in minimize()
  → method='Cobyla' is WRONG (case-sensitive)
  → Use: method='COBYLA' (all caps)
□ TRAP: Not setting maxiter for long VQE runs
  → Default iterations may be too few or too many
  → Use: minimize(..., options={'maxiter': 100})
□ TRAP: Expecting fast convergence on hardware
  → VQE on noisy hardware takes many iterations (50-200+)
□ TRAP: Using same initial params every time
  → Try multiple random starts to avoid local minima

QAOA-SPECIFIC TRAPS:
□ TRAP: Wrong QAOA layer order
  → Cost then Mixer (γ before β), NOT Mixer then Cost
  → Remember: "CostMix" mnemonic
□ TRAP: Wrong parameter order in QAOA
  → Parameters should be (γ, β) not (β, γ)
□ TRAP: Forgetting initial superposition
  → QAOA starts with qc.h(range(n)) on all qubits
□ TRAP: Using single angle instead of doubled
  → QAOA uses qc.rzz(2*gamma, i, j), not qc.rzz(gamma, i, j)
□ TRAP: Missing edges in Cost layer
  → Must apply rzz to all problem edges
□ TRAP: Wrong mixer: using RZ instead of RX
  → Mixer is qc.rx(2*beta, i), not qc.rz(...)

ORDERING CONFUSION TRAPS:
□ TRAP: Confusing SparsePauliOp ordering with bitstring ordering
  → SparsePauliOp: leftmost = q0 ('XIZ' = X on q0)
  → Bitstrings: rightmost = q0 ('01' = q0=1)
  → They're OPPOSITE!
□ TRAP: Reading 'ZIX' as Z on q2
  → 'ZIX' means Z on q0, I on q1, X on q2 (left-to-right)
□ TRAP: Expecting tensor product right-to-left
  → X⊗I⊗Z in math notation = 'XIZ' in Qiskit (same direction)
□ TRAP: Using statevector indexing for SparsePauliOp
  → Statevector index |01⟩ = 1 (binary), but 'ZI' acts on q0 with Z

OPTIONS & CONFIGURATION TRAPS:
□ TRAP: Confusing twirling defaults Sampler vs Estimator
  → Sampler: gates=False, measure=False (both OFF)
  → Estimator: gates=True, measure=True (both ON)
□ TRAP: Setting resilience_level to 3 or higher
  → Valid range is 0-2; higher values cause error
□ TRAP: Expecting resilience_level=2 same speed as 0
  → Level 2 (M3+ZNE) is 5-10x slower than level 0
□ TRAP: Using precision=0.0
  → precision must be positive; 0 or negative raises ValueError
□ TRAP: Expecting exact precision
  → precision is best-effort target, not guaranteed
□ TRAP: Not setting options before first run
  → Options must be set before job submission to take effect

TYPE & METHOD TRAPS:
□ TRAP: Using .coeffs on result instead of observable
  → result doesn't have coeffs; SparsePauliOp.coeffs has them
□ TRAP: Trying to extract counts from Estimator
  → Estimator returns expectation values, not counts
  → For counts, use Sampler
□ TRAP: Using get_counts() on Estimator result
  → No such method; use result[0].data.evs
□ TRAP: Expecting stds to be integers
  → stds are floats (standard deviations), not counts

IMPORT & VERSION TRAPS:
□ TRAP: from qiskit.primitives import Estimator (V1, deprecated)
  → Use: from qiskit.primitives import StatevectorEstimator (V2)
□ TRAP: from qiskit_ibm_runtime import Estimator
  → Use: from qiskit_ibm_runtime import EstimatorV2 (explicit V2)
□ TRAP: Mixing V1 and V2 interfaces
  → V2 uses .run([(qc, obs)]), V1 uses different format
□ TRAP: Importing SparsePauliOp from wrong module
  → Use: from qiskit.quantum_info import SparsePauliOp
  → Not from qiskit.opflow (deprecated)

VQE-SPECIFIC TRAPS:
□ TRAP: Not returning scalar from cost function
  → cost_function must return float, not array: return evs[0]
□ TRAP: Creating new estimator in each cost call
  → Create estimator once outside, reuse in cost function
□ TRAP: Not storing intermediate results
  → VQE iterations lost if not saved during optimization
□ TRAP: Using too simple ansatz
  → Ansatz must be expressive enough to represent ground state
□ TRAP: Starting with zero initial parameters
  → Try small random values: np.random.rand(n_params) * 0.1

COMMON MISTAKES:
□ TRAP: Running circuit without transpilation on hardware
  → Runtime auto-transpiles but exam may test explicit transpilation
□ TRAP: Not handling job failures gracefully
  → Always wrap job.result() in try/except
□ TRAP: Assuming immediate result availability
  → Hardware jobs queue; check job.status() before result()
□ TRAP: Using same circuit object for multiple PUBs
  → If circuit modified after first PUB, affects later; use .copy()
□ TRAP: Forgetting observable for each circuit in batch
  → Each PUB needs (circuit, observable), not just circuit
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 6 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🚫 "ENM" - Estimator No Measures - MOST CRITICAL               │
│    Estimator circuits MUST NOT have measurement gates           │
│    → Opposite of Sampler ("S needs M")                          │
│    → Will ERROR if measurements present                         │
│    💡 Think: "Estimator Expects No Measurements"                │
│                                                                  │
│ 📐 "TiPO" - Tensor in Pauli Order                              │
│    'XIZ' = X⊗I⊗Z (left to right = q0 to q2)                    │
│    → Leftmost character = qubit 0                               │
│    💡 Visual: X I Z → q0 q1 q2 (reading direction matches)      │
│    💡 Opposite of bitstring! ('01' = rightmost is q0)           │
│                                                                  │
│ 🔗 "0-D-EVS" Chain (note the S!) - CRITICAL PATH               │
│    result[0].data.evs (plural!)                                 │
│    → [0] = first PUB, data = container, evs = expectation values│
│    💡 "Zero Dogs Eat Very Slowly" - each word is a step         │
│    💡 Always plural: evs and stds (NEVER ev or std)             │
│                                                                  │
│ 📦 "COPP" - Circuit Observable Params Precision                 │
│    Estimator PUB: (circuit, observable, params, precision)      │
│    → All except circuit/observable are optional                 │
│    → Order matters: cannot swap positions!                      │
│    💡 "Cops Observe People Precisely"                           │
│                                                                  │
│ 🎯 "COBYLA for Quantum" - OPTIMIZER CHOICE                      │
│    Gradient-free optimizer for noisy VQE/QAOA                   │
│    → No gradients needed (robust to noise)                      │
│    → All caps: method='COBYLA' not 'Cobyla'                     │
│    💡 "Can't Obtain By Yielding Linear Approximations"          │
│                                                                  │
│ 🔄 "CostMix" - Cost then Mixer - QAOA ORDER                     │
│    QAOA layer order: Cost(γ) then Mixer(β)                      │
│    → γ comes before β in parameters                             │
│    → Cost encodes problem, Mixer maintains superposition        │
│    💡 "First you pay the Cost, then you Mix it up"              │
│                                                                  │
│ 🛡️ "012 = None-M3-ZNE" - RESILIENCE LEVELS                     │
│    resilience_level values:                                     │
│    → 0 = None (ideal/debug) - fastest                           │
│    → 1 = M3 mitigation - moderate speed                         │
│    → 2 = M3 + ZNE (Zero Noise Extrapolation) - slowest but best│
│    💡 "0 is None, 1 is M3, 2 is M3+ZNE" (count up!)             │
│                                                                  │
│ 🔀 "GMGM vs GOMO" - TWIRLING DEFAULTS                           │
│    Estimator: Gates More, Measure More (both ON = True)         │
│    Sampler: Gates Off, Measure Off (both OFF = False)           │
│    💡 Estimator is "active", Sampler is "passive"               │
│    💡 E = Energized (on), S = Still (off)                       │
│                                                                  │
│ 🔤 "Plural with S" - RESULT ATTRIBUTES                          │
│    result[0].data.evs (plural with s)                           │
│    result[0].data.stds (plural with s)                          │
│    → NEVER singular ev or std (AttributeError!)                 │
│    💡 "evs" rhymes with "several" (multiple values)             │
│                                                                  │
│ 🎭 "E vs S" - Estimator vs Sampler Quick Reference              │
│    Estimator: NO measurements | Returns ⟨O⟩ | Needs observable  │
│    Sampler: Measurements REQUIRED | Returns counts | No observable│
│    💡 "Estimator Expects numbers, Sampler Sees bits"            │
│                                                                  │
│ 🧬 "VQE = Vary-Quantum-Estimate" - VQE WORKFLOW                 │
│    1. Vary parameters (classical optimizer)                     │
│    2. Quantum circuit with new parameters                       │
│    3. Estimate energy ⟨H⟩                                       │
│    4. Repeat until converged                                    │
│    💡 Alternating quantum-classical loop                        │
│                                                                  │
│ ⚖️ "Observable Must Match" - QUBIT COUNT RULE                   │
│    Circuit with n qubits needs n-character Pauli string         │
│    → 3 qubits → 'ZZZ', 'XIZ', 'III' (all length 3)             │
│    💡 "One letter per qubit"                                    │
│                                                                  │
│ 🎲 "Expectation = Average" - INTERPRETATION                     │
│    Expectation value ⟨O⟩ is weighted average of eigenvalues     │
│    → Range: -1 to +1 for single Pauli operator                  │
│    → Not a probability (can be negative!)                       │
│    💡 "Expected value if you measured many times"               │
│                                                                  │
│ 🔧 "SparsePauliOp = String + Coeffs" - CONSTRUCTION             │
│    SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])                      │
│    → Two lists: Pauli strings and their coefficients            │
│    💡 "Strings describe operators, coeffs are weights"          │
│                                                                  │
│ 🗺️ "Layout After Transpile" - OBSERVABLE REMAPPING             │
│    After transpilation, qubits may be remapped                  │
│    → Must use: obs.apply_layout(transpiled.layout)              │
│    💡 "Transpile changes map, update observable GPS"            │
│                                                                  │
│ 🚀 "Precision ≠ Accuracy" - HARDWARE LIMITATION                 │
│    precision parameter is target, not guarantee                 │
│    → Hardware noise limits achievable precision                 │
│    → Higher precision = more shots = slower                     │
│    💡 "Ask for precision, get what hardware can deliver"        │
│                                                                  │
│ 🎚️ "Gamma Before Beta" - QAOA PARAMETERS                       │
│    QAOA parameters: (γ, β) in alphabetical order                │
│    → γ controls Cost layer                                      │
│    → β controls Mixer layer                                     │
│    💡 "Alphabetical: Cost before Mixer"                         │
│                                                                  │
│ 🔄 "assign_parameters Returns New" - BINDING BEHAVIOR           │
│    assign_parameters() creates NEW circuit, doesn't modify      │
│    → bound_qc = qc.assign_parameters([...])                     │
│    → Original qc unchanged                                      │
│    💡 "Binding is non-destructive"                              │
│                                                                  │
│ 📊 "evs is Array Not Scalar" - TYPE AWARENESS                   │
│    result[0].data.evs is numpy array, even for single observable│
│    → Must index: ev = result[0].data.evs[0]                     │
│    💡 "evs = array of values, need [0] to extract first"        │
│                                                                  │
│ ⚡ "V2 Only" - VERSION ENFORCEMENT                              │
│    Only use V2 primitives: StatevectorEstimator, EstimatorV2    │
│    → V1 (Estimator) is deprecated                               │
│    💡 "V2 is the way, V1 is yesterday"                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║         SECTION 6: ESTIMATOR - ONE-PAGE SUMMARY                       ║
║                      (12% of Exam - ~8 Questions)                      ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 BASIC USAGE WORKFLOW                                               ║
║  ├─ 1. IMPORTS                                                         ║
║  │   ├─ from qiskit.primitives import StatevectorEstimator  # ideal  ║
║  │   ├─ from qiskit_ibm_runtime import EstimatorV2  # hardware       ║
║  │   └─ from qiskit.quantum_info import SparsePauliOp                ║
║  ├─ 2. CREATE CIRCUIT WITHOUT MEASUREMENTS (CRITICAL!)                ║
║  │   ├─ qc = QuantumCircuit(2)  # NO ClassicalRegister               ║
║  │   ├─ qc.h(0); qc.cx(0,1)  # quantum operations                     ║
║  │   └─ NO qc.measure_all()! ← Estimator FORBIDS measurements        ║
║  ├─ 3. CREATE OBSERVABLE                                               ║
║  │   └─ obs = SparsePauliOp('ZZ')  # must match circuit qubit count  ║
║  ├─ 4. INITIALIZE ESTIMATOR                                            ║
║  │   └─ estimator = StatevectorEstimator()  # or EstimatorV2(backend)║
║  ├─ 5. RUN WITH PUB FORMAT                                             ║
║  │   └─ job = estimator.run([(qc, obs)])  # (circuit, observable)    ║
║  ├─ 6. EXTRACT EXPECTATION VALUES                                      ║
║  │   ├─ result = job.result()  # PrimitiveResult                     ║
║  │   └─ ev = result[0].data.evs[0]  # note: evs is array, [0] index!║
║  └─ Key: NO measurements, MUST have observable, evs plural            ║
║                                                                        ║
║  📊 SPARSEPAULI ORDERING (Critical for Exam!)                          ║
║  ├─ Convention: Leftmost character = qubit 0 (OPPOSITE of bitstrings)║
║  ├─ Examples:                                                          ║
║  │   ├─ SparsePauliOp('XIZ') = X⊗I⊗Z                                  ║
║  │   │   ├─ X acts on qubit 0 (leftmost)                              ║
║  │   │   ├─ I acts on qubit 1 (middle)                                ║
║  │   │   └─ Z acts on qubit 2 (rightmost)                             ║
║  │   ├─ SparsePauliOp('ZZ') = Z⊗Z on qubits 0,1                       ║
║  │   └─ Position matches qubit: string[i] → qubit i                   ║
║  └─ TRAP: Bitstrings use opposite convention! (rightmost = q0)        ║
║                                                                        ║
║  📦 PUB FORMATS (Primitive Unified Bloc)                               ║
║  ├─ Anatomy: (circuit, observable, parameters, precision)             ║
║  │   ├─ circuit: QuantumCircuit WITHOUT measurements                  ║
║  │   ├─ observable: SparsePauliOp (REQUIRED for Estimator!)           ║
║  │   ├─ parameters: list of values or None (optional)                 ║
║  │   └─ precision: float target or None (optional)                    ║
║  ├─ EXAMPLES:                                                          ║
║  │   ├─ Basic:           [(qc, obs)]                # minimal         ║
║  │   ├─ With params:     [(qc, obs, [0.5, 1.2])]  # 2 param values   ║
║  │   ├─ With precision:  [(qc, obs, None, 0.01)]  # None placeholder ║
║  │   ├─ Full spec:       [(qc, obs, [0.5], 0.01)] # all specified    ║
║  │   └─ Multiple PUBs:   [(qc1, obs1), (qc2, obs2), (qc3, obs3)]     ║
║  └─ Critical: Observable REQUIRED (unlike Sampler where it's absent)  ║
║                                                                        ║
║  🔗 RESULT EXTRACTION CHAIN (MEMORIZE!)                                ║
║  ├─ Full path: result[0].data.evs[0]                                  ║
║  │   ├─ result       → PrimitiveResult (list-like container)          ║
║  │   ├─ [0]          → Index first PUB (PubResult object)             ║
║  │   ├─ .data        → DataBin (holds expectation value arrays)       ║
║  │   ├─ .evs         → Array of expectation values (PLURAL!)          ║
║  │   └─ [0]          → Index first observable (evs is array)          ║
║  ├─ Alternative attributes:                                            ║
║  │   └─ .stds        → Array of standard deviations (also plural!)    ║
║  ├─ Multiple observables:                                              ║
║  │   ├─ evs = result[0].data.evs  # all values: [⟨O₁⟩, ⟨O₂⟩, ...]    ║
║  │   └─ stds = result[0].data.stds  # all stds: [σ₁, σ₂, ...]        ║
║  └─ Multi-PUB indexing:                                                ║
║      ├─ result[0].data.evs  # first circuit-observable                ║
║      ├─ result[1].data.evs  # second circuit-observable               ║
║      └─ result[i].data.evs  # i-th PUB                                ║
║                                                                        ║
║  🔄 MULTIPLE OBSERVABLES (Efficiency Pattern)                          ║
║  ├─ Single circuit, multiple observables (efficient!):                ║
║  │   ├─ obs_list = [SparsePauliOp('ZZ'), SparsePauliOp('XX')]        ║
║  │   ├─ job = estimator.run([(qc, obs_list)])  # one PUB             ║
║  │   ├─ evs = result[0].data.evs  # array: [⟨ZZ⟩, ⟨XX⟩]              ║
║  │   └─ Benefit: shares circuit evaluation across observables         ║
║  └─ Multiple PUBs (separate circuits):                                 ║
║      ├─ job = estimator.run([(qc1, obs1), (qc2, obs2)])               ║
║      ├─ ev1 = result[0].data.evs[0]  # from qc1                       ║
║      └─ ev2 = result[1].data.evs[0]  # from qc2                       ║
║                                                                        ║
║  🧬 VQE PATTERN (Variational Quantum Eigensolver)                      ║
║  ├─ Purpose: Find ground state energy of Hamiltonian                  ║
║  ├─ Components:                                                        ║
║  │   ├─ H = SparsePauliOp([...])  # Hamiltonian (energy operator)    ║
║  │   ├─ ansatz = parameterized circuit (NO measurements)              ║
║  │   ├─ cost_func: params → ⟨H⟩ (expectation value)                   ║
║  │   └─ optimizer: minimize cost_func (COBYLA recommended)            ║
║  ├─ Complete workflow:                                                 ║
║  │   ├─ 1. def cost_function(params):                                 ║
║  │   │       bound_qc = ansatz.assign_parameters(params)              ║
║  │   │       job = estimator.run([(bound_qc, H)])                     ║
║  │   │       return job.result()[0].data.evs[0]                       ║
║  │   ├─ 2. initial_params = [0.0, 0.0]  # or random                  ║
║  │   ├─ 3. result = minimize(cost_function, initial_params,           ║
║  │   │                        method='COBYLA')                        ║
║  │   ├─ 4. optimal_energy = result.fun                                ║
║  │   └─ 5. optimal_params = result.x                                  ║
║  └─ Key: Ansatz NO measurements, use COBYLA (gradient-free)           ║
║                                                                        ║
║  🔄 QAOA PATTERN (Quantum Approximate Optimization Algorithm)          ║
║  ├─ Purpose: Approximate solution to combinatorial optimization       ║
║  ├─ Structure (MEMORIZE ORDER!):                                       ║
║  │   ├─ 1. Initial state: qc.h(range(n))  # equal superposition      ║
║  │   ├─ 2. Cost layer: encode problem (γ parameter)                  ║
║  │   │   └─ qc.rzz(2*gamma, i, j)  # for each problem edge           ║
║  │   ├─ 3. Mixer layer: maintain superposition (β parameter)          ║
║  │   │   └─ qc.rx(2*beta, i)  # for each qubit                       ║
║  │   └─ 4. NO measurements! (Use Estimator to get ⟨H⟩)                ║
║  ├─ Parameter convention:                                              ║
║  │   ├─ γ (gamma) controls Cost layer                                 ║
║  │   ├─ β (beta) controls Mixer layer                                 ║
║  │   └─ Order: (γ, β) - "Cost then Mixer" or "CostMix"                ║
║  ├─ Complete example:                                                  ║
║  │   ├─ def qaoa_cost(params):                                        ║
║  │   │       gamma, beta = params                                     ║
║  │   │       qc = build_qaoa_circuit(gamma, beta)                     ║
║  │   │       job = estimator.run([(qc, cost_hamiltonian)])            ║
║  │   │       return job.result()[0].data.evs[0]                       ║
║  │   └─ result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')    ║
║  └─ Critical: Cost BEFORE Mixer (γ before β)                          ║
║                                                                        ║
║  ⚙️ ADVANCED OPTIONS (estimator.options)                               ║
║  ├─ Error mitigation:                                                  ║
║  │   ├─ .resilience_level = 0  # none (ideal/fastest)                ║
║  │   ├─ .resilience_level = 1  # M3 mitigation (moderate)            ║
║  │   └─ .resilience_level = 2  # M3+ZNE (best but 5-10x slower)      ║
║  ├─ Twirling (randomized compilation):                                ║
║  │   ├─ .twirling.enable_gates = True   # default ON for Estimator  ║
║  │   ├─ .twirling.enable_measure = True # default ON for Estimator  ║
║  │   └─ .twirling.num_randomizations = 32  # rounds of randomization ║
║  ├─ Circuit optimization:                                              ║
║  │   ├─ .optimization_level = 3  # transpiler (0-3)                  ║
║  │   └─ .default_precision = 0.01  # target precision                ║
║  └─ Dynamical Decoupling:                                              ║
║      ├─ .dynamical_decoupling.enable = True                           ║
║      └─ .dynamical_decoupling.sequence_type = 'XY4'                   ║
║                                                                        ║
║  🎭 ESTIMATOR VS SAMPLER (Key Differences)                             ║
║  ├─ Estimator:                                                         ║
║  │   ├─ NO measurements (FORBIDDEN!)                                   ║
║  │   ├─ Returns: expectation values ⟨ψ|O|ψ⟩ (continuous floats)       ║
║  │   ├─ PUB format: (circuit, observable)                             ║
║  │   ├─ Use case: VQE, QAOA, computing energies/observables           ║
║  │   ├─ Result: result[0].data.evs (array of floats)                  ║
║  │   └─ Twirling defaults: gates=True, measure=True (both ON)         ║
║  ├─ Sampler:                                                           ║
║  │   ├─ Measurements REQUIRED                                          ║
║  │   ├─ Returns: counts/bitstrings (discrete outcomes)                 ║
║  │   ├─ PUB format: (circuit,) - no observable                        ║
║  │   ├─ Use case: sampling probability distributions                   ║
║  │   ├─ Result: result[0].data.meas.get_counts() (dict)               ║
║  │   └─ Twirling defaults: gates=False, measure=False (both OFF)      ║
║  └─ Key: Mutually exclusive patterns - NEVER mix!                     ║
║                                                                        ║
║  🔢 OBSERVABLE CONSTRUCTION                                            ║
║  ├─ Single Pauli string:                                               ║
║  │   ├─ SparsePauliOp('Z')    # single qubit                          ║
║  │   ├─ SparsePauliOp('ZZ')   # two qubits                            ║
║  │   └─ SparsePauliOp('XIZ')  # three qubits (X⊗I⊗Z)                  ║
║  ├─ Weighted sum (Hamiltonian):                                        ║
║  │   ├─ SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])  # 1.0*ZZ + 0.5*XX   ║
║  │   └─ Alternative: SparsePauliOp.from_list([('ZZ', 1.0), ...])     ║
║  ├─ Qubit count constraint:                                            ║
║  │   └─ Must match circuit: 3-qubit circuit → 3-char Pauli string     ║
║  └─ Special cases:                                                     ║
║      ├─ Identity: SparsePauliOp('III') → always returns 1.0           ║
║      └─ After transpile: obs.apply_layout(layout) to remap qubits     ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (HIGHEST PRIORITY!)                              ║
║  ╔════════════════════════════════════════════════════════════════╗  ║
║  ║ 1. ❌ Adding measurements → Estimator ERROR (not warning!)      ║  ║
║  ║    ✓ NEVER use measure() or measure_all() with Estimator       ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 2. ❌ Using string observable: estimator.run([(qc, 'ZZ')])      ║  ║
║  ║    ✓ MUST use SparsePauliOp: run([(qc, SparsePauliOp('ZZ'))])  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 3. ❌ result[0].evs - missing .data                             ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (never skip .data!)           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 4. ❌ result[0].data.ev - using singular (no such attribute!)   ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (plural with s!)              ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 5. ❌ Parameters as scalar: (qc, obs, 0.5)                      ║  ║
║  ║    ✓ MUST be list: (qc, obs, [0.5]) even for single param!     ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 6. ❌ Using Sampler PUB format: [(qc,)]                         ║  ║
║  ║    ✓ Estimator needs observable: [(qc, obs)]                   ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 7. ❌ Gradient optimizers: BFGS, L-BFGS-B (fail with noise)     ║  ║
║  ║    ✓ Use gradient-free: method='COBYLA' or 'SPSA'              ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 8. ❌ QAOA order: Mixer then Cost                               ║  ║
║  ║    ✓ CORRECT: Cost then Mixer (γ before β) "CostMix"           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 9. ❌ Ordering: 'ZIX' means X on q0 (WRONG!)                    ║  ║
║  ║    ✓ SparsePauliOp 'ZIX' = Z on q0, I on q1, X on q2 (L→R)     ║  ║
║  ║    ✓ OPPOSITE of bitstrings! ('01' = rightmost q0)             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 10. ❌ Not using apply_layout() after transpilation             ║  ║
║  ║     ✓ MUST remap: obs.apply_layout(transpiled.layout)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 11. ❌ Twirling defaults: assuming same as Sampler              ║  ║
║  ║     ✓ Estimator: gates=True, measure=True (both ON)            ║  ║
║  ║     ✓ Sampler: gates=False, measure=False (both OFF)           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 12. ❌ Observable qubit mismatch: 3-qubit circuit, 'ZZ' obs     ║  ║
║  ║     ✓ MUST match: 3 qubits → 'ZZI' or 'XIZ' (3 chars)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 13. ❌ Forgetting assign_parameters() in VQE loop               ║  ║
║  ║     ✓ MUST bind: bound = ansatz.assign_parameters(params)      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 14. ❌ Treating evs as scalar when it's array                   ║  ║
║  ║     ✓ evs is array: use evs[0] to extract single value         ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 15. ❌ Using V1 import: from qiskit.primitives import Estimator ║  ║
║  ║     ✓ CORRECT V2: import StatevectorEstimator or EstimatorV2   ║  ║
║  ╚════════════════════════════════════════════════════════════════╝  ║
║                                                                        ║
║  💡 MEMORY AIDS (CRITICAL!)                                            ║
║  ├─ "ENM" - Estimator No Measures (MOST CRITICAL!)                    ║
║  ├─ "TiPO" - Tensor in Pauli Order (leftmost = q0)                    ║
║  ├─ "0-D-EVS" - result[0].data.evs chain (plural!)                    ║
║  ├─ "COPP" - Circuit Observable Params Precision                      ║
║  ├─ "COBYLA for Quantum" - gradient-free optimizer                    ║
║  ├─ "CostMix" - Cost layer then Mixer layer (γ before β)              ║
║  ├─ "012 = None-M3-ZNE" - resilience levels                           ║
║  └─ "GMGM vs GOMO" - Estimator (on/on) vs Sampler (off/off)           ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
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
