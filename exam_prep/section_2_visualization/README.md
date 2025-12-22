# Section 2: Visualization (11% of Exam)

> **Exam Weight**: ~7 questions | **Difficulty**: Medium | **Must Master**: ✅✅

---

## 📖 Overview

This section covers all visualization capabilities in Qiskit: drawing circuits in multiple formats, visualizing quantum states on Bloch spheres and other representations, plotting measurement results, and understanding backend topology. Visualization is critical for debugging, learning, and presenting quantum algorithms.

### What You'll Learn

1. **Circuit Drawing**: Multiple output formats (text, mpl, latex) and customization options
2. **State Visualization**: Bloch sphere, state city, Q-sphere, Hinton, and Pauli vector plots
3. **Measurement Results**: Histograms and probability distributions from quantum runs
4. **Backend Topology**: Gate maps and coupling maps for hardware-aware design
5. **Dynamic Circuits**: Visualizing classical feedforward and conditional operations

---

## 🎯 Why This Section Matters (Conceptual Foundation)

### 🧠 Conceptual Deep Dive

#### Analogy: Musical Score vs Performance Recording

**Visualization is like having two types of musical documentation:**

- **Circuit diagram** = Musical score
  - Shows the instructions (notes/gates) in order
  - Static representation of what WILL happen
  - Different formats: simple text, detailed printed sheet, publication-quality

- **State visualization** = Sound wave display
  - Shows the CURRENT state of the quantum system
  - Dynamic - changes after each gate
  - Bloch sphere = individual note frequencies
  - State city/Q-sphere = full chord analysis

- **Histogram** = Recording playback
  - Shows what was MEASURED (heard)
  - Probabilistic - varies each performance
  - Counts = how many times each outcome occurred

### Key Mental Model: Statevector vs StatevectorSampler

```
┌─────────────────────────────────────────────────────────────────┐
│ Statevector = "What IS the quantum state?"                      │
│   • Mathematical description of the quantum system               │
│   • Returns: [0.707+0j, 0, 0, 0.707+0j]  (exact amplitudes)     │
│   • Like asking "What's inside Schrödinger's box?"               │
│   • ⚠️ Impossible on real hardware! (simulation only)            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ StatevectorSampler = "What would we MEASURE?"                   │
│   • Simulates the act of measuring the quantum system            │
│   • Returns: {'00': 512, '11': 488}  (measurement outcomes)      │
│   • Like asking "What do we see when we open the box?"           │
│   • ✅ Mimics real hardware behavior (useful for testing)        │
└─────────────────────────────────────────────────────────────────┘
```

### Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    VISUALIZATION DECISION TREE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  What do you want to visualize?                                  │
│                                                                  │
│  ├─ Circuit structure ──────► qc.draw(output='mpl')             │
│  │                                                               │
│  ├─ Quantum state ──────────► Need Statevector                  │
│  │   ├─ Single qubit ───────► plot_bloch_multivector()          │
│  │   ├─ Amplitudes ─────────► plot_state_city()                 │
│  │   ├─ Probabilities+Phase ► plot_state_qsphere()              │
│  │   ├─ Density matrix ─────► plot_state_hinton()               │
│  │   └─ Pauli decomposition ► plot_state_paulivec()             │
│  │                                                               │
│  ├─ Measurement counts ─────► Need counts dict                  │
│  │   ├─ Raw counts ─────────► plot_histogram()                  │
│  │   └─ Probabilities ──────► plot_distribution()               │
│  │                                                               │
│  └─ Backend topology ───────► plot_gate_map(backend)            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Topics Covered (Quick Reference)

| Topic | Description | Exam Weight | Priority |
|-------|-------------|-------------|----------|
| **qc.draw()** | Circuit diagrams in text/mpl/latex | High | 🔴 |
| **plot_bloch_multivector()** | Single-qubit states on Bloch sphere | High | 🔴 |
| **plot_state_city()** | 3D bar plot of amplitudes | Medium | 🟡 |
| **plot_histogram()** | Measurement count visualization | High | 🔴 |
| **plot_distribution()** | Normalized probability bars | Medium | 🟡 |
| **plot_gate_map()** | Backend qubit connectivity | Low | 🟢 |
| **Statevector vs Sampler** | When to use which tool | High | 🔴 |

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION 2 LEARNING PATH                       │
├─────────────────────────────────────────────────────────────────┤
│  START HERE                                                      │
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. CIRCUIT DRAWING                                           ││
│  │    └─ qc.draw() with text/mpl/latex                         ││
│  │    └─ Styling and parameters                                 ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 2. STATE VISUALIZATION                                       ││
│  │    └─ Statevector class                                     ││
│  │    └─ Bloch sphere, City, Q-sphere, Hinton, Paulivec        ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 3. MEASUREMENT VISUALIZATION                                 ││
│  │    └─ StatevectorSampler for counts                         ││
│  │    └─ plot_histogram vs plot_distribution                   ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 4. BACKEND & DYNAMIC CIRCUITS                                ││
│  │    └─ plot_gate_map, plot_coupling_map                      ││
│  │    └─ if_test control flow visualization                    ││
│  └─────────────────────────────────────────────────────────────┘│
│      ↓                                                          │
│  COMPLETE: Ready for Visualization exam questions                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Circuit Drawing

> **STRUCTURE**: Learn qc.draw() output formats and customization
> **LEARNING FLOW**: Each sub-topic has 7 elements (learn → trap → mnemonic → test)

### Overview

Circuit drawing converts a QuantumCircuit into a visual representation. Three main output formats serve different purposes: text for terminals, matplotlib for notebooks/reports, LaTeX for publications.

---

### 🔹 qc.draw() - Basic Circuit Visualization

#### 1. Definition

`qc.draw()` renders a quantum circuit as a diagram. It supports multiple output formats and extensive customization for different use cases from quick debugging to publication-quality figures.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like choosing how to print a document:
- **text** = Plain text email (works everywhere, basic formatting)
- **mpl** = Word document with graphics (rich, interactive)
- **latex** = Professionally typeset PDF (publication-ready)

**Intuition Builder**: The circuit diagram is your primary debugging tool. You'll look at it constantly to verify your circuit is correct before running.

#### 3. Math + Visual

**Output Format Comparison**:
```
TEXT:                         MPL:                      LATEX:
     ┌───┐               ┌───┐                    ┌───┐
q_0: ┤ H ├──■──          │ H │──●──               │ H │──●──
     └───┘┌─┴─┐          └───┘  │                 └───┘  │
q_1: ─────┤ X ├──        ───────⊕──               ───────⊕──
          └───┘          
```

#### 4. Implementation (Basic → Advanced)

**Qiskit Syntax**:
```python
qc.draw(output='mpl')  # Returns matplotlib figure
```

**Parameters**:
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `output` | str | 'text', 'mpl', 'latex', 'latex_source' | 'text' |
| `reverse_bits` | bool | Put MSB on top (match physics convention) | False |
| `fold` | int | Columns before wrapping, -1 for no fold | None |
| `scale` | float | Scale factor for diagram | None |
| `style` | dict/str | Styling options ('iqp', 'bw', 'clifford') | None |
| `idle_wires` | bool | Show wires with no operations | True |
| `filename` | str | Save to file path | None |

