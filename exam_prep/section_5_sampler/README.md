# Section 5: Sampler Primitive

> **Exam Weight**: 12% (~8 questions) | **Difficulty**: Medium-High | **Must Master**: ✅✅✅

---

## 📖 Overview

**Sampler** is the NEW way (Qiskit 1.0+) to get measurement statistics from quantum circuits. It replaces deprecated methods like `execute()`, `Aer.get_backend()`, and `backend.run()`.

### What You'll Learn

| Concept | Description | Exam Focus |
|---------|-------------|------------|
| Sampler Primitive | Get measurement outcomes (counts, bitstrings) | **HIGH** |
| PUB Format | Primitive Unified Bloc syntax `[(circuit,)]` | **CRITICAL** |
| Result Extraction | `result[0].data.meas.get_counts()` chain | **HIGH** |
| Twirling Options | Error mitigation via Pauli twirling | Medium |
| Dynamical Decoupling | Error suppression for idle qubits | Medium |
| BitArray Methods | `get_counts()` vs `get_bitstrings()` | **HIGH** |

---

## 🗺️ Visual Overview: Sampler Workflow

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

## 📊 Topics Quick Reference

| Topic | Key APIs | Common Trap | Mnemonic |
|-------|----------|-------------|----------|
| Sampler Basics | `StatevectorSampler()`, `SamplerV2()` | Must have measurements | **"S = Sampling needs Measures"** |
| PUB Format | `[(circuit,)]`, `[(circuit, params, shots)]` | Missing trailing comma | **"CPS = Circuit, Params, Shots"** |
| Result Extraction | `.data.meas.get_counts()` | Wrong attribute chain | **"DrMeGC = Data.Register.Method.Get_Counts"** |
| Twirling | `enable_gates`, `enable_measure` | Different defaults Sampler vs Estimator | **"Sampler: Gates Off, Measure Off"** |
| Dynamical Decoupling | `enable`, `sequence_type` | Only helps with idle qubits | **"DD = Defend During Downtime"** |

---

## 📚 Learning Path

```
Sampler Basics ──► PUB Format ──► Result Extraction ──► Multiple Circuits
      │                                                        │
      └──────────── Twirling & DD (Error Mitigation) ──────────┘
```

---

# 📘 Topic 1: Sampler Primitive

## What are Primitives?

### 1️⃣ Definition

**Primitives** are high-level computational building blocks that provide a simplified interface for running quantum computations. Qiskit 1.0+ provides two core primitives:

- **Sampler** → Measurement outcomes (bitstrings, counts)
- **Estimator** → Expectation values (observables)

### 2️⃣ Analogy: The Loaded Die 🎲

Using a `Sampler` is like rolling a loaded die to figure out its bias:
- **Circuit**: The manufacturing process that creates the bias
- **Shots**: How many times you roll it (e.g., 1000 times)
- **Counts**: Tallying up how often each face appears
- **Outcome**: Understanding the probability distribution

Just as rolling a die many times reveals its bias, running a quantum circuit through Sampler many times reveals the probability distribution of quantum states.

### 3️⃣ Visual: Sampler vs Old Methods

```
Old Way (Deprecated):              New Way (Qiskit 1.0+):
    execute()                          Sampler
    Aer.get_backend()                  
    backend.run()   
❌ DON'T use these anymore!        ✅ Use Sampler Primitive!

Why Primitives?
✓ Hardware-agnostic (same code for simulator/hardware)
✓ Auto-transpilation
✓ Error mitigation built-in
✓ Cleaner, more Pythonic API
✓ Future-proof (IBM's long-term direction)
```

### 4️⃣ Implementation Pattern

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# 1. Create circuit WITH measurements (required!)
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # MUST add measurements for Sampler!

# 2. Create Sampler
sampler = StatevectorSampler()

# 3. Run circuit
job = sampler.run([qc], shots=1024)

# 4. Get results
result = job.result()
counts = result[0].data.meas.get_counts()

print(counts)  # {'00': 512, '11': 512}
```

### 5️⃣ Trap: Sampler REQUIRES Measurements

```python
# ❌ WRONG - No measurements!
qc = QuantumCircuit(1)
qc.h(0)
sampler.run([(qc,)])  # ERROR! No measurements

# ✅ CORRECT - Has measurements
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)  # OR use qc.measure_all()
sampler.run([(qc,)])  # Works!
```

### 6️⃣ Mnemonic: **"S = Sampling needs Measures"**

**S**ampler **S**amples → needs **M**easurements  
If circuit has no `measure()` or `measure_all()`, Sampler will fail!

### 7️⃣ Quick Check

**Q: What happens if you run Sampler on a circuit without measurements?**

<details>
<summary>Answer</summary>

The circuit will raise an error because Sampler needs measurements to sample from. Always include `qc.measure()` or `qc.measure_all()` before running with Sampler.
</details>

---

## Sampler with Real Hardware

### 1️⃣ Definition

`SamplerV2` from `qiskit_ibm_runtime` allows running circuits on real IBM Quantum hardware or cloud simulators with automatic transpilation and error mitigation.

### 2️⃣ Analogy: Cloud vs Local Calculator 🖥️☁️

- **StatevectorSampler**: Like using a calculator app on your phone (local, fast, perfect)
- **SamplerV2 with backend**: Like submitting calculations to a powerful supercomputer (real hardware, noise, but authentic quantum behavior)

### 3️⃣ Visual: Sampler Types

```
┌─────────────────────────────────────────────┐
│           Sampler Types                      │
├──────────────────┬──────────────────────────┤
│ StatevectorSampler│ SamplerV2 (Runtime)     │
├──────────────────┼──────────────────────────┤
│ Local simulation  │ Real hardware/cloud     │
│ Perfect results   │ Noisy results           │
│ Fast              │ Queue times             │
│ No account needed │ IBM Quantum account     │
│ Testing/debug     │ Production              │
└──────────────────┴──────────────────────────┘
```

### 4️⃣ Implementation Pattern

```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Connect to IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')  # or other backend

# Create Sampler with backend
sampler = Sampler(mode=backend)

# Run circuit (same as local)
job = sampler.run([(qc,)], shots=1024)
result = job.result()
counts = result[0].data.meas.get_counts()
```

### 5️⃣ Trap: `mode=` vs `backend=` Parameter

```python
# ✅ CORRECT for SamplerV2
sampler = Sampler(mode=backend)

# ⚠️ OLD SYNTAX (may still work but deprecated)
sampler = Sampler(backend=backend)
```

### 6️⃣ Mnemonic: **"Mode for Modern"**

SamplerV2 uses `mode=backend`, not `backend=backend`. Modern API = Mode parameter.

### 7️⃣ Quick Check

**Q: Which Sampler type would you use for quick local testing?**

<details>
<summary>Answer</summary>

`StatevectorSampler` - it runs locally, requires no account, and gives perfect (noiseless) results for testing.
</details>

---

# 📘 Topic 2: PUB Format (Primitive Unified Blocs)

## PUB Syntax

### 1️⃣ Definition

**PUB (Primitive Unified Bloc)** is the standardized input format for primitives in Qiskit 1.0+. Format: `(circuit, parameter_values, shots)` wrapped in a list.

### 2️⃣ Analogy: Shipping Package 📦

Think of a PUB as a shipping package:
- **List `[...]`**: The shipping container holding multiple packages
- **Tuple `(...)`**: Each individual package
- **Circuit**: The item being shipped
- **Parameters**: Special handling instructions
- **Shots**: How many copies to make

### 3️⃣ Visual: PUB Format Reference

```
PUB Format:  [(circuit, parameter_values, shots)]
              │  │       │                 │
              │  │       │                 └─ Optional: shots per circuit
              │  │       └─── Optional: list of parameter values
              │  └─────────── Required: QuantumCircuit
              └───────────── Required: list wrapper

Memory Aid: "CPS = Circuit, Params, Shots"
```

### 4️⃣ Implementation Patterns

```python
# Single circuit, no parameters
pub = [(qc,)]  # ← Note trailing comma!

# With parameter values
from qiskit.circuit import Parameter
theta = Parameter('θ')
qc_param = QuantumCircuit(1, 1)
qc_param.ry(theta, 0)
qc_param.measure(0, 0)

pub = [(qc_param, [0.5])]  # θ = 0.5

# With custom shots
pub = [(qc, None, 2048)]  # 2048 shots for this circuit

# Multiple circuits
pubs = [(qc1,), (qc2,), (qc3,)]

# Multiple parameter sets (parameter sweep)
pubs = [
    (qc_param, [0.0]),
    (qc_param, [np.pi/2]),
    (qc_param, [np.pi])
]
job = sampler.run(pubs)
```

### 5️⃣ Trap: Trailing Comma Creates Tuple

```python
# ❌ WRONG - Not a tuple!
(circuit)     # Just circuit in parentheses

