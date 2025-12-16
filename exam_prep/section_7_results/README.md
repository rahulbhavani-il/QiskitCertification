# Section 7: Result Extraction

> **Exam Weight**: 10% (~7 Questions) | **Difficulty**: High | **Status**: MOST TESTED PATTERNS

```
┌─────────────────────────────────────────────────────────────────┐
│  CRITICAL: Result extraction patterns appear in EVERY exam!     │
│  • result[0].data.meas.get_counts() - Sampler (MEMORIZE!)      │
│  • result[0].data.evs - Estimator (MEMORIZE!)                  │
│  • Understanding nested structure is ESSENTIAL                   │
└─────────────────────────────────────────────────────────────────┘
```

## 📚 Overview

Result extraction retrieves data from primitive execution (Sampler/Estimator). This is one of the **most tested** topics on the certification exam, with 5-7 questions focusing on correct result access patterns.

**Key Concepts**:
- **Sampler Results**: Measurement counts and bitstrings
- **Estimator Results**: Expectation values and standard deviations  
- **Metadata**: Execution information and diagnostics
- **Result Structure**: Nested access patterns (result → [i] → data → meas)

---

## 🎯 Why This Section Matters

### 🧠 Conceptual Deep Dive

#### Analogy: The Survey Results
Extracting results is like analyzing survey data.
- **Raw Data**: The pile of survey forms (the `Result` object).
- **Counts**: Tallying up the answers (Sampler results).
- **Averages**: Calculating the mean opinion (Estimator results).
- **Metadata**: Checking the timestamps and location of the survey (Execution metadata).

#### The "Data" Wrapper
In Qiskit Primitives V2, results are wrapped in a `PubResult` (Primitive Unified Bloc). Think of this as a standardized envelope that holds both the answer (data) and the context (metadata).

### 1. **MOST TESTED Topic**
Result access patterns appear in **EVERY** certification exam. You MUST memorize:
- `result[0].data.meas.get_counts()` for Sampler
- `result[0].data.evs` for Estimator

### 2. **Different Primitives = Different Methods**
Sampler and Estimator have completely different result structures:
- Sampler: Returns measurement counts/bitstrings
- Estimator: Returns expectation values/standard deviations

### 3. **Post-Processing Foundation**
All data analysis starts with result extraction:
- Convert counts to probabilities
- Calculate statistics
- Analyze measurement outcomes
- Debug circuit behavior

### 4. **Debugging Tool**
Metadata reveals execution issues:
- Shot count verification
- Backend information
- Error messages
- Execution time

---

## 📖 Core Concepts

### Sampler Result Structure

```
SamplerResult (PrimitiveResult)
  └─ [0] PubResult (first circuit)
      └─ .data (DataBin)
          └─ .meas (BitArray - default classical register name)
              ├─ .get_counts() → {'00': 512, '11': 512}
              ├─ .get_bitstrings() → ['00', '11', '00', ...]
              └─ .get_int_counts() → {0: 512, 3: 512}
```

**Why nested?**
- Supports batch execution (multiple circuits)
- Each circuit has its own result
- Data contains all classical registers
- `meas` is the default register name

### Estimator Result Structure

```
EstimatorResult (PrimitiveResult)
  └─ [0] PubResult (first circuit)
      └─ .data (DataBin)
          ├─ .evs → 0.5 (expectation value - float)
          └─ .stds → 0.02 (standard deviation - float)
```

---

## 💻 Code Examples

### Example 1: Sampler Result Extraction (MOST TESTED)

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

# Create Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run with Sampler
sampler = Sampler()
job = sampler.run([qc], shots=1024)
result = job.result()

# EXAM CRITICAL: Access counts
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': 512, '11': 512}

# Alternative: Get bitstrings
bitstrings = result[0].data.meas.get_bitstrings()
print(bitstrings[:5])  # ['00', '11', '00', '11', '00']

