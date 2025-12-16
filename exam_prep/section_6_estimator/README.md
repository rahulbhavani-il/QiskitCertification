# Section 6: Estimator Primitive & VQE/QAOA (12% of Exam)

> **Exam Weight**: ~8 questions | **Difficulty**: Medium-High | **Must Master**: ✅✅✅

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

- Calculate expectation values ⟨ψ|H|ψ⟩
- Observable specification (SparsePauliOp)
- EstimatorV2 API
- VQE (Variational Quantum Eigensolver) pattern
- QAOA (Quantum Approximate Optimization Algorithm)
- scipy.optimize integration

---

## 🎯 Core Concepts

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 1: Z operator on |+⟩ state

State: |+⟩ = 1/√2(|0⟩ + |1⟩)
Observable: Z = |0⟩⟨0| - |1⟩⟨1|

Step-by-step calculation:
⟨Z⟩ = ⟨+|Z|+⟩
    = 1/√2(⟨0| + ⟨1|) · Z · 1/√2(|0⟩ + |1⟩)
    = 1/2(⟨0| + ⟨1|) · (|0⟩ - |1⟩)
    = 1/2(⟨0|0⟩ - ⟨0|1⟩ + ⟨1|0⟩ - ⟨1|1⟩)
    = 1/2(1 - 0 + 0 - 1)
    = 0

Using eigenvalue decomposition:
Z eigenstates: |0⟩ (λ₊=+1), |1⟩ (λ₋=-1)
Probabilities: P(|0⟩) = |⟨0|+⟩|² = |1/√2|² = 1/2
              P(|1⟩) = |⟨1|+⟩|² = |1/√2|² = 1/2
              
⟨Z⟩ = (+1)·(1/2) + (-1)·(1/2) = 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Example 2: Multi-qubit observable ZZ on Bell state

State: |Φ⁺⟩ = 1/√2(|00⟩ + |11⟩)
Observable: ZZ = Z⊗Z

ZZ eigenstates and eigenvalues:
|00⟩ → (+1)(+1) = +1
|01⟩ → (+1)(-1) = -1
|10⟩ → (-1)(+1) = -1
|11⟩ → (-1)(-1) = +1

Calculation:
⟨ZZ⟩ = ⟨Φ⁺|ZZ|Φ⁺⟩
     = 1/2(⟨00| + ⟨11|) · ZZ · (|00⟩ + |11⟩)
     = 1/2(⟨00|ZZ|00⟩ + ⟨00|ZZ|11⟩ + ⟨11|ZZ|00⟩ + ⟨11|ZZ|11⟩)
     = 1/2((+1) + 0 + 0 + (+1))
     = 1

Using probabilities:
P(|00⟩) = 1/2 → contributes (+1)·(1/2) = +1/2
P(|11⟩) = 1/2 → contributes (+1)·(1/2) = +1/2
⟨ZZ⟩ = 1/2 + 1/2 = 1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Theory: Hermitian Operators

For physical observables:
• Must be Hermitian: O† = O
• Eigenvalues are real: λᵢ ∈ ℝ
• Eigenstates are orthonormal: ⟨φᵢ|φⱼ⟩ = δᵢⱼ
• Spectral decomposition: O = Σᵢ λᵢ|φᵢ⟩⟨φᵢ|

Pauli operators (Z, X, Y):
Eigenvalues: ±1
Expectation range: ⟨O⟩ ∈ [-1, +1]

General Hamiltonian:
H = Σⱼ cⱼ Pⱼ  (sum of Pauli terms)
where cⱼ ∈ ℝ (coefficients), Pⱼ ∈ {I,X,Y,Z}⊗ⁿ

⟨H⟩ = Σⱼ cⱼ⟨Pⱼ⟩  (linearity of expectation)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Connection to Measurements:

Statistical interpretation:
If you measure O repeatedly on identical states |ψ⟩:

Measurements: λ₁, λ₂, λ₃, ..., λₙ (each is an eigenvalue)
Sample mean: μₙ = (1/n)Σₖ₌₁ⁿ λₖ

As n→∞:  μₙ → ⟨O⟩ = ⟨ψ|O|ψ⟩