# ❌ WRONG - List instead of tuple  
[circuit]     # This is a list

# ✅ CORRECT - Tuple with trailing comma
(circuit,)    # Single-element tuple

# Full example of WRONG vs RIGHT:
❌ sampler.run([circuit])      # Missing tuple!
❌ sampler.run((circuit))      # Missing comma (not a tuple!)
❌ sampler.run([(circuit)])    # Still missing comma inside!

✅ sampler.run([(circuit,)])   # Correct: Tuple in list!
```

### 6️⃣ Mnemonic: **"TiL = Tuple in List"**

- **Outer**: **L**ist `[...]` of PUBs (even if just one)
- **Inner**: **T**uple `(...)` for each PUB (with trailing comma!)
- **Order**: **CPS** = Circuit, Parameters, Shots

### 7️⃣ Quick Check

**Q: What's wrong with `sampler.run([(qc)])`?**

<details>
<summary>Answer</summary>

Missing trailing comma! `(qc)` is not a tuple, it's just `qc` in parentheses. Correct: `sampler.run([(qc,)])`
</details>

---

## Complete PUB Reference Table

| Scenario | PUB Format | Example |
|----------|------------|----------|
| Single circuit, no params | `[(circuit,)]` | `sampler.run([(qc,)])` |
| Single circuit with params | `[(circuit, params)]` | `sampler.run([(qc, [0.5, 1.2])])` |
| Multiple circuits | `[(qc1,), (qc2,)]` | `sampler.run([(qc1,), (qc2,)])` |
| Custom shots per circuit | `[(circuit, None, shots)]` | `sampler.run([(qc, None, 2048)])` |
| Everything custom | `[(circuit, params, shots)]` | `sampler.run([(qc, [0.5], 4096)])` |

---

# 📘 Topic 3: Result Extraction

## get_counts() Method

### 1️⃣ Definition

The result extraction chain `result[index].data.register_name.get_counts()` retrieves measurement counts as a dictionary from Sampler results.

### 2️⃣ Analogy: Russian Nesting Dolls 🪆

Extracting results is like opening nested Russian dolls:
1. **result**: The outer doll (contains all PUB results)
2. **result[0]**: First inner doll (first circuit's result)
3. **.data**: Next layer (measurement data container)
4. **.meas**: Next layer (the specific register - default name "meas")
5. **.get_counts()**: The treasure inside (actual count dictionary)

### 3️⃣ Visual: Result Extraction Chain

```
result[0].data.meas.get_counts()
   ↑       ↑    ↑       ↑
   │       │    │       └─ Method to call (returns dict)
   │       │    └───────── Measurement register name ("meas" is default)
   │       └───────────── Data attribute (contains BitArrays)
   └─────────────────── Index (which circuit's result)
```

### 4️⃣ Implementation Pattern

```python
# Run circuit
job = sampler.run([(qc,)], shots=1024)
result = job.result()

# Extract counts for first (or only) circuit
pub_result = result[0]
counts = pub_result.data.meas.get_counts()
# {'00': 502, '11': 522}

# For multiple circuits, use index:
# counts1 = result[0].data.meas.get_counts()
# counts2 = result[1].data.meas.get_counts()

# Access metadata
metadata = pub_result.metadata
print(f"Shots: {metadata.get('shots', 'N/A')}")
```

### 5️⃣ Trap: Register Name Must Match

```python
# If you use custom classical register name:
from qiskit import ClassicalRegister
cr = ClassicalRegister(2, 'my_result')
qc = QuantumCircuit(2)
qc.add_register(cr)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], cr)

# Then access with THAT name:
counts = result[0].data.my_result.get_counts()  # NOT .meas!

# With measure_all(), default name is "meas":
qc.measure_all()
counts = result[0].data.meas.get_counts()
```

### 6️⃣ Mnemonic: **"DrMeGC = Data.Register.Method.Get_Counts"**

**D**ata → **R**egister → **M**ethod → **G**et **C**ounts

Or remember: **"0-D-M-G"** = `[0].data.meas.get_counts()`

### 7️⃣ Quick Check

**Q: How do you access counts from the third circuit in a multi-circuit run?**

<details>
<summary>Answer</summary>

`result[2].data.meas.get_counts()` - remember indices are 0-based, so third circuit is index 2.
</details>

---

## get_counts() vs get_bitstrings()

### 1️⃣ Definition

Two methods for extracting measurement data:
- `get_counts()`: Returns dictionary with aggregated outcome counts
- `get_bitstrings()`: Returns list of individual shot outcomes

### 2️⃣ Analogy: Election Results 🗳️

- **get_counts()**: Like election results - "Candidate A: 512 votes, Candidate B: 488 votes"
- **get_bitstrings()**: Like the individual ballots - ["A", "B", "A", "A", "B", ...]

### 3️⃣ Visual: Comparison Table

| Method | Returns | Length | Use Case |
|--------|---------|--------|----------|
| `get_counts()` | `dict` | # unique outcomes | Probabilities, histograms |
| `get_bitstrings()` | `list[str]` | # shots | Individual shots, correlations |

### 4️⃣ Implementation Pattern

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Bell state circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
result = job.result()
bit_array = result[0].data.meas

# Method 1: get_counts() - aggregated
counts = bit_array.get_counts()
print(f"Counts: {counts}")  # {'00': 512, '11': 488}

# Method 2: get_bitstrings() - raw shots
bitstrings = bit_array.get_bitstrings()
print(f"First 10 shots: {bitstrings[:10]}")  # ['00', '11', '11', '00', ...]
print(f"Total shots: {len(bitstrings)}")     # 1000

# Post-selection: count shots where qubit 0 was |1⟩
# Note: LSB ordering - rightmost bit is qubit 0
q0_is_1 = sum(1 for bs in bitstrings if bs[-1] == '1')
print(f"Shots where q0=1: {q0_is_1}")
```

### 5️⃣ Trap: Bit Ordering (LSB)

```python
# Qiskit uses LSB (Least Significant Bit) ordering
# Rightmost bit = qubit 0, leftmost bit = highest qubit

# For bitstring '01':
# '01' means qubit 1 = 0, qubit 0 = 1
#  ↑↑
#  │└─ qubit 0
#  └── qubit 1

# To check qubit 0 in bitstring:
bitstring = '01'
qubit_0 = bitstring[-1]  # '1' (rightmost)
qubit_1 = bitstring[-2]  # '0' (second from right)
```

### 6️⃣ Mnemonic: **"Counts for Counting, Bits for Browsing"**

- **get_counts()**: When you just want totals (histogram)
- **get_bitstrings()**: When you need to browse individual shots (analysis)

### 7️⃣ Quick Check

**Q: Which method returns a list with length equal to the number of shots?**

<details>
<summary>Answer</summary>

`get_bitstrings()` - it returns one string per shot, so length equals number of shots.
</details>

---

# 📘 Topic 4: Twirling Options

## Pauli Twirling

### 1️⃣ Definition

**Pauli twirling** is an error mitigation technique that converts coherent noise (systematic, correlated errors) into Pauli noise (stochastic, uncorrelated errors) by randomly applying Pauli gates around two-qubit gates.

### 2️⃣ Analogy: Noise Scrambler 📻

Imagine you're listening to a radio with interference:
- **Coherent noise**: A steady hum that gets louder over time (compounds)
- **Pauli twirling**: Randomly changing the interference pattern each time you listen
- **Result**: The hum becomes random static that averages out over many listens

### 3️⃣ Math: Why Twirling Helps

The key insight: Two-qubit gates like CNOT are invariant under certain Pauli operations:

$$P_2 \cdot \text{CNOT} \cdot P_1 = \text{CNOT}$$

| Error Type | Without Twirling | With Twirling |
|------------|------------------|---------------|
| Coherent (systematic) | Adds up coherently | Converted to stochastic |
| Error accumulation | ~O(n²) with depth | ~O(n) with depth |
| Mitigation difficulty | Hard to correct | Easier to model & correct |

### 4️⃣ Implementation Pattern

```python
from qiskit_ibm_runtime import SamplerV2 as Sampler

sampler = Sampler(mode=backend)

# Gate twirling (twirl 2-qubit gates)
sampler.options.twirling.enable_gates = True
sampler.options.twirling.enable_measure = False  # Default for Sampler

# Randomization settings
sampler.options.twirling.num_randomizations = 32
sampler.options.twirling.shots_per_randomization = 100
# Total shots = num_randomizations × shots_per_randomization

# Strategy (which qubits to twirl)
sampler.options.twirling.strategy = "active-accum"
```

### 5️⃣ Trap: Sampler vs Estimator Twirling Defaults

| Option | Sampler Default | Estimator Default |
|--------|-----------------|-------------------|
| `enable_gates` | `False` | `False` |
| `enable_measure` | `False` ⚠️ | `True` ⚠️ |
| `strategy` | `"active-accum"` | `"active-accum"` |

