# Section 7: Result Extraction (10% of Exam)

> **Exam Weight**: ~7 questions | **Difficulty**: High | **Must Master**: ✅✅✅

---

## 📖 Overview

Result extraction retrieves data from primitive execution (Sampler/Estimator). This is one of the **most tested** topics on the certification exam - result access patterns appear in virtually EVERY exam with 5-7 direct questions.

### What You'll Learn

1. **Sampler Result Access**: The `result[0].data.meas.get_counts()` pattern
2. **Estimator Result Access**: The `result[0].data.evs` pattern
3. **PUB Format**: Primitive Unified Bloc input structure
4. **Multiple Circuit Results**: Batch processing and iteration
5. **Metadata Access**: Execution information and diagnostics
6. **JobStatus Enumeration**: Job lifecycle states
7. **service.jobs() Filtering**: Job history retrieval
8. **RuntimeEncoder/Decoder**: Serialization for IBM Quantum

---

## 🎯 Why This Section Matters (Conceptual Foundation)

### 🧠 Conceptual Deep Dive

#### Analogy: The Survey Results Office
Extracting quantum results is like analyzing data at a survey processing center:

- **Raw Data (Result object)**: The sealed envelope containing all survey responses
- **Index [0] (Circuit selector)**: Which batch of surveys you're analyzing
- **data (DataBin)**: Opening the envelope to access the contents
- **meas (BitArray)**: The specific section with counted responses
- **get_counts()**: Reading the tallied results

Just as a survey office processes forms into statistics, Qiskit's result structure transforms quantum measurements into usable data.

#### The "Data" Wrapper (PubResult)
In Qiskit Primitives V2, results are wrapped in a `PubResult` (Primitive Unified Bloc). Think of this as a standardized envelope that holds both:
- **The answer** (data - counts or expectation values)
- **The context** (metadata - execution details)

### Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                 RESULT EXTRACTION HIERARCHY                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   job.result()                                                   │
│       │                                                          │
│       ▼                                                          │
│   PrimitiveResult                                                │
│       │                                                          │
│       ├── [0] ──► PubResult (first circuit)                     │
│       │              │                                           │
│       │              ├── .data ──► DataBin                      │
│       │              │     │                                     │
│       │              │     ├── SAMPLER: .meas ──► BitArray      │
│       │              │     │                    ├─ get_counts() │
│       │              │     │                    ├─ get_bitstrings()
│       │              │     │                    └─ get_int_counts()
│       │              │     │                                     │
│       │              │     └── ESTIMATOR: .evs, .stds ──► float │
│       │              │                                           │
│       │              └── .metadata ──► dict                     │
│       │                                                          │
│       ├── [1] ──► PubResult (second circuit)                    │
│       ├── [2] ──► ...                                           │
│       └── [n] ──► PubResult (nth circuit)                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Covered (Quick Reference)

| Topic | Description | Exam Weight | Priority |
|-------|-------------|-------------|----------|
| **Sampler Result Access** | `result[0].data.meas.get_counts()` | Very High | 🔴 |
| **Estimator Result Access** | `result[0].data.evs` | Very High | 🔴 |
| **PUB Format** | Input structure for primitives | High | 🔴 |
| **Multiple Circuits** | Batch processing with indices | High | 🔴 |
| **Metadata** | Execution information | Medium | 🟡 |
| **JobStatus** | Job lifecycle enumeration | Medium | 🟡 |
| **service.jobs()** | Job history filtering | Medium | 🟡 |
| **RuntimeEncoder/Decoder** | Serialization | Low | 🟢 |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION 7 LEARNING PATH                       │
├─────────────────────────────────────────────────────────────────┤
│  START HERE                                                      │
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. SAMPLER RESULTS (Most Tested!)                           ││
│  │    └─ result[0].data.meas.get_counts()                      ││
│  │    └─ get_bitstrings(), get_int_counts()                    ││
│  │    └─ BitArray properties                                   ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 2. ESTIMATOR RESULTS                                        ││
│  │    └─ result[0].data.evs (plural!)                          ││
│  │    └─ result[0].data.stds                                   ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 3. PUB FORMAT                                               ││
│  │    └─ Sampler: (circuit, params, shots)                     ││
│  │    └─ Estimator: (circuit, observable, params, precision)   ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 4. MULTIPLE CIRCUITS & METADATA                             ││
│  │    └─ Indexing: result[0], result[1], ...                   ││
│  │    └─ Iteration: for pub_result in result                   ││
│  │    └─ Metadata: result[i].metadata                          ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 5. JOB MANAGEMENT                                           ││
│  │    └─ JobStatus enumeration                                 ││
│  │    └─ service.jobs() filtering                              ││
│  │    └─ RuntimeEncoder/Decoder                                ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  COMPLETE: Ready for Result Extraction exam questions            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Sampler Result Extraction

> **EXAM CRITICAL**: This is THE most tested pattern on the certification!
> You MUST memorize `result[0].data.meas.get_counts()` perfectly.

### Overview

Sampler returns measurement outcomes as counts, bitstrings, or integer representations. The result structure requires navigating through multiple layers: index → data → meas → method.

---

### 🔹 get_counts() - Primary Result Access

#### 1. Definition
`get_counts()` returns measurement outcomes as a dictionary mapping bitstrings to their occurrence counts. This is the most common result extraction method on the exam.

#### 2. Analogy + Intuition
**Real-World Analogy**
Think of `get_counts()` like tallying votes in an election:
- Each measurement is a vote cast
- Each unique outcome (bitstring) is a candidate
- The count is how many votes that candidate received

**Intuition Builder**
The nested access pattern exists because:
- `result[0]` - Select which circuit's results (batch support)
- `.data` - Access the data container (vs metadata)
- `.meas` - Specify which classical register (default name)
- `.get_counts()` - Get the dictionary format

#### 3. Math + Visual
**Mathematical Foundation**
$$\text{counts} = \{|b_i\rangle: n_i | i = 1, \ldots, k\}$$
Where $n_i$ is the number of times bitstring $b_i$ was measured out of total shots.

**Visual Representation**
```
Sampler Result Structure:
                                                   
   result (PrimitiveResult)                        
      │                                            
      └──[0] (PubResult)                          
            │                                      
            └──.data (DataBin)                    
                  │                                
                  └──.meas (BitArray)             
                        │                          
                        ├── .get_counts()  ──► {'00': 512, '11': 512}
                        ├── .get_bitstrings() ──► ['00', '11', '00', ...]
                        └── .get_int_counts() ──► {0: 512, 3: 512}
```

#### 4. Implementation (Basic → Advanced)
**Qiskit Syntax**
```python
counts = result[0].data.meas.get_counts()
```