This is why Estimator can calculate ⟨O⟩ either:
1. Exactly (statevector simulation)
2. Statistically (real hardware with shots)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Variational Principle (VQE Foundation):

For any quantum state |ψ⟩ and Hamiltonian H:
⟨ψ|H|ψ⟩ ≥ E₀

where E₀ is the ground state energy (lowest eigenvalue of H).

Proof sketch:
Expand |ψ⟩ in eigenbasis of H:
|ψ⟩ = Σᵢ cᵢ|Eᵢ⟩  where H|Eᵢ⟩ = Eᵢ|Eᵢ⟩

⟨H⟩ = Σᵢ |cᵢ|² Eᵢ
    ≥ E₀ · Σᵢ |cᵢ|²  (since Eᵢ ≥ E₀ for all i)
    = E₀  (normalization: Σᵢ |cᵢ|² = 1)

Equality holds ⟺ |ψ⟩ = |E₀⟩ (ground state)

This is why VQE works: minimizing ⟨H⟩ pushes toward ground state!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

## 📈 Estimator Primitive

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create circuit (NO measurements needed!)
qc = QuantumCircuit(1)
qc.h(0)  # Create |+⟩

# Define observable
observable = SparsePauliOp("Z")  # Z operator

# Create Estimator
estimator = StatevectorEstimator()

# Run (circuit, observable) pair
job = estimator.run([(qc, observable)])

# Get expectation value
result = job.result()
expectation_value = result[0].data.evs

print(f"⟨Z⟩ = {expectation_value}")  # ≈ 0.0
```

### ⚠️ EXAM CRITICAL: SparsePauliOp Construction

**Observable Format Rules**:
```python
from qiskit.quantum_info import SparsePauliOp

# Single Pauli operator
SparsePauliOp('Z')     # Z on qubit 0
SparsePauliOp('X')     # X on qubit 0

# Multi-qubit tensor products (RIGHT TO LEFT!)
SparsePauliOp('ZZ')    # Z⊗Z: Z on qubit 0 AND Z on qubit 1
SparsePauliOp('XY')    # X⊗Y: X on qubit 0 AND Y on qubit 1
SparsePauliOp('IZ')    # I⊗Z: Identity on qubit 0, Z on qubit 1

# Multiple terms (sum) - Hamiltonians
SparsePauliOp(['ZZ', 'XX'])  # ZZ + XX
SparsePauliOp(['ZZ', 'XX'], [0.5, 0.5])  # 0.5*ZZ + 0.5*XX

# H2 Molecule Example (EXAM COMMON!)
H = SparsePauliOp(
    ["II", "ZI", "IZ", "ZZ", "XX"],
    [-1.05, 0.39, 0.39, -0.01, 0.18]
)
```

**⚠️ EXAM TRAP: Qubit Ordering**
```python
# String 'ZX' means:
#  ┌─┬─┐
#  │Z│X│  = Z on qubit 0, X on qubit 1
#  └─┴─┘
#  q0 q1

# NOT left-to-right visually!
# It's TENSOR PRODUCT order

SparsePauliOp('ZXY')  # Z⊗X⊗Y
# Qubit 0: Z
# Qubit 1: X  
# Qubit 2: Y
```

**CRITICAL: Estimator does NOT need measurements**
```python
qc = QuantumCircuit(1)
qc.h(0)
# No measure() needed!
✅ estimator.run([(qc, SparsePauliOp('Z'))])  # Correct!