**EXAM TRAP**: `enable_measure` defaults are DIFFERENT between Sampler and Estimator!

### 6️⃣ Mnemonic: **"Sampler: Gates Off, Measure Off (GOMO)"**

Sampler defaults: **G**ates **O**ff, **M**easure **O**ff  
Estimator defaults: Gates Off, **Measure ON**

### 7️⃣ Quick Check

**Q: What is the default value of `enable_measure` for Sampler twirling?**

<details>
<summary>Answer</summary>

`False` - Sampler defaults to measure twirling OFF, while Estimator defaults to measure twirling ON.
</details>

---

## Twirling Strategies

| Strategy | Description | Use Case |
|----------|-------------|----------|
| `"active"` | Only qubits with gates in current layer | Minimal overhead |
| `"active-accum"` | All qubits used up to current layer | **Default**, balanced |
| `"active-circuit"` | All qubits used anywhere in circuit | More thorough |
| `"all"` | ALL qubits in circuit | Maximum twirling |

---

# 📘 Topic 5: Dynamical Decoupling

## DD for Sampler

### 1️⃣ Definition

**Dynamical decoupling (DD)** is an error suppression technique that inserts pulse sequences on idle qubits to cancel out coherent errors from unwanted interactions with the environment.

### 2️⃣ Analogy: Stretching During Breaks 🧘

When a qubit is idle, errors accumulate like stiffness when sitting too long:
- **Idle qubit**: Like sitting at a desk (errors accumulate)
- **DD pulses**: Like stretching breaks (reset and refresh)
- **Result**: Qubit stays "healthier" through long circuits

### 3️⃣ Visual: DD Sequences

```
Without DD:           With DD:
    ─────────────        ─[X]──[X]──
    (qubit idles,        (pulses cancel errors,
     errors accumulate)   net effect = identity)

DD Sequences:
• "XX"   = X - X        (simple, default)
• "XpXm" = X+ - X-      (robust to pulse errors)
• "XY4"  = X - Y - X - Y (superior suppression)
```

### 4️⃣ Implementation Pattern

```python
from qiskit_ibm_runtime import SamplerV2 as Sampler

sampler = Sampler(mode=backend)

# Enable dynamical decoupling
sampler.options.dynamical_decoupling.enable = True

# Choose sequence type
sampler.options.dynamical_decoupling.sequence_type = "XX"  # Default
# Options: "XX", "XpXm", "XY4"

# How to distribute pulses in idle periods
sampler.options.dynamical_decoupling.extra_slack_distribution = "middle"
# Options: "middle", "edges"

# Scheduling method (when to insert DD)
sampler.options.dynamical_decoupling.scheduling_method = "alap"
# Options: "alap" (As Late As Possible), "asap"
```

### 5️⃣ Trap: DD Only Helps with Idle Qubits

```python
# ✅ DD helps here - qubit 0 is idle during cx(1,2)
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.barrier()  # Qubit 0 idles while 1,2 are operated
qc.cx(1, 2)   # DD pulses inserted on qubit 0
qc.barrier()
qc.cx(0, 1)
qc.measure_all()

# ⚠️ DD doesn't help much - no idle periods
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.h(1)
qc.cx(0, 1)  # No gaps - DD has minimal effect
qc.measure_all()
```

### 6️⃣ Mnemonic: **"DD = Defend During Downtime"**

**D**ynamical **D**ecoupling = **D**efend qubits **D**uring **D**owntime (idle periods)

### 7️⃣ Quick Check

**Q: What sequence type provides the best error suppression for DD?**

<details>
<summary>Answer</summary>

`"XY4"` - the X-Y-X-Y sequence provides superior error suppression compared to "XX" or "XpXm".
</details>

---

# 📘 Topic 6: Sampler vs Estimator Comparison

### 1️⃣ Definition

| Aspect | Sampler | Estimator |
|--------|---------|-----------|
| **Purpose** | Measurement outcomes | Expectation values |
| **Returns** | Counts, bitstrings | ⟨ψ\|O\|ψ⟩ values |
| **Requires** | Measurements in circuit | Observable (no measurements!) |

### 2️⃣ Visual: When to Use Which

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

┌────────────────────────────────────────────┐
│         Use Estimator When:                 │
├────────────────────────────────────────────┤
│ • You need expectation values              │
│ • VQE/QAOA energy calculations             │
│ • Observable-based metrics                 │
│ • Quantum chemistry applications           │
└────────────────────────────────────────────┘

EXAM TIP:
- Counts/Probabilities → Sampler (Section 5)
- Expectation values → Estimator (Section 6)
```

### 3️⃣ PUB Format Comparison

| Aspect | Sampler PUB | Estimator PUB |
|--------|-------------|---------------|
| **Format** | `(circuit, params, shots)` | `(circuit, observable, params, precision)` |
| **Required** | circuit | circuit, observable |
| **Measurements** | REQUIRED ✓ | NOT ALLOWED ✗ |
| **Observable** | N/A | SparsePauliOp |

```python
# SAMPLER: (circuit, parameter_values, shots)
sampler.run([(qc_with_meas, [0.5], 2048)])

# ESTIMATOR: (circuit, observable, parameter_values, precision)
estimator.run([(qc_no_meas, SparsePauliOp('ZZ'), [0.5], 0.01)])
```

### 4️⃣ Mnemonic: **"Sampler Samples, Estimator Expects"**

- **S**ampler → **S**amples measurement outcomes
- **E**stimator → **E**xpectation values (⟨O⟩)

---

# 📘 Topic 7: Practical Patterns

## Pattern 1: Circuit Debugging with Sampler

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

## Pattern 2: Multi-Circuit Comparison

```python
# Create variations
circuits = []
for n_layers in [1, 2, 3, 4]:
    qc = QuantumCircuit(3, 3)
    for _ in range(n_layers):
        qc.h([0, 1, 2])
        qc.cx(0, 1)
        qc.cx(1, 2)
    qc.measure([0,1,2], [0,1,2])
    circuits.append((qc,))  # Note: tuple format!

# Run all at once
sampler = StatevectorSampler()
job = sampler.run(circuits, shots=1024)
results = job.result()

# Analyze each
for i, pub_result in enumerate(results):
    counts = pub_result.data.meas.get_counts()
    print(f"Layers {i+1}: {counts}")
```

## Pattern 3: Probability Distribution Analysis

```python
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

## Pattern 4: Parameterized Circuit Sweep

```python
from qiskit.circuit import Parameter
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

# 🚨 Master Trap List

| # | Trap | Wrong | Correct | Mnemonic |
|---|------|-------|---------|----------|
| 1 | Missing measurements | `qc = QuantumCircuit(1); sampler.run([(qc,)])` | `qc.measure_all(); sampler.run([(qc,)])` | **S needs M** |
| 2 | Missing trailing comma | `sampler.run([(qc)])` | `sampler.run([(qc,)])` | **TiL** |
| 3 | Parentheses vs tuple | `(circuit)` | `(circuit,)` | **Comma creates tuple** |
| 4 | Wrong result chain | `result.counts` | `result[0].data.meas.get_counts()` | **DrMeGC** |
| 5 | Wrong register name | `.data.meas` for custom register | `.data.your_register_name` | **Match the name** |
| 6 | Sampler twirling defaults | Assuming measure=True | Sampler: measure=False | **GOMO** |
| 7 | DD without idle qubits | Expecting DD to always help | DD only helps with gaps | **DD = Downtime Defense** |
| 8 | Bit ordering | Leftmost = qubit 0 | Rightmost = qubit 0 (LSB) | **LSB = Last is Start Bit** |

---

# 📝 Practice Exam Questions

### Question 1: PUB Format
What is the correct way to run a single circuit with Sampler?

A) `sampler.run(qc)`  
B) `sampler.run([qc])`  
C) `sampler.run((qc))`  
D) `sampler.run([(qc,)])`

<details>
<summary>Answer</summary>

**D) `sampler.run([(qc,)])`**

PUBs must be tuples in a list. The trailing comma creates a single-element tuple.
</details>

---

### Question 2: Result Extraction
How do you extract counts from the second circuit in a multi-circuit Sampler run?

A) `result.data.meas.get_counts(1)`  
B) `result[1].data.meas.get_counts()`  
C) `result.get_counts(1)`  
D) `result[2].data.meas.get_counts()`

<details>
<summary>Answer</summary>

**B) `result[1].data.meas.get_counts()`**

Use 0-based indexing, so second circuit is index 1. Then chain `.data.meas.get_counts()`.
</details>

---

### Question 3: Measurement Requirement
Which statement about Sampler is TRUE?

A) Sampler automatically adds measurements if missing  
B) Sampler requires circuits to have measurements  
C) Sampler works with or without measurements  
D) Sampler removes measurements before execution

<details>
<summary>Answer</summary>

**B) Sampler requires circuits to have measurements**

Unlike Estimator (which requires NO measurements), Sampler requires measurements to sample from.
</details>

---

### Question 4: Twirling Defaults
What is the default value of `enable_measure` for Sampler twirling?

A) True  
B) False  
C) None  
D) "auto"

<details>
<summary>Answer</summary>

**B) False**

Sampler defaults to `enable_measure=False`, while Estimator defaults to `enable_measure=True`.
</details>

---

### Question 5: BitArray Methods
Which method returns individual shot outcomes as a list?

A) `get_counts()`  
B) `get_probabilities()`  
C) `get_bitstrings()`  
D) `get_shots()`

<details>
<summary>Answer</summary>

**C) `get_bitstrings()`**

`get_bitstrings()` returns a list of individual bitstring outcomes, one per shot.
</details>

---

### Question 6: Sampler vs Estimator
Which primitive requires measurements in the circuit?

A) Estimator only  
B) Sampler only  
C) Both Sampler and Estimator  
D) Neither

<details>
<summary>Answer</summary>

**B) Sampler only**

Sampler REQUIRES measurements to sample from. Estimator requires NO measurements (it uses observables instead).
</details>

---

### Question 7: Dynamical Decoupling
When does dynamical decoupling provide the most benefit?

A) In circuits with no barriers  
B) In circuits with idle qubits  
C) In circuits with only single-qubit gates  
D) In very short circuits

<details>
<summary>Answer</summary>

**B) In circuits with idle qubits**

DD inserts pulses during idle periods to suppress errors. No idle time = minimal DD benefit.
</details>

---

### Part B: Code Analysis (3-5 minutes each)

**Q8**: What's wrong with this code?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# No measurements!

sampler = StatevectorSampler()
job = sampler.run([(qc,)])
result = job.result()
counts = result[0].data.meas.get_counts()
```