# Convert to probabilities
total_shots = sum(counts.values())
probabilities = {k: v/total_shots for k, v in counts.items()}
print(probabilities)  # {'00': 0.5, '11': 0.5}
```

**🎯 EXAM TIP**: The pattern `result[0].data.meas.get_counts()` appears in nearly EVERY exam!

### ⚠️ RESULT ACCESS PATTERN CHEAT SHEET (MEMORIZE!)

```python
# ═══════════════════════════════════════════════════════
#  SAMPLER RESULTS
# ═══════════════════════════════════════════════════════
job = sampler.run([qc], shots=1024)
result = job.result()

# Most common (95% of exam questions):
counts = result[0].data.meas.get_counts()  # {'00': 512, '11': 512}

# Alternative methods:
bitstrings = result[0].data.meas.get_bitstrings()  # ['00', '11', ...]
bitarray = result[0].data.meas  # BitArray object

# Metadata:
shots = result[0].metadata['shots']

# ═══════════════════════════════════════════════════════
#  ESTIMATOR RESULTS  
# ═══════════════════════════════════════════════════════
job = estimator.run([(qc, obs)])
result = job.result()

# Expectation value (note: .evs is PLURAL!):
expectation = result[0].data.evs  # scalar value

# Standard deviation:
std = result[0].data.stds  # scalar value

# ═══════════════════════════════════════════════════════
#  MULTIPLE CIRCUITS
# ═══════════════════════════════════════════════════════
job = sampler.run([(qc1,), (qc2,)])
result = job.result()

counts1 = result[0].data.meas.get_counts()  # First circuit
counts2 = result[1].data.meas.get_counts()  # Second circuit

# Loop through all results:
for i, pub_result in enumerate(result):
    counts = pub_result.data.meas.get_counts()
    print(f"Circuit {i}: {counts}")
```

**Memory Aid: "Result[Index].Data.Meas.Get_counts()"**
- Think: **R**esult → **I**ndex → **D**ata → **M**eas → **G**et
- Mnemonic: "**R**eally **I**ntelligent **D**evelopers **M**emorize **G**atterns"

**Common Mistakes**:
```python
❌ result.data.meas.get_counts()     # Missing [0] index!
❌ result[0].meas.get_counts()       # Missing .data
❌ result[0].data.get_counts()       # Missing .meas
❌ result[0].data.meas.counts()      # Missing .get_
✅ result[0].data.meas.get_counts()  # CORRECT!
```

### 🎓 Exam Question Patterns - Results

**Pattern 1: "Extract measurement counts from Sampler result"**
```python
# This is THE most tested pattern!
result = job.result()
counts = result[0].data.meas.get_counts()

# Expect to see in 90% of Sampler questions!
```

**Pattern 2: "Get expectation value from Estimator result"**
```python
result = job.result()
expectation = result[0].data.evs  # Note: evs (plural!)
std_dev = result[0].data.stds     # Note: stds (plural!)
```

**Pattern 3: "Process multiple circuit results"**
```python
# Loop pattern:
for i, pub_result in enumerate(result):
    counts = pub_result.data.meas.get_counts()
    print(f"Circuit {i}: {counts}")

# Or direct indexing:
counts_0 = result[0].data.meas.get_counts()
counts_1 = result[1].data.meas.get_counts()
```

**Pattern 4: "Convert counts to probabilities"**
```python
# ALWAYS required in post-processing:
total = sum(counts.values())
probs = {bitstring: count/total for bitstring, count in counts.items()}
```

### 🔧 Troubleshooting Guide - Results

```
Error: 'PrimitiveResult' has no attribute 'get_counts'
→ Missing [0] index! Use: result[0].data.meas.get_counts()

Error: 'PubResult' has no attribute 'meas'
→ Missing .data! Use: result[0].data.meas.get_counts()

Error: 'DataBin' has no attribute 'get_counts'
→ Missing .meas! Use: result[0].data.meas.get_counts()

Error: 'BitArray' has no attribute 'counts'
→ Use .get_counts() not .counts()!