# Adding measure() will cause ERROR
qc.measure_all()
❌ estimator.run([(qc, SparsePauliOp('Z'))])  # ERROR!
```

### ⚠️ EXAM CRITICAL: Estimator PUB Format Complete Reference

**PUB = (circuit, observable, parameter_values, precision)**

| Scenario | PUB Format | Example |
|----------|------------|----------|
| Basic circuit + observable | `[(circuit, observable)]` | `estimator.run([(qc, obs)])` |
| With parameter values | `[(circuit, observable, params)]` | `estimator.run([(qc, obs, [0.5, 1.2])])` |
| With precision | `[(circuit, observable, params, precision)]` | `estimator.run([(qc, obs, [0.5], 0.01)])` |
| No params, with precision | `[(circuit, observable, None, precision)]` | `estimator.run([(qc, obs, None, 0.01)])` |
| Multiple PUBs | `[(qc1, obs1), (qc2, obs2)]` | See below |

**PUB Tuple Structure**:
```python
pub = (circuit, observable, parameter_values, precision)
#       │         │              │               │
#       │         │              │               └─ Optional: target precision (float)
#       │         │              └─ Optional: list of parameter values
#       │         └─ REQUIRED: SparsePauliOp observable
#       └─ REQUIRED: QuantumCircuit (NO measurements!)
```

**Complete Examples**:
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import Parameter

# Example 1: Basic usage (circuit, observable)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
obs = SparsePauliOp('ZZ')

estimator = StatevectorEstimator()
job = estimator.run([(qc, obs)])  # Basic PUB

# Example 2: Parameterized circuit with values
theta = Parameter('θ')
qc_param = QuantumCircuit(1)
qc_param.ry(theta, 0)

pub = (qc_param, SparsePauliOp('Z'), [0.5])  # θ = 0.5
job = estimator.run([pub])

# Example 3: With custom precision (for hardware)
pub = (qc, obs, None, 0.01)  # precision = 0.01
job = estimator.run([pub])

# Example 4: Multiple parameter sets (batch)
theta_values = [[0.0], [0.5], [1.0], [1.5]]
pubs = [(qc_param, SparsePauliOp('Z'), val) for val in theta_values]
job = estimator.run(pubs)

# Example 5: Multiple observables for same circuit
observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]
pubs = [(qc, obs) for obs in observables]
job = estimator.run(pubs)
```

**Common PUB Mistakes for Estimator**:
```python
❌ WRONG: estimator.run([circuit])  # Missing observable!
✅ RIGHT: estimator.run([(circuit, observable)])

❌ WRONG: estimator.run([(circuit, 'ZZ')])  # String not SparsePauliOp!
✅ RIGHT: estimator.run([(circuit, SparsePauliOp('ZZ'))])

❌ WRONG: estimator.run([(circuit_with_measure, observable)])  # Has measurements!
✅ RIGHT: Remove measurements from circuit

❌ WRONG: estimator.run([(circuit, observable, 0.5)])  # params must be list!
✅ RIGHT: estimator.run([(circuit, observable, [0.5])])
```

**Memory Aid: "COPPP" for Estimator PUB**
- **C**ircuit (required, NO measurements)
- **O**bservable (required, SparsePauliOp)
- **P**arameters (optional, list of values)
- **P**recision (optional, float)

### Multi-Observable Measurement

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Define multiple observables
observables = [
    SparsePauliOp("ZZ"),  # Z⊗Z correlation
    SparsePauliOp("XX"),  # X⊗X correlation
    SparsePauliOp("YY"),  # Y⊗Y correlation
    SparsePauliOp("ZI"),  # Single qubit Z
]

# Create PUBs: (circuit, observable) pairs
pubs = [(qc, obs) for obs in observables]

# Run all at once
estimator = StatevectorEstimator()
job = estimator.run(pubs)

# Get results
results = job.result()
for i, label in enumerate(["ZZ", "XX", "YY", "ZI"]):
    evs = results[i].data.evs
    print(f"⟨{label}⟩ = {evs:.3f}")

# Output:
# ⟨ZZ⟩ = 1.000  ← Perfect correlation
# ⟨XX⟩ = 1.000  ← Also correlated
# ⟨YY⟩ = -1.000 ← Anti-correlated
# ⟨ZI⟩ = 0.000  ← No bias
```

### Estimator with Real Hardware

```python
from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2 as Estimator, Options

# Connect
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Configure error mitigation
options = Options()
options.resilience_level = 1  # M3 mitigation (EXAM TESTED!)
options.optimization_level = 3  # Aggressive transpilation
options.execution.shots = 4096  # Number of shots

# Create Estimator
estimator = Estimator(backend=backend, options=options)

