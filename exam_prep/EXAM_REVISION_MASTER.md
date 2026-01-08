# 🎯 Qiskit Certification Exam - Complete Revision Guide

> **Document Type**: Master Revision Notebook  
> **Last Updated**: December 2025  
> **Purpose**: Comprehensive review of ALL exam concepts (organized by source notebooks)

---

## 📚 Coverage Map

| Section | Topic | Weight | Sub-sections |
|---------|-------|--------|--------------|
| **Section 1** | Quantum Operations | 16% | single_qubit_gates, multi_qubit_gates, state_preparation |
| **Section 2** | Visualization | 11% | circuit_visualization, state_visualization, visualization_examples |
| **Section 3** | Create Circuits | **18%** | circuit_basics, parameterized_circuits, circuit_composition, circuit_library, classical_control, dynamic_circuits |
| **Section 4** | Run Circuits | 15% | transpilation, options_configuration, jobs_and_sessions, backend_target, runtime_service |
| **Section 5** | Sampler | 12% | sampler_primitive |
| **Section 6** | Estimator & VQE | 12% | estimator_primitive, vqe_pattern |
| **Section 7** | Results | 10% | result_extraction |
| **Section 8** | OpenQASM | 6% | openqasm_operations |
| **Section 9** | Quantum Information | 3% | clifford_circuits, operator_class, statevector_densitymatrix, fidelity, quantum_channels, randomized_benchmarking |

---

## 🧠 Document Structure

Each sub-section follows the same format:
1. **🧠 Conceptual Deep Dive** - Analogies and visual explanations
2. **✅ Key Takeaways** - Essential knowledge with code examples
3. **🚨 Critical Exam Facts** - Must-memorize bullet points
4. **📋 Exam Patterns** - Common question types with solutions

---

## ⚡ Critical Code Patterns (Quick Reference)

**Sampler Result:**
```python
counts = result[0].data.meas.get_counts()
```

**Estimator Result:**
```python
expectation = result[0].data.evs
```

**OpenQASM Import (STATIC!):**
```python
qc = QuantumCircuit.from_qasm_str(qasm_string)  # Not qc.from_qasm_str()!
```

**Properties vs Methods:**
```python
qc.num_qubits    # Property (no parentheses)
qc.depth()       # Method (needs parentheses)
```

---

# Section 1: Quantum Operations (16%)

---

## 1.1 Single-Qubit Gates
> Source: `section_1_quantum_operations/single_qubit_gates.ipynb`

### 🧠 Conceptual Deep Dive: The Spinning Coin Analogy

**Classical Bit**: A coin lying flat - either heads (0) or tails (1)

**Quantum Qubit**: A spinning coin in the air!
- While spinning, it's **both heads AND tails simultaneously** (superposition)
- The **axis of spin** determines the probabilities when you catch it
- **Measurement** = catching the coin → it becomes definitely heads or tails

**The Bloch Sphere**: Imagine the coin spinning in 3D space
```
           |0⟩ (North Pole)
            ↑
            |
    |+⟩ ←---+---→ |-⟩  (Equator: X-axis)
            |
            ↓
           |1⟩ (South Pole)

- Vertical axis (Z): |0⟩ at top, |1⟩ at bottom
- Horizontal plane: Superposition states like |+⟩, |-⟩
- Quantum gates = rotations of this spinning coin!
```

**Key Insight**: 
- |0⟩ and |1⟩ are just two special points on the sphere
- A qubit can point in ANY direction (infinite possibilities!)
- Gates rotate the state vector to different positions

### 🔬 Global vs Relative Phase

**Critical Exam Concept!**

