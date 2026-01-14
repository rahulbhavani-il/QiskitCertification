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

## ✅ Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS:
□ Result hierarchy: PrimitiveResult → PubResult → DataBin (3-level structure)
□ Sampler returns counts (dictionary), Estimator returns expectation values (floats)
□ get_counts() returns dict with string keys: {'00': 512, '11': 512}
□ get_bitstrings() returns list of all shot results: ['00', '11', '00', ...]
□ get_int_counts() returns dict with integer keys: {0: 512, 3: 512}
□ len(get_bitstrings()) equals shots, len(get_counts()) equals unique outcomes
□ PUB format for Sampler: (circuit, params, shots) - measurements required
□ PUB format for Estimator: (circuit, observable, params, precision) - no measurements
□ Sampler circuits MUST have measurements (qc.measure_all())
□ Estimator circuits MUST NOT have measurements
□ Multiple circuits accessed by index: result[0], result[1], result[2]
□ JobStatus enum values: INITIALIZING, QUEUED, VALIDATING, RUNNING, CANCELLED, DONE, ERROR
□ BitArray provides multiple access methods for measurement results
□ DataBin attributes vary by primitive: Sampler has register names, Estimator has evs/stds
□ result[0].data.evs and result[0].data.stds are properties (not methods!)

RESULT OBJECT TYPES:
□ PrimitiveResult: Top-level container returned by job.result()
□ PubResult: Individual result for one PUB (circuit-observable pair)
□ DataBin: Container for actual data (counts, bitstrings, evs, stds)
□ BitArray: 2D array structure [shots × num_bits] for measurement outcomes
□ JobStatus: Enum class representing job lifecycle states
□ Job: Object representing submitted work, has status() and result() methods
□ Metadata: Dict-like object containing execution information

DATA ACCESS PATTERNS:
□ result[i] indexes into PUB results (0-based indexing)
□ result[i].data accesses DataBin for i-th PUB
□ result[i].data.register_name accesses BitArray for specific register
□ BitArray.get_counts() method returns dict of outcome frequencies
□ BitArray.get_bitstrings() method returns list of all measurement outcomes
□ BitArray.get_int_counts() method returns dict with integer keys
□ result[i].metadata accesses execution metadata (shots, circuit_metadata, etc.)
□ len(result) returns number of PUBs in result

CONSTRAINTS & LIMITATIONS:
□ PrimitiveResult is list-like but not actually a list (custom container)
□ Cannot modify result data after retrieval (immutable)
□ get_counts() preserves shot allocation: sum(counts.values()) == shots
□ get_bitstrings() always returns list with length equal to shots
□ get_int_counts() uses binary interpretation with LSB ordering
□ evs and stds are numpy arrays, even for single observable
□ Register names must match circuit's classical register names
□ JobStatus comparisons must use enum values, not strings
□ job.result() blocks execution until completion (synchronous)
□ Cancelled jobs cannot retrieve results (raises error)
□ Error jobs raise exception when calling result()

KEY DEFINITIONS:
□ Shots: Number of times circuit is executed (repetitions)
□ Outcome: Specific bitstring result from one shot (e.g., '00', '11')
□ Unique outcomes: Distinct bitstrings that appeared (keys in get_counts())
□ Counts: Dictionary mapping outcomes to their frequencies
□ Bitstrings: Ordered list of all measurement outcomes (one per shot)
□ Expectation value: ⟨O⟩ = ⟨ψ|O|ψ⟩ (Estimator result)
□ Standard deviation: Statistical uncertainty in expectation value
□ PUB (Primitive Unified Bloc): Tuple specifying one circuit execution
□ Register name: Identifier for classical register (e.g., 'meas', 'c', 'output')
□ Job ID: Unique identifier for submitted job (string)

JOB LIFECYCLE:
□ INITIALIZING: Job object created, preparing for submission
□ QUEUED: Job waiting in queue for available resources
□ VALIDATING: Backend validating circuit and parameters
□ RUNNING: Circuit actively executing on quantum hardware
□ DONE: Execution completed successfully, results available
□ ERROR: Execution failed, error message available
□ CANCELLED: User or system cancelled job before completion
□ Terminal states: DONE, ERROR, CANCELLED (no further transitions)
□ job.done() returns True for all terminal states
□ job.in_final_state() checks if job has reached terminal state

BITARRAY SPECIFICS:
□ BitArray shape: (num_shots, num_bits) - 2D numpy-like array
□ BitArray is read-only: cannot modify after creation
□ Slicing supported: bit_array[:, 0] gets first qubit results for all shots
□ Boolean indexing supported: bit_array[bit_array[:, 0] == 1]
□ Conversion methods: get_counts(), get_bitstrings(), get_int_counts()
□ Memory efficient: stores bits compactly, not as strings
□ Iteration: for bitstring in bit_array.get_bitstrings() iterates outcomes

METADATA CONTENTS:
□ shots: Actual number of shots executed
□ circuit_metadata: Information about circuit structure
□ readout_mitigation_overhead: Time spent on mitigation (if enabled)
□ num_circuits: Number of circuits in PUB (usually 1)
□ execution_time: Time spent executing on hardware
□ Some metadata fields backend-specific (hardware dependent)