**Parameters**
| Method | Returns | Format |
|--------|---------|--------|
| `get_counts()` | `dict[str, int]` | `{'00': 512, '11': 512}` |
| `get_bitstrings()` | `list[str]` | `['00', '11', '00', ...]` |
| `get_int_counts()` | `dict[int, int]` | `{0: 512, 3: 512}` |

**Basic Example**
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# Create and run Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1024)
result = job.result()

# EXAM CRITICAL: The pattern you MUST know
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': ~512, '11': ~512}
```

**Intermediate Example**
```python
# Convert counts to probabilities
counts = result[0].data.meas.get_counts()
total = sum(counts.values())
probabilities = {state: count/total for state, count in counts.items()}
print(probabilities)  # {'00': 0.5, '11': 0.5}
```

**Advanced Example**
```python
# Multiple circuits with different result extraction
qc1 = QuantumCircuit(1); qc1.h(0); qc1.measure_all()
qc2 = QuantumCircuit(1); qc2.x(0); qc2.measure_all()

job = sampler.run([(qc1,), (qc2,)], shots=1024)
result = job.result()

# Access individual circuits
counts1 = result[0].data.meas.get_counts()  # {'0': ~512, '1': ~512}
counts2 = result[1].data.meas.get_counts()  # {'1': 1024}

# Or iterate through all
for i, pub_result in enumerate(result):
    print(f"Circuit {i}: {pub_result.data.meas.get_counts()}")
```

#### 5. ⚠️ Trap Alert
> **LEARN THE TRAP NOW** - This is the #1 exam mistake!

**Trap: Missing Access Levels**
- ❌ **Wrong**: `result.data.meas.get_counts()` - Missing [0] index!
- ❌ **Wrong**: `result[0].meas.get_counts()` - Missing .data!
- ❌ **Wrong**: `result[0].data.get_counts()` - Missing .meas!
- ❌ **Wrong**: `result[0].data.meas.counts()` - Missing .get_!
- ✅ **Correct**: `result[0].data.meas.get_counts()`

```python
# ❌ WRONG - Each of these will fail!
result.data.meas.get_counts()      # 'PrimitiveResult' has no attribute 'data'
result[0].meas.get_counts()        # 'PubResult' has no attribute 'meas'
result[0].data.get_counts()        # 'DataBin' has no attribute 'get_counts'
result[0].data.meas.counts()       # 'BitArray' has no attribute 'counts'

# ✅ CORRECT - All four levels required!
result[0].data.meas.get_counts()   # {'00': 512, '11': 512}
```

#### 6. 🧠 Mnemonic
> **LOCK IT IN NOW** - One memorable phrase for this pattern

**"Really Intelligent Developers Memorize Gatterns"**
- **R**esult → **I**ndex → **D**ata → **M**eas → **G**et_counts()
- Meaning: Each letter reminds you of a required access level
- Example: `result[0].data.meas.get_counts()`

**Alternative: "RIDMG" pronounced "ridmig"**

#### 7. ⚡ Quick Check
> **TEST YOURSELF NOW** - Active recall within 30 seconds

**Q: Write the complete line to extract counts from a Sampler result.**

<details>
<summary>Answer</summary>

**A**: `counts = result[0].data.meas.get_counts()`

All four levels required: result → [0] → .data → .meas → .get_counts()
</details>

---

### 🔹 get_bitstrings() - Raw Measurement List

#### 1. Definition
`get_bitstrings()` returns all individual measurement outcomes as a list of strings, preserving the order in which measurements occurred.

#### 2. Analogy + Intuition
**Real-World Analogy**
If `get_counts()` is the vote tally board, `get_bitstrings()` is the stack of individual ballot papers before counting. You see every single outcome in sequence.

**Intuition Builder**
Use when you need:
- Individual shot-by-shot data
- Statistical analysis beyond counts
- Order-dependent processing

#### 3. Math + Visual
**Visual Representation**
```
For 8 shots:

get_counts():      {'00': 4, '11': 4}
get_bitstrings():  ['00', '11', '00', '11', '11', '00', '11', '00']
                    └─ Every measurement preserved in order ──┘
```

#### 4. Implementation
**Qiskit Syntax**
```python
bitstrings = result[0].data.meas.get_bitstrings()
```

**Basic Example**
```python
bitstrings = result[0].data.meas.get_bitstrings()
print(bitstrings[:5])  # First 5: ['00', '11', '00', '11', '00']
print(len(bitstrings))  # Total shots (e.g., 1024)
```

**Advanced Example**
```python
# Statistical analysis on individual shots
import numpy as np
bitstrings = result[0].data.meas.get_bitstrings()

# Convert to integers for analysis
int_vals = [int(bs, 2) for bs in bitstrings]
print(f"Mean: {np.mean(int_vals):.2f}")
print(f"Std: {np.std(int_vals):.2f}")
```

#### 5. ⚠️ Trap Alert
**Trap: Length vs Counts**
- ❌ **Wrong**: Expecting `len(bitstrings)` to equal number of unique outcomes
- ✅ **Correct**: `len(bitstrings)` equals total shots

```python
# len(get_bitstrings()) = shots
# len(get_counts()) = number of unique outcomes

bitstrings = result[0].data.meas.get_bitstrings()  # Length: 1024
counts = result[0].data.meas.get_counts()          # Length: 2 (unique outcomes)
```

#### 6. 🧠 Mnemonic
**"Bitstrings = Big list"**
- Meaning: get_bitstrings() returns ALL measurements (big), counts is summary (small)

#### 7. ⚡ Quick Check
**Q: If you ran 1000 shots measuring a Bell state, what's len(result[0].data.meas.get_bitstrings())?**

<details>
<summary>Answer</summary>

**A**: 1000 (equals the number of shots, not unique outcomes)
</details>

---

### 🔹 get_int_counts() - Integer Format

#### 1. Definition
`get_int_counts()` returns counts with bitstrings converted to their integer representations.

#### 2. Analogy + Intuition
**Real-World Analogy**
Like expressing binary numbers as decimals: '00' → 0, '01' → 1, '10' → 2, '11' → 3

#### 3. Math + Visual
```
Bitstring to Integer Mapping:
'00' → 0  (0*2¹ + 0*2⁰)
'01' → 1  (0*2¹ + 1*2⁰)
'10' → 2  (1*2¹ + 0*2⁰)
'11' → 3  (1*2¹ + 1*2⁰)

