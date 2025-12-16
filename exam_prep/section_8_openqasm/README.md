# Section 8: OpenQASM Operations

> **Exam Weight**: 6% (~4 Questions) | **Difficulty**: Medium | **Status**: EXAM TRAP - Static Methods!

```
┌─────────────────────────────────────────────────────────────────┐
│  EXAM TRAP: from_qasm_str() is a STATIC method!                │
│  • QuantumCircuit.from_qasm_str(string) ✓ CORRECT              │
│  • qc.from_qasm_str(string) ✗ WRONG                            │
│  • This trips up many exam takers - don't be one of them!      │
└─────────────────────────────────────────────────────────────────┘
```

## 📚 Overview

OpenQASM (Open Quantum Assembly Language) is the standard text format for representing quantum circuits, enabling interoperability between quantum computing frameworks (Qiskit, Cirq, Q#, etc.).

**Key Operations**:
- **Export**: `circuit.qasm()` - Convert circuit to QASM string
- **Import**: `QuantumCircuit.from_qasm_str()` - Create circuit from QASM (STATIC!)
- **File I/O**: `QuantumCircuit.from_qasm_file()` - Load from file (STATIC!)
- **QASM 2.0**: `qiskit.qasm2` module (dump, dumps, load, loads)
- **QASM 3.0**: `qiskit.qasm3` module (dump, dumps, load, loads, Exporter)
- **Versions**: QASM 2.0 (default) vs QASM 3.0 (advanced features)

---

## 🎯 Why This Section Matters

### 🧠 Conceptual Deep Dive

#### Analogy: The Blueprint
OpenQASM is like the blueprint of a building.
- **Circuit Object**: The 3D model in the architect's software (Python object).
- **OpenQASM**: The printed 2D blueprints (Text format).
- **Hardware**: The actual building constructed from the blueprints.
- **Portability**: Any contractor (simulator/hardware) can build the house if they have the blueprint, regardless of what software drew it.

#### The "Assembly" Language
QASM stands for Quantum ASseMbly language. Just like classical assembly code moves data between registers and performs basic arithmetic, QASM moves quantum states and performs basic gates.

### 1. **Interoperability**
Share circuits between different quantum frameworks:
- Qiskit → Cirq
- Qiskit → Q#
- Qiskit → other quantum languages

### 2. **Storage & Version Control**
Save circuits as human-readable text files:
- Track changes with Git
- Archive circuit designs
- Document algorithms

### 3. **Debugging**
Inspect circuit structure in text format:
- Verify gate sequences
- Check qubit assignments
- Validate measurements

### 4. **EXAM TRAP**
The `from_qasm_str()` and `from_qasm_file()` methods are **STATIC** - this is a common exam mistake that can cost you points!

---

## 📖 Core Concepts

### OpenQASM Versions

#### QASM 2.0 (Qiskit Default)
```qasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
```

**Features**:
- Basic quantum gates
- Measurements
- Classical registers
- Simple structure

#### QASM 3.0 (Advanced)
```qasm
OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
bit[2] c;

// Classical control
if (c[0] == 1) {
    x q[1];
}

// Loops
for int i in [0:3] {
    h q[i];
}
```

**Features**:
- Classical control flow (if/else)
- Loops (for, while)
- Subroutines/functions
- More powerful (but less supported)

---

## 🔷 QASM 3.0 Deep Dive

### QASM 3.0 Module Functions

```python
from qiskit import qasm3

# Export functions
qasm3.dumps(circuit)           # Export to string
qasm3.dump(circuit, file)      # Export to file object

# Import functions  
qasm3.loads(qasm_string)       # Import from string
qasm3.load(filename)           # Import from file

# Advanced exporter
exporter = qasm3.Exporter(includes=[], disable_constants=False)
qasm_str = exporter.dumps(circuit)
```

### QASM 3.0 Syntax Differences

| Feature | QASM 2.0 | QASM 3.0 |
|---------|----------|----------|
| **Header** | `OPENQASM 2.0;` | `OPENQASM 3.0;` |
| **Standard library** | `include "qelib1.inc";` | `include "stdgates.inc";` |
| **Qubit declaration** | `qreg q[2];` | `qubit[2] q;` |
| **Bit declaration** | `creg c[2];` | `bit[2] c;` |
| **Parameters** | Not native | `input float[64] theta;` |
| **Control flow** | Limited | Full `if/else`, `for`, `while` |

### QASM 3.0 Examples

#### Basic Export/Import

```python
from qiskit import QuantumCircuit, qasm3

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Export to QASM 3.0 string
qasm3_str = qasm3.dumps(qc)
print(qasm3_str)
# Output:
# OPENQASM 3.0;
# include "stdgates.inc";
# qubit[2] q;
# bit[2] c;
# h q[0];
# cx q[0], q[1];
# c[0] = measure q[0];
# c[1] = measure q[1];

# Import from QASM 3.0 string
restored = qasm3.loads(qasm3_str)
```

#### File Operations with QASM 3.0

```python
from qiskit import QuantumCircuit, qasm3

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Save to file
with open('circuit.qasm3', 'w') as f:
    qasm3.dump(qc, f)

# Load from file
loaded_qc = qasm3.load('circuit.qasm3')
```

#### Parameterized Circuits in QASM 3.0

```python
from qiskit import QuantumCircuit, qasm3
from qiskit.circuit import Parameter

theta = Parameter('theta')
qc = QuantumCircuit(1)
qc.ry(theta, 0)

# Export parameterized circuit
qasm3_str = qasm3.dumps(qc)
print(qasm3_str)
# OPENQASM 3.0;
# include "stdgates.inc";
# input float[64] theta;    ← Parameters become inputs!
# qubit[1] q;
# ry(theta) q[0];
```

#### Classical Control Flow in QASM 3.0

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

# Export with control flow
qasm3_str = qasm3.dumps(qc)
print(qasm3_str)
# OPENQASM 3.0;
# include "stdgates.inc";
# qubit[2] q;
# bit[2] c;
# h q[0];
# c[0] = measure q[0];
# if (c[0] == 1) {
#     x q[1];
# }
```

#### Custom Exporter Options

```python
from qiskit import QuantumCircuit, qasm3

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Default export (includes stdgates.inc)
default_qasm = qasm3.dumps(qc)

# Custom exporter without includes
exporter = qasm3.Exporter(
    includes=[],                # No include statements
    disable_constants=True,     # No constant folding
)
custom_qasm = exporter.dumps(qc)

# Custom exporter with specific includes
exporter2 = qasm3.Exporter(
    includes=['stdgates.inc', 'custom_gates.inc']
)
```

### QASM 3.0 vs QASM 2.0 Comparison

```python
from qiskit import QuantumCircuit
from qiskit import qasm2, qasm3

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# QASM 2.0 output
print("=== QASM 2.0 ===")
print(qasm2.dumps(qc))
# OPENQASM 2.0;
# include "qelib1.inc";
# qreg q[2];
# creg c[2];
# h q[0];
# cx q[0],q[1];
# measure q[0] -> c[0];
# measure q[1] -> c[1];

# QASM 3.0 output
print("=== QASM 3.0 ===")
print(qasm3.dumps(qc))
# OPENQASM 3.0;
# include "stdgates.inc";
# qubit[2] q;
# bit[2] c;
# h q[0];
# cx q[0], q[1];
# c[0] = measure q[0];
# c[1] = measure q[1];
```

---

## 💻 Code Examples

### Example 1: Export Circuit to QASM (Most Common)

```python
from qiskit import QuantumCircuit

# Create Bell state circuit
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

**🎯 EXAM TIP**: `qasm()` returns a string in OpenQASM 2.0 format by default.

### Example 2: Import from QASM String (STATIC METHOD - CRITICAL!)

```python
from qiskit import QuantumCircuit

# QASM string
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

# CORRECT: Static method on class
qc = QuantumCircuit.from_qasm_str(qasm_string)
print(qc.draw())

# WRONG: Instance method (will fail!)
# qc = qc.from_qasm_str(qasm_string)  # ✗ ERROR!
```

**🎯 EXAM TRAP**: `from_qasm_str()` is called on the **CLASS** (QuantumCircuit), not an instance!

### ⚠️ STATIC METHOD EXAM PATTERN (HIGHEST TESTED!)

**The #1 Exam Trick Question in Section 8**:

```python
# Question: "How do you load a circuit from QASM string?"

# ❌ WRONG OPTIONS (All fail!):
qc = QuantumCircuit(2)
qc.from_qasm_str(qasm_string)  # Instance method - FAILS!
qc = qc.from_qasm_str(qasm_string)  # Still wrong
QuantumCircuit().from_qasm_str(qasm_string)  # Wasteful + wrong pattern

# ✅ CORRECT:
qc = QuantumCircuit.from_qasm_str(qasm_string)  # Static/class method!
```

**Why is this tested so much?**
- Most Python methods are instance methods (`obj.method()`)
- QASM import methods are **class methods** (`Class.method()`)
- This is counter-intuitive and trips up 70% of exam takers!

**Memory Aid: "FROM needs NO OBJECT"**
- `from_qasm_str` = "**FROM** string" → No object needed, call on CLASS
- `from_qasm_file` = "**FROM** file" → No object needed, call on CLASS
- `qasm()` = "**TO** string" → Needs object (instance method)

**Complete Pattern Recognition**:
```python
# STATIC (Class methods - no instance needed):
QuantumCircuit.from_qasm_str(string)   # ✅ Import
QuantumCircuit.from_qasm_file(path)    # ✅ Import

# INSTANCE (Object methods - needs existing circuit):
qc.qasm()                              # ✅ Export to string
qc.draw()                              # ✅ Visualize
qc.decompose()                         # ✅ Break down gates
```

### 🎓 Exam Question Patterns - OpenQASM

**Pattern 1: "Identify the STATIC method"**
```python
# Question will show 4 options:
A) qc = QuantumCircuit(); qc.from_qasm_str(s)  # ❌
B) qc = QuantumCircuit.from_qasm_str(s)        # ✅ CORRECT!
C) qc = from_qasm_str(s)                       # ❌
D) qc = qasm_str(s)                            # ❌
```

**Pattern 2: "QASM version support"**
```
OpenQASM 2.0 → Fully supported, default
OpenQASM 3.0 → Partial support, advanced features

qc.qasm() → Always outputs QASM 2.0
```

**Pattern 3: "Export vs Import methods"**
```python
# Export (instance methods):
qasm_string = qc.qasm()           # To string
with open('file.qasm', 'w') as f:
    f.write(qc.qasm())            # To file

# Import (STATIC methods):
qc = QuantumCircuit.from_qasm_str(string)  # From string
qc = QuantumCircuit.from_qasm_file(path)   # From file
```

**Pattern 4: "What's in a QASM file?"**
```qasm
OPENQASM 2.0;              ← Version declaration
include "qelib1.inc";      ← Standard gate library
qreg q[2];                 ← Quantum register
creg c[2];                 ← Classical register
h q[0];                    ← Gate operations
cx q[0],q[1];
measure q[0] -> c[0];      ← Measurements
```

### 🧠 Memory Aids - OpenQASM

**"FROM uses Class, TO uses Object"**
- FROM QASM (import) → Class method → `QuantumCircuit.from_qasm_*()`
- TO QASM (export) → Instance method → `qc.qasm()`

**"Static = No Dot Before Class Name"**
- `QuantumCircuit.from_qasm_str()` ← No `qc.` prefix!
- Think: You don't have a circuit yet, so you can't call it on one!

**"Two Import Methods, One Export"**
- Import: `from_qasm_str()` and `from_qasm_file()`
- Export: `qasm()`

### ✅ OpenQASM Method Checklist

```
□ Importing? Use QuantumCircuit.from_qasm_*() (STATIC)
□ Exporting? Use qc.qasm() (INSTANCE)
□ Reading file? Use from_qasm_file() not from_qasm_str()
□ Writing file? Use qc.qasm() then write to file manually
□ Remember: No circuit object needed for import!
```

### Example 3: Save and Load QASM Files

```python
from qiskit import QuantumCircuit

# Create circuit
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure_all()

# Save to file
with open('my_circuit.qasm', 'w') as f:
    f.write(qc.qasm())

# Load from file (STATIC METHOD!)
loaded_qc = QuantumCircuit.from_qasm_file('my_circuit.qasm')
print(loaded_qc.draw())
```

**🎯 EXAM TIP**: `from_qasm_file()` is also a STATIC method!

### Example 4: QASM for Different Circuit Types

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

# Simple single-qubit circuit
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.x(0)
print("Single qubit QASM:")
print(qc1.qasm())
print()

# Multi-qubit with barriers
qc2 = QuantumCircuit(3)
qc2.h(0)
qc2.barrier()
qc2.cx(0, 1)
qc2.cx(1, 2)
qc2.barrier()
qc2.measure_all()
print("Multi-qubit QASM:")
print(qc2.qasm())
print()

# Parameterized circuit
theta = Parameter('θ')
qc3 = QuantumCircuit(1)
qc3.ry(theta, 0)
qc3.measure_all()
print("Parameterized QASM:")
print(qc3.qasm())
```

### Example 5: QASM Interoperability

```python
from qiskit import QuantumCircuit

# Create circuit in Qiskit
qiskit_circuit = QuantumCircuit(2)
qiskit_circuit.h(0)
qiskit_circuit.cx(0, 1)
qiskit_circuit.measure_all()

# Export to QASM
qasm_code = qiskit_circuit.qasm()

# This QASM can now be used in:
# - Cirq (Google's framework)
# - Q# (Microsoft's quantum language)
# - PyQuil (Rigetti's framework)
# - Any QASM-compatible system

print("Shareable QASM code:")
print(qasm_code)

# Import back into Qiskit
reimported_circuit = QuantumCircuit.from_qasm_str(qasm_code)
print("\nReimported circuit:")
print(reimported_circuit.draw())
```

### Example 6: Verify Circuit Equivalence

```python
from qiskit import QuantumCircuit

# Original circuit
original_qc = QuantumCircuit(2)
original_qc.h(0)
original_qc.cx(0, 1)
original_qc.measure_all()

# Export and reimport
qasm_str = original_qc.qasm()
restored_qc = QuantumCircuit.from_qasm_str(qasm_str)

# Visual comparison
print("Original:")
print(original_qc.draw())
print("\nRestored from QASM:")
print(restored_qc.draw())

# Verify structure
print(f"\nOriginal depth: {original_qc.depth()}")
print(f"Restored depth: {restored_qc.depth()}")
print(f"Original size: {original_qc.size()}")
print(f"Restored size: {restored_qc.size()}")
```

---

## 🎯 Exam Focus Areas

### 1. Static Method Trap (HIGHEST PRIORITY)

**Question Pattern**: "How do you import a circuit from a QASM string?"

**CORRECT Answer**:
```python
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

**WRONG Answers** (Common Exam Mistakes):
```python
qc = qc.from_qasm_str(qasm_string)  # ✗ Instance method
qc.from_qasm_str(qasm_string)        # ✗ No assignment
qc = from_qasm_str(qasm_string)      # ✗ Not imported
```

**🎯 EXAM TIP**: The word "STATIC" should trigger alarm bells - call on the class!

### 2. Export Method

**Question Pattern**: "How do you export a circuit to OpenQASM format?"

**Answer**:
```python
qasm_string = qc.qasm()  # Returns string
```

**Key Points**:
- ✅ Returns a string (OpenQASM 2.0 by default)
- ✅ Instance method (called on circuit object)
- ✅ No parameters needed for basic usage

### 3. File Operations

**Question Pattern**: "How do you save/load circuits as QASM files?"

**Answer**:
```python
# Save
with open('circuit.qasm', 'w') as f:
    f.write(qc.qasm())

# Load (STATIC!)
qc = QuantumCircuit.from_qasm_file('circuit.qasm')
```

### 4. QASM Versions

**Question Pattern**: "What's the default QASM version in Qiskit?"

**Answer**: OpenQASM 2.0

**Key Differences**:
| Feature | QASM 2.0 | QASM 3.0 |
|---------|----------|----------|
| Status | Default in Qiskit | Experimental |
| Control flow | Limited | Full (if/else, loops) |
| Subroutines | No | Yes |
| Compatibility | Universal | Limited |

---

## 📊 Quick Reference

### Method Cheat Sheet

| Operation | Method | Type | Returns |
|-----------|--------|------|---------|
| Export to string | `qc.qasm()` | Instance | `str` |
| Import from string | `QuantumCircuit.from_qasm_str(s)` | **STATIC** | `QuantumCircuit` |
| Import from file | `QuantumCircuit.from_qasm_file(f)` | **STATIC** | `QuantumCircuit` |

### Common Patterns

```python
# Pattern 1: Export
qasm_code = circuit.qasm()

# Pattern 2: Import from string (STATIC!)
circuit = QuantumCircuit.from_qasm_str(qasm_code)

# Pattern 3: Import from file (STATIC!)
circuit = QuantumCircuit.from_qasm_file('file.qasm')

# Pattern 4: Save to file
with open('file.qasm', 'w') as f:
    f.write(circuit.qasm())
```

---

## 🧪 Practice Problems

### Problem 1: Export and Print

**Question**: Create a 2-qubit Bell state and export to QASM.

```python
from qiskit import QuantumCircuit

# TODO: Create Bell state and print QASM
```

<details>
<summary>Solution</summary>

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

qasm_string = qc.qasm()
print(qasm_string)
```
</details>

### Problem 2: Import from String

**Question**: Import this QASM code into Qiskit:

```qasm
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0],q[1];
```

<details>
<summary>Solution</summary>

```python
from qiskit import QuantumCircuit