VERSION-SPECIFIC:
□ V2 primitives return PrimitiveResult (consistent interface)
□ V1 primitives deprecated: different result structure (avoid!)
□ get_memory() replaced by get_bitstrings() in V2
□ Result.get_counts() (V1) vs result[0].data.meas.get_counts() (V2)
□ V2 enforces PUB structure, V1 was more flexible but inconsistent
```

### 💻 Code Pattern Checklist
```
ESSENTIAL IMPORTS:
□ from qiskit.primitives import StatevectorSampler, StatevectorEstimator
□ from qiskit_ibm_runtime import SamplerV2, EstimatorV2
□ from qiskit_ibm_runtime import QiskitRuntimeService
□ from qiskit.providers import JobStatus  # for status comparisons
□ from qiskit.quantum_info import SparsePauliOp
□ import numpy as np  # for array operations on results

SAMPLER RESULT EXTRACTION:
□ result = job.result()  # PrimitiveResult object
□ counts = result[0].data.meas.get_counts()  # dict: {'00': 512, '11': 512}
□ bitstrings = result[0].data.meas.get_bitstrings()  # list: ['00', '11', '00', ...]
□ int_counts = result[0].data.meas.get_int_counts()  # dict: {0: 512, 3: 512}
□ num_shots = len(bitstrings)  # or sum(counts.values())
□ unique_outcomes = len(counts)  # number of distinct bitstrings
□ most_frequent = max(counts, key=counts.get)  # most common outcome

ESTIMATOR RESULT EXTRACTION:
□ result = job.result()  # PrimitiveResult object
□ expectation = result[0].data.evs  # numpy array (PROPERTY, no parentheses!)
□ std_dev = result[0].data.stds  # numpy array (PROPERTY, no parentheses!)
□ ev_value = result[0].data.evs[0]  # extract first expectation value
□ std_value = result[0].data.stds[0]  # extract first standard deviation
□ all_evs = [result[i].data.evs for i in range(len(result))]  # collect all

MULTIPLE PUB RESULTS:
□ for i, pub_result in enumerate(result):  # iterate all PUBs
□     counts = pub_result.data.meas.get_counts()
□ first_result = result[0].data.meas.get_counts()  # first PUB
□ second_result = result[1].data.meas.get_counts()  # second PUB
□ num_pubs = len(result)  # total number of PUBs
□ all_counts = [result[i].data.meas.get_counts() for i in range(len(result))]

CUSTOM REGISTER NAMES:
□ from qiskit.circuit import ClassicalRegister
□ cr = ClassicalRegister(2, 'output')  # custom name 'output'
□ qc.add_register(cr)
□ qc.measure([0, 1], cr)
□ counts = result[0].data.output.get_counts()  # use 'output' not 'meas'
□ register_name = qc.cregs[0].name  # get register name programmatically
□ bit_array = getattr(result[0].data, register_name)  # dynamic access

JOB STATUS CHECKING:
□ status = job.status()  # returns JobStatus enum
□ if job.status() == JobStatus.DONE:  # check if complete
□     result = job.result()
□ if job.status() == JobStatus.ERROR:  # check if failed
□     print(job.error_message())
□ is_done = job.done()  # boolean, True when in terminal state
□ job.wait_for_final_state()  # blocking wait for completion
□ job.wait_for_final_state(timeout=300)  # wait with timeout

JOB MANAGEMENT:
□ job_id = job.job_id()  # get unique job ID
□ service = QiskitRuntimeService()
□ job = service.job(job_id)  # retrieve job by ID
□ jobs = service.jobs(limit=10)  # get recent jobs
□ jobs = service.jobs(pending=False)  # get completed jobs only
□ jobs = service.jobs(program_id='sampler')  # filter by program
□ job.cancel()  # cancel running job
□ job.refresh()  # update job status from server

RESULT METADATA ACCESS:
□ metadata = result[0].metadata  # get metadata dict
□ actual_shots = metadata['shots']  # actual shots executed
□ circuit_metadata = metadata.get('circuit_metadata', {})
□ execution_time = metadata.get('execution_time')
□ for key, value in metadata.items():  # iterate metadata

BITARRAY OPERATIONS:
□ bit_array = result[0].data.meas  # get BitArray
□ shape = bit_array.shape  # (num_shots, num_bits)
□ num_shots, num_bits = bit_array.shape
□ first_qubit_results = bit_array[:, 0]  # all shots for qubit 0
□ first_shot_outcome = bit_array[0, :]  # all qubits for first shot
□ bitstring = bit_array.get_bitstrings()[0]  # first outcome as string

COUNTS MANIPULATION:
□ total_shots = sum(counts.values())  # sum all frequencies
□ probability_00 = counts.get('00', 0) / total_shots  # compute probability
□ sorted_outcomes = sorted(counts.items(), key=lambda x: x[1], reverse=True)
□ top_outcome, top_count = max(counts.items(), key=lambda x: x[1])
□ zero_count = counts.get('00', 0)  # safe access with default
□ filtered = {k: v for k, v in counts.items() if v > 100}  # filter by count