get_counts():     {'00': 512, '11': 512}
get_int_counts(): {0: 512, 3: 512}
```

#### 4. Implementation
```python
int_counts = result[0].data.meas.get_int_counts()
print(int_counts)  # {0: 512, 3: 512}
```

#### 5. ⚠️ Trap Alert
**Trap: Qubit Ordering**
- Qiskit uses little-endian bit ordering
- Rightmost bit is qubit 0
- '10' means qubit 1 is |1⟩ and qubit 0 is |0⟩

#### 6. 🧠 Mnemonic
**"Int counts = Integers, not strings"**

#### 7. ⚡ Quick Check
**Q: For a 2-qubit Bell state, what would get_int_counts() return?**

<details>
<summary>Answer</summary>

**A**: `{0: ~512, 3: ~512}` (0='00', 3='11')
</details>

---

## 📊 Sampler Results - Consolidated Review

### Comparison Table

| Method | Returns | Use Case | Example Output |
|--------|---------|----------|----------------|
| `get_counts()` | `dict[str, int]` | Most common, exam default | `{'00': 512}` |
| `get_bitstrings()` | `list[str]` | Shot-by-shot analysis | `['00', '11', ...]` |
| `get_int_counts()` | `dict[int, int]` | Numerical processing | `{0: 512, 3: 512}` |

### Quick Reference Card
```
┌─────────────────────────────────────────────────────────────────┐
│ SAMPLER RESULT EXTRACTION - QUICK REFERENCE                     │
├─────────────────────────────────────────────────────────────────┤
│ PRIMARY (95% of exam questions):                                │
│   counts = result[0].data.meas.get_counts()                     │
│                                                                  │
│ ALTERNATIVES:                                                    │
│   bitstrings = result[0].data.meas.get_bitstrings()             │
│   int_counts = result[0].data.meas.get_int_counts()             │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONIC: "RIDMG" - Result Index Data Meas Get                  │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAP: Missing any access level = AttributeError!            │
│   ❌ result.data.meas.get_counts()     # Missing [0]            │
│   ❌ result[0].meas.get_counts()       # Missing .data          │
│   ✅ result[0].data.meas.get_counts()  # CORRECT                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Estimator Result Extraction

> **EXAM CRITICAL**: Second most tested pattern!
> Remember: `.evs` (plural) not `.ev`!

### Overview

Estimator returns expectation values (⟨ψ|O|ψ⟩) and standard deviations for observables. Unlike Sampler, results are floats not dictionaries.

---

### 🔹 evs - Expectation Values

#### 1. Definition
`.evs` (expectation values - plural!) returns the computed expectation value of the observable on the quantum state. It's a float, not a method.

#### 2. Analogy + Intuition
**Real-World Analogy**
If Sampler is like counting individual votes, Estimator is like calculating the average opinion score. You get one number summarizing the measurement.

**Intuition Builder**
- Expectation value = weighted average of observable eigenvalues
- For Pauli Z: ⟨Z⟩ ranges from -1 (all |1⟩) to +1 (all |0⟩)

#### 3. Math + Visual
**Mathematical Foundation**
$$\langle O \rangle = \langle\psi|O|\psi\rangle = \sum_i p_i \lambda_i$$

Where $p_i$ are measurement probabilities and $\lambda_i$ are eigenvalues.

**Visual Representation**
```
Estimator Result Structure:

   result (PrimitiveResult)
      │
      └──[0] (PubResult)
            │
            └──.data (DataBin)
                  │
                  ├── .evs  ──► 0.5 (float - expectation value)
                  └── .stds ──► 0.02 (float - standard deviation)
```

#### 4. Implementation (Basic → Advanced)
**Qiskit Syntax**
```python
expectation = result[0].data.evs  # Property, NOT a method!
```

**Basic Example**
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Create Bell state (no measurements!)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Define observable
obs = SparsePauliOp('ZZ')

# Run
estimator = StatevectorEstimator()
job = estimator.run([(qc, obs)])
result = job.result()

# EXAM CRITICAL: The pattern you MUST know
expectation = result[0].data.evs  # 1.0 for Bell state
std_dev = result[0].data.stds
print(f"⟨ZZ⟩ = {expectation}")
```

**Intermediate Example**
```python
# Multiple observables on same circuit
obs_list = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]

# Run as separate PUBs
pubs = [(qc, obs) for obs in obs_list]
job = estimator.run(pubs)
result = job.result()

# Access each result
for i, name in enumerate(['ZZ', 'XX', 'YY']):
    print(f"⟨{name}⟩ = {result[i].data.evs:.4f}")
```

#### 5. ⚠️ Trap Alert
**Trap 1: Singular vs Plural**
- ❌ **Wrong**: `result[0].data.ev` - Missing 's'!
- ❌ **Wrong**: `result[0].data.std` - Missing 's'!
- ✅ **Correct**: `result[0].data.evs` and `result[0].data.stds`

**Trap 2: Property vs Method**
- ❌ **Wrong**: `result[0].data.evs()` - It's a property, not method!
- ✅ **Correct**: `result[0].data.evs` - No parentheses!

```python
# ❌ WRONG
expectation = result[0].data.ev    # AttributeError: no attribute 'ev'
expectation = result[0].data.evs() # TypeError: 'float' not callable

# ✅ CORRECT
expectation = result[0].data.evs   # 0.5 (no parentheses!)
```

#### 6. 🧠 Mnemonic
**"EVS = Expectation ValueS (plural!)"**
- Always use the plural form: evs, stds
- No parentheses - they're properties, not methods!

**Alternative: "S for Standard and Single-point"**

#### 7. ⚡ Quick Check
**Q: Write the complete line to get expectation value from Estimator result.**

<details>
<summary>Answer</summary>

**A**: `expectation = result[0].data.evs`

Note: No parentheses! It's a property, not a method.
</details>

---

### 🔹 stds - Standard Deviations

#### 1. Definition
`.stds` returns the statistical uncertainty (standard deviation) of the expectation value measurement.

#### 2. Analogy + Intuition
**Real-World Analogy**
If `.evs` is the poll result ("54% approve"), `.stds` is the margin of error ("±3%").

#### 3. Implementation
```python
std_dev = result[0].data.stds
print(f"Uncertainty: ±{std_dev:.4f}")
```

#### 4. ⚠️ Trap Alert
**Trap: stds vs std**
- ❌ **Wrong**: `result[0].data.std`
- ✅ **Correct**: `result[0].data.stds` (plural!)

#### 5. 🧠 Mnemonic
**"Standards are plural"**

#### 6. ⚡ Quick Check
**Q: What does `.stds` represent?**

<details>
<summary>Answer</summary>

**A**: The standard deviation (uncertainty) of the expectation value measurement.
</details>

---

## 📊 Estimator Results - Consolidated Review

### Comparison with Sampler

| Aspect | Sampler | Estimator |
|--------|---------|-----------|
| **Primary Access** | `result[0].data.meas.get_counts()` | `result[0].data.evs` |
| **Return Type** | `dict[str, int]` | `float` |
| **Alternative** | `.get_bitstrings()` | `.stds` |
| **Circuit** | MUST have measurements | MUST NOT have measurements |
| **Input** | `(circuit,)` or `(circuit, params)` | `(circuit, observable)` |
| **Uses** | Counting outcomes | Computing expectation values |

### Quick Reference Card
```
┌─────────────────────────────────────────────────────────────────┐
│ ESTIMATOR RESULT EXTRACTION - QUICK REFERENCE                   │
├─────────────────────────────────────────────────────────────────┤
│ PRIMARY:                                                         │
│   expectation = result[0].data.evs    # Note: PROPERTY!         │
│   std_dev = result[0].data.stds                                  │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONIC: "EVS = Expectation ValueS (plural)"                   │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAPS:                                                       │
│   ❌ result[0].data.ev     # Missing 's'                        │
│   ❌ result[0].data.evs()  # Not a method!                      │
│   ✅ result[0].data.evs    # CORRECT                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 PUB Format (Primitive Unified Bloc)