**Basic Example**:
```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Simple text output (terminal-friendly)
print(qc.draw())  # Default: output='text'
```

**Intermediate Example**:
```python
# Matplotlib output with styling
fig = qc.draw(
    output='mpl',
    reverse_bits=True,  # MSB on top
    fold=20             # Wrap after 20 columns
)
```

**Advanced Example**:
```python
# Publication-quality with all options
qc.draw(
    output='mpl',
    reverse_bits=True,
    fold=-1,               # Never fold
    scale=1.5,             # 150% size
    idle_wires=False,      # Hide empty wires
    style={'backgroundcolor': '#FFFFFF'},
    filename='my_circuit.png'
)
```

#### 5. ⚠️ Trap Alert

> **LEARN THE TRAP NOW** - Don't let misconceptions form!

**Trap: Default is TEXT, not MPL**
- ❌ **Wrong**: Assuming `qc.draw()` returns a figure
- ✅ **Correct**: Default is text; use `qc.draw('mpl')` for figure
- 🔍 **Why it's tricky**: In notebooks, text still "works" but looks worse

```python
# ❌ WRONG - Won't display nicely in notebook
qc.draw()  # Returns text representation

# ✅ CORRECT - Rich graphical output
qc.draw('mpl')  # Returns matplotlib figure
```

**Trap: reverse_bits Convention**
- ❌ **Wrong**: Top wire is always qubit 0
- ✅ **Correct**: `reverse_bits=True` puts MSB (highest index) on top
- 🔍 **Why it's tricky**: Physics papers use opposite convention from Qiskit default

#### 6. 🧠 Mnemonic

> **LOCK IT IN NOW** - One memorable phrase

**"MPL for My Pretty Layout"**
- Meaning: When you want a nice visual, use `output='mpl'`
- Example: `qc.draw('mpl')` for notebooks and reports

**"Reverse Bits = Reading Order"**
- Meaning: `reverse_bits=True` makes |01⟩ read as qubit-0=0, qubit-1=1 (top to bottom)

#### 7. ⚡ Quick Check

> **TEST YOURSELF NOW** - Active recall within 30 seconds

**Q: What parameter makes the highest-indexed qubit appear at the TOP of the diagram?**

<details>
<summary>Answer</summary>

**A**: `reverse_bits=True`

```python
qc.draw(output='mpl', reverse_bits=True)
```

This matches the physics convention where MSB (most significant bit) is on top.
</details>

---

### 🔹 Output Styles and Formats

#### 1. Definition

Qiskit provides preset styles ('iqp', 'bw', 'clifford') and custom styling dictionaries to control colors, fonts, and layout of circuit diagrams.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like choosing a theme in presentation software:
- **iqp** = Default colorful theme (IBM Quantum colors)
- **bw** = Black & white (for printing/papers)
- **clifford** = Minimalist (emphasis on Clifford gates)

#### 3. Math + Visual

**Style Comparison**:
```
IQP Style:          BW Style:           Custom Style:
┌───┐              ┌───┐               ┌───┐
│ H │ (blue)       │ H │ (black)       │ H │ (your color)
└───┘              └───┘               └───┘
```

#### 4. Implementation (Basic → Advanced)

**Built-in Styles**:
```python
# IQP style (default IBM Quantum look)
qc.draw(output='mpl', style='iqp')

# Black and white (for papers)
qc.draw(output='mpl', style='bw')

# Clifford style
qc.draw(output='mpl', style='clifford')
```

**Custom Style Dictionary**:
```python
custom_style = {
    'backgroundcolor': '#FFFFFF',
    'linecolor': '#000000',
    'textcolor': '#000000',
    'gatetextcolor': '#000000',
    'subfontsize': 10,
    'showindex': True
}
qc.draw(output='mpl', style=custom_style)
```

#### 5. ⚠️ Trap Alert

**Trap: Style Only Works with MPL**
- ❌ **Wrong**: `qc.draw(style='iqp')` - doesn't work with text output
- ✅ **Correct**: `qc.draw(output='mpl', style='iqp')`
- 🔍 **Why it's tricky**: Text output ignores style parameter silently

```python
# ❌ WRONG - style ignored for text
qc.draw(style='iqp')  # Still text output!

# ✅ CORRECT - must specify mpl
qc.draw(output='mpl', style='iqp')
```

#### 6. 🧠 Mnemonic

**"Style needs MPL as its canvas"**
- Meaning: Styling only applies to matplotlib output
- Example: Always pair `style=` with `output='mpl'`

#### 7. ⚡ Quick Check

**Q: What output format must you use to apply circuit styling?**

<details>
<summary>Answer</summary>

**A**: `output='mpl'` (matplotlib)

Styles like 'iqp', 'bw', 'clifford' only work with matplotlib output, not text or latex.
</details>

---

## 📊 Circuit Drawing - Consolidated Review

### Comparison Table

| Aspect | text | mpl | latex |
|--------|------|-----|-------|
| **Use Case** | Terminal/debugging | Notebooks/reports | Publications |
| **Syntax** | `qc.draw()` | `qc.draw('mpl')` | `qc.draw('latex')` |
| **Styling** | ❌ None | ✅ Full support | Limited |
| **Interactive** | ❌ No | ✅ Yes | ❌ No |
| **Dependencies** | None | matplotlib | pdflatex |

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ CIRCUIT DRAWING - QUICK REFERENCE                               │
├─────────────────────────────────────────────────────────────────┤
│ qc.draw()           - Text output (default, terminal)           │
│ qc.draw('mpl')      - Matplotlib figure (notebooks)             │
│ qc.draw('latex')    - LaTeX rendering (papers)                  │
├─────────────────────────────────────────────────────────────────┤
│ KEY PARAMETERS:                                                 │
│ • reverse_bits=True - MSB on top (physics convention)           │
│ • fold=N            - Wrap after N columns                      │
│ • style='iqp'       - Apply style (mpl only)                    │
│ • filename='x.png'  - Save to file                              │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONICS:                                                      │
│ • "MPL for My Pretty Layout"                                    │
│ • "Reverse Bits = Reading Order"                                │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAPS:                                                      │
│ • Default is text, not mpl                                      │
│ • Style only works with mpl                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 State Visualization

> **STRUCTURE**: Visualizing quantum states (before measurement)
> **CRITICAL**: All state visualizations need `Statevector` (no measurements in circuit!)

### Overview

State visualization shows the quantum state of a circuit BEFORE measurement. Unlike classical computation, quantum states exist in superposition with complex amplitudes. Multiple visualization tools reveal different aspects: probability, phase, individual qubit states, and density matrix structure.

---

### 🔹 Statevector Class

#### 1. Definition

`Statevector` is a class from `qiskit.quantum_info` that represents the exact mathematical state of a quantum system as a vector of complex amplitudes. It provides complete quantum information including phase.

#### 2. Analogy + Intuition

