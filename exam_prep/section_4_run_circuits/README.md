# Section 4: Run Circuits on Backend (15% of Exam)

> **Exam Weight**: ~10 questions | **Difficulty**: Medium-High | **Must Master**: ✅✅

---

## 📖 Overview

This section covers how to **execute quantum circuits** on real quantum hardware and simulators using IBM Quantum Runtime services. Understanding transpilation, backend configuration, sessions, job management, and options is CRITICAL for the exam.

### What You'll Learn

1. **QiskitRuntimeService**: Connecting to IBM Quantum, backend selection
2. **Transpilation**: Converting circuits to hardware-executable form
3. **Advanced Transpilation**: PassManager stages, layout/routing methods
4. **Sessions & Batches**: Execution modes for different use cases
5. **Job Management**: JobStatus enum, job retrieval, lifecycle
6. **Options Configuration**: Optimization, resilience, shots
7. **Backend Target**: Understanding hardware constraints (V2 API)
8. **Coupling Maps**: Hardware topology and qubit connectivity
9. **Broadcasting Rules**: Parameter/observable array handling

---

## 🎯 Why This Section Matters (Conceptual Foundation)

### 🧠 Conceptual Deep Dive

#### Analogy: The Translator

Transpilation is like translating a poem from English to Japanese:
- **Source**: Your abstract circuit (the poem)
- **Target**: The specific quantum device (the Japanese language)
- **Constraints**: The device only supports certain gates (vocabulary) and connections (grammar)
- **Goal**: Preserve the meaning (logic) while adapting to the constraints
- **Optimization**: A good translator (transpiler) makes the result elegant and efficient

#### Virtual vs. Physical Qubits
- **Virtual Qubit**: The logical variable in your code (`q[0]`). It's perfect and abstract.
- **Physical Qubit**: The actual superconducting loop on the chip. It has noise, decoherence, and specific connections.
- **Mapping**: The transpiler decides which physical qubit plays the role of which virtual qubit.

### Visual Overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                    CIRCUIT EXECUTION PIPELINE                         │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   Your Code                                                           │
│       ↓                                                               │
│   ┌──────────────────────┐                                           │
│   │  QuantumCircuit      │  ← You write this (abstract gates)        │
│   └──────────────────────┘                                           │
│       ↓                                                               │
│   ┌──────────────────────┐                                           │
│   │  transpile()         │  ← Convert to hardware gates              │
│   └──────────────────────┘                                           │
│       ↓                                                               │
│   ┌──────────────────────┐                                           │
│   │  QiskitRuntimeService│  ← Connect to IBM Cloud                   │
│   └──────────────────────┘                                           │
│       ↓                                                               │
│   ┌──────────────────────┐                                           │
│   │  Sampler/Estimator   │  ← Primitives (V2 API)                    │
│   └──────────────────────┘                                           │
│       ↓                                                               │
│   ┌──────────────────────┐                                           │
│   │  IBM Quantum Backend │  ← Real hardware or simulator             │
│   └──────────────────────┘                                           │
│       ↓                                                               │
│   Results (counts, expectation values)                                │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Covered (Quick Reference)

| Topic | Description | Exam Weight | Priority |
|-------|-------------|-------------|----------|
| **QiskitRuntimeService** | IBM Quantum connection, backend access | High | 🔴 |
| **transpile()** | Circuit-to-hardware conversion | High | 🔴 |
| **Optimization Levels** | 0-3 optimization aggressiveness | High | 🔴 |
| **Sessions & Batches** | Execution modes | Medium | 🟡 |
| **JobStatus** | Job lifecycle management | High | 🔴 |
| **Options** | Configuration (resilience, shots) | High | 🔴 |
| **Backend Target** | V2 API, hardware properties | Medium | 🟡 |
| **Coupling Maps** | Qubit connectivity graph | Medium | 🟡 |
| **Broadcasting** | Parameter/observable arrays | Medium | 🟡 |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION 4 LEARNING PATH                       │
├─────────────────────────────────────────────────────────────────┤
│  START HERE                                                      │
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. QiskitRuntimeService                                     ││
│  │    └─ save_account(), service.backend(), least_busy()       ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 2. TRANSPILATION (CORE!)                                    ││
│  │    └─ transpile(), optimization_level 0-3                   ││
│  │    └─ Basis gates, coupling map, initial_layout             ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 3. ADVANCED TRANSPILATION                                   ││
│  │    └─ 6-stage pipeline, PassManager, layout/routing methods ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 4. JOBS & SESSIONS                                          ││
│  │    └─ JobStatus enum, Session vs Batch, mode= parameter     ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 5. OPTIONS CONFIGURATION                                    ││
│  │    └─ optimization_level, resilience_level, shots           ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 6. BACKEND TARGET (V2 API)                                  ││
│  │    └─ target.operation_names, qubit_properties, T1/T2       ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  COMPLETE: Ready for Section 4 exam questions                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 QiskitRuntimeService

### Overview
QiskitRuntimeService is the gateway to IBM Quantum. It handles authentication, backend discovery, and job submission.

---

### 🔹 Setup & Authentication

#### 1. Definition
QiskitRuntimeService manages connections to IBM Quantum cloud services, providing access to real quantum hardware and simulators.

#### 2. Analogy + Intuition
**Real-World Analogy**: Like logging into a cloud computing platform (AWS, Azure) - you need credentials, then you can access available resources (backends).

**Intuition Builder**: Your circuit needs to run somewhere. QiskitRuntimeService is the "login portal" that gives you access to IBM's quantum computers.

#### 3. Implementation

**Qiskit Syntax**
```python
from qiskit_ibm_runtime import QiskitRuntimeService

# First time: Save credentials
QiskitRuntimeService.save_account(
    channel='ibm_quantum',
    token='YOUR_IBM_QUANTUM_TOKEN',
    overwrite=True
)

# After saving: Load service
service = QiskitRuntimeService()
```

**Parameters**
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `channel` | str | 'ibm_quantum' or 'ibm_cloud' | 'ibm_quantum' |
| `token` | str | API token from quantum.ibm.com | Required |
| `overwrite` | bool | Replace existing credentials | False |

**Accessing Backends**
```python
# List all available backends
backends = service.backends()
for backend in backends:
    print(f"{backend.name}: {backend.num_qubits} qubits")

# Get specific backend
backend = service.backend('ibm_brisbane')

# Get least busy backend
backend = service.least_busy(min_num_qubits=5)
```

#### 4. ⚠️ Trap Alert

**Trap: Forgetting to save account first**
- ❌ **Wrong**: `service = QiskitRuntimeService()` without saving credentials
- ✅ **Correct**: First `save_account()`, then instantiate service
- 🔍 **Why it's tricky**: save_account only needed once, then credentials persist

```python
# ❌ WRONG - no credentials saved
service = QiskitRuntimeService()  # Error if no saved account!

# ✅ CORRECT - save once, use forever
QiskitRuntimeService.save_account(token='...', overwrite=True)
service = QiskitRuntimeService()  # Works!
```

#### 5. 🧠 Mnemonic
**"SAVE before you SERVE"**
- Save account → then Service works
- SAVE = credentials, SERVE = service

#### 6. ⚡ Quick Check

**Q: What method saves IBM Quantum credentials for future use?**

<details>
<summary>Answer</summary>

**A**: `QiskitRuntimeService.save_account(token='...', channel='ibm_quantum')`

This only needs to be called once - credentials are persisted to disk.
</details>

---

## 🔧 Transpilation (EXAM CRITICAL!)

### Overview
Transpilation converts your abstract quantum circuit into a form executable on specific hardware. This is the MOST TESTED topic in this section.

---

### 🔹 The transpile() Function

#### 1. Definition
`transpile()` transforms a quantum circuit to match hardware constraints: basis gates, qubit connectivity, and optimization.

#### 2. Analogy + Intuition
**Real-World Analogy**: 
- **Compiler**: Like compiling C code to assembly - high-level → machine-specific
- **GPS Navigation**: Finds the best route through hardware constraints

**Intuition Builder**: Your H gate doesn't physically exist on hardware - it must become RZ+SX. Your CX(0,5) might need SWAP gates if qubits 0 and 5 aren't connected.

#### 3. Math + Visual

**Visual: Transpilation Effect**
```
Your Circuit:              Hardware Reality:
     ┌───┐                    ┌────┐
q_0: ┤ H ├──■──           q_0:┤ RZ ├──■──    ← H → RZ + SX
     └───┘┌─┴─┐               └────┘┌─┴─┐
q_1: ─────┤ X ├           q_1: ─────┤ X ├    ← CX allowed
          └───┘                     └───┘
          ↓                          ↓
     Arbitrary gates            Basis gates only!
     Any qubit pair            Coupling map constraints!
```

#### 4. Implementation

**Qiskit Syntax**
```python
from qiskit import transpile

transpiled = transpile(
    qc,
    backend=backend,
    optimization_level=3
)
```

**Parameters**
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `circuits` | QuantumCircuit | Circuit(s) to transpile | Required |
| `backend` | Backend | Target hardware | None |
| `optimization_level` | int | 0-3 (higher = better) | 2 |
| `basis_gates` | list | Override basis gates | From backend |
| `coupling_map` | list | Override connectivity | From backend |
| `initial_layout` | list | Manual qubit mapping | Auto |
| `seed_transpiler` | int | Reproducibility | None |