> **EXAM CRITICAL**: PUB defines how to pass data to primitives.
> Different primitives have different PUB structures!

### Overview

PUB (Primitive Unified Bloc) is the standard input format for primitives. Sampler and Estimator have different PUB structures with different required/optional fields.

---

### 🔹 Sampler PUB Format

#### 1. Definition
Sampler PUB: `(circuit, parameter_values, shots)`

#### 2. Visual Representation
```
SAMPLER PUB = (circuit, parameter_values, shots)
               │         │                │
               │         │                └── Optional: int (default varies)
               │         └── Optional: list matching circuit.parameters
               └── Required: QuantumCircuit WITH measurements
```

#### 3. Implementation Examples

| Scenario | PUB Format | Example |
|----------|------------|---------|
| Basic circuit | `(circuit,)` | `sampler.run([(qc,)])` |
| With parameters | `(circuit, params)` | `sampler.run([(qc, [0.5])])` |
| Custom shots | `(circuit, None, shots)` | `sampler.run([(qc, None, 2048)])` |
| All options | `(circuit, params, shots)` | `sampler.run([(qc, [0.5], 4096)])` |

```python
# Basic
sampler.run([(qc,)])

# With parameters
sampler.run([(qc, [0.5, 1.0])])

# Custom shots (None for params placeholder)
sampler.run([(qc, None, 2048)])

# All options
sampler.run([(qc, [0.5, 1.0], 4096)])
```

#### 4. ⚠️ Trap Alert
**Trap: Trailing Comma Required for Single-Element Tuple**
- ❌ **Wrong**: `sampler.run([(circuit)])`
- ✅ **Correct**: `sampler.run([(circuit,)])`

```python
# ❌ WRONG
sampler.run([(qc)])      # This is a list with qc, not a tuple!
sampler.run([circuit])   # Not a tuple at all!

# ✅ CORRECT
sampler.run([(qc,)])     # Trailing comma makes it a tuple!
```

#### 5. 🧠 Mnemonic
**"Sampler: Circuit, Params, Shots - CPS"**

---

### 🔹 Estimator PUB Format

#### 1. Definition
Estimator PUB: `(circuit, observable, parameter_values, precision)`

#### 2. Visual Representation
```
ESTIMATOR PUB = (circuit, observable, parameter_values, precision)
                 │        │           │                 │
                 │        │           │                 └── Optional: float
                 │        │           └── Optional: list matching circuit.parameters
                 │        └── Required: SparsePauliOp (NOT string!)
                 └── Required: QuantumCircuit WITHOUT measurements
```

#### 3. Implementation Examples

| Scenario | PUB Format | Example |
|----------|------------|---------|
| Basic | `(circuit, observable)` | `estimator.run([(qc, obs)])` |
| With params | `(circuit, observable, params)` | `estimator.run([(qc, obs, [0.5])])` |
| With precision | `(circuit, obs, None, prec)` | `estimator.run([(qc, obs, None, 0.01)])` |
| All options | `(circuit, obs, params, prec)` | `estimator.run([(qc, obs, [0.5], 0.01)])` |

```python
# Basic
estimator.run([(qc, SparsePauliOp('ZZ'))])

# With parameters
estimator.run([(qc, obs, [0.5, 1.0])])

# With precision
estimator.run([(qc, obs, None, 0.01)])

# All options
estimator.run([(qc, obs, [0.5, 1.0], 0.01)])
```

#### 4. ⚠️ Trap Alert
**Trap 1: Observable Must Be SparsePauliOp**
- ❌ **Wrong**: `estimator.run([(qc, 'ZZ')])`
- ✅ **Correct**: `estimator.run([(qc, SparsePauliOp('ZZ'))])`

**Trap 2: Circuit Must NOT Have Measurements**
- ❌ **Wrong**: Using circuit with `measure_all()`
- ✅ **Correct**: Use circuit without measurements

```python
# ❌ WRONG
estimator.run([(qc, 'ZZ')])                    # String not SparsePauliOp!
estimator.run([(qc_with_measurements, obs)])   # Has measurements!

# ✅ CORRECT
estimator.run([(qc, SparsePauliOp('ZZ'))])     # SparsePauliOp object
```

#### 5. 🧠 Mnemonic
**"Estimator: Circuit, Observable, Params, Precision - COPP"**

---

## 📊 PUB Format - Consolidated Review

### Side-by-Side Comparison

| Aspect | Sampler PUB | Estimator PUB |
|--------|-------------|---------------|
| **Format** | `(circuit, params, shots)` | `(circuit, obs, params, precision)` |
| **Required** | circuit | circuit, observable |
| **Circuit** | WITH measurements | WITHOUT measurements |
| **Observable** | N/A | SparsePauliOp (required!) |

### Common PUB Mistakes
```python
# SAMPLER MISTAKES:
❌ sampler.run([circuit])           # Not a list of tuples!
❌ sampler.run([(circuit)])         # Missing trailing comma!
❌ sampler.run([(circuit_no_meas,)])# No measurements!
✅ sampler.run([(circuit,)])        # Correct!

# ESTIMATOR MISTAKES:
❌ estimator.run([(circuit,)])      # Missing observable!
❌ estimator.run([(circuit, 'ZZ')]) # String not SparsePauliOp!
❌ estimator.run([(qc_meas, obs)])  # Has measurements!
✅ estimator.run([(circuit, SparsePauliOp('ZZ'))]) # Correct!
```

