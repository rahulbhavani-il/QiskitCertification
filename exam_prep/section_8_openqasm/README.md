# Section 8: OpenQASM Operations

> **Exam Weight**: 6% (~4 Questions) | **Difficulty**: Medium | **Must Master**: Static Methods, QASM 2 vs 3

```
┌─────────────────────────────────────────────────────────────────┐
│  🎯 EXAM TRAP #1: from_qasm_str() is a STATIC method!          │
│  ✅ QuantumCircuit.from_qasm_str(string)  → Call on CLASS      │
│  ❌ qc.from_qasm_str(string)              → NOT on instance!   │
│                                                                 │
│  📌 Mnemonic: "FROM needs NO OBJECT"                           │
│     Import = Class method (no circuit exists yet!)             │
│     Export = Instance method (need circuit to export)          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Overview

OpenQASM (Open Quantum Assembly Language) is the standard text format for quantum circuits, enabling interoperability between quantum frameworks.

### What You'll Learn

| Sub-Topic | Key Concept | Exam Trap |
|-----------|-------------|-----------|
| 8.1 QASM Export | `qc.qasm()` | Instance method (needs circuit) |
| 8.2 QASM Import | `QuantumCircuit.from_qasm_str()` | **STATIC** (call on class!) |
| 8.3 File I/O | `from_qasm_file()` | Also **STATIC** |
| 8.4 QASM 2 vs 3 | `qasm2` vs `qasm3` modules | Different syntax & features |
| 8.5 QASM 3 Types | `bit`, `int`, `float`, `angle` | Type declarations |

---

## 🧠 Conceptual Deep Dive

### The Blueprint Analogy

```
┌──────────────────────────────────────────────────────────────────┐
│                    THE BLUEPRINT ANALOGY                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Python Circuit Object ──► OpenQASM Text ──► Hardware/Simulator │
│         (3D Model)           (Blueprint)        (Building)       │
│                                                                  │
│  Think of OpenQASM as a blueprint:                              │
│  • Architect's Software = Qiskit (Python objects)               │
│  • Printed Blueprint = OpenQASM (text format)                   │
│  • Construction Site = Quantum Hardware                          │
│                                                                  │
│  Any contractor can build from the blueprint!                   │
│  (Qiskit, Cirq, Q#, PyQuil all read QASM)                      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Why QASM Matters

1. **Interoperability** - Share circuits between Qiskit ↔ Cirq ↔ Q# ↔ PyQuil
2. **Storage** - Human-readable text files, Git-friendly
3. **Debugging** - Inspect circuit structure directly
4. **Portability** - Run on any QASM-compatible hardware

---

## 🗺️ Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                   OPENQASM OPERATIONS MAP                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────┐         ┌──────────────────┐                │
│   │ Python Code  │ ═══════►│   QASM String    │                │
│   │    (qc)      │ qc.qasm()│   (text)        │                │
│   └──────────────┘         └──────────────────┘                │
│          ▲                          │                          │
│          │                          │                          │
│          │ QuantumCircuit           │ write()                  │
│          │ .from_qasm_str()         ▼                          │
│          │    (STATIC!)      ┌──────────────────┐              │
│          └───────────────────│  .qasm file      │              │
│                              │  (on disk)       │              │
│          ▲                   └──────────────────┘              │
│          │                          │                          │
│          │ QuantumCircuit           │                          │
│          │ .from_qasm_file()        │                          │
│          │    (STATIC!)             ▼                          │
│          └──────────────────────────┘                          │
│                                                                 │
│  ⚠️ IMPORT = STATIC (Class method)                             │
│  ✅ EXPORT = INSTANCE (Object method)                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Quick Reference

| Method | Type | Signature | Returns |
|--------|------|-----------|---------|
| `qasm()` | Instance | `qc.qasm()` | `str` (QASM 2.0) |
| `from_qasm_str()` | **STATIC** | `QuantumCircuit.from_qasm_str(s)` | `QuantumCircuit` |
| `from_qasm_file()` | **STATIC** | `QuantumCircuit.from_qasm_file(f)` | `QuantumCircuit` |
| `qasm2.dumps()` | Function | `qasm2.dumps(qc)` | `str` (QASM 2.0) |
| `qasm2.loads()` | Function | `qasm2.loads(s)` | `QuantumCircuit` |
| `qasm3.dumps()` | Function | `qasm3.dumps(qc)` | `str` (QASM 3.0) |
| `qasm3.loads()` | Function | `qasm3.loads(s)` | `QuantumCircuit` |

---

## 🛤️ Learning Path

```
START
  │
  ▼
┌─────────────────────────────────┐
│ 8.1 QASM Export (.qasm())       │ ← Instance method
│     "Circuit to Text"           │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 8.2 QASM Import (from_qasm_*)   │ ← STATIC methods!
│     "Text to Circuit"           │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 8.3 File I/O                    │
│     "Save/Load .qasm files"     │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 8.4 QASM 2 vs QASM 3            │
│     "Versions & Features"       │
└─────────────────────────────────┘
  │
  ▼
┌─────────────────────────────────┐
│ 8.5 QASM 3 Data Types           │
│     "Advanced Type System"      │
└─────────────────────────────────┘
  │
  ▼
 END
```

---

# 📖 TOPIC 8.1: QASM Export - `qc.qasm()`

## 8.1.1 Basic Export

### Definition
The `qasm()` method exports a QuantumCircuit to OpenQASM 2.0 string format.

### Analogy
**"Taking a photo"** - The circuit exists as a 3D object (Python), and `qasm()` takes a "photo" (text snapshot) that can be printed and shared.

### Signature

```python
QuantumCircuit.qasm() -> str
```

**Parameters**: None required for basic usage
**Returns**: `str` - OpenQASM 2.0 formatted string

### Implementation

```python
from qiskit import QuantumCircuit

# Create a Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Export to QASM string
qasm_string = qc.qasm()
print(qasm_string)
```

**Output**:
```qasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg meas[2];
h q[0];
cx q[0],q[1];
barrier q[0],q[1];
measure q[0] -> meas[0];
measure q[1] -> meas[1];
```

### ⚠️ Trap Alert

```python
# ❌ WRONG - not saving the string
qc.qasm()  # Returns string but discards it!

# ✅ CORRECT - assign to variable
qasm_string = qc.qasm()
```

### 🧠 Mnemonic: "QASM needs Q"
- `qc.qasm()` - needs a **q**uantum **c**ircuit object
- It's an instance method - you must have a circuit first!

### ✅ Quick Check
Q: What does `qc.qasm()` return?
A: A string in OpenQASM 2.0 format

---

## 8.1.2 QASM 2.0 Structure

### Definition
OpenQASM 2.0 files have a specific structure with version declaration, includes, registers, and operations.

### Analogy
**"Recipe format"** - Every recipe has: title (version), ingredients list (registers), and steps (gates). QASM has the same structure.

### Visual Structure

```
┌─────────────────────────────────────────────────────┐
│ OPENQASM 2.0 FILE STRUCTURE                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  OPENQASM 2.0;              ← 1. Version header     │
│  include "qelib1.inc";      ← 2. Gate library       │
│  qreg q[2];                 ← 3. Quantum register   │
│  creg c[2];                 ← 4. Classical register │
│  h q[0];                    ← 5. Gate operations    │
│  cx q[0],q[1];              │                       │
│  measure q[0] -> c[0];      ← 6. Measurements       │
│  measure q[1] -> c[1];      │                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2, name='bell')
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print("=== QASM 2.0 Structure ===")
for i, line in enumerate(qc.qasm().split('\n'), 1):
    print(f"{i:2}: {line}")
```

### ⚠️ Trap Alert

```python
# QASM gate names may differ from Qiskit!
# Qiskit: qc.cx(0, 1)
# QASM:   cx q[0],q[1];

# Some gates have different names:
# Qiskit: qc.ccx(0, 1, 2)  (Toffoli)
# QASM:   ccx q[0],q[1],q[2];
```

### 🧠 Mnemonic: "VIRL-GM"
**V**ersion, **I**nclude, **R**egisters (q then c), **L**ogic (gates), **M**easure

### ✅ Quick Check
Q: What's the first line of every QASM 2.0 file?
A: `OPENQASM 2.0;`

---

# 📖 TOPIC 8.2: QASM Import - Static Methods ⚠️

## 8.2.1 from_qasm_str() - EXAM CRITICAL!

### Definition
`from_qasm_str()` creates a QuantumCircuit from an OpenQASM string. **It is a STATIC/CLASS method!**

### Analogy
**"Building from blueprints"** - You don't need an existing building to read blueprints. Similarly, you don't need an existing circuit to import QASM - that's why it's a CLASS method!

### Math/Visual

```
┌───────────────────────────────────────────────────────────────┐
│ STATIC vs INSTANCE METHODS                                    │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  INSTANCE Method:  object.method()                            │
│    qc.qasm()       ← Need existing circuit (qc)              │
│    qc.draw()       ← Need existing circuit                   │
│    qc.depth()      ← Need existing circuit                   │
│                                                               │
│  STATIC/CLASS Method:  Class.method()                         │
│    QuantumCircuit.from_qasm_str(s)   ← NO circuit needed!    │
│    QuantumCircuit.from_qasm_file(f)  ← NO circuit needed!    │
│                                                               │
│  ⚠️ Why static? You're CREATING a circuit, not using one!    │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Implementation

```python
from qiskit import QuantumCircuit

qasm_string = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
"""

# ✅ CORRECT: Static method on CLASS
qc = QuantumCircuit.from_qasm_str(qasm_string)
print(qc.draw())

# ❌ WRONG: Instance method (will fail!)
# qc = qc.from_qasm_str(qasm_string)  # ERROR!
```

### ⚠️ Trap Alert - THE #1 EXAM TRAP!

```python
# ❌ WRONG - All of these FAIL!
qc = QuantumCircuit(2)
qc.from_qasm_str(qasm_string)           # Instance method - WRONG!
qc = qc.from_qasm_str(qasm_string)      # Still wrong!
QuantumCircuit().from_qasm_str(string)  # Wasteful + wrong pattern

# ✅ CORRECT - Call on the CLASS
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

### 🧠 Mnemonic: "FROM needs NO OBJECT" (FNO)
- `from_qasm_str` → "**FROM** string" → No object needed, call on CLASS
- `from_qasm_file` → "**FROM** file" → No object needed, call on CLASS
- `qasm()` → "**TO** string" → Needs object (instance method)

### 🧠 Mnemonic: "STATIC = Start from Scratch"
- **S**tatic methods **S**tart from **S**cratch
- You don't have a circuit yet, so call on the Class!

### ✅ Quick Check
Q: What's wrong with `qc.from_qasm_str(s)`?
A: `from_qasm_str()` is STATIC - call `QuantumCircuit.from_qasm_str(s)` instead!

---

## 8.2.2 from_qasm_file() - Also Static!

### Definition
`from_qasm_file()` loads a QuantumCircuit from a QASM file. Also a STATIC method!

### Analogy
**"Opening a saved blueprint"** - You don't need an existing building to open a blueprint file from disk.

### Implementation

```python
from qiskit import QuantumCircuit

# ✅ CORRECT: Static method on CLASS
qc = QuantumCircuit.from_qasm_file('my_circuit.qasm')

# ❌ WRONG: Instance method
# qc = qc.from_qasm_file('my_circuit.qasm')  # ERROR!
```

### ⚠️ Trap Alert

```python
# Both import methods are STATIC!
QuantumCircuit.from_qasm_str(string)  # Static
QuantumCircuit.from_qasm_file(path)   # Static

# The export method is INSTANCE!
qc.qasm()  # Instance
```

### 🧠 Mnemonic: "Two FROMs, One TO"
- **FROM** string → `QuantumCircuit.from_qasm_str()` (Static)
- **FROM** file → `QuantumCircuit.from_qasm_file()` (Static)
- **TO** string → `qc.qasm()` (Instance)

### ✅ Quick Check
Q: Is `from_qasm_file()` static or instance?
A: STATIC - call `QuantumCircuit.from_qasm_file(path)`

---

# 📖 TOPIC 8.3: File I/O Operations

## 8.3.1 Saving QASM Files

### Definition
Save a circuit to a `.qasm` file using standard Python file I/O with `qc.qasm()`.

### Analogy
**"Printing and filing a blueprint"** - You print (`qasm()`) the blueprint and file it (`write()`).

### Implementation

```python
from qiskit import QuantumCircuit

# Create circuit
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()

# Save to file
with open('ghz_circuit.qasm', 'w') as f:
    f.write(qc.qasm())

print("✅ Saved to ghz_circuit.qasm")
```

### ⚠️ Trap Alert

```python
# There's NO direct save_to_file() method!
# Must use standard file I/O

# ❌ WRONG - no such method
qc.save_to_qasm('file.qasm')  # Doesn't exist!

# ✅ CORRECT - use Python file I/O
with open('file.qasm', 'w') as f:
    f.write(qc.qasm())
```

### 🧠 Mnemonic: "Write What QASM Returns"
- `qasm()` returns a string
- `write()` writes a string
- Chain them: `f.write(qc.qasm())`

### ✅ Quick Check
Q: How do you save a circuit to a .qasm file?
A: `with open('file.qasm', 'w') as f: f.write(qc.qasm())`

---

## 8.3.2 Loading QASM Files

### Definition
Load a circuit from a `.qasm` file using the static `from_qasm_file()` method.

### Implementation

```python
from qiskit import QuantumCircuit

# Load from file (STATIC METHOD!)
qc = QuantumCircuit.from_qasm_file('ghz_circuit.qasm')
print(qc.draw())
```

### ⚠️ Trap Alert

```python
# Don't confuse file loading methods!

# ❌ WRONG - there's no load() method
qc = QuantumCircuit.load('file.qasm')  # Doesn't exist!

# ❌ WRONG - from_qasm_str is for strings, not files
with open('file.qasm', 'r') as f:
    qc = QuantumCircuit.from_qasm_str(f)  # f is file object, not string!

# ✅ CORRECT - use from_qasm_file directly
qc = QuantumCircuit.from_qasm_file('file.qasm')

# ✅ ALSO CORRECT - read file then from_qasm_str
with open('file.qasm', 'r') as f:
    qc = QuantumCircuit.from_qasm_str(f.read())  # f.read() returns string
```

### 🧠 Mnemonic: "File→File, String→String"
- `from_qasm_file()` takes a **file path**
- `from_qasm_str()` takes a **string**

### ✅ Quick Check
Q: What's the argument to `from_qasm_file()`?
A: A file path (string), not a file object

---

## 8.3.3 Round-Trip Verification

### Definition
Export a circuit to QASM and reimport it to verify equivalence.

### Implementation

```python
from qiskit import QuantumCircuit

# Create original
original = QuantumCircuit(2)
original.h(0)
original.cx(0, 1)
original.measure_all()

# Export to QASM
qasm_str = original.qasm()

# Reimport (STATIC!)
restored = QuantumCircuit.from_qasm_str(qasm_str)

# Verify
print(f"Original depth: {original.depth()}")
print(f"Restored depth: {restored.depth()}")
print(f"Match: {original.depth() == restored.depth()}")

# Visual comparison
print("\nOriginal:")
print(original.draw())
print("\nRestored:")
print(restored.draw())
```

### ⚠️ Trap Alert

```python
# Circuit names may not survive round-trip!
qc = QuantumCircuit(2, name='my_circuit')
restored = QuantumCircuit.from_qasm_str(qc.qasm())
# restored may have different name!
```

### 🧠 Mnemonic: "Export-Import-Compare"

### ✅ Quick Check
Q: What method pattern tests QASM round-trip?
A: `qc.qasm()` → `QuantumCircuit.from_qasm_str()` → compare

---

# 📖 TOPIC 8.4: QASM 2 vs QASM 3

## 8.4.1 qasm2 Module

### Definition
The `qiskit.qasm2` module provides explicit QASM 2.0 import/export functions.

### Analogy
**"Standard format"** - QASM 2.0 is like PDF - universally readable, simpler, widely supported.

### Implementation

```python
from qiskit import QuantumCircuit
from qiskit import qasm2

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Export with qasm2 module
qasm2_str = qasm2.dumps(qc)
print("=== QASM 2.0 ===")
print(qasm2_str)

# Import with qasm2 module
restored = qasm2.loads(qasm2_str)
```

### ⚠️ Trap Alert

```python
# qasm2 functions vs QuantumCircuit methods:

# qasm2 module functions:
qasm2.dumps(qc)      # Export to string
qasm2.loads(s)       # Import from string
qasm2.dump(qc, f)    # Export to file object
qasm2.load(f)        # Import from file object

# QuantumCircuit methods:
qc.qasm()                              # Export to QASM 2.0 string
QuantumCircuit.from_qasm_str(s)        # Import from string
QuantumCircuit.from_qasm_file(path)    # Import from file path
```

### 🧠 Mnemonic: "DumpS/LoadS = Strings, Dump/Load = Files"
- `dumps`/`loads` → work with **s**trings
- `dump`/`load` → work with file objects

### ✅ Quick Check
Q: What's the difference between `qasm2.dumps()` and `qc.qasm()`?
A: Same output (QASM 2.0), different API (`qasm2.dumps(qc)` vs `qc.qasm()`)

---

## 8.4.2 qasm3 Module

### Definition
The `qiskit.qasm3` module provides OpenQASM 3.0 export capabilities with advanced features.

### Analogy
**"Advanced format"** - QASM 3.0 is like a Word doc with macros - more features but less portable.

### Implementation

```python
from qiskit import QuantumCircuit
from qiskit import qasm3

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Export with qasm3 module
qasm3_str = qasm3.dumps(qc)
print("=== QASM 3.0 ===")
print(qasm3_str)
```

**QASM 3.0 Output**:
```qasm
OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c[0] = measure q[0];
c[1] = measure q[1];
```

### ⚠️ Trap Alert

```python
# QASM 2.0 vs 3.0 syntax differences:

# Version declaration:
# QASM 2.0: OPENQASM 2.0;
# QASM 3.0: OPENQASM 3.0;

# Include file:
# QASM 2.0: include "qelib1.inc";
# QASM 3.0: include "stdgates.inc";

# Register declaration:
# QASM 2.0: qreg q[2]; creg c[2];
# QASM 3.0: qubit[2] q; bit[2] c;

# Measurement syntax:
# QASM 2.0: measure q[0] -> c[0];
# QASM 3.0: c[0] = measure q[0];
```

### 🧠 Mnemonic: "3.0 uses ="
- QASM 2.0: `measure q[0] -> c[0];` (arrow)
- QASM 3.0: `c[0] = measure q[0];` (assignment)

### ✅ Quick Check
Q: How does measurement syntax differ between QASM 2 and 3?
A: QASM 2: `measure q -> c;` | QASM 3: `c = measure q;`

---

## 8.4.3 QASM 2 vs QASM 3 Comparison

### Visual Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│              QASM 2.0 vs QASM 3.0 COMPARISON                    │
├───────────────────────────┬─────────────────────────────────────┤
│      QASM 2.0             │           QASM 3.0                  │
├───────────────────────────┼─────────────────────────────────────┤
│ OPENQASM 2.0;             │ OPENQASM 3.0;                       │
│ include "qelib1.inc";     │ include "stdgates.inc";             │
│ qreg q[2];                │ qubit[2] q;                         │
│ creg c[2];                │ bit[2] c;                           │
│ h q[0];                   │ h q[0];                             │
│ cx q[0],q[1];             │ cx q[0], q[1];                      │
│ measure q[0] -> c[0];     │ c[0] = measure q[0];                │
├───────────────────────────┴─────────────────────────────────────┤
│ Features:                                                        │
│ QASM 2.0: Basic gates, measurements, universal compatibility    │
│ QASM 3.0: Control flow, subroutines, types, parameters          │
└─────────────────────────────────────────────────────────────────┘
```

### Comparison Table

| Feature | QASM 2.0 | QASM 3.0 |
|---------|----------|----------|
| **Status** | Default, stable | Advanced, experimental |
| **Include** | `qelib1.inc` | `stdgates.inc` |
| **Qubits** | `qreg q[n];` | `qubit[n] q;` |
| **Bits** | `creg c[n];` | `bit[n] c;` |
| **Measure** | `measure q -> c;` | `c = measure q;` |
| **Control flow** | Limited | `if`, `for`, `while` |
| **Subroutines** | No | `def`, `gate` |
| **Types** | Basic | `int`, `float`, `angle` |
| **Compatibility** | Universal | Limited |

### Implementation

```python
from qiskit import QuantumCircuit
from qiskit import qasm2, qasm3

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print("=== QASM 2.0 ===")
print(qasm2.dumps(qc))
print("\n=== QASM 3.0 ===")
print(qasm3.dumps(qc))
```

### ⚠️ Trap Alert

```python
# Exam question: "What's the default QASM version in Qiskit?"
# Answer: QASM 2.0

# qc.qasm() returns QASM 2.0 by default
# For QASM 3.0, use qasm3.dumps(qc)
```

### 🧠 Mnemonic: "2 is Two-way, 3 is Three-plus features"
- QASM 2.0: Universal compatibility (two-way between all frameworks)
- QASM 3.0: More features (control flow, types, etc.)

### ✅ Quick Check
Q: What version does `qc.qasm()` output by default?
A: OpenQASM 2.0

---

## 8.4.4 QASM 3 Advanced Features

### Definition
QASM 3.0 supports parameterized circuits, classical control flow, and custom exporter options.

### Parameterized Circuits

```python
from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import Parameter

theta = Parameter('theta')
qc = QuantumCircuit(1)
qc.ry(theta, 0)

qasm3_str = qasm3.dumps(qc)
print(qasm3_str)
# OPENQASM 3.0;
# include "stdgates.inc";
# input float[64] theta;    ← Parameters become inputs!
# qubit[1] q;
# ry(theta) q[0];
```

### Classical Control Flow

```python
from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import QuantumRegister, ClassicalRegister

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

qc.h(qr[0])
qc.measure(qr[0], cr[0])

# Classical conditional
with qc.if_test((cr[0], 1)):
    qc.x(qr[1])

qasm3_str = qasm3.dumps(qc)
# Output includes: if (c[0] == 1) { x q[1]; }
```

### Custom Exporter

```python
from qiskit import QuantumCircuit, qasm3

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Custom exporter without includes
exporter = qasm3.Exporter(
    includes=[],                # No include statements
    disable_constants=True,     # No constant folding
)
custom_qasm = exporter.dumps(qc)
```

### ⚠️ Trap Alert

```python
# QASM 3 parameter syntax:
# input float[64] theta;     ← Parameters become 'input' declarations

# QASM 3 conditional syntax:
# if (c[0] == 1) { x q[1]; } ← Full if/else support
```

### 🧠 Mnemonic: "3.0 = Inputs + Ifs"
- QASM 3.0 supports `input` parameters and `if` statements

### ✅ Quick Check
Q: How do parameters appear in QASM 3.0?
A: As `input` declarations: `input float[64] theta;`

---

# 📖 TOPIC 8.5: OpenQASM 3 Data Types

## 8.5.1 Complete Type Reference

### Definition
OpenQASM 3.0 introduces a comprehensive type system for classical data manipulation.

### Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│              QASM 3.0 TYPE HIERARCHY                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  QUANTUM TYPES                                                  │
│  ├── qubit              Single qubit                           │
│  └── qubit[n]           Qubit array                            │
│                                                                 │
│  CLASSICAL TYPES                                                │
│  ├── bit               Single bit (0 or 1)                     │
│  ├── bit[n]            Bit array                               │
│  ├── int[n]            Signed integer (n bits)                 │
│  ├── uint[n]           Unsigned integer (n bits)               │
│  ├── float[n]          Floating point (16/32/64)               │
│  ├── angle[n]          Fixed-point angle [0, 2π)               │
│  ├── bool              Boolean (true/false)                    │
│  ├── duration          Time duration                           │
│  ├── stretch           Flexible duration                       │
│  └── complex[float[n]] Complex number                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Type Reference Table

| Type | Description | Example | Range/Notes |
|------|-------------|---------|-------------|
| `bit` | Single classical bit | `bit c;` | 0 or 1 |
| `bit[n]` | Bit array | `bit[8] reg;` | Array of n bits |
| `int[n]` | Signed integer | `int[32] counter;` | Signed, n-bit |
| `uint[n]` | Unsigned integer | `uint[16] count;` | Unsigned, n-bit |
| `float[n]` | Floating point | `float[64] angle;` | n = 16, 32, 64 |
| `angle[n]` | Fixed-point angle | `angle[32] theta;` | Range [0, 2π) |
| `bool` | Boolean | `bool flag;` | true/false |
| `duration` | Time duration | `duration d;` | With time units |
| `stretch` | Flexible duration | `stretch s;` | Scheduler resolved |
| `complex[float[n]]` | Complex number | `complex[float[64]] c;` | Complex type |

### ⚠️ Trap Alert

```python
# int vs uint:
# int[8]  → signed: -128 to 127
# uint[8] → unsigned: 0 to 255

# float precision:
# float[16] → half precision (rarely used)
# float[32] → single precision
# float[64] → double precision (default)
```

### 🧠 Mnemonic: "BIFA-BD" (Basic Integer Float Angle - Bool Duration)
- **B**it, **I**nt, **F**loat, **A**ngle, **B**ool, **D**uration

### ✅ Quick Check
Q: What type is best for rotation angles in QASM 3?
A: `angle[n]` - optimized for range [0, 2π)

---

## 8.5.2 Built-in Constants

### Definition
QASM 3.0 provides mathematical constants for use in gate operations.

### Implementation

```qasm
OPENQASM 3.0;

// Mathematical constants
pi      // π = 3.14159265...
tau     // τ = 2π = 6.28318530...
euler   // e = 2.71828182...

// Usage in gates
rx(pi/2) q[0];      // X rotation by π/2
rz(tau/4) q[1];     // Z rotation by τ/4 = π/2
```

### Constant Reference

| Constant | Value | Description |
|----------|-------|-------------|
| `pi` | π ≈ 3.14159 | Circle ratio |
| `tau` | τ = 2π ≈ 6.28318 | Full rotation |
| `euler` | e ≈ 2.71828 | Euler's number |

### ⚠️ Trap Alert

```python
# QASM 3 constants are lowercase!
# ✅ pi, tau, euler
# ❌ PI, TAU, EULER

# tau = 2*pi (convenient for full rotations)
# rx(tau/4) = rx(pi/2)
```

### 🧠 Mnemonic: "PTE" (Pi, Tau, Euler)

### ✅ Quick Check
Q: What is `tau` in QASM 3.0?
A: τ = 2π (one full rotation)

---

## 8.5.3 Duration Type

### Definition
The `duration` type represents time intervals with explicit units.

### Implementation

```qasm
OPENQASM 3.0;

// Duration with units
duration d = 100ns;         // 100 nanoseconds
duration t = 1us;           // 1 microsecond
duration gate_time = 50dt;  // 50 device time units
```

### Duration Units

| Unit | Description | Example |
|------|-------------|---------|
| `ns` | Nanoseconds | `100ns` |
| `us` | Microseconds | `1us` |
| `ms` | Milliseconds | `1ms` |
| `s` | Seconds | `1s` |
| `dt` | Device time unit | `50dt` |

### ⚠️ Trap Alert

```python
# dt = device-specific time unit
# The actual duration of 1dt depends on the backend!

# Common exam question: "What is dt?"
# Answer: Backend-specific time unit
```

### 🧠 Mnemonic: "NUMsS-DT" (Nano, Micro, Milli, Seconds, Device Time)

### ✅ Quick Check
Q: What time units does QASM 3 support?
A: ns, us, ms, s, dt

---

# 📖 Topic Consolidated Review

## Static vs Instance Methods Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                STATIC vs INSTANCE CHEAT SHEET                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🔵 STATIC METHODS (Call on CLASS):                             │
│     QuantumCircuit.from_qasm_str(string)   # Import from string │
│     QuantumCircuit.from_qasm_file(path)    # Import from file   │
│                                                                 │
│  🟢 INSTANCE METHODS (Call on OBJECT):                          │
│     qc.qasm()        # Export to string                         │
│     qc.draw()        # Visualize                                │
│     qc.decompose()   # Break down gates                         │
│                                                                 │
│  💡 Memory Aid: "FROM needs NO OBJECT"                          │
│     • Import = creating circuit = no existing object needed     │
│     • Export = using circuit = need existing object             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## QASM Module Functions Summary

| Module | Function | Purpose |
|--------|----------|---------|
| `qasm2` | `dumps(qc)` | Circuit → QASM 2.0 string |
| `qasm2` | `loads(s)` | QASM 2.0 string → Circuit |
| `qasm2` | `dump(qc, f)` | Circuit → File object |
| `qasm2` | `load(f)` | File object → Circuit |
| `qasm3` | `dumps(qc)` | Circuit → QASM 3.0 string |
| `qasm3` | `loads(s)` | QASM 3.0 string → Circuit |
| `qasm3` | `Exporter` | Custom export options |

## QASM Syntax Comparison

| Element | QASM 2.0 | QASM 3.0 |
|---------|----------|----------|
| Version | `OPENQASM 2.0;` | `OPENQASM 3.0;` |
| Include | `include "qelib1.inc";` | `include "stdgates.inc";` |
| Qubits | `qreg q[2];` | `qubit[2] q;` |
| Bits | `creg c[2];` | `bit[2] c;` |
| Measure | `measure q[0] -> c[0];` | `c[0] = measure q[0];` |
| Control | Limited | `if`, `for`, `while` |

---

# ⚠️ Master Trap List

## Trap 1: Instance vs Static Method (CRITICAL!)

```python
# ❌ WRONG - calling static method on instance
qc = QuantumCircuit(2)
qc.from_qasm_str(qasm_string)  # FAILS!
qc = qc.from_qasm_str(qasm_string)  # FAILS!

# ✅ CORRECT - calling static method on class
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

**Mnemonic**: "FROM needs NO OBJECT" (FNO)

---

## Trap 2: Forgetting Assignment

```python
# ❌ WRONG - no assignment
QuantumCircuit.from_qasm_str(qasm_string)  # Returns circuit but discards it!
qc.qasm()  # Returns string but discards it!

# ✅ CORRECT - assign to variable
qc = QuantumCircuit.from_qasm_str(qasm_string)
qasm_str = qc.qasm()
```

**Mnemonic**: "Assign what you Import/Export"

---

## Trap 3: Wrong Method Name

```python
# ❌ WRONG - no such methods
qc = QuantumCircuit.from_qasm(qasm_string)      # Missing _str!
qc = QuantumCircuit.load_qasm(qasm_string)      # Wrong name!
qc = QuantumCircuit.from_qasm_string(s)         # Wrong name!

# ✅ CORRECT - exact method names
qc = QuantumCircuit.from_qasm_str(qasm_string)
qc = QuantumCircuit.from_qasm_file(path)
```

**Mnemonic**: "STR for String, FILE for File"

---

## Trap 4: File vs String Methods

```python
# ❌ WRONG - mixing file and string methods
with open('file.qasm', 'r') as f:
    qc = QuantumCircuit.from_qasm_str(f)  # f is file object, not string!

qc = QuantumCircuit.from_qasm_file(qasm_string)  # String is not a path!

# ✅ CORRECT - match method to argument type
qc = QuantumCircuit.from_qasm_file('file.qasm')  # Path string
qc = QuantumCircuit.from_qasm_str(qasm_string)   # QASM string
```

**Mnemonic**: "File→File, String→String"

---

## Trap 5: QASM Version Confusion

```python
# qc.qasm() returns QASM 2.0 (not 3.0!)
qasm2_output = qc.qasm()  # Always QASM 2.0

# For QASM 3.0, use qasm3 module
from qiskit import qasm3
qasm3_output = qasm3.dumps(qc)
```

**Mnemonic**: "qasm() = 2, qasm3 = 3"

---

## Trap 6: dumps vs dump (with 's')

```python
from qiskit import qasm2

# dumps = string (has 's' for string)
qasm_str = qasm2.dumps(qc)

# dump = file (no 's')
with open('file.qasm', 'w') as f:
    qasm2.dump(qc, f)
```

**Mnemonic**: "S for String: dumpS, loadS"

---

## Trap 7: QASM 2 vs 3 Syntax

```python
# QASM 2.0 measurement:
# measure q[0] -> c[0];    ← Arrow syntax

# QASM 3.0 measurement:
# c[0] = measure q[0];     ← Assignment syntax

# Different include files!
# QASM 2.0: qelib1.inc
# QASM 3.0: stdgates.inc
```

**Mnemonic**: "2 uses Arrow, 3 uses Assign"

---

## Trap 8: No Direct Save Method

```python
# ❌ WRONG - no such method exists
qc.save_qasm('file.qasm')
qc.to_qasm_file('file.qasm')

# ✅ CORRECT - use standard file I/O
with open('file.qasm', 'w') as f:
    f.write(qc.qasm())
```

**Mnemonic**: "Write What QASM Returns"

---

# 🧠 All Mnemonics Summary

| # | Mnemonic | Meaning |
|---|----------|---------|
| 1 | **FNO** | "FROM needs NO Object" - Static methods |
| 2 | **STATIC = Start from Scratch** | Static methods create new circuits |
| 3 | **Two FROMs, One TO** | `from_qasm_str`, `from_qasm_file` (static) vs `qasm()` (instance) |
| 4 | **VIRL-GM** | QASM structure: Version, Include, Registers, Logic, Measure |
| 5 | **File→File, String→String** | Match method to argument type |
| 6 | **S for String** | `dumps`/`loads` work with strings |
| 7 | **2 uses Arrow, 3 uses Assign** | Measurement syntax difference |
| 8 | **qasm() = 2, qasm3 = 3** | Default version is QASM 2.0 |
| 9 | **PTE** | QASM 3 constants: Pi, Tau, Euler |
| 10 | **BIFA-BD** | QASM 3 types: Bit, Int, Float, Angle, Bool, Duration |

---

# 📝 Practice Exam

## Question 1: Static Method Identification

**What's wrong with this code?**

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qasm_str = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0],q[1];
"""
new_qc = qc.from_qasm_str(qasm_str)
```

A) Missing measurement operations  
B) `from_qasm_str()` should be called on the class, not an instance  
C) The QASM string is invalid  
D) Missing classical register  

<details>
<summary>Answer</summary>

**B) `from_qasm_str()` should be called on the class, not an instance**

Correct code:
```python
new_qc = QuantumCircuit.from_qasm_str(qasm_str)
```

**Mnemonic**: "FROM needs NO OBJECT"
</details>

---

## Question 2: Export Method

**Which code correctly exports a circuit to QASM?**

A) `qasm_str = QuantumCircuit.qasm(qc)`  
B) `qasm_str = qc.qasm()`  
C) `qasm_str = qasm(qc)`  
D) `qasm_str = qc.to_qasm()`  

<details>
<summary>Answer</summary>

**B) `qasm_str = qc.qasm()`**

`qasm()` is an instance method called on the circuit object.
</details>

---

## Question 3: QASM Version

**What version does `qc.qasm()` output by default?**

A) OpenQASM 1.0  
B) OpenQASM 2.0  
C) OpenQASM 3.0  
D) Depends on circuit complexity  

<details>
<summary>Answer</summary>

**B) OpenQASM 2.0**

For QASM 3.0, use `qasm3.dumps(qc)`.
</details>

---

## Question 4: File Loading

**Which code correctly loads a circuit from a QASM file?**

A) `qc = QuantumCircuit.load('circuit.qasm')`  
B) `qc = QuantumCircuit.from_qasm('circuit.qasm')`  
C) `qc = QuantumCircuit.from_qasm_file('circuit.qasm')`  
D) `qc = qc.from_qasm_file('circuit.qasm')`  

<details>
<summary>Answer</summary>

**C) `qc = QuantumCircuit.from_qasm_file('circuit.qasm')`**

`from_qasm_file()` is a static method called on the class.
</details>

---

## Question 5: QASM Measurement Syntax

**What's the measurement syntax in OpenQASM 3.0?**

A) `measure q[0] -> c[0];`  
B) `c[0] = measure q[0];`  
C) `measure(q[0], c[0]);`  
D) `c[0] <- measure q[0];`  

<details>
<summary>Answer</summary>

**B) `c[0] = measure q[0];`**

QASM 3.0 uses assignment syntax, while QASM 2.0 uses arrow syntax.

**Mnemonic**: "2 uses Arrow, 3 uses Assign"
</details>

---

## Question 6: dumps vs dump

**What's the difference between `qasm2.dumps()` and `qasm2.dump()`?**

A) `dumps` is deprecated  
B) `dumps` returns a string, `dump` writes to a file object  
C) `dump` is faster  
D) No difference  

<details>
<summary>Answer</summary>

**B) `dumps` returns a string, `dump` writes to a file object**

**Mnemonic**: "S for String: dumpS, loadS"
</details>

---

## Question 7: Spot the Error

**What's wrong with this code?**

```python
from qiskit import QuantumCircuit

with open('circuit.qasm', 'r') as f:
    qc = QuantumCircuit.from_qasm_str(f)
```

A) Should use `from_qasm_file()` instead  
B) `from_qasm_str()` takes a string, not a file object  
C) Both A and B are correct  
D) Nothing is wrong  

<details>
<summary>Answer</summary>

**C) Both A and B are correct**

Either:
```python
qc = QuantumCircuit.from_qasm_file('circuit.qasm')
```
Or:
```python
with open('circuit.qasm', 'r') as f:
    qc = QuantumCircuit.from_qasm_str(f.read())  # Note: f.read()
```
</details>

---

## Question 8: QASM 3 Types

**Which type is best for rotation angles in QASM 3.0?**

A) `int[32]`  
B) `float[64]`  
C) `angle[32]`  
D) `bit[32]`  

<details>
<summary>Answer</summary>

**C) `angle[32]`**

The `angle` type is optimized for values in the range [0, 2π).
</details>

---

### Part B: Code Analysis (3-5 minutes each)

**Q9**: What's wrong with this code?
```python
from qiskit import QuantumCircuit

qasm_str = '''OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0], q[1];
'''

qc = QuantumCircuit(2)
new_qc = qc.from_qasm_str(qasm_str)
```

<details>
<summary>Answer</summary>

**Error**: `from_qasm_str()` is a STATIC method, not an instance method.

**Step-by-step**:
1. Creates a QuantumCircuit object `qc`
2. Tries to call `from_qasm_str()` as instance method ❌
3. This fails because `from_qasm_str()` must be called on the CLASS

**Correct code**:
```python
new_qc = QuantumCircuit.from_qasm_str(qasm_str)
```

**Mnemonic**: "FROM needs NO OBJECT"
</details>

---

**Q10**: What does this code output?
```python
from qiskit import QuantumCircuit, qasm3

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

qasm_output = qasm3.dumps(qc)
print("include" in qasm_output)
print("stdgates.inc" in qasm_output)
print("OPENQASM 3.0" in qasm_output)
```

<details>
<summary>Answer</summary>

**Output**:
```
True
True
True
```

**Explanation**:
1. `qasm3.dumps()` exports to QASM 3.0 format
2. QASM 3.0 includes `stdgates.inc` by default
3. Header is `OPENQASM 3.0;`
4. All three checks return True

**Topic**: QASM 3.0 format
</details>

---

**Q11**: What's the output of this code?
```python
from qiskit import qasm2

qasm_str = '''OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0], q[1];
'''

qc = qasm2.loads(qasm_str)
print(qc.num_qubits)
print(qc.num_clbits)
```

<details>
<summary>Answer</summary>

**Output**:
```
2
2
```

**Explanation**:
1. `qasm2.loads()` parses QASM 2.0 string
2. Creates circuit with 2 qubits (`qreg q[2]`)
3. Creates circuit with 2 classical bits (`creg c[2]`)

**Topic**: qasm2 module
</details>

---

**Q12**: Will this code work? What's the result?
```python
from qiskit import QuantumCircuit, qasm3

qasm3_str = '''OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c[0] = measure q[0];
c[1] = measure q[1];
'''

qc = qasm3.loads(qasm3_str)
qasm_out = qasm3.dumps(qc)
qc2 = qasm3.loads(qasm_out)
print(qc.num_qubits == qc2.num_qubits)
```

<details>
<summary>Answer</summary>

**Output**:
```
True
```

**Explanation**:
1. Import QASM 3.0 string → `qc` (2 qubits)
2. Export `qc` back to QASM 3.0 string
3. Import again → `qc2` (2 qubits)
4. Roundtrip preserves structure
5. Comparison returns True

**Topic**: QASM roundtrip
</details>

---

**Q13**: What's wrong with this QASM 3.0 code?
```qasm
OPENQASM 3.0;
include "qelib1.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
measure q -> c;
```

<details>
<summary>Answer</summary>

**Two errors**:
1. Wrong include file: `qelib1.inc` is QASM 2.0, should be `stdgates.inc`
2. Wrong measurement syntax: `measure q -> c` is QASM 2.0, should be `c = measure q`

**Correct QASM 3.0**:
```qasm
OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c[0] = measure q[0];
c[1] = measure q[1];
```

**Mnemonic**: "2 uses Arrow, 3 uses Assign"
</details>

---

### Part C: Scenario-Based (5-7 minutes each)

**Q14**: You're building a quantum circuit library that needs to share circuits with a collaborator using Cirq. What's the best approach to ensure interoperability?

<details>
<summary>Answer</summary>

**Approach**:
1. Use OpenQASM 2.0 for maximum compatibility
2. Export circuits using `qc.qasm()` or `qasm2.dumps(qc)`
3. Save to `.qasm` files for sharing

**Implementation**:
```python
from qiskit import QuantumCircuit

# Create your circuit
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# Export to QASM 2.0 (most compatible)
qasm_str = qc.qasm()  # Returns QASM 2.0

# Save to file
with open('shared_circuit.qasm', 'w') as f:
    f.write(qasm_str)

# Collaborator can import in Cirq:
# import cirq
# circuit = cirq.read_qasm('shared_circuit.qasm')
```

**Key insight**: QASM 2.0 is the universal format - all major frameworks support it!
</details>

---

**Q15**: You need to import a circuit from a QASM file, modify it by adding measurements, then export it back. Write the complete code.

<details>
<summary>Answer</summary>

**Implementation**:
```python
from qiskit import QuantumCircuit, qasm3

# Step 1: Load from file (STATIC method!)
qc = qasm3.load('input_circuit.qasm')

# Step 2: Add measurements
qc.measure_all()  # Add measurement to all qubits

# Step 3: Export back to file
with open('modified_circuit.qasm', 'w') as f:
    qasm3.dump(qc, f)

# Verify
print(f"Qubits: {qc.num_qubits}")
print(f"Classical bits: {qc.num_clbits}")
print("Circuit modified and saved!")
```

**Topics combined**: File I/O, circuit modification, QASM export
**Key insight**: Use `qasm3.load()` (function) for files, not `from_qasm_file()`
</details>

---

**Q16**: Your team is transitioning from QASM 2.0 to QASM 3.0. Write code that takes a QASM 2.0 string and converts it to QASM 3.0 format.

<details>
<summary>Answer</summary>

**Implementation**:
```python
from qiskit import QuantumCircuit, qasm2, qasm3

def convert_qasm2_to_qasm3(qasm2_string):
    """Convert QASM 2.0 string to QASM 3.0 format."""
    # Step 1: Import QASM 2.0
    qc = qasm2.loads(qasm2_string)
    
    # Step 2: Export as QASM 3.0
    qasm3_string = qasm3.dumps(qc)
    
    return qasm3_string

# Example usage
qasm2_input = '''OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0], q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
'''

qasm3_output = convert_qasm2_to_qasm3(qasm2_input)
print("Converted QASM 3.0:")
print(qasm3_output)
```

**Key differences in output**:
- Header: `OPENQASM 3.0;`
- Include: `stdgates.inc`
- Registers: `qubit[2] q; bit[2] c;`
- Measurement: `c[0] = measure q[0];`

**Topics combined**: qasm2 module, qasm3 module, format conversion
</details>

---

### Score Yourself

| Section | Total Qs | Your Score | Percentage |
|---------|----------|------------|------------|
| Part A (Quick Fire) | 8 | /8 | % |
| Part B (Code Analysis) | 5 | /5 | % |
| Part C (Scenarios) | 3 | /3 | % |
| **TOTAL** | **16** | **/16** | **%** |

**Interpretation**:
- 90-100%: Ready for Section 8 exam questions
- 75-89%: Review static vs instance methods
- Below 75%: Re-study QASM import/export patterns

---

# 💡 Key Takeaways

## Concept Mastery Checklist

```
□ I understand the difference between QASM 2.0 and QASM 3.0 syntax
□ I know qasm2 module uses loads()/dumps()/load()/dump()
□ I know qasm3 module uses loads()/dumps()/load()/dump()
□ I understand QuantumCircuit has legacy methods (qasm(), from_qasm_str(), from_qasm_file())
□ I know the difference between string methods (*s) and file methods (no s)
□ I can identify QASM version from header (OPENQASM 2.0 vs 3.0)
□ I know include file differences (qelib1.inc vs stdgates.inc)
□ I understand register syntax differences (qreg/creg vs qubit[]/bit[])
□ I know measurement syntax (arrow vs assignment)
```

## Code Mastery Checklist

```
□ I can export circuit to QASM 2.0: qc.qasm() or qasm2.dumps(qc)
□ I can export circuit to QASM 3.0: qasm3.dumps(qc)
□ I can import QASM 2.0 string: qasm2.loads(string) or QuantumCircuit.from_qasm_str(string)
□ I can import QASM 3.0 string: qasm3.loads(string)
□ I can save to file: qasm2.dump(qc, file) or qasm3.dump(qc, file)
□ I can load from file: qasm2.load(file) or qasm3.load(file)
□ I can convert QASM 2.0 to 3.0: qasm3.dumps(qasm2.loads(qasm2_string))
□ I can check circuit validity after roundtrip import/export
```

## Trap Avoidance Checklist

```
□ I know from_qasm_str() is STATIC (call on class, not instance)
□ I know from_qasm_file() is STATIC (call on class, not instance)  
□ I won't confuse loads() (string) with load() (file)
□ I won't confuse dumps() (string) with dump() (file)
□ I won't mix QASM 2.0 include files with QASM 3.0 code
□ I won't use arrow syntax in QASM 3.0 measurements
□ I remember qc.qasm() returns QASM 2.0, not 3.0
□ I know qasm2/qasm3 modules are functions, not methods
```

## Mnemonic Recall Box

```
┌─────────────────────────────────────────────────┐
│  "FROM needs NO OBJECT"                         │
│  → from_qasm_str() is STATIC                    │
│                                                 │
│  "s = string, no s = file"                      │
│  → loads/dumps for strings, load/dump for files │
│                                                 │
│  "2 uses Arrow, 3 uses Assign"                  │
│  → QASM 2.0: measure q -> c                     │
│  → QASM 3.0: c = measure q                      │
│                                                 │
│  "QELIB is TWO, STD is THREE"                   │
│  → qelib1.inc = QASM 2.0                        │
│  → stdgates.inc = QASM 3.0                      │
│                                                 │
│  "Export: Instance, Import: Static"             │
│  → qc.qasm() - instance method                  │
│  → QuantumCircuit.from_qasm_str() - static      │
└─────────────────────────────────────────────────┘
```

## One-Page Summary Box

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           OPENQASM QUICK REFERENCE                            │
├──────────────────────────────────────────────────────────────────────────────┤
│  EXPORT (Circuit → String/File)                                               │
│  ─────────────────────────────                                               │
│  QASM 2.0:  qc.qasm()              # Returns string (instance method)        │
│             qasm2.dumps(qc)        # Returns string (function)               │
│             qasm2.dump(qc, file)   # Writes to file (function)               │
│  QASM 3.0:  qasm3.dumps(qc)        # Returns string (function)               │
│             qasm3.dump(qc, file)   # Writes to file (function)               │
│                                                                               │
│  IMPORT (String/File → Circuit)                                               │
│  ─────────────────────────────────                                           │
│  QASM 2.0:  QuantumCircuit.from_qasm_str(s)   # STATIC! Class method         │
│             QuantumCircuit.from_qasm_file(f)  # STATIC! Class method         │
│             qasm2.loads(s)                    # Function                     │
│             qasm2.load(file)                  # Function                     │
│  QASM 3.0:  qasm3.loads(s)                    # Function                     │
│             qasm3.load(file)                  # Function                     │
├──────────────────────────────────────────────────────────────────────────────┤
│  VERSION DIFFERENCES                                                          │
│  ───────────────────                                                         │
│  Feature         │ QASM 2.0          │ QASM 3.0                              │
│  ────────────────┼───────────────────┼───────────────────────────────────────│
│  Header          │ OPENQASM 2.0;     │ OPENQASM 3.0;                         │
│  Include         │ qelib1.inc        │ stdgates.inc                          │
│  Qubit reg       │ qreg q[2];        │ qubit[2] q;                           │
│  Classical reg   │ creg c[2];        │ bit[2] c;                             │
│  Measurement     │ measure q -> c;   │ c = measure q;                        │
├──────────────────────────────────────────────────────────────────────────────┤
│  ⚠️  #1 EXAM TRAP: from_qasm_str() is STATIC - NO INSTANCE!                   │
│  ❌ qc.from_qasm_str(s)              # WRONG - instance call                  │
│  ✅ QuantumCircuit.from_qasm_str(s)  # CORRECT - class call                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Files in This Section

| File | Purpose | Key Content |
|------|---------|-------------|
| [README.md](README.md) | Complete learning guide | Theory, 8 traps, 16 practice questions, checklists |
| [openqasm_operations.ipynb](openqasm_operations.ipynb) | CODE LABORATORY | Executable examples, trap demonstrations, challenges |
| [README_OLD.md](README_OLD.md) | Backup | Previous version for reference |
| [openqasm_operations_OLD.ipynb](openqasm_operations_OLD.ipynb) | Backup | Previous notebook version |

---

## ➡️ Next Steps

1. **Complete the notebook**: Run all cells in [openqasm_operations.ipynb](openqasm_operations.ipynb)
2. **Practice the traps**: Identify static vs instance methods in 3 code snippets
3. **Do the challenges**: Complete all 3 Code Challenges without looking at solutions
4. **Take Practice Exam**: Score at least 90% on the 16-question exam above
5. **Review Section 9**: Continue to [Section 9: Quantum Information](../section_9_quantum_info/README.md) for Operators, Pauli, state vectors

---

## 🔗 Related Sections

- **Section 3**: Circuit creation methods
- **Section 2**: Circuit visualization (vs QASM text format)
- **Section 4**: Transpilation (can export transpiled circuits to QASM)

---

## 📚 Additional Resources

- OpenQASM 2.0 Spec: [github.com/openqasm/openqasm](https://github.com/openqasm/openqasm)
- OpenQASM 3.0 Spec: [openqasm.com](https://openqasm.com)
- IBM Quantum Docs: [docs.quantum.ibm.com](https://docs.quantum.ibm.com)

---

**Remember the #1 Exam Trap**:
```python
# ❌ qc.from_qasm_str(string)  - WRONG (instance)
# ✅ QuantumCircuit.from_qasm_str(string)  - CORRECT (static)
```

🎯 **Exam Success Tip**: Write "STATIC METHOD" on your scratch paper before the exam starts!

---

*Last Updated: 2025-01-15 | Qiskit Version: 1.x | Exam Weight: ~6%*