CONVERSION BETWEEN FORMATS:
□ int_key = int(string_key, 2)  # convert '11' to 3
□ string_key = format(int_key, f'0{num_bits}b')  # convert 3 to '11'
□ counts_from_bitstrings = {}
□ for bs in bitstrings:
□     counts_from_bitstrings[bs] = counts_from_bitstrings.get(bs, 0) + 1

MULTIPLE OBSERVABLES (ESTIMATOR):
□ observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX')]
□ job = estimator.run([(qc, observables)])
□ evs = result[0].data.evs  # array: [⟨ZZ⟩, ⟨XX⟩]
□ stds = result[0].data.stds  # array: [σ_ZZ, σ_XX]
□ for i, (obs, ev, std) in enumerate(zip(observables, evs, stds)):
□     print(f"Observable {i}: {ev} ± {std}")

ERROR HANDLING:
□ try:
□     result = job.result()
□ except Exception as e:
□     print(f"Job failed: {e}")
□ if job.status() == JobStatus.ERROR:
□     error_msg = job.error_message()
□ if not job.done():
□     print("Job still running...")
□ assert job.in_final_state(), "Job not completed"

RESULT VALIDATION:
□ assert len(result) > 0, "No results returned"
□ assert hasattr(result[0].data, 'meas'), "Missing 'meas' register"
□ counts = result[0].data.meas.get_counts()
□ assert sum(counts.values()) == shots, "Shot count mismatch"
□ assert len(bitstrings) == shots, "Bitstring count mismatch"
□ assert all(len(bs) == num_bits for bs in bitstrings), "Bitstring length mismatch"

ADVANCED ACCESS PATTERNS:
□ # Dynamic register access
□ for reg_name in dir(result[0].data):
□     if not reg_name.startswith('_'):
□         bit_array = getattr(result[0].data, reg_name)
□ # Extract specific bits
□ first_two_bits = [bs[:2] for bs in bitstrings]
□ # Marginal counts (project onto subset of qubits)
□ marginal = {}
□ for outcome, count in counts.items():
□     key = outcome[:2]  # first two bits
□     marginal[key] = marginal.get(key, 0) + count

COMPARISON AND ANALYSIS:
□ # Compare two results
□ counts1 = result[0].data.meas.get_counts()
□ counts2 = result[1].data.meas.get_counts()
□ difference = {k: counts1.get(k, 0) - counts2.get(k, 0) for k in counts1}
□ # Statistical analysis
□ from scipy.stats import chisquare
□ observed = list(counts.values())
□ expected = [shots / len(counts)] * len(counts)
□ chi2, p_value = chisquare(observed, expected)

ITERATING RESULTS:
□ # By index
□ for i in range(len(result)):
□     counts = result[i].data.meas.get_counts()
□ # By enumeration
□ for idx, pub_result in enumerate(result):
□     ev = pub_result.data.evs if hasattr(pub_result.data, 'evs') else None
□ # Collect all outcomes
□ all_outcomes = []
□ for pub in result:
□     all_outcomes.extend(pub.data.meas.get_bitstrings())
```

### ⚠️ Exam Trap Checklist
```
RESULT CHAIN TRAPS:
□ TRAP: Missing [0] index in result chain
  → result.data.meas is WRONG (PrimitiveResult not indexed)
  → Use: result[0].data.meas (must index into PubResult)
□ TRAP: Missing .data in chain
  → result[0].meas.get_counts() is WRONG (PubResult has no meas)
  → Use: result[0].data.meas.get_counts() (data is required!)
□ TRAP: Missing .meas (or register name) in chain
  → result[0].data.get_counts() is WRONG (DataBin has no get_counts())
  → Use: result[0].data.meas.get_counts() (register name required!)
□ TRAP: Missing .get_ prefix
  → result[0].data.meas.counts() is WRONG (no such method)
  → Use: result[0].data.meas.get_counts() (get_ prefix required!)
□ TRAP: Using wrong register name
  → Assuming 'meas' when register is named 'c' or 'output'
  → Check: qc.cregs[0].name to get actual name
□ TRAP: Calling get_counts on DataBin instead of BitArray
  → result[0].data.get_counts() doesn't exist
  → Must go through register: result[0].data.meas.get_counts()

PROPERTY VS METHOD TRAPS:
□ TRAP: Using singular evs/stds
  → result[0].data.ev is WRONG (no such attribute)
  → Use: result[0].data.evs (plural with 's'!)
□ TRAP: Calling evs/stds as methods
  → result[0].data.evs() is WRONG (properties, not methods!)
  → Use: result[0].data.evs (no parentheses!)
□ TRAP: Using .get_evs() or .get_stds()
  → No such methods exist
  → Direct property access: result[0].data.evs
□ TRAP: Confusing when to use parentheses
  → get_counts() = method (needs ())
  → evs = property (no ())
  → Rule: "get_" prefix = method, otherwise property

PUB FORMAT TRAPS:
□ TRAP: Missing trailing comma in single-circuit PUB
  → [(circuit)] is WRONG (list with circuit object, not tuple)
  → Use: [(circuit,)] (list with tuple - comma makes tuple!)
□ TRAP: Using list instead of tuple for PUB
  → [[circuit, params]] is WRONG
  → Use: [(circuit, params)] (tuple inside list)