### Quick Reference Card
```
┌─────────────────────────────────────────────────────────────────┐
│ PUB FORMAT - QUICK REFERENCE                                     │
├─────────────────────────────────────────────────────────────────┤
│ SAMPLER PUB = (circuit, params, shots)                          │
│   └─ Circuit MUST have measurements                              │
│   └─ Trailing comma required: (circuit,)                        │
│                                                                  │
│ ESTIMATOR PUB = (circuit, observable, params, precision)        │
│   └─ Circuit MUST NOT have measurements                          │
│   └─ Observable MUST be SparsePauliOp                           │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONICS:                                                       │
│   Sampler: "CPS" - Circuit, Params, Shots                       │
│   Estimator: "COPP" - Circuit, Observable, Params, Precision    │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAP: Trailing comma for single-element tuple!              │
│   ❌ [(circuit)]  →  ✅ [(circuit,)]                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Multiple Circuits and Metadata

> Processing batch results and accessing execution information.

### Overview

Primitives support batch execution of multiple circuits. Results are indexed by position, and metadata provides execution details.

---

### 🔹 Multiple Circuit Processing

#### 1. Definition
When running multiple circuits, access results using indices: `result[0]`, `result[1]`, etc.

#### 2. Implementation
**Iteration Pattern**
```python
job = sampler.run([(qc1,), (qc2,), (qc3,)])
result = job.result()

# Iterate through all results
for i, pub_result in enumerate(result):
    counts = pub_result.data.meas.get_counts()
    print(f"Circuit {i}: {counts}")
```

**Direct Indexing Pattern**
```python
counts_0 = result[0].data.meas.get_counts()  # First circuit
counts_1 = result[1].data.meas.get_counts()  # Second circuit
counts_2 = result[2].data.meas.get_counts()  # Third circuit
```

#### 3. ⚠️ Trap Alert
**Trap: Index Out of Range**
- Number of results = number of PUBs submitted
- Accessing `result[n]` where n >= number of circuits raises IndexError

#### 4. 🧠 Mnemonic
**"One PUB, One Result"**
- Each tuple in the input list produces one indexed result

#### 5. ⚡ Quick Check
**Q: If you run `sampler.run([(qc1,), (qc2,)])`, how do you get counts for qc2?**

<details>
<summary>Answer</summary>

**A**: `result[1].data.meas.get_counts()` (second circuit = index 1)
</details>

---

### 🔹 Metadata Access

#### 1. Definition
Metadata contains execution information: shots, timing, backend details.

#### 2. Implementation
```python
metadata = result[0].metadata
print(f"Shots: {metadata.get('shots', 'N/A')}")
print(f"Duration: {metadata.get('execution_time', 'N/A')}")
```

#### 3. Common Metadata Fields
| Field | Type | Description |
|-------|------|-------------|
| `shots` | int | Number of shots executed |
| `execution_time` | float | Time to execute |
| Backend-specific fields | varies | Depends on backend |

---

## 🔧 Job Management

> JobStatus enumeration and service.jobs() filtering for IBM Quantum.

---

### 🔹 JobStatus Enumeration

#### 1. Definition
`JobStatus` indicates the current state of a job on IBM Quantum backends.

#### 2. All Status Values (MEMORIZE!)
```python
from qiskit.providers import JobStatus

JobStatus.INITIALIZING   # Job being initialized
JobStatus.QUEUED         # Waiting in queue
JobStatus.VALIDATING     # Being validated
JobStatus.RUNNING        # Currently executing
JobStatus.CANCELLED      # User cancelled
JobStatus.DONE           # Successfully completed
JobStatus.ERROR          # Failed with error
```

#### 3. Visual: Job Lifecycle
```
INITIALIZING → QUEUED → VALIDATING → RUNNING → DONE
                                              ↗
                              or → CANCELLED
                                              ↘
                                    or → ERROR
```

#### 4. Implementation
```python
job = sampler.run([(qc,)])
status = job.status()

if status == JobStatus.DONE:
    result = job.result()
elif status == JobStatus.ERROR:
    print("Job failed!")
elif status == JobStatus.QUEUED:
    print(f"Position: {job.queue_position()}")
```

#### 5. ⚠️ Trap Alert
**Trap: String vs Enum Comparison**
- ❌ **Wrong**: `if job.status() == "DONE":`
- ✅ **Correct**: `if job.status() == JobStatus.DONE:`

#### 6. 🧠 Mnemonic
**"IQVRCDE" - "I Queue Very Real Challenges Daily, Expert!"**
- **I**NITIALIZING → **Q**UEUED → **V**ALIDATING → **R**UNNING → **C**ANCELLED/**D**ONE/**E**RROR

#### 7. ⚡ Quick Check
**Q: Which JobStatus allows you to call job.result()?**

<details>
<summary>Answer</summary>

**A**: `JobStatus.DONE` (only after successful completion)
</details>

---

### 🔹 service.jobs() Filtering

#### 1. Definition
`service.jobs()` retrieves job history with filtering options.

#### 2. Parameters Table
| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | int | Max jobs to return (default: 10) |
| `skip` | int | Jobs to skip (pagination) |
| `backend_name` | str | Filter by backend |
| `pending` | bool | True=pending, False=completed |
| `created_after` | datetime | Jobs after this time |
| `created_before` | datetime | Jobs before this time |
| `program_id` | str | Filter by program |
| `job_tags` | list[str] | Filter by tags |

#### 3. Implementation
```python
from qiskit_ibm_runtime import QiskitRuntimeService
from datetime import datetime, timedelta

service = QiskitRuntimeService()

# Get last 50 jobs
jobs = service.jobs(limit=50)

# Filter by backend
jobs = service.jobs(backend_name="ibm_brisbane")

# Only completed jobs
jobs = service.jobs(pending=False)

# Last 7 days
start = datetime.now() - timedelta(days=7)
jobs = service.jobs(created_after=start)

# Combined filters
jobs = service.jobs(
    backend_name="ibm_brisbane",
    pending=False,
    limit=20
)
```

#### 4. 🧠 Mnemonic
**"LSPPC" - "List, Skip, Pending, Parameters, Created"**
- Common filter parameters

---

### 🔹 RuntimeEncoder/RuntimeDecoder

#### 1. Definition
`RuntimeEncoder`/`RuntimeDecoder` serialize Qiskit objects to/from JSON for IBM Quantum transmission.

#### 2. When to Use
| Use Case | Use Encoder/Decoder? |
|----------|---------------------|
| Primitives API | No - automatic |
| Custom Runtime Programs | **YES** |
| Saving circuits to files | Optional |
| REST API calls | **YES** |

#### 3. Implementation
```python
import json
from qiskit_ibm_runtime import RuntimeEncoder, RuntimeDecoder