**Basic Example**
```python
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 2)

transpiled = transpile(qc, backend, optimization_level=3)
print(f"Original depth: {qc.depth()}")
print(f"Transpiled depth: {transpiled.depth()}")
```

#### 5. ⚠️ Trap Alert

**Trap 1: Thinking transpilation is deterministic**
- ❌ **Wrong**: Expecting same output every time
- ✅ **Correct**: Different runs may produce different circuits
- 🔍 **Why**: Random seed affects layout/routing choices

```python
# ❌ WRONG assumption
qc1 = transpile(qc, backend, optimization_level=3)
qc2 = transpile(qc, backend, optimization_level=3)
# qc1 and qc2 might be DIFFERENT!

# ✅ CORRECT - use seed for reproducibility
qc1 = transpile(qc, backend, seed_transpiler=42)
qc2 = transpile(qc, backend, seed_transpiler=42)
# Now qc1 == qc2
```

**Trap 2: Thinking primitives require manual transpilation**
- ❌ **Wrong**: Always transpiling before Sampler/Estimator
- ✅ **Correct**: Primitives auto-transpile internally
- 🔍 **Why**: Manual transpile gives control, but isn't required

```python
# Both work!
sampler.run([qc])  # Auto-transpiles
sampler.run([transpile(qc, backend)])  # Manual control
```

#### 6. 🧠 Mnemonic
**"Transpile = TRANSlate + comPILE"**
- TRANS: Translate gates to hardware basis
- PILE: Pile on optimizations

#### 7. ⚡ Quick Check

**Q: What is the default optimization_level for transpile()?**

<details>
<summary>Answer</summary>

**A**: 2 (Medium optimization)

- Level 0: No optimization
- Level 1: Light optimization
- Level 2: **DEFAULT** - balanced
- Level 3: Heavy optimization
</details>

---

### 🔹 Optimization Levels (EXAM ESSENTIAL!)

#### 1. Definition
Optimization levels (0-3) control how aggressively the transpiler optimizes your circuit for the target hardware.

#### 2. Analogy + Intuition
**Real-World Analogy**: Like compiler optimization flags (-O0 to -O3):
- O0: Debug mode (fast compile, no optimization)
- O3: Release mode (slow compile, best performance)

#### 3. Visual Reference

```
┌─────────────────────────────────────────────────────────────────┐
│              OPTIMIZATION LEVELS COMPARISON                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Level 0: "DEBUG"      Level 1: "FAST"                          │
│  ┌────────────────┐    ┌────────────────┐                       │
│  │ • Basis only   │    │ • Basic cancel │                       │
│  │ • Simple layout│    │ • Fast compile │                       │
│  │ • No optimize  │    │ • Light opts   │                       │
│  └────────────────┘    └────────────────┘                       │
│                                                                  │
│  Level 2: "DEFAULT"    Level 3: "BEST"                          │
│  ┌────────────────┐    ┌────────────────┐                       │
│  │ • Commutativity│    │ • Aggressive   │                       │
│  │ • Smart layout │    │ • Multiple try │                       │
│  │ • Gate merge   │    │ • Resynthesis  │                       │
│  └────────────────┘    └────────────────┘                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 4. Implementation

```python
# Compare all levels
for level in [0, 1, 2, 3]:
    transpiled = transpile(qc, backend, optimization_level=level)
    print(f"Level {level}: depth={transpiled.depth()}, gates={transpiled.size()}")

# Output example:
# Level 0: depth=15, gates=45
# Level 1: depth=12, gates=38
# Level 2: depth=10, gates=32  ← Default
# Level 3: depth=8, gates=28   ← Best, slowest
```

**Decision Tree**
```
┌─ What's your goal? ───────────────────────┐
│  Debugging transpiler? → Level 0          │
│  Quick prototyping? → Level 1             │
│  Production (default)? → Level 2          │
│  Best quality? → Level 3                  │
└───────────────────────────────────────────┘
```

#### 5. ⚠️ Trap Alert

**Trap: Thinking higher level always means fewer gates**
- ❌ **Wrong**: Level 3 always produces smallest circuit
- ✅ **Correct**: Level 3 tries harder but isn't guaranteed
- 🔍 **Why**: Optimization is heuristic, not perfect

#### 6. 🧠 Mnemonic
**"0=Zero, 1=One pass, 2=Two-way, 3=Three+ tries"**
- 0: Zero optimization (just translation)
- 1: One quick pass
- 2: Two-way optimization (default)
- 3: Three or more attempts for best result

#### 7. ⚡ Quick Check

**Q: Which optimization_level should you use for maximum circuit quality?**

<details>
<summary>Answer</summary>

**A**: Level 3

It's the slowest to compile but produces the best optimized circuits for hardware execution.
</details>

---

## 🔧 Advanced Transpilation

### Overview
Understanding the 6-stage transpilation pipeline and custom pass managers for fine-grained control.

---

### 🔹 The 6-Stage Pipeline

#### 1. Definition
The transpiler processes circuits through 6 sequential stages: Init → Layout → Routing → Translation → Optimization → Scheduling.

#### 2. Visual Reference

```
┌───────────────────────────────────────────────────────────────────┐
│                      TRANSPILATION PIPELINE                        │
├───────────────────────────────────────────────────────────────────┤
│  Stage 1: INIT       → Unroll custom gates, validate circuit      │
│           ↓                                                        │
│  Stage 2: LAYOUT     → Map virtual qubits → physical qubits       │
│           ↓                                                        │
│  Stage 3: ROUTING    → Insert SWAPs for non-adjacent qubits       │
│           ↓                                                        │
│  Stage 4: TRANSLATION → Convert to basis gates                    │
│           ↓                                                        │
│  Stage 5: OPTIMIZATION → Simplify, cancel gates, optimize         │
│           ↓                                                        │
│  Stage 6: SCHEDULING → Add timing information (optional)          │
└───────────────────────────────────────────────────────────────────┘
```

| Stage | Purpose | Key Operations |
|-------|---------|----------------|
| **Init** | Prepare circuit | Unroll 3+ qubit gates |
| **Layout** | Map qubits | Analyze connectivity, assign positions |
| **Routing** | Handle connectivity | Insert SWAP gates where needed |
| **Translation** | Convert gates | Replace with hardware basis gates |
| **Optimization** | Reduce overhead | Merge gates, cancel redundancies |
| **Scheduling** | Add timing | Compute delays, align operations |

#### 3. Implementation

**generate_preset_pass_manager() API**
```python
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

pm = generate_preset_pass_manager(
    optimization_level=2,
    backend=backend
)
transpiled = pm.run(circuit)
```

**Layout Methods**
| Method | Strategy | Best For |
|--------|----------|----------|
| `'trivial'` | Identity mapping | Testing |
| `'dense'` | Most connected qubits | Dense circuits |
| `'sabre'` | SABRE algorithm | General purpose (default) |

**Routing Methods**
| Method | Strategy | Best For |
|--------|----------|----------|
| `'basic'` | Sequential SWAPs | Simple circuits |
| `'stochastic'` | Random search | Sometimes better |
| `'sabre'` | SABRE routing | Most circuits (default) |

#### 4. ⚠️ Trap Alert

**Trap: Forgetting to apply layout to observables!**
- ❌ **Wrong**: Using original observable after transpilation
- ✅ **Correct**: `observable.apply_layout(transpiled.layout)`

```python
# ❌ WRONG - observable on wrong qubits
transpiled = pm.run(circuit)
pub = (transpiled, observable)  # Observable not remapped!

# ✅ CORRECT - remap observable
mapped_obs = observable.apply_layout(transpiled.layout)
pub = (transpiled, mapped_obs)
```

#### 5. 🧠 Mnemonic
**"ILRTOS" = "I Love Running Transpiled Optimized Schedules"**
- **I**nit
- **L**ayout  
- **R**outing
- **T**ranslation
- **O**ptimization
- **S**cheduling

#### 6. ⚡ Quick Check

**Q: How many CNOT gates does a SWAP gate decompose into?**

<details>
<summary>Answer</summary>

**A**: 3 CNOT gates

SWAP = CX + CX + CX (with different control/target patterns)

This is why routing overhead is expensive!
</details>

---

## 🔧 Jobs and Sessions

### Overview
Understanding execution modes (Job, Session, Batch) and job lifecycle management.

---

### 🔹 Execution Modes

#### 1. Definition
IBM Quantum offers three execution modes: Job (single), Session (sequential with reservation), and Batch (parallel).

#### 2. Visual Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXECUTION MODE DECISION                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─ How many jobs? ─────────────────────────────────────────┐   │
│  │                                                           │   │
│  │    Just 1        Multiple           Iterative            │   │
│  │    circuit       independent        algorithm            │   │
│  │       ↓              ↓                  ↓                │   │
│  │   ┌───────┐    ┌───────────┐    ┌─────────────┐         │   │
│  │   │ JOB   │    │  BATCH    │    │  SESSION    │         │   │
│  │   │ MODE  │    │  MODE     │    │  MODE       │         │   │
│  │   └───────┘    └───────────┘    └─────────────┘         │   │
│  │                                                           │   │
│  │   Testing       Param sweeps     VQE/QAOA                │   │
│  │   One-off       Benchmarking     Feedback loops          │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 3. Implementation

**The `mode=` Parameter (v0.24.0+)**
```python
from qiskit_ibm_runtime import (
    EstimatorV2 as Estimator,
    SamplerV2 as Sampler,
    Session, Batch
)