<details>
<summary>Answer</summary>

**Problem**: Circuit has no measurements! Sampler requires measurements to sample from.

**Fix**: Add `qc.measure_all()` or explicit measurements:
```python
qc = QuantumCircuit(2, 2)  # Add classical bits
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # Add measurements
```

**Mnemonic**: "S needs M" = Sampler needs Measurements
</details>

---

**Q9**: What does this code print?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.x(0)  # |1⟩ state
qc.measure(0, 0)

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=100)
result = job.result()
counts = result[0].data.meas.get_counts()

print(len(counts))
print(list(counts.keys())[0])
```

<details>
<summary>Answer</summary>

**Output**:
```
1
1
```

**Explanation**:
1. X gate puts qubit in |1⟩ state
2. All 100 shots measure '1'
3. `len(counts)` = 1 (only one unique outcome)
4. The only key is '1'
</details>

---

**Q10**: Fix the PUB format errors in this code:
```python
sampler = StatevectorSampler()

# Attempt 1
job1 = sampler.run([qc])

# Attempt 2  
job2 = sampler.run([(qc)])

# Attempt 3
job3 = sampler.run((qc,))
```

<details>
<summary>Answer</summary>

**All three are wrong!**

1. `[qc]` - Missing tuple! Should be `[(qc,)]`
2. `[(qc)]` - Missing trailing comma! `(qc)` is not a tuple
3. `(qc,)` - Missing list wrapper! PUBs must be in a list

**Correct**:
```python
job = sampler.run([(qc,)])
```

**Mnemonic**: "TiL" = Tuple in List
</details>

---

**Q11**: What does this code output?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
result = job.result()

bitstrings = result[0].data.meas.get_bitstrings()
counts = result[0].data.meas.get_counts()

print(len(bitstrings))
print(len(counts))
```

<details>
<summary>Answer</summary>

**Output**:
```
1000
2
```

**Explanation**:
1. `get_bitstrings()` returns one string per shot → length = 1000
2. `get_counts()` returns unique outcomes → Bell state has 2: '00' and '11'

**Key insight**: `len(bitstrings)` = shots, `len(counts)` = unique outcomes
</details>

---

**Q12**: What's the problem with this result extraction?
```python
result = job.result()

# These all fail - why?
counts1 = result.data.meas.get_counts()
counts2 = result[0].meas.get_counts()
counts3 = result[0].data.get_counts()
```

<details>
<summary>Answer</summary>

**All three are wrong - each missing part of the chain!**

1. `result.data.meas.get_counts()` - Missing `[0]` index
2. `result[0].meas.get_counts()` - Missing `.data`
3. `result[0].data.get_counts()` - Missing `.meas`

**Correct chain**:
```python
counts = result[0].data.meas.get_counts()
```

**Mnemonic**: "0-D-M-G" = `[0].data.meas.get_counts()`
</details>

---

### Part C: Scenario-Based (5-7 minutes each)

**Q13**: You need to run 3 different circuits and compare their output distributions. Write complete code to create a Bell state, GHZ state, and W state circuit, run them all together, and print counts for each.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Circuit 1: Bell state (2 qubits)
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
bell.measure_all()

# Circuit 2: GHZ state (3 qubits)
ghz = QuantumCircuit(3)
ghz.h(0)
ghz.cx(0, 1)
ghz.cx(0, 2)
ghz.measure_all()

# Circuit 3: W state approximation (3 qubits)
w = QuantumCircuit(3)
w.ry(1.9106, 0)  # arccos(1/sqrt(3))
w.ch(0, 1)
w.cx(1, 2)
w.measure_all()

# Run all together as PUBs
sampler = StatevectorSampler()
pubs = [(bell,), (ghz,), (w,)]  # Note: tuple format!
job = sampler.run(pubs, shots=1024)
result = job.result()

# Print counts for each
names = ['Bell', 'GHZ', 'W']
for i, name in enumerate(names):
    counts = result[i].data.meas.get_counts()
    print(f"{name}: {counts}")
```

**Expected output**:
- Bell: `{'00': ~512, '11': ~512}`
- GHZ: `{'000': ~512, '111': ~512}`
- W: Approximately equal `{'001': ~341, '010': ~341, '100': ~341}`
</details>

---

**Q14**: Write code to perform a parameter sweep on a single-qubit rotation, measuring P(|1⟩) for θ = 0, π/4, π/2, 3π/4, π.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
import numpy as np

# Create parameterized circuit
theta = Parameter('θ')
qc = QuantumCircuit(1, 1)
qc.ry(theta, 0)  # Rotation around Y axis
qc.measure(0, 0)

# Define sweep values
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]

# Create PUBs with different parameter values
pubs = [(qc, [angle]) for angle in angles]

# Run all at once
sampler = StatevectorSampler()
job = sampler.run(pubs, shots=1024)
result = job.result()

# Extract and print P(|1⟩) for each angle
print("Parameter Sweep Results:")
print("θ (rad)   | P(|1⟩)")
print("-" * 20)
for i, angle in enumerate(angles):
    counts = result[i].data.meas.get_counts()
    prob_1 = counts.get('1', 0) / 1024
    print(f"{angle:.4f}   | {prob_1:.3f}")

# Expected: 0→0, π/4→0.146, π/2→0.5, 3π/4→0.854, π→1.0
```

**Key insight**: RY(θ) gives P(|1⟩) = sin²(θ/2)
</details>

---

**Q15**: You're debugging a circuit and need to check if measurements match the expected distribution. Write a function that takes Sampler results and returns True if the distribution matches expected within tolerance.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

def verify_distribution(result, expected_probs, tolerance=0.05):
    """
    Verify that measurement results match expected probabilities.
    
    Args:
        result: PrimitiveResult from Sampler
        expected_probs: dict like {'00': 0.5, '11': 0.5}
        tolerance: allowed deviation (default 5%)
    
    Returns:
        bool: True if all probabilities within tolerance
    """
    counts = result[0].data.meas.get_counts()
    total_shots = sum(counts.values())
    
    # Convert counts to probabilities
    actual_probs = {state: count/total_shots for state, count in counts.items()}
    
    # Check each expected state
    for state, expected in expected_probs.items():
        actual = actual_probs.get(state, 0)
        if abs(actual - expected) > tolerance:
            print(f"Mismatch for |{state}⟩: expected {expected:.3f}, got {actual:.3f}")
            return False
    
    # Check for unexpected states
    for state in actual_probs:
        if state not in expected_probs and actual_probs[state] > tolerance:
            print(f"Unexpected state |{state}⟩ with prob {actual_probs[state]:.3f}")
            return False
    
    return True

# Example usage
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
result = job.result()