# Encode
data = {'circuit': qc, 'observable': SparsePauliOp('ZZ')}
encoded = json.dumps(data, cls=RuntimeEncoder)

# Decode
recovered = json.loads(encoded, cls=RuntimeDecoder)
```

#### 4. Supported Types
- QuantumCircuit
- SparsePauliOp, Pauli, Operator
- Parameter, ParameterVector
- numpy arrays
- Standard Python types

---

## ⚠️ MASTER TRAP LIST

> All traps from all topics - organized for final review.

### Trap Summary Table

| # | Topic | Trap Name | ❌ Wrong | ✅ Correct | Mnemonic |
|---|-------|-----------|----------|-----------|----------|
| 1 | Sampler | Missing [0] | `result.data.meas` | `result[0].data.meas` | "RIDMG" |
| 2 | Sampler | Missing .data | `result[0].meas` | `result[0].data.meas` | "RIDMG" |
| 3 | Sampler | Missing .meas | `result[0].data.get_counts()` | `result[0].data.meas.get_counts()` | "RIDMG" |
| 4 | Sampler | Missing .get_ | `result[0].data.meas.counts()` | `result[0].data.meas.get_counts()` | "RIDMG" |
| 5 | Estimator | Singular ev | `result[0].data.ev` | `result[0].data.evs` | "EVS = plural" |
| 6 | Estimator | Method call | `result[0].data.evs()` | `result[0].data.evs` | "Property, no ()" |
| 7 | PUB | Missing comma | `[(circuit)]` | `[(circuit,)]` | "Trailing comma!" |
| 8 | PUB | String obs | `(qc, 'ZZ')` | `(qc, SparsePauliOp('ZZ'))` | "COPP" |
| 9 | JobStatus | String compare | `== "DONE"` | `== JobStatus.DONE` | "Use enum" |

### Critical Traps Deep Dive

**🚨 Critical Trap 1: The RIDMG Chain**
```python
# ❌ WRONG - Missing any level fails!
result.data.meas.get_counts()       # Missing [0]
result[0].meas.get_counts()         # Missing .data
result[0].data.get_counts()         # Missing .meas
result[0].data.meas.counts()        # Missing .get_

# ✅ CORRECT - All levels required!
result[0].data.meas.get_counts()
```
- **Why students fall for it**: Seems redundant, forget one level
- **How to avoid**: Memorize "RIDMG" - Result Index Data Meas Get

**🚨 Critical Trap 2: EVS Plural and Property**
```python
# ❌ WRONG
result[0].data.ev      # Missing 's'!
result[0].data.evs()   # Not a method!

# ✅ CORRECT
result[0].data.evs     # Property - no parentheses!
```
- **Why students fall for it**: "ev" looks complete, methods need ()
- **How to avoid**: "EVS = Expectation ValueS" (plural, property)

**🚨 Critical Trap 3: Trailing Comma**
```python
# ❌ WRONG
sampler.run([(circuit)])     # This is [(circuit)], not [(circuit,)]

# ✅ CORRECT
sampler.run([(circuit,)])    # Trailing comma creates tuple!
```
- **Why students fall for it**: Python allows `(x)` without comma
- **How to avoid**: Single-element tuples ALWAYS need trailing comma

---

## 📝 PRACTICE EXAM

### Part A: Quick Fire (1-2 minutes each)

**Q1**: What method extracts measurement counts from Sampler?
<details>
<summary>Answer</summary>

**A**: `result[0].data.meas.get_counts()`
</details>

**Q2**: What property gives expectation value from Estimator?
<details>
<summary>Answer</summary>

**A**: `result[0].data.evs` (plural, property not method!)
</details>

**Q3**: What's wrong with `estimator.run([(qc, 'ZZ')])`?
<details>
<summary>Answer</summary>

**A**: Observable must be SparsePauliOp, not string. Use `SparsePauliOp('ZZ')`
</details>

**Q4**: How do you access the third circuit's results?
<details>
<summary>Answer</summary>

**A**: `result[2].data.meas.get_counts()` (zero-indexed)
</details>

**Q5**: What's wrong with `result[0].data.evs()`?
<details>
<summary>Answer</summary>

**A**: `.evs` is a property, not a method. Remove the parentheses: `result[0].data.evs`
</details>

### Part B: Code Analysis (3-5 minutes each)

**Q6**: What does this code print?
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
result = job.result()
print(len(result[0].data.meas.get_bitstrings()))
```
<details>
<summary>Answer</summary>

**A**: `1000` (number of shots, not unique outcomes)
</details>

**Q7**: Which line has an error?
```python
estimator = StatevectorEstimator()
qc = QuantumCircuit(2)
qc.h(0)
qc.measure_all()  # Line A
obs = SparsePauliOp('ZZ')
job = estimator.run([(qc, obs)])  # Line B
```
<details>
<summary>Answer</summary>

**A**: Line A - Estimator circuits must NOT have measurements. Remove `qc.measure_all()`.
</details>

**Q8**: What's returned?
```python
result = job.result()
counts = result[0].data.meas.get_int_counts()
# For Bell state measurement
```
<details>
<summary>Answer</summary>

**A**: `{0: ~500, 3: ~500}` - Integer keys (0='00', 3='11')
</details>

---

**Q9**: What does this code output?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1)
qc.x(0)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=100)
result = job.result()

counts = result[0].data.meas.get_counts()
print(sum(counts.values()))
```
<details>
<summary>Answer</summary>

**A**: `100`

**Explanation**:
1. Creates |1⟩ state with X gate
2. Measures all qubits
3. Runs 100 shots
4. `get_counts()` returns `{'1': 100}`
5. `sum(counts.values())` = 100 (total shots)

**Topic**: get_counts() returns counts that sum to shots
</details>

---

**Q10**: What's wrong with this code and what will happen?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()  # Has measurements!

obs = SparsePauliOp('ZZ')
estimator = StatevectorEstimator()
job = estimator.run([(qc, obs)])
result = job.result()
print(result[0].data.evs)
```
<details>
<summary>Answer</summary>

**Problem**: Circuit has measurements but Estimator requires circuits WITHOUT measurements.

**Result**: This will raise an error. Estimator computes expectation values, not measurement statistics.

**Fix**: Remove `qc.measure_all()`

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO measurements for Estimator!
```

**Topic**: Estimator circuit requirements
</details>

---

**Q11**: What does this code print?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc1,), (qc2,)], shots=1000)
result = job.result()

print(len(result))
print('1' in result[1].data.meas.get_counts())
```
<details>
<summary>Answer</summary>

**Output**:
```
2
True
```