# Job Mode (direct backend)
sampler = Sampler(mode=backend)

# Session Mode (reserved access)
with Session(backend=backend) as session:
    estimator = Estimator(mode=session)
    # Multiple jobs share dedicated QPU

# Batch Mode (parallel execution)
with Batch(backend=backend) as batch:
    sampler = Sampler(mode=batch)
    # Jobs grouped for efficiency
```

#### Example Scenarios with Pseudocode

**Scenario 1: Job Mode - Single Test Circuit**
```python
# Testing a single algorithm
from qiskit_ibm_runtime import SamplerV2 as Sampler

# Direct backend execution (no session needed)
sampler = Sampler(mode=backend)

# Run once
job = sampler.run([bell_circuit])
result = job.result()
counts = result[0].data.meas.get_counts()

# Use case: Quick tests, debugging, one-off measurements
```

**Scenario 2: Batch Mode - Parameter Sweep**
```python
# Benchmarking 50 circuits with different parameters
from qiskit_ibm_runtime import Batch, SamplerV2 as Sampler

# Prepare 50 independent circuits
circuits = [create_vqe_circuit(theta) for theta in np.linspace(0, 2*np.pi, 50)]

# Batch groups jobs for efficient parallel execution
with Batch(backend=backend) as batch:
    sampler = Sampler(mode=batch)
    job = sampler.run(circuits)  # All 50 submit together
    result = job.result()

# Use case: Parameter sweeps, benchmarking, independent circuits
# Backend optimizes execution order for efficiency
```

**Scenario 3: Session Mode - VQE Algorithm**
```python
# Variational algorithm with ~100 iterations
from qiskit_ibm_runtime import Session, EstimatorV2 as Estimator

with Session(backend=backend, max_time="1h") as session:
    estimator = Estimator(mode=session)
    
    params = initial_params
    for iteration in range(100):
        # Measure cost function
        pub = (vqe_circuit, hamiltonian, params)
        job = estimator.run([pub])
        result = job.result()
        cost = result[0].data.evs[0]
        
        # Classical optimizer updates params
        params = optimizer.step(cost, params)
        
        # Next iteration uses SAME reserved QPU (no re-queuing!)
    
    final_energy = cost

# Use case: VQE, QAOA, any algorithm with classical feedback loop
# Session reserves QPU, preventing queue delays between iterations
```

**Scenario 4: Session Mode - QAOA with Mid-Circuit Feedback**
```python
# QAOA with adaptive layers based on intermediate results
with Session(backend=backend) as session:
    sampler = Sampler(mode=session)
    
    # Layer 1
    job1 = sampler.run([qaoa_layer1])
    result1 = job1.result()
    counts1 = result1[0].data.meas.get_counts()
    
    # Analyze counts, decide next layer
    if max(counts1.values()) > threshold:
        qaoa_layer2 = build_deeper_circuit()
    else:
        qaoa_layer2 = build_shallower_circuit()
    
    # Layer 2 runs without queuing delay
    job2 = sampler.run([qaoa_layer2])
    result2 = job2.result()

# Use case: Adaptive algorithms, quantum error correction calibration
```

**Scenario 5: Batch Mode - Benchmarking Multiple Algorithms**
```python
# Compare 20 different quantum algorithms
algorithms = [
    deutsch_jozsa(),
    grover_search(),
    simon_algorithm(),
    # ... 17 more
]

with Batch(backend=backend) as batch:
    sampler = Sampler(mode=batch)
    
    # All algorithms submit together
    job = sampler.run(algorithms)
    results = job.result()
    
    # Process all results
    for i, result in enumerate(results):
        counts = result.data.meas.get_counts()
        success_rate = measure_algorithm_success(counts)
        print(f"Algorithm {i}: {success_rate:.2%} success")

# Use case: Fair comparison (same backend conditions), parallel benchmarking
```

#### Decision Tree for Mode Selection

```
┌─ Do you need results to inform next circuit? ───────────┐
│                                                          │
│  NO                           YES                        │
│   ↓                            ↓                         │
│  How many circuits?      → SESSION MODE                  │
│   ↓                        (iterative, feedback)        │
│  Just 1?                                                 │
│   ↓                                                      │
│  YES → JOB MODE                                          │
│  (single, testing)                                       │
│   ↓                                                      │
│  NO → BATCH MODE                                         │
│  (many, independent)                                     │
└──────────────────────────────────────────────────────────┘
```

**Mode Selection Guidelines**

| Situation | Recommended Mode | Reason |
|-----------|-----------------|---------|
| Single circuit test | Job | Simplest, no overhead |
| 10-100 independent circuits | Batch | Parallel execution, grouped |
| VQE/QAOA optimization | Session | Reserved access, no re-queuing |
| Parameter sweep (no feedback) | Batch | Independent, can parallelize |
| Adaptive algorithm | Session | Each result informs next circuit |
| Quick prototype | Job | Fast, minimal setup |
| Production workload | Batch or Session | Depends on interdependence |

**Visual: Mode Comparison**

```
┌────────────────────────────────────────────────────────┐
│              EXECUTION MODE CHARACTERISTICS             │
├────────────────────────────────────────────────────────┤
│                                                         │
│  JOB MODE:           BATCH MODE:        SESSION MODE:  │
│                                                         │
│  Single Circuit      Multiple Circuits   Iterative     │
│  ┌────┐              ┌─┬─┬─┬─┬─┐        ┌──→──→──→──┐ │
│  │ QC │              │ │ │ │ │ │        │   Loop    │ │
│  └────┘              └─┴─┴─┴─┴─┘        └──←──←──←──┘ │
│                                                         │
│  Queue once          Queue once          Reserved QPU  │
│  Run immediately     Optimized order     Sequential    │
│  No overhead         Grouped              No re-queue  │
│                                                         │
│  Best for:           Best for:           Best for:     │
│  • Testing           • Benchmarks         • VQE/QAOA   │
│  • Debugging         • Param sweeps       • Adaptive   │
│  • One-off           • Independent        • Feedback   │
│                                                         │
└────────────────────────────────────────────────────────┘
```

**Common Pitfalls**

❌ **Using Session for independent circuits**
- Wastes reserved time waiting for results
- Better: Use Batch mode for parallel execution

❌ **Using Batch for VQE iterations**
- Each iteration must wait in queue
- Better: Use Session for reserved access

✅ **Correct patterns:**
- Job: Single circuit, testing phase
- Batch: 50 Grover instances with different databases
- Session: VQE with 200 cost function evaluations

#### 4. ⚠️ Trap Alert

**Trap: Using deprecated `session=` parameter**
- ❌ **Wrong**: `Estimator(session=session)` (old syntax)
- ✅ **Correct**: `Estimator(mode=session)` (v0.24.0+)

#### 5. 🧠 Mnemonic
**"JBS = Jobs, Batch, Session"**
- **J**ob: Just one
- **B**atch: Bundle together
- **S**ession: Sequential reserved

#### 6. ⚡ Quick Check

**Q: Which execution mode reserves dedicated QPU access for iterative algorithms like VQE?**

<details>
<summary>Answer</summary>

**A**: Session mode

Sessions provide exclusive access so intermediate results can inform next circuit without waiting in queue.
</details>

---

### 🔹 JobStatus Enum (EXAM TESTED!)

#### 1. Definition
JobStatus is an enum representing the current state of a quantum job through its lifecycle.

#### 2. Visual Reference

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ INITIALIZING│───▶│   QUEUED    │───▶│  VALIDATING │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                        ┌─────────────────────┼─────────────────────┐
                        ▼                     ▼                     ▼
                 ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
                 │   RUNNING   │       │    ERROR    │       │  CANCELLED  │
                 └──────┬──────┘       └─────────────┘       └─────────────┘
                        │                   Final               Final
                        ▼                   State               State
                 ┌─────────────┐
                 │    DONE     │
                 └─────────────┘
                    Final State
```

#### 3. Implementation

```python
from qiskit.providers import JobStatus

job = sampler.run([qc])

# Check status
status = job.status()

if status == JobStatus.DONE:
    result = job.result()
elif status == JobStatus.ERROR:
    print("Job failed!")
elif status == JobStatus.CANCELLED:
    print("Job was cancelled")
```

**Job Methods**
| Method | Return | Description |
|--------|--------|-------------|
| `job_id()` | str | Unique identifier |
| `status()` | JobStatus | Current state |
| `result()` | PrimitiveResult | Get results (blocks) |
| `cancel()` | None | Cancel running job |
| `done()` | bool | True if finished |

**Job Retrieval Pattern**
```python
# Save job ID
job_id = job.job_id()
print(f"Save this: {job_id}")

# Later... retrieve
service = QiskitRuntimeService()
retrieved_job = service.job(job_id)

if retrieved_job.status() == JobStatus.DONE:
    result = retrieved_job.result()
```

#### 4. ⚠️ Trap Alert

**Trap: Not checking status before getting results**
- ❌ **Wrong**: `job.result()` on a queued job (blocks forever)
- ✅ **Correct**: Check `job.done()` or use timeout