Got: result[0].data.c.get_counts() but wanted 'meas'
→ Register name changed! Check circuit: qc.measure(..., 'meas')
```

### ✅ Result Extraction Checklist

```
□ Called job.result() first?
□ Using [0] index for first circuit?
□ Added .data after index?
□ Added .meas (or correct register name)?
□ Called .get_counts() method?
□ For Estimator: Using .evs not .ev?
□ Handling multiple circuits: Loop or multiple indices?
```

### Example 2: Estimator Result Extraction

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import Estimator

# Create circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Define observable (ZZ operator)
observable = SparsePauliOp(['ZZ'])

# Run with Estimator
estimator = Estimator()
job = estimator.run([(qc, observable)])
result = job.result()

# EXAM CRITICAL: Access expectation value
expectation_value = result[0].data.evs
std_dev = result[0].data.stds

print(f"Expectation: {expectation_value}")  # ~1.0 for Bell state
print(f"Std Dev: {std_dev}")  # ~0.0
```

**🎯 EXAM TIP**: Remember `.evs` (plural) not `.ev`!

### Example 3: Multiple Circuits (Batch Processing)

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

# Create multiple circuits
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.measure_all()

qc2 = QuantumCircuit(1)
qc2.x(0)
qc2.measure_all()

# Run batch
sampler = Sampler()
job = sampler.run([qc1, qc2], shots=1000)
result = job.result()

# Access each circuit's results
for i, pub_result in enumerate(result):
    counts = pub_result.data.meas.get_counts()
    print(f"Circuit {i}: {counts}")

# Or directly:
counts1 = result[0].data.meas.get_counts()  # Circuit 1
counts2 = result[1].data.meas.get_counts()  # Circuit 2
```

### Example 4: Accessing Metadata

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = Sampler()
job = sampler.run([qc], shots=2048)
result = job.result()

# Access metadata
metadata = result[0].metadata
print(f"Shots: {metadata.get('shots', 'N/A')}")
print(f"Duration: {metadata.get('execution_time', 'N/A')}")

# Full metadata inspection
print(f"All metadata: {metadata}")
```

### Example 5: Parameterized Circuits with Results

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import Sampler
import numpy as np

# Parameterized circuit
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.ry(theta, 0)
qc.measure_all()

# Run with multiple parameter values
sampler = Sampler()
angles = [0, np.pi/4, np.pi/2, np.pi]
job = sampler.run([(qc, [angle]) for angle in angles], shots=1000)
result = job.result()

# Extract results for each parameter value
for i, angle in enumerate(angles):
    counts = result[i].data.meas.get_counts()
    print(f"θ={angle:.2f}: {counts}")
```

### Example 6: Error Handling

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = Sampler()

try:
    job = sampler.run([qc], shots=1024)
    result = job.result()
    
    # Safe result access
    if result and len(result) > 0:
        counts = result[0].data.meas.get_counts()
        print(f"Success: {counts}")
    else:
        print("No results returned")
        
except Exception as e:
    print(f"Error: {e}")
    # Check job status
    print(f"Job status: {job.status()}")
```

---

## 🎯 Exam Focus Areas

### 1. Sampler Result Access (HIGHEST PRIORITY)

**Question Pattern**: "How do you access measurement counts from Sampler results?"

**Answer**: 
```python
counts = result[0].data.meas.get_counts()
```

**Key Points**:
- ✅ `result[0]` accesses first circuit result
- ✅ `.data` contains measurement data
- ✅ `.meas` is default classical register name
- ✅ `.get_counts()` returns dictionary

### 2. Estimator Result Access (SECOND PRIORITY)

**Question Pattern**: "How do you get expectation values from Estimator?"

**Answer**:
```python
expectation = result[0].data.evs
std_deviation = result[0].data.stds
```

**Key Points**:
- ✅ `.evs` returns expectation value (float)
- ✅ `.stds` returns standard deviation (float)
- ✅ Remember plural forms: `evs` and `stds`

### 3. Multiple Circuits

**Question Pattern**: "How do you process results from multiple circuits?"

**Answer**:
```python
for i, pub_result in enumerate(result):
    counts = pub_result.data.meas.get_counts()
```

### 4. Common Mistakes (EXAM TRAPS!)

❌ **WRONG**: `result.data.meas.get_counts()` - Missing index  
✅ **CORRECT**: `result[0].data.meas.get_counts()`