qasm_str = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
h q[0];
cx q[0],q[1];
"""

# STATIC method!
qc = QuantumCircuit.from_qasm_str(qasm_str)
print(qc.draw())
```
</details>

### Problem 3: Round-Trip Test

**Question**: Create a circuit, export to QASM, reimport, and verify equivalence.

```python
from qiskit import QuantumCircuit

# TODO: Create → Export → Import → Verify
```

<details>
<summary>Solution</summary>

```python
from qiskit import QuantumCircuit

# Create
original = QuantumCircuit(3)
original.h(0)
original.cx(0, 1)
original.cx(1, 2)
original.measure_all()

# Export
qasm_str = original.qasm()

# Import (STATIC!)
restored = QuantumCircuit.from_qasm_str(qasm_str)

# Verify
print(f"Original depth: {original.depth()}")
print(f"Restored depth: {restored.depth()}")
print(f"Match: {original.depth() == restored.depth()}")
```
</details>

### Problem 4: Spot the Error

**Question**: What's wrong with this code?

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

qasm_str = qc.qasm()

# Import back
new_qc = qc.from_qasm_str(qasm_str)  # What's wrong here?
```

<details>
<summary>Solution</summary>

```python
# WRONG: from_qasm_str() called on instance
new_qc = qc.from_qasm_str(qasm_str)  # ✗

# CORRECT: from_qasm_str() is STATIC - call on class
new_qc = QuantumCircuit.from_qasm_str(qasm_str)  # ✓
```

**Explanation**: `from_qasm_str()` is a static method and must be called on the `QuantumCircuit` class, not on an instance (`qc`).
</details>

---

## ⚠️ Common Exam Mistakes

### Mistake 1: Instance vs Static
```python
# ✗ WRONG - calling static method on instance
qc = qc.from_qasm_str(qasm_string)

# ✓ CORRECT - calling static method on class
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

### Mistake 2: Forgetting to Assign
```python
# ✗ WRONG - no assignment
QuantumCircuit.from_qasm_str(qasm_string)

# ✓ CORRECT - assign to variable
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

### Mistake 3: Using Wrong Method Name
```python
# ✗ WRONG - no such method
qc = QuantumCircuit.from_qasm(qasm_string)

# ✓ CORRECT - full method name
qc = QuantumCircuit.from_qasm_str(qasm_string)
```

### Mistake 4: Calling qasm() without Assignment
```python
# ✗ WRONG - not saving the string
qc.qasm()

# ✓ CORRECT - save to variable
qasm_string = qc.qasm()
```

---

## 💡 Key Takeaways

1. **MEMORIZE**: `QuantumCircuit.from_qasm_str()` is **STATIC**
2. **Export**: `circuit.qasm()` returns OpenQASM 2.0 string
3. **Import**: Always call `from_qasm_str()` on **QuantumCircuit class**
4. **Files**: `from_qasm_file()` is also **STATIC**
5. **Default version**: Qiskit uses OpenQASM 2.0 by default
6. **Interoperability**: QASM enables circuit sharing between frameworks
7. **Human-readable**: QASM is text format for easy inspection

---

## 🔗 Related Sections

- **Section 3**: Circuit creation methods
- **Section 2**: Circuit visualization (vs QASM text format)
- **Section 4**: Transpilation (can export transpiled circuits to QASM)

---

## 📚 Additional Resources

- OpenQASM Specification: [https://github.com/openqasm/openqasm](https://github.com/openqasm/openqasm)
- IBM Quantum Docs: [https://docs.quantum.ibm.com/](https://docs.quantum.ibm.com/)
- Practice: Run `qasm_operations.py` examples

---

**Remember the Exam Trap**: 
```python
# ✗ qc.from_qasm_str(string)  - WRONG
# ✓ QuantumCircuit.from_qasm_str(string)  - CORRECT
```

🎯 **Exam Success Tip**: Write "STATIC METHOD" on your scratch paper before the exam starts!