□ TRAP: Forgetting outer list
  → (circuit,) alone is WRONG
  → Use: [(circuit,)] (tuple must be in list)
□ TRAP: Wrong PUB element order
  → Sampler: (params, circuit, shots) is WRONG
  → Correct: (circuit, params, shots) - "CPS" order

OBSERVABLE TRAPS:
□ TRAP: Using string for Estimator observable
  → estimator.run([(qc, 'ZZ')]) is WRONG
  → Use: estimator.run([(qc, SparsePauliOp('ZZ'))])
□ TRAP: Missing observable in Estimator PUB
  → [(qc,)] is Sampler format, missing observable for Estimator
  → Use: [(qc, obs)] for Estimator
□ TRAP: Adding observable to Sampler PUB
  → [(qc, obs)] is WRONG for Sampler (no observable needed)
  → Use: [(qc,)] for Sampler

JOB STATUS TRAPS:
□ TRAP: Comparing JobStatus with string
  → if job.status() == "DONE" is WRONG
  → Use: if job.status() == JobStatus.DONE (enum comparison!)
□ TRAP: Using lowercase status
  → JobStatus.done is WRONG (wrong case)
  → Use: JobStatus.DONE (uppercase!)
□ TRAP: Confusing done() method with DONE status
  → job.done() returns True for ERROR and CANCELLED too!
  → Check specific: job.status() == JobStatus.DONE
□ TRAP: Not handling ERROR status
  → Assuming done() means success
  → Check: if job.status() == JobStatus.ERROR before result()
□ TRAP: Calling result() on cancelled job
  → Raises exception if job was cancelled
  → Check status first: if job.status() == JobStatus.DONE

COUNTS VS BITSTRINGS TRAPS:
□ TRAP: Confusing get_counts() keys (strings) vs get_int_counts() keys (ints)
  → get_counts() returns {'00': 512}, get_int_counts() returns {0: 512}
  → Cannot mix: counts['00'] ✓, counts[0] ✗
□ TRAP: Forgetting that get_bitstrings() length equals shots
  → len(get_bitstrings()) == shots (one entry per shot)
  → len(get_counts()) == number of unique outcomes (typically much less)
□ TRAP: Expecting get_bitstrings() to return set or dict
  → Returns list: ['00', '11', '00', ...] (order preserved, duplicates included)
□ TRAP: Assuming counts preserve order
  → Dict doesn't guarantee order (though Python 3.7+ preserves insertion)
  → Sort if order matters: sorted(counts.items())
□ TRAP: Accessing non-existent key in counts
  → counts['00'] raises KeyError if '00' never occurred
  → Use: counts.get('00', 0) for safe access with default

TYPE AND CONVERSION TRAPS:
□ TRAP: Treating bitstrings as integers
  → '00' is string, not int
  → Convert: int('00', 2) = 0
□ TRAP: Wrong binary conversion direction
  → int('10', 2) = 2 (interprets as MSB)
  → For LSB ordering, reverse first: int('10'[::-1], 2) = 1
□ TRAP: Not padding when converting int to bitstring
  → bin(3) = '0b11', need '011' for 3 qubits
  → Use: format(3, '03b') or f'{3:03b}'
□ TRAP: Expecting evs to be scalar when it's array
  → result[0].data.evs is numpy array, even for single observable
  → Extract: ev = result[0].data.evs[0]
□ TRAP: Trying to modify immutable results
  → Result objects are read-only
  → Create new dict: modified = dict(counts); modified['00'] += 1

INDEXING TRAPS:
□ TRAP: Using negative indices expecting Python list behavior
  → result[-1] may not work as expected (not standard list)
  → Use: result[len(result)-1] or iterate forward
□ TRAP: Assuming result[0] always exists
  → Empty results possible (though rare)
  → Check: if len(result) > 0 before accessing
□ TRAP: Out-of-bounds PUB index
  → result[3] when only 3 PUBs (indices 0,1,2)
  → Check: i < len(result)
□ TRAP: Using wrong index for multi-observable results
  → result[i].data.evs[j] where i=PUB index, j=observable index
  → Don't confuse the two indices!

METADATA TRAPS:
□ TRAP: Assuming all metadata fields always present
  → Some fields are backend-specific or optional
  → Use: metadata.get('field', default) for safe access
□ TRAP: Confusing requested shots with actual shots
  → Request 1024, but metadata['shots'] might differ slightly
  → Use metadata['shots'] for actual count
□ TRAP: Treating metadata as regular dict
  → Some implementations use custom objects
  → Use .get() method or hasattr() for safety

MULTIPLE PUB TRAPS:
□ TRAP: Assuming all PUBs have same structure
  → Different circuits can have different register names
  → Check each: result[i].data.<register_name>
□ TRAP: Using same index for circuit and result
  → If you ran [(qc1,), (qc2,), (qc3,)], result[0] is qc1
  → But if parameter sweep, indexing differs
□ TRAP: Forgetting to iterate when multiple PUBs
  → result[0] only gives first result
  → Use: for pub in result to process all

V1 VS V2 CONFUSION TRAPS:
□ TRAP: Using V1 result access patterns
  → result.get_counts() is V1, doesn't work in V2
  → V2: result[0].data.meas.get_counts()