**Explanation**:
1. Two PUBs submitted → `len(result)` = 2
2. `result[1]` is qc2 (X gate, always measures |1⟩)
3. `get_counts()` returns `{'1': 1000}`
4. `'1' in counts` → True

**Topic**: Multiple circuit result indexing
</details>

---

**Q12**: What's the output?
```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Observable ZZ
obs = SparsePauliOp('ZZ')

estimator = StatevectorEstimator()
job = estimator.run([(qc, obs)])
result = job.result()

print(type(result[0].data.evs).__name__)
print(result[0].data.evs == 1.0)
```
<details>
<summary>Answer</summary>

**Output**:
```
float64
True
```

**Explanation**:
1. Bell state |00⟩ + |11⟩ (normalized) has ⟨ZZ⟩ = 1.0
2. `.evs` returns a numpy float64
3. ZZ eigenvalue: +1 for |00⟩ and |11⟩, -1 for |01⟩ and |10⟩
4. Bell state only has |00⟩ and |11⟩, so ⟨ZZ⟩ = 1.0

**Topic**: Estimator expectation values
</details>

---

**Q13**: Fix this code to extract counts properly:
```python
result = job.result()
# These all fail - why?
# counts = result.data.meas.get_counts()
# counts = result[0].meas.get_counts()
# counts = result[0].data.get_counts()
```
<details>
<summary>Answer</summary>

**All three are wrong because they're missing access levels!**

1. `result.data.meas.get_counts()` - Missing `[0]` index
2. `result[0].meas.get_counts()` - Missing `.data`
3. `result[0].data.get_counts()` - Missing `.meas`

**Correct**:
```python
counts = result[0].data.meas.get_counts()
```

**Mnemonic**: "RIDMG" - Result Index Data Meas Get

**Topic**: Sampler result access chain
</details>

---

### Part C: Scenario-Based (5-7 minutes each)

**Q14**: You're building a quantum application that needs to run the same circuit with different parameters and compare results. Write complete code to:
1. Create a parameterized circuit
2. Run with 3 different parameter values
3. Extract and print counts for each

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
import numpy as np

# Step 1: Create parameterized circuit
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.ry(theta, 0)
qc.measure_all()

# Step 2: Define parameter values
param_values = [[0], [np.pi/2], [np.pi]]  # 0, π/2, π

# Step 3: Create PUBs with different parameters
pubs = [(qc, params) for params in param_values]

# Step 4: Run Sampler
sampler = StatevectorSampler()
job = sampler.run(pubs, shots=1000)
result = job.result()

# Step 5: Extract and print counts for each
labels = ['θ=0 (|0⟩)', 'θ=π/2 (superposition)', 'θ=π (|1⟩)']
for i, label in enumerate(labels):
    counts = result[i].data.meas.get_counts()
    print(f"{label}: {counts}")
```

**Expected Output**:
```
θ=0 (|0⟩): {'0': 1000}
θ=π/2 (superposition): {'0': ~500, '1': ~500}
θ=π (|1⟩): {'1': 1000}
```

**Topics combined**: Parameterized circuits, multiple PUBs, result indexing
</details>

---

**Q15**: You need to measure both ZZ and XX observables on a Bell state and check if they both equal 1. Write complete code.

<details>
<summary>Answer</summary>

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Step 1: Create Bell state (NO measurements!)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Step 2: Define observables
obs_zz = SparsePauliOp('ZZ')
obs_xx = SparsePauliOp('XX')

# Step 3: Create PUBs
pubs = [(qc, obs_zz), (qc, obs_xx)]

# Step 4: Run Estimator
estimator = StatevectorEstimator()
job = estimator.run(pubs)
result = job.result()

# Step 5: Extract expectation values
evs_zz = result[0].data.evs
evs_xx = result[1].data.evs

print(f"⟨ZZ⟩ = {evs_zz}")
print(f"⟨XX⟩ = {evs_xx}")
print(f"Both equal 1.0: {evs_zz == 1.0 and evs_xx == 1.0}")
```

**Expected Output**:
```
⟨ZZ⟩ = 1.0
⟨XX⟩ = 1.0
Both equal 1.0: True
```

**Key insight**: Bell state |Φ+⟩ has ⟨ZZ⟩ = ⟨XX⟩ = 1, ⟨YY⟩ = -1

**Topics combined**: Estimator, multiple observables, Bell state properties
</details>

---

**Q16**: Write a function that takes a Sampler result and returns the most frequently measured state and its probability.

<details>
<summary>Answer</summary>

```python
def get_most_frequent_state(result):
    """
    Extract the most frequently measured state from Sampler result.
    
    Args:
        result: PrimitiveResult from Sampler
        
    Returns:
        tuple: (state, probability)
    """
    # Step 1: Get counts
    counts = result[0].data.meas.get_counts()
    
    # Step 2: Find most frequent state
    most_frequent = max(counts, key=counts.get)
    
    # Step 3: Calculate probability
    total_shots = sum(counts.values())
    probability = counts[most_frequent] / total_shots
    
    return most_frequent, probability

# Example usage
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.x(0)  # |01⟩ state (little-endian: qubit 0 is rightmost)
qc.measure_all()

sampler = StatevectorSampler()
job = sampler.run([(qc,)], shots=1000)
result = job.result()

state, prob = get_most_frequent_state(result)
print(f"Most frequent: {state} with probability {prob:.2%}")
# Output: Most frequent: 01 with probability 100.00%
```

**Topics combined**: Result extraction, counts processing, probability calculation
</details>

---

### Score Yourself

| Section | Total Qs | Your Score | Percentage |
|---------|----------|------------|------------|
| Part A (Quick Fire) | 5 | /5 | % |
| Part B (Code Analysis) | 8 | /8 | % |
| Part C (Scenarios) | 3 | /3 | % |
| **TOTAL** | **16** | **/16** | **%** |

**Interpretation**:
- 90-100%: Ready for Section 7 exam questions
- 75-89%: Review the RIDMG pattern and evs property
- Below 75%: Re-study result extraction hierarchy

---

## 💡 KEY TAKEAWAYS

## Concept Mastery Checklist

```
□ I understand the result hierarchy: PrimitiveResult → PubResult → DataBin
□ I know Sampler returns counts (dict), Estimator returns floats
□ I understand the difference between get_counts(), get_bitstrings(), get_int_counts()
□ I know len(get_bitstrings()) = shots, len(get_counts()) = unique outcomes
□ I understand PUB format: Sampler (circuit, params, shots), Estimator (circuit, obs, params, precision)
□ I know Sampler circuits MUST have measurements
□ I know Estimator circuits MUST NOT have measurements
□ I understand multiple circuit result indexing (result[0], result[1], ...)
□ I know all JobStatus values (INITIALIZING, QUEUED, VALIDATING, RUNNING, CANCELLED, DONE, ERROR)
```