**Real-World Analogy**: Statevector is like an X-ray machine that shows everything inside:
- You see ALL probabilities and phases
- But this "X-ray" only works in simulation - impossible on real hardware
- Once you measure (open the box), the full state is lost

**Intuition Builder**: Real quantum computers can't give you the statevector - measurement collapses it. Statevector is a simulator-only tool for understanding and debugging.

#### 3. Math + Visual

**Statevector Format**:
```
For a 2-qubit Bell state:
|ψ⟩ = (|00⟩ + |11⟩) / √2

Statevector.data = [0.707+0j, 0+0j, 0+0j, 0.707+0j]
                     |00⟩     |01⟩  |10⟩   |11⟩
```

#### 4. Implementation (Basic → Advanced)

**Basic Creation**:
```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# ⚠️ NO measurements in circuit!

state = Statevector(qc)
print(state.data)  # [0.707+0j, 0+0j, 0+0j, 0.707+0j]
```

**Key Methods**:
```python
# Get probabilities (|amplitude|²)
probs = state.probabilities()  # [0.5, 0, 0, 0.5]

# Check if states are equivalent
state1.equiv(state2)  # True if same up to global phase

# Draw the state
state.draw('bloch')  # Bloch representation
```

#### 5. ⚠️ Trap Alert

**Trap: Measurements Break Statevector**
- ❌ **Wrong**: Getting statevector from circuit WITH measurements
- ✅ **Correct**: Circuit must NOT have measurements
- 🔍 **Why it's tricky**: Statevector(qc_with_measurements) works but gives post-measurement state!

```python
# ❌ WRONG - measurements in circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure(0, 0)  # ❌ Measurement!
state = Statevector(qc)  # Gives collapsed state, not superposition!

# ✅ CORRECT - no measurements
qc = QuantumCircuit(2)
qc.h(0)
state = Statevector(qc)  # Clean quantum state
```

#### 6. 🧠 Mnemonic

**"No M before S" (No Measure before Statevector)**
- Meaning: Remove measurements before getting Statevector
- Example: Statevector needs a measurement-free circuit

#### 7. ⚡ Quick Check

**Q: If you want to see the exact quantum state including phase information, which class do you use?**

<details>
<summary>Answer</summary>

**A**: `Statevector` from `qiskit.quantum_info`

```python
from qiskit.quantum_info import Statevector
state = Statevector(qc)  # qc must have NO measurements!
```
</details>

---

### 🔹 plot_bloch_multivector()

#### 1. Definition

`plot_bloch_multivector()` visualizes a multi-qubit state by showing each qubit's reduced state on its own Bloch sphere. For entangled states, individual qubits appear as mixed states (inside the sphere, not on surface).

#### 2. Analogy + Intuition

**Real-World Analogy**: Like splitting a team photo into individual portraits:
- Each person (qubit) gets their own frame (Bloch sphere)
- For entangled qubits, the individual "portrait" looks blurry (mixed state)
- Pure single-qubit states are on the sphere surface; mixed states are inside

**Intuition Builder**: The Bloch sphere is the natural way to visualize a single qubit: poles are |0⟩ and |1⟩, equator is superpositions, and the arrow shows the state.

#### 3. Math + Visual

**Bloch Sphere Geometry**:
```
         |0⟩ (North pole)
          ↑
    |+⟩ ──●── |−⟩  (Equator = superpositions)
          ↓
         |1⟩ (South pole)

Single qubit |+⟩ = (|0⟩ + |1⟩)/√2:
Arrow points to equator (positive X direction)
```

**Visual for Entangled State**:
```
Bell state (|00⟩ + |11⟩)/√2:

Qubit 0:        Qubit 1:
   ↑               ↑
   ● (center)      ● (center)
   
Both show arrows at CENTER (mixed state)
because individual qubits are maximally entangled!
```

#### 4. Implementation (Basic → Advanced)

**Qiskit Syntax**:
```python
from qiskit.visualization import plot_bloch_multivector
plot_bloch_multivector(state)
```

**Parameters**:
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `state` | Statevector | Quantum state to visualize | Required |
| `title` | str | Plot title | '' |
| `figsize` | tuple | Figure size | None |
| `filename` | str | Save to file | None |

**Basic Example**:
```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.h(0)  # |+⟩ state

state = Statevector(qc)
plot_bloch_multivector(state)  # Shows arrow pointing to +X
```

**Multi-Qubit Example**:
```python
# Bell state
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector(qc)
plot_bloch_multivector(state)
# Shows 2 spheres, both with arrows at center (entangled!)
```

#### 5. ⚠️ Trap Alert

**Trap: Entangled Qubits Appear Mixed**
- ❌ **Wrong**: Expecting arrows on surface for Bell state
- ✅ **Correct**: Entangled qubits show arrows at center (mixed when viewed individually)
- 🔍 **Why it's tricky**: Students expect "pure" looking states, but entanglement changes individual qubit appearance

**Trap: Input Must Be Statevector, Not Counts**
- ❌ **Wrong**: `plot_bloch_multivector({'00': 50, '11': 50})`
- ✅ **Correct**: `plot_bloch_multivector(Statevector(qc))`

```python
# ❌ WRONG - can't use counts
counts = {'00': 500, '11': 500}
plot_bloch_multivector(counts)  # TypeError!

# ✅ CORRECT - use Statevector
state = Statevector(qc)
plot_bloch_multivector(state)
```

#### 6. 🧠 Mnemonic

**"Bloch for single-qubit soul"**
- Meaning: Bloch sphere shows each qubit's individual state
- Example: Use when you want to see what each qubit looks like

**"Center = Correlated (entangled)"**
- Meaning: Arrow at center of sphere indicates entanglement
- Example: Bell state shows both qubits with centered arrows

#### 7. ⚡ Quick Check

**Q: A Bell state is visualized with plot_bloch_multivector(). Where do the arrows point?**

<details>
<summary>Answer</summary>

**A**: At the center of each sphere (origin)

Entangled qubits have maximally mixed reduced density matrices. When viewed individually, they appear to be in a completely mixed state, so the arrow points to the center rather than the surface.
</details>

---

### 🔹 plot_state_city()

#### 1. Definition

`plot_state_city()` shows the density matrix as a 3D bar chart ("cityscape"), with bars representing the magnitude of each matrix element. Real and imaginary parts are shown separately.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like a city skyline where:
- Building height = amplitude magnitude
- Building position = which basis states are involved
- Real city vs Imaginary city = two separate plots

**Intuition Builder**: Use when you need to see EXACT amplitude values. The "city" metaphor helps: tall buildings (high amplitudes) are probable states.

#### 3. Math + Visual

**City Plot Layout**:
```
       Real Part:                 Imaginary Part:
        ▓▓      ▓▓                (all zero for real states)
        ▓▓      ▓▓
        ▓▓      ▓▓
       ─────────────              ─────────────
       00 01 10 11                00 01 10 11
```

#### 4. Implementation

**Qiskit Syntax**:
```python
from qiskit.visualization import plot_state_city
plot_state_city(state, title="My State")
```