**Global Phase** (Doesn't matter):
```
|ψ⟩ vs e^(iθ)|ψ⟩  →  Physically identical!
Example: |0⟩ and -|0⟩ are the same state
```

**Relative Phase** (Matters!):
```
|+⟩ = (|0⟩ + |1⟩)/√2  vs  |-⟩ = (|0⟩ - |1⟩)/√2
                              ↑
                    This minus sign matters!
```

**Why?** 
- Global phase: All components multiplied by same phase → no interference effect
- Relative phase: Different components have different phases → creates interference!

**Exam Trap**: Don't confuse Z|0⟩ = |0⟩ (unchanged) with Z|1⟩ = -|1⟩ (phase flip)

### 📐 Bloch Sphere Coordinates

Every qubit state can be written as:
```
|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩

Where:
- θ (theta): Angle from Z-axis (0° to 180°)
- φ (phi): Angle around Z-axis (0° to 360°)
```

**Key Points:**
- |0⟩: θ=0° (North Pole)
- |1⟩: θ=180° (South Pole)
- |+⟩: θ=90°, φ=0° (Positive X)
- |-⟩: θ=90°, φ=180° (Negative X)
- |+i⟩: θ=90°, φ=90° (Positive Y)
- |-i⟩: θ=90°, φ=270° (Negative Y)

### ✅ Key Takeaways

#### 1. Pauli Gates (X, Y, Z) - EXAM ESSENTIAL

**Mnemonic: "X-Men Flip, Z-Men Phase"**

```python
# X Gate - Bit flip (|0⟩ ↔ |1⟩)
qc.x(0)
# X|0⟩ = |1⟩, X|1⟩ = |0⟩
# Matrix: [[0,1],[1,0]]

# Y Gate - Bit + phase flip
qc.y(0)
# Y|0⟩ = i|1⟩, Y|1⟩ = -i|0⟩
# Y = iXZ

# Z Gate - Phase flip (adds -1 to |1⟩)
qc.z(0)
# Z|0⟩ = |0⟩ (unchanged!), Z|1⟩ = -|1⟩
# Matrix: [[1,0],[0,-1]]
```

**⚠️ EXAM TRAP**: Z gate doesn't change |0⟩!
- Z|0⟩ = |0⟩ (stays the same)
- Z|1⟩ = -|1⟩ (only adds minus sign)
- Z changes |+⟩ → |-⟩

#### 2. Hadamard Gate (H) - MOST IMPORTANT

**Mnemonic: "Hadamard Makes Plus"**

```python
qc.h(0)
# H|0⟩ = |+⟩ = (|0⟩ + |1⟩)/√2
# H|1⟩ = |-⟩ = (|0⟩ - |1⟩)/√2
# H² = I (self-inverse)
```

**Exam Pattern Recognition**:
```python
# This pattern appears in EVERY exam:
qc.h(0)        # Step 1: Create superposition
qc.cx(0, 1)    # Step 2: Create entanglement → Bell state!
```

#### 3. Phase Gates (S, T, P)

**Mnemonic: "Phase Powers: S-Squared, T-Forth"**

```python
qc.s(0)    # S = √Z (90° phase = π/2)
qc.t(0)    # T = √S = ⁴√Z (45° phase = π/4)
qc.p(λ, 0) # P(λ) - arbitrary phase
qc.sdg(0)  # S† (S-dagger) - inverse of S
qc.tdg(0)  # T† (T-dagger) - inverse of T
```

**Relationships:**
```
S² = Z
T² = S
T⁴ = Z
S = P(π/2)
T = P(π/4)
Z = P(π)
```

**⚠️ EXAM TRAP**: Phase gates don't change measurement probabilities!
- They only affect the phase, not the amplitudes
- P(|0⟩) and P(|1⟩) remain the same after S, T, or P gates

#### 4. Rotation Gates (RX, RY, RZ)

```python
qc.rx(θ, 0)  # Rotation around X-axis
qc.ry(θ, 0)  # Rotation around Y-axis (creates superpositions!)
qc.rz(θ, 0)  # Rotation around Z-axis (phase shift)
```

**⚠️ Special Cases - MEMORIZE These!**
```
RX(π) = X  (180° rotation around X = bit flip)
RY(π) = Y  (180° rotation around Y)
RZ(π) = Z  (180° rotation around Z = phase flip)

RX(2π) = -I  (Full rotation adds global phase -1)
RY(2π) = -I
RZ(2π) = -I
```

#### 5. Universal U Gate

```python
qc.u(θ, φ, λ, 0)  # Can represent ANY single-qubit gate
# Express common gates with U:
# H = U(π/2, 0, π)
# X = U(π, 0, π)
```

### 🚨 Critical Exam Facts

- ✅ X² = Y² = Z² = I (all Pauli gates are self-inverse)
- ✅ H² = I (Hadamard is self-inverse)
- ✅ S² = Z, T² = S, T⁴ = Z
- ✅ Z|0⟩ = |0⟩ (unchanged!), Z|1⟩ = -|1⟩
- ✅ RX(π) = X, RY(π) = Y, RZ(π) = Z (up to global phase)
- ✅ X = HZH (gate equivalence)
- ✅ Phase gates only affect |1⟩ component
- ✅ H|0⟩ = |+⟩ (positive X-axis), H|1⟩ = |-⟩ (negative X-axis)

### 🔄 Gate Commutativity - CRITICAL EXAM TOPIC!

**Definition:**
- **Commutative**: Order doesn't matter → AB = BA
- **Non-commutative**: Order matters → AB ≠ BA

**Decision Tree - Do Gates Commute?**
```
                    Two Gates (A and B)
                           |
                 ┌─────────┴─────────┐
                 │                   │
          Same Qubit?          Different Qubits?
                 │                   │
         ┌───────┴────────┐          │
         │                │          └──> ✓ Always Commute
    Same Gate?    Different Gates?
         │                │
    ✓ Commute      Check matrices...
    (X·X = I)
```

**Commutativity Table (Same Qubit) - MEMORIZE!**

| Gates | Commute? | Reason |
|-------|----------|--------|
| X, X | ✅ Yes | X² = I (self-inverse) |
| Z, Z | ✅ Yes | Z² = I |
| H, H | ✅ Yes | H² = I |
| Z, S | ✅ Yes | Both diagonal (phase gates) |
| S, T | ✅ Yes | Both diagonal (phase gates) |
| **X, Z** | ❌ **No** | **XZ = -ZX (anticommute!)** |
| **X, Y** | ❌ **No** | **XY = iZ** |
| **Y, Z** | ❌ **No** | **YZ = iX** |
| **H, S** | ❌ **No** | **HS ≠ SH** |
| **H, X** | ❌ **No** | **HXH = Z** |

**Rule of Thumb:**
- Same gate → Always commutes (XX = I, etc.)
- Different qubits → Always commutes
- Phase gates (Z, S, T, P) → Commute with each other
- Pauli X, Y, Z → **Anticommute** pairwise!

### 📋 Exam Patterns

**Pattern 1: "What state does H|0⟩ create?"**
```python
H|0⟩ = |+⟩ = (|0⟩ + |1⟩)/√2
```

**Pattern 2: "What does Z do to |+⟩?"**
```python
Z|+⟩ = Z(|0⟩+|1⟩)/√2 = (|0⟩-|1⟩)/√2 = |-⟩
```

**Pattern 3: "Gate equivalences?"**
```python
X = HZH
S = T²
Z = S² = T⁴
```

**Pattern 4: "Do X and Z commute?"**
```python
# NO! They ANTICOMMUTE
# XZ|0⟩ = X|0⟩ = |1⟩
# ZX|0⟩ = Z|1⟩ = -|1⟩
# They differ by minus sign: XZ = -ZX
```

**Pattern 5: "What is the result of H·X·H|0⟩?"**
```python
# HXH = Z (gate equivalence)
# So: HXH|0⟩ = Z|0⟩ = |0⟩
```

### 📊 Gate Comparison Table

| Gate | Matrix | On |0⟩ | On |1⟩ | Self-inverse? |
|------|--------|--------|--------|---------------|
| I | [[1,0],[0,1]] | |0⟩ | |1⟩ | ✓ |
| X | [[0,1],[1,0]] | |1⟩ | |0⟩ | ✓ |
| Y | [[0,-i],[i,0]] | i|1⟩ | -i|0⟩ | ✓ |
| Z | [[1,0],[0,-1]] | |0⟩ | -|1⟩ | ✓ |
| H | [[1,1],[1,-1]]/√2 | |+⟩ | |-⟩ | ✓ |
| S | [[1,0],[0,i]] | |0⟩ | i|1⟩ | ✗ (S²=Z) |
| T | [[1,0],[0,e^iπ/4]] | |0⟩ | e^iπ/4|1⟩ | ✗ (T⁴=Z) |

---

## 1.2 Multi-Qubit Gates
> Source: `section_1_quantum_operations/multi_qubit_gates.ipynb`

### 🧠 Conceptual Deep Dive

**Key Exam Mnemonic: "Control BEFORE Target"**

```python
qc.cx(control, target)
# Control is the FIRST parameter
# Target is the SECOND parameter
# qc.cx(0, 1): q0 controls, q1 is flipped
```

**⚠️ EXAM TRAP**: Direction matters!
```python
qc.cx(0, 1) ≠ qc.cx(1, 0)
|10⟩ →CX(0,1)→ |11⟩  BUT |10⟩ →CX(1,0)→ |10⟩ (no change!)
```

### ✅ Key Takeaways

#### 1. CNOT Gate (CX) - MOST IMPORTANT

**Controlled-NOT**: Flips target if control is |1⟩

```python
qc.cx(control, target)  # or qc.cnot(control, target)
```

**Truth Table:**
```
|00⟩ → |00⟩  (ctrl=0, no flip)
|01⟩ → |01⟩  (ctrl=0, no flip)
|10⟩ → |11⟩  (ctrl=1, FLIP!)
|11⟩ → |10⟩  (ctrl=1, FLIP!)
```

**Creating Entanglement:**
```python
qc.h(0)       # Superposition
qc.cx(0, 1)   # Entanglement
# Result: Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2
```

#### 2. CZ Gate (Controlled-Z)

Applies Z to target if control is |1⟩

**Key Property**: CZ is symmetric (control and target are interchangeable)

```python
qc.cz(0, 1)  # cz(0,1) = cz(1,0)!
```

**Truth Table:**
```
|00⟩ → |00⟩
|01⟩ → |01⟩
|10⟩ → |10⟩
|11⟩ → -|11⟩  (phase flip on |11⟩ only)
```

**CZ ≡ H-CNOT-H Sandwich:**
```python
# These are equivalent:
qc.cz(0, 1)
# Same as:
qc.h(1); qc.cx(0, 1); qc.h(1)
```

#### 3. SWAP Gate

Swaps two qubits: |01⟩ ↔ |10⟩

```python
qc.swap(0, 1)
# Can be decomposed as 3 CNOTs:
# qc.cx(0,1); qc.cx(1,0); qc.cx(0,1)
```

#### 4. Toffoli Gate (CCX)

**Controlled-Controlled-NOT**: Flips target if BOTH controls are |1⟩

```python
qc.ccx(control1, control2, target)
```

**Truth Table (Target flips only if both controls=1):**
```
|000⟩ → |000⟩
|001⟩ → |001⟩
|010⟩ → |010⟩
|011⟩ → |011⟩
|100⟩ → |100⟩
|101⟩ → |101⟩
|110⟩ → |111⟩  ← Target flipped!
|111⟩ → |110⟩  ← Target flipped!
```

**Classical**: Toffoli implements AND operation

### 🔔 Bell States - MEMORIZE ALL 4! ⚠️

**GUARANTEED EXAM QUESTIONS!**

| State | Expression | Circuit |
|-------|------------|---------|
| \|Φ+⟩ | (|00⟩ + |11⟩)/√2 | H(0) + CNOT(0,1) |
| \|Φ-⟩ | (|00⟩ - |11⟩)/√2 | H(0) + Z(0) + CNOT(0,1) |
| \|Ψ+⟩ | (|01⟩ + |10⟩)/√2 | H(0) + X(1) + CNOT(0,1) |
| \|Ψ-⟩ | (|01⟩ - |10⟩)/√2 | H(0) + Z(0) + X(1) + CNOT(0,1) |

**Recipe to Remember:**
- H + CNOT creates |Φ+⟩
- Add Z(0) for negative phase: Φ+ → Φ-
- Add X(1) to swap qubits: Φ → Ψ

**Step-by-Step: |Φ+⟩ Creation**
```
Step 1: |ψ₀⟩ = |00⟩
Step 2: After H(q0): |ψ₁⟩ = (|00⟩+|10⟩)/√2
Step 3: After CNOT(q0,q1): |ψ₂⟩ = (|00⟩+|11⟩)/√2 = |Φ+⟩
```

### 🌀 GHZ States - Multi-qubit Entanglement

**GHZ = Greenberger-Horne-Zeilinger state**

Pattern: H on first qubit + CNOT chain

```python
# 3-qubit GHZ: (|000⟩ + |111⟩)/√2
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)

# n-qubit GHZ pattern:
qc.h(0)
for i in range(1, n):
    qc.cx(0, i)
```

### ⚡ Phase Kickback - Advanced Concept

**Critical for Deutsch-Jozsa, Grover's Algorithm!**

When a controlled operation acts on a target in superposition, the phase "kicks back" to the control qubit!

```python
qc.h(0)        # Control in |+⟩
qc.x(1)        # Target to |1⟩
qc.h(1)        # Target in |-⟩
qc.cx(0, 1)    # Phase kickback happens here!
```

**Why it matters:**
- Enables quantum parallelism
- Used in Deutsch-Jozsa, Grover's algorithms
- Phase information transfers to control qubit

### 🚨 Critical Exam Facts

- ✅ `qc.cx(control, target)` - control is FIRST parameter
- ✅ CNOT is NOT symmetric: cx(0,1) ≠ cx(1,0)
- ✅ CZ IS symmetric: cz(0,1) = cz(1,0)
- ✅ SWAP = 3 CNOTs
- ✅ Toffoli flips target only if BOTH controls = 1
- ✅ H + CNOT creates Bell state (most common pattern!)
- ✅ CZ = H-CNOT-H sandwich
- ✅ Memorize all 4 Bell state circuits!

### 📋 Exam Patterns

**Pattern 1: "CNOT truth table?"**
```
|00⟩→|00⟩, |01⟩→|01⟩, |10⟩→|11⟩, |11⟩→|10⟩
```

**Pattern 2: "Create Bell state |Φ+⟩?"**
```python
qc.h(0)
qc.cx(0, 1)
```

**Pattern 3: "CZ equivalence?"**
```python
qc.cz(0,1) ≡ qc.h(1); qc.cx(0,1); qc.h(1)
```

**Pattern 4: "What's different between Bell states?"**
- Φ vs Ψ: Which qubits are correlated (same vs opposite)
- + vs -: Phase (positive vs negative)

### 📊 Multi-Qubit Gates Comparison

| Gate | Qubits | Description | Key Property |
|------|--------|-------------|--------------|
| CNOT | 2 | Controlled-NOT | Creates entanglement |
| CZ | 2 | Controlled-Z | Symmetric |
| SWAP | 2 | Exchange qubits | 3 CNOTs |
| CCX | 3 | Toffoli (2 controls) | Universal |

---

## 1.3 State Preparation
> Source: `section_1_quantum_operations/state_preparation.ipynb`

### 🧠 Conceptual Deep Dive

**Key Exam Mnemonics:**

**"Barriers Block, Reset Returns"**
- `barrier()` = Visual only, blocks optimization
- `reset()` = Active operation, returns to |0⟩

**Initialize vs Reset:**
- `initialize()`: Synthesis (adds many gates)
- `reset()`: Measurement-based (active reset)

### ✅ Key Takeaways

#### 1. Initialize() - Arbitrary State Preparation

**What it does**: Sets qubit to specific quantum state (arbitrary superposition)

**When to use:**
- Algorithm initialization (Grover, VQE, etc.)
- Preparing training data for quantum ML
- Setting up specific test states

**How it works:**
- Decomposes target state into sequence of gates
- Automatically normalizes if amplitudes don't sum to 1
- Can initialize single or multiple qubits

```python
# Initialize to |1⟩
qc.initialize([0, 1], 0)

# Initialize to |+⟩
qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0)

# Initialize 2-qubit Bell state
qc.initialize([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)], [0, 1])
```

**Exam Fact**: `initialize()` synthesizes a circuit - not a single gate!

#### 2. Barrier() - Circuit Alignment

**What it does**: Visual separator that prevents optimization across boundary

**When to use:**
- Organize circuits into logical sections
- Prevent transpiler from optimizing away gates
- Align operations across multiple qubits
- Debug: see clear circuit structure

**How it works:**
- Does NOT change quantum state
- Only affects transpilation/optimization
- Acts as "fence" for gate reordering

```python
qc.h(range(3))
qc.barrier()  # Visual separator
qc.cx(0, 1)
qc.cx(1, 2)
qc.barrier()
qc.h(range(3))
```

**Exam Fact**: `barrier()` is visual only - doesn't appear in final operations!

#### 3. Reset() - Reset to |0⟩

**What it does**: Returns qubit to |0⟩ state (measurement + conditional flip)

**When to use:**
- Qubit recycling in limited hardware
- Mid-circuit resets in error correction
- Clearing ancilla qubits for reuse
- Dynamic circuits

**How it works:**
1. Measures qubit
2. If result is |1⟩, applies X gate
3. Guarantees qubit is in |0⟩

```python
qc.reset(0)  # Forces qubit to |0⟩
```

**Exam Fact**: `reset()` uses measurement - different from `initialize([1,0], q)`!

#### 4. Delay() - Timing Control

For pulse-level timing control:

```python
qc.delay(100, 0, unit='ns')   # nanoseconds
qc.delay(1, 0, unit='us')     # microseconds
qc.delay(1, 0, unit='ms')     # milliseconds
```

### ⚠️ EXAM TRAP: Initialize vs Reset

| Feature | initialize() | reset() |
|---------|-------------|---------|
| Method | Gate synthesis | Measurement-based |
| Speed | Slower (many gates) | Faster (measure + flip) |
| Use case | Arbitrary states | Return to |0⟩ only |
| Circuit depth | Deep | Shallow |

### 📌 Common State Preparation Patterns

**Pattern 1: Single-Qubit Superposition**
```python
# Create |+⟩ = (|0⟩+|1⟩)/√2
qc.h(0)

# Alternative with initialize
qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0)
```

**Pattern 2: Multi-Qubit Superposition**
```python
# Create all 2^n states equally
for i in range(n):
    qc.h(i)
# Result: (|00...0⟩ + |00...1⟩ + ... + |11...1⟩) / √(2^n)
```

**Pattern 3: Specific Multi-Qubit State**
```python
# Create |Ψ⟩ = α|00⟩ + β|01⟩ + γ|10⟩ + δ|11⟩
amplitudes = [α, β, γ, δ]
qc.initialize(amplitudes, [0, 1])
```

**Exam Fact**: Applying H to n qubits creates superposition of ALL 2^n states!

### 🔄 Gate Equivalences for State Preparation

**These relationships appear in exam questions!**

```
X = RX(π)              (180° rotation = bit flip)
H|0⟩ = RY(π/2)|0⟩     (Hadamard ≈ Y-rotation by 90°)
initialize([1,0]) ≈ reset()  (Both give |0⟩, different methods)
```

**Exam Pattern**: "Which operation prepares state |+⟩?"
- Answer: H|0⟩ (most common)
- Alternative: RY(π/2)|0⟩
- Alternative: initialize([1/√2, 1/√2], 0)

### 🚨 Critical Exam Facts

- ✅ `initialize()` uses gate synthesis (many gates)
- ✅ `reset()` uses measurement (faster for |0⟩)
- ✅ `barrier()` has NO quantum effect - visual only
- ✅ `barrier()` prevents optimization across it
- ✅ H⊗n creates superposition of ALL 2^n states
- ✅ `delay()` for pulse-level timing control

### 📋 Exam Patterns

**Pattern 1: "What does barrier() do?"**
```python
# Prevents transpiler optimization across barrier
# NO quantum effect - purely organizational
```

**Pattern 2: "Fastest way to return to |0⟩?"**
```python
qc.reset(0)  # NOT initialize([1,0], 0)
```

**Pattern 3: "Create uniform superposition?"**
```python
for i in range(n):
    qc.h(i)
# Creates (|00...0⟩ + |00...1⟩ + ... + |11...1⟩)/√(2^n)
```

### 🎓 Section 1 Complete Checklist

Before moving on, make sure you can:
- [ ] Explain all Pauli gates (X, Y, Z) and their effects
- [ ] Use Hadamard to create superposition
- [ ] Know phase gate relationships (S² = Z, T² = S)
- [ ] Create all 4 Bell states from memory
- [ ] Understand CNOT direction (control, target)
- [ ] Know CZ is symmetric, CNOT is not
- [ ] Explain difference between initialize() and reset()
- [ ] Know barrier() has no quantum effect

---

# Section 2: Visualization (11%)

---

## 2.1 Circuit Visualization
> Source: `section_2_visualization/circuit_visualization.ipynb`

### 🧠 Conceptual Deep Dive

**The Musical Score Analogy:**
- **Time**: Flows left to right (like reading music)
- **Staff Lines**: Each line = a qubit (like an instrument)
- **Notes**: Gates are notes played on instruments
- **Chords**: Multi-qubit gates = chords across instruments

**Exam Mnemonic: "Text Makes LaTeX"**
Remember the 4 output formats: **T**ext, **M**pl, **L**atex, **L**atex_source

**Reading Order TRAP:**
- Default: q_0 at TOP (first line)
- With `reverse_bits=True`: q_n-1 (MSB) at TOP
- Math convention vs Qiskit convention!

### ✅ Key Takeaways

#### Four Output Formats (MEMORIZE ALL!)

```python
# 1. TEXT - ASCII art (DEFAULT)
print(qc.draw())              # or qc.draw(output='text')
# Output: ASCII characters, works everywhere

# 2. MPL - Matplotlib figure
qc.draw(output='mpl')
# Output: Rich graphical display, requires matplotlib

# 3. LATEX - Rendered PDF
qc.draw(output='latex')
# Output: Publication-quality PDF, requires LaTeX installed

# 4. LATEX_SOURCE - Raw LaTeX code
qc.draw(output='latex_source')
# Output: String of LaTeX code you can paste into documents
```

**⚠️ EXAM TRAP**: `output` parameter MUST be a STRING!
```python
qc.draw(output=mpl)    # ❌ WRONG - NameError
qc.draw(output='mpl')  # ✅ CORRECT
```

#### All Drawing Options

```python
qc.draw(
    output='mpl',           # Output format (text, mpl, latex, latex_source)
    reverse_bits=True,      # MSB on top (math convention)
    fold=20,                # Wrap circuit after N columns
    idle_wires=False,       # Hide unused qubits
    scale=1.5,              # Scale factor (mpl only)
    filename='circuit.png', # Save to file
    style={'name': 'iqp'}   # Visual style (mpl only)
)
```

#### reverse_bits Behavior

```python
# 3-qubit circuit example
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# Default (reverse_bits=False): q_0 on TOP
#      ┌───┐          
# q_0: ┤ H ├──■───────
#      └───┘┌─┴─┐     
# q_1: ─────┤ X ├──■──
#           └───┘┌─┴─┐
# q_2: ──────────┤ X ├
#                └───┘

# With reverse_bits=True: q_2 (MSB) on TOP
# q_2: ──────────┤ X ├
#           └───┘┌─┴─┐
# q_1: ─────┤ X ├──■──
#      └───┘┌─┴─┐     
# q_0: ┤ H ├──■───────
#      ┌───┘          
```

**Exam Pattern**: "Which qubit is at the top?"
- Default: q_0 (LSB) at top
- `reverse_bits=True`: q_n-1 (MSB) at top

#### Style Options (mpl only)

```python
# Built-in styles
qc.draw(output='mpl', style={'name': 'iqp'})
qc.draw(output='mpl', style={'name': 'bw'})      # Black and white
qc.draw(output='mpl', style={'name': 'clifford'})

# Custom colors
style = {
    'backgroundcolor': '#EEEEEE',
    'linecolor': '#000000',
    'displaycolor': {'cx': '#888888'},
}
qc.draw(output='mpl', style=style)
```

### 📊 Understanding Counts

**EXAM TRAP**: Qiskit bit ordering in measurement strings!

```python
qc = QuantumCircuit(3, 3)
qc.x(2)  # Flip qubit 2
qc.measure([0, 1, 2], [0, 1, 2])

# Result: '100'
# String is READ RIGHT TO LEFT: c[2]c[1]c[0]
# c[0] = '0' (rightmost) ← from q[0]
# c[1] = '0' (middle)    ← from q[1]
# c[2] = '1' (leftmost)  ← from q[2]
```

**Golden Rule**: `result_string[i] = measurement of c[n-1-i]`
- Rightmost character = c[0] = measurement of q[0]
- Leftmost character = c[n-1] = measurement of q[n-1]

### 📋 Circuit Drawing Quick Reference

| Format | Use Case | Requires |
|--------|----------|----------|
| `'text'` | Quick inspection, notebooks | Nothing |
| `'mpl'` | Presentations, documentation | matplotlib |
| `'latex'` | Publications | LaTeX system |
| `'latex_source'` | Manual LaTeX editing | Nothing |

### 🚨 Critical Exam Facts

- ✅ `output` must be a STRING: `'mpl'` not `mpl`
- ✅ Default output is `'text'` (ASCII)
- ✅ `reverse_bits=True` puts MSB (q_n-1) on top
- ✅ Default is `reverse_bits=False` (q_0 on top)
- ✅ `idle_wires=False` hides qubits with no gates
- ✅ Result strings read RIGHT to LEFT
- ✅ `scale` option only works with `mpl` output

### 📋 Exam Patterns

**Pattern 1: "What's wrong with this code?"**
```python
qc.draw(output=mpl)  # ❌ Missing quotes!
qc.draw(output='mpl')  # ✅ Correct
```

**Pattern 2: "Draw for publication?"**
```python
qc.draw(output='latex')  # Or output='mpl'
```

**Pattern 3: "Hide unused qubits?"**
```python
qc.draw(idle_wires=False)
```

**Pattern 4: "Get LaTeX code to paste?"**
```python
latex_code = qc.draw(output='latex_source')
```

---

## 2.2 State Visualization
> Source: `section_2_visualization/state_visualization.ipynb`

### 🧠 Conceptual Deep Dive

**Two Ways to Get States - CRITICAL DIFFERENCE!**

| Method | Requirements | Returns |
|--------|--------------|---------|
| `Statevector` | NO measurements | Full quantum state |
| `StatevectorSampler` | MUST have measurements | Counts dictionary |

**Exam Mnemonic: "Vector = Values, Sampler = Samples"**
- Statevector gives you exact probability **values**
- StatevectorSampler gives you measurement **samples**

### ✅ Key Takeaways

#### Method 1: Statevector (Direct State Access)

```python
from qiskit.quantum_info import Statevector

# Create circuit WITHOUT measurements
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO qc.measure()!

# Get exact quantum state
sv = Statevector.from_instruction(qc)
print(sv)  # Shows all amplitudes
```

**When to Use Statevector:**
- Debugging/learning
- Exact amplitude analysis
- State visualization functions
- Small circuits (scales exponentially!)

#### Method 2: StatevectorSampler (Sampling)

```python
from qiskit.primitives import StatevectorSampler

# Create circuit WITH measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # REQUIRED!

# Get measurement samples
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.meas.get_counts()
```

**When to Use StatevectorSampler:**
- Simulating real hardware behavior
- Getting probability distributions
- Histogram visualization
- Testing algorithms

### 📊 Visualization Compatibility Matrix

**MEMORIZE THIS TABLE!**

| Input Type | plot_histogram | plot_bloch_multivector | plot_state_city | plot_state_qsphere | plot_state_hinton | plot_state_paulivec |
|------------|----------------|------------------------|-----------------|-------------------|-------------------|---------------------|
| `Statevector` | ❌ Use `.probabilities_dict()` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `counts` dict | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| `result[0].data.meas` | Use `.get_counts()` | ❌ | ❌ | ❌ | ❌ | ❌ |

**Key Rule**: 
- **State visualizations** (bloch, city, qsphere, hinton, paulivec) need `Statevector`
- **Histogram** needs `counts` dictionary

### 🎨 State Visualization Functions

#### 1. plot_bloch_multivector - Individual Qubit States

```python
from qiskit.visualization import plot_bloch_multivector

sv = Statevector.from_instruction(qc)
plot_bloch_multivector(sv)
```

**What it shows:**
- One Bloch sphere per qubit
- Shows individual qubit state in 3D
- |0⟩ at north pole, |1⟩ at south pole
- |+⟩ on +X axis, |-⟩ on -X axis

**⚠️ EXAM TRAP**: Entangled qubits show as MIXED states (inside the sphere)!
```python
# Bell state |Φ+⟩
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
sv = Statevector.from_instruction(qc)
plot_bloch_multivector(sv)
# Each qubit appears at CENTER of sphere!
# Because individual qubits in entangled state are mixed
```

#### 2. plot_state_city - 3D Bar Chart of Density Matrix

```python
from qiskit.visualization import plot_state_city

sv = Statevector.from_instruction(qc)
plot_state_city(sv)
```

**What it shows:**
- Real and imaginary parts of density matrix
- 3D bar chart where height = magnitude
- Good for seeing coherences (off-diagonal elements)

**When to use:**
- Analyzing multi-qubit states
- Visualizing density matrices
- Seeing interference patterns

#### 3. plot_state_qsphere - Global State Visualization

```python
from qiskit.visualization import plot_state_qsphere

sv = Statevector.from_instruction(qc)
plot_state_qsphere(sv)
```

**What it shows:**
- All basis states on one sphere
- Size of blob = probability amplitude
- Color = phase
- North pole = |00...0⟩, South pole = |11...1⟩

**Best for:**
- Seeing phase relationships
- Understanding superposition
- Visualizing multi-qubit states compactly

#### 4. plot_state_hinton - 2D Grid of Density Matrix

```python
from qiskit.visualization import plot_state_hinton

sv = Statevector.from_instruction(qc)
plot_state_hinton(sv)
```

**What it shows:**
- 2D grid representation
- Square size = magnitude
- Color = sign (positive/negative)
- Simpler than city plot for large states

#### 5. plot_state_paulivec - Pauli Expectation Values

```python
from qiskit.visualization import plot_state_paulivec

sv = Statevector.from_instruction(qc)
plot_state_paulivec(sv)
```

**What it shows:**
- Expectation values of all Pauli operators
- Bar chart format
- Shows II, IX, IY, IZ, XI, XX, etc.

#### 6. plot_histogram - Measurement Results

```python
from qiskit.visualization import plot_histogram

# From counts dictionary
plot_histogram(counts)

# From Statevector (convert first!)
sv = Statevector.from_instruction(qc)
probs = sv.probabilities_dict()
plot_histogram(probs)
```

**⚠️ EXAM TRAP**: `plot_histogram` needs a dictionary, not a result object!
```python
# ❌ WRONG
plot_histogram(result)
plot_histogram(result[0].data.meas)

# ✅ CORRECT
counts = result[0].data.meas.get_counts()
plot_histogram(counts)
```

#### 7. plot_distribution - Alternative Histogram

```python
from qiskit.visualization import plot_distribution

# Works with quasi-probabilities and counts
plot_distribution(counts)
```

### 📊 Decision Flowchart: Which Visualization?

```
Question: What do you want to see?
├── Individual qubit states → plot_bloch_multivector
├── Phase relationships → plot_state_qsphere
├── Density matrix details → plot_state_city or plot_state_hinton
├── Pauli decomposition → plot_state_paulivec
└── Measurement probabilities → plot_histogram
```

```
Question: What data do you have?
├── Statevector object
│   ├── Direct visualization → plot_bloch_multivector, city, qsphere, hinton, paulivec
│   └── Histogram → .probabilities_dict() then plot_histogram
└── Counts dictionary
    └── plot_histogram or plot_distribution
```

### 🔍 Verifying States with Visualization

**Bell State |Φ+⟩ Verification:**
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
sv = Statevector.from_instruction(qc)

# Method 1: Check amplitudes
print(sv)  # Should show [0.707, 0, 0, 0.707]

# Method 2: Probabilities
print(sv.probabilities_dict())  # {'00': 0.5, '11': 0.5}

# Method 3: Bloch spheres
plot_bloch_multivector(sv)  # Both qubits at center (mixed)

# Method 4: QSphere
plot_state_qsphere(sv)  # Blobs at |00⟩ and |11⟩
```

**GHZ State Verification:**
```python
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
sv = Statevector.from_instruction(qc)

print(sv.probabilities_dict())  # {'000': 0.5, '111': 0.5}
plot_state_qsphere(sv)  # Blobs at |000⟩ and |111⟩
```

### 🚨 Critical Exam Facts

- ✅ `Statevector` requires NO measurements in circuit
- ✅ `StatevectorSampler` REQUIRES measurements
- ✅ State visualization functions need `Statevector`, not counts
- ✅ `plot_histogram` needs dictionary, use `.get_counts()`
- ✅ Entangled qubits show as mixed states on Bloch sphere
- ✅ QSphere shows global state with phase as color
- ✅ City plot shows density matrix in 3D

### 📋 Exam Patterns

**Pattern 1: "Visualize Bell state phases?"**
```python
sv = Statevector.from_instruction(qc)
plot_state_qsphere(sv)  # Color shows phase
```

**Pattern 2: "Why are Bloch spheres at center?"**
```python
# Entangled state! Individual qubits are mixed states
# Use qsphere or city for full picture
```

**Pattern 3: "Get histogram from Statevector?"**
```python
sv = Statevector.from_instruction(qc)
probs = sv.probabilities_dict()
plot_histogram(probs)
```

**Pattern 4: "What's wrong with this code?"**
```python
# ❌ WRONG
qc.measure_all()
sv = Statevector.from_instruction(qc)  # Fails with measurements!

# ✅ CORRECT - remove measurements or use separate circuit
```

---

## 2.3 Visualization Examples
> Source: `section_2_visualization/visualization_examples.ipynb`

### 🧠 Conceptual Deep Dive

**Superposition vs Entanglement - EXAM DISTINCTION!**

| Property | Superposition | Entanglement |
|----------|---------------|--------------|
| Qubits | Single or multiple | Multiple required |
| Independence | Qubits independent | Qubits correlated |
| Bloch sphere | On surface | At center (mixed) |
| Separable | Yes | No |

**Visual Signatures:**
- **Superposition**: Bloch vector ON the sphere surface
- **Entanglement**: Bloch vector INSIDE sphere (mixed state)

### ✅ Complete Visualization Workflow

#### Example 1: Superposition State

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere

# Create superposition
qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
# State: (|00⟩ + |01⟩ + |10⟩ + |11⟩)/2

# Visualize
sv = Statevector.from_instruction(qc)

# Bloch: Both qubits ON surface (pure states)
plot_bloch_multivector(sv)

# QSphere: Equal blobs at all 4 basis states
plot_state_qsphere(sv)

# Probabilities
print(sv.probabilities_dict())
# {'00': 0.25, '01': 0.25, '10': 0.25, '11': 0.25}
```

#### Example 2: Entangled State

```python
# Create Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# State: (|00⟩ + |11⟩)/√2

sv = Statevector.from_instruction(qc)

# Bloch: Both qubits AT CENTER (mixed states!)
plot_bloch_multivector(sv)

# QSphere: Blobs only at |00⟩ and |11⟩
plot_state_qsphere(sv)

# Probabilities
print(sv.probabilities_dict())
# {'00': 0.5, '11': 0.5}
```

### 📊 Side-by-Side Comparison

**2 Qubits with H on each (Superposition):**
```
- Circuit: H(0), H(1)
- State: |++⟩ = (|00⟩+|01⟩+|10⟩+|11⟩)/2
- Bloch: Both qubits at |+⟩ position (on +X axis)
- QSphere: 4 equal blobs
- Separable: YES (can write as |+⟩⊗|+⟩)
```

**Bell State (Entanglement):**
```
- Circuit: H(0), CX(0,1)
- State: |Φ+⟩ = (|00⟩+|11⟩)/√2
- Bloch: Both qubits at center (mixed)
- QSphere: 2 blobs at |00⟩ and |11⟩
- Separable: NO (cannot factor)
```

### 🔄 Full Workflow: Circuit → Counts → Histogram

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Step 1: Create circuit WITH measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Step 2: Run with sampler
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()

# Step 3: Extract counts properly!
counts = result[0].data.meas.get_counts()
print(counts)  # {'00': ~500, '11': ~500}

# Step 4: Visualize
plot_histogram(counts)
```

### 📋 Exam Practice Questions

**Q1: "What visualization shows phase information?"**
- Answer: `plot_state_qsphere` (color = phase)

**Q2: "Why does plot_bloch_multivector show center for Bell state?"**
- Answer: Individual qubits in entangled state are mixed states

**Q3: "How to visualize exact quantum state?"**
- Answer: Use `Statevector.from_instruction(qc)` without measurements

**Q4: "What's the difference between superposition and entanglement on Bloch sphere?"**
- Superposition: Vector on surface (pure state)
- Entanglement: Vector at center (mixed state)

**Q5: "Which takes a Statevector? Which takes counts?"**
- Statevector: bloch_multivector, state_city, state_qsphere, state_hinton, state_paulivec
- Counts: plot_histogram, plot_distribution

### 🚨 Critical Exam Facts Summary

**Circuit Drawing:**
- ✅ `output` must be string: `'mpl'` not `mpl`
- ✅ 4 formats: text, mpl, latex, latex_source
- ✅ `reverse_bits=True` puts MSB on top
- ✅ Result strings read RIGHT to LEFT

**State Visualization:**
- ✅ `Statevector` = NO measurements required
- ✅ `StatevectorSampler` = measurements REQUIRED
- ✅ Entangled states show as mixed on Bloch sphere
- ✅ `plot_histogram` needs `.get_counts()` dictionary

**Workflow:**
- ✅ State analysis: `Statevector.from_instruction(qc)`
- ✅ Sampling: `StatevectorSampler` with measurements
- ✅ Phase info: `plot_state_qsphere`
- ✅ Individual qubits: `plot_bloch_multivector`

### 🎓 Section 2 Complete Checklist

Before moving on, make sure you can:
- [ ] Draw circuits with all 4 output formats
- [ ] Explain reverse_bits behavior
- [ ] Know when to use Statevector vs StatevectorSampler
- [ ] Choose the right visualization for your data
- [ ] Convert between Statevector and probabilities
- [ ] Understand why entanglement shows as mixed state
- [ ] Extract counts from sampler result correctly

---

# Section 3: Create Circuits (18% - HIGHEST WEIGHT!)

---

## 3.1 Circuit Basics
> Source: `section_3_create_circuits/circuit_basics.ipynb`

### 🧠 Conceptual Deep Dive

**Circuit = Blueprint:**
- Quantum circuit is a blueprint for computation
- Specifies what gates to apply and in what order
- Properties tell you about the blueprint's complexity

**Exam Mnemonic: "Width = Wires, Depth = Delays, Size = Sum"**
- **Width**: Total number of wires (qubits + classical bits)
- **Depth**: Longest sequential path (critical path)
- **Size**: Total number of operations

### ✅ Key Takeaways

#### Circuit Creation Methods

**Method 1: Simple Creation (Most Common - 90% of time)**
```python
# Just qubits (no classical bits needed yet)
qc1 = QuantumCircuit(2)

# Qubits + classical bits (for measurement)
qc2 = QuantumCircuit(2, 2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0, 1], [0, 1])

