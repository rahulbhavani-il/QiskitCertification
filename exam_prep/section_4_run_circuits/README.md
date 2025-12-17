# Section 4: Run Circuits on Backend (15% of Exam)

> **Exam Weight**: ~10 questions | **Difficulty**: Medium-High | **Must Master**: ✅✅

---

## 📖 Overview

This section covers how to **execute circuits** on real quantum hardware and simulators using IBM Quantum services. Understanding transpilation, backends, sessions, and job management is CRITICAL.

### What You'll Learn

1. **QiskitRuntimeService**: Connecting to IBM Quantum
2. **Transpilation**: Converting circuits for hardware
3. **Jobs & Sessions**: Managing execution
4. **Options Configuration**: Optimization, resilience, shots
5. **Backend Target**: Understanding hardware constraints

---

## 🌐 IBM Quantum Runtime Architecture

```
Your Code
    ↓
┌──────────────────────┐
│  Qiskit Circuit      │  ← You write this
└──────────────────────┘
    ↓
┌──────────────────────┐
│  transpile()         │  ← Convert to hardware gates
└──────────────────────┘
    ↓
┌──────────────────────┐
│  QiskitRuntimeService│  ← Connect to IBM Cloud
└──────────────────────┘
    ↓
┌──────────────────────┐
│  Sampler/Estimator   │  ← Primitives (V2 API)
└──────────────────────┘
    ↓
┌──────────────────────┐
│  IBM Quantum Backend │  ← Real hardware or simulator
└──────────────────────┘
    ↓
Results (counts, expectation values, etc.)
```

### 🧠 Conceptual Deep Dive

#### Analogy: The Translator
Transpilation is like translating a poem from English to Japanese.
- **Source**: Your abstract circuit (the poem).
- **Target**: The specific quantum device (the Japanese language).
- **Constraints**: The device only supports certain gates (vocabulary) and connections (grammar).
- **Goal**: Preserve the meaning (logic) while adapting to the constraints.
- **Optimization**: A good translator (transpiler) makes the result elegant and efficient (fewer gates, less noise).

#### Virtual vs. Physical Qubits
- **Virtual Qubit**: The logical variable in your code (`q[0]`). It's perfect and abstract.
- **Physical Qubit**: The actual superconducting loop on the chip (Physical Qubit 42). It has noise, decoherence, and specific connections.
- **Mapping**: The transpiler decides which physical qubit plays the role of which virtual qubit.

---

## 🔌 QiskitRuntimeService

### Setup & Authentication

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

**Get your token**: https://quantum.ibm.com/account

### Accessing Backends

```python
# List all available backends
backends = service.backends()
for backend in backends:
    print(f"{backend.name}: {backend.num_qubits} qubits")

# Get specific backend
backend = service.backend('ibm_brisbane')  # 127-qubit system (cloud)
# backend = service.backend('ibmq_qasm_simulator')  # Cloud simulator

# For local simulation (no IBM account needed):
from qiskit_aer import AerSimulator
backend = AerSimulator()  # Runs on your local computer

# ⚠️ Note: AerSimulator can be used for most examples in this README
# ✅ Works for: Transpilation, Options, Jobs, basic execution
# ⚠️ Limitations: No real hardware noise, no IBM Runtime primitives (SamplerV2/EstimatorV2)
# 💡 For full IBM Runtime features (Sessions, Batch, resilience_level), use cloud backends

# Backend information
print(f"Name: {backend.name}")
print(f"Qubits: {backend.num_qubits}")
print(f"Max shots: {backend.max_shots}")
print(f"Status: {backend.status()}")
```

### Backend Selection Strategies

```python
# Get least busy backend
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

# Filter backends by criteria
backends = service.backends(
    filters=lambda x: (
        x.num_qubits >= 5 and
        not x.simulator and
        x.status().operational
    )
)

# Find least busy
from qiskit_ibm_runtime import QiskitRuntimeService
backend = service.least_busy(min_num_qubits=5)
print(f"Using: {backend.name}")
```

---

## ⚙️ Transpilation (EXAM CRITICAL!)

### Why Transpilation is Mandatory

```
Your Circuit:              Hardware Reality:
     ┌───┐                    ┌────┐
q_0: ┤ T ├──■──           q_0:┤ RZ ├──■──    ← T → RZ + SX
     └───┘┌─┴─┐               └────┘┌─┴─┐
q_1: ─────┤ X ├           q_1: ─────┤ X ├    ← CX allowed
          └───┘                     └───┘
          ↓                          ↓
     Arbitrary gates            Basis gates only!
     Any qubit pair            Coupling map constraints!
```

**Hardware Constraints**:
1. **Basis Gates**: Only specific gates are native (e.g., `{CX, RZ, SX, X}`)
2. **Coupling Map**: Only certain qubit pairs can interact directly
3. **Gate Errors**: Some qubits/gates have better fidelity

### The transpile() Function

```python
from qiskit import transpile, QuantumCircuit

qc = QuantumCircuit(3)
qc.h(0)
qc.t(1)
qc.cx(0, 2)  # May not be valid on hardware!

# Transpile for backend
transpiled = transpile(
    qc,
    backend=backend,                 # Target hardware
    optimization_level=3             # 0-3 (higher = more optimization)
)

print(f"Original depth: {qc.depth()}")
print(f"Transpiled depth: {transpiled.depth()}")
print(f"Original gates: {qc.count_ops()}")
print(f"Transpiled gates: {transpiled.count_ops()}")
```

### Optimization Levels (EXAM ESSENTIAL!)

```python
"""
Level 0: No optimization
- Translate to basis gates only
- Simple layout (first available)
- Routing added as needed
- USE: Debugging, see raw hardware translation

Level 1: Light optimization  
- Basic gate cancellations
- Some commutativity analysis
- Fast compilation
- USE: Quick prototyping

Level 2: Medium optimization (DEFAULT)
- Commutativity-based optimization
- Smart layout selection
- Gate consolidation
- USE: Standard production workflows

Level 3: Heavy optimization
- Aggressive resynthesis
- Multiple layout attempts
- Circuit equivalence checking
- Slow but best circuits
```

### ⚠️ Exam Decision Tree - Which Optimization Level?

```
Choose optimization_level based on:

┌─ Hardware execution? ────────────────────┐
│  YES → Use level 2 or 3                  │
│  NO (Simulator) → Use level 0 or 1       │
└──────────────────────────────────────────┘

┌─ Circuit already optimized? ─────────────┐
│  YES → Use level 0                       │
│  NO → Use level 1+                       │
└──────────────────────────────────────────┘

┌─ Speed vs Quality? ──────────────────────┐
│  Speed → level 1 (fast)                  │
│  Quality → level 3 (slow, best)          │
│  Balanced → level 2 (DEFAULT)            │
└──────────────────────────────────────────┘

┌─ Debugging transpiler? ──────────────────┐
│  YES → level 0 (minimal changes)         │
│  NO → level 2                            │
└──────────────────────────────────────────┘
```

**Memory Aid**: "0=Debug, 1=Fast, 2=Default, 3=Best"

### ⚠️ Common Transpilation Traps

**Trap 1: Must transpile before primitives?**
```python
# NO! Primitives auto-transpile
✅ sampler.run([qc])  # Auto-transpiles internally

# But manual transpile gives you control:
✅ transpiled = transpile(qc, backend, optimization_level=3)
✅ sampler.run([transpiled])  # Use your optimized version
```

**Trap 2: Transpilation is NOT deterministic**
```python
qc1 = transpile(qc, backend, optimization_level=3)
qc2 = transpile(qc, backend, optimization_level=3)
# qc1 and qc2 might be DIFFERENT! (different layouts, gate choices)
```

**Trap 3: Coupling map direction**
```python
# If backend only has edge (0 → 1) but not (1 → 0):
qc.cx(0, 1)  # ✅ Directly supported
qc.cx(1, 0)  # ⚠️ Requires SWAP or gate reversal (adds H gates)
```

### 🎓 Exam Question Patterns - Running Circuits

**Pattern 1: "Which backend for...?"**
```
Fastest testing → 'ibmq_qasm_simulator'
Real quantum effects → least_busy(min_num_qubits=X)
Specific hardware → service.backend('ibm_brisbane')
Noise-free ideal → StatevectorSimulator
```

**Pattern 2: "What does transpile() do?"**
```
1. Translates to basis gates (e.g., H→RZ+SX)
2. Maps virtual qubits to physical qubits
3. Adds SWAP gates for connectivity
4. Optimizes circuit depth
```

**Pattern 3: "When is transpilation required?"**
```
❌ NOT required: Primitives (auto-transpile)
✅ Required: backend.run() (deprecated method)
✅ Optional but recommended: Manual control for optimization
```