**Example**:
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector(qc)
plot_state_city(state, title="Bell State City Plot")
```

#### 5. ⚠️ Trap Alert

**Trap: Only Works with Statevector**
```python
# ❌ WRONG
plot_state_city({'00': 500})  # TypeError!

# ✅ CORRECT
plot_state_city(Statevector(qc))
```

#### 6. 🧠 Mnemonic

**"City shows the heights (amplitudes)"**
- Meaning: Bars = amplitude magnitudes, easy to compare
- Example: Use when debugging exact values

#### 7. ⚡ Quick Check

**Q: What does plot_state_city() show for a Bell state (|00⟩ + |11⟩)/√2?**

<details>
<summary>Answer</summary>

**A**: Two tall bars at positions (0,0) and (1,1) in the real part, with height ~0.5 each, and flat (zero) imaginary part.

This corresponds to the density matrix having non-zero elements only at ρ₀₀,₀₀, ρ₀₀,₁₁, ρ₁₁,₀₀, and ρ₁₁,₁₁.
</details>

---

### 🔹 plot_state_qsphere()

#### 1. Definition

`plot_state_qsphere()` shows the quantum state on a spherical surface where each computational basis state is a marker. Marker size indicates probability, and color indicates phase.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like a globe with cities:
- City location = basis state
- City size = probability of that state
- City color = phase angle

#### 3. Math + Visual

**Q-Sphere Layout**:
```
       ○ (|00⟩, large, blue = phase 0)
      / \
     ●   ●  (|01⟩, |10⟩ if any probability)
      \ /
       ○ (|11⟩, large, blue = same phase)
```

#### 4. Implementation

```python
from qiskit.visualization import plot_state_qsphere
plot_state_qsphere(state)
```

#### 5. ⚠️ Trap Alert

**Trap: Q-sphere is NOT Bloch sphere**
- Q-sphere: One sphere, multiple markers for multi-qubit states
- Bloch sphere: One sphere PER qubit

#### 6. 🧠 Mnemonic

**"Q-sphere = Quantity + Phase"**
- Size = Quantity (probability)
- Color = Phase

#### 7. ⚡ Quick Check

**Q: On a Q-sphere, what does marker SIZE represent?**

<details>
<summary>Answer</summary>

**A**: Probability (|amplitude|²) of that basis state.

Larger markers = higher probability of measuring that outcome.
</details>

---

### 🔹 plot_state_hinton() and plot_state_paulivec()

#### 1. Definition

- **plot_state_hinton()**: Shows density matrix as squares where size = magnitude, color = sign (white=positive, black=negative)
- **plot_state_paulivec()**: Shows expectation values of all Pauli operator combinations

#### 2. Analogy + Intuition

**Hinton**: Like a checkerboard where square size shows correlation strength between basis states. Useful for seeing entanglement structure.

**Paulivec**: Like breaking down a chord into its component notes. Shows how much each Pauli operator contributes.

#### 3. Implementation

```python
from qiskit.visualization import plot_state_hinton, plot_state_paulivec

plot_state_hinton(state)
plot_state_paulivec(state)
```

#### 4. When to Use

| Visualization | Best For |
|---------------|----------|
| Hinton | Density matrix structure, entanglement, coherences |
| Paulivec | VQE, quantum chemistry, Pauli decomposition |

---

## 📊 State Visualization - Consolidated Review

### Visualization Compatibility Matrix

| Visualization | Statevector | counts dict |
|---------------|:-----------:|:-----------:|
| `plot_bloch_multivector()` | ✅ | ❌ |
| `plot_state_city()` | ✅ | ❌ |
| `plot_state_qsphere()` | ✅ | ❌ |
| `plot_state_hinton()` | ✅ | ❌ |
| `plot_state_paulivec()` | ✅ | ❌ |
| `plot_histogram()` | ❌ | ✅ |
| `plot_distribution()` | ❌ | ✅ |

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ STATE VISUALIZATION - QUICK REFERENCE                           │
├─────────────────────────────────────────────────────────────────┤
│ ALL REQUIRE: Statevector (no measurements in circuit!)          │
├─────────────────────────────────────────────────────────────────┤
│ plot_bloch_multivector(sv) - Individual qubit Bloch spheres     │
│ plot_state_city(sv)        - 3D bars of density matrix          │
│ plot_state_qsphere(sv)     - Probability + phase on sphere      │
│ plot_state_hinton(sv)      - Density matrix as squares          │
│ plot_state_paulivec(sv)    - Pauli operator expectations        │
├─────────────────────────────────────────────────────────────────┤
│ MNEMONICS:                                                      │
│ • "No M before S" - No Measure before Statevector               │
│ • "Bloch for single-qubit soul"                                 │
│ • "City shows heights (amplitudes)"                             │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAPS:                                                      │
│ • Statevector needs measurement-free circuit                    │
│ • Can't use counts with state visualizations                    │
│ • Entangled qubits appear mixed on Bloch sphere                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Measurement Visualization

> **STRUCTURE**: Visualizing counts/probabilities AFTER measurement
> **CRITICAL**: Use StatevectorSampler to get counts, then visualize

### Overview

Measurement visualization shows what was OBSERVED when running a quantum circuit. Unlike state visualization, this shows classical outcomes (bit strings) and their frequencies. Works with real hardware output too!

---

### 🔹 StatevectorSampler vs Statevector

#### 1. Definition

| Tool | Purpose |
|------|---------|
| `Statevector` | Get exact quantum state (amplitudes + phase) |
| `StatevectorSampler` | Simulate measurement sampling (counts) |

#### 2. Analogy + Intuition

**Dice Analogy**:
- **Statevector** = Knowing exact probabilities (1/6 each face)
- **StatevectorSampler** = Actually rolling dice 1000 times

#### 3. Critical Differences

| Aspect | Statevector | StatevectorSampler |
|--------|-------------|-------------------|
| **Import** | `from qiskit.quantum_info import Statevector` | `from qiskit.primitives import StatevectorSampler` |
| **Measurements** | ❌ Circuit must NOT have measurements | ✅ Circuit MUST have measurements |
| **Output** | Complex amplitudes | Counts dictionary |
| **Randomness** | Deterministic | Probabilistic (varies with shots) |

#### 4. Implementation

**Statevector (exact state)**:
```python
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# NO measurements!

state = Statevector(qc)
print(state.data)  # [0.707+0j, 0, 0, 0.707+0j]
```

**StatevectorSampler (simulated counts)**:
```python
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])  # MUST have measurements!

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
counts = job.result()[0].data.meas.get_counts()
print(counts)  # {'00': 507, '11': 493}
```

#### 5. ⚠️ Trap Alert

**Trap: Opposite Measurement Requirements**
- ❌ Statevector with measurements → collapsed state
- ❌ StatevectorSampler without measurements → no counts

```python
# ❌ TRAP: Sampler without measurements
qc = QuantumCircuit(2)
qc.h(0)
# No measurements!
sampler.run([qc])  # Won't have count data!