```python
# ❌ Could block indefinitely
result = job.result()

# ✅ Better - with timeout
result = job.result(timeout=300)  # 5 minute max
```

#### 5. 🧠 Mnemonic
**"IQVR-DEC"** (Job Status Flow)
- **I**nitializing → **Q**ueued → **V**alidating → **R**unning
- Then: **D**one, **E**rror, or **C**ancelled

#### 6. ⚡ Quick Check

**Q: What JobStatus value indicates a job completed successfully?**

<details>
<summary>Answer</summary>

**A**: `JobStatus.DONE`

Other final states are ERROR and CANCELLED.
</details>

---

## 🔧 PrimitiveResult & BitArray (EXAM CRITICAL!)

### Overview
Understanding result structures is essential - PrimitiveResult contains PubResults, and Sampler results use BitArray.

---

### 🔹 Result Structure Hierarchy

#### 1. Definition
`PrimitiveResult` is the top-level container returned by primitives. It holds one `PubResult` per submitted PUB (Primitive Unified Bloc).

#### 2. Visual Reference

```
job.result() → PrimitiveResult
              └── PubResult[0]  (for first PUB)
                  ├── metadata (dict)
                  └── data (DataBin)
                      ├── evs (Estimator) / meas (Sampler)
                      ├── stds (Estimator)
                      └── ... other fields
              └── PubResult[1]  (for second PUB)
              └── ... 
```

#### 3. Implementation

**Estimator Results**
```python
from qiskit_ibm_runtime import EstimatorV2 as Estimator

job = estimator.run([pub1, pub2])
result = job.result()  # PrimitiveResult

# Access each PUB's result
pub_result_0 = result[0]  # PubResult for pub1
pub_result_1 = result[1]  # PubResult for pub2

# Estimator DataBin
data = pub_result_0.data
evs = data.evs        # Expectation values (np.ndarray)
stds = data.stds      # Standard deviations (np.ndarray)

print(f"⟨O⟩ = {evs} ± {stds}")
```

**Sampler Results**
```python
from qiskit_ibm_runtime import SamplerV2 as Sampler

job = sampler.run([pub])
result = job.result()

# Access BitArray (stored under classical register name)
pub_result = result[0]
bit_array = pub_result.data.meas  # Or data.c, data.cr, etc.

# BitArray properties
print(f"Shape: {bit_array.shape}")
print(f"Num shots: {bit_array.num_shots}")
print(f"Num bits: {bit_array.num_bits}")
```

#### 4. ⚠️ Trap Alert