❌ **WRONG**: `result[0].get_counts()` - Missing .data.meas  
✅ **CORRECT**: `result[0].data.meas.get_counts()`

❌ **WRONG**: `result[0].data.evs()` - evs is property, not method  
✅ **CORRECT**: `result[0].data.evs`

❌ **WRONG**: `result[0].data.ev` - It's plural (evs)  
✅ **CORRECT**: `result[0].data.evs`

---

## 📊 Quick Reference Table

| Operation | Sampler | Estimator |
|-----------|---------|-----------|
| Get main result | `result[0].data.meas.get_counts()` | `result[0].data.evs` |
| Get alternative | `result[0].data.meas.get_bitstrings()` | `result[0].data.stds` |
| Return type | `dict[str, int]` | `float` |
| Multiple circuits | `result[i].data.meas.get_counts()` | `result[i].data.evs` |
| Metadata | `result[i].metadata` | `result[i].metadata` |

---

## 🧪 Practice Problems

### Problem 1: Basic Sampler Result

**Question**: Extract counts from a Bell state measurement.

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = Sampler()
job = sampler.run([qc], shots=1024)
result = job.result()

# TODO: Extract and print counts
```

<details>
<summary>Solution</summary>

```python
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': ~512, '11': ~512}
```
</details>

### Problem 2: Convert Counts to Probabilities

**Question**: Calculate probabilities from Sampler counts.

```python
# Given:
counts = {'00': 512, '01': 256, '10': 128, '11': 128}

# TODO: Convert to probabilities
```

<details>
<summary>Solution</summary>

```python
total_shots = sum(counts.values())
probabilities = {state: count/total_shots for state, count in counts.items()}
print(probabilities)
# {'00': 0.5, '01': 0.25, '10': 0.125, '11': 0.125}
```
</details>

### Problem 3: Multiple Circuit Results

**Question**: Run 3 different circuits and extract all counts.

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

qc1 = QuantumCircuit(1); qc1.h(0); qc1.measure_all()
qc2 = QuantumCircuit(1); qc2.x(0); qc2.measure_all()
qc3 = QuantumCircuit(1); qc3.measure_all()

sampler = Sampler()
job = sampler.run([qc1, qc2, qc3], shots=1000)
result = job.result()

# TODO: Extract counts for all three circuits
```

<details>
<summary>Solution</summary>

```python
all_counts = []
for i in range(3):
    counts = result[i].data.meas.get_counts()
    all_counts.append(counts)
    print(f"Circuit {i}: {counts}")

# Or:
counts1 = result[0].data.meas.get_counts()
counts2 = result[1].data.meas.get_counts()
counts3 = result[2].data.meas.get_counts()
```
</details>

---

## 💡 Key Takeaways

1. **MEMORIZE**: `result[0].data.meas.get_counts()` for Sampler
2. **MEMORIZE**: `result[0].data.evs` for Estimator
3. **Understand nesting**: result → [index] → data → meas/evs
4. **Different primitives**: Sampler returns counts, Estimator returns floats
5. **Index matters**: `result[0]` for first circuit, `result[1]` for second, etc.
6. **Plural forms**: `.evs` and `.stds` (not `.ev` or `.std`)
7. **Metadata available**: `result[i].metadata` for execution details

---

## 🔗 Related Sections

- **Section 5**: Sampler primitive usage
- **Section 6**: Estimator primitive usage
- **Section 3**: Circuit creation for measurement
- **Section 4**: Transpilation before execution

---

## 📚 Additional Resources

- IBM Quantum Documentation: [Primitives Results](https://docs.quantum.ibm.com/)
- Qiskit API: `PrimitiveResult`, `DataBin`, `BitArray`
- Practice: Run `result_extraction.py` examples

---

**Remember**: Result extraction patterns appear in **EVERY** exam. Master these two lines:
- `result[0].data.meas.get_counts()` (Sampler)
- `result[0].data.evs` (Estimator)

🎯 **Exam Success Tip**: Write these patterns 10 times before the exam!