# ✅ CORRECT: Add measurements for Sampler
qc.measure_all()
sampler.run([qc], shots=1000)
```

#### 6. 🧠 Mnemonic

**"State = What it IS, Sample = What we SEE"**
- Statevector = internal quantum state
- StatevectorSampler = simulated measurement outcomes

#### 7. ⚡ Quick Check

**Q: You want to simulate running a circuit 10,000 times. Which tool?**

<details>
<summary>Answer</summary>

**A**: `StatevectorSampler`

```python
sampler = StatevectorSampler()
job = sampler.run([qc], shots=10000)  # 10,000 simulated runs
```

Statevector gives exact amplitudes (no sampling), StatevectorSampler simulates actual measurement statistics.
</details>

---

### 🔹 plot_histogram()

#### 1. Definition

`plot_histogram()` creates a bar chart showing measurement counts. Each bar is a basis state (bit string), height is number of occurrences.

#### 2. Analogy + Intuition

**Real-World Analogy**: Like an election results bar chart:
- Each candidate (bit string) gets a bar
- Bar height = number of votes (occurrences)
- Shows raw counts, not percentages

#### 3. Math + Visual

**Histogram Layout**:
```
Counts
  500 │      ▓▓▓▓                    ▓▓▓▓
  400 │      ▓▓▓▓                    ▓▓▓▓
  300 │      ▓▓▓▓                    ▓▓▓▓
  200 │      ▓▓▓▓                    ▓▓▓▓
  100 │      ▓▓▓▓                    ▓▓▓▓
    0 ├──────────────────────────────────
           00      01      10      11
           
Bell state: ~50% |00⟩, ~50% |11⟩
```

#### 4. Implementation

**Qiskit Syntax**:
```python
from qiskit.visualization import plot_histogram
plot_histogram(counts)
```

**Parameters**:
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `data` | dict/list | Counts dict or list of dicts | Required |
| `legend` | list | Labels for multiple histograms | None |
| `sort` | str | 'value', 'value_desc', 'asc', 'desc' | None |
| `bar_labels` | bool | Show count on bars | True |
| `title` | str | Plot title | None |
| `figsize` | tuple | Figure dimensions | None |

**Basic Example**:
```python
from qiskit.visualization import plot_histogram

counts = {'00': 507, '11': 493}
plot_histogram(counts)
```

**Compare Multiple Results**:
```python
# Compare two algorithms
counts1 = {'00': 500, '11': 500}      # Bell state
counts2 = {'00': 250, '01': 250, '10': 250, '11': 250}  # Uniform

plot_histogram([counts1, counts2], legend=['Bell', 'Uniform'])
```

#### 5. ⚠️ Trap Alert

**Trap: Can't Use Statevector**
```python
# ❌ WRONG
state = Statevector(qc)
plot_histogram(state)  # TypeError! Expects dict

# ✅ CORRECT
counts = sampler.run([qc], shots=1000).result()[0].data.meas.get_counts()
plot_histogram(counts)
```

#### 6. 🧠 Mnemonic

**"Histogram = How many times"**
- Raw counts of measurement outcomes
- Heights are integers (occurrences)

#### 7. ⚡ Quick Check

**Q: What input type does plot_histogram() expect?**

<details>
<summary>Answer</summary>

**A**: A dictionary with bit strings as keys and counts as values.

```python
counts = {'00': 512, '11': 488}  # ✅ Correct format
plot_histogram(counts)
```
</details>

---

### 🔹 plot_distribution()

#### 1. Definition

`plot_distribution()` is similar to plot_histogram but shows normalized probabilities (values sum to 1) instead of raw counts.

#### 2. Comparison

| Aspect | plot_histogram | plot_distribution |
|--------|----------------|-------------------|
| Y-axis | Raw counts | Probabilities (0-1) |
| Sum of bars | Total shots | 1.0 |
| Use case | Comparing experiments | Theoretical comparison |

#### 3. Implementation

```python
from qiskit.visualization import plot_distribution

counts = {'00': 507, '11': 493}
plot_distribution(counts)  # Shows ~0.507 and ~0.493
```

---

## 📊 Measurement Visualization - Consolidated Review

### Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ MEASUREMENT VISUALIZATION - QUICK REFERENCE                     │
├─────────────────────────────────────────────────────────────────┤
│ GETTING COUNTS:                                                 │
│ sampler = StatevectorSampler()                                  │
│ job = sampler.run([qc], shots=1000)                             │
│ counts = job.result()[0].data.meas.get_counts()                 │
├─────────────────────────────────────────────────────────────────┤
│ plot_histogram(counts) - Raw counts bar chart                   │
│ plot_distribution(counts) - Normalized probability bars         │
├─────────────────────────────────────────────────────────────────┤
│ COMPARE MULTIPLE:                                               │
│ plot_histogram([counts1, counts2], legend=['A', 'B'])           │
├─────────────────────────────────────────────────────────────────┤
│ TOP TRAP: Must use counts dict, not Statevector!                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔍 Understanding Histogram Patterns: Superposition vs Entanglement

> **EXAM CRITICAL**: Given a histogram, identify whether the state is superposition or entanglement!

### Key Concepts

#### Superposition

**Definition**: A single qubit exists in **multiple states simultaneously** until measured. A qubit in superposition is not in state |0⟩ OR |1⟩, but in a combination of BOTH at the same time.

**Mathematical Form**:
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$

**Key Characteristics**:
- Applies to a **single qubit** (or independent qubits)
- Created using **Hadamard gate (H)**: `qc.h(0)`
- Upon measurement, collapses to ONE definite state
- Qubits decide **INDEPENDENTLY**

#### Entanglement

**Definition**: Two or more qubits become **correlated** such that the quantum state of one qubit **cannot be described independently** of the others. Measuring one instantly determines the state of the other(s).

**Mathematical Form** (Bell State):
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

**Key Characteristics**:
- Requires **multiple qubits** (minimum 2)
- Created using **H gate + CNOT**: `qc.h(0); qc.cx(0, 1)`
- Qubits are **correlated** — measuring one affects the other
- Qubits decide **TOGETHER**

### Visual Comparison: Histogram Patterns

```
SUPERPOSITION (2 independent qubits):         ENTANGLEMENT (2 correlated qubits):
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│  qc.h(0)                        │           │  qc.h(0)                        │
│  qc.h(1)                        │           │  qc.cx(0, 1)                    │
│                                 │           │                                 │
│  Histogram:                     │           │  Histogram:                     │
│   25%  25%  25%  25%            │           │   50%              50%          │
│   ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓            │           │   ▓▓▓▓▓▓            ▓▓▓▓▓▓      │
│   00   01   10   11             │           │   00   01   10   11             │
│                                 │           │         (none) (none)           │
│  Each qubit decides             │           │  Qubits decide                  │
│  INDEPENDENTLY                  │           │  TOGETHER                       │
└─────────────────────────────────┘           └─────────────────────────────────┘
```

### Quick Comparison Table

| Aspect | Superposition | Entanglement |
|--------|---------------|--------------|
| **Applies to** | Single qubit (or independent qubits) | Multiple qubits (minimum 2) |
| **Independence** | Qubits are independent | Qubits cannot be described independently |
| **Creation** | H gate alone: `qc.h(0)` | H + CNOT: `qc.h(0); qc.cx(0,1)` |
| **Measurement correlation** | Independent outcomes | Correlated outcomes |
| **Histogram pattern** | 4 equal bars (uniform) | 2 bars only (correlated) |

### Conceptual Analogy

```
SUPERPOSITION = Flipping 2 independent coins
  • Each coin is heads AND tails until you look
  • Looking at coin 1 tells you nothing about coin 2
  • All 4 outcomes equally likely: HH, HT, TH, TT