# Verify Bell state distribution
expected = {'00': 0.5, '11': 0.5}
is_valid = verify_distribution(result, expected)
print(f"Distribution valid: {is_valid}")
```

**Topics combined**: Result extraction, probability analysis, testing/debugging
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
- 90-100%: Ready for Section 5 exam questions
- 75-89%: Review PUB format and result extraction chain
- Below 75%: Re-study Sampler basics

---

# ✅ Pre-Flight Checklist

Before running Sampler, verify:

```
□ Circuit has measure() or measure_all()?
□ Using tuple format: [(circuit,)]?
□ Trailing comma present: (circuit,) not (circuit)?
□ Accessing results: result[0].data.meas.get_counts()?
□ Handling multiple circuits: result[i] for each?
□ Correct register name if using custom classical register?
□ Shots parameter: Default varies by implementation?
```

---

## ✅ Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS:
□ Primitives replace execute()/backend.run() in Qiskit 1.0+
□ Sampler returns counts/bitstrings, Estimator returns expectation values
□ Sampler REQUIRES measurements in circuit ("S needs M")
□ PUB format: [(circuit, params, shots)] - Primitive Unified Bloc
□ Result extraction chain: result[0].data.meas.get_counts()
□ get_counts() returns string keys, get_bitstrings() returns list of strings
□ Twirling defaults differ: Sampler (gates=False, measure=False), Estimator (gates=True, measure=True)
□ Dynamical Decoupling helps only with idle qubits during execution
□ Qiskit uses LSB bit ordering: rightmost = qubit 0 (little-endian)
□ StatevectorSampler for ideal simulation, SamplerV2 for hardware/noisy simulation
□ Multiple circuits in single run: [(qc1,), (qc2,), (qc3,)]
□ Each PUB in result accessed by index: result[i].data.meas

CONSTRAINTS & LIMITATIONS:
□ Sampler will ERROR if no measurements in circuit (not just return empty)
□ Maximum 300 circuits per job submission in runtime (exceeding causes error)
□ shots parameter must be positive integer (0 or negative causes ValueError)
□ Parameter binding must match circuit's num_parameters exactly
□ Classical register names must be unique within circuit (duplicate names error)
□ PUB tuple must have circuit first; other positions are positional
□ Cannot modify circuit after measurement gate has been added
□ BitArray slicing uses measurement register order, not qubit order
□ Sampler ignores observables if provided (they're for Estimator only)
□ Default shots=1024 if not specified (differs from old backend.run default 4096)
□ Session expires after 5 minutes idle (jobs fail if session closed)
□ Each PUB runs independently - no shared quantum state between PUBs

KEY DEFINITIONS:
□ PUB (Primitive Unified Bloc): Tuple format (circuit, parameters, shots) for unified API
□ DataBin: Container object holding measurement results per classical register
□ BitArray: 2D array structure [shots × num_bits] storing measurement outcomes
□ PrimitiveResult: Top-level result container holding list of PubResult objects
□ PubResult: Individual result for one PUB containing metadata and DataBin
□ Twirling: Randomized compilation technique converting coherent noise to stochastic
□ Dynamical Decoupling: Pulse sequences on idle qubits to reduce decoherence
□ LSB ordering: Least Significant Bit first (rightmost bit = qubit 0)
□ Shots: Number of circuit repetitions (samples) to estimate probability distribution
□ Classical register: Named bit collection for storing measurement outcomes
□ Measurement basis: Computational basis {|0⟩, |1⟩} unless rotated before measure

ARCHITECTURE & WORKFLOW:
□ Sampler uses V2 interface: run() returns Job, result() returns PrimitiveResult
□ StatevectorSampler simulates ideal quantum computer (no noise)
□ SamplerV2 connects to IBM Quantum hardware or noisy simulators
□ Runtime primitives batch-optimize multiple circuits for efficiency
□ Primitive options persist across multiple run() calls on same instance
□ Job queuing: jobs wait in QUEUED state until resources available
□ Results persist in cloud for 7 days after completion (then deleted)
□ Primitive sessions allow priority access and reduced queue times

VERSION-SPECIFIC:
□ V1 primitives deprecated: use V2 (SamplerV2, not Sampler)
□ Old execute() removed in Qiskit 1.0 - use primitives exclusively
□ backend.run() still exists but discouraged for new code
□ qiskit-ibm-runtime separate package required for hardware access
□ StatevectorSampler in qiskit.primitives (local), SamplerV2 in qiskit_ibm_runtime
```

### 💻 Code Pattern Checklist
```
ESSENTIAL IMPORTS:
□ from qiskit.primitives import StatevectorSampler  # ideal/local simulation
□ from qiskit_ibm_runtime import SamplerV2  # hardware/runtime
□ from qiskit_ibm_runtime import QiskitRuntimeService  # backend access
□ from qiskit import QuantumCircuit  # circuit creation
□ from qiskit.circuit import Parameter  # parameterized circuits
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager  # optimization

SAMPLER INITIALIZATION:
□ sampler = StatevectorSampler()  # no arguments, local ideal sim
□ service = QiskitRuntimeService(); backend = service.backend("ibm_brisbane")
□ sampler = SamplerV2(mode=backend)  # runtime with specific backend
□ sampler = SamplerV2(mode=backend, options=options_dict)  # with options
□ sampler = StatevectorSampler(default_shots=2048)  # custom default shots
□ sampler = StatevectorSampler(seed=42)  # reproducible random sampling

CIRCUIT PREPARATION (CRITICAL):
□ qc.measure_all()  # add measurements to all qubits (REQUIRED!)
□ qc.measure(qubit, clbit)  # selective measurement
□ qc.measure(qreg, creg)  # measure entire registers
□ from qiskit.circuit import ClassicalRegister; cr = ClassicalRegister(3, 'output')
□ qc.add_register(cr); qc.measure([0,1,2], cr)  # custom register
□ qc.barrier()  # optional: separate quantum ops from measurements visually

BASIC RUN PATTERNS:
□ job = sampler.run([(qc,)], shots=1024)  # single circuit (trailing comma!)
□ job = sampler.run([(qc,)])  # uses default shots (1024)
□ result = job.result()  # blocking call, waits for completion
□ counts = result[0].data.meas.get_counts()  # extract counts dict
□ bitstrings = result[0].data.meas.get_bitstrings()  # extract list

PARAMETERIZED CIRCUITS:
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.rx(theta, 0); qc.ry(phi, 1)  # add parameterized gates
□ job = sampler.run([(qc, [0.5, 1.2])])  # bind [θ=0.5, φ=1.2]
□ job = sampler.run([(qc, [0.5, 1.2], 2048)])  # with custom shots
□ job = sampler.run([(qc, None, 2048)])  # no params, custom shots (None placeholder)
□ param_values = [[0, 0], [0, π/2], [π/2, 0], [π/2, π/2]]
□ jobs = [sampler.run([(qc, vals)]) for vals in param_values]  # sweep parameters

MULTIPLE CIRCUITS:
□ job = sampler.run([(qc1,), (qc2,), (qc3,)])  # batch submission
□ result[0].data.meas.get_counts()  # qc1 results
□ result[1].data.meas.get_counts()  # qc2 results
□ result[2].data.meas.get_counts()  # qc3 results
□ for i, pub_result in enumerate(result):  # iterate all
□     counts = pub_result.data.meas.get_counts()
□ all_counts = [r.data.meas.get_counts() for r in result]  # list comprehension

RESULT EXTRACTION (FULL CHAIN):
□ result = job.result()  # PrimitiveResult object
□ pub_result = result[0]  # PubResult for first PUB
□ data_bin = pub_result.data  # DataBin container
□ bit_array = data_bin.meas  # BitArray for "meas" register
□ counts = bit_array.get_counts()  # dict: {'00': 512, '11': 512}
□ bitstrings = bit_array.get_bitstrings()  # list: ['00', '11', '00', ...]
□ int_counts = bit_array.get_int_counts()  # dict with int keys: {0: 512, 3: 512}
□ metadata = pub_result.metadata  # access metadata (shots, etc.)

CUSTOM REGISTER NAMES:
□ cr = ClassicalRegister(2, 'output'); qc.add_register(cr)
□ qc.measure([0,1], cr)
□ counts = result[0].data.output.get_counts()  # use 'output' not 'meas'
□ bitstrings = result[0].data.output.get_bitstrings()
□ register_name = qc.cregs[0].name  # programmatically get name

OPTIONS CONFIGURATION:
□ options = sampler.options  # get current options
□ options.default_shots = 4096  # change default shots
□ sampler.options.default_shots = 2048  # direct assignment
□ options.twirling.enable_gates = True  # enable gate twirling
□ options.twirling.enable_measure = True  # enable measurement twirling
□ options.twirling.num_randomizations = 32  # set twirling rounds
□ options.dynamical_decoupling.enable = True  # enable DD
□ options.dynamical_decoupling.sequence_type = 'XY4'  # DD sequence
□ options.dynamical_decoupling.extra_slack_distribution = 'middle'
□ options.optimization_level = 3  # transpiler optimization (0-3)
□ options.resilience_level = 1  # error mitigation level (0-2)

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
□ assert qc.num_clbits > 0, "Circuit missing measurements!"
□ if not any(isinstance(inst.operation, Measure) for inst in qc.data):
□     raise ValueError("Sampler requires measurements")

TRANSPILATION PATTERNS:
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
□ qc_transpiled = pm.run(qc)  # transpile before sampling
□ isa_circuit = qc.transpile(backend=backend)  # alternative
□ job = sampler.run([(qc_transpiled,)])  # run pre-transpiled circuit
```