**Trap: Using wrong register name for BitArray**
- ❌ **Wrong**: `result[0].data.counts` (doesn't exist!)
- ✅ **Correct**: `result[0].data.meas` or the actual register name

```python
# Register name depends on how circuit was created
qc.measure_all()        # → data.meas
qc.measure(q, c)        # → data.c (or register name)

# Named registers
cr = ClassicalRegister(2, 'my_reg')
# → data.my_reg
```

#### 5. 🧠 Mnemonic
**"PUB = Primitive Unified Bloc"**
- Each PUB → One PubResult
- Estimator: `.data.evs` and `.data.stds`
- Sampler: `.data.<register_name>` (BitArray)

#### 6. ⚡ Quick Check

**Q: How do you access expectation values from an Estimator result?**

<details>
<summary>Answer</summary>

**A**: `result[0].data.evs`

The `evs` attribute contains the expectation values as a numpy array.
</details>

---

### 🔹 BitArray Methods (EXAM TESTED!)

#### 1. Definition
BitArray is Qiskit's container for measurement shot data, with methods to convert between formats.

#### 2. Visual Reference

```
BitArray (1024 shots, 2 bits)
│
├── get_counts()      → {'00': 512, '11': 512}
├── get_bitstrings()  → ['00', '11', '00', ...]
├── get_int_counts()  → {0: 512, 3: 512}
├── slice_bits([0])   → BitArray (partial qubits)
└── slice_shots(range(100)) → BitArray (fewer shots)
```

#### 3. Implementation

```python
bit_array = result[0].data.meas

# Method 1: get_counts() - Dict of bitstring frequencies
counts = bit_array.get_counts()
# {'00': 512, '01': 10, '10': 8, '11': 494}

# Method 2: get_bitstrings() - List of shot results
bitstrings = bit_array.get_bitstrings()
# ['00', '11', '00', '11', '01', ...]  (one per shot)

# Method 3: get_int_counts() - Integer representation
int_counts = bit_array.get_int_counts()
# {0: 512, 1: 10, 2: 8, 3: 494}

# Method 4: slice_bits() - Extract specific bits
partial = bit_array.slice_bits([0, 1])
partial_counts = partial.get_counts()

# Method 5: slice_shots() - Subset of shots
first_100 = bit_array.slice_shots(range(100))
```

**Conversion Quick Reference**
| Method | Returns | Use Case |
|--------|---------|----------|
| `get_counts()` | `dict[str, int]` | Standard analysis |
| `get_bitstrings()` | `list[str]` | Shot-by-shot analysis |
| `get_int_counts()` | `dict[int, int]` | Numerical processing |
| `slice_bits([i,j])` | `BitArray` | Partial qubit data |
| `slice_shots(range)` | `BitArray` | Subset of shots |

#### 4. ⚠️ Trap Alert

**Trap: Confusing get_counts() vs get_int_counts()**
- `get_counts()`: Keys are bitstrings `'11'`
- `get_int_counts()`: Keys are integers `3`

```python
# Same data, different formats
counts = bit_array.get_counts()
# {'00': 500, '11': 524}

int_counts = bit_array.get_int_counts()
# {0: 500, 3: 524}  # '11' binary = 3 decimal
```

**Trap: Bit ordering**
- Qiskit uses **little-endian**: `q[0]` is rightmost bit
- `'01'` means q[0]=1, q[1]=0

#### 5. 🧠 Mnemonic
**"Counts, Strings, Ints, Slice"**
- **C**ounts: Dictionary frequencies
- **S**trings: Individual shots list
- **I**nts: Integer keys
- **Slice**: Partial data extraction

#### 6. ⚡ Quick Check

**Q: What method converts BitArray to a dictionary with integer keys?**

<details>
<summary>Answer</summary>

**A**: `bit_array.get_int_counts()`

Returns `{0: count, 1: count, ...}` where keys are decimal values of bitstrings.
</details>

---

### 🔹 Multiple Classical Registers

#### 1. Definition
When a circuit has multiple classical registers, each appears as a separate BitArray in the result.

#### 2. Implementation

```python
from qiskit import QuantumCircuit, ClassicalRegister

# Circuit with multiple registers
cr_alpha = ClassicalRegister(2, 'alpha')
cr_beta = ClassicalRegister(2, 'beta')
qc = QuantumCircuit(4, cr_alpha, cr_beta)

qc.h(range(4))
qc.measure([0, 1], cr_alpha)
qc.measure([2, 3], cr_beta)

# Access each register separately
result = sampler.run([(qc,)]).result()
data = result[0].data

alpha_counts = data.alpha.get_counts()
beta_counts = data.beta.get_counts()
```

#### 3. ⚠️ Trap Alert

**Trap: Expecting combined counts with multiple registers**
- ❌ **Wrong**: `data.meas` when using named registers
- ✅ **Correct**: `data.<register_name>` for each register

#### 4. ⚡ Quick Check

**Q: If you have `ClassicalRegister(2, 'cr')`, how do you access its counts?**

<details>
<summary>Answer</summary>

**A**: `result[0].data.cr.get_counts()`

The register name becomes the attribute name on the DataBin.
</details>

---

## 🔧 Options Configuration (EXAM TESTED!)

### Overview
The Options class controls HOW circuits execute: optimization level, error mitigation, and shot count.

---

### 🔹 The Options Class

#### 1. Definition
Options is a configuration object that sets execution parameters for primitives (Sampler, Estimator).

#### 2. Analogy + Intuition
**Real-World Analogy**: Like camera settings before taking a photo:
- **ISO** (optimization_level): Quality vs speed
- **Flash** (resilience_level): Compensate for noise
- **Shots** (execution.shots): How many samples to average

#### 3. Implementation

```python
from qiskit_ibm_runtime import Options

options = Options()
options.optimization_level = 3        # 0-3
options.resilience_level = 1          # 0-2
options.execution.shots = 4096

# Use with primitives
sampler = Sampler(backend=backend, options=options)
```

**Key Options**
| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `optimization_level` | 0-3 | 2 | Transpiler optimization |
| `resilience_level` | 0-2 | 0 | Error mitigation |
| `execution.shots` | int | 4000 | Measurement count |
| `dynamical_decoupling.enable` | bool | False | DD sequences |

#### 4. Resilience Levels

```
Level 0: No error mitigation
- Raw hardware results
- Fastest execution

Level 1: M3 (Matrix-free Measurement Mitigation)
- Corrects readout errors
- ~20% overhead

Level 2: ZNE + M3 (Zero-Noise Extrapolation)
- Estimates zero-noise result
- ~3-5× overhead
```

**Configuration Scenarios**
```python
# Rapid Prototyping
options.optimization_level = 1
options.resilience_level = 0
options.execution.shots = 1024

# Production
options.optimization_level = 3
options.resilience_level = 1
options.execution.shots = 4096

# Maximum Quality
options.optimization_level = 3
options.resilience_level = 2
options.execution.shots = 8192
```

**Options Decision Tree (EXAM CRITICAL!)**
```
┌─ What's your priority? ──────────────────────┐
│  Speed → optimization_level=1, resilience=0  │
│  Quality → optimization_level=3, resilience=1│
│  Research → optimization_level=3, resilience=2│
└───────────────────────────────────────────────┘

┌─ What hardware? ─────────────────────────────┐
│  Simulator → resilience_level=0              │
│  Real hardware → resilience_level=1          │
│  Noisy hardware → resilience_level=2         │
└───────────────────────────────────────────────┘

┌─ How precise? ───────────────────────────────┐
│  Quick test → shots=1024                     │
│  Standard → shots=4096                       │
│  High precision → shots=8192+                │
└───────────────────────────────────────────────┘
```

**Visual: Error Mitigation Effect**
```
Without Mitigation (Level 0):     With M3 (Level 1):
    
 Ideal: 50% |00⟩, 50% |11⟩       Ideal: 50% |00⟩, 50% |11⟩
 
 |00⟩: ████████ 45%              |00⟩: █████████ 49%
 |01⟩: █ 3%                      |01⟩:  1%
 |10⟩: █ 2%                      |10⟩:  <1%
 |11⟩: ████████ 50%              |11⟩: ██████████ 50%
 
 Readout errors visible!          Corrected to ideal!
```

#### 5. ⚠️ Trap Alert

**Trap: Confusing optimization_level locations**
- ❌ **Wrong**: `options.transpilation.optimization_level`
- ✅ **Correct**: `options.optimization_level`

```python
# ✅ CORRECT
options.optimization_level = 3

# ❌ This is different (skip transpilation entirely)
options.transpilation.skip_transpilation = True
```

#### 6. 🧠 Mnemonic
**"ORS" = Optimization, Resilience, Shots**
- **O**ptimization: How smart is compilation?
- **R**esilience: How much error correction?
- **S**hots: How many measurements?

#### 7. ⚡ Quick Check

**Q: What resilience_level applies M3 measurement error mitigation?**

<details>
<summary>Answer</summary>

**A**: Level 1

- Level 0: No mitigation
- Level 1: M3 (measurement mitigation)
- Level 2: M3 + ZNE (zero-noise extrapolation)
</details>

---

## 🔧 Backend Target (V2 API)

### Overview
The Target object in Backend V2 API provides unified access to all hardware properties.

---

### 🔹 V1 vs V2 API

#### 1. Definition
Backend V2 consolidates hardware information into a single `target` object, replacing scattered V1 methods.

#### 2. Visual Reference

```
V1 API (Legacy):               V2 API (Current):
┌──────────────────────┐      ┌──────────────────────┐
│ Backend              │      │ Backend V2           │
│  ├─ configuration() │      │  └─ target           │
│  ├─ properties()    │      │      ├─ operations   │
│  ├─ defaults()      │      │      ├─ qargs        │
│  └─ coupling_map    │      │      ├─ properties   │
└──────────────────────┘      │      └─ instructions │
Multiple scattered methods     └──────────────────────┘
                              Single unified interface
```

#### 3. Code Comparison

| Feature | V1 (Deprecated) | V2 (Current) |
|---------|-----------------|--------------|
| Basis gates | `backend.configuration().basis_gates` | `backend.target.operation_names` |
| Coupling map | `backend.configuration().coupling_map` | `backend.target.build_coupling_map()` |
| Gate support | Manual parsing | `target.instruction_supported('cx', (0,1))` |
| Gate error | `backend.properties().gate_property(...)` | `target['cx'][(0,1)].error` |
| Qubit T1 | `backend.properties().qubit_property(...)` | `target.qubit_properties[0].t1` |
| Num qubits | `backend.configuration().n_qubits` | `backend.num_qubits` |

#### 4. Implementation

```python
backend = service.backend('ibm_brisbane')
target = backend.target

# Operations
print(target.operation_names)  # ['cx', 'rz', 'sx', 'x', ...]

# Check instruction support
target.instruction_supported('cx', (0, 1))  # True/False

# Gate properties
cx_props = target['cx'][(0, 1)]
print(f"Error: {cx_props.error}")
print(f"Duration: {cx_props.duration} dt")

# Qubit properties
qubit_props = target.qubit_properties[0]
print(f"T1: {qubit_props.t1}")
print(f"T2: {qubit_props.t2}")
print(f"Frequency: {qubit_props.frequency}")
```

#### 5. ⚠️ Trap Alert

**Trap: Using V1 API methods on V2 backends**
- ❌ **Wrong**: `backend.configuration().basis_gates`
- ✅ **Correct**: `backend.target.operation_names`

#### 6. 🧠 Mnemonic
**"TARGET"** - What Target provides:
- **T**iming (gate durations)
- **A**vailability (gate support)
- **R**eliability (error rates)
- **G**eometry (coupling map)
- **E**nvironment (T1, T2, frequency)
- **T**ruth (single source)

#### 7. ⚡ Quick Check

**Q: How do you check if CX is supported between qubits 0 and 1 using V2 API?**

<details>
<summary>Answer</summary>

**A**: `backend.target.instruction_supported('cx', (0, 1))`

Returns True if the instruction is natively supported on those qubits.
</details>

---

### 🔹 Qubit Properties: T1, T2, Frequency

#### 1. Definition
- **T1 (Relaxation)**: Time for |1⟩ to decay to |0⟩ (energy loss)
- **T2 (Dephasing)**: Time for superposition to lose coherence (phase scramble)
- **Frequency**: Resonant frequency for qubit control (GHz)

#### 2. Analogy + Intuition

**T1 = "Battery Life"** 🔋
- How long qubit stays "charged" (in |1⟩)
- Longer T1 = deeper circuits possible

**T2 = "Tuning Fork"** 🎵
- How long qubit stays "in tune" (coherent)
- Longer T2 = better superpositions
- Always T2 ≤ 2×T1

**Frequency = "Radio Station"** 📻
- Each qubit has unique frequency
- Used to address specific qubits

#### 3. Visual Reference

```
┌─────────────────────────────────────────────────────────┐
│           QUBIT HEALTH CERTIFICATE                       │
├─────────────────────────────────────────────────────────┤
│  T1 (Energy Stamina)     🔋 How long it stays "charged"  │
│  ├─ Like: Battery life                                   │
│  └─ Typical: 50-200 μs                                   │
│                                                          │
│  T2 (Phase Stability)    ⏱️ How long it stays "in sync"  │
│  ├─ Like: Clock accuracy                                 │
│  └─ Typical: 50-150 μs (always ≤ 2×T1)                  │
│                                                          │
│  Frequency (Address)     📍 Its unique "phone number"    │
│  ├─ Like: Radio dial position                            │
│  └─ Typical: 4.5-5.5 GHz                                │
└─────────────────────────────────────────────────────────┘
```

#### 4. Implementation

```python
target = backend.target
qubit_props = target.qubit_properties[0]

t1 = qubit_props.t1  # e.g., 150e-6 seconds
t2 = qubit_props.t2  # e.g., 100e-6 seconds
freq = qubit_props.frequency  # e.g., 5.0e9 Hz

# Circuit duration check
circuit_time = transpiled.depth() * 50e-9  # ~50ns per gate
if circuit_time > t2 * 0.1:  # 10% rule
    print("⚠️ Circuit may suffer decoherence!")
```

#### 5. ⚠️ Trap Alert

**Trap: Thinking T2 can exceed 2×T1**
- ❌ **Wrong**: T2 = 300μs when T1 = 100μs
- ✅ **Correct**: T2 ≤ 2×T1 (always!)
- 🔍 **Why**: Phase loss includes energy loss

#### 6. 🧠 Mnemonic
**"T2 ≤ Two Times T1"**
- T**2** can never be more than **2**×T1
- Phase loss always accompanies energy loss

#### 7. ⚡ Quick Check

**Q: If T1 = 100μs, what's the maximum possible T2?**

<details>
<summary>Answer</summary>

**A**: 200μs (2 × T1)

T2 ≤ 2×T1 is a fundamental physical constraint.
</details>

---

## 🔧 Coupling Maps

### Overview
Coupling maps describe which qubit pairs can directly perform two-qubit gates.

---

### 🔹 Coupling Map Basics

#### 1. Definition
A coupling map is a directed graph showing physical connections between qubits on the quantum chip.

#### 2. Analogy + Intuition
**Real-World Analogy**: Road network between cities
- **Qubits** = Cities
- **Connections** = Roads  
- **CX gate** = Traveling between cities
- **No connection** = Need detour (SWAP gates)

#### 3. Visual Reference

```
Example: Linear Chain
Coupling Map: [[0,1], [1,2], [2,3]]

Physical Layout:
    q0 ── q1 ── q2 ── q3

Supported Operations:
✅ CX(0, 1) - Direct
✅ CX(1, 2) - Direct  
❌ CX(0, 3) - Need routing through q1, q2
```

```
Example: T-Shape
         q0
         │
    q2 ─ q1 ─ q3

✅ CX(0, 1), CX(1, 2), CX(1, 3) - Direct
❌ CX(0, 3), CX(2, 3) - Need q1 as intermediary
```

#### 4. Implementation

```python
# Get coupling map
coupling_map = backend.target.build_coupling_map()

# Check distance
distance = coupling_map.distance(0, 4)
if distance == 1:
    print("Direct neighbors")
else:
    print(f"Need {distance - 1} hops")

# Visualize
from qiskit.visualization import plot_coupling_map
plot_coupling_map(backend)
```

**Simulating Coupling Maps Locally**
```python
from qiskit_aer import AerSimulator
from qiskit.transpiler import CouplingMap

# Custom coupling map
custom_map = CouplingMap([[0,1], [1,2], [2,3]])
sim = AerSimulator(coupling_map=custom_map)

# Transpile with constraints
transpiled = transpile(qc, backend=sim, optimization_level=3)
```

#### 5. ⚠️ Trap Alert

**Trap: Assuming bidirectional connections**
- ❌ **Wrong**: If [0,1] exists, [1,0] must exist
- ✅ **Correct**: Direction matters - check both!
- 🔍 **Why**: CX(0,1) ≠ CX(1,0) in hardware

```python
# Check directionality
has_01 = [0, 1] in coupling_map.get_edges()
has_10 = [1, 0] in coupling_map.get_edges()
print(f"CX(0,1): {has_01}, CX(1,0): {has_10}")
```

#### 6. 🧠 Mnemonic
**"Coupling Map = Road Map"**
- Direct connection = Highway (1 CX)
- No connection = Dirt road (many SWAPs)
- Transpiler = GPS (finds best route)

**"SWAP = 3 CX"**
- Each SWAP costs 3 CNOT gates
- Each CNOT ~1% error
- 1 SWAP ≈ 3% error accumulation!

#### 7. ⚡ Quick Check

**Q: Why does transpiling CX(0, 5) increase circuit depth when qubits 0 and 5 aren't connected?**

<details>
<summary>Answer</summary>

**A**: SWAP gates must be inserted to route the operation through connected qubits.

Each SWAP = 3 CNOTs, so routing can dramatically increase depth and errors.
</details>

---

## 🔧 Broadcasting Rules

### Overview
Broadcasting determines how parameter arrays and observable arrays combine in primitives.

---

### 🔹 Broadcasting Patterns

#### 1. Definition
Broadcasting (from NumPy) allows primitives to process multiple parameter sets and observables efficiently without explicit loops.

#### 2. Visual Reference

```
Pattern 1: Broadcast Single Observable
┌─────────────────────────────────────────┐
│ Observable: [ZZ]           shape ()     │
│ Parameters: [θ₀, θ₁, θ₂, θ₃, θ₄]  (5,) │
│                                         │
│ Result: [⟨ZZ⟩(θ₀), ⟨ZZ⟩(θ₁), ...]  (5,)│
└─────────────────────────────────────────┘

Pattern 2: Zip (One-to-One)
┌─────────────────────────────────────────┐
│ Observables: [O₀, O₁, O₂, O₃, O₄]  (5,)│
│ Parameters:  [θ₀, θ₁, θ₂, θ₃, θ₄]  (5,)│
│                                         │
│ Result: [⟨O₀⟩(θ₀), ⟨O₁⟩(θ₁), ...]  (5,)│
└─────────────────────────────────────────┘

Pattern 3: Outer Product
┌─────────────────────────────────────────┐
│ Observables: shape (3, 1)               │
│ Parameters: shape (1, 5)                │
│                                         │
│ Result: shape (3, 5) - all combinations │
└─────────────────────────────────────────┘
```

#### 3. Implementation

```python
# Pattern 1: Single observable, multiple params
params = np.linspace(0, np.pi, 5)  # (5,)
observable = SparsePauliOp("ZZ")   # scalar
pub = (qc, observable, params)
# Result: 5 expectation values

# Pattern 2: Zip (matching shapes)
observables = [SparsePauliOp("ZZ"), SparsePauliOp("XX")]  # (2,)
params = [0.1, 0.2]  # (2,)
pub = (qc, observables, params)
# Result[0] = ⟨ZZ⟩(0.1), Result[1] = ⟨XX⟩(0.2)

# Pattern 3: Outer product
observables = [[SparsePauliOp("ZZ")], [SparsePauliOp("XX")]]  # (2,1)
params = np.array([0.1, 0.2, 0.3]).reshape(1, 3)  # (1,3)
pub = (qc, observables, params)
# Result: (2, 3) - all 6 combinations
```

#### 4. ⚠️ Trap Alert

**Trap: Incompatible shapes**
- ❌ **Wrong**: params shape (5,), observables shape (3,)
- ✅ **Correct**: Shapes must be broadcastable (equal or one is 1)

```python
# ❌ ERROR: 5 and 3 incompatible
params = np.random.uniform(size=(5,))
observables = [SparsePauliOp("ZZ")] * 3

# ✅ Fix: reshape for outer product
params = np.random.uniform(size=(1, 5))      # (1, 5)
observables = [[o] for o in observables]      # (3, 1)
# Broadcasts to (3, 5)
```

#### 5. 🧠 Mnemonic
**"Zip or Product - Check Your Shapes"**
- Same shape = Zip (paired)
- (1,N) × (M,1) = Outer product (all pairs)

#### 6. ⚡ Quick Check

**Q: If parameters have shape (1, 5) and observables have shape (3, 1), what's the result shape?**

<details>
<summary>Answer</summary>

**A**: (3, 5)

Broadcasting creates an outer product of all 15 combinations.
</details>

---

## 📊 Consolidated Review: Main Topics

### Comparison Table

| Topic | Key Method/Class | Default | Common Trap |
|-------|-----------------|---------|-------------|
| **RuntimeService** | `QiskitRuntimeService()` | - | Forgetting save_account() |
| **Transpilation** | `transpile(qc, backend)` | level=2 | Non-deterministic |
| **Opt Level** | `optimization_level` | 2 | Higher isn't always better |
| **Sessions** | `Session(backend=...)` | - | Using `session=` not `mode=` |
| **JobStatus** | `job.status()` | - | Not checking before result() |
| **Options** | `Options()` | shots=4000 | Wrong attribute path |
| **BitArray** | `data.meas.get_counts()` | - | Wrong register name |
| **Target** | `backend.target` | - | Using V1 API methods |
| **T1/T2** | `qubit_properties[i].t1` | - | Thinking T2 > 2×T1 |
| **Coupling** | `build_coupling_map()` | - | Assuming bidirectional |

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 4 - QUICK REFERENCE                                     │
├─────────────────────────────────────────────────────────────────┤
│ SERVICE:                                                         │
│   service = QiskitRuntimeService()                               │
│   backend = service.backend('ibm_brisbane')                     │
│                                                                  │
│ TRANSPILE:                                                       │
│   transpiled = transpile(qc, backend, optimization_level=3)     │
│   Levels: 0=Debug, 1=Fast, 2=Default, 3=Best                    │
│                                                                  │
│ OPTIONS:                                                         │
│   options = Options()                                            │
│   options.optimization_level = 3  (0-3)                         │
│   options.resilience_level = 1    (0-2, M3)                     │
│   options.execution.shots = 4096                                │
│                                                                  │
│ SESSIONS:                                                        │
│   with Session(backend=backend) as session:                     │
│       sampler = Sampler(mode=session)                           │
│                                                                  │
│ JOBS:                                                            │
│   job.status()  →  JobStatus.DONE/ERROR/CANCELLED               │
│   job.result()  →  PrimitiveResult                              │
│   service.job(job_id)  →  Retrieve later                        │
│                                                                  │
│ RESULTS:                                                         │
│   result[0].data.evs      →  Estimator expectation values       │
│   result[0].data.meas     →  Sampler BitArray                   │
│   bit_array.get_counts()  →  {'00': 512, '11': 512}             │
│   bit_array.get_int_counts() → {0: 512, 3: 512}                 │
│                                                                  │
│ TARGET (V2):                                                     │
│   target = backend.target                                        │
│   target.operation_names  →  Basis gates                        │
│   target.instruction_supported('cx', (0,1))                     │
│   target.qubit_properties[0].t1, .t2, .frequency                │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONICS:                                                       │
│ • "SAVE before SERVE" - save_account() before service           │
│ • "0=Zero, 1=One, 2=Two-way, 3=Three+" - opt levels             │
│ • "ORS" - Options = Optimization, Resilience, Shots             │
│ • "TARGET" - Timing, Availability, Reliability, Geometry...     │
│ • "T2 ≤ 2×T1" - Always true!                                    │
│ • "SWAP = 3 CX" - Routing is expensive!                         │
│ • "ILRTOS" - Init, Layout, Routing, Translation, Opt, Sched     │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAPS:                                                       │
│ • transpile() is NOT deterministic (use seed)                   │
│ • Primitives auto-transpile (manual not required)               │
│ • mode= not session= (v0.24.0+)                                 │
│ • apply_layout() for observables after transpile                │
│ • T2 can NEVER exceed 2×T1                                      │
│ • Coupling map direction matters                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ MASTER TRAP LIST

### Trap Summary Table

| # | Topic | Trap | ❌ Wrong | ✅ Correct | Mnemonic |
|---|-------|------|----------|-----------|----------|
| 1 | Service | No credentials | `QiskitRuntimeService()` without save | `save_account()` first | "SAVE before SERVE" |
| 2 | Transpile | Deterministic | Same output every time | Use `seed_transpiler` | "Seed for Same" |
| 3 | Transpile | Required for primitives | Always manual transpile | Primitives auto-transpile | - |
| 4 | Options | Wrong path | `options.transpilation.optimization_level` | `options.optimization_level` | - |
| 5 | Sessions | Old parameter | `Estimator(session=session)` | `Estimator(mode=session)` | "mode is Modern" |
| 6 | Jobs | No status check | `job.result()` immediately | Check `job.done()` first | - |
| 7 | Target | V1 API | `backend.configuration()` | `backend.target` | "TARGET is Truth" |
| 8 | T1/T2 | T2 > 2×T1 | Assume any T2 value | T2 ≤ 2×T1 always | "T2 ≤ Two×T1" |
| 9 | Layout | No observable remap | Use original observable | `obs.apply_layout(transpiled.layout)` | - |
| 10 | Coupling | Bidirectional | [0,1] means [1,0] exists | Check both directions | - |
| 11 | SWAP | Cheap | SWAP is 1 gate | SWAP = 3 CNOTs | "SWAP = 3 CX" |
| 12 | Broadcast | Incompatible shapes | (5,) and (3,) arrays | Reshape for broadcast | - |
| 13 | BitArray | Wrong register | `data.counts` | `data.meas` or register name | - |
| 14 | BitArray | get_counts vs int | Confusing formats | `get_counts()` = str keys, `get_int_counts()` = int keys | - |
| 15 | Bit Order | Big endian | q[0] is leftmost | q[0] is **rightmost** (little-endian) | - |

---

## 📝 PRACTICE EXAM

### Part A: Quick Fire (10 Questions)

**Q1**: What is the default optimization_level for transpile()?
<details><summary>Answer</summary>

**A**: 2 (Medium optimization)
</details>

**Q2**: Which resilience_level applies M3 measurement error mitigation?
<details><summary>Answer</summary>

**A**: Level 1 (Level 0=none, Level 2=M3+ZNE)
</details>

**Q3**: If T1 = 80μs, what's the maximum possible T2?
<details><summary>Answer</summary>

**A**: 160μs (2 × T1)
</details>

**Q4**: How many CNOT gates does a SWAP decompose into?
<details><summary>Answer</summary>

**A**: 3 CNOT gates
</details>

**Q5**: Which execution mode provides reserved QPU access for VQE?
<details><summary>Answer</summary>

**A**: Session mode
</details>

**Q6**: What parameter ensures transpilation reproducibility?
<details><summary>Answer</summary>

**A**: `seed_transpiler` (e.g., `transpile(qc, backend, seed_transpiler=42)`)
</details>

**Q7**: In V2 API, how do you get the basis gates from a backend?
<details><summary>Answer</summary>

**A**: `backend.target.operation_names`
</details>

**Q8**: What's the correct parameter for passing sessions in Runtime v0.24.0+?
<details><summary>Answer</summary>

**A**: `mode=session` (not `session=session`)
</details>

**Q9**: What are the 6 stages of the transpilation pipeline in order?
<details><summary>Answer</summary>

**A**: Init → Layout → Routing → Translation → Optimization → Scheduling (ILRTOS)
</details>

**Q10**: What method retrieves a job by its ID from the service?
<details><summary>Answer</summary>

**A**: `service.job(job_id)`
</details>

### Part B: Code Analysis (5 Questions)

**Q11**: What's wrong with this code?
```python
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')
```
<details><summary>Answer</summary>

**A**: Missing `save_account()` - credentials must be saved first (unless previously saved).
</details>

**Q12**: What's the issue here?
```python
transpiled = pm.run(circuit)
pub = (transpiled, observable)  # SparsePauliOp("ZZ")
estimator.run([pub])
```
<details><summary>Answer</summary>

**A**: Observable not remapped after transpilation. Should use:
`mapped_obs = observable.apply_layout(transpiled.layout)`
</details>

**Q13**: Identify the trap:
```python
qc1 = transpile(qc, backend, optimization_level=3)
qc2 = transpile(qc, backend, optimization_level=3)
assert qc1 == qc2  # Will this pass?
```
<details><summary>Answer</summary>

**A**: This may FAIL - transpilation is NOT deterministic. Use `seed_transpiler=42` for reproducibility.
</details>

**Q14**: What's the issue with this Options configuration?
```python
options = Options()
options.transpilation.optimization_level = 3
```
<details><summary>Answer</summary>

**A**: Wrong attribute path. Should be `options.optimization_level = 3` (not under `transpilation`).
</details>

**Q15**: What will this code print?
```python
from qiskit.providers import JobStatus
job = sampler.run([qc])
if job.status() == JobStatus.DONE:
    print("Finished!")
else:
    print("Not done yet")
```
<details><summary>Answer</summary>

**A**: Almost certainly "Not done yet" - jobs start in INITIALIZING state, not DONE. The job needs time to complete.
</details>

### Part C: Real-World Scenarios (3 Questions)

**Q16**: You're running a VQE optimization that requires 500 iterations. Each iteration submits a job to measure the cost function. What execution mode should you use and why?

<details><summary>Answer</summary>

**A**: **Session mode** with the Estimator primitive.

```python
with Session(backend=backend) as session:
    estimator = Estimator(mode=session)
    for i in range(500):
        # VQE iteration - reserved access prevents queuing
        job = estimator.run([(circuit, observable, params)])
        result = job.result()
        cost = result[0].data.evs
        params = optimizer.step(cost)  # Update parameters
```

**Why Sessions?**
- Reserved QPU access between jobs
- No re-queuing overhead for 500 iterations
- Maintains consistent hardware conditions
- Ideal for iterative algorithms with parameter updates
</details>

**Q17**: Your transpiled circuit has depth 500, but the backend qubits have T2 times around 100μs and gate durations of ~50ns per gate. Should you proceed with execution? Explain your analysis.

<details><summary>Answer</summary>

**A**: **No - the circuit will likely fail due to decoherence.**

**Analysis:**
```python
# Approximate circuit time
gate_time = 50e-9  # 50 nanoseconds
circuit_depth = 500
circuit_time = depth * gate_time  # = 25 microseconds

# T2 comparison
t2 = 100e-6  # 100 microseconds
circuit_to_t2_ratio = circuit_time / t2  # = 0.25 (25%)
```

**10% Rule**: Circuits should complete within ~10% of T2 for reliable results.
- Your circuit takes 25% of T2 → Expect significant decoherence errors

**Solutions:**
1. Increase optimization_level to reduce depth
2. Use resilience_level=2 for error mitigation
3. Select qubits with longer T2 times
4. Simplify the algorithm if possible
</details>

**Q18**: You need to transpile 100 circuits to submit as a batch job. All circuits should produce identical transpilation results when re-run later. What parameters must you set?

<details><summary>Answer</summary>

**A**: Set `seed_transpiler` for reproducibility:

```python
from qiskit import transpile

# Deterministic transpilation for all circuits
transpiled_circuits = transpile(
    circuits,
    backend=backend,
    optimization_level=3,
    seed_transpiler=42  # CRITICAL for reproducibility
)

# Submit as batch
with Batch(backend=backend) as batch:
    sampler = Sampler(mode=batch)
    job = sampler.run(transpiled_circuits)
```

**Why `seed_transpiler`?**
- Transpilation involves randomized algorithms (layout selection, routing decisions)
- Without a seed, same circuit → different outputs each run
- `seed_transpiler` fixes the random number generator
- Essential for benchmarking, debugging, and reproducible research

**Note**: Even with the seed, changing Qiskit version or backend calibration may produce different results.
</details>

---

## ✅ Key Takeaways

### 📚 Concept Checklist
```
□ QiskitRuntimeService is the gateway to IBM Quantum backends
□ Credentials: save_account() stores token persistently
□ Backend selection: service.backend('name') or service.least_busy()
□ Transpilation converts abstract circuits to hardware-executable form
□ 6-stage pipeline: Init → Layout → Routing → Translation → Optimization → Scheduling
□ optimization_level: 0=debug, 1=fast, 2=default, 3=best
□ resilience_level: 0=none, 1=M3 mitigation, 2=M3+ZNE
□ Session mode: reserved access for iterative algorithms (VQE)
□ Batch mode: parallel execution for independent circuits
□ Job mode: single submission (default)
□ JobStatus flow: INITIALIZING → QUEUED → VALIDATING → RUNNING → DONE
□ Backend V2 API: target object consolidates all hardware info
□ T1 = relaxation time (energy decay), T2 = dephasing time (coherence loss)
□ Physical constraint: T2 ≤ 2×T1 (always true!)
□ Coupling map = connectivity graph for 2-qubit gates
□ SWAP gate = 3 CNOTs (expensive routing overhead)
□ BitArray: get_counts() returns string keys, get_int_counts() returns int keys
□ Broadcasting: parameter/observable shapes must be compatible
```

### 💻 Code Pattern Checklist
```
□ service = QiskitRuntimeService() connects to IBM Quantum
□ QiskitRuntimeService.save_account(channel='ibm_quantum', token='...') saves credentials
□ backend = service.backend('ibm_brisbane') selects specific backend
□ backend = service.least_busy(simulator=False) selects best available
□ transpiled = transpile(qc, backend, optimization_level=3) compiles circuit
□ transpile(..., seed_transpiler=42) ensures reproducibility
□ with Session(backend=backend) as session: creates session context
□ sampler = Sampler(mode=session) attaches primitive to session
□ options = Options() creates configuration object
□ options.optimization_level = 3 sets optimization (NOT options.transpilation.optimization_level)
□ options.resilience_level = 1 enables M3 mitigation
□ options.execution.shots = 8192 sets measurement count
□ job.status() returns JobStatus enum
□ job.done() returns True when complete
□ result = job.result() blocks until complete, returns PrimitiveResult
□ service.job(job_id) retrieves job by ID
□ target = backend.target accesses V2 hardware info
□ target.operation_names returns basis gates list
□ target.instruction_supported('cx', (0, 1)) checks gate availability
□ target.qubit_properties[0].t1 / .t2 / .frequency returns qubit properties
□ coupling_map = target.build_coupling_map() gets connectivity
□ result[0].data.meas returns BitArray (Sampler)
□ result[0].data.evs returns expectation values (Estimator)
□ bit_array.get_counts() returns {'00': 512, '11': 512}
□ bit_array.get_int_counts() returns {0: 512, 3: 512}
□ observable.apply_layout(transpiled.layout) remaps after transpilation
```

### ⚠️ Exam Trap Checklist
```
□ TRAP: Using QiskitRuntimeService() without save_account() first
□ TRAP: Assuming transpile() is deterministic (use seed_transpiler!)
□ TRAP: Manual transpilation before primitives (they auto-transpile)
□ TRAP: options.transpilation.optimization_level (wrong path!)
  → Use: options.optimization_level
□ TRAP: Estimator(session=session) is DEPRECATED
  → Use: Estimator(mode=session)
□ TRAP: Calling job.result() without checking job.done()
□ TRAP: Using V1 API: backend.configuration().basis_gates
  → Use V2: backend.target.operation_names
□ TRAP: Assuming T2 can exceed 2×T1 (impossible!)
□ TRAP: Not remapping observable after transpilation
  → Use: obs.apply_layout(transpiled.layout)
□ TRAP: Assuming coupling map is bidirectional
  → Check both [0,1] and [1,0] directions
□ TRAP: Treating SWAP as cheap (it's 3 CNOTs!)
□ TRAP: Incompatible broadcast shapes for params/observables
□ TRAP: Using data.counts instead of data.meas or register name
□ TRAP: Confusing get_counts() (strings) vs get_int_counts() (ints)
□ TRAP: Assuming q[0] is leftmost bit (it's rightmost - little-endian!)
□ TRAP: Higher optimization_level always better (sometimes slower, not better)
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 4 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🔑 "SAVE before SERVE"                                          │
│    save_account() → then QiskitRuntimeService()                 │
│                                                                  │
│ 🔢 "0=Zero, 1=One, 2=Two-way, 3=Three+"                         │
│    Opt Level 0: Zero optimization (debug)                       │
│    Opt Level 1: One-pass (fast)                                 │
│    Opt Level 2: Two-way (default, bidirectional)               │
│    Opt Level 3: Three+ passes (maximum)                        │
│                                                                  │
│ 🔧 "ILRTOS" - 6-Stage Transpilation Pipeline                    │
│    Init → Layout → Routing → Translation → Opt → Scheduling     │
│                                                                  │
│ 📊 "ORS" - Options Remember                                     │
│    O = Optimization level (0-3)                                 │
│    R = Resilience level (0-2)                                   │
│    S = Shots (default 4000)                                     │
│                                                                  │
│ 💼 "JBS" - Execution Modes                                      │
│    J = Job (single, default)                                    │
│    B = Batch (parallel, independent)                            │
│    S = Session (reserved, iterative)                            │
│                                                                  │
│ 📈 "IQVR-DEC" - JobStatus Flow                                  │
│    I → Q → V → R → (D | E | C)                                  │
│    INITIALIZING → QUEUED → VALIDATING → RUNNING →               │
│    (DONE | ERROR | CANCELLED)                                   │
│                                                                  │
│ 🎯 "TARGET" - What V2 Target Provides                           │
│    T = Timing (gate durations)                                  │
│    A = Availability (gate support)                              │
│    R = Reliability (error rates)                                │
│    G = Geometry (coupling map)                                  │
│    E = Environment (T1, T2, frequency)                          │
│    T = Truth (single source)                                    │
│                                                                  │
│ ⏱️ "T2 ≤ Two Times T1"                                          │
│    T2 can NEVER exceed 2 × T1 (physics!)                        │
│                                                                  │
│ 🔄 "SWAP = 3 CX"                                                 │
│    Each SWAP decomposes to 3 CNOTs                              │
│    Routing is EXPENSIVE! (~3% error per SWAP)                   │
│                                                                  │
│ 🆕 "mode is Modern"                                             │
│    Use mode=session, NOT session=session                        │
│                                                                  │
│ 🌱 "Seed for Same"                                              │
│    seed_transpiler=42 for reproducible results                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 4: RUN CIRCUITS ON BACKEND - ONE-PAGE SUMMARY             ║
║                      (15% of Exam - ~10 Questions)                     ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🔌 RUNTIME SERVICE                                                    ║
║  ├─ save_account() first, then QiskitRuntimeService()                 ║
║  ├─ backend = service.backend('ibm_brisbane')                         ║
║  └─ backend = service.least_busy(simulator=False)                     ║
║                                                                        ║
║  ⚙️ TRANSPILATION                                                      ║
║  ├─ transpile(qc, backend, optimization_level=3, seed_transpiler=42)  ║
║  ├─ Pipeline: Init → Layout → Routing → Translation → Opt → Sched     ║
║  ├─ Level 0: Debug │ Level 1: Fast │ Level 2: Default │ Level 3: Best ║
║  └─ NOT deterministic without seed_transpiler!                        ║
║                                                                        ║
║  📋 OPTIONS                                                            ║
║  ├─ options.optimization_level = 3  (NOT transpilation.opt...)        ║
║  ├─ options.resilience_level = 1  (0=none, 1=M3, 2=M3+ZNE)           ║
║  └─ options.execution.shots = 4096                                    ║
║                                                                        ║
║  🔄 EXECUTION MODES                                                    ║
║  ├─ Job: Single submission (default)                                  ║
║  ├─ Batch: Parallel independent circuits                              ║
║  └─ Session: Reserved access for iterative (VQE) - mode=session       ║
║                                                                        ║
║  📊 JOB STATUS FLOW                                                    ║
║  INITIALIZING → QUEUED → VALIDATING → RUNNING → DONE/ERROR/CANCELLED ║
║  └─ Check job.done() before job.result()                              ║
║                                                                        ║
║  🎯 BACKEND TARGET (V2)                                                ║
║  ├─ target = backend.target (NOT backend.configuration()!)            ║
║  ├─ target.operation_names → basis gates                              ║
║  ├─ target.instruction_supported('cx', (0,1)) → availability          ║
║  ├─ target.qubit_properties[i].t1, .t2, .frequency                    ║
║  └─ target.build_coupling_map() → connectivity                        ║
║                                                                        ║
║  ⏱️ QUBIT PROPERTIES                                                   ║
║  ├─ T1: Energy relaxation time (~100μs)                               ║
║  ├─ T2: Phase coherence time (T2 ≤ 2×T1 ALWAYS!)                      ║
║  └─ Rule: Circuit time < 10% of T2 for reliable results               ║
║                                                                        ║
║  🗺️ COUPLING MAPS                                                      ║
║  ├─ Defines which qubits can do 2-qubit gates directly                ║
║  ├─ Direction matters! [0,1] ≠ [1,0]                                  ║
║  └─ SWAP = 3 CNOTs (routing is expensive!)                            ║
║                                                                        ║
║  📦 RESULTS                                                            ║
║  ├─ Sampler: result[0].data.meas → BitArray                           ║
║  ├─ Estimator: result[0].data.evs → expectation values                ║
║  ├─ get_counts() → {'00': 512, '11': 512}                             ║
║  └─ get_int_counts() → {0: 512, 3: 512}                               ║
║                                                                        ║
║  ⚠️ TOP 5 EXAM TRAPS                                                   ║
║  1. transpile() is NOT deterministic (use seed_transpiler)            ║
║  2. mode=session (NOT session=session) for Runtime v0.24.0+           ║
║  3. options.optimization_level (NOT options.transpilation...)         ║
║  4. T2 ≤ 2×T1 (ALWAYS - physics constraint!)                          ║
║  5. SWAP = 3 CNOTs (routing adds significant overhead)                ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 📁 Files in This Section

| Notebook | Topics Covered |
|----------|----------------|
| `runtime_service.ipynb` | QiskitRuntimeService, authentication, backend selection |
| `transpilation.ipynb` | transpile(), optimization levels, basis gates |
| `advanced_transpilation.ipynb` | PassManager, 6-stage pipeline, layout/routing |
| `jobs_and_sessions.ipynb` | JobStatus, Sessions, Batch, job retrieval |
| `options_configuration.ipynb` | Options class, resilience, shots |
| `backend_target.ipynb` | V2 API, Target object, coupling maps, T1/T2 |

---

## 🔗 Next Steps

1. Practice transpiling at all optimization levels
2. Understand coupling maps and SWAP overhead
3. Master Options configuration
4. Learn job management patterns
5. Move to **Section 5 (Sampler)** for measurement primitives

**Transpilation + Runtime = Core of real quantum computing!** 🚀⚡