ENTANGLEMENT = Two magic coins that are linked
  • Both coins are in superposition together
  • If coin 1 shows heads, coin 2 MUST show heads
  • If coin 1 shows tails, coin 2 MUST show tails
  • Only 2 outcomes possible: HH or TT
  • "Looking" at one instantly determines the other
```

### Why This Matters for Visualization

When you see a histogram:
- **4 equal bars** → Superposition (independent qubits)
- **Only 00 and 11** → Bell state entanglement
- **Only 01 and 10** → Other Bell state (anti-correlated)

---

## 🔧 Backend Visualization

### 🔹 plot_gate_map()

#### 1. Definition

`plot_gate_map()` visualizes the coupling map of a quantum backend - shows which qubits can directly perform two-qubit gates (like CNOT).

#### 2. Why Topology Matters

Real quantum computers don't have all-to-all connectivity. Physical qubits are arranged in specific patterns:

```
Ideal (All-to-All):          Real Hardware (Limited):
    0 ──── 1                     0 ── 1 ── 2
    │\    /│                          │
    │ \  / │                     3 ── 4 ── 5
    │  \/  │                          │
    │  /\  │                     6 ── 7 ── 8
    2 ──── 3                   (Grid topology)
```

#### 3. Implementation

```python
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.visualization import plot_gate_map

backend = GenericBackendV2(num_qubits=5)
plot_gate_map(backend)
```

**Parameters**:
| Parameter | Type | Description |
|-----------|------|-------------|
| `backend` | Backend | Backend to visualize |
| `plot_directed` | bool | Show arrow directions |
| `label_qubits` | bool | Number the qubits |
| `figsize` | tuple | Figure size |

#### 4. ⚠️ Trap Alert

**Trap: plot_gate_map vs plot_coupling_map**
| Function | Input |
|----------|-------|
| `plot_gate_map()` | Backend object |
| `plot_coupling_map()` | CouplingMap object |

```python
# plot_gate_map - takes backend
plot_gate_map(backend)

# plot_coupling_map - takes coupling_map
plot_coupling_map(backend.coupling_map)
```

---

### 🔹 plot_circuit_layout() - Transpilation Mapping

#### 1. Definition

`plot_circuit_layout()` shows how a circuit was mapped onto physical qubits after transpilation. It visualizes which physical qubits were assigned to your logical qubits.

#### 2. Why This Matters

After transpilation, your logical qubits (0, 1, 2...) are mapped to physical qubits on the device. This function shows that mapping, which is essential for understanding:
- Why SWAP gates were inserted
- Which physical qubits your algorithm uses
- How to optimize qubit placement

#### 3. Implementation

```python
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_circuit_layout
from qiskit.providers.fake_provider import GenericBackendV2

# Create circuit
qc = QuantumCircuit(3)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)

# Transpile to backend
backend = GenericBackendV2(num_qubits=5)
transpiled = transpile(qc, backend)

# Show layout on device
plot_circuit_layout(transpiled, backend)
```

#### 4. ⚠️ Trap Alert

**Trap: Must Use Transpiled Circuit**
- ❌ **Wrong**: `plot_circuit_layout(qc, backend)` - original circuit has no layout
- ✅ **Correct**: `plot_circuit_layout(transpiled, backend)` - transpiled circuit has layout

---

## 🔧 Dynamic Circuit Visualization

### 🔹 Classical Feedforward (if_test)

#### 1. Definition

Dynamic circuits use mid-circuit measurements to control subsequent operations. The `if_test` context manager creates conditional gates based on classical bit values.

#### 2. Visual Notation

```
Simple if_test (condition on 1):
q: ─────M─────●─────
             │
             ├──X──  ← X applied only if measured 1
             │
c: ═════╪════╪═════
```

#### 3. Implementation

```python
from qiskit.circuit import QuantumCircuit, QuantumRegister, ClassicalRegister

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)

qc.h(qr[0])
qc.measure(qr[0], cr[0])

with qc.if_test((cr[0], 1)):  # If measured 1
    qc.x(qr[0])               # Apply X gate

qc.draw('mpl', style='iqp')  # IQP style best for control flow
```

#### 4. Best Practices

- Use `output='mpl'` for control flow rendering
- Use `style='iqp'` for optimized dynamic circuit display
- Set `idle_wires=False` to hide unused wires

---

## ⚠️ MASTER TRAP LIST

> **ALL traps from ALL topics** - organized for final review before exam.

### Trap Summary Table

| # | Topic | Trap Name | ❌ Wrong | ✅ Correct |
|---|-------|-----------|----------|-----------|
| 1 | qc.draw() | Default is text | `qc.draw()` for graphics | `qc.draw('mpl')` |
| 2 | Styling | Style with text | `qc.draw(style='iqp')` | `qc.draw('mpl', style='iqp')` |
| 3 | Statevector | Measurements OK | Circuit with measures | No measurements |
| 4 | Bloch sphere | Expects counts | `plot_bloch(counts)` | `plot_bloch(Statevector)` |
| 5 | Histogram | Expects state | `plot_histogram(state)` | `plot_histogram(counts)` |
| 6 | Sampler | No measurements | Circuit without measure | Must have measurements |
| 7 | Entanglement | Pure on Bloch | Arrow on surface | Arrow at center (mixed) |
| 8 | plot_gate_map | Wrong input type | `plot_gate_map(coupling_map)` | `plot_gate_map(backend)` |
| 9 | plot_circuit_layout | Original circuit | `plot_circuit_layout(qc, backend)` | `plot_circuit_layout(transpiled, backend)` |

---

## 📝 PRACTICE EXAM

### Part A: Quick Fire

**Q1**: What's the default output format for `qc.draw()`?
<details>
<summary>Answer</summary>

**A**: text
</details>

**Q2**: Which parameter puts the highest-indexed qubit at the TOP of the circuit diagram?
<details>
<summary>Answer</summary>

**A**: `reverse_bits=True`
</details>

**Q3**: Can you use `plot_state_city()` with measurement counts?
<details>
<summary>Answer</summary>

**A**: No - it requires a Statevector, not counts dictionary.
</details>

**Q4**: What does it mean when a qubit's Bloch sphere arrow points to the center?
<details>
<summary>Answer</summary>

**A**: The qubit is in a mixed state, typically indicating it's entangled with another qubit.
</details>

**Q5**: Which tool gives probabilistic results: Statevector or StatevectorSampler?
<details>
<summary>Answer</summary>

**A**: StatevectorSampler (varies each run due to sampling). Statevector is deterministic.
</details>

### Part B: Code Analysis

**Q6**: What's wrong with this code?
```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
plot_histogram(Statevector(qc))
```
<details>
<summary>Answer</summary>

**A**: `plot_histogram()` expects a counts dictionary, not a Statevector.

**Fix**:
```python
from qiskit.primitives import StatevectorSampler
qc.measure_all()
sampler = StatevectorSampler()
counts = sampler.run([qc], shots=1000).result()[0].data.meas.get_counts()
plot_histogram(counts)
```
</details>

**Q7**: What's wrong with this code?
```python
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.measure(0, 0)
state = Statevector(qc)
plot_state_city(state)
```
<details>
<summary>Answer</summary>

**A**: The circuit has measurements, so Statevector gives the post-measurement (collapsed) state, not the superposition.

**Fix**: Remove measurements before getting Statevector:
```python
qc = QuantumCircuit(2)
qc.h(0)
state = Statevector(qc)
plot_state_city(state)
```
</details>

### Part C: Real-World Scenarios (3 Questions)

**Q8**: You're presenting a quantum algorithm to stakeholders and need to show:
1. The circuit structure
2. The theoretical state at each step
3. What results look like when run 10,000 times

What visualization tools would you use for each?

<details>
<summary>Answer</summary>

**A**: Use three different visualization approaches:

**1. Circuit structure:**
```python
qc.draw(output='mpl', style='iqp', reverse_bits=True)
```
Use matplotlib for presentation quality with IQP styling.

**2. Theoretical state at each step:**
```python
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_city