## Code Mastery Checklist

```
□ I can write result[0].data.meas.get_counts() from memory
□ I can write result[0].data.evs from memory (no parentheses!)
□ I can write result[0].data.stds from memory
□ I can iterate through multiple circuit results: for pub in result:
□ I can access specific circuit: result[i].data.meas.get_counts()
□ I can create Sampler PUB: [(circuit,)] with trailing comma
□ I can create Estimator PUB: [(circuit, SparsePauliOp('ZZ'))]
□ I can check job status: job.status() == JobStatus.DONE
□ I can filter jobs: service.jobs(pending=False, limit=10)
```

## Trap Avoidance Checklist

```
□ I won't forget [0] index: result[0].data (not result.data)
□ I won't forget .data: result[0].data.meas (not result[0].meas)
□ I won't forget .meas: result[0].data.meas.get_counts() (not result[0].data.get_counts())
□ I won't forget .get_: get_counts() not counts()
□ I won't use singular: evs not ev, stds not std
□ I won't call evs as method: result[0].data.evs not result[0].data.evs()
□ I won't forget trailing comma: [(circuit,)] not [(circuit)]
□ I won't use string for observable: SparsePauliOp('ZZ') not 'ZZ'
□ I won't compare JobStatus with string: == JobStatus.DONE not == "DONE"
```

## Mnemonic Recall Box

```
┌─────────────────────────────────────────────────────────────────┐
│  "RIDMG" - Result Index Data Meas Get                           │
│  → result[0].data.meas.get_counts()                             │
│                                                                  │
│  "EVS = Expectation ValueS (plural)"                            │
│  → result[0].data.evs (property, not method!)                   │
│                                                                  │
│  "CPS" - Circuit, Params, Shots                                 │
│  → Sampler PUB format                                           │
│                                                                  │
│  "COPP" - Circuit, Observable, Params, Precision                │
│  → Estimator PUB format                                         │
│                                                                  │
│  "IQVRCDE" - I Queue Very Real Challenges Daily, Expert!        │
│  → INITIALIZING, QUEUED, VALIDATING, RUNNING, CANCELLED,        │
│    DONE, ERROR                                                  │
│                                                                  │
│  "Trailing comma for tuples"                                    │
│  → (circuit,) not (circuit)                                     │
└─────────────────────────────────────────────────────────────────┘
```

## One-Page Summary Box

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        RESULT EXTRACTION QUICK REFERENCE                      │
├──────────────────────────────────────────────────────────────────────────────┤
│  SAMPLER RESULTS (95% of exam questions)                                      │
│  ───────────────────────────────────────                                     │
│  counts = result[0].data.meas.get_counts()     # {'00': 512, '11': 512}      │
│  bitstrings = result[0].data.meas.get_bitstrings()  # ['00', '11', ...]      │
│  int_counts = result[0].data.meas.get_int_counts()  # {0: 512, 3: 512}       │
│                                                                               │
│  ESTIMATOR RESULTS                                                            │
│  ─────────────────                                                           │
│  expectation = result[0].data.evs    # float - NO PARENTHESES!               │
│  std_dev = result[0].data.stds       # float - NO PARENTHESES!               │
│                                                                               │
│  PUB FORMATS                                                                  │
│  ───────────                                                                 │
│  Sampler:   sampler.run([(circuit,)])                   # CPS                │
│             sampler.run([(circuit, params, shots)])                          │
│                                                                               │
│  Estimator: estimator.run([(circuit, SparsePauliOp('ZZ'))])  # COPP          │
│             estimator.run([(circuit, obs, params, precision)])               │
│                                                                               │
│  MULTIPLE CIRCUITS                                                            │
│  ─────────────────                                                           │
│  result[0].data.meas.get_counts()   # First circuit                          │
│  result[1].data.meas.get_counts()   # Second circuit                         │
│  for i, pub in enumerate(result):   # Iterate all                            │
│      counts = pub.data.meas.get_counts()                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  ⚠️ TOP EXAM TRAPS                                                            │
│  ──────────────────                                                          │
│  ❌ result.data.meas.get_counts()    # Missing [0]                            │
│  ❌ result[0].meas.get_counts()      # Missing .data                          │
│  ❌ result[0].data.get_counts()      # Missing .meas                          │
│  ❌ result[0].data.meas.counts()     # Missing .get_                          │
│  ❌ result[0].data.ev                # Missing 's' → use evs                  │
│  ❌ result[0].data.evs()             # Property not method!                   │
│  ❌ [(circuit)]                      # Missing comma → [(circuit,)]           │
│  ✅ result[0].data.meas.get_counts() # CORRECT                                │
│  ✅ result[0].data.evs               # CORRECT                                │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Files in This Section

| File | Purpose | Key Content |
|------|---------|-------------|
| [README.md](README.md) | Complete learning guide | Theory, 9 traps, 16 practice questions, checklists |
| [result_extraction.ipynb](result_extraction.ipynb) | CODE LABORATORY | Executable examples, trap demonstrations, challenges |
| [README_OLD.md](README_OLD.md) | Backup | Previous version for reference |

---

## ➡️ Next Steps

1. **Complete the notebook**: Run all cells in [result_extraction.ipynb](result_extraction.ipynb)
2. **Practice the patterns**: Write RIDMG pattern 10 times from memory
3. **Do trap identification**: Find errors in 5 code snippets without looking
4. **Take Practice Exam**: Score at least 90% on the 16-question exam above
5. **Review Section 8**: Continue to [Section 8: OpenQASM](../section_8_openqasm/README.md) for QASM import/export

---

## 🔗 Related Sections

- **Section 5**: Sampler primitive usage
- **Section 6**: Estimator primitive usage  
- **Section 3**: Circuit creation for measurement
- **Section 4**: Transpilation before execution

---

## 📚 Additional Resources

- Qiskit Primitives Guide: [docs.quantum.ibm.com/guides/primitives](https://docs.quantum.ibm.com/guides/primitives)
- IBM Quantum Runtime: [docs.quantum.ibm.com/api/qiskit-ibm-runtime](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime)
- Result Types Reference: [docs.quantum.ibm.com/api/qiskit/primitives](https://docs.quantum.ibm.com/api/qiskit/primitives)

---

**🎯 Exam Success Tip**: Write these two patterns 10 times before the exam!
- `result[0].data.meas.get_counts()`
- `result[0].data.evs`

---

*Last Updated: 2025-01-15 | Qiskit Version: 1.x | Exam Weight: ~10%*