□ TRAP: Using get_memory() (V1 method)
  → V2 uses get_bitstrings() instead
□ TRAP: Expecting Result object instead of PrimitiveResult
  → V1 returned Result, V2 returns PrimitiveResult (different structure)
□ TRAP: Mixing V1 and V2 code examples
  → Documentation may show both; ensure using V2 patterns

ESTIMATOR-SPECIFIC TRAPS:
□ TRAP: Trying to get counts from Estimator result
  → Estimator has no counts, only evs and stds
  → Use Sampler if you need counts
□ TRAP: Expecting measurements in Estimator circuits
  → Estimator circuits must NOT have measurements
  → Will error if measurements present
□ TRAP: Accessing wrong result attributes
  → result[0].data.meas doesn't exist for Estimator
  → Use: result[0].data.evs and result[0].data.stds

SAMPLER-SPECIFIC TRAPS:
□ TRAP: Trying to get expectation values from Sampler
  → Sampler has no evs, only counts/bitstrings
  → Use Estimator if you need expectation values
□ TRAP: Forgetting measurements in Sampler circuits
  → Sampler requires measurements
  → Will error if no measurements

ADVANCED TRAPS:
□ TRAP: Assuming job.result() is cached
  → Each call may re-fetch from server
  → Store: result = job.result(), then reuse
□ TRAP: Not handling job timeout
  → job.wait_for_final_state() can hang indefinitely
  → Use: job.wait_for_final_state(timeout=300)
□ TRAP: Comparing float expectation values with ==
  → Floating point precision issues
  → Use: np.isclose(ev1, ev2) or abs(ev1 - ev2) < 1e-6