# Create circuit WITHOUT measurements
qc_state = QuantumCircuit(n)
# Add gates step by step, visualize after each:
for step in steps:
    qc_state.append(step)
    state = Statevector(qc_state)
    plot_bloch_multivector(state)  # Individual qubit view
    plot_state_city(state)          # Full amplitude view
```

**3. Simulated run results:**
```python
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram

# Circuit WITH measurements
qc_measure = qc_state.copy()
qc_measure.measure_all()

sampler = StatevectorSampler()
job = sampler.run([qc_measure], shots=10000)
counts = job.result()[0].data.meas.get_counts()
plot_histogram(counts, title="Results from 10,000 shots")
```
</details>

**Q9**: Your colleague claims their Bell state preparation is correct, but when you visualize it with `plot_bloch_multivector()`, both qubits show arrows pointing at the center of the sphere. They think this means the state is wrong. How do you explain this?

<details>
<summary>Answer</summary>

**A**: **The state is actually CORRECT!** This is expected behavior for entangled states.

**Explanation:**
```
Bell state: |ψ⟩ = (|00⟩ + |11⟩)/√2

When you trace out one qubit to look at the other individually,
each qubit appears to be in a maximally mixed state:
ρ₀ = ρ₁ = I/2 (identity/2)

A maximally mixed state has NO preferred direction, so the 
Bloch vector points to the origin (center of sphere).
```

**The "center arrow" PROVES entanglement:**
- Pure separable states: arrows on the SURFACE of sphere
- Entangled states: arrows INSIDE the sphere (mixed when viewed individually)
- Maximally entangled (Bell state): arrows at CENTER (maximally mixed)

**To verify the Bell state is correct, use a different visualization:**
```python
# plot_state_city shows the full density matrix
plot_state_city(state)  # Should show bars at 00 and 11 positions

# Or check the state vector directly
print(state.data)  # Should be [0.707, 0, 0, 0.707]
```

**Mnemonic: "Center = Correlated"** - arrows at center indicate quantum correlations (entanglement).
</details>

**Q10**: You need to debug a 5-qubit circuit that should produce equal superposition of all 32 states. The histogram shows uneven bars. Walk through your debugging process using visualization tools.

<details>
<summary>Answer</summary>

**A**: Systematic debugging with visualization:

**Step 1: Visualize the circuit first**
```python
qc.draw(output='mpl', fold=30)
# Check: Are there H gates on ALL 5 qubits?
# Check: Are there unexpected gates causing interference?
```

**Step 2: Check state at each stage (remove measurements temporarily)**
```python
qc_debug = qc.remove_final_measurements(inplace=False)

# After just the H layer:
qc_h_only = QuantumCircuit(5)
qc_h_only.h([0,1,2,3,4])

state = Statevector(qc_h_only)
probs = state.probabilities()
print(f"Should all be ~0.03125: {probs}")  # 1/32 = 0.03125

# Compare with actual circuit state
actual_state = Statevector(qc_debug)
plot_state_qsphere(actual_state)  # All markers should be same size
```

**Step 3: Verify measurements aren't the issue**
```python
# Run with many shots to reduce statistical noise
sampler = StatevectorSampler()
job = sampler.run([qc], shots=100000)  # More shots = better statistics
counts = job.result()[0].data.meas.get_counts()

# All 32 outcomes should have ~3125 counts (100000/32)
plot_histogram(counts, sort='asc')
```

**Common issues found:**
- Missing H gate on one qubit → half the states missing
- Extra CNOT or CZ gate → interference patterns
- Measurement on wrong classical bits → scrambled labels
- Not enough shots → statistical variation looks like error
</details>

---

## ✅ Key Takeaways

### 📚 Concept Checklist
```
□ qc.draw() renders circuit as diagram (text, mpl, or latex format)
□ Default draw output is TEXT, not matplotlib
□ reverse_bits=True puts MSB (highest index) on top (physics convention)
□ style parameter only works with output='mpl'
□ Statevector = exact quantum state with amplitudes and phase
□ Statevector requires circuit WITHOUT measurements
□ StatevectorSampler = simulated measurement sampling (probabilistic)
□ StatevectorSampler requires circuit WITH measurements
□ plot_bloch_multivector shows each qubit on individual Bloch sphere
□ Entangled qubits appear MIXED (arrow at center) on Bloch sphere
□ plot_state_city shows density matrix as 3D bar chart
□ plot_state_qsphere shows probability (size) and phase (color) on sphere
□ plot_histogram shows raw measurement counts (needs counts dict)
□ plot_distribution shows normalized probabilities (sums to 1)
□ plot_gate_map visualizes backend qubit connectivity
□ Q-sphere is NOT the same as Bloch sphere (different visualizations)
```

### 💻 Code Pattern Checklist
```
□ qc.draw() returns text representation (default)
□ qc.draw('mpl') returns matplotlib figure
□ qc.draw('latex') returns LaTeX rendering
□ qc.draw(output='mpl', reverse_bits=True) puts MSB on top
□ qc.draw(output='mpl', style='iqp') applies IBM Quantum style
□ qc.draw(output='mpl', style='bw') applies black/white style
□ qc.draw(output='mpl', fold=20) wraps after 20 columns
□ qc.draw(output='mpl', idle_wires=False) hides empty wires
□ qc.draw(output='mpl', filename='circuit.png') saves to file
□ from qiskit.quantum_info import Statevector
□ state = Statevector(qc) creates statevector from circuit (NO measurements!)
□ state.data returns complex amplitude array
□ state.probabilities() returns probability array
□ state.draw('bloch') draws Bloch representation
□ from qiskit.visualization import plot_bloch_multivector
□ plot_bloch_multivector(state) visualizes multi-qubit state
□ from qiskit.visualization import plot_state_city, plot_state_qsphere
□ plot_state_city(state) shows 3D amplitude bars
□ plot_state_qsphere(state) shows probability + phase on sphere
□ from qiskit.primitives import StatevectorSampler
□ sampler = StatevectorSampler() creates sampler
□ job = sampler.run([qc], shots=1000) runs with 1000 shots
□ counts = job.result()[0].data.meas.get_counts() extracts counts
□ from qiskit.visualization import plot_histogram, plot_distribution
□ plot_histogram(counts) shows raw count bars
□ plot_histogram([counts1, counts2], legend=['A', 'B']) compares results
□ plot_distribution(counts) shows normalized probabilities
□ from qiskit.visualization import plot_gate_map
□ plot_gate_map(backend) visualizes qubit connectivity
```

### ⚠️ Exam Trap Checklist
```
□ TRAP: qc.draw() default is TEXT, not mpl!
  → Use: qc.draw('mpl') for graphical output