### ⚠️ Exam Trap Checklist
```
MEASUREMENT TRAPS:
□ TRAP: Forgetting measurements in circuit
  → Sampler REQUIRES measure() or measure_all() - will ERROR not warn
□ TRAP: Adding measurements after calling sampler.run()
  → Must add measurements BEFORE creating PUB tuple
□ TRAP: Using Estimator patterns with Sampler
  → Sampler needs measurements, Estimator forbids them
□ TRAP: Forgetting measure_all() returns None
  → qc.measure_all() modifies in-place, don't assign: qc = qc.measure_all() ❌
□ TRAP: Measuring after barrier thinking it's optional
  → barrier() is visual only, measure() is functional requirement

TUPLE/PUB FORMAT TRAPS:
□ TRAP: sampler.run([qc]) missing tuple wrapping
  → Use: sampler.run([(qc,)]) - PUB must be tuple inside list
□ TRAP: sampler.run([(qc)]) missing trailing comma
  → (qc) is NOT a tuple, use (qc,) with comma to make single-element tuple
□ TRAP: sampler.run((qc,)) missing outer list
  → PUBs must be in list: [(qc,)] not (qc,)
□ TRAP: Forgetting trailing comma in single-circuit PUB
  → [(qc)] is a list with qc, [(qc,)] is a list with tuple containing qc
□ TRAP: Using dict instead of tuple for PUB
  → Cannot use {'circuit': qc, 'shots': 1024}, must use (qc, None, 1024)
□ TRAP: Wrong PUB tuple order
  → Order is (circuit, params, shots) - cannot swap positions

RESULT EXTRACTION TRAPS:
□ TRAP: result.data.meas.get_counts() missing [0] index
  → Use: result[0].data.meas.get_counts() - result is list-like
□ TRAP: result[0].meas.get_counts() missing .data
  → Chain is result[0].data.meas, not result[0].meas
□ TRAP: result[0].data.get_counts() missing register name
  → Must specify register: .data.meas or .data.custom_name
□ TRAP: Assuming register name is always "meas"
  → Check circuit: custom registers have custom names (use qc.cregs[0].name)
□ TRAP: Using result.job_id() instead of job.job_id()
  → job_id() is method on Job object, not PrimitiveResult
□ TRAP: Accessing result[i] when only ran i circuits
  → result[3] fails if only 3 circuits (indices 0,1,2); check len(result)
□ TRAP: Not checking if register exists before accessing
  → hasattr(result[0].data, 'meas') or inspect dir(result[0].data)

PARAMETER BINDING TRAPS:
□ TRAP: Wrong number of parameter values
  → If circuit has 2 params, must provide exactly 2 values, not 1 or 3
□ TRAP: Parameter order confusion
  → Values bind in order parameters were created: [θ, φ] not [φ, θ]
□ TRAP: Using None for parameters when circuit has parameters
  → None means "no parameters", use [0, 0] or actual values
□ TRAP: Forgetting to unbind parameters before second run
  → Parameters persist; either use new values or explicitly reset
□ TRAP: Mixing parameter objects and values
  → Pass values [0.5, 1.2], not [Parameter('θ'), 0.5]

SHOTS & COUNTS TRAPS:
□ TRAP: Using get_counts() expecting integers
  → get_counts() returns string keys: {'00': 512}, use get_int_counts() for {0: 512}
□ TRAP: Setting shots=0 or negative
  → shots must be positive integer; 0 raises ValueError
□ TRAP: Assuming shots are per circuit in batch
  → shots apply to each PUB independently, not total across all PUBs
□ TRAP: Expecting exact shot counts
  → sum(counts.values()) equals requested shots, not approximate
□ TRAP: Dividing counts by wrong shot number
  → Use metadata: result[0].metadata['shots'] to get actual value

OPTIONS & CONFIGURATION TRAPS:
□ TRAP: Confusing Sampler/Estimator twirling defaults
  → Sampler: gates=False, measure=False (both off)
  → Estimator: gates=True, measure=True (both on)
□ TRAP: Setting options after run() expecting them to apply
  → Options set after job submission don't affect that job
□ TRAP: Modifying options object without reassigning
  → Some operations require: sampler.options = options after modification
□ TRAP: Using optimization_level > 3 or < 0
  → Valid range is 0-3; other values raise ValueError
□ TRAP: Expecting DD to help without idle time
  → DD only helps qubits waiting during execution; no effect on busy qubits
□ TRAP: Enabling DD on circuits without multi-qubit gates
  → DD inserts pulses during idle times; single-qubit circuits have minimal benefit

BIT ORDERING TRAPS:
□ TRAP: Confusing bit ordering: leftmost ≠ qubit 0
  → Qiskit uses LSB: rightmost = q[0] (little-endian)
□ TRAP: Reading '01' as "qubit 0 is 0, qubit 1 is 1"
  → '01' means q[0]=1, q[1]=0 (read right-to-left)
□ TRAP: Assuming MSB ordering from other quantum frameworks
  → Many frameworks use MSB (leftmost=q[0]); Qiskit is opposite
□ TRAP: Converting binary string to int wrong direction
  → int('01', 2) gives 1 in MSB; for LSB must reverse: int('01'[::-1], 2)
□ TRAP: Matching bitstring to statevector index incorrectly
  → '01' in LSB corresponds to statevector[2], not statevector[1]

TYPE & METHOD TRAPS:
□ TRAP: Using .result() multiple times expecting cached result
  → Each result() call may re-fetch; store in variable: res = job.result()
□ TRAP: Calling get_counts() on PrimitiveResult instead of BitArray
  → get_counts() is on result[0].data.meas, not on result
□ TRAP: Using get_memory() (old Qiskit method)
  → Use get_bitstrings() instead; get_memory() doesn't exist in V2
□ TRAP: Expecting get_bitstrings() to return counts dict
  → Returns list of strings; use get_counts() for dict
□ TRAP: Trying to access individual shot outcomes from counts
  → counts only has aggregated data; use get_bitstrings() for individual shots

IMPORT & VERSION TRAPS:
□ TRAP: from qiskit.primitives import Sampler (V1, deprecated)
  → Use: from qiskit.primitives import StatevectorSampler (V2)
□ TRAP: from qiskit_ibm_runtime import Sampler
  → Use: from qiskit_ibm_runtime import SamplerV2 (explicit V2)
□ TRAP: Mixing qiskit.primitives and qiskit_ibm_runtime imports
  → Local sim: qiskit.primitives.StatevectorSampler
  → Hardware: qiskit_ibm_runtime.SamplerV2
□ TRAP: Using execute() thinking it works with primitives
  → execute() removed in 1.0+; only use sampler.run()
□ TRAP: Expecting backend.run() interface
  → Sampler.run() uses PUB format, not (circuit, shots=X) like backend.run()

COMMON MISTAKES:
□ TRAP: Running circuit without transpilation on hardware
  → Runtime auto-transpiles but exam may test explicit transpilation
□ TRAP: Forgetting session context for batch jobs
  → Use with Session(backend=backend) as session: for priority access
□ TRAP: Not handling job failures gracefully
  → Always wrap job.result() in try/except; jobs can fail mid-run
□ TRAP: Assuming immediate result availability
  → Hardware jobs queue; check job.status() before result()
□ TRAP: Using same circuit object for multiple PUBs thinking they're independent
  → If circuit is modified after first PUB, affects later PUBs; use .copy()
□ TRAP: Mixing shots at PUB level and sampler level
  → PUB-level shots override sampler default; be explicit to avoid confusion
```