# Run
job = estimator.run([(qc, observable)])
result = job.result()
evs = result[0].data.evs
stds = result[0].data.stds  # Standard deviations (plural!)
```

### 🎓 Exam Question Patterns - Estimator

**Pattern 1: "What observable for this Hamiltonian?"**
```python
# Given: H = 1.5*ZZ + 0.3*XX - 0.7*Z
obs = SparsePauliOp(['ZZ', 'XX', 'ZI'], [1.5, 0.3, -0.7])
```

**Pattern 2: "Qubit ordering in Pauli strings"**
```python
# STRING: 'ZXY' means:
# Qubit 0: Z (leftmost)
# Qubit 1: X (middle)
# Qubit 2: Y (rightmost)

# It's tensor product: Z ⊗ X ⊗ Y
```

**Pattern 3: "Access expectation value and std"**
```python
result[0].data.evs   # Expectation values (plural!)
result[0].data.stds  # Standard deviations (plural!)

# ❌ result[0].data.ev   # WRONG: Missing 's'
# ❌ result[0].evs       # WRONG: Missing .data
```

**Pattern 4: "resilience_level values"**
```python
options.resilience_level = 0  # No error mitigation (fast but noisy)
options.resilience_level = 1  # M3 mitigation (balanced) ← RECOMMENDED
options.resilience_level = 2  # ZNE + PEC (slow but accurate)
```

---

## 🔬 VQE Pattern (Variational Quantum Eigensolver)

### What is VQE?

**VQE**: Hybrid quantum-classical algorithm to find ground state energy

```
Goal: Minimize ⟨ψ(θ)|H|ψ(θ)⟩

Components:
1. Ansatz: Parameterized circuit |ψ(θ)⟩
2. Hamiltonian: Observable H (energy operator)
3. Estimator: Computes ⟨H⟩
4. Classical Optimizer: Adjusts θ to minimize ⟨H⟩

Variational Principle: ⟨ψ|H|ψ⟩ ≥ E₀
(Measured energy always ≥ ground state energy)
```

### Complete VQE Implementation

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
ansatz.ry(theta, 0)

# 3. Define cost function
estimator = StatevectorEstimator()
iteration_count = [0]

def cost_function(params):
    # Bind parameters
    qc = ansatz.assign_parameters(params)
    
    # Calculate ⟨H⟩
    job = estimator.run([(qc, H)])
    result = job.result()
    energy = result[0].data.evs
    
    # Track progress
    iteration_count[0] += 1
    if iteration_count[0] % 10 == 0:
        print(f"Iteration {iteration_count[0]}: E = {energy:.6f}")
    
    return energy

# 4. Optimize with classical optimizer
print("Starting VQE optimization...")
initial_params = [0.0, 0.0]

result = minimize(
    cost_function,
    initial_params,
    method='COBYLA',  # EXAM COMMON!
    options={'maxiter': 100}
)

# 5. Results
print(f"\nGround state energy: {result.fun:.6f}")
print(f"Optimal parameters: θ={result.x[0]:.4f}, φ={result.x[1]:.4f}")
print(f"Total iterations: {iteration_count[0]}")
```

### VQE Optimizers (EXAM TESTED!)

```python
from scipy.optimize import minimize

# COBYLA - Constrained Optimization BY Linear Approximation
# • Gradient-free (good for noisy quantum functions)
# • Most common in Qiskit examples
# • No derivatives needed
result = minimize(cost, [0.0], method='COBYLA')

# SLSQP - Sequential Least SQuares Programming
# • Gradient-free
# • Handles constraints well
result = minimize(cost, [0.0], method='SLSQP')

# Nelder-Mead - Simplex method
# • Gradient-free
# • Good for low-dimensional problems
result = minimize(cost, [0.0], method='Nelder-Mead')

# EXAM TIP: All are gradient-free (suitable for quantum!)
# COBYLA is the most commonly tested
```

---

## 🎯 QAOA Pattern (Quantum Approximate Optimization Algorithm)

### What is QAOA?

**QAOA**: Variational algorithm for combinatorial optimization