# Syntax: QuantumCircuit(n_qubits, n_classical_bits)
```

**Method 2: Using Named Registers**
```python
# Create named registers
qr = QuantumRegister(3, 'q')   # 3 qubits named 'q'
cr = ClassicalRegister(3, 'c')  # 3 classical bits named 'c'

qc = QuantumCircuit(qr, cr)
qc.h(qr[0])
qc.cx(qr[0], qr[1])
qc.measure(qr, cr)
```

**Method 3: Multiple Registers (Advanced)**
```python
# Separate logical units
data_qubits = QuantumRegister(4, 'data')
ancilla_qubits = QuantumRegister(2, 'ancilla')
measurements = ClassicalRegister(4, 'meas')
syndrome = ClassicalRegister(2, 'syndrome')

qc = QuantumCircuit(data_qubits, ancilla_qubits, measurements, syndrome)
```

### 📏 Circuit Properties (EXAM CRITICAL!)

**The Big Three: Depth, Size, Width - TESTED IN EVERY EXAM!**

```python
# GHZ state circuit example
qc = QuantumCircuit(3, 3)
qc.h(0)              # Layer 1
qc.cx(0, 1)          # Layer 2
qc.cx(1, 2)          # Layer 3
qc.measure([0,1,2], [0,1,2])  # Layer 4

# Properties:
qc.depth()      # 4 - Critical path length (longest sequential chain)
qc.size()       # 6 - Total gate count (1 H + 2 CX + 3 Measure)
qc.width()      # 6 - Total wires (3 qubits + 3 classical)
qc.num_qubits   # 3 - Number of quantum wires (PROPERTY!)
qc.num_clbits   # 3 - Number of classical wires (PROPERTY!)
qc.count_ops()  # {'h': 1, 'cx': 2, 'measure': 3} - Dictionary
```

### ⚠️ EXAM TRAP #1: Property vs Method

**This is tested CONSTANTLY on the exam!**

```python
# ❌ WRONG - These are PROPERTIES (no parentheses!)
qc.num_qubits()   # ERROR!
qc.num_clbits()   # ERROR!

# ✅ CORRECT - Properties
qc.num_qubits     # No ()
qc.num_clbits     # No ()

# ✅ CORRECT - Methods (with parentheses)
qc.depth()        # With ()
qc.size()         # With ()
qc.width()        # With ()
qc.count_ops()    # With ()
```

**Memory aid**: "Numbers are properties, calculations are methods!"

### 📊 Understanding Depth vs Size

**Parallel Operations Don't Add Depth!**

```python
# Example 1: Parallel operations - Depth = 1
qc_parallel = QuantumCircuit(3)
qc_parallel.h(0)  # Layer 1
qc_parallel.h(1)  # Layer 1 (parallel!)
qc_parallel.h(2)  # Layer 1 (parallel!)
# Depth: 1, Size: 3 (all gates in same layer)

# Example 2: Sequential operations - Depth = 3
qc_sequential = QuantumCircuit(1)
qc_sequential.h(0)  # Layer 1
qc_sequential.x(0)  # Layer 2
qc_sequential.z(0)  # Layer 3
# Depth: 3, Size: 3 (each gate in different layer)

# Example 3: Mixed (common exam question!)
qc_mixed = QuantumCircuit(3)
qc_mixed.h(0)       # Layer 1
qc_mixed.h(1)       # Layer 1 (parallel with above)
qc_mixed.cx(0, 2)   # Layer 2 (depends on q0)
qc_mixed.x(1)       # Layer 2 (parallel with CX, different qubits)
# Depth: 2, Size: 4
```

**Algorithm for calculating depth manually:**
1. Go through gates in order
2. Track which qubits are "busy" in each layer
3. If gate uses a qubit that's busy → new layer
4. If all qubits are free → same layer
5. Count total layers

### 🚨 Critical Exam Facts

- ✅ `num_qubits` and `num_clbits` are **PROPERTIES** (no parentheses)
- ✅ `depth()`, `size()`, `width()`, `count_ops()` are **METHODS** (with parentheses)
- ✅ Depth = longest path, NOT total gates
- ✅ Width = qubits + classical bits
- ✅ Parallel gates don't increase depth!
- ✅ `QuantumCircuit(n, m)` creates n qubits and m classical bits

### 📋 Exam Patterns

**Pattern 1: "What's the depth of this circuit with parallel gates?"**
→ Count layers, not gates!

**Pattern 2: "Is `num_qubits` a property or method?"**
→ Property (no parentheses)

**Pattern 3: "What's the width of QuantumCircuit(3, 2)?"**
→ 3 + 2 = 5

---

## 3.2 Circuit Composition
> Source: `section_3_create_circuits/circuit_composition.ipynb`

### 🧠 Conceptual Deep Dive

**compose() vs tensor() - MOST TESTED SECTION 3 QUESTION!**

| Method | Dimension | Result |
|--------|-----------|--------|
| `compose()` | Time (sequential) | Same qubits, gates run one after another |
| `tensor()` | Space (parallel) | Different qubits, creates larger system |

### ✅ Key Takeaways

#### compose() - Sequential Composition

```python
# Basic compose - sequential execution
qc1 = QuantumCircuit(2)
qc1.h([0, 1])

qc2 = QuantumCircuit(2)
qc2.cx(0, 1)

# Compose: qc1 THEN qc2
full_circuit = qc1.compose(qc2)
# Gates from qc1, followed by gates from qc2
```

**compose() with qubit mapping:**
```python
# Apply small circuit to specific qubits in large circuit
qc_large = QuantumCircuit(4)
qc_large.h(range(4))

qc_small = QuantumCircuit(2)
qc_small.cx(0, 1)

# Apply small circuit to qubits 1 and 2 of large circuit
result = qc_large.compose(qc_small, qubits=[1, 2])
```

#### tensor() - Parallel Composition

```python
# tensor - parallel systems
system1 = QuantumCircuit(2)
system1.h(0)
system1.cx(0, 1)

system2 = QuantumCircuit(2)
system2.x([0, 1])

# Tensor product: side-by-side
combined = system1.tensor(system2)
# Total qubits: 4 (2 + 2)
# Systems operate independently
```

### 📊 Visual Comparison

```python
# compose() - Same qubits, deeper circuit
# 2 qubits, gates run sequentially

# tensor() - More qubits, parallel execution
# 4 qubits, gates run simultaneously
```

**Key Difference:**
- compose: 2 qubits, deeper circuit (sequential)
- tensor: 4 qubits, shallower circuit (parallel)

#### append() - Adding Gates and Circuits

```python
# Append gates to circuit
qc = QuantumCircuit(3)
qc.h([0, 1, 2])

# Append QFT as a single gate block
from qiskit.circuit.library import QFTGate
qc.append(QFTGate(3), [0, 1, 2])
# QFT appears as single block (not decomposed)

# Append custom operation
bell_gate = QuantumCircuit(2, name='Bell')
bell_gate.h(0)
bell_gate.cx(0, 1)
qc.append(bell_gate.to_gate(), [0, 1])
```

#### inverse() - Reverse and Adjoint

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.t(0)

# Get inverse
qc_inv = qc.inverse()
# Gates reversed AND inverted (T† instead of T)

# Verify: original + inverse = identity
qc_full = qc.compose(qc.inverse())
# Returns to |00⟩
```

#### power() - Repeat Circuit

```python
qc = QuantumCircuit(1)
qc.s(0)  # S gate (√Z)

# S² = Z
qc_squared = qc.power(2)
```

#### decompose() - Expand to Basic Gates

```python
qc = QuantumCircuit(3)
qc.append(QFTGate(3), range(3))

# Decompose to basic gates
qc_decomposed = qc.decompose()
# QFT expanded into H, CRZ, SWAP gates
```

### 🚨 Critical Exam Facts

- ✅ **compose()** = sequential, **tensor()** = parallel (MOST TESTED!)
- ✅ compose() keeps qubit count, tensor() adds qubits
- ✅ inverse() reverses order AND takes adjoint
- ✅ decompose() expands composite gates
- ✅ append() adds single gates, compose() adds full circuits

### 📋 Exam Patterns

**Pattern 1: "Two 2-qubit circuits. Which creates 4-qubit circuit?"**
→ tensor() (parallel = more qubits)

**Pattern 2: "What does inverse() do to H, then T?"**
→ Returns T†, then H (reverse order + adjoint)