### 🧠 Mnemonic Recall Box

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 5 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🎯 "S needs M" - MOST CRITICAL                                  │
│    Sampler needs Measurements                                   │
│    → Always add measure() or measure_all() BEFORE run()         │
│    → No measurements = ERROR, not empty result                  │
│    💡 Think: "Sampler Samples Measurements"                     │
│                                                                  │
│ 📦 "TiL" - Tuple in List                                        │
│    PUB format: [(circuit,)] with trailing comma                 │
│    → (qc,) is tuple, (qc) is just parentheses                   │
│    → [qc] is wrong, [(qc,)] is right                            │
│    💡 Visual: [ (qc,) ] - "brackets hug a tuple"                │
│                                                                  │
│ 🔢 "CPS" - Circuit, Params, Shots                               │
│    PUB order: (circuit, parameter_values, shots)                │
│    → All three optional after circuit                           │
│    → Can use None as placeholder: (qc, None, 2048)              │
│    💡 Analogy: "Car (circuit) Picks (params) Speed (shots)"     │
│                                                                  │
│ 🔗 "0-D-M-G" Chain - CRITICAL PATH                              │
│    result[0].data.meas.get_counts()                             │
│    → [0] = first PUB result (list index)                        │
│    → data = data container (DataBin)                            │
│    → meas = register name (default name)                        │
│    → get_counts() = extraction method                           │
│    💡 Visual: "Zero Dogs Make Good pets"                        │
│    💡 Each step required: skip ANY = AttributeError             │
│                                                                  │
│ 📋 "DrMeGC" - Data.Register.Method.Get_Counts                   │
│    Full chain breakdown for memorization                        │
│    → Never skip .data or register name                          │
│    → result[0].meas ❌  result[0].data.meas ✓                   │
│    💡 Pronunciation: "Doctor McGee" (friendly reminder)         │
│                                                                  │
│ 🎚️ "GOMO" - Gates Off, Measure Off                             │
│    Sampler twirling defaults (both False)                       │
│    → Opposite of Estimator (both True = "GOMT")                 │
│    💡 Sampler is "GO-MO" (no motion), Estimator is "GOMT" (go!) │
│    💡 S = Still (off), E = Energized (on)                       │
│                                                                  │
│ 🛡️ "DD = Defend During Downtime"                                │
│    Dynamical Decoupling helps idle qubits only                  │
│    → Only useful when qubits wait during execution              │
│    → No idle time = no DD benefit                               │
│    💡 Think: "bodyguard protects you while you're resting"      │
│                                                                  │
│ 🔄 "LSB = Little Side is Beginning"                             │
│    Least Significant Bit ordering (rightmost = q[0])            │
│    → '01' means q[0]=1, q[1]=0 (read RIGHT to LEFT)             │
│    → Opposite of most text reading (left-to-right)              │
│    💡 Visual: q[1]q[0] → '10' has 1 on left (q[1])              │
│    💡 Analogy: "Arabic/Hebrew reading direction"                │
│                                                                  │
│ 🔤 "String Counts, Int Counts"                                  │
│    get_counts() → {'00': 512} (strings)                         │
│    get_int_counts() → {0: 512} (integers)                       │
│    💡 String is default; Int requires explicit method           │
│    💡 "get_counts() = String by default"                        │
│                                                                  │
│ 🎭 "S vs E" - Sampler vs Estimator Quick Reference              │
│    Sampler: Measurements REQUIRED | Returns counts/bitstrings  │
│    Estimator: NO measurements | Returns expectation values      │
│    💡 "Sampler Sees bits, Estimator Expects numbers"            │
│    💡 Sampler = discrete, Estimator = continuous                │
│                                                                  │
│ 🔟 "Comma Makes Tuple"                                          │
│    (qc,) is tuple, (qc) is just grouping parentheses            │
│    → Python requires comma for single-element tuples            │
│    → [(qc,)] vs [(qc)] completely different!                    │
│    💡 "No comma = no tuple = error"                             │
│    💡 Test: type((qc,)) → tuple, type((qc)) → QuantumCircuit    │
│                                                                  │
│ 🎯 "PUB = Package Under Brackets"                               │
│    Each PUB is independently packaged job                       │
│    → Multiple PUBs = batch processing                           │
│    → Each PUB gets own result: result[i]                        │
│    💡 Think: "mailing multiple packages at once"                │
│                                                                  │
│ 🔑 "Register Name = Key to Data"                                │
│    result[0].data.REGISTER_NAME.get_counts()                    │
│    → "meas" is default name from measure_all()                  │
│    → Custom registers = custom names                            │
│    💡 "Forgot name? Check qc.cregs[0].name"                     │
│                                                                  │
│ 📊 "BitArray is 2D" - Shape Understanding                       │
│    BitArray shape: [num_shots, num_bits]                        │
│    → get_counts() collapses to frequency dict                   │
│    → get_bitstrings() flattens to list                          │
│    💡 "Array of shots, each shot is array of bits"              │
│                                                                  │
│ 🚀 "Default Shots = 1K" (1024)                                  │
│    If shots not specified, defaults to 1024                     │
│    → Old backend.run() used 4096 (different!)                   │
│    💡 "1K shots = 1 kilo-sample"                                │
│                                                                  │
│ ⚡ "V2 = Victory 2" - Always Use V2                             │
│    StatevectorSampler (V2), SamplerV2 (not Sampler)            │
│    → V1 deprecated, exam assumes V2                             │
│    💡 "V2 is the way to go"                                     │
│                                                                  │
│ 🎪 "Result is Plural" - List-like Container                     │
│    result[0] required even for single PUB                       │
│    → Always index: never just result.data                       │
│    💡 "Results live in array, always use [index]"               │
│                                                                  │
│ 🔧 "Options Persist" - Configuration Stickiness                 │
│    sampler.options set once, applies to all future runs         │
│    → Change options between runs affects later jobs             │
│    💡 "Options are instance variables, not run() parameters"    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║           SECTION 5: SAMPLER - ONE-PAGE SUMMARY                       ║
║                      (12% of Exam - ~8 Questions)                      ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 BASIC USAGE WORKFLOW                                               ║
║  ├─ 1. IMPORTS                                                         ║
║  │   ├─ from qiskit.primitives import StatevectorSampler  # ideal    ║
║  │   └─ from qiskit_ibm_runtime import SamplerV2  # hardware         ║
║  ├─ 2. CREATE CIRCUIT + MEASUREMENTS (CRITICAL!)                      ║
║  │   ├─ qc = QuantumCircuit(2)                                        ║
║  │   ├─ qc.h(0); qc.cx(0,1)  # quantum operations                     ║
║  │   └─ qc.measure_all()  # ← REQUIRED! Sampler fails without this   ║
║  ├─ 3. INITIALIZE SAMPLER                                             ║
║  │   └─ sampler = StatevectorSampler()  # or SamplerV2(mode=backend) ║
║  ├─ 4. RUN WITH PUB FORMAT                                            ║
║  │   └─ job = sampler.run([(qc,)], shots=1024)  # note: (qc,) tuple! ║
║  ├─ 5. EXTRACT RESULTS                                                ║
║  │   ├─ result = job.result()  # PrimitiveResult                     ║
║  │   └─ counts = result[0].data.meas.get_counts()  # full chain      ║
║  └─ Key: MUST have measurements, MUST use tuple, MUST index result    ║
║                                                                        ║
║  📦 PUB FORMATS (Primitive Unified Bloc)                               ║
║  ├─ Anatomy: (circuit, parameters, shots)                             ║
║  │   ├─ circuit: QuantumCircuit with measurements                     ║
║  │   ├─ parameters: list of values or None (optional)                 ║
║  │   └─ shots: int override or None (optional, defaults to 1024)      ║
║  ├─ EXAMPLES:                                                          ║
║  │   ├─ Basic single:     [(qc,)]                    # trailing comma!║
║  │   ├─ With parameters:  [(qc, [0.5, 1.2])]        # 2 param values ║
║  │   ├─ Custom shots:     [(qc, None, 2048)]        # None placeholder║
║  │   ├─ Full spec:        [(qc, [0.5, 1.2], 2048)]  # all specified  ║
║  │   └─ Multiple PUBs:    [(qc1,), (qc2,), (qc3,)]  # batch 3 circuits║
║  └─ Critical: Each PUB must be TUPLE; list contains tuples            ║
║                                                                        ║
║  🔗 RESULT EXTRACTION CHAIN (MEMORIZE!)                                ║
║  ├─ Full path: result[0].data.meas.get_counts()                       ║
║  │   ├─ result       → PrimitiveResult (list-like container)          ║
║  │   ├─ [0]          → Index first PUB (PubResult object)             ║
║  │   ├─ .data        → DataBin (holds all classical registers)        ║
║  │   ├─ .meas        → BitArray for "meas" register (default name)    ║
║  │   └─ .get_counts()→ Method returning dict {'00': 512, '11': 512}   ║
║  ├─ Alternative methods on BitArray:                                   ║
║  │   ├─ .get_bitstrings()   → ['00', '11', '00', ...] (list)          ║
║  │   └─ .get_int_counts()   → {0: 512, 3: 512} (int keys)             ║
║  ├─ Custom register names:                                             ║
║  │   └─ result[0].data.output.get_counts()  # 'output' not 'meas'     ║
║  └─ Multi-PUB indexing:                                                ║
║      ├─ result[0].data.meas.get_counts()  # first circuit             ║
║      ├─ result[1].data.meas.get_counts()  # second circuit            ║
║      └─ result[i].data.meas.get_counts()  # i-th circuit              ║
║                                                                        ║
║  🔄 MULTIPLE CIRCUITS (Batch Processing)                               ║
║  ├─ Single submission:                                                 ║
║  │   └─ job = sampler.run([(qc1,), (qc2,), (qc3,)])                   ║
║  ├─ Individual access:                                                 ║
║  │   ├─ result[0]  → qc1 results                                      ║
║  │   ├─ result[1]  → qc2 results                                      ║
║  │   └─ result[2]  → qc3 results                                      ║
║  ├─ Iteration pattern:                                                 ║
║  │   ├─ for i, pub_result in enumerate(result):                       ║
║  │   │       counts = pub_result.data.meas.get_counts()                ║
║  │   └─ OR: all_counts = [r.data.meas.get_counts() for r in result]   ║
║  └─ Each PUB independent: separate shots, separate results            ║
║                                                                        ║
║  ⚙️ ADVANCED OPTIONS (sampler.options)                                 ║
║  ├─ Configuration types:                                               ║
║  │   ├─ .default_shots = 2048           # change default              ║
║  │   ├─ .optimization_level = 3         # transpiler (0-3)            ║
║  │   ├─ .resilience_level = 1           # error mitigation (0-2)      ║
║  │   ├─ .twirling.enable_gates = True   # randomized compilation      ║
║  │   ├─ .twirling.enable_measure = True # measurement twirling        ║
║  │   ├─ .twirling.num_randomizations=32 # rounds of twirling          ║
║  │   ├─ .dynamical_decoupling.enable=True  # idle qubit protection    ║
║  │   └─ .dynamical_decoupling.sequence_type='XY4'  # DD sequence      ║
║  ├─ Setting options:                                                   ║
║  │   ├─ options = sampler.options       # get current                 ║
║  │   ├─ options.default_shots = 4096    # modify                      ║
║  │   └─ sampler.options = options       # reassign (some cases)       ║
║  └─ Options persist across multiple run() calls on same instance      ║
║                                                                        ║
║  🎭 SAMPLER VS ESTIMATOR                                               ║
║  ├─ Sampler:                                                           ║
║  │   ├─ REQUIRES measurements in circuit                              ║
║  │   ├─ Returns: counts/bitstrings (discrete outcomes)                ║
║  │   ├─ PUB format: [(circuit,)]                                      ║
║  │   ├─ Use case: sampling probability distributions                  ║
║  │   └─ Twirling defaults: gates=False, measure=False (both OFF)      ║
║  ├─ Estimator:                                                         ║
║  │   ├─ NO measurements (forbidden)                                    ║
║  │   ├─ Returns: expectation values ⟨ψ|O|ψ⟩ (continuous)              ║
║  │   ├─ PUB format: [(circuit, observable)]                           ║
║  │   ├─ Use case: computing energy, observables                       ║
║  │   └─ Twirling defaults: gates=True, measure=True (both ON)         ║
║  └─ Key: Mutually exclusive patterns - don't mix!                     ║
║                                                                        ║
║  🔢 BIT ORDERING (Critical for Exam!)                                  ║
║  ├─ Qiskit uses LSB (Least Significant Bit first)                     ║
║  │   └─ Rightmost bit = qubit 0 (little-endian)                       ║
║  ├─ Reading bitstrings:                                                ║
║  │   ├─ '01' → q[0]=1, q[1]=0  (read right-to-left!)                  ║
║  │   ├─ '10' → q[0]=0, q[1]=1                                         ║
║  │   └─ '101' → q[0]=1, q[1]=0, q[2]=1                                ║
║  ├─ Conversion to integer:                                             ║
║  │   ├─ '01' in LSB = 2 in decimal (not 1!)                           ║
║  │   └─ Must reverse for standard conversion: int('01'[::-1], 2)      ║
║  └─ TRAP: Most frameworks use MSB (leftmost=q[0]); Qiskit opposite!   ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (HIGHEST PRIORITY!)                              ║
║  ╔════════════════════════════════════════════════════════════════╗  ║
║  ║ 1. ❌ No measurements → Sampler ERROR (not warning!)            ║  ║
║  ║    ✓ ALWAYS: qc.measure_all() before sampler.run()             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 2. ❌ sampler.run([qc]) - missing tuple wrapper                 ║  ║
║  ║    ✓ CORRECT: sampler.run([(qc,)]) with trailing comma         ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 3. ❌ sampler.run([(qc)]) - missing comma (NOT a tuple!)        ║  ║
║  ║    ✓ CORRECT: (qc,) with comma makes single-element tuple      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 4. ❌ result.data.meas.get_counts() - missing [0] index         ║  ║
║  ║    ✓ CORRECT: result[0].data.meas.get_counts()                 ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 5. ❌ result[0].meas.get_counts() - missing .data               ║  ║
║  ║    ✓ CORRECT: result[0].data.meas (never skip .data!)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 6. ❌ Assuming register always named "meas"                     ║  ║
║  ║    ✓ CHECK: qc.cregs[0].name for actual name                   ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 7. ❌ Twirling defaults: Sampler ≠ Estimator                    ║  ║
║  ║    ✓ Sampler: gates=False, measure=False (both OFF)            ║  ║
║  ║    ✓ Estimator: gates=True, measure=True (both ON)             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 8. ❌ Bit ordering: '01' ≠ q[0]=0, q[1]=1                       ║  ║
║  ║    ✓ CORRECT: '01' → q[0]=1, q[1]=0 (LSB = right-to-left)      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 9. ❌ get_counts() returns integers                             ║  ║
║  ║    ✓ Returns STRING keys: {'00': 512}                          ║  ║
║  ║    ✓ For ints use: get_int_counts() → {0: 512}                 ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 10. ❌ Wrong parameter count: [0.5] for 2-param circuit         ║  ║
║  ║     ✓ Must match exactly: 2 params need 2 values               ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 11. ❌ PUB order: (shots, circuit, params)                      ║  ║
║  ║     ✓ CORRECT: (circuit, params, shots) - "CPS"                ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 12. ❌ DD helps all circuits                                    ║  ║
║  ║     ✓ Only helps circuits with IDLE qubits during execution    ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 13. ❌ from qiskit.primitives import Sampler (V1, deprecated)   ║  ║
║  ║     ✓ CORRECT: import StatevectorSampler (V2) or SamplerV2     ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 14. ❌ Options set after run() affecting that job              ║  ║
║  ║     ✓ Options must be set BEFORE job submission                ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 15. ❌ Using shots=0 or negative                                ║  ║
║  ║     ✓ shots must be positive int (ValueError otherwise)        ║  ║
║  ╚════════════════════════════════════════════════════════════════╝  ║
║                                                                        ║
║  💡 MEMORY AIDS                                                        ║
║  ├─ "S needs M" - Sampler needs Measurements (CRITICAL!)              ║
║  ├─ "TiL" - Tuple in List: [(qc,)] format                             ║
║  ├─ "0-D-M-G" - result[0].data.meas.get_counts() chain                ║
║  ├─ "GOMO" - Gates Off, Measure Off (Sampler twirling defaults)       ║
║  ├─ "LSB = Little Side is Beginning" - rightmost = q[0]               ║
║  └─ "Comma Makes Tuple" - (qc,) is tuple, (qc) is not!                ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 📁 Files in This Section