```
QAOA Structure:
┌──────────────────────────────────┐
│ 1. Initial State: |+⟩ⁿ          │
│    (equal superposition)         │
├──────────────────────────────────┤
│ 2. Cost Layer: e^(-iγH_cost)    │
│    - Problem-specific            │
│    - rzz gates for graphs        │
├──────────────────────────────────┤
│ 3. Mixer Layer: e^(-iβH_mixer)  │
│    - Standard rx gates           │
│    - Explores solution space     │
├──────────────────────────────────┤
│ 4. Repeat p times (depth)       │
└──────────────────────────────────┘

Parameters:
• γ (gamma): Cost layer angles
• β (beta): Mixer layer angles
• p: Number of layers
```

### QAOA for MaxCut

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# MaxCut on triangle graph: 3 nodes, 3 edges
# Edges: (0,1), (1,2), (0,2)

# Cost Hamiltonian
H_cost = SparsePauliOp(
    ['ZZ I', 'Z IZ', 'I ZZ'],  # Edges (0,1), (0,2), (1,2)
    [1.0, 1.0, 1.0]
)

gamma = Parameter('γ')
beta = Parameter('β')

def qaoa_circuit(p=1):
    """Create QAOA circuit with p layers"""
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

# QAOA optimization
estimator = StatevectorEstimator()

def qaoa_cost(params):
    gamma_val, beta_val = params
    
    # Build circuit with parameters
    qc = qaoa_circuit(p=1)
    qc = qc.assign_parameters([gamma_val, beta_val])
    
    # Evaluate
    job = estimator.run([(qc, H_cost)])
    result = job.result()
    return result[0].data.evs

# Optimize
print("Running QAOA...")
initial = [0.5, 0.5]  # [γ, β]
result = minimize(qaoa_cost, initial, method='COBYLA')

print(f"Optimal energy: {result.fun:.4f}")
print(f"Optimal γ = {result.x[0]:.4f}, β = {result.x[1]:.4f}")
```

### QAOA Key Concepts (MEMORIZE!)

```python
# Cost layer: Encodes problem
qc.rzz(2*gamma, i, j)  # For each edge in graph

# Mixer layer: Explores solutions  
qc.rx(2*beta, i)  # For each qubit

# Initial state: Equal superposition
qc.h([0, 1, 2, ...])  # All qubits

# Parameters per layer:
# - One γ (gamma) for cost
# - One β (beta) for mixer
# - Total: 2p parameters for p layers
```

---

## 💡 Practical Patterns

### Pattern 1: H2 Molecule Energy

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# H2 Hamiltonian (Jordan-Wigner encoding)
H = SparsePauliOp(
    ["II", "ZI", "IZ", "ZZ", "XX"],
    [-1.05, 0.39, 0.39, -0.01, 0.18]
)

# Trial state
qc = QuantumCircuit(2)
qc.x(0)  # Hartree-Fock |10⟩
qc.ry(0.2, 1)  # Add excitation

# Calculate energy
estimator = StatevectorEstimator()
job = estimator.run([(qc, H)])
energy = job.result()[0].data.evs

print(f"Energy: {energy:.4f} Hartree")
# Expected ground state: ~-1.85 Hartree
```

### Pattern 2: GHZ State Verification

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create GHZ state: (|000⟩ + |111⟩)/√2
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# Entanglement witnesses
witnesses = [
    SparsePauliOp('XXX'),  # All X correlations
    SparsePauliOp('ZZI'),  # Pairwise Z
    SparsePauliOp('ZIZ'),
    SparsePauliOp('IZZ'),
]

estimator = StatevectorEstimator()
pubs = [(qc, w) for w in witnesses]
job = estimator.run(pubs)
result = job.result()

print("GHZ State Witnesses:")
print(f"⟨XXX⟩ = {result[0].data.evs:.3f}")  # -1.0
print(f"⟨ZZI⟩ = {result[1].data.evs:.3f}")  # 1.0
print(f"⟨ZIZ⟩ = {result[2].data.evs:.3f}")  # 1.0
print(f"⟨IZZ⟩ = {result[3].data.evs:.3f}")  # 1.0
```

### Pattern 3: Multi-Layer VQE Comparison

```python
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize
import numpy as np

# Hamiltonian
H = SparsePauliOp(['ZZ', 'XX', 'YY'], [1.0, 0.5, 0.5])