---

## 3.3 Parameterized Circuits
> Source: `section_3_create_circuits/parameterized_circuits.ipynb`

### 🧠 Conceptual Deep Dive

**Parameters = Symbolic Placeholders**
- Create circuit templates
- Bind values later (at execution time)
- Essential for VQE, QAOA, ML

**Exam Mnemonic: "Parameters are Placeholders - Assign to Execute!"**

### ✅ Key Takeaways

#### Single Parameter

```python
from qiskit.circuit import Parameter

# Create parameter
theta = Parameter('θ')

# Use in circuit
qc = QuantumCircuit(1)
qc.ry(theta, 0)

# Circuit is symbolic (not executable yet!)
print(qc.parameters)  # {θ}
```

#### assign_parameters() - MOST TESTED METHOD!

```python
# Bind parameter to value
bound_circuit = qc.assign_parameters({theta: np.pi/4})
# No parameters left - circuit is executable!

# Bind to multiple values (VQE pattern!)
angles = [0, np.pi/4, np.pi/2, np.pi]
for angle in angles:
    bound = qc.assign_parameters({theta: angle})
```

### ⚠️ EXAM TRAP: assign_parameters() Returns NEW Circuit!

```python
# ❌ WRONG - Original circuit unchanged
qc.assign_parameters({theta: 0.5})
# qc still has parameter!

# ✅ CORRECT - Capture returned circuit
bound_qc = qc.assign_parameters({theta: 0.5})
# bound_qc has no parameters
```

#### ParameterVector - Multiple Parameters

```python
from qiskit.circuit import ParameterVector

# Create parameter vector
params = ParameterVector('θ', 3)
# Creates: θ[0], θ[1], θ[2]

# Use in circuit
qc = QuantumCircuit(3)
for i in range(3):
    qc.ry(params[i], i)

# Bind vector with list
values = [np.pi/2, np.pi/3, np.pi/4]
bound_qc = qc.assign_parameters({params: values})
```

#### VQE Ansatz Pattern (GUARANTEED EXAM QUESTION!)

```python
def create_vqe_ansatz(n_qubits, depth):
    """
    Hardware-efficient ansatz for VQE
    
    EXAM PATTERN - MEMORIZE THIS STRUCTURE:
    1. Create ParameterVector
    2. Add rotation layers
    3. Add entangling layers
    4. Repeat for depth
    """
    qc = QuantumCircuit(n_qubits)
    
    # Parameters: 2 angles per qubit per layer
    params = ParameterVector('θ', n_qubits * depth * 2)
    idx = 0
    
    for d in range(depth):
        # Rotation layer (Y rotations)
        for i in range(n_qubits):
            qc.ry(params[idx], i)
            idx += 1
        
        # Rotation layer (Z rotations)
        for i in range(n_qubits):
            qc.rz(params[idx], i)
            idx += 1
        
        # Entangling layer
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)
    
    return qc, params
```

**VQE Optimization Loop Pattern:**
```python
for iteration in range(max_iterations):
    # 1. Bind parameters
    bound_circuit = ansatz.assign_parameters({params: current_params})
    
    # 2. Run on quantum computer (Estimator)
    energy = estimator.run([bound_circuit], [hamiltonian]).result()
    
    # 3. Optimize parameters
    current_params = optimizer.step(energy)
    
    # 4. Check convergence
    if converged:
        break
```

#### Parameter Expressions

```python
theta = Parameter('θ')
phi = Parameter('φ')

qc = QuantumCircuit(1)
qc.rx(theta, 0)
qc.ry(2*theta, 0)        # Expression: 2θ
qc.rz(theta + phi, 0)    # Expression: θ + φ

# Bind
bound = qc.assign_parameters({theta: np.pi/4, phi: np.pi/6})
```

#### Partial Binding

```python
# Bind only some parameters
partial = qc.assign_parameters({theta: np.pi/4})
# phi still unbound - can bind later
```

### 🚨 Critical Exam Facts

- ✅ assign_parameters() **returns NEW circuit**
- ✅ ParameterVector more efficient than multiple Parameters
- ✅ Circuits with parameters are **not executable**
- ✅ VQE binds parameters **every iteration**
- ✅ Can use expressions: `2*theta`, `theta + phi`
- ✅ Partial binding possible (bind some, keep others)

### 📋 Exam Patterns

**Pattern 1: "Does assign_parameters() modify original?"**
→ No! Returns new circuit

**Pattern 2: "How many parameters in ParameterVector('θ', 5)?"**
→ 5 parameters

**Pattern 3: "VQE workflow?"**
→ Create ansatz → loop(bind → measure → optimize)

---

## 3.4 Circuit Library
> Source: `section_3_create_circuits/circuit_library.ipynb`

### 🧠 Conceptual Deep Dive

**Pre-built circuits for common algorithms:**
- QFT for Shor's, QPE
- Ansätze for VQE, QAOA
- Standard gate libraries

### ✅ Key Takeaways

#### QFT (Quantum Fourier Transform) - EXAM CRITICAL!

```python
from qiskit.circuit.library import QFTGate

# Create QFT
qft3 = QFTGate(3)

# Use in circuit
qc = QuantumCircuit(3)
qc.append(qft3, range(3))

# Inverse QFT
iqft3 = QFTGate(3).inverse()

# QFT + Inverse = Identity
qc.compose(qft3, inplace=True)
qc.compose(iqft3, inplace=True)  # Returns to initial state
```

**EXAM: QFT used in Shor's algorithm & quantum phase estimation!**

#### RealAmplitudes - VQE Ansatz (GUARANTEED EXAM!)

```python
from qiskit.circuit.library import real_amplitudes

# Create RealAmplitudes ansatz
ansatz = real_amplitudes(num_qubits=3, reps=2)

# Structure:
# - Rotation Layer: RY gates on all qubits
# - Entangling Layer: CNOT gates
# - Repeat for 'reps' times
# - Final Rotation Layer

# Parameters formula: num_qubits * (reps + 1)
# Example: 3 qubits, 2 reps = 3 * 3 = 9 parameters
```

**Entanglement patterns:**
```python
# Linear entanglement (default)
ansatz_linear = real_amplitudes(3, entanglement='linear', reps=1)

# Full entanglement
ansatz_full = real_amplitudes(3, entanglement='full', reps=1)
```

#### EfficientSU2 - More Expressive Ansatz

```python
from qiskit.circuit.library import efficient_su2

ansatz = efficient_su2(num_qubits=3, reps=2)
# Uses both RY and RZ rotations
# More parameters than RealAmplitudes
```

**Comparison:**
| Feature | RealAmplitudes | EfficientSU2 |
|---------|----------------|---------------|
| Rotation gates | RY only | RY + RZ |
| Parameters | Fewer | More (doubled) |
| Expressivity | Lower | Higher |
| Use case | Simple VQE | Complex VQE |

#### TwoLocal (n_local) - Custom Ansatz Builder

```python
from qiskit.circuit.library import n_local

ansatz = n_local(
    num_qubits=3,
    rotation_blocks='ry',        # Single-qubit gates
    entanglement_blocks='cz',    # Two-qubit gates
    reps=2
)

# Multiple rotation gates
ansatz2 = n_local(
    num_qubits=2,
    rotation_blocks=['ry', 'rz'],  # Both RY and RZ
    entanglement_blocks='cx',
    reps=1
)
```

### 🚨 Critical Exam Facts