**Pattern 4: "Optimization level selection"**
```
Debugging → 0 (no optimization)
Quick test → 1 (light)
Production → 2 (default, balanced)
Best quality → 3 (heavy, slow)
```

### 🧠 Memory Aids - Running Circuits

**"Transpile = Translate + Optimize"**
- Trans: Translate gates to hardware basis
- Pile: Pile on optimizations

**"Levels: 0=Zero changes, 1=One pass, 2=Two-way, 3=Three+ passes"**
- 0: Minimal (just basis translation)
- 1: Fast (single optimization pass)
- 2: Default (two-way optimization)
- 3: Maximum (multiple strategies)

**"Basis Gates = Hardware Vocabulary"**
- Your circuit: High-level language
- Basis gates: Assembly language
- Transpile: Compiler

**"Coupling Map = Road Network"**
- Qubits: Cities
- Connections: Roads
- SWAP: Detour when no direct road
- USE: Performance-critical applications
"""

# Example: Compare optimization levels
from qiskit import transpile, QuantumCircuit

qc = QuantumCircuit(5)
qc.h(0)
for i in range(4):
    qc.cx(i, i+1)

for level in [0, 1, 2, 3]:
    transpiled = transpile(qc, backend, optimization_level=level)
    print(f"Level {level}: depth={transpiled.depth()}, size={transpiled.size()}")

# Output example:
# Level 0: depth=15, size=45
# Level 1: depth=12, size=38
# Level 2: depth=10, size=32  ← Default
# Level 3: depth=8, size=28   ← Best, but slowest
```

### Visual: Optimization Impact

```
Original Circuit:
     ┌───┐          
q_0: ┤ H ├──■───────
     └───┘┌─┴─┐     
q_1: ─────┤ X ├──■──
          └───┘┌─┴─┐
q_2: ──────────┤ X ├
               └───┘

After Level 0 (minimal):
     ┌────┐┌────┐               
q_0: ┤ RZ ├┤ SX ├──-■────────────  (H → RZ + SX + RZ)
     └────┘└────┘ ┌─┴─┐          
q_1: ─────────────┤ X ├──■───────  (Must route through SWAP)
                  └───┘  │       
q_2: ─────────────X──────┼───────  (SWAP inserted!)
                  │      │       
q_3: ─────────────X──────┤-------       
                       ┌─┴─┐    
q_4: ──────────────────┤ X ├────
                       └───┘    

After Level 3 (optimized):
     ┌────┐          
q_0: ┤ RZ ├──■───────  (Optimized route, fewer gates)
     └────┘┌─┴─┐     
q_2: ──────┤ X ├──■──  (Smart layout avoided SWAP!)
           └───┘┌─┴─┐
q_4: ───────────┤ X ├
                └───┘
```

### Key Transpilation Parameters

```python
transpiled = transpile(
    circuits,
    backend=backend,                 # Target backend (provides basis_gates, coupling_map)
    optimization_level=3,            # 0-3, default=2
    basis_gates=['cx', 'rz', 'sx'],  # Override basis gates
    coupling_map=[[0,1], [1,2]],     # Override connectivity
    initial_layout=[0, 2, 4],        # Manual qubit mapping
    seed_transpiler=42,              # Reproducible results
    approximation_degree=0.99        # Allow approximate synthesis
)
```

---

## 🎮 Jobs and Sessions

### Single Job Execution

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import SamplerV2 as Sampler

# Create and transpile circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])

transpiled = transpile(qc, backend)

# Run with Sampler
sampler = Sampler(backend=backend)
job = sampler.run([transpiled], shots=1024)

# Get results
print(f"Job ID: {job.job_id()}")
print(f"Status: {job.status()}")

result = job.result()
counts = result[0].data.meas.get_counts()
print(counts)
```

### Sessions: Batch Multiple Jobs

```python
from qiskit_ibm_runtime import Session, SamplerV2 as Sampler

# Create session for multiple jobs
with Session(backend=backend) as session:
    sampler = Sampler(session=session)
    
    # Run multiple circuits in same session
    job1 = sampler.run([qc1], shots=1024)
    job2 = sampler.run([qc2], shots=1024)
    job3 = sampler.run([qc3], shots=1024)
    
    # Get results
    result1 = job1.result()
    result2 = job2.result()
    result3 = job3.result()

# Session automatically closes
```

**Why use Sessions?**
- Reduced queue time (reserved slot)
- Better for iterative algorithms (VQE, QAOA)
- Cost-effective for multiple circuits

### Batch: Run Multiple Circuits Together

```python
from qiskit_ibm_runtime import Batch, SamplerV2 as Sampler

# Batch multiple circuits for parallel execution
with Batch(backend=backend) as batch:
    sampler = Sampler(mode=batch)
    
    # Submit all circuits at once
    circuits = [qc1, qc2, qc3, qc4, qc5]
    job = sampler.run(circuits, shots=1024)
    
    # Results for all circuits
    results = job.result()
    for i, result in enumerate(results):
        print(f"Circuit {i}: {result.data.meas.get_counts()}")
```

### Job Management

```python
# Check job status
print(job.status())  # JobStatus.QUEUED, RUNNING, DONE, ERROR

# Wait for completion
result = job.result()  # Blocks until done

# Retrieve old job
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
old_job = service.job('job_id_here')
result = old_job.result()

# Cancel job
job.cancel()

# Job metadata
print(job.metrics())  # Timing, resource usage
```

---

## ⚡ Options Configuration (EXAM TESTED!)

### What are Options?

**Options** is a configuration class that controls HOW your circuits are executed on quantum hardware. Think of it as the "settings menu" for quantum jobs.

```python
from qiskit_ibm_runtime import Options

options = Options()  # Creates default configuration
```

**Analogy**: Like camera settings before taking a photo:
- **ISO** (optimization_level): Quality vs speed tradeoff
- **Flash** (resilience_level): Compensate for poor lighting (noise)
- **Shots** (execution.shots): How many photos to take and average

### Why Use Options?

```
Without Options:           With Optimized Options:
┌─────────────────────┐   ┌─────────────────────┐
│ Default settings    │   │ Tuned for your needs│
│ • optimization=2    │   │ • optimization=3    │
│ • resilience=0      │   │ • resilience=1      │
│ • shots=4000        │   │ • shots=8192        │
│ • No DD             │   │ • Dynamical decoupling │
└─────────────────────┘   └─────────────────────┘
         ↓                          ↓
   Generic results            Optimized results
   50% accuracy               85% accuracy
   Fast execution             Best quality
```

**Key Benefits**:
1. **Performance**: Better circuit optimization (fewer gates)
2. **Accuracy**: Error mitigation reduces noise
3. **Efficiency**: Tune shots for your precision needs
4. **Reliability**: Dynamical decoupling fights decoherence

### Core Options Categories

#### 1. Optimization Level (Circuit Quality)

```python
options.optimization_level = 3  # 0-3

# What each level does:
Level 0: "Raw Translation"
- Only converts to basis gates
- No optimization
- Use: Debugging transpiler issues

Level 1: "Quick & Dirty" 
- Basic gate cancellations
- Fast compilation
- Use: Rapid prototyping

Level 2: "Production Default"
- Smart gate rewriting
- Layout optimization  
- Use: Standard workflows

Level 3: "Maximum Quality"
- Aggressive optimization
- Multiple layout attempts
- Use: Final production runs
```

#### 2. Resilience Level (Error Mitigation)

```python
options.resilience_level = 1  # 0-2

Level 0: "No Mitigation"
- Raw hardware results
- Fastest execution
- Use: Perfect simulators

Level 1: "M3 Correction"
- Fixes readout errors
- ~20% time overhead
- Use: Most real hardware

Level 2: "Full Mitigation" 
- M3 + Zero-noise extrapolation
- ~300% time overhead
- Use: Critical accuracy needs
```

#### 3. Execution Settings

```python
options.execution.shots = 8192  # Number of measurements

# Shot selection guide:
1024 shots: Quick testing, ~3% statistical error
4096 shots: Standard production, ~1.5% error  
8192 shots: High precision, ~1% error
16384 shots: Research quality, ~0.7% error
```

#### 4. Advanced Settings

```python
# Dynamical decoupling (fights decoherence)
options.dynamical_decoupling.enable = True
options.dynamical_decoupling.sequence_type = 'XY4'

# Transpilation control
options.transpilation.skip_transpilation = False  # Let primitive transpile
options.transpilation.initial_layout = [0, 2, 4]  # Manual qubit mapping
```

### When to Use Each Configuration

#### Scenario 1: Rapid Prototyping
```python
options = Options()
options.optimization_level = 1    # Fast compilation
options.resilience_level = 0      # No error correction overhead
options.execution.shots = 1024    # Quick results

# Use: Testing algorithm logic, parameter sweeps
```

#### Scenario 2: Standard Production
```python
options = Options()
options.optimization_level = 2    # Balanced optimization (default)
options.resilience_level = 1      # M3 error mitigation
options.execution.shots = 4096    # Good statistical accuracy

# Use: Most real applications, publication results
```

#### Scenario 3: Maximum Quality
```python
options = Options()
options.optimization_level = 3    # Best circuit optimization
options.resilience_level = 2      # Full error mitigation
options.execution.shots = 8192    # High precision
options.dynamical_decoupling.enable = True  # Fight decoherence

# Use: Critical research, benchmark comparisons
```

#### Scenario 4: Debugging/Development
```python
options = Options()
options.optimization_level = 0    # Minimal transpiler changes
options.resilience_level = 0      # Raw results
options.execution.shots = 1024    # Fast feedback
options.transpilation.skip_transpilation = False

# Use: Understanding transpiler behavior, debugging circuits
```

### Complete Example: Options in Action

```python
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler, Options

# Setup
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()

# Configure for high-quality results
options = Options()
options.optimization_level = 3        # Best optimization
options.resilience_level = 1          # M3 error mitigation  
options.execution.shots = 8192        # High precision
options.dynamical_decoupling.enable = True  # Reduce decoherence

# Run with optimized settings
sampler = Sampler(backend=backend, options=options)
job = sampler.run([qc])

result = job.result()
print(f"High-quality results: {result[0].data.meas.get_counts()}")
```

### Options Decision Tree (EXAM CRITICAL!)

```
Choose Options based on:

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

┌─ Circuit depth? ─────────────────────────────┐
│  Shallow (<10 gates) → DD not needed         │
│  Deep (>20 gates) → enable DD               │
└───────────────────────────────────────────────┘
```

**Memory Aid**: "Options = Optimization + Resilience + Shots"
- Optimization: How smart is the compilation?
- Resilience: How much error correction?
- Shots: How many measurements for statistics?

### The Options Class

```python
from qiskit_ibm_runtime import Options

options = Options()

# Optimization level (0-3)
options.optimization_level = 3  # MOST TESTED!

# Resilience level (error mitigation: 0-2)
options.resilience_level = 1  # 0=none, 1=M3, 2=ZNE+M3

# Execution options
options.execution.shots = 4096  # Number of shots (default 4000)

# Transpilation options
options.transpilation.skip_transpilation = False
options.transpilation.initial_layout = [0, 2, 4]

# Dynamical decoupling (reduce decoherence)
options.dynamical_decoupling.enable = True
options.dynamical_decoupling.sequence_type = 'XY4'

# Use with primitives
from qiskit_ibm_runtime import SamplerV2 as Sampler

sampler = Sampler(backend=backend, options=options)
job = sampler.run([qc], shots=4096)
```

### Resilience Levels (Error Mitigation)

```
Level 0: No error mitigation
- Raw results from hardware
- Fastest execution
- USE: Simulator or debugging

Level 1: M3 (Matrix-free Measurement Mitigation)
- Corrects readout errors
- ~20% overhead
- USE: Most production circuits

Level 2: ZNE + M3 (Zero-Noise Extrapolation + M3)
- Estimates zero-noise result
- ~3-5× overhead
- USE: Critical accuracy requirements
```

**Visual: Error Mitigation Effect**

```
Without Mitigation (Level 0):        With M3 (Level 1):
    
 Ideal: 50% |00⟩, 50% |11⟩         Ideal: 50% |00⟩, 50% |11⟩
 Measured:                          Corrected:
    
 |00⟩: ████████ 45%                |00⟩: █████████ 49%
 |01⟩: █ 3%                        |01⟩:  1%
 |10⟩: █ 2%                        |10⟩:  <1%
 |11⟩: ████████ 50%                |11⟩: ██████████ 50%
    
 Readout errors visible!            Corrected to ideal!
```

### Common Options Patterns

```python
# Fast prototyping (simulator)
options = Options()
options.optimization_level = 1
options.resilience_level = 0
options.execution.shots = 1024

# Production (real hardware)
options = Options()
options.optimization_level = 3
options.resilience_level = 1
options.execution.shots = 4096
options.dynamical_decoupling.enable = True

# High accuracy (research)
options = Options()
options.optimization_level = 3
options.resilience_level = 2  # ZNE + M3
options.execution.shots = 8192
```

---

## 🎯 Backend Target V2 API

### What is Backend V2 API?

The **Backend V2 API** is the modern interface for interacting with quantum hardware in Qiskit, introduced to provide a more structured and efficient way to access backend properties and capabilities.

```python
# V2 API (Current, Recommended)
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')  # Returns BackendV2 object

# Access unified target
target = backend.target  # Single source of truth
```

**Key Concept**: The V2 API consolidates all hardware information into a single **`Target`** object, making it easier to query capabilities, constraints, and properties.

### V1 vs V2 API Comparison

#### Architecture Differences

```
V1 API (Legacy, Pre-2023):          V2 API (Current, 2023+):
┌──────────────────────────┐       ┌──────────────────────────┐
│ Backend                  │       │ Backend V2               │
│  ├─ configuration()      │       │  └─ target              │
│  ├─ properties()         │       │      ├─ operations       │
│  ├─ defaults()           │       │      ├─ qargs           │
│  └─ coupling_map         │       │      ├─ properties      │
└──────────────────────────┘       │      └─ instructions    │
Multiple scattered methods         └──────────────────────────┘
                                   Single unified interface
```

#### Code Comparison Table
| **Feature** | **Definition** | **V1 API (Old)** | **V2 API (New)** |
|-------------|----------------|------------------|------------------|
| **Get basis gates** | The set of native quantum gates that the hardware can physically execute (all other gates must be decomposed into these) | `backend.configuration().basis_gates` | `backend.target.operation_names` |
| **Get coupling map** | The graph of physical connections between qubits that determines which qubit pairs can perform two-qubit gates directly | `backend.configuration().coupling_map` | `backend.target.build_coupling_map()` |
| **Check gate support** | Verify whether a specific gate operation is natively supported on a particular set of qubits | Manual parsing of config | `target.instruction_supported('cx', (0,1))` |
| **Gate properties** | Hardware characteristics of a gate including error rate (probability of failure) and duration (execution time in device units) | `backend.properties().gate_property(...)` | `target['cx'][(0,1)].error` |
| **Qubit properties** | Physical characteristics of individual qubits including T1 (relaxation time), T2 (dephasing time), and operating frequency | `backend.properties().qubit_property(...)` | `target.qubit_properties[0].t1` |
| **Number of qubits** | The total count of physical qubits available on the quantum processor | `backend.configuration().n_qubits` | `backend.num_qubits` |

### Qubit Properties Deep Dive: T1, T2, and Frequency

#### T1 (Relaxation Time) - "Energy Decay"

**Definition**: T1 measures how long a qubit can maintain its excited state |1⟩ before spontaneously decaying to the ground state |0⟩ due to energy loss to the environment.

```
Time = 0          Time = T1         Time = 2×T1
|1⟩ ████████      |1⟩ ████          |1⟩ ██
                  
Energy leaks out like heat from a hot cup of coffee
```

**Physical Meaning**:
- **What happens**: The qubit loses energy to its surroundings (like a ball rolling downhill)
- **Typical values**: 50-200 microseconds on IBM hardware
- **Impact**: Limits how long your circuit can run before |1⟩ states corrupt to |0⟩

**Memory Aid - "T1 = Temperature Drop"** 🌡️
- Think of T1 as how long a **hot coffee stays hot**
- |1⟩ = Hot (excited state)
- |0⟩ = Room temperature (ground state)
- T1 = Time for coffee to cool down halfway
- **Longer T1 = Better thermos = Better qubit**

#### T2 (Dephasing Time) - "Phase Scramble"

**Definition**: T2 measures how long a qubit can maintain coherent superposition before random phase fluctuations destroy the quantum information. It's always ≤ 2×T1.

```
Time = 0                    Time = T2
|+⟩ = |0⟩ + |1⟩            Phase scrambled!
     ↑ precise phase             ↑ random phase

Like a spinning top that starts wobbling
```

**Physical Meaning**:
- **What happens**: Environmental noise causes random rotations around the Z-axis
- **Typical values**: 50-150 microseconds (always T2 ≤ 2×T1)
- **Impact**: Limits quality of superposition states and phase-sensitive operations

**Memory Aid - "T2 = Tuning Fork"** 🎵
- Think of T2 as how long a **tuning fork stays in tune**
- Superposition = Perfect pitch (in tune)
- Dephasing = Going out of tune (frequency drift)
- T2 = Time before the note becomes unrecognizable
- **Longer T2 = Better tuning fork = Better phase coherence**

#### Frequency - "Qubit's Radio Station"

**Definition**: The resonant frequency (in GHz) at which the qubit transitions between |0⟩ and |1⟩ states. This is the energy difference E = hf where h is Planck's constant.

```
|1⟩ ─────────────  Energy E₁
    │
    │ ΔE = hf (frequency determines this gap)
    │
|0⟩ ─────────────  Energy E₀

f = (E₁ - E₀) / h ≈ 5 GHz for IBM transmons
```

**Note**: Frequency is unrelated to device time units (dt). 
- **Frequency (GHz)**: Physical property of the qubit's energy levels
- **dt (nanoseconds)**: Hardware clock resolution for scheduling pulses

They are independent parameters—dt is the timing granularity for control signals, while frequency is the electromagnetic "address" used to manipulate a specific qubit.

**Physical Meaning**:
- **What happens**: Control pulses at this exact frequency flip the qubit
- **Typical values**: 4.5-5.5 GHz for IBM superconducting qubits
- **Impact**: Each qubit has unique frequency to avoid crosstalk

**Memory Aid - "Frequency = Radio Station"** 📻
- Each qubit is tuned to a **different radio station**
- Qubit 0 = 4.8 GHz (Station 1)
- Qubit 1 = 5.1 GHz (Station 2)
- To control a qubit, you **tune to its station**
- Different frequencies = No interference between qubits

### Combined Memory Aid: "The Qubit Health Report" 🏥

```
┌─────────────────────────────────────────────────────────┐
│           QUBIT HEALTH CERTIFICATE                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  T1 (Energy Stamina)     🔋 How long it stays "charged"  │
│  ├─ Like: Battery life                                   │
│  └─ Longer = Can run deeper circuits                     │
│                                                          │
│  T2 (Phase Stability)    ⏱️ How long it stays "in sync"  │
│  ├─ Like: Clock accuracy                                 │
│  └─ Longer = Better superpositions                       │
│                                                          │
│  Frequency (Address)     📍 Its unique "phone number"    │
│  ├─ Like: Radio dial position                            │
│  └─ Different = No crosstalk                             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```
### Practical Impact on Circuit Design

**Why This Matters**: Your quantum circuit must execute faster than your qubits lose their quantum properties. If your circuit takes too long, the qubits will "forget" their state before you finish computing.

```python
# Check if your circuit fits within coherence limits
target = backend.target
qubit_props = target.qubit_properties[0]

t1 = qubit_props.t1  # e.g., 150e-6 seconds (150 μs)
t2 = qubit_props.t2  # e.g., 100e-6 seconds (100 μs)

# Estimate circuit duration (rough: 50ns per gate)
circuit_duration = transpiled.depth() * 50e-9  # seconds

if circuit_duration > t2 * 0.1:  # Rule of thumb: stay under 10% of T2
    print("⚠️ Warning: Circuit may suffer from decoherence!")
    print(f"  Circuit: {circuit_duration*1e6:.1f} μs")
    print(f"  T2 limit: {t2*1e6:.1f} μs (use < {t2*0.1*1e6:.1f} μs)")
else:
    print("✅ Circuit duration within safe coherence limits")
```

**What This Code Does (Plain English)**:

1. **Get qubit timing specs**: Retrieves T1 and T2 values (how long the qubit stays "good")

2. **Estimate your circuit's runtime**: Multiplies circuit depth by ~50 nanoseconds per gate (rough average for IBM hardware)

3. **Apply the 10% rule**: Your circuit should ideally complete in less than 10% of T2 time
    - **Why 10%?** This safety margin accounts for the fact that decoherence effects accumulate. At 10% of T2, you've lost roughly 10% of your quantum information. Beyond this, errors grow rapidly.

4. **Warn if too slow**: If your circuit exceeds this limit, results will be unreliable due to qubits losing coherence mid-computation

**Example Scenario**:
- T2 = 100 μs (microseconds)
- Safe limit = 10 μs (10% of T2)
- Your circuit depth = 300 gates
- Circuit duration = 300 × 50ns = 15 μs
- **Result**: ⚠️ Warning! 15 μs > 10 μs limit

**Device Time Units (dt)**

The **device time unit (dt)** is the fundamental time resolution of a quantum device's control system. It represents the smallest discrete time step at which the hardware can schedule operations.

```
1 dt = Hardware clock period ≈ 0.222 nanoseconds (typical IBM systems)

Example:
    If dt = 0.222 ns and a CX gate takes 256 dt:
    CX duration = 256 × 0.222 ns ≈ 57 nanoseconds
```

**Why dt instead of seconds?**
- All pulse schedules are quantized to dt boundaries
- Hardware operates on discrete clock cycles
- Ensures synchronization between control signals

**Access dt value:**
```python
dt = backend.dt  # Returns dt in seconds (e.g., 2.22e-10)
```
**Relationship to Device Time Units (dt)**:

The gate durations in the Target object are given in **device time units (dt)**, not seconds. To convert:

```python
# Get the dt value (time per device unit) from backend
dt = backend.dt  # e.g., 0.222e-9 seconds (0.222 nanoseconds)

# Gate duration is stored in dt units
cx_duration_dt = target['cx'][(0,1)].duration  # e.g., 256 dt

# Convert to seconds
cx_duration_seconds = cx_duration_dt * dt  # 256 × 0.222ns ≈ 57 ns

# More accurate circuit duration estimate:
total_duration = sum(
     target[gate][(qubits)].duration * dt 
     for gate, qubits in circuit_operations
)
```

**Why dt instead of seconds?**
- Hardware clock operates in discrete time steps
- All pulse schedules are aligned to dt boundaries
- Typical dt ≈ 0.2-0.5 nanoseconds for IBM systems

**Memory Aid**: "dt = Device Tick" - the smallest time step the hardware clock can resolve.

**Practical Solutions When Circuit is Too Long**:
1. Increase `optimization_level` to reduce gate count
2. Choose qubits with higher T1/T2 values
3. Enable dynamical decoupling to fight decoherence
4. Simplify your algorithm if possible

### Exam Quick Reference

| Property | What It Measures | Analogy | Typical Value | Longer = Better? |
|----------|------------------|---------|---------------|------------------|
| **T1** | Energy retention | Battery life | 50-200 μs | ✅ Yes |
| **T2** | Phase coherence | Clock drift | 50-150 μs | ✅ Yes |
| **Frequency** | Qubit address | Radio station | 4.5-5.5 GHz | N/A (unique) |

**Key Relationship**: T2 ≤ 2×T1 (always! phase loss includes energy loss)

**Mnemonic**: "**T**wo is **T**wice **T**oo much" → T2 can never exceed 2×T1


#### Detailed Code Examples

**Example 1: Getting Basis Gates**

```python
# V1 API (Deprecated)
from qiskit.providers.ibmq import IBMQ

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend_v1 = provider.get_backend('ibmq_manila')

basis_gates = backend_v1.configuration().basis_gates
print(f"V1 basis gates: {basis_gates}")
# Output: ['id', 'rz', 'sx', 'x', 'cx', 'reset']

# V2 API (Current)
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend_v2 = service.backend('ibm_brisbane')

basis_gates = backend_v2.target.operation_names
print(f"V2 basis gates: {basis_gates}")
# Output: ['cx', 'rz', 'sx', 'x', 'measure', 'delay']
```

**Example 2: Checking Gate Support**

```python
# V1 API (Manual and cumbersome)
config = backend_v1.configuration()
coupling_map = config.coupling_map

# Check if CX(0,1) is supported
cx_01_supported = [0, 1] in coupling_map or [1, 0] in coupling_map
print(f"V1 CX(0,1) supported: {cx_01_supported}")

# V2 API (Simple and direct)
cx_01_supported = backend_v2.target.instruction_supported('cx', (0, 1))
print(f"V2 CX(0,1) supported: {cx_01_supported}")
# Output: True (if qubits are connected)
```

**Example 3: Getting Gate Error Rates**

```python
# V1 API (Multi-step process)
props = backend_v1.properties()
cx_error = props.gate_property('cx', [0, 1], 'gate_error')
print(f"V1 CX(0,1) error: {cx_error}")
# Output: 0.0123

# V2 API (Direct access)
cx_props = backend_v2.target['cx'][(0, 1)]
print(f"V2 CX(0,1) error: {cx_props.error}")
# Output: 0.0123
print(f"V2 CX(0,1) duration: {cx_props.duration} dt")
# Output: 256 dt (device time units)
```

**Example 4: Qubit Properties**

```python
# V1 API
props = backend_v1.properties()
t1 = props.qubit_property(0, 'T1')
t2 = props.qubit_property(0, 'T2')
frequency = props.qubit_property(0, 'frequency')
print(f"V1 Qubit 0: T1={t1}, T2={t2}, freq={frequency}")

# V2 API (Cleaner object access)
qubit_props = backend_v2.target.qubit_properties[0]
print(f"V2 Qubit 0: T1={qubit_props.t1}s, T2={qubit_props.t2}s, freq={qubit_props.frequency}Hz")
```

### Why V2 is Better

#### 1. **Single Source of Truth**
```python
# V1: Scattered across multiple objects
config = backend.configuration()  # Gates, qubits, coupling
props = backend.properties()       # Errors, T1/T2
defaults = backend.defaults()      # Default pulse schedules

# V2: Everything in one place
target = backend.target  # All hardware info unified
```

#### 2. **Type Safety and Validation**
```python
# V2 validates operations at query time
if backend.target.instruction_supported('h', (0,)):
    # H gate is natively supported on qubit 0
    pass
else:
    # Need to decompose H into basis gates
    pass
```

#### 3. **Better Performance**
```python
# V1: Multiple API calls
gates = backend.configuration().basis_gates
errors = [backend.properties().gate_property('cx', [i, i+1], 'gate_error') 
          for i in range(4)]

# V2: Single target object, efficient queries
gates = backend.target.operation_names
errors = [backend.target['cx'][(i, i+1)].error for i in range(4)]
```

#### 4. **Future-Proof**
- V2 is actively maintained (V1 is deprecated)
- Better support for new hardware features
- Compatible with Qiskit Runtime primitives (Sampler, Estimator)

### Target Object Deep Dive

```python
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')
target = backend.target

# 1. All supported operations
print(f"Operations: {target.operation_names}")
# ['cx', 'rz', 'sx', 'x', 'measure', 'delay', 'reset']

# 2. Number of qubits
print(f"Qubits: {target.num_qubits}")  # 127

# 3. Check specific instruction
if target.instruction_supported('cx', (0, 1)):
    print("CX gate available between qubits 0 and 1")

# 4. Get instruction properties
cx_inst = target['cx'][(0, 1)]
print(f"CX(0,1) error: {cx_inst.error:.4f}")
print(f"CX(0,1) duration: {cx_inst.duration} dt")

# 5. Qubit-specific properties
qubit_0 = target.qubit_properties[0]
print(f"Qubit 0: T1={qubit_0.t1*1e6:.1f}µs, T2={qubit_0.t2*1e6:.1f}µs")

# 6. Build coupling map (V2 style)
coupling_map = target.build_coupling_map()
print(f"Coupling map edges: {len(coupling_map)} connections")
```

### Migration Guide: V1 → V2

```python
# ❌ V1 (Don't use anymore)
from qiskit.providers.ibmq import IBMQ

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_manila')

# ✅ V2 (Use this)
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')
```

**Common Migration Patterns**:

| **V1 Code** | **V2 Equivalent** |
|-------------|-------------------|
| `backend.configuration().basis_gates` | `backend.target.operation_names` |
| `backend.configuration().n_qubits` | `backend.num_qubits` |
| `backend.configuration().coupling_map` | `backend.target.build_coupling_map()` |
| `backend.properties().gate_error('cx', [0,1])` | `backend.target['cx'][(0,1)].error` |
| `backend.properties().t1(0)` | `backend.target.qubit_properties[0].t1` |

### Exam Relevance

**V2 API is the standard for Qiskit certification exams (2024+)**. You should:

✅ Know how to access `backend.target`  
✅ Understand `target.instruction_supported()`  
✅ Be able to query gate properties via `target['gate'][(qubits)]`  
✅ Know `target.operation_names` returns basis gates  
✅ Recognize V1 code as deprecated (but may appear in legacy questions)

**Memory Aid**: "Target = The bullseye for all hardware info"
**Memory Aid**: "TARGET" - What the Target object provides:
- **T**iming (gate durations) - How long each gate takes to execute (in device time units 'dt')
- **A**vailability (which gates on which qubits) - Which operations are natively supported on specific qubits
- **R**eliability (error rates) - Gate and readout error probabilities
- **G**eometry (coupling map) - Physical connectivity between qubits (which pairs can perform two-qubit gates)
- **E**nvironment (T1, T2, frequency) - Qubit coherence times and operating frequencies
- **T**ruth (single source) - One unified object containing all hardware specifications

#### Device Property Definitions

**Gate Duration (Timing)**
- **What**: Time required to execute a gate operation, measured in device time units (dt)
- **Device Perspective**: Physical time for control pulses to manipulate qubit states
- **Example**: CX gate might take 256 dt (~500 nanoseconds on typical IBM hardware)
- **Why It Matters**: Longer gates → more decoherence → higher error rates
- **Access**: `target['cx'][(0,1)].duration`

**Coupling Map (Geometry)**
- **What**: Graph of physical connections between qubits that can directly interact
- **Device Perspective**: Hardware wiring - only certain qubit pairs have physical coupling elements (like capacitors or resonators)
- **Example**: If qubits 0 and 1 are connected, CX(0,1) is direct; CX(0,2) requires routing through qubit 1
- **Why It Matters**: Operations on non-connected qubits need SWAP gates (expensive!)
- **Visualization**: `[[0,1], [1,2], [1,3]]` means 0↔1, 1↔2, 1↔3 are connected
- **Access**: `target.build_coupling_map()`

**T1 (Relaxation Time)**
- **What**: Time for an excited qubit |1⟩ to decay to ground state |0⟩
- **Device Perspective**: Energy loss to the environment (like a ringing bell losing sound)
- **Typical Values**: 50-200 microseconds on IBM hardware
- **Why It Matters**: Sets maximum circuit duration before qubit loses its state
- **Analogy**: Battery discharge time - how long your qubit stays "charged"
- **Access**: `target.qubit_properties[0].t1`

**T2 (Dephasing Time)**
- **What**: Time for qubit to lose phase coherence (superposition degrades)
- **Device Perspective**: Random phase fluctuations from noise (like a spinning top wobbling)
- **Typical Values**: 50-150 microseconds (always ≤ 2×T1)
- **Why It Matters**: Limits quality of superposition states (Hadamard, phase gates)
- **Analogy**: Clock drift - how long your qubit keeps accurate "time"
- **Access**: `target.qubit_properties[0].t2`

**Frequency**
- **What**: Resonant frequency of the qubit (in GHz)
- **Device Perspective**: Energy difference between |0⟩ and |1⟩ states (E = hf)
- **Typical Values**: 4.5-5.5 GHz for IBM transmon qubits
- **Why It Matters**: Used to address specific qubits without affecting neighbors
- **Analogy**: Radio station frequency - each qubit "broadcasts" at its own channel
- **Access**: `target.qubit_properties[0].frequency`

**Error Rate (Reliability)**
- **What**: Probability that a gate operation fails
- **Device Perspective**: Combination of control errors, decoherence, and crosstalk
- **Typical Values**: 
    - Single-qubit gates: 0.01-0.1% (1×10⁻⁴ to 1×10⁻³)
    - Two-qubit gates (CX): 0.5-2% (5×10⁻³ to 2×10⁻²)
    - Readout: 1-5% (1×10⁻² to 5×10⁻²)
- **Why It Matters**: Accumulates with circuit depth - 100 gates × 1% error = disaster!
- **Access**: `target['cx'][(0,1)].error`

#### Visual Hardware Model

```
Physical Quantum Chip Layout:

        Qubit 0 (f=4.8GHz, T1=120µs, T2=100µs)
             │
     Coupling (CX error=1.2%, duration=256dt)
             │
        Qubit 1 (f=4.9GHz, T1=150µs, T2=110µs)
             │
     Coupling (CX error=0.8%, duration=240dt)
             │
        Qubit 2 (f=5.1GHz, T1=95µs, T2=85µs)

Direct connections: 0↔1, 1↔2
No direct: 0↔2 (need routing through 1)
```

#### Practical Implications

```python
# Example: Choosing best qubit for long circuit
target = backend.target

best_qubit = None
best_t1 = 0

for i, props in enumerate(target.qubit_properties):
        if props and props.t1 > best_t1:
                best_t1 = props.t1
                best_qubit = i

print(f"Use qubit {best_qubit}: T1={best_t1*1e6:.1f}µs")
# For a 50µs circuit, pick qubits with T1 > 100µs

# Example: Avoiding high-error gates
for qargs, props in target['cx'].items():
        if props.error > 0.015:  # 1.5% threshold
                print(f"Warning: CX{qargs} has high error {props.error:.3f}")
```

### Practical Example: Finding Best Qubits

```python
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')
target = backend.target

# Find the best CX gate (lowest error)
best_cx_error = float('inf')
best_cx_pair = None

for instruction, qargs_dict in target.items():
    if instruction == 'cx':
        for qargs, props in qargs_dict.items():
            if props.error < best_cx_error:
                best_cx_error = props.error
                best_cx_pair = qargs

print(f"Best CX gate: qubits {best_cx_pair} with error {best_cx_error:.4f}")
# Output: Best CX gate: qubits (42, 43) with error 0.0089

# Find best qubit (longest T1)
best_t1 = 0
best_qubit = None

for i, qubit_props in enumerate(target.qubit_properties):
    if qubit_props and qubit_props.t1 > best_t1:
        best_t1 = qubit_props.t1
        best_qubit = i

print(f"Best qubit: {best_qubit} with T1={best_t1*1e6:.1f}µs")
# Output: Best qubit: 87 with T1=152.3µs
```


### Understanding Hardware Capabilities

```python
backend = service.backend('ibm_brisbane')
target = backend.target

# Supported operations
operations = target.operation_names
print(f"Native gates: {operations}")
# Output: ['cx', 'rz', 'sx', 'x', 'measure', 'delay']

# Check if operation supported on qubits
has_cx_01 = target.instruction_supported('cx', (0, 1))
has_cx_02 = target.instruction_supported('cx', (0, 2))
print(f"CX(0,1) supported: {has_cx_01}")  # True (if connected)
print(f"CX(0,2) supported: {has_cx_02}")  # False (if not connected)

# Get gate properties
cx_props = target['cx'][(0, 1)]
print(f"CX(0,1) error: {cx_props.error}")
print(f"CX(0,1) duration: {cx_props.duration} dt")

# Qubit properties
qubit_props = target.qubit_properties[0]
print(f"T1: {qubit_props.t1} seconds")
print(f"T2: {qubit_props.t2} seconds")
print(f"Frequency: {qubit_props.frequency} GHz")
```

### Coupling Map: Complete Guide

#### What is a Coupling Map?

A **coupling map** is a description of the physical connectivity between qubits on a quantum chip. It tells you which pairs of qubits can directly perform two-qubit gates (like CNOT/CX).

**Simple Analogy**: Think of a coupling map as a road network between cities:
- **Qubits** = Cities
- **Connections** = Roads
- **CX gate** = Traveling between cities
- **Direct connection** = Direct highway
- **No connection** = Need to go through other cities (expensive!)

#### Why Coupling Maps Exist

Quantum computers are physical devices with real hardware constraints:

```
Ideal World (Your Code):        Physical Reality (Hardware):
    
    Any qubit can                Only connected qubits
    interact with any            can interact directly
    other qubit                  
                                 
    q0 ←→ q1                    q0 ── q1
    q0 ←→ q2                    │
    q0 ←→ q3                    q2    q3  ← q0 and q3 NOT connected!
    q1 ←→ q2                         │
    q1 ←→ q3                         q4
    q2 ←→ q3
    (All possible!)              (Limited by physics!)
```

**Physical Reason**: Qubits are superconducting circuits. To make two qubits interact, they need a physical coupling element (like a capacitor or resonator) between them. You can't connect every qubit to every other qubit because:
1. **Space constraints**: Too many wires would cause crosstalk
2. **Engineering limits**: Each connection adds complexity
3. **Noise**: More connections = more sources of error

#### Coupling Map Structure

A coupling map is a **directed graph** represented as a list of edges:

```python
coupling_map = [
    [0, 1],  # Qubit 0 can control qubit 1
    [1, 0],  # Qubit 1 can control qubit 0
    [1, 2],  # Qubit 1 can control qubit 2
    [2, 1],  # Qubit 2 can control qubit 1
    [2, 3],  # Qubit 2 can control qubit 3
    [3, 2],  # Qubit 3 can control qubit 2
]
```

**Important**: Direction matters for CNOT gates!
- `[0, 1]` means CX(control=0, target=1) is directly supported
- `[1, 0]` means CX(control=1, target=0) is directly supported
- If only `[0, 1]` exists (not `[1, 0]`), then CX(1, 0) requires extra gates (Hadamards) to reverse

#### Visual Examples

**Example 1: Linear Chain (Simplest)**

```
Coupling Map: [[0,1], [1,2], [2,3]]

Physical Layout:
    q0 ── q1 ── q2 ── q3

Supported Operations:
✅ CX(0, 1) - Direct
✅ CX(1, 2) - Direct  
✅ CX(2, 3) - Direct
❌ CX(0, 2) - Need routing through q1
❌ CX(0, 3) - Need routing through q1 and q2
❌ CX(1, 3) - Need routing through q2
```

**Example 2: T-Shape**

```
Coupling Map: [[0,1], [1,0], [1,2], [2,1], [1,3], [3,1]]

Physical Layout:
         q0
         │
    q2 ─ q1 ─ q3

Supported Operations:
✅ CX(0, 1), CX(1, 0) - Bidirectional
✅ CX(1, 2), CX(2, 1) - Bidirectional
✅ CX(1, 3), CX(3, 1) - Bidirectional
❌ CX(0, 2) - Need q1 as intermediary
❌ CX(0, 3) - Need q1 as intermediary
❌ CX(2, 3) - Need q1 as intermediary
```

**Example 3: Grid (IBM Heavy-Hex)**

```
Coupling Map: [[0,1], [1,0], [1,2], [2,1], [0,3], [3,0], 
               [2,4], [4,2], [3,4], [4,3]]

Physical Layout:
    q0 ── q1 ── q2
    │           │
    q3 ──────── q4

Supported Operations:
✅ CX(0, 1), CX(1, 2) - Horizontal edges
✅ CX(0, 3), CX(2, 4) - Vertical edges
✅ CX(3, 4) - Diagonal edge
❌ CX(0, 2) - Need routing (0→1→2)
❌ CX(1, 3) - Need routing (1→0→3 or 1→2→4→3)
```

#### Real IBM Hardware Example

**IBM Nairobi (7 qubits) - Heavy-Hex Topology**:

```
Coupling Map Visualization:

         q0
        ╱  ╲
      q1    q3
       │  ╳  │
      q2    q4
        ╲  ╱
         q5
          │
         q6

Edges (bidirectional):
[0,1], [1,0], [1,2], [2,1],
[0,3], [3,0], [3,4], [4,3],
[2,5], [5,2], [4,5], [5,4],
[5,6], [6,5]

Total: 14 directed edges = 7 bidirectional connections
```

#### How Transpiler Uses Coupling Map

**Scenario**: You write `CX(0, 4)` but qubits 0 and 4 are NOT connected.

**Transpiler Solutions**:

**Option 1: SWAP gates** (change physical location)
```
Original:               After SWAPs:
CX(0, 4)    →          SWAP(0, 1)
                       SWAP(1, 3)  
                       CX(3, 4)
                       SWAP(1, 3)
                       SWAP(0, 1)

Cost: 3 CX per SWAP = 9 CX gates total! 😱
```

**Option 2: Smart Initial Layout** (map virtual qubits cleverly)
```
Your code:              Transpiler mapping:
q_virtual[0] → CX → q_virtual[4]    q_physical[3] → CX → q_physical[4]
                                    
By mapping virtual q0 to physical q3, CX becomes direct!
Cost: 1 CX gate ✅
```

**This is why optimization_level matters!**
- Level 0: Dumb mapping, many SWAPs
- Level 3: Smart mapping, minimal SWAPs
#### Accessing Coupling Map in Code

```python
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_nairobi')

# Method 1: Backend V2 API (Recommended)
coupling_map = backend.target.build_coupling_map()
print(coupling_map)
# Output: CouplingMap([[0, 1], [1, 0], [1, 2], ...])

# Method 2: Direct attribute (also works)
coupling_map = backend.coupling_map
print(coupling_map)

# Get list of edges
edges = coupling_map.get_edges()
print(f"Edges: {edges}")
# [(0, 1), (1, 0), (1, 2), (2, 1), ...]

# Check if qubits are connected
is_connected = coupling_map.distance(0, 4)
if is_connected == 1:
    print("Direct connection")
elif is_connected > 1:
    print(f"Requires {is_connected - 1} intermediate qubits")
else:
    print("Not connected")
```

#### Simulating Coupling Maps on Local Simulators

**Yes!** You can simulate hardware coupling maps on local simulators for testing without using IBM Quantum credits.

**Why Simulate Coupling Maps?**
- Test transpilation behavior before running on real hardware
- Debug routing and SWAP insertion logic
- Verify circuit optimization strategies
- No queue time or cost

**Method 1: AerSimulator with Coupling Map** (Recommended)

```python
from qiskit_aer import AerSimulator
from qiskit.transpiler import CouplingMap

# Define a custom coupling map (e.g., linear chain)
custom_coupling = CouplingMap([[0,1], [1,0], [1,2], [2,1], [2,3], [3,2]])

# Create simulator with coupling map constraint
backend = AerSimulator(coupling_map=custom_coupling)

print(f"Simulator coupling map: {backend.coupling_map}")
# Output: [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]

# Now transpile as if it were real hardware
from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(4)
qc.h(0)
qc.cx(0, 3)  # Not directly connected in linear chain!

transpiled = transpile(qc, backend=backend, optimization_level=3)
print(f"Depth after routing: {transpiled.depth()}")
# Will show added SWAP gates to route 0→3
```

**Method 2: Simulate IBM Hardware Topology**

```python
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

# Get real hardware coupling map
service = QiskitRuntimeService()
real_backend = service.backend('ibm_nairobi')
real_coupling_map = real_backend.coupling_map

# Create simulator that mimics real hardware
sim_backend = AerSimulator(coupling_map=real_coupling_map)

# Transpile as if running on ibm_nairobi
transpiled = transpile(qc, backend=sim_backend, optimization_level=3)

# Execute on simulator (no queue, instant results!)
job = sim_backend.run(transpiled, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)
```

**Method 3: FakeBackend (IBM Hardware Mockups)**

```python
from qiskit_ibm_runtime.fake_provider import FakeManilaV2

# Pre-configured simulator mimicking IBM Manila (5 qubits)
fake_backend = FakeManilaV2()

print(f"Fake backend coupling map: {fake_backend.coupling_map}")
# Output: Real IBM Manila topology

print(f"Basis gates: {fake_backend.target.operation_names}")
# Output: ['cx', 'rz', 'sx', 'x', 'id', 'measure']

# Transpile with realistic constraints
transpiled = transpile(qc, backend=fake_backend, optimization_level=3)

# Run locally (no IBM account needed!)
from qiskit_aer import AerSimulator
sim = AerSimulator.from_backend(fake_backend)
job = sim.run(transpiled)
result = job.result()
```

**Comparison Table**

| **Method** | **Coupling Map** | **Basis Gates** | **Noise Model** | **Use Case** |
|------------|------------------|-----------------|-----------------|--------------|
| `AerSimulator()` | None (all-to-all) | Universal | No | Quick testing |
| `AerSimulator(coupling_map=...)` | Custom | Universal | No | Test routing logic |
| `AerSimulator.from_backend(real)` | Real hardware | Real hardware | Optional | Pre-production testing |
| `FakeBackendV2` | Real hardware | Real hardware | Yes (optional) | Offline development |

**Testing Transpilation with Simulated Coupling Maps**

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.transpiler import CouplingMap

# Scenario: Test how circuit adapts to different topologies

qc = QuantumCircuit(5)
qc.h(0)
qc.cx(0, 4)  # Long-distance gate
qc.cx(1, 3)

# Test 1: Linear topology
linear_map = CouplingMap([[i, i+1] for i in range(4)])
sim_linear = AerSimulator(coupling_map=linear_map)
transpiled_linear = transpile(qc, sim_linear, optimization_level=3)
print(f"Linear topology depth: {transpiled_linear.depth()}")

# Test 2: Grid topology
grid_map = CouplingMap([[0,1], [1,2], [0,3], [3,4], [1,4]])
sim_grid = AerSimulator(coupling_map=grid_map)
transpiled_grid = transpile(qc, sim_grid, optimization_level=3)
print(f"Grid topology depth: {transpiled_grid.depth()}")

# Test 3: All-to-all (no constraints)
sim_ideal = AerSimulator()  # No coupling map
transpiled_ideal = transpile(qc, sim_ideal, optimization_level=3)
print(f"Ideal topology depth: {transpiled_ideal.depth()}")

# Output example:
# Linear topology depth: 15 (many SWAPs)
# Grid topology depth: 9 (better routing)
# Ideal topology depth: 3 (no routing needed)
```

**Key Advantages of Simulated Coupling Maps**

✅ **No IBM account required** (for custom AerSimulator)  
✅ **Instant execution** (no queue)  
✅ **Free testing** (no quantum credits used)  
✅ **Reproducible results** (no hardware noise)  
✅ **Iterate quickly** (test multiple topologies)  
✅ **Educational** (understand SWAP insertion visually)

**Limitations**

❌ **No real noise** (unless using FakeBackend with noise model)  
❌ **No IBM Runtime features** (Sessions, Batch require real backends)  
❌ **No resilience_level testing** (error mitigation needs real errors)  
❌ **Oversimplified** (real hardware has directional coupling, gate errors)

**Best Practice Workflow**

```python
# Step 1: Develop on simulator with coupling map
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeNairobiV2

fake_backend = FakeNairobiV2()
transpiled = transpile(qc, fake_backend, optimization_level=3)

# Step 2: Test locally
sim = AerSimulator.from_backend(fake_backend)
result = sim.run(transpiled, shots=1024).result()
print(result.get_counts())

# Step 3: Verify on real hardware (when ready)
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
real_backend = service.backend('ibm_nairobi')
job = real_backend.run(transpiled, shots=1024)  # Uses quantum credits
```

**Exam Tip**: Know that coupling maps can be simulated for testing, but emphasize that real hardware behavior (noise, errors, timing) cannot be fully replicated by simulators.

**Memory Aid**: "Coupling Map = Testable Constraint" 
- Topology is just a graph → Can simulate structure
- Noise is physical → Cannot simulate perfectly

```python
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_nairobi')

# Method 1: Backend V2 API (Recommended)
coupling_map = backend.target.build_coupling_map()
print(coupling_map)
# Output: CouplingMap([[0, 1], [1, 0], [1, 2], ...])

# Method 2: Direct attribute (also works)
coupling_map = backend.coupling_map
print(coupling_map)

# Get list of edges
edges = coupling_map.get_edges()
print(f"Edges: {edges}")
# [(0, 1), (1, 0), (1, 2), (2, 1), ...]

# Check if qubits are connected
is_connected = coupling_map.distance(0, 4)
if is_connected == 1:
    print("Direct connection")
elif is_connected > 1:
    print(f"Requires {is_connected - 1} intermediate qubits")
else:
    print("Not connected")
```

#### Coupling Map and Circuit Depth

**Key Insight**: Poor qubit mapping increases circuit depth dramatically!

```
Circuit: H(q0) - CX(q0, q4) - H(q4)

Bad Mapping (q0→physical 0, q4→physical 4, not connected):
    Depth = 1 + 9 (SWAPs) + 1 = 11 gates

Good Mapping (q0→physical 3, q4→physical 4, connected):
    Depth = 1 + 1 (CX) + 1 = 3 gates

🎯 Smart mapping reduced depth by 73%!
```

#### Visualizing Coupling Maps

```python
from qiskit.visualization import plot_coupling_map

# Plot backend coupling map
plot_coupling_map(backend)

# Or create custom coupling map
from qiskit.transpiler import CouplingMap

custom_map = CouplingMap([[0,1], [1,2], [2,3], [3,0]])  # Square
plot_coupling_map(custom_map)
```

#### Common Coupling Map Topologies

**1. Linear/Chain**: `q0─q1─q2─q3`
- **Pros**: Simple, easy to understand
- **Cons**: Long-distance gates expensive
- **Used in**: Early IBM devices, tutorials

**2. Heavy-Hex (IBM Standard)**: Hexagonal tiles
- **Pros**: Balance between connectivity and error rates
- **Cons**: Some qubits poorly connected
- **Used in**: IBM Quantum (Brisbane, Kyoto, Osaka)

**3. Grid/Lattice**: `q0─q1─q2`
```
                   │  │  │
                  q3─q4─q5
```
- **Pros**: Good for 2D problems (simulations)
- **Cons**: Corner qubits have fewer connections
- **Used in**: Google Sycamore, some superconducting chips

**4. All-to-All (Trapped Ions)**: Every qubit connected
- **Pros**: No routing overhead!
- **Cons**: Not scalable to many qubits
- **Used in**: IonQ, small superconducting chips

#### Exam-Relevant Facts

**Q: What happens if you use CX on disconnected qubits?**
```python
# Without transpilation
qc.cx(0, 4)  # If not connected
backend.run(qc)  # ❌ ERROR: Invalid coupling

# With transpilation
transpiled = transpile(qc, backend)  # ✅ Adds SWAPs automatically
```

**Q: How to check if two qubits are connected?**
```python
coupling_map = backend.coupling_map
distance = coupling_map.distance(0, 4)

if distance == 1:
    print("Direct neighbors")
elif distance > 1:
    print(f"Need {distance - 1} hops")
else:
    print("Disconnected")
```

**Q: Does coupling map affect single-qubit gates?**
```
❌ NO! Single-qubit gates (H, X, RZ) work on ANY qubit.
✅ YES! Only two-qubit gates (CX, CZ, SWAP) require coupling.
```

**Q: What is the most connected qubit?**
```python
from collections import Counter

edges = backend.coupling_map.get_edges()
counter = Counter([edge[0] for edge in edges])
most_connected = counter.most_common(1)[0]
print(f"Qubit {most_connected[0]} has {most_connected[1]} connections")
```

#### Memory Aids

**"Coupling Map = Road Map"**
- Direct connection = Highway (fast, 1 CX)
- No connection = Dirt road (slow, many SWAPs)
- Transpiler = GPS (finds best route)

**"SWAP is Expensive"**
- 1 SWAP = 3 CX gates
- Each CX has ~1% error
- 1 SWAP ≈ 3% error accumulation!

**"Layout Matters More Than You Think"**
- Bad layout: 10× more gates
- Good layout: Matches your circuit to hardware
- optimization_level=3: Tries multiple layouts

#### Practical Example: Effect of Coupling Map

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.backend('ibm_nairobi')  # 7 qubits

# Create circuit with long-distance CX
qc = QuantumCircuit(7)
qc.h(0)
qc.cx(0, 6)  # Qubits 0 and 6 are far apart!
qc.h(6)

print(f"Original depth: {qc.depth()}")  # 3 gates

# Transpile with different optimization levels
for level in [0, 1, 2, 3]:
    transpiled = transpile(qc, backend, optimization_level=level)
    print(f"Level {level}: depth={transpiled.depth()}, CX count={transpiled.count_ops().get('cx', 0)}")

# Output:
# Level 0: depth=15, CX count=7  ← Many SWAPs!
# Level 1: depth=12, CX count=5
# Level 2: depth=9, CX count=3
# Level 3: depth=7, CX count=1   ← Found optimal route!
```

#### Summary

**Coupling Map = Hardware Connectivity**
- Describes which qubit pairs can interact
- Represented as directed graph (list of edges)
- Critical for transpilation and optimization
- Poor mapping → many SWAPs → deep circuits → more errors

**Key Actions**:
1. Always check `backend.coupling_map` before running
2. Use `optimization_level=3` for best layout
3. Design circuits with connectivity in mind (if possible)
4. Visualize coupling map to understand hardware topology

**Exam Tip**: If asked "Why does transpilation increase circuit depth?", answer: "To satisfy coupling map constraints by adding SWAP gates for disconnected qubits."

```
IBM Brisbane (127 qubits) - Partial Coupling Map:

     0 ── 1 ── 2
     │    │    │
     3 ── 4 ── 5
     │    │    │
     6 ── 7 ── 8
     
Edges: [(0,1), (1,2), (0,3), (1,4), ...]

CX(0,1): ✓ Direct
CX(0,2): ✗ Need routing (0→1→2 or SWAP)
CX(0,8): ✗ Need multiple hops
```

**Extracting Coupling Map**:

```python
coupling_map = backend.coupling_map
print(f"Connectivity: {coupling_map}")
# Output: [[0,1], [1,0], [1,2], [2,1], ...]

# Visualize
from qiskit.visualization import plot_coupling_map
plot_coupling_map(backend)
```

---

## ✅ Exam Quick Reference

### Must Memorize

```python
# Runtime service
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Transpilation
from qiskit import transpile
transpiled = transpile(qc, backend, optimization_level=3)

# Optimization levels
0: No optimization (basis + layout only)
1: Light (fast, basic cancellations)
2: Medium (default, commutativity)
3: Heavy (best quality, slowest)

# Options
from qiskit_ibm_runtime import Options
options = Options()
options.optimization_level = 3      # 0-3
options.resilience_level = 1        # 0-2
options.execution.shots = 4096

# Primitives with options
from qiskit_ibm_runtime import SamplerV2 as Sampler
sampler = Sampler(backend=backend, options=options)
job = sampler.run([qc], shots=1024)

# Job management
job.status()
job.result()
job.cancel()
```

### Common Exam Questions

**Q1: What is the default optimization_level?**
- Answer: 2 (medium optimization)

**Q2: What does resilience_level=1 do?**
- Answer: Applies M3 (measurement error mitigation)

**Q3: How to transpile for specific backend?**
```python
transpiled = transpile(qc, backend=backend, optimization_level=3)
```

**Q4: What's the difference between Session and Batch?**
- Session: Sequential jobs with reserved access
- Batch: Parallel execution of multiple circuits

---

## 🎯 Practice Example: Complete Workflow

This section demonstrates a complete quantum circuit execution workflow using all methods discussed in this guide. For detailed hands-on practice with side-by-side comparisons, see:

**📝 [Comprehensive Practical Example](../practical_workflow_comparison.md)**

The practical example covers:
- Multiple backend options (simulator, fake backend, real hardware)
- All transpilation optimization levels (0-3) with visual comparisons
- Different Options configurations (prototyping, production, research)
- Session vs Batch execution modes
- Job management and result retrieval
- Performance metrics and trade-offs

### Quick Preview

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler, Options

# 1. Connect to IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibmq_qasm_simulator')

# 2. Create circuit
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

# 3. Transpile with optimization
transpiled = transpile(qc, backend=backend, optimization_level=3)

# 4. Configure options for production
options = Options()
options.optimization_level = 3
options.resilience_level = 1
options.execution.shots = 4096

# 5. Run with Sampler
sampler = Sampler(backend=backend, options=options)
job = sampler.run([transpiled])

# 6. Get results
result = job.result()
counts = result[0].data.meas.get_counts()
print(f"Measurement counts: {counts}")
```

**See the full practical guide for:**
- ✅ Method-by-method comparisons
- ✅ Decision trees for choosing approaches
- ✅ Performance benchmarks
- ✅ Common pitfalls and solutions
- ✅ Copy-paste ready code templates

```python
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler, Options

# 1. Connect to IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibmq_qasm_simulator')

# 2. Create circuit
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

print("Original circuit:")
print(qc.draw())
print(f"Depth: {qc.depth()}, Size: {qc.size()}")

# 3. Transpile with optimization
transpiled = transpile(qc, backend=backend, optimization_level=3)
print("\nTranspiled circuit:")
print(transpiled.draw())
print(f"Depth: {transpiled.depth()}, Size: {transpiled.size()}")

# 4. Configure options
options = Options()
options.optimization_level = 3
options.resilience_level = 1
options.execution.shots = 4096

# 5. Run with Sampler
sampler = Sampler(backend=backend, options=options)
job = sampler.run([transpiled])

print(f"\nJob ID: {job.job_id()}")
print(f"Status: {job.status()}")

# 6. Get and visualize results
result = job.result()
counts = result[0].data.meas.get_counts()

from qiskit.visualization import plot_histogram
plot_histogram(counts)

print(f"\nMeasurement counts: {counts}")
```

---

## 📁 Files in This Section

### Python Notebooks (.ipynb)

1. **`01_runtime_service.ipynb`** - QiskitRuntimeService setup, authentication, backend selection strategies
2. **`02_transpilation.ipynb`** - transpile() function, optimization levels 0-3, basis gates, coupling maps
3. **`03_jobs_and_sessions.ipynb`** - Job lifecycle, Sessions for iterative algorithms, Batch execution
4. **`04_options_configuration.ipynb`** - Options class, optimization_level, resilience_level, execution.shots
5. **`05_backend_target.ipynb`** - Backend V2 API, Target object, coupling maps, gate properties

---

## 🎓 Key Takeaways

```
✅ QiskitRuntimeService connects to IBM Quantum
✅ transpile() is MANDATORY for hardware execution
✅ optimization_level: 0-3 (higher = better circuits, slower compile)
✅ resilience_level: 0-2 (higher = more error mitigation)
✅ Default: optimization_level=2, shots=4000
✅ Sessions for sequential jobs (VQE iterations)
✅ Batch for parallel execution
✅ Backend target provides hardware constraints
✅ This is 15% of exam - understand deeply!
```

---

## 🔗 Next Steps

1. Practice transpiling circuits at all optimization levels
2. Understand coupling maps and routing
3. Master Options configuration
4. Learn job management and Sessions
5. Move to **Section 5 (Sampler)** for measurement statistics

**Transpilation + Runtime = Core of real quantum computing!** 🚀⚡