def create_ansatz(n_layers):
    """Create ansatz with n layers"""
    params = ParameterVector('θ', n_layers * 2)
    qc = QuantumCircuit(2)
    
    for i in range(n_layers):
        qc.ry(params[2*i], 0)
        qc.ry(params[2*i+1], 1)
        qc.cx(0, 1)
    
    return qc, params

estimator = StatevectorEstimator()

# Test different depths
for n_layers in [1, 2, 3, 4]:
    ansatz, params = create_ansatz(n_layers)
    
    def cost(param_values):
        qc = ansatz.assign_parameters(param_values)
        job = estimator.run([(qc, H)])
        return job.result()[0].data.evs
    
    initial = np.zeros(n_layers * 2)
    result = minimize(cost, initial, method='COBYLA', options={'maxiter': 100})
    
    print(f"Layers={n_layers}: E={result.fun:.6f}, Params={len(initial)}")
```

---
---

## 🎯 Practice Problems

### Problem 1: Bell State Correlations

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Measure correlations
observables = [SparsePauliOp(op) for op in ['ZZ', 'XX', 'YY']]
pubs = [(qc, obs) for obs in observables]

estimator = StatevectorEstimator()
job = estimator.run(pubs)
results = job.result()

for i, label in enumerate(['ZZ', 'XX', 'YY']):
    print(f"⟨{label}⟩ = {results[i].data.evs:.3f}")
# Expected: ZZ=1.0, XX=1.0, YY=-1.0
```

### Problem 2: Simple VQE

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# Hamiltonian
H = SparsePauliOp(['ZI', 'IZ', 'XX'], [1.0, 1.0, 0.5])

# Ansatz
theta = Parameter('θ')
qc = QuantumCircuit(2)
qc.ry(theta, 0)
qc.ry(theta, 1)
qc.cx(0, 1)

# VQE
estimator = StatevectorEstimator()

def cost(params):
    job = estimator.run([(qc.assign_parameters(params), H)])
    return job.result()[0].data.evs

result = minimize(cost, [0.5], method='COBYLA')
print(f"Ground energy: {result.fun:.4f}")
print(f"Optimal θ: {result.x[0]:.4f}")
```

### Problem 3: QAOA MaxCut

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize

# MaxCut Hamiltonian (2 nodes, 1 edge)
H_cost = SparsePauliOp(['ZZ'], [1.0])

gamma = Parameter('γ')
beta = Parameter('β')

qc = QuantumCircuit(2)
qc.h([0, 1])  # Initial state
qc.rzz(2*gamma, 0, 1)  # Cost layer
qc.rx(2*beta, 0)  # Mixer layer
qc.rx(2*beta, 1)

estimator = StatevectorEstimator()

def qaoa_cost(params):
    qc_bound = qc.assign_parameters(params)
    job = estimator.run([(qc_bound, H_cost)])
    return job.result()[0].data.evs

result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')
print(f"Optimal cost: {result.fun:.4f}")
print(f"γ={result.x[0]:.4f}, β={result.x[1]:.4f}")
```

---

## 📁 Files in This Section

**Section 6 - Estimator & VQE/QAOA**:
1. **`estimator_primitive.ipynb`** - Complete Estimator tutorial with multi-observable patterns
2. **`vqe_pattern.ipynb`** - VQE and QAOA implementations with scipy.optimize

---

## 🎓 Key Takeaways

```
✅ Estimator = expectation values ⟨O⟩
✅ NO measurements needed in circuit
✅ SparsePauliOp("ZZ") for observables
✅ result[0].data.evs (plural!)
✅ VQE: minimize ⟨H⟩ with scipy.optimize
✅ QAOA: rzz for cost, rx for mixer
✅ COBYLA optimizer most common
✅ H2 molecule: 5-term Hamiltonian
✅ resilience_level=1 for error mitigation
✅ 12% of exam - MASTER THIS!
```

---

## 🔗 Next Steps

1. Master SparsePauliOp construction
2. Practice VQE pattern with different Hamiltonians
3. Implement QAOA for simple graphs
4. Understand scipy.optimize integration
5. Know resilience_level options
6. Move to **Section 7 (Results)** for advanced result processing

**Estimator, VQE, and QAOA are CRITICAL for the exam!** 🚀⚡