□ TRAP: style='iqp' ignored with text output
  → Must use: qc.draw(output='mpl', style='iqp')
□ TRAP: Statevector with measurements gives COLLAPSED state!
  → Remove measurements before: state = Statevector(qc_no_measure)
□ TRAP: plot_bloch_multivector(counts) → TypeError!
  → Needs Statevector: plot_bloch_multivector(Statevector(qc))
□ TRAP: plot_histogram(Statevector(qc)) → TypeError!
  → Needs counts dict: plot_histogram(counts)
□ TRAP: StatevectorSampler without measurements → no counts!
  → Circuit MUST have measurements for Sampler
□ TRAP: Entangled qubits show arrows at CENTER on Bloch sphere
  → This is CORRECT! Center = mixed/entangled (not a bug)
□ TRAP: Q-sphere is NOT Bloch sphere
  → Q-sphere: one sphere, multiple markers
  → Bloch: one sphere PER qubit
□ TRAP: plot_gate_map vs plot_coupling_map
  → plot_gate_map(backend) - takes Backend
  → plot_coupling_map(coupling_map) - takes CouplingMap
□ TRAP: plot_circuit_layout needs transpiled circuit
  → plot_circuit_layout(transpiled, backend) - NOT original circuit
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 2 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🎨 "MPL for My Pretty Layout"                                    │
│    Use qc.draw('mpl') for nice graphical output                 │
│    Default is boring text!                                      │
│                                                                  │
│ 📏 "Reverse Bits = Reading Order"                                │
│    reverse_bits=True makes |01⟩ read naturally top-to-bottom    │
│    Matches physics convention (MSB on top)                      │
│                                                                  │
│ 🚫 "No M before S" (No Measure before Statevector)               │
│    Statevector needs measurement-FREE circuit                   │
│    Measurements collapse the state!                             │
│                                                                  │
│ 👁️ "State = IS, Sample = SEE"                                    │
│    Statevector = what the state IS (exact amplitudes)           │
│    StatevectorSampler = what we would SEE (measurements)        │
│                                                                  │
│ 📊 "Histogram = How many times"                                  │
│    Shows raw counts of measurement outcomes                     │
│    Needs counts dict, NOT Statevector!                          │
│                                                                  │
│ 🔗 "Center = Correlated"                                         │
│    Arrow at center of Bloch sphere = entangled/mixed state      │
│    This is EXPECTED for Bell states!                            │
│                                                                  │
│ 🏙️ "City shows heights (amplitudes)"                             │
│    plot_state_city = 3D bars showing amplitude magnitudes       │
│    Great for seeing exact values                                │
│                                                                  │
│ 🌐 "Q-sphere = Quantity + Phase"                                 │
│    Marker Size = Quantity (probability)                         │
│    Marker Color = Phase angle                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 2: VISUALIZATION - ONE-PAGE SUMMARY                       ║
║                (11% of Exam - ~7 Questions)                           ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎨 CIRCUIT DRAWING                                                    ║
║  ├─ qc.draw() = text (default)                                        ║
║  ├─ qc.draw('mpl') = matplotlib figure (for notebooks)                ║
║  ├─ qc.draw('latex') = LaTeX (for publications)                       ║
║  ├─ reverse_bits=True = MSB on top (physics convention)               ║
║  └─ style='iqp'/'bw' only works with output='mpl'                     ║
║                                                                        ║
║  📊 STATE VISUALIZATION (needs Statevector, NO measurements!)          ║
║  ├─ state = Statevector(qc) - circuit must have NO measurements       ║
║  ├─ plot_bloch_multivector(state) - individual qubit Bloch spheres    ║
║  ├─ plot_state_city(state) - 3D amplitude bars                        ║
║  ├─ plot_state_qsphere(state) - probability (size) + phase (color)    ║
║  ├─ plot_state_hinton(state) - density matrix as squares              ║
║  └─ plot_state_paulivec(state) - Pauli operator expectations          ║
║                                                                        ║
║  📈 MEASUREMENT VISUALIZATION (needs counts dict, WITH measurements!)  ║
║  ├─ sampler = StatevectorSampler()                                    ║
║  ├─ job = sampler.run([qc], shots=1000)  # qc MUST have measurements  ║
║  ├─ counts = job.result()[0].data.meas.get_counts()                   ║
║  ├─ plot_histogram(counts) - raw counts bar chart                     ║
║  └─ plot_distribution(counts) - normalized probabilities              ║
║                                                                        ║
║  🗺️ BACKEND VISUALIZATION                                              ║
║  ├─ plot_gate_map(backend) - qubit connectivity diagram               ║
║  └─ plot_coupling_map(coupling_map) - takes CouplingMap object        ║
║                                                                        ║
║  ⚠️ TOP 5 EXAM TRAPS                                                   ║
║  1. Default qc.draw() is TEXT, not mpl (use qc.draw('mpl'))           ║
║  2. Statevector needs circuit WITHOUT measurements!                   ║
║  3. StatevectorSampler needs circuit WITH measurements!               ║
║  4. plot_histogram needs counts dict, NOT Statevector                 ║
║  5. Entangled qubits show arrows at CENTER on Bloch (this is correct!)║
║                                                                        ║
║  🔄 STATEVECTOR vs STATEVECTORSAMPLER                                  ║
║  ├─ Statevector: Exact state (amplitudes + phase), NO measurements    ║
║  └─ StatevectorSampler: Simulated counts, WITH measurements           ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## 📁 Files in This Section

| File | Description | Key Topics |
|------|-------------|------------|
| `circuit_visualization.ipynb` | Circuit drawing CODE LAB | qc.draw(), styles, parameters |
| `state_visualization.ipynb` | State viz CODE LAB | Bloch, city, qsphere, hinton |
| `visualization_examples.ipynb` | Combined examples CODE LAB | Statevector vs Sampler comparison |

---

## 🔗 Next Steps

1. Practice circuit drawing with all output formats
2. Visualize states at each step of an algorithm
3. Use histograms to verify measurement statistics
4. Move to **Section 3 (Circuit Creation)** to build complex circuits

**Visualization is your debugging superpower - use it to see the quantum world!** 🎨✨

---

*Last Updated: 2025*