- ✅ QFT used in quantum algorithms (Shor's, QPE)
- ✅ RealAmplitudes: RY rotations only
- ✅ EfficientSU2: RY + RZ rotations (more parameters)
- ✅ More reps = more parameters = deeper circuit
- ✅ TwoLocal is general template for ansätze
- ✅ RealAmplitudes params: `num_qubits * (reps + 1)`

### 📋 Exam Patterns

**Pattern 1: "How to create QFT?"**
→ `QFTGate(n)` for n qubits

**Pattern 2: "Which has more parameters for same qubits and reps?"**
→ EfficientSU2 (uses both RY and RZ)

**Pattern 3: "How many parameters in RealAmplitudes(3, reps=2)?"**
→ 3 * (2 + 1) = 9 parameters

---

## 3.5 Classical Control
> Source: `section_3_create_circuits/classical_control.ipynb`

### 🧠 Conceptual Deep Dive

**Dynamic circuits = Mid-circuit measurements + Conditional operations**
- Measure during execution (not just at end)
- Apply gates based on measurement results
- Essential for teleportation, error correction

### ✅ Key Takeaways

#### c_if() - Conditional Gate Execution

```python
# Basic c_if() usage
qc = QuantumCircuit(2, 2)

# Measure qubit 0
qc.h(0)
qc.measure(0, 0)

# Apply X to qubit 1 IF classical bit 0 is 1
qc.x(1).c_if(qc.clbits[0], 1)
# X(1) executes ONLY if measurement result is 1!
```

**c_if() Syntax:**
```python
gate.c_if(classical_register_or_bit, value)
# gate: Any quantum gate
# classical_register_or_bit: Classical register or single bit
# value: Integer value to check (0 or 1 for single bit)
```

#### Classical Register Value Encoding

| Bit 1 | Bit 0 | Integer Value |
|-------|-------|---------------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 2 |
| 1 | 1 | 3 |

```python
# Conditional on entire register value
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(3, cr)

qc.h([0, 1])
qc.measure([0, 1], cr)

# Execute if cr == 3 (binary 11, both bits are 1)
qc.x(2).c_if(cr, 3)
```

### 🚨 QUANTUM TELEPORTATION (GUARANTEED EXAM!)

**MEMORIZE THIS PATTERN - 100% GUARANTEED EXAM QUESTION!**

```python
qc = QuantumCircuit(3, 2)

# STEP 0: Prepare state to teleport (qubit 0)
qc.h(0)  # Example: teleport |+⟩ state
qc.barrier()

# STEP 1: Create entanglement (qubits 1 and 2)
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# STEP 2: Bell measurement (qubits 0 and 1)
qc.cx(0, 1)
qc.h(0)
qc.barrier()
qc.measure([0, 1], [0, 1])
qc.barrier()

# STEP 3: Conditional corrections (CRITICAL!)
qc.x(2).c_if(qc.clbits[1], 1)  # If c[1]=1, apply X
qc.z(2).c_if(qc.clbits[0], 1)  # If c[0]=1, apply Z
```

### 🔥 TELEPORTATION CRITICAL EXAM FACTS:

1. ✅ X correction depends on **c[1]** (second measurement)
2. ✅ Z correction depends on **c[0]** (first measurement)
3. ✅ Entanglement is **H + CNOT** on qubits 1, 2
4. ✅ Bell measurement is **CNOT + H + measure** on qubits 0, 1
5. ✅ Result appears on qubit **2** (Bob's qubit)
6. ✅ Qubits 1 and 2 are entangled (Alice and Bob)

**Teleportation Cheat Sheet:**
```python
# MEMORIZE THIS - GUARANTEED EXAM!
qc = QuantumCircuit(3, 2)

# Prepare state (varies)
qc.prepare(0)

# Entangle (FIXED)
qc.h(1)
qc.cx(1, 2)

# Bell measure (FIXED)
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])

# Correct (FIXED)
qc.x(2).c_if(qc.clbits[1], 1)  # X on c[1]
qc.z(2).c_if(qc.clbits[0], 1)  # Z on c[0]
```

**Mnemonic**: "X on c[1], Z on c[0]" - alphabetical order!

#### Mid-Circuit Measurements

```python
qc = QuantumCircuit(2, 2)

# First part
qc.h(0)
qc.cx(0, 1)

# Mid-circuit measurement
qc.measure(0, 0)

# Continue after measurement
qc.h(1)
qc.measure(1, 1)
```

#### Reset and Reuse

```python
qc = QuantumCircuit(1, 2)

# First use
qc.h(0)
qc.measure(0, 0)

# Reset to |0⟩
qc.reset(0)

# Reuse qubit
qc.x(0)
qc.measure(0, 1)
```

### 🚨 Critical Exam Facts

- ✅ Teleportation X correction: `c_if(qc.clbits[1], 1)`
- ✅ Teleportation Z correction: `c_if(qc.clbits[0], 1)`
- ✅ c_if() syntax: `gate.c_if(classical_bit, value)`
- ✅ Entangle qubits 1 and 2 in teleportation
- ✅ Result appears on qubit 2 (Bob's qubit)
- ✅ Register value is binary integer
- ✅ reset() is non-reversible operation

### 📋 Exam Patterns

**Pattern 1: "Conditional gate syntax?"**
→ `gate.c_if(classical_bit, value)`

**Pattern 2: "Teleportation X correction?"**
→ `qc.x(2).c_if(qc.clbits[1], 1)`

**Pattern 3: "Which qubits entangled in teleportation?"**
→ Qubits 1 and 2

---

## 3.6 Dynamic Circuits
> Source: Modern quantum hardware features

### 🧠 Conceptual Deep Dive

**Dynamic vs Static Circuits:**
- **Static circuits**: All measurements at the end, no feedback
- **Dynamic circuits**: Mid-circuit measurements with real-time classical control
- **Feed-forward**: Measurement results influence future operations

**Real-Time Decision Making:**
- Measure = "Check the answer mid-test"
- Conditional gate = "Adjust strategy based on answer"
- Essential for error correction, teleportation, adaptive algorithms

**The Restaurant Analogy:**
- Static: Order full meal upfront, eat at end
- Dynamic: Taste dish, adjust seasoning, continue cooking (real-time feedback)

### ✅ Key Takeaways

#### if_test() - Modern Dynamic Circuit Syntax

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)

# Mid-circuit measurement
qc.h(0)
qc.measure(0, 0)

# Modern if_test syntax (preferred over c_if)
with qc.if_test((qc.clbits[0], 1)):
    qc.x(1)  # Execute if measurement result is 1

# Multiple operations in conditional block
with qc.if_test((qc.clbits[0], 1)):
    qc.h(1)
    qc.x(1)
    qc.z(1)
```

**if_test() vs c_if():**
- `if_test()`: Modern, supports multiple gates, cleaner syntax
- `c_if()`: Legacy, single gate only, still widely used

#### while_loop() - Iterative Circuits

```python
from qiskit.circuit import QuantumCircuit

qc = QuantumCircuit(2, 1)

# Loop until measurement returns 1
with qc.while_loop((qc.clbits[0], 0)):  # While c[0] == 0
    qc.h(0)
    qc.measure(0, 0)

# Useful for: probabilistic algorithms, error correction loops
```

#### for_loop() - Counted Iterations

```python
# Repeat operation N times
qc = QuantumCircuit(1)

# Apply H gate 5 times
with qc.for_loop(range(5)):
    qc.h(0)

# With loop variable
with qc.for_loop(range(3)) as i:
    qc.rx(0.1 * i, 0)  # Different angle each iteration
```

#### switch_case() - Multiple Branches

```python
qc = QuantumCircuit(2, 2)

qc.h(0)
qc.h(1)
qc.measure([0, 1], [0, 1])

# Switch based on measurement result
with qc.switch(qc.clbits[0]) as case:
    with case(0):  # If c[0] == 0
        qc.x(1)
    with case(1):  # If c[0] == 1
        qc.z(1)
    with case(case.DEFAULT):  # Default case
        qc.h(1)
```

#### break and continue Statements

```python
qc = QuantumCircuit(2, 1)

with qc.while_loop((qc.clbits[0], 0)):
    qc.h(0)
    qc.measure(0, 0)
    
    # Break if certain condition
    with qc.if_test((qc.clbits[0], 1)):
        qc.break_loop()  # Exit the while loop
```

### ⚠️ EXAM TRAP: Backend Support

```python
# ❌ Not all backends support dynamic circuits!
# Most simulators: ✅ Support
# Real hardware: ⚠️ Limited support (check backend.configuration())

# Check support
backend = provider.get_backend('ibm_brisbane')
config = backend.configuration()
print(config.supported_features)  # Look for 'dynamic_circuits'
```

### 🚨 Critical Exam Facts

**Dynamic Circuit Features:**
- ✅ `if_test()` - Modern conditional execution (preferred)
- ✅ `while_loop()` - Conditional iteration
- ✅ `for_loop()` - Counted iteration  
- ✅ `switch_case()` - Multi-way branching
- ✅ `break_loop()` / `continue_loop()` - Loop control
- ✅ `reset()` - Return qubit to |0⟩ for reuse
- ✅ Mid-circuit measurements enable all of the above

**Key Differences:**
- ✅ `if_test()` uses `with` statement, supports multiple gates
- ✅ `c_if()` is method chaining, single gate only
- ✅ `if_test()` syntax: `with qc.if_test((classical_bit, value)):`
- ✅ `c_if()` syntax: `gate.c_if(classical_bit, value)`

**Backend Compatibility:**
- ✅ Not all backends support dynamic circuits
- ✅ Check `backend.configuration().supported_features`
- ✅ Aer simulator: Full support
- ✅ Real hardware: Growing support (2024+)

**Common Use Cases:**
- ✅ Quantum teleportation (classical corrections)
- ✅ Quantum error correction (syndrome measurement + correction)
- ✅ Adaptive VQE (adjust parameters based on measurements)
- ✅ Repeat-until-success algorithms

### 📋 Exam Patterns

**Pattern 1: "Modern dynamic circuit syntax?"**
```python
# if_test (modern)
with qc.if_test((qc.clbits[0], 1)):
    qc.x(1)

# c_if (legacy, still tested!)
qc.x(1).c_if(qc.clbits[0], 1)
```

**Pattern 2: "Loop until measurement returns 1?"**
```python
with qc.while_loop((qc.clbits[0], 0)):  # While c[0] == 0
    qc.h(0)
    qc.measure(0, 0)
```

**Pattern 3: "Repeat operation N times?"**
```python
with qc.for_loop(range(N)):
    qc.h(0)
```

**Pattern 4: "Multiple conditional branches?"**
```python
with qc.switch(qc.clbits[0]) as case:
    with case(0):
        qc.x(1)
    with case(1):
        qc.z(1)
```

**Pattern 5: "Reset and reuse qubit?"**
```python
qc.measure(0, 0)  # Measure qubit
qc.reset(0)       # Reset to |0⟩
qc.h(0)           # Reuse qubit
```

**Pattern 6: "Check backend support?"**
```python
config = backend.configuration()
supports_dynamic = 'dynamic_circuits' in config.supported_features
```

**Pattern 7: "Memory Aid?"**
```
"If-While-For-Switch-Reset"
- if_test: One-time conditional
- while_loop: Repeat until condition
- for_loop: Fixed iterations
- switch: Multiple branches
- reset: Qubit reuse
All require mid-circuit measurement!
```

---

### 🎓 Section 3 Complete Checklist

Before moving on, make sure you can:
- [ ] Create circuits with QuantumCircuit() in multiple ways
- [ ] Know property vs method: num_qubits vs depth()
- [ ] Calculate depth for parallel/sequential gates
- [ ] Use compose() vs tensor() correctly
- [ ] Create and bind parameterized circuits
- [ ] Use assign_parameters() and capture return value
- [ ] Know VQE ansatz pattern with ParameterVector
- [ ] Use QFT, RealAmplitudes, EfficientSU2 from library
- [ ] Implement quantum teleportation with c_if()
- [ ] Know teleportation corrections: X on c[1], Z on c[0]
- [ ] Use if_test() for modern dynamic circuits
- [ ] Understand while_loop(), for_loop(), switch_case()
- [ ] Know when to use reset() for qubit reuse
- [ ] Check backend support for dynamic circuits

---

# Section 4: Run Circuits (15%)

---

## 4.1 Transpilation
> Source: `section_4_run_circuits/transpilation.ipynb`

### 🧠 Conceptual Deep Dive

**Translator Analogy:**
- **Source**: Your abstract circuit (the poem)
- **Target**: Quantum hardware (Japanese language)
- **Constraints**: Device-specific gates and connectivity
- **Goal**: Preserve meaning while adapting to constraints

**Virtual vs Physical Qubits:**
- Virtual qubits: Your logical variables (`q[0]`)
- Physical qubits: Actual hardware qubits
- Transpiler maps virtual → physical

**What Transpilation Does:**
1. **Basis Gate Translation** - Convert to hardware-native gates (e.g., H → RZ + SX)
2. **Layout/Routing** - Map virtual → physical qubits + add SWAPs for connectivity
3. **Optimization** - Reduce gates while preserving function

**EXAM FACT**: Transpilation is MANDATORY for real hardware execution!

### ✅ Key Takeaways

#### Basic Usage

```python
from qiskit import transpile

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Basic transpilation
qc_trans = transpile(qc)

# With backend (provides basis_gates + coupling_map)
qc_trans = transpile(qc, backend=backend, optimization_level=3)
```

#### transpile() Signature

```python
transpile(
    circuits,                    # Circuit or list of circuits
    backend=None,                # Target backend (optional)
    basis_gates=None,            # Allowed gates (optional)
    coupling_map=None,           # Qubit connectivity (optional)
    optimization_level=1,        # 0-3 (default: 1)
    initial_layout=None,         # Manual qubit mapping (optional)
    seed_transpiler=None         # Reproducibility (optional)
)
```

**EXAM TIP**: `backend` auto-provides `basis_gates` and `coupling_map`!

### 📊 Optimization Levels (MEMORIZE!)

| Level | Speed | Quality | Use Case |
|-------|-------|---------|----------|
| 0 | Fastest | Lowest | Testing, debugging |
| 1 | Fast | Good | General purpose (DEFAULT) |
| 2 | Medium | Better | Production |
| 3 | Slowest | Best | Critical experiments |

**Memory Aid**: "0=Debug, 1=Default, 2=Better, 3=Best-Slow!"

```python
# Level 0: No optimization
qc_0 = transpile(qc, optimization_level=0)

# Level 1: Light optimization (DEFAULT)
qc_1 = transpile(qc, optimization_level=1)

# Level 2: Medium optimization
qc_2 = transpile(qc, optimization_level=2)

# Level 3: Heavy optimization (best quality)
qc_3 = transpile(qc, optimization_level=3)
```

### 🔧 Basis Gates

**IBM Hardware (most common):**
```python
basis_gates = ['cx', 'id', 'rz', 'sx', 'x']
```

**Alternative Sets:**
```python
# Some backends use ECR instead of CX
basis_gates = ['ecr', 'id', 'rz', 'sx', 'x']
```

### 🗺️ Coupling Map

```python
# Linear coupling map (1D chain)
coupling_map = [(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2)]

# Circuit that violates coupling
qc = QuantumCircuit(4)
qc.cx(0, 3)  # Not directly connected!

# Transpile adds SWAP gates to route
qc_trans = transpile(qc, coupling_map=coupling_map)
```

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
# qc1 and qc2 might be DIFFERENT!
# Use seed_transpiler=42 for reproducibility
```

### 🚨 Critical Exam Facts

- ✅ Default `optimization_level=1`
- ✅ `backend` parameter provides basis_gates + coupling_map
- ✅ Level 3 = best quality, slowest
- ✅ Transpilation is MANDATORY for hardware
- ✅ Primitives auto-transpile, but explicit gives control
- ✅ `transpile()` from `qiskit` not `qiskit_ibm_runtime`
- ✅ Coupling map = list of tuples [(0,1), (1,0), ...]

---

## 4.2 Backend Target V2 API
> Source: `section_4_run_circuits/backend_target.ipynb`

### 🧠 Conceptual Deep Dive

**V2 is the standard for Qiskit 2.X certification!**

```
V1 API (DEPRECATED):           V2 API (CURRENT):
backend.configuration()        backend.target
backend.properties()           backend.target.operation_names
config.basis_gates             backend.target.instruction_supported()
```

### ✅ Key Takeaways

#### V1 → V2 Translation Table (MEMORIZE!)

| Feature | V1 API (Old) | V2 API (New) |
|---------|--------------|--------------|
| Get basis gates | `backend.configuration().basis_gates` | `backend.target.operation_names` |
| Get coupling map | `backend.configuration().coupling_map` | `backend.target.build_coupling_map()` |
| Check gate support | Manual parsing | `target.instruction_supported('cx', (0,1))` |
| Number of qubits | `backend.configuration().n_qubits` | `backend.num_qubits` |

#### operation_names vs basis_gates

```python
# V1 basis_gates (gates only)
['cx', 'rz', 'sx', 'x', 'id']

# V2 operation_names (all operations)
['cx', 'rz', 'sx', 'x', 'id', 'measure', 'reset', 'delay', ...]
```

**V2 includes non-gate operations (measure, reset, delay)!**

#### instruction_supported() (EXAM CRITICAL!)

```python
# Check if gate supported on specific qubits
target = backend.target

# Check single-qubit gate (note trailing comma!)
supported = target.instruction_supported('sx', qargs=(0,))

# Check two-qubit gate
supported = target.instruction_supported('cx', qargs=(0, 1))
```

### ⚠️ EXAM TRAP: qargs Format

```python
# CORRECT - tuple
target.instruction_supported('cx', qargs=(0, 1))  # ✓
target.instruction_supported('sx', qargs=(0,))    # ✓

# WRONG - list or no comma for single qubit
target.instruction_supported('cx', qargs=[0, 1])  # ❌
target.instruction_supported('sx', qargs=(0))     # ❌
```

### 🚨 Critical Exam Facts

- ✅ V2 is Qiskit 2.X standard
- ✅ `backend.target` not `backend.configuration()`
- ✅ `operation_names` not `basis_gates`
- ✅ `instruction_supported(op, qargs=(i,j))`
- ✅ qargs must be tuple: `(0,)` not `(0)`
- ✅ operation_names includes measure/reset

---

## 4.3 QiskitRuntimeService
> Source: `section_4_run_circuits/runtime_service.ipynb`

### 🧠 Conceptual Deep Dive

**QiskitRuntimeService = Gateway to IBM Quantum**

```
Your Code (Local)
    ↓
┌──────────────────────┐
│  QiskitRuntimeService│  ← Authentication
└──────────────────────┘
    ↓ (Internet)
┌──────────────────────┐
│  IBM Quantum Cloud   │  ← Queue, scheduling
└──────────────────────┘
    ↓
┌──────────────────────┐
│  Quantum Backend     │  ← Real QPU or Simulator
└──────────────────────┘
```

### ✅ Key Takeaways

#### Three Initialization Patterns

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# PATTERN 1: Save account (one-time setup)
QiskitRuntimeService.save_account(
    channel='ibm_quantum',
    token='YOUR_TOKEN',
    overwrite=True
)

# PATTERN 2: Default initialization (uses saved credentials)
service = QiskitRuntimeService()

# PATTERN 3: Explicit token (not recommended for production)
service = QiskitRuntimeService(
    channel='ibm_quantum',
    token='YOUR_TOKEN'
)
```

#### Backend Selection

```python
# Get specific backend
backend = service.backend('ibm_brisbane')

# List all backends
backends = service.backends()

# Find least busy (EXAM COMMON!)
backend = service.least_busy(
    operational=True,
    simulator=False
)
```

#### Backend Properties (V2 API)

```python
backend.name           # String: 'ibm_brisbane'
backend.num_qubits     # Integer: 127
backend.operation_names  # List: ['ecr', 'rz', 'sx', ...]
backend.coupling_map   # List of tuples
backend.target         # Target object
```

### ⚠️ EXAM TRAP: Channels

```python
# CORRECT
channel='ibm_quantum'  # ✓ Free IBM Quantum Platform

# WRONG
channel='ibm_quantum_platform'  # ❌ Old name
channel='quantum'               # ❌ Wrong
```

### 🚨 Critical Exam Facts

- ✅ `QiskitRuntimeService()` uses saved credentials
- ✅ `save_account()` is one-time setup
- ✅ V2 API: `backend.operation_names` (not `basis_gates`)
- ✅ `least_busy()` finds shortest queue
- ✅ Simulators have 'simulator' in name
- ✅ `channel='ibm_quantum'` for free tier

---

## 4.4 Jobs and Sessions
> Source: `section_4_run_circuits/jobs_and_sessions.ipynb`

### 🧠 Conceptual Deep Dive

| Concept | Restaurant Analogy |
|---------|-------------------|
| **Job** | A single order |
| **Batch** | Group order (independent circuits) |
| **Session** | Reserved private room (sequential access) |

### ✅ Key Takeaways

#### Job Lifecycle

```python
job = sampler.run([circuit])  # Returns immediately

# Job states: QUEUED → RUNNING → DONE

# Get results (BLOCKING!)
result = job.result()

# Check status (non-blocking)
status = job.status()
```

#### job.result() vs job.status()

```python
# job.result() - BLOCKING
result = job.result()  # Waits until job completes

# job.status() - NON-BLOCKING
status = job.status()  # Returns immediately
```

**EXAM TIP**: `result()` blocks, `status()` does not!

#### Session Pattern (EXAM CRITICAL!)

```python
from qiskit_ibm_runtime import Session, Sampler

with Session(backend=backend) as session:
    # Pass session to primitive (NOT backend!)
    sampler = Sampler(session=session)
    
    for i in range(10):  # VQE iterations
        job = sampler.run([circuit])
        result = job.result()
        
# Session auto-closes after context exit
```

### ⚠️ EXAM TRAP: Session vs Backend Parameter

```python
# CORRECT - Use session parameter
with Session(backend=backend) as session:
    sampler = Sampler(session=session)  # ✓

# WRONG - Don't use backend in session
with Session(backend=backend) as session:
    sampler = Sampler(backend=backend)  # ❌
```

#### Session vs Batch

| Need | Use |
|------|-----|
| Sequential, dependent jobs (VQE) | **Session** |
| Parallel, independent circuits | **Batch** |

### 🚨 Critical Exam Facts

- ✅ `job.result()` BLOCKS until done
- ✅ `job.status()` returns immediately
- ✅ Session uses `session` parameter not `backend`
- ✅ Sessions recommended for iterative algorithms (VQE)
- ✅ `job.job_id()` for retrieval
- ✅ Context manager auto-closes session

---

## 4.5 Options Configuration
> Source: `section_4_run_circuits/options_configuration.ipynb`

### 🧠 Conceptual Deep Dive

**Options = Settings for quantum job execution**

### ✅ Key Takeaways

#### Default Values (MEMORIZE!)

```python
from qiskit_ibm_runtime import Options

options = Options()
options.execution.shots        # 4096 (NOT 1024!)
options.optimization_level     # 2 (NOT 1 like transpile!)
options.resilience_level       # 0 (no mitigation)
```

#### Namespace Structure

```
Options()
├── optimization_level (0-3)     [top-level]
├── resilience_level (0-2)       [top-level]
├── execution
│   ├── shots (default 4096)
│   └── init_qubits (default True)
└── simulator
    └── seed_simulator (optional)
```

#### Resilience Levels

| Level | Method | Use Case |
|-------|--------|----------|
| 0 | None | Simulator, debugging |
| 1 | TREX (Twirled Readout Error Extinction) | Most production |
| 2 | ZNE (Zero-Noise Extrapolation) | Critical accuracy |

### ⚠️ EXAM TRAP: Default Values

```python
# Options defaults (DIFFERENT from transpile!)
options.execution.shots = 4096  # ✓ NOT 1024!
options.optimization_level = 2  # ✓ NOT 1!
```

### ⚠️ EXAM TRAP: Accessing Shots

```python
# CORRECT - nested under execution
options.execution.shots = 1000  # ✓

# WRONG - not top-level
options.shots = 1000  # ❌
```

#### Complete Configuration Pattern

```python
from qiskit_ibm_runtime import Sampler, Options

options = Options()
options.optimization_level = 3
options.resilience_level = 1
options.execution.shots = 2000

sampler = Sampler(backend=backend, options=options)
job = sampler.run([circuit])
```

### 🚨 Critical Exam Facts

- ✅ Default shots = **4096** (NOT 1024!)
- ✅ Default optimization_level in Options = **2** (NOT 1!)
- ✅ Access shots via `options.execution.shots`
- ✅ resilience_level is top-level (not nested)
- ✅ Higher resilience = better accuracy, more overhead

### 🎓 Section 4 Complete Checklist

Before moving on, make sure you can:
- [ ] Use transpile() with optimization levels 0-3
- [ ] Know default optimization_level is 1 for transpile, 2 for Options
- [ ] Use V2 backend API: target, operation_names
- [ ] Initialize QiskitRuntimeService and select backends
- [ ] Use Sessions for VQE/iterative algorithms
- [ ] Know job.result() blocks, job.status() doesn't
- [ ] Configure Options with correct namespaces
- [ ] Know default shots is 4096, not 1024

---

# Section 5: Sampler Primitive (12%)

---

## 5.1 Sampler Primitive
> Source: `section_5_sampler/sampler_primitive.ipynb`

### 🧠 Conceptual Deep Dive

**Sampler = Survey Taker (Loaded Die Analogy):**
- **Circuit** = How the die is manufactured
- **Shots** = How many times you roll it
- **Counts** = Tally of outcomes `{'00': 512, '11': 512}`

**Sampler answers:** "If I measure this circuit, what outcomes do I get?"

**CRITICAL**: Circuit MUST have measurements!

### ⚠️ EXAM TRAP: Sampler vs Estimator

| Feature | Sampler | Estimator |
|---------|---------|------------|
| **Purpose** | Measurement counts | Expectation values |
| **Needs measurements?** | ✅ YES | ❌ NO |
| **Output** | `{'00': 512, '11': 512}` | `⟨H⟩ = 0.73` |
| **Use case** | Get bitstrings | Calculate energy |

**Memory Aid**: "Sampler = Sample bitstrings, Estimator = Estimate ⟨O⟩"

### ✅ Key Takeaways

#### Basic Pattern

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler as Sampler

# Create circuit WITH measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])  # MUST have measurements!

# Create Sampler
sampler = Sampler()

# Run circuit
job = sampler.run([qc], shots=1024)

# Get results
result = job.result()
counts = result[0].data.meas.get_counts()

print(counts)  # {'00': 512, '11': 512}
```

### 🎯 EXAM CRITICAL: Result Access Pattern

**MEMORIZE THIS**:
```python
counts = result[0].data.meas.get_counts()
          ↑      ↑    ↑       ↑
          │      │    │       └─ Method to get dict
          │      │    └───────── Measurement register name
          │      └───────────── Data attribute
          └─────────────────── Circuit index
```

#### Multiple Circuits

```python
# Run multiple circuits together
job = sampler.run([qc1, qc2, qc3], shots=1024)
result = job.result()

# Access each result
counts1 = result[0].data.meas.get_counts()
counts2 = result[1].data.meas.get_counts()
counts3 = result[2].data.meas.get_counts()
```

#### Parameterized Circuits

```python
from qiskit.circuit import Parameter
import numpy as np

theta = Parameter('θ')
qc = QuantumCircuit(1, 1)
qc.ry(theta, 0)
qc.measure(0, 0)

# Must bind parameters BEFORE Sampler
qc_bound = qc.assign_parameters({theta: np.pi/4})
job = sampler.run([qc_bound], shots=1024)
```

### ⚠️ EXAM TRAP: Parameter Binding

```python
# WRONG - Don't pass parameterized circuit
qc.ry(Parameter('θ'), 0)
sampler.run([qc])  # ❌ ERROR!

# CORRECT - Bind first
qc_bound = qc.assign_parameters({'θ': 0.5})
sampler.run([qc_bound])  # ✅
```

### 📊 PUB Format (EXAM CRITICAL!)

**PUB** = Primitive Unified Bloc = (circuit, parameters, shots)

**CRITICAL**: Must be tuple inside list!

```python
# Single circuit (note trailing comma!)
sampler.run([(qc,)])  # ✓ Correct

# WRONG patterns:
sampler.run(qc)        # ❌ Not wrapped
sampler.run([qc])      # ❌ Not tuple
sampler.run((qc))      # ❌ Missing comma

# With parameters
sampler.run([(qc, [0.5])])

# Multiple circuits
sampler.run([(qc1,), (qc2,), (qc3,)])
```

### ⚠️ EXAM TRAP: Trailing Comma

```python
(qc)     # NOT a tuple! Just parentheses
(qc,)    # ✓ Tuple with one element

# In Python:
type((qc))   # <class 'QuantumCircuit'>
type((qc,))  # <class 'tuple'>
```

### 📊 Local vs Runtime Comparison

| Feature | Local | Runtime |
|---------|-------|---------|
| Import from | `qiskit.primitives` | `qiskit_ibm_runtime` |
| Runs on | Your computer | IBM hardware |
| Requires account | No | Yes |
| Speed | Instant | Queue time |
| Noise | None (perfect) | Real hardware noise |
| Result access | **Same for both** | **Same for both** |

```python
# Local Sampler (simulation)
from qiskit.primitives import StatevectorSampler as Sampler
sampler = Sampler()

# Runtime Sampler (real hardware)
from qiskit_ibm_runtime import Sampler
sampler = Sampler(backend=backend)
```

### 📝 Result Processing

```python
# Get counts
counts = result[0].data.meas.get_counts()
# Returns: {'00': 512, '11': 512}

# Convert to probabilities
total_shots = sum(counts.values())
probs = {state: count/total_shots for state, count in counts.items()}
# Returns: {'00': 0.5, '11': 0.5}

# Most probable state
most_probable = max(counts, key=counts.get)
```

### 🚨 Critical Exam Facts

- ✅ **MEMORIZE**: `result[0].data.meas.get_counts()`
- ✅ Circuit MUST have measurements
- ✅ Must bind parameters before running
- ✅ PUB format: `[(circuit,)]` with trailing comma
- ✅ Local: `qiskit.primitives`, Runtime: `qiskit_ibm_runtime`
- ✅ Multiple circuits: `result[i].data.meas.get_counts()`

### 📋 Exam Patterns

**Pattern 1: "What's wrong with this Sampler code?"**
→ Check: measurements, parameter binding, PUB format, imports

**Pattern 2: "How to extract counts?"**
→ `result[0].data.meas.get_counts()`

**Pattern 3: "Does Sampler need measurements?"**
→ YES! (Unlike Estimator)

### 🎓 Section 5 Complete Checklist

Before moving on, make sure you can:
- [ ] Know Sampler requires measurements
- [ ] Access counts: `result[0].data.meas.get_counts()`
- [ ] Use PUB format with trailing comma
- [ ] Bind parameters before running
- [ ] Know Local vs Runtime imports
- [ ] Process multiple circuits with result[i]

---

# Section 6: Estimator Primitive (10%)

---

## 6.1 Estimator Primitive
> Source: `section_6_estimator/estimator_primitive.ipynb`

### 🧠 Conceptual Deep Dive

**Estimator = Average Calculator**
- Given a circuit (quantum state) and an observable (measurement operator)
- Returns the expectation value ⟨ψ|O|ψ⟩

**Estimator answers:** "What's the average value of this observable?"

**CRITICAL**: No measurements needed! Estimator works at the state level.

### ⚠️ EXAM TRAP: Estimator vs Sampler

| Feature | Estimator | Sampler |
|---------|-----------|---------|
| **Output** | `⟨O⟩` value | Counts dict |
| **Needs measurements?** | ❌ NO | ✅ YES |
| **Result access** | `result[0].data.evs` | `result[0].data.meas.get_counts()` |
| **Use case** | Calculate energy | Get bitstrings |

### ✅ Key Takeaways

#### Basic Pattern

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit.quantum_info import SparsePauliOp

# Create circuit WITHOUT measurements!
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO measurements!

# Create observable
observable = SparsePauliOp('ZZ')

# Create Estimator
estimator = Estimator()

# Run estimation
job = estimator.run([(qc, observable)])

# Get result
result = job.result()
expval = result[0].data.evs  # Note: 'evs' not 'evs()'!

print(f"⟨ZZ⟩ = {expval}")  # ⟨ZZ⟩ = 1.0
```

### 🎯 EXAM CRITICAL: Result Access

**MEMORIZE THIS**:
```python
expval = result[0].data.evs
               ↑      ↑    ↑
               │      │    └─ expectation valueS (plural! attribute not method)
               │      └────── Data attribute
               └───────────── Circuit index
```

⚠️ **TRAP**: It's `evs` (attribute), NOT `evs()` (method)!

### 📊 SparsePauliOp: Qubit Ordering (CRITICAL!)

**EXAM TRAP**: Qiskit uses RIGHT-TO-LEFT ordering!

```python
SparsePauliOp('ZX')
#              ↑↑
#              │└─ Applied to qubit 0 (rightmost)
#              └── Applied to qubit 1 (leftmost)
```

**Examples**:
- `'Z'` on 1 qubit = Z on qubit 0
- `'ZX'` on 2 qubits = X on qubit 0, Z on qubit 1
- `'IZX'` on 3 qubits = X on q0, Z on q1, I on q2

**Memory Aid**: "Read RIGHT to LEFT, q0 to qN"

### 📊 SparsePauliOp Construction

```python
from qiskit.quantum_info import SparsePauliOp

# Single Pauli
Z = SparsePauliOp('Z')

# Multi-qubit Pauli
ZZ = SparsePauliOp('ZZ')  # Z⊗Z

# With coefficient
op = SparsePauliOp(['Z'], [0.5])  # 0.5 * Z

# Sum of terms (Hamiltonian)
H = SparsePauliOp(['ZZ', 'XX', 'YY'], [1.0, 0.5, 0.5])
# = 1.0*ZZ + 0.5*XX + 0.5*YY

# Alternative construction
H = SparsePauliOp.from_list([
    ('ZZ', 1.0),
    ('XX', 0.5),
    ('YY', 0.5)
])
```

### ⚠️ EXAM TRAP: No Measurements for Estimator!

```python
# WRONG - Estimator doesn't need measurements
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure([0,1], [0,1])  # ❌ Don't add measurements!

# CORRECT - No measurements
qc = QuantumCircuit(2)  # No classical bits
qc.h(0)
qc.cx(0, 1)
# Let Estimator handle the math
```

### 📊 Multiple Observables

```python
# Multiple observables on same circuit
observables = [
    SparsePauliOp('ZZ'),
    SparsePauliOp('XX'),
    SparsePauliOp('YY')
]

# Run all at once
job = estimator.run([(qc, obs) for obs in observables])
result = job.result()

# Access each result
zz_exp = result[0].data.evs
xx_exp = result[1].data.evs
yy_exp = result[2].data.evs
```

### 📊 Bell State Expectations (EXAM FAVORITE!)

For Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2:

| Observable | Value | Why |
|------------|-------|-----|
| ⟨ZZ⟩ | +1 | Both qubits same in Z basis |
| ⟨XX⟩ | +1 | Both qubits same in X basis |
| ⟨YY⟩ | -1 | Negative correlation in Y basis |
| ⟨ZI⟩ | 0 | q0 equally +1/-1 |
| ⟨IZ⟩ | 0 | q1 equally +1/-1 |

**Memory Aid**: "ZZ and XX = +1, YY = -1 for Bell state"

### 📊 Local vs Runtime Comparison

```python
# Local Estimator (simulation)
from qiskit.primitives import StatevectorEstimator as Estimator
estimator = Estimator()

# Runtime Estimator (real hardware)
from qiskit_ibm_runtime import Estimator
estimator = Estimator(backend=backend)
```

### 🚨 Critical Exam Facts

- ✅ **MEMORIZE**: `result[0].data.evs` (attribute, not method!)
- ✅ NO measurements needed
- ✅ Qubit ordering: RIGHT TO LEFT
- ✅ SparsePauliOp('ZX') = X on q0, Z on q1
- ✅ Bell state: ⟨ZZ⟩=⟨XX⟩=+1, ⟨YY⟩=-1

---

## 6.2 VQE Pattern
> Source: `section_6_estimator/vqe_pattern.ipynb`

### 🧠 Conceptual Deep Dive

**VQE** = Variational Quantum Eigensolver

**Goal**: Find the minimum eigenvalue (ground state energy) of a Hamiltonian

**Components**:
1. **Ansatz** = Parameterized circuit (trial state)
2. **Hamiltonian** = Energy operator (what we minimize)
3. **Estimator** = Calculates ⟨H⟩
4. **Optimizer** = Adjusts parameters

### 📊 VQE Loop

```
┌─────────────────────────────────────────────────┐
│                                                 │
│    ┌─────────┐    ┌───────────┐    ┌────────┐  │
│    │ Ansatz  │───►│ Estimator │───►│ Energy │  │
│    │(θ₁,θ₂..)│    │   ⟨H⟩     │    │  E(θ)  │  │
│    └────┬────┘    └───────────┘    └───┬────┘  │
│         │                               │       │
│         │    ┌───────────────┐         │       │
│         └────│   Optimizer   │◄────────┘       │
│              │ (minimize E)  │                  │
│              └───────────────┘                  │
└─────────────────────────────────────────────────┘
```

### ✅ Complete VQE Template (EXAM PATTERN!)

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit.quantum_info import SparsePauliOp
from scipy.optimize import minimize
import numpy as np

# 1. ANSATZ - Parameterized circuit
def create_ansatz(n_qubits, n_layers):
    """Create a hardware-efficient ansatz."""
    qc = QuantumCircuit(n_qubits)
    params = []
    
    for layer in range(n_layers):
        for i in range(n_qubits):
            theta = Parameter(f'θ_{layer}_{i}')
            params.append(theta)
            qc.ry(theta, i)
        
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)
    
    return qc, params

# 2. HAMILTONIAN - What we minimize
H = SparsePauliOp.from_list([
    ('ZZ', 1.0),
    ('XI', 0.5),
    ('IX', 0.5)
])

# 3. CREATE ANSATZ
ansatz, params = create_ansatz(n_qubits=2, n_layers=2)

# 4. COST FUNCTION
estimator = Estimator()

def cost_function(param_values):
    """Evaluate ⟨H⟩ for given parameters."""
    # Bind parameters
    param_dict = dict(zip(params, param_values))
    bound_circuit = ansatz.assign_parameters(param_dict)
    
    # Run estimator
    job = estimator.run([(bound_circuit, H)])
    result = job.result()
    energy = result[0].data.evs
    
    return float(energy)

# 5. OPTIMIZE
initial_params = np.random.uniform(-np.pi, np.pi, len(params))

result = minimize(
    cost_function,
    initial_params,
    method='COBYLA',
    options={'maxiter': 100}
)

print(f"Minimum energy: {result.fun}")
print(f"Optimal parameters: {result.x}")
```

### 📊 VQE Components Summary

| Component | Purpose | Qiskit Class |
|-----------|---------|--------------|
| Ansatz | Trial wavefunction | `QuantumCircuit` with `Parameter` |
| Hamiltonian | Energy operator | `SparsePauliOp` |
| Estimator | Calculate ⟨H⟩ | `StatevectorEstimator` / `Estimator` |
| Optimizer | Find minimum | `scipy.optimize.minimize` |

### ⚠️ EXAM TRAP: Cost Function Pattern

```python
def cost_function(param_values):
    # 1. Create parameter dictionary
    param_dict = dict(zip(params, param_values))
    
    # 2. Bind parameters to circuit
    bound_circuit = ansatz.assign_parameters(param_dict)
    
    # 3. Run estimator (no measurements!)
    job = estimator.run([(bound_circuit, hamiltonian)])
    
    # 4. Extract energy
    energy = job.result()[0].data.evs
    
    # 5. Return as float (optimizer expects float)
    return float(energy)
```

### 📊 Common Ansätze

**Hardware-Efficient Ansatz (HEA)**:
```python
# RY rotations + CNOT entanglement
for i in range(n_qubits):
    qc.ry(Parameter(f'θ_{i}'), i)
for i in range(n_qubits - 1):
    qc.cx(i, i + 1)
```

**Simple Ansatz for Exam**:
```python
from qiskit.circuit import Parameter

qc = QuantumCircuit(2)
θ1 = Parameter('θ1')
θ2 = Parameter('θ2')
qc.ry(θ1, 0)
qc.ry(θ2, 1)
qc.cx(0, 1)
```

### 📊 Common Hamiltonians

**Heisenberg Hamiltonian**:
```python
H = SparsePauliOp.from_list([
    ('XX', J),
    ('YY', J),
    ('ZZ', J)
])
```

**Transverse Field Ising Model**:
```python
H = SparsePauliOp.from_list([
    ('ZZ', -J),   # Interaction term
    ('XI', -h),   # Transverse field on q0
    ('IX', -h)    # Transverse field on q1
])
```

### 📊 Optimizers

| Optimizer | Gradient-Free? | Good For |
|-----------|----------------|----------|
| COBYLA | Yes | Noisy functions |
| SPSA | Yes | Noisy hardware |
| L-BFGS-B | No | Smooth functions |
| Nelder-Mead | Yes | General purpose |

```python
# COBYLA - Most common for VQE
result = minimize(cost_function, x0, method='COBYLA')

# SPSA - Good for noisy
from scipy.optimize import minimize
result = minimize(cost_function, x0, method='Nelder-Mead')
```

### 🚨 VQE Critical Exam Facts

- ✅ VQE = Ansatz + Hamiltonian + Estimator + Optimizer
- ✅ Ansatz has parameters, Hamiltonian is SparsePauliOp
- ✅ Cost function returns `float(result[0].data.evs)`
- ✅ No measurements in ansatz!
- ✅ Use `assign_parameters()` before each iteration
- ✅ Optimizer is classical (scipy.optimize.minimize)

### 📋 Exam Patterns

**Pattern 1: "What are the components of VQE?"**
→ Ansatz, Hamiltonian, Estimator, Classical Optimizer

**Pattern 2: "What does VQE minimize?"**
→ Expectation value ⟨ψ(θ)|H|ψ(θ)⟩

**Pattern 3: "How does Estimator work in VQE?"**
→ Calculates ⟨H⟩ without measurements, returns expectation value

**Pattern 4: "What's wrong with this VQE code?"**
→ Check: measurements (shouldn't have), parameter binding, result access

### 🎓 Section 6 Complete Checklist

Before moving on, make sure you can:
- [ ] Know Estimator doesn't need measurements
- [ ] Access expectation value: `result[0].data.evs`
- [ ] Understand SparsePauliOp qubit ordering (RIGHT TO LEFT)
- [ ] Build Hamiltonians with SparsePauliOp
- [ ] Know Bell state expectations (ZZ=XX=+1, YY=-1)
- [ ] Implement complete VQE loop
- [ ] Know VQE components: Ansatz + Hamiltonian + Estimator + Optimizer
- [ ] Write a cost function for VQE

---
# Section 7: Results (10%)

---

## 7.1 Result Extraction
> Source: `section_7_results/result_extraction.ipynb`

### 🧠 Conceptual Deep Dive

**Results = Survey Analysis:**
- Raw result object = pile of survey forms
- Counts (Sampler) = tallying answers
- Expectation (Estimator) = calculating mean

**PubResult (Primitive Unified Bloc):**
- Standardized envelope holding data + metadata
- Access via `result[0].data`

### ✅ Key Takeaways

**Sampler Result Pattern:**
```python
# MEMORIZE THIS!
counts = result[0].data.meas.get_counts()
# Returns: {'00': 512, '11': 512}
```

**Result Structure (Sampler):**
```
result
  └─[0]              # First circuit
     └─.data
        └─.meas      # Register name
           ├─.get_counts()      → dict
           ├─.get_bitstrings()  → list
           └─.get_int_counts()  → dict
```

**Estimator Result Pattern:**
```python
# MEMORIZE THIS!
expectation = result[0].data.evs
std = result[0].data.stds
# evs and stds are PROPERTIES (no parentheses!)
```

**Result Structure (Estimator):**
```
result
  └─[0]              # First PUB
     └─.data
        ├─.evs       → float
        └─.stds      → float
```

### 🚨 Critical Exam Facts

- ✅ ALWAYS index result: `result[0]` not `result`
- ✅ ALWAYS access `.data`
- ✅ Sampler: `.get_counts()` is a METHOD (needs `()`)
- ✅ Estimator: `.evs` is a PROPERTY (no `()`)
- ✅ Register name: `.meas` (measure_all) or `.c` (custom ClassicalRegister)
- ✅ Multiple circuits: `result[i]` for each

### 📋 Exam Patterns

**Pattern 1: "Extract Sampler counts?"**
```python
# ❌ ALL WRONG
result.get_counts()              # Missing [0]
result[0].get_counts()           # Missing .data
result[0].data.get_counts()      # Missing register
result[0].data.meas.counts()     # Wrong method

# ✅ CORRECT
result[0].data.meas.get_counts()
```

**Pattern 2: "Extract Estimator value?"**
```python
# ❌ WRONG
result[0].data.evs()  # evs is property, not method!
result[0].evs         # Missing .data

# ✅ CORRECT
result[0].data.evs    # No parentheses!
```

**Pattern 3: "Memory Aid?"**
```
"Really Intelligent Developers Memorize Gatterns"
R-esult → I-ndex → D-ata → M-eas → G-et_counts()
```

---

# Section 8: OpenQASM (6%)

---

## 8.1 OpenQASM Operations
> Source: `section_8_openqasm/openqasm_operations.ipynb`

### 🧠 Conceptual Deep Dive

**OpenQASM = Blueprint Format:**
- Circuit object = 3D model in architect software
- OpenQASM = printed 2D blueprints (text)
- Portable: any simulator/hardware can read it

**QASM = Quantum Assembly Language:**
- Low-level, portable text representation
- Standard interchange format

**Two Versions:**
- **OpenQASM 2.0**: Legacy standard, widely supported
- **OpenQASM 3.0**: Modern standard with advanced features (loops, conditionals, real-time control)

### ✅ Key Takeaways

#### OpenQASM 2.0 (Default)

**Export to QASM (Instance Method):**
```python
# Instance method - call on circuit object
qasm_string = qc.qasm()  # Default: QASM 2.0
```

**QASM 2.0 Output Structure:**
```
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
h q[0];
cx q[0],q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
```

**Import from QASM 2.0 (STATIC Methods!):**
```python
# ✅ CORRECT - Static method on CLASS
qc = QuantumCircuit.from_qasm_str(qasm_string)
qc = QuantumCircuit.from_qasm_file('circuit.qasm')

# ❌ WRONG - NOT instance methods!
qc = QuantumCircuit(2)
qc.from_qasm_str(qasm_string)  # AttributeError!
```

**File I/O Pattern:**
```python
# Save
with open('circuit.qasm', 'w') as f:
    f.write(qc.qasm())

# Load (STATIC!)
qc = QuantumCircuit.from_qasm_file('circuit.qasm')
```

#### OpenQASM 3.0 (Modern Features)

**Export to QASM 3.0:**
```python
from qiskit import qasm3

# Export circuit to QASM 3.0 string
qasm3_string = qasm3.dumps(qc)

# Alternative: instance method
qasm3_string = qc.qasm3()
```

**QASM 3.0 Output Structure:**
```
OPENQASM 3;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
cx q[0], q[1];
c[0] = measure q[0];
c[1] = measure q[1];
```

**Import from QASM 3.0:**
```python
from qiskit import qasm3

# Load from QASM 3.0 string
qc = qasm3.loads(qasm3_string)

# Load from QASM 3.0 file
with open('circuit_v3.qasm', 'r') as f:
    qc = qasm3.load(f)
```

**QASM 3.0 Advanced Features:**
```python
# Classical control flow (if statements)
qasm3_code = """
OPENQASM 3;
include "stdgates.inc";
qubit[2] q;
bit[2] c;
h q[0];
c[0] = measure q[0];
if (c[0] == 1) {
    x q[1];
}
"""
qc = qasm3.loads(qasm3_code)

# Real-time measurement feedback
# Loops and advanced control structures
# Better type system
```
##### Custom Exporter

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

**Key Differences: QASM 2.0 vs 3.0:**

| Feature | QASM 2.0 | QASM 3.0 |
|---------|----------|----------|
| **Syntax** | `qreg q[2];` | `qubit[2] q;` |
| **Include** | `qelib1.inc` | `stdgates.inc` |
| **Measure** | `measure q[0] -> c[0];` | `c[0] = measure q[0];` |
| **If statements** | ❌ Limited | ✅ Full support |
| **Loops** | ❌ No | ✅ for/while loops |
| **Export method** | `qc.qasm()` | `qc.qasm3()` or `qasm3.dumps(qc)` |
| **Import method** | `QuantumCircuit.from_qasm_str()` | `qasm3.loads()` |
| **Real-time control** | ❌ No | ✅ Yes |

**When to Use Each:**
- **QASM 2.0**: Maximum compatibility, simple circuits, legacy systems
- **QASM 3.0**: Advanced features, dynamic circuits, modern hardware

### 🚨 Critical Exam Facts

**QASM 2.0 (Default):**
- ✅ `qasm()` is INSTANCE method: `qc.qasm()`
- ✅ `from_qasm_str()` is STATIC: `QuantumCircuit.from_qasm_str()`
- ✅ `from_qasm_file()` is STATIC: `QuantumCircuit.from_qasm_file()`
- ✅ **THIS IS THE #1 EXAM TRAP in Section 8!**

**QASM 3.0 (Modern):**
- ✅ Export: `qc.qasm3()` or `qasm3.dumps(qc)`
- ✅ Import: `qasm3.loads(qasm3_string)` or `qasm3.load(file)`
- ✅ Different syntax: `qubit[2] q;` not `qreg q[2];`
- ✅ Supports if statements, loops, real-time control
- ✅ Measurement syntax: `c[0] = measure q[0];` (assignment style)

**Version Comparison:**
- ✅ Default export is QASM 2.0 via `qc.qasm()`
- ✅ QASM 3.0 has more features but different import module
- ✅ QASM 2.0 uses `QuantumCircuit.from_qasm_str()` (static)
- ✅ QASM 3.0 uses `qasm3.loads()` (function from qiskit.qasm3)

### 📋 Exam Patterns

**Pattern 1: "Export to QASM?"**
```python
# QASM 2.0 (default)
qasm_str = qc.qasm()  # Instance method ✅

# QASM 3.0
qasm3_str = qc.qasm3()  # Instance method ✅
# OR
from qiskit import qasm3
qasm3_str = qasm3.dumps(qc)  # Function ✅
```

**Pattern 2: "Load from QASM string?"**
```python
# ❌ WRONG - Most common mistake!
qc = QuantumCircuit(2)
qc.from_qasm_str(qasm_str)

# ✅ CORRECT - Static method for QASM 2.0!
qc = QuantumCircuit.from_qasm_str(qasm_str)

# ✅ CORRECT - Function for QASM 3.0!
from qiskit import qasm3
qc = qasm3.loads(qasm3_str)
```

**Pattern 3: "What's wrong with this code?"**
```python
qc = QuantumCircuit(2)
new_qc = qc.from_qasm_str(qasm_string)  # ❌

# Answer: from_qasm_str is STATIC!
qc = QuantumCircuit.from_qasm_str(qasm_string)  # ✅
```

**Pattern 4: "Export and import QASM 3.0?"**
```python
from qiskit import qasm3

# Export
qasm3_string = qasm3.dumps(qc)
# OR
qasm3_string = qc.qasm3()

# Import
qc_loaded = qasm3.loads(qasm3_string)

# ❌ WRONG - Don't mix versions!
qc = QuantumCircuit.from_qasm_str(qasm3_string)  # May fail!
```

**Pattern 5: "Identify QASM version?"**
```python
# QASM 2.0 starts with:
# OPENQASM 2.0;
# include "qelib1.inc";
# qreg q[2];

# QASM 3.0 starts with:
# OPENQASM 3;
# include "stdgates.inc";
# qubit[2] q;
```

**Pattern 6: "Memory Aid?"**
```
"FROM needs NO OBJECT, QASM3 needs IMPORT"
- from_qasm_str() = static method, no instance needed (QASM 2.0)
- from_qasm_file() = static method, no instance needed (QASM 2.0)
- qasm() = instance method, needs existing circuit (QASM 2.0)
- qasm3.loads() = function, needs import (QASM 3.0)
- qasm3.dumps() = function, needs import (QASM 3.0)
```

---

# Section 9: Quantum Information (3%)

---

## 9.1 Clifford Circuits
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**The Simulatable Club:**
- **Clifford gates**: A special set of gates {H, S, CNOT, X, Y, Z, S†} that can be efficiently simulated on classical computers
- **T gate**: NOT Clifford - once you add T, you leave the realm of efficient classical simulation
- **Gottesman-Knill theorem**: Clifford circuits can be simulated classically even with millions of qubits

**The Quality Control Analogy:**
- Manufacturing Plant = Quantum Computer
- Product Blueprint = Ideal Circuit/Gate
- Actual Product = Noisy Implementation
- Quality Inspector = Quantum Info Tools

### ✅ Key Takeaways

#### Clifford Gate Set (MEMORIZE!)

**Clifford gates**: {H, S, S†, CNOT, X, Y, Z}

```python
from qiskit.quantum_info import Clifford
from qiskit import QuantumCircuit

# Create Clifford from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)  # Bell state preparation
cliff = Clifford(qc)

# Check equivalence
cliff1 = Clifford(circuit1)
cliff2 = Clifford(circuit2)
print(cliff1 == cliff2)  # Direct comparison works

# Convert back to circuit
equivalent_circuit = cliff.to_circuit()

# Compose Cliffords
composed = cliff1.compose(cliff2)
```

### ⚠️ EXAM TRAP #1: T Gate is Clifford

**CRITICAL - Most Common Trap!**

```python
# ❌ WRONG - T gate is NOT Clifford!
qc = QuantumCircuit(1)
qc.h(0)
qc.t(0)  # T gate breaks Clifford property!
# cliff = Clifford(qc)  # This will FAIL!

# ✅ CORRECT - S gate IS Clifford
qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)  # S gate is Clifford ✓
cliff = Clifford(qc)  # Works!
```

**Mnemonic**: **"HSCP - No T!"** (H, S, CNOT, Paulis - but NOT T!)

### 🚨 Critical Exam Facts

- ✅ Clifford set: {H, S, S†, CNOT, X, Y, Z} - efficiently simulatable
- ✅ **T gate is NOT Clifford** (most tested trap!)
- ✅ T gate needed for universality (non-Clifford)
- ✅ Clifford circuits can simulate millions of qubits classically
- ✅ Used in randomized benchmarking and error correction

---

## 9.2 Operator Class
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**The Full Recipe:**
- Circuit = cooking instructions (steps)
- Operator = complete mathematical formula (transformation matrix)
- Stores full $2^n \times 2^n$ complex matrix for n-qubit operation

### ✅ Key Takeaways

```python
from qiskit.quantum_info import Operator
from qiskit import QuantumCircuit

# Create from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
op = Operator(qc)

# Get unitary matrix
print(op.data)  # numpy 4×4 array

# Check equivalence (up to global phase!)
op1 = Operator(circuit1)
op2 = Operator(circuit2)
print(op1.equiv(op2))  # ✅ Use .equiv() not ==

# Compose operators
combined = op1.compose(op2)  # op2 first, then op1!

# Tensor product
tensor = op1.tensor(op2)  # op1 ⊗ op2
```

### ⚠️ EXAM TRAP #2: Using == Instead of .equiv()

```python
# ❌ WRONG - Returns False due to global phase
print(op1 == op2)  # Strict matrix equality

# ✅ CORRECT - Returns True (same physics)
print(op1.equiv(op2))  # Phase-invariant comparison
```

**Mnemonic**: **"EQUIV for EQUIValent physics"**

### ⚠️ EXAM TRAP #3: Compose Order

```python
# Compose order is COUNTERINTUITIVE (like matrix multiplication)
# op1.compose(op2) = op1 × op2 = op2 applied FIRST!

h_op = Operator(HGate())
x_op = Operator(XGate())

# To apply H first, then X:
result = x_op.compose(h_op)  # ✅ h_op first, then x_op
```

**Mnemonic**: **"Compose = Right to Left"** (like matrix multiplication)

### 🚨 Critical Exam Facts

- ✅ Use `.equiv()` not `==` for circuit equivalence checking
- ✅ `.equiv()` ignores global phase (physically meaningful comparison)
- ✅ Compose order: `op1.compose(op2)` applies op2 first
- ✅ Operator stores full $2^n \times 2^n$ matrix

---

## 9.3 Statevector and DensityMatrix
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**Pure vs Mixed States:**
- **Statevector**: Pure states only (perfect quantum state)
- **DensityMatrix**: Pure + Mixed states (includes classical uncertainty)

**The Complete Picture vs Snapshot:**
- Statevector = Perfect photograph of single quantum state
- DensityMatrix = Blurry photo (mixture of different states)

### ✅ Key Takeaways

#### Statevector (Pure States Only)

```python
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

# Create from label
sv = Statevector.from_label('0')  # |0⟩
sv_plus = Statevector.from_label('+')  # |+⟩

# Create from circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
bell_state = Statevector.from_instruction(qc)

# Get probabilities
probs = bell_state.probabilities()
print(probs)  # [0.5, 0, 0, 0.5] for Bell state

# Evolve with operator
from qiskit.quantum_info import Operator
evolved = sv.evolve(Operator.from_label('X'))
```

#### DensityMatrix (Pure + Mixed States)

```python
from qiskit.quantum_info import DensityMatrix
import numpy as np

# Create from Statevector
sv = Statevector.from_label('+')
rho_plus = DensityMatrix(sv)  # Pure state

# Create maximally mixed state (classical mixture!)
mixed = DensityMatrix(np.eye(2) / 2)  # I/2

# Check purity
print(rho_plus.purity())  # 1.0 (pure state)
print(mixed.purity())  # 0.5 (mixed state)

# Key: Tr(ρ²) = 1 for pure, < 1 for mixed
```

### ⚠️ EXAM TRAP #4: Superposition ≠ Mixture

**CRITICAL DISTINCTION!**

```python
# |+⟩ = SUPERPOSITION (pure state, purity = 1)
plus = Statevector.from_label('+')  
# This is NOT a 50/50 mixture! It's coherent superposition with interference

# 50/50 MIXTURE (mixed state, purity = 0.5)
# Must use DensityMatrix!
mixed = DensityMatrix(np.array([[0.5, 0], [0, 0.5]]))

# The difference: PURITY
print(f"|+⟩ purity: {DensityMatrix(plus).purity()}")  # 1.0 (pure)
print(f"Mixture purity: {mixed.purity()}")  # 0.5 (mixed)
```

**Mnemonic**: **"DM for Dirty/Mixed, SV for Single/Pure"**

### 🚨 Critical Exam Facts

- ✅ Statevector: Pure states only (coherent superposition)
- ✅ DensityMatrix: Can represent both pure and mixed states
- ✅ Purity: Tr(ρ²) = 1 for pure, < 1 for mixed
- ✅ Superposition ≠ Mixture! |+⟩ is pure (purity=1)
- ✅ Normalization: $\sum_i |a_i|^2 = 1$ for valid quantum states

---

## 9.4 Fidelity Measures
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**Similarity Score:**
- Fidelity measures how close two quantum states are
- Range: [0, 1] where 1 = identical, 0 = orthogonal
- For pure states: $F = |\langle\psi|\phi\rangle|^2$

### ✅ Key Takeaways

```python
from qiskit.quantum_info import state_fidelity, Statevector

# Compare two states
state1 = Statevector.from_label('0')
state2 = Statevector.from_label('+')

fid = state_fidelity(state1, state2)
print(f"Fidelity: {fid}")  # 0.5

# Identical states
same_fid = state_fidelity(state1, state1)
print(f"Same state: {same_fid}")  # 1.0

# Orthogonal states
state3 = Statevector.from_label('1')
ortho_fid = state_fidelity(state1, state3)
print(f"Orthogonal: {ortho_fid}")  # 0.0
```

**Fidelity Interpretation:**

| Fidelity | Quality | Interpretation |
|----------|---------|----------------|
| 0.99+ | Excellent | High-quality gate/state |
| 0.95-0.99 | Good | Acceptable for most applications |
| 0.90-0.95 | Moderate | May need error mitigation |
| < 0.90 | Poor | Significant noise present |
| 0.5 | Random | No correlation (for qubits) |
| 0.0 | Orthogonal | Completely different states |

### ⚠️ EXAM TRAP #5: Fidelity Can Exceed 1

```python
# ❌ WRONG - "High fidelity might be 1.5 or 2.0"
# Fidelity is ALWAYS between 0 and 1!

# ✅ CORRECT
assert 0 <= fid <= 1  # Always true!
```

**Mnemonic**: **"Fidelity = Faithful to [0,1]"**

### Process and Average Gate Fidelity

```python
from qiskit.quantum_info import process_fidelity, average_gate_fidelity, Operator

# Compare ideal vs noisy operation
ideal_gate = Operator.from_label('X')
noisy_gate = Operator(noisy_circuit)

# Process fidelity
proc_fid = process_fidelity(noisy_gate, ideal_gate)

# Average gate fidelity (standard metric for gate quality)
avg_fid = average_gate_fidelity(noisy_gate, ideal_gate)
```

### 🚨 Critical Exam Facts

- ✅ Fidelity range: **ALWAYS [0, 1]**, never exceeds 1
- ✅ 1 = identical states, 0 = orthogonal states
- ✅ Average gate fidelity is the standard metric for gate quality
- ✅ |0⟩ and |1⟩ are orthogonal → fidelity = 0
- ✅ |0⟩ and |+⟩ → fidelity = 0.5

---

## 9.5 Quantum Channels
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**Three Views of the Same Noise:**
- Like describing weather as temperature/humidity/pressure
- Kraus/SuperOp/Choi are different representations of same quantum noise

### ✅ Key Takeaways

**Three Channel Representations:**

```python
from qiskit.quantum_info import Kraus, SuperOp, Choi
import numpy as np

# Kraus: Sum of operators ρ → Σₖ Kₖ ρ Kₖ†
# Best for understanding physics

# SuperOp: Matrix on vectorized density matrix
# Best for mathematical manipulation

# Choi: Channel applied to maximally entangled state
# Best for tomography

# They're all equivalent - convert between them:
channel = Kraus(kraus_ops)
superop = SuperOp(channel)
choi = Choi(channel)
```

**Common Noise Channels:**

| Channel | Effect | Use Case |
|---------|--------|----------|
| Depolarizing | Random Pauli errors | General noise model |
| Amplitude Damping | Energy relaxation (T1) | Spontaneous emission |
| Phase Damping | Dephasing (T2) | Loss of coherence |
| Bit Flip | X errors with probability p | Simple error model |
| Phase Flip | Z errors with probability p | Simple error model |

**Mnemonic**: **"KSC = Know, Solve, Check"**
- **K**raus: Know the physics
- **S**uperOp: Solve mathematically
- **C**hoi: Check properties

### 🚨 Critical Exam Facts

- ✅ Three equivalent representations: Kraus, SuperOp, Choi
- ✅ Kraus best for physics intuition
- ✅ Can convert between all three
- ✅ Depolarizing channel applies random Pauli errors

---

## 9.6 Randomized Benchmarking
> Source: `section_9_quantum_info/quantum_info_advanced.ipynb`

### 🧠 Conceptual Deep Dive

**Stress Test for Gates:**
- Apply many random Clifford operations
- Then undo them all with inverse
- If gates are perfect, you get back to start
- Error rate tells you how much "drift" accumulates

### ✅ Key Takeaways

```python
from qiskit_experiments.library import StandardRB
from qiskit_ibm_runtime import QiskitRuntimeService

# Setup backend
service = QiskitRuntimeService()
backend = service.backend('ibm_brisbane')

# Create RB experiment
rb_exp = StandardRB(
    physical_qubits=[0],           # Which qubit(s)
    lengths=[1, 10, 20, 50, 100],  # Sequence lengths
    num_samples=10,                # Circuits per length
    seed=42
)

# Run and extract Error Per Clifford (EPC)
rb_data = rb_exp.run(backend).block_for_results()
epc = rb_data.analysis_results('EPC').value
print(f"Error per Clifford: {epc:.4f}")

# Good values: EPC < 0.01 (1%)
```

**RB Protocol:**
1. Prepare |0⟩
2. Apply random Cliffords: C₁ → C₂ → ... → Cₘ
3. Apply inverse: C_inv = (Cₘ...C₂C₁)⁻¹
4. Measure (should return |0⟩ if no errors)
5. Repeat for different sequence lengths
6. Fit exponential decay → extract EPC

### ⚠️ EXAM TRAP #6: RB Measures SPAM Errors

```python
# ❌ WRONG - RB does NOT measure SPAM errors
# RB is specifically designed to be SPAM-free!

# ✅ CORRECT - RB isolates GATE errors only
# The inverse operation cancels SPAM effects
```

**Mnemonic**: **"RB = Really 'Bout Gates (not SPAM)"**

### 🚨 Critical Exam Facts

- ✅ RB is **SPAM-free** (no state prep or measurement errors)
- ✅ Uses only Clifford gates (efficiently implementable)
- ✅ EPC (Error Per Clifford) < 0.01 is good
- ✅ Inverse operation cancels SPAM effects
- ✅ Measures average gate error rate

---

### 🎓 Section 9 Complete Checklist

Before moving on, make sure you can:
- [ ] Know Clifford gates: {H, S, CNOT, X, Y, Z} - T is NOT Clifford!
- [ ] Use `Operator.equiv()` not `==` for circuit equivalence
- [ ] Understand compose order: `op1.compose(op2)` applies op2 first
- [ ] Know Statevector is for pure states only
- [ ] Use DensityMatrix for mixed states (purity < 1)
- [ ] Understand superposition ≠ mixture (|+⟩ is pure!)
- [ ] Know fidelity range is ALWAYS [0, 1]
- [ ] Calculate state_fidelity between two states
- [ ] Know three channel representations: Kraus, SuperOp, Choi
- [ ] Understand RB is SPAM-free (measures gate errors only)

---

# 🎯 Master Exam Checklist

## Before the Exam, Verify You Can:

### Section 1 - Quantum Operations (16%)
- [ ] Create superposition with H gate
- [ ] Build Bell state (H + CNOT)
- [ ] Explain Pauli gates (X, Y, Z) and their effects
- [ ] Use rotation gates (RX, RY, RZ) with parameters
- [ ] Understand phase gates (S, T) relationships: S=√Z, T=√S
- [ ] Explain CNOT direction: `qc.cx(control, target)`
- [ ] Know CZ is symmetric but CNOT is not
- [ ] Understand global vs relative phase

### Section 2 - Visualization (11%)
- [ ] Draw circuits: `qc.draw(output='mpl')` or `'text'`
- [ ] Use `plot_histogram(counts)` correctly
- [ ] Visualize states on Bloch sphere
- [ ] Get Statevector: `Statevector.from_instruction(qc)`

### Section 3 - Create Circuits (18% - HIGHEST!)
- [ ] Distinguish properties (`num_qubits`) from methods (`depth()`)
- [ ] Use `Parameter` and `ParameterVector`
- [ ] Use `assign_parameters()` correctly (returns NEW circuit!)
- [ ] Use `compose()` for sequential, `tensor()` for parallel
- [ ] Know `RealAmplitudes` parameters: `num_qubits × (reps + 1)`
- [ ] Compare `RealAmplitudes` vs `EfficientSU2`
- [ ] Use `QFTGate(n).inverse()` for inverse QFT

### Section 4 - Run Circuits (15%)
- [ ] Choose correct optimization level (0-3)
- [ ] Know defaults: transpile=1, Options=2
- [ ] Configure Options correctly: `options.execution.shots = 4096`
- [ ] Know `resilience_level` is TOP-LEVEL, not nested
- [ ] Use V2 backend API (`operation_names`, `target`)
- [ ] Use Session for VQE: `Sampler(session=session)`
- [ ] Use Batch for independent parallel circuits

### Section 5 - Sampler (12%)
- [ ] Extract counts: `result[0].data.meas.get_counts()`
- [ ] Remember circuits NEED measurements
- [ ] Use correct register name (`.meas` vs `.c`)
- [ ] Bind parameters BEFORE running Sampler

### Section 6 - Estimator & VQE (12%)
- [ ] Define Hamiltonians with `SparsePauliOp.from_list()`
- [ ] Know Pauli string ordering (right-to-left, little-endian)
- [ ] Extract expectation: `result[0].data.evs`
- [ ] Circuits should NOT have measurements
- [ ] Write VQE cost function pattern from memory

### Section 7 - Results (10%)
- [ ] Write `result[0].data.meas.get_counts()` from memory
- [ ] Write `result[0].data.evs` from memory
- [ ] Know `.evs` and `.stds` are PROPERTIES (no parentheses!)
- [ ] Distinguish Sampler vs Estimator result access

### Section 8 - OpenQASM (6%)
- [ ] Know `from_qasm_str()` is STATIC method
- [ ] Write `QuantumCircuit.from_qasm_str()` correctly
- [ ] Export with `qc.qasm()` (instance method)
- [ ] Know default is QASM 2.0

### Section 9 - Quantum Information (3%)
- [ ] Know Clifford gates: {H, S, CNOT, X, Y, Z} - **T is NOT Clifford!**
- [ ] Use `Operator.equiv()` not `==` for equivalence checking
- [ ] Understand compose order is "right to left"
- [ ] Know Statevector for pure states, DensityMatrix for mixed
- [ ] Remember superposition ≠ mixture (|+⟩ is pure, purity=1)
- [ ] Know fidelity range is ALWAYS [0, 1], never exceeds 1
- [ ] Use `state_fidelity()` to compare quantum states
- [ ] Know channel representations: Kraus/SuperOp/Choi
- [ ] Understand RB is SPAM-free (gate errors only)

---

# 🧠 Memory Aids & Mnemonics

## Properties vs Methods
**"Numbers are PROPERTIES, Actions are METHODS"**
- `qc.num_qubits` - noun, no action → PROPERTY (no `()`)
- `qc.depth()` - verb, computing → METHOD (needs `()`)

## Optimization Levels
**"0=Debug, 1=Fast, 2=Default, 3=Best"**
- Level 0: Zero optimization (debugging)
- Level 1: One quick pass (transpile default)
- Level 2: Two-way analysis (Options default)
- Level 3: Three+ aggressive strategies

## Result Extraction
**"Really Intelligent Developers Memorize Gatterns"**
- **R**esult → `result`
- **I**ndex → `[0]`
- **D**ata → `.data`
- **M**eas → `.meas`
- **G**et → `.get_counts()`

Full pattern: `result[0].data.meas.get_counts()`

## OpenQASM
**"FROM needs NO OBJECT"**
- Export: `qc.qasm()` (easy, instance method)
- Import: `QuantumCircuit.from_qasm_str()` (CLASS method, no instance)

## Sampler vs Estimator
**"Sampler Sees (measurements), Estimator Expects (no measurements)"**
- **S**ampler = **S**ample bitstrings (WITH measurements)
- **E**stimator = **E**stimate ⟨O⟩ (NO measurements)

## Transpilation
**"Transpile = Translate + Optimize"**

## Options
**"Options = Optimization + Resilience + Shots"**
- `optimization_level` - top level
- `resilience_level` - top level (NOT nested!)
- `execution.shots` - nested

## CNOT Direction
**"Control BEFORE Target"**
- `qc.cx(control, target)`
- First parameter = control qubit
- Second parameter = target qubit

## Pauli Strings
**"Read RIGHT to LEFT"**
- `'ZX'` = Z on q0, X on q1
- `'XYZ'` = X on q0, Y on q1, Z on q2

## Circuit Composition
**"compose = sequential, tensor = parallel"**
- `compose()` - same qubits, gates added after (time)
- `tensor()` - more qubits, side by side (space)

## VQE Components
**"AHEM" = Ansatz, Hamiltonian, Estimator, Minimize**
1. **A**nsatz - parameterized circuit
2. **H**amiltonian - SparsePauliOp observable
3. **E**stimator - computes ⟨H⟩
4. **M**inimize - scipy.optimize

---

# ⚡ Last-Minute Quick Reference

## Top 10 Most Common Exam Traps

### 1. Property vs Method
```python
qc.num_qubits    # ✅ Property - NO ()
qc.num_qubits()  # ❌ Error! 'int' object not callable
qc.depth()       # ✅ Method - needs ()
qc.depth         # ❌ Returns function object, not value
```

### 2. OpenQASM Import (STATIC!)
```python
QuantumCircuit.from_qasm_str(s)  # ✅ STATIC method on CLASS
qc.from_qasm_str(s)              # ❌ Instance method doesn't exist!
```

### 3. Result Extraction - Sampler
```python
result[0].data.meas.get_counts()  # ✅ Complete path
result.get_counts()               # ❌ Missing [0]
result[0].get_counts()            # ❌ Missing .data
result[0].data.get_counts()       # ❌ Missing register name
```

### 4. Result Extraction - Estimator
```python
result[0].data.evs   # ✅ Property, no ()
result[0].data.evs() # ❌ Not callable
result[0].evs        # ❌ Missing .data
```

### 5. Default Values
```python
options.execution.shots = 4096     # ✅ Default (not 1024!)
transpile() optimization_level = 1 # ✅ transpile default
Options() optimization_level = 2   # ✅ Options default (different!)
```

### 6. V2 vs V1 Backend API
```python
backend.operation_names            # ✅ V2 API
backend.target                     # ✅ V2 API
backend.configuration().basis_gates # ❌ V1 deprecated
```

### 7. Sampler vs Estimator Requirements
```python
# Sampler - NEEDS measurements
qc.measure_all()
sampler.run([qc])  # ✅

# Estimator - NO measurements
# Don't add measure_all()!
estimator.run([(qc, observable)])  # ✅
```

### 8. assign_parameters() Returns NEW Circuit
```python
qc.assign_parameters({theta: 0.5})  # ❌ Original unchanged!
bound = qc.assign_parameters({theta: 0.5})  # ✅ Capture return
```

### 9. resilience_level is TOP-LEVEL
```python
options.resilience_level = 1     # ✅ Correct
options.resilience.level = 1     # ❌ Wrong - not nested!
options.execution.shots = 4096   # ✅ This one IS nested
```

### 10. Session Parameter
```python
with Session(backend=backend) as session:
    sampler = Sampler(session=session)  # ✅ Use session
    sampler = Sampler(backend=backend)  # ❌ Don't use backend
```

---

## Quick Decision Trees

### Which Primitive?
```
Need measurement counts? → Sampler (WITH measurements)
Need expectation value?  → Estimator (NO measurements)
```

### Which Optimization Level?
```
Debugging/testing?     → 0
Quick prototyping?     → 1 (transpile default)
Production code?       → 2 (Options default)
Critical experiment?   → 3 (best quality)
```

### Which Execution Mode?
```
Single job?                    → Direct run
Multiple independent circuits? → Batch
Iterative algorithm (VQE)?     → Session
```

---

## Exam Day Checklist

### Before Starting
- [ ] Read questions carefully (watch for "NOT" or "EXCEPT")
- [ ] Flag difficult questions, return later
- [ ] 1.5 minutes per question average

### Result Pattern (Write 3x)
```python
# Sampler
result[0].data.meas.get_counts()

# Estimator
result[0].data.evs
```

### OpenQASM Pattern (Write 3x)
```python
# Export (instance)
qasm_str = qc.qasm()

# Import (STATIC!)
qc = QuantumCircuit.from_qasm_str(qasm_str)
```

---

# 🎓 Final Exam Tips

## Time Management
- 60 questions in 90 minutes = 1.5 minutes per question
- Flag difficult questions and return later
- Don't spend >3 minutes on any single question

## Strategy
1. **First pass**: Answer all questions you're confident about
2. **Second pass**: Tackle flagged questions
3. **Final pass**: Educated guesses on remaining

## Day Before
- Review this notebook's "Critical Exam Facts" sections
- Review "Quick Reference" section
- Don't learn new concepts - reinforce what you know
- Get good sleep!

## During Exam
- Read questions carefully (watch for "NOT" or "EXCEPT")
- Look for keywords: "V2 API", "deprecated", "STATIC", "property", "method"
- Remember the common traps documented here
- Trust your preparation!

---

## Section Weights Reference

| Section | Topic | Weight | Questions |
|---------|-------|--------|-----------|
| 1 | Quantum Operations | 16% | ~10 |
| 2 | Visualization | 11% | ~7 |
| 3 | Create Circuits | **18%** | ~11 |
| 4 | Run Circuits | 15% | ~9 |
| 5 | Sampler | 12% | ~7 |
| 6 | Estimator & VQE | 12% | ~7 |
| 7 | Results | 10% | ~6 |
| 8 | OpenQASM | 6% | ~4 |
| 9 | Advanced Topics | Bonus | Cross-cutting |

**Focus Areas**: Sections 3, 4, 1 (highest weight)
**Trap Areas**: Sections 7, 8 (result extraction, static methods)
**Advanced**: Section 9 (dynamic circuits, PassManager, job management)

---

## Pattern Summary Card

### Create
```python
qc = QuantumCircuit(n_qubits, n_clbits)
qc.num_qubits     # Property
qc.depth()        # Method
bound = qc.assign_parameters({theta: 0.5})
```

### Transpile
```python
transpiled = transpile(qc, backend, optimization_level=2)
```

### Sampler
```python
sampler = Sampler()
result = sampler.run([qc]).result()
counts = result[0].data.meas.get_counts()
```

### Estimator
```python
estimator = Estimator()
result = estimator.run([(qc, H)]).result()
energy = result[0].data.evs
```

### VQE
```python
def cost(params):
    qc = ansatz.assign_parameters(params)
    return estimator.run([(qc, H)]).result()[0].data.evs
```

### OpenQASM
```python
qasm_str = qc.qasm()  # Export (instance)
qc = QuantumCircuit.from_qasm_str(qasm_str)  # Import (STATIC!)
```

---

# 🚀 You've Got This!

**This revision guide covers ALL exam concepts systematically. Trust your preparation and good luck!** 🎯

---