| File | Purpose | Key Content |
|------|---------|-------------|
| [README.md](README.md) | Complete learning guide | Theory, 8 traps, 15 practice questions, checklists |
| [sampler_primitive.ipynb](sampler_primitive.ipynb) | CODE LABORATORY | Executable examples, trap demonstrations, challenges |
| [README_OLD.md](README_OLD.md) | Backup | Previous version for reference |

---

## ➡️ Next Steps

1. **Complete the notebook**: Run all cells in [sampler_primitive.ipynb](sampler_primitive.ipynb)
2. **Practice PUB format**: Write 5 different PUB variations
3. **Master the chain**: Write `result[0].data.meas.get_counts()` 10 times
4. **Take Practice Exam**: Score at least 90% on the 15-question exam above
5. **Compare with Estimator**: Review [Section 6: Estimator](../section_6_estimator/README.md) for differences

---

## 🔗 Related Sections

- **Section 4**: [Run Circuits](../section_4_run_circuits/) - Runtime fundamentals
- **Section 6**: [Estimator](../section_6_estimator/) - Expectation values
- **Section 7**: [Results](../section_7_results/) - Advanced result processing

---

## 📚 Additional Resources

- Qiskit Primitives Guide: [docs.quantum.ibm.com/guides/primitives](https://docs.quantum.ibm.com/guides/primitives)
- Sampler API Reference: [docs.quantum.ibm.com/api/qiskit/primitives](https://docs.quantum.ibm.com/api/qiskit/primitives)
- IBM Runtime: [docs.quantum.ibm.com/api/qiskit-ibm-runtime](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime)

---

**Sampler is 12% of the exam - MASTER THIS!** 🚀⚡

---

*Last Updated: 2025-01-15 | Qiskit Version: 1.x | Exam Weight: ~12%*