□ TRAP: Forgetting shots are statistical samples
  → Results vary between runs (not deterministic on hardware)
  → Compare distributions, not exact counts
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 7 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🔗 "RIDMG" - Result Index Data Meas Get - MOST CRITICAL        │
│    result[0].data.meas.get_counts()                             │
│    → R = result (PrimitiveResult)                               │
│    → I = [0] Index (into PubResult)                             │
│    → D = .data (DataBin)                                        │
│    → M = .meas (register name/BitArray)                         │
│    → G = .get_counts() (method)                                 │
│    💡 "Really Important Data Means Getting counts"              │
│    💡 Each step REQUIRED - skip any = AttributeError            │
│                                                                  │
│ 📊 "EVS = Expectation ValueS (plural)" - PROPERTY!             │
│    result[0].data.evs (property, no parentheses!)               │
│    → Always plural: evs and stds                                │
│    → Never: ev or std (don't exist!)                            │
│    💡 "Every Value Stays plural" (evs)                          │
│    💡 "Standard Deviations Stay plural" (stds)                  │
│                                                                  │
│ 📦 "CPS" - Circuit, Params, Shots - SAMPLER PUB                │
│    Sampler PUB format: (circuit, params, shots)                 │
│    → All after circuit are optional                             │
│    → Order matters: Circuit first, Params second, Shots third   │
│    💡 "Car Picks Speed" (circuit picks parameters and shots)    │
│                                                                  │
│ 🎯 "COPP" - Circuit, Observable, Params, Precision - ESTIMATOR │
│    Estimator PUB format: (circuit, observable, params, prec)    │
│    → Observable required, others optional                       │
│    → Order matters: Cannot swap positions!                      │
│    💡 "Cops Observe People Precisely"                           │
│                                                                  │
│ 📈 "IQVRCDE" - Job Status Flow                                 │
│    I = INITIALIZING → Q = QUEUED → V = VALIDATING →            │
│    R = RUNNING → (C = CANCELLED or D = DONE or E = ERROR)      │
│    💡 "I Queue Very Real Challenges Daily, Expert!"             │
│    💡 Last three (C/D/E) are terminal states                    │
│                                                                  │
│ 🎯 "Trailing comma makes Tuple" - CRITICAL!                    │
│    (circuit,) is tuple, (circuit) is just parentheses           │
│    → [(circuit,)] for PUB format                                │
│    → Python syntax: comma required for single-element tuple     │
│    💡 "No comma = no tuple = error"                             │
│    💡 Test: type((x,)) = tuple, type((x)) = type of x           │
│                                                                  │
│ 🔤 "Methods Get, Properties Are" - PARENTHESES RULE            │
│    get_counts() = method (with parentheses)                     │
│    evs = property (without parentheses)                         │
│    → Never call evs() or stds() - they're not methods!          │
│    💡 "get_" prefix = method (needs ())                         │
│    💡 No "get_" = property (no ())                              │
│                                                                  │
│ 📏 "Bitstrings = Shots, Counts = Unique"                       │
│    len(get_bitstrings()) = total shots                          │
│    len(get_counts()) = unique outcomes                          │
│    → Bitstrings list is longer (one entry per shot)             │
│    💡 "Bitstrings count all, Counts count unique"               │
│    💡 1024 shots, 2 unique → len(bitstrings)=1024, len(counts)=2│
│                                                                  │
│ 🔢 "String Keys, Int Keys" - get_counts vs get_int_counts      │
│    get_counts() → {'00': 512, '11': 512} (string keys)          │
│    get_int_counts() → {0: 512, 3: 512} (integer keys)           │
│    💡 "Default is String, Int needs explicit method"            │
│    💡 '00' string ≠ 0 integer (different dict keys!)            │
│                                                                  │
│ 🎭 "Enum Not String" - JobStatus Comparison                    │
│    job.status() == JobStatus.DONE ✓                             │
│    job.status() == "DONE" ✗                                     │
│    → Must use enum, not string                                  │
│    💡 "JobStatus is enum class, not string constant"            │
│                                                                  │
│ 📍 "Index Then Data" - Two-Step Access                         │
│    result → result[0] → result[0].data                          │
│    → Cannot skip [0]: result.data doesn't exist                 │
│    💡 "Index into PubResults before accessing data"             │
│    💡 "result[i]" where i = PUB number (0-based)                │
│                                                                  │
│ 🎪 "Register Name Varies" - Don't Assume "meas"                │
│    result[0].data.meas ← default name                           │
│    result[0].data.c ← if register named 'c'                     │
│    result[0].data.output ← if register named 'output'           │
│    💡 Check: qc.cregs[0].name to get actual name                │
│                                                                  │
│ 🔄 "Three-Level Hierarchy" - Result Structure                  │
│    Level 1: PrimitiveResult (from job.result())                 │
│    Level 2: PubResult (result[i] for i-th PUB)                  │
│    Level 3: DataBin (result[i].data)                            │
│    💡 "Primitive → Pub → Data" (PPD)                            │
│    💡 Each level must be traversed explicitly                   │
│                                                                  │
│ 🎲 "Sampler Counts, Estimator Expects" - Output Types          │
│    Sampler → counts/bitstrings (discrete)                       │
│    Estimator → expectation values (continuous)                  │
│    💡 "Sampler Samples, Estimator Estimates"                    │
│    💡 Different data attributes: meas vs evs/stds               │
│                                                                  │
│ 🔑 "done() Means Terminal, Not Success" - Status Check         │
│    job.done() returns True for DONE, ERROR, CANCELLED           │
│    → Doesn't mean success, just "finished"                      │
│    💡 "done() = terminal state, not necessarily DONE status"    │
│    💡 Check: job.status() == JobStatus.DONE for success         │
│                                                                  │
│ 🧮 "Sum Counts = Shots" - Validation Check                     │
│    sum(counts.values()) should equal total shots                │
│    → Sanity check for data integrity                            │
│    💡 "All shots accounted for in counts"                       │
│                                                                  │
│ 📐 "BitArray is 2D" - Shape Understanding                       │
│    BitArray.shape = (num_shots, num_bits)                       │
│    → First dimension: shots, Second dimension: qubits           │
│    💡 "Array of shots, each shot has bits"                      │
│                                                                  │
│ 🔍 "Metadata Has Actual Shots" - True Count                    │
│    result[0].metadata['shots'] = actual shots executed          │
│    → May differ slightly from requested                         │
│    💡 "Metadata tells truth about execution"                    │
│                                                                  │
│ 🎯 "V2 Has Three Levels, V1 Had One" - Version Difference      │
│    V2: result[0].data.meas.get_counts() (three levels)          │
│    V1: result.get_counts() (direct access)                      │
│    💡 "V2 more structured, V1 simpler but deprecated"           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║         SECTION 7: RESULTS - ONE-PAGE SUMMARY                         ║
║                      (10% of Exam - ~6-7 Questions)                    ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 RESULT HIERARCHY (95% of questions!) - MEMORIZE THIS!             ║
║  ├─ Three-Level Structure:                                             ║
║  │   ├─ Level 1: PrimitiveResult (job.result())                       ║
║  │   │   └─ Container for all PUB results                             ║
║  │   ├─ Level 2: PubResult (result[0], result[1], ...)                ║
║  │   │   └─ Individual result for each PUB (circuit execution)        ║
║  │   └─ Level 3: DataBin (result[0].data)                             ║
║  │       ├─ Sampler: BitArrays by register name (.meas, .c, etc.)     ║
║  │       └─ Estimator: Properties .evs and .stds                      ║
║  ├─ Access Pattern: result[index].data.attribute                      ║
║  │   └─ MUST traverse all levels - cannot skip any                    ║
║  └─ Key: Each level has specific methods/attributes                   ║
║                                                                        ║
║  📊 SAMPLER RESULTS (Discrete Outcomes)                                ║
║  ├─ Full extraction chain:                                             ║
║  │   └─ counts = result[0].data.meas.get_counts()                     ║
║  │       ├─ result = PrimitiveResult object                           ║
║  │       ├─ [0] = index into first PubResult                          ║
║  │       ├─ .data = DataBin container                                 ║
║  │       ├─ .meas = BitArray for 'meas' register                      ║
║  │       └─ .get_counts() = method returning dict                     ║
║  ├─ Three extraction methods:                                          ║
║  │   ├─ get_counts() → {'00': 512, '11': 512} (string keys)           ║
║  │   │   └─ Returns: dict mapping bitstrings to frequencies           ║
║  │   ├─ get_bitstrings() → ['00', '11', '00', ...] (list)             ║
║  │   │   └─ Returns: list of all outcomes, length = shots             ║
║  │   └─ get_int_counts() → {0: 512, 3: 512} (integer keys)            ║
║  │       └─ Returns: dict with binary-to-int converted keys           ║
║  ├─ Length relationships (CRITICAL!):                                  ║
║  │   ├─ len(get_bitstrings()) = total shots (e.g., 1024)              ║
║  │   ├─ len(get_counts()) = unique outcomes (e.g., 2)                 ║
║  │   └─ sum(counts.values()) = total shots (validation check)         ║
║  └─ Register name variations:                                          ║
║      ├─ Default: result[0].data.meas (measure_all() creates 'meas')   ║
║      ├─ Custom: result[0].data.output (if register named 'output')    ║
║      └─ Check: qc.cregs[0].name to get actual register name           ║
║                                                                        ║
║  🎯 ESTIMATOR RESULTS (Continuous Expectation Values)                  ║
║  ├─ Access pattern (PROPERTIES, not methods!):                         ║
║  │   ├─ expectation = result[0].data.evs  (NO parentheses!)           ║
║  │   ├─ std_dev = result[0].data.stds     (NO parentheses!)           ║
║  │   └─ Both are numpy arrays, even for single observable             ║
║  ├─ Extract single values:                                             ║
║  │   ├─ ev_value = result[0].data.evs[0]   # first expectation        ║
║  │   └─ std_value = result[0].data.stds[0] # first std dev            ║
║  ├─ Multiple observables:                                              ║
║  │   ├─ evs = result[0].data.evs  # array: [⟨O₁⟩, ⟨O₂⟩, ⟨O₃⟩]         ║
║  │   └─ stds = result[0].data.stds  # array: [σ₁, σ₂, σ₃]             ║
║  └─ CRITICAL: Always plural (evs, stds), never singular (ev, std)     ║
║                                                                        ║
║  📦 PUB FORMATS (Primitive Unified Bloc)                               ║
║  ├─ Sampler PUB: (circuit, parameters, shots)                         ║
║  │   ├─ Mnemonic: "CPS" - Circuit, Params, Shots                      ║
║  │   ├─ Basic:        [(circuit,)]              # trailing comma!     ║
║  │   ├─ With params:  [(circuit, [0.5, 1.2])]  # parameter values    ║
║  │   ├─ With shots:   [(circuit, None, 2048)]  # None placeholder    ║
║  │   └─ Full:         [(circuit, [0.5], 2048)] # all specified       ║
║  ├─ Estimator PUB: (circuit, observable, parameters, precision)       ║
║  │   ├─ Mnemonic: "COPP" - Circuit, Observable, Params, Precision    ║
║  │   ├─ Basic:        [(circuit, obs)]                                ║
║  │   ├─ With params:  [(circuit, obs, [0.5, 1.2])]                   ║
║  │   ├─ With precision: [(circuit, obs, None, 0.01)]                  ║
║  │   └─ Full:         [(circuit, obs, [0.5], 0.01)]                  ║
║  └─ CRITICAL: Tuple inside list - comma required for single element   ║
║      └─ [(circuit,)] NOT [(circuit)] - comma makes it tuple!          ║
║                                                                        ║
║  🔄 MULTIPLE CIRCUITS/PUBS                                             ║
║  ├─ Indexing pattern:                                                  ║
║  │   ├─ result[0] → first PUB/circuit                                 ║
║  │   ├─ result[1] → second PUB/circuit                                ║
║  │   └─ result[i] → i-th PUB/circuit (0-based)                        ║
║  ├─ Iteration patterns:                                                ║
║  │   ├─ for i in range(len(result)):                                  ║
║  │   │       counts = result[i].data.meas.get_counts()                ║
║  │   ├─ for pub_result in result:                                     ║
║  │   │       counts = pub_result.data.meas.get_counts()               ║
║  │   └─ all_counts = [r.data.meas.get_counts() for r in result]       ║
║  └─ Number of results: len(result) = number of PUBs submitted         ║
║                                                                        ║
║  📈 JOB STATUS MANAGEMENT                                              ║
║  ├─ Status checking:                                                   ║
║  │   ├─ status = job.status()  # returns JobStatus enum               ║
║  │   ├─ is_done = job.done()   # returns boolean (True when terminal) ║
║  │   └─ job.wait_for_final_state()  # blocking wait                   ║
║  ├─ Status lifecycle (in order):                                       ║
║  │   ├─ INITIALIZING → Job object created                             ║
║  │   ├─ QUEUED → Waiting for resources                                ║
║  │   ├─ VALIDATING → Backend checking circuit                         ║
║  │   ├─ RUNNING → Actively executing                                  ║
║  │   └─ Terminal states (one of):                                     ║
║  │       ├─ DONE → Success, results available                         ║
║  │       ├─ ERROR → Failed, check error_message()                     ║
║  │       └─ CANCELLED → User/system cancelled                         ║
║  ├─ Comparison pattern:                                                ║
║  │   ├─ if job.status() == JobStatus.DONE:  # use enum!               ║
║  │   ├─ NOT: if job.status() == "DONE"  # wrong! (string)             ║
║  │   └─ Import: from qiskit.providers import JobStatus                ║
║  └─ CRITICAL: done() returns True for ERROR and CANCELLED too!        ║
║      └─ Check specific status for success: status() == JobStatus.DONE ║
║                                                                        ║
║  🔢 DATA TYPE CONVERSIONS                                              ║
║  ├─ String to integer:                                                 ║
║  │   ├─ int('00', 2) = 0  # binary string to int                      ║
║  │   └─ int('11', 2) = 3  # interprets as binary                      ║
║  ├─ Integer to string:                                                 ║
║  │   ├─ format(0, '02b') = '00'  # with padding                       ║
║  │   ├─ f'{3:02b}' = '11'  # f-string format                          ║
║  │   └─ bin(3) = '0b11'  # without padding (avoid for Qiskit)         ║
║  ├─ Bitstring ordering (LSB):                                          ║
║  │   ├─ '01' means q[0]=1, q[1]=0 (rightmost = qubit 0)               ║
║  │   └─ For standard binary: may need to reverse string               ║
║  └─ Array extraction:                                                  ║
║      ├─ evs is array: extract with evs[0], evs[1], etc.               ║
║      └─ counts is dict: extract with counts['00'], counts.get('11', 0)║
║                                                                        ║
║  🔍 METADATA ACCESS                                                    ║
║  ├─ Access pattern:                                                    ║
║  │   └─ metadata = result[0].metadata  # dict-like object             ║
║  ├─ Common fields:                                                     ║
║  │   ├─ metadata['shots'] → actual shots executed                     ║
║  │   ├─ metadata.get('circuit_metadata', {}) → circuit info           ║
║  │   └─ metadata.get('execution_time') → time spent                   ║
║  └─ Safe access: use .get() method for optional fields                ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (HIGHEST PRIORITY!)                              ║
║  ╔════════════════════════════════════════════════════════════════╗  ║
║  ║ 1. ❌ Missing [0]: result.data.meas (skipping PubResult index)  ║  ║
║  ║    ✓ CORRECT: result[0].data.meas (must index first!)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 2. ❌ Missing .data: result[0].meas (skipping DataBin)          ║  ║
║  ║    ✓ CORRECT: result[0].data.meas (data is required!)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 3. ❌ Missing register: result[0].data.get_counts()             ║  ║
║  ║    ✓ CORRECT: result[0].data.meas.get_counts() (register name!)║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 4. ❌ Missing .get_: result[0].data.meas.counts()               ║  ║
║  ║    ✓ CORRECT: result[0].data.meas.get_counts() (get_ prefix!)  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 5. ❌ Singular: result[0].data.ev (no such attribute!)          ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (always plural with s!)       ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 6. ❌ Calling property as method: result[0].data.evs()          ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (NO parentheses - property!)  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 7. ❌ Missing comma: [(circuit)] - not a tuple!                 ║  ║
║  ║    ✓ CORRECT: [(circuit,)] - comma makes single-element tuple  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 8. ❌ String observable: estimator.run([(qc, 'ZZ')])            ║  ║
║  ║    ✓ CORRECT: estimator.run([(qc, SparsePauliOp('ZZ'))])       ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 9. ❌ String comparison: job.status() == "DONE"                 ║  ║
║  ║    ✓ CORRECT: job.status() == JobStatus.DONE (use enum!)       ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 10. ❌ Confusing lengths: len(get_bitstrings()) = unique        ║  ║
║  ║     ✓ CORRECT: len(get_bitstrings()) = shots (total count)     ║  ║
║  ║     ✓ CORRECT: len(get_counts()) = unique outcomes             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 11. ❌ String vs int keys: counts[0] when using get_counts()   ║  ║
║  ║     ✓ get_counts() uses strings: counts['00']                  ║  ║
║  ║     ✓ get_int_counts() uses ints: int_counts[0]                ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 12. ❌ Assuming register always 'meas' (may be 'c', 'output')  ║  ║
║  ║     ✓ CHECK: qc.cregs[0].name or use actual name from circuit  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 13. ❌ Treating evs as scalar: ev = result[0].data.evs          ║  ║
║  ║     ✓ evs is array: ev = result[0].data.evs[0] (index!)        ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 14. ❌ Assuming done() means success (also True for ERROR!)     ║  ║
║  ║     ✓ Check explicit: job.status() == JobStatus.DONE           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 15. ❌ Using V1 patterns: result.get_counts() (deprecated)      ║  ║
║  ║     ✓ V2 requires: result[0].data.meas.get_counts()            ║  ║
║  ╚════════════════════════════════════════════════════════════════╝  ║
║                                                                        ║
║  💡 MEMORY AIDS (CRITICAL!)                                            ║
║  ├─ "RIDMG" - Result Index Data Meas Get (chain for Sampler)          ║
║  ├─ "EVS = Expectation ValueS" (plural, property)                     ║
║  ├─ "CPS" - Circuit Params Shots (Sampler PUB)                        ║
║  ├─ "COPP" - Circuit Observable Params Precision (Estimator PUB)      ║
║  ├─ "Methods Get, Properties Are" (get_counts() vs evs)               ║
║  ├─ "Bitstrings = Shots, Counts = Unique" (length relationship)       ║
║  ├─ "Trailing comma makes Tuple" ((circuit,) not (circuit))           ║
║  └─ "Enum Not String" (JobStatus.DONE not "DONE")                     ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
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
