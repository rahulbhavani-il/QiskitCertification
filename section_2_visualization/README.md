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
CIRCUIT DRAWING CONCEPTS:
□ qc.draw() renders circuit as diagram (text, mpl, or latex format)
□ Default draw output is TEXT, not matplotlib (exam trap!)
□ output parameter accepts: 'text', 'mpl', 'latex', 'latex_source'
□ reverse_bits=True puts MSB (highest index qubit) on top (physics convention)
□ reverse_bits=False (default) puts qubit 0 on top (computational convention)
□ style parameter only works with output='mpl' (ignored for text/latex)
□ Available styles: 'iqp' (IBM Quantum Platform), 'bw' (black/white), 'clifford', 'textbook'
□ fold parameter wraps circuit diagram after N columns (default=-1, no folding)
□ idle_wires=False hides empty/unused wires in visualization
□ scale parameter adjusts size of matplotlib output (default=1.0)
□ with_layout=True shows physical qubit mapping (needs transpiled circuit)
□ initial_state=True shows initial state labels |0⟩ on left side
□ plot_barriers=True shows barrier gates in visualization (default=True)
□ justify parameter aligns gates: 'left', 'right', 'none' (default='left')
□ filename parameter saves figure to file (PNG, PDF, SVG supported)
□ cregbundle=True bundles classical register wires into single line

STATEVECTOR CONCEPTS:
□ Statevector = exact quantum state with complex amplitudes and global phase
□ Statevector represents 2^n dimensional complex vector for n qubits
□ Statevector requires circuit WITHOUT measurements (measurements collapse state)
□ Statevector normalization: sum of |amplitude|^2 = 1 (probability conservation)
□ Statevector can be created from: circuit, array, other Statevector
□ Statevector is computed on classical simulator (not real quantum hardware)
□ Statevector simulation complexity grows exponentially: O(2^n) memory
□ Maximum practical qubits for Statevector: ~30 qubits (memory limitations)
□ Statevector.data returns numpy array of complex amplitudes
□ Statevector.probabilities() returns real-valued probability distribution
□ Statevector.evolve(gate) applies gate to state (returns new Statevector)
□ Statevector.is_valid() checks if state is normalized (sum of probabilities = 1)
□ Global phase in Statevector: physically unobservable but mathematically present
□ Statevector supports density matrix conversion: DensityMatrix.from_label()

SAMPLING CONCEPTS:
□ StatevectorSampler = simulated measurement sampling (probabilistic outcomes)
□ StatevectorSampler requires circuit WITH measurements (classical bits recorded)
□ StatevectorSampler uses ideal simulation (no noise, perfect gates)
□ shots parameter controls number of measurement samples (default=1024)
□ Statistical uncertainty scales as 1/√(shots) - more shots = less variance
□ StatevectorSampler returns PubResult containing counts/bitstrings
□ Sampler.run() accepts list of circuits (batch execution)
□ Each PubResult has .data attribute with measurement outcomes
□ get_counts() returns counts dict: {'00': 512, '01': 488, ...}
□ get_bitstrings() returns array of individual measurement outcomes
□ seed parameter enables reproducible pseudorandom sampling
□ StatevectorSampler vs Backend.run(): sampler is ideal, backend has noise

BLOCH SPHERE CONCEPTS:
□ plot_bloch_multivector shows each qubit on individual Bloch sphere
□ Bloch sphere represents single-qubit state: |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
□ Bloch vector coordinates: (x, y, z) derived from Pauli expectation values
□ Pure states appear as vectors on surface of Bloch sphere (radius = 1)
□ Mixed states appear as vectors inside Bloch sphere (radius < 1)
□ Entangled qubits appear MIXED (arrow at center) on individual Bloch spheres
□ Arrow at center means qubit is maximally mixed: ρ = I/2 (completely uncertain)
□ Bloch sphere north pole = |0⟩, south pole = |1⟩
□ Bloch sphere x-axis = |+⟩ (positive) and |-⟩ (negative)
□ Bloch sphere y-axis = |+i⟩ (positive) and |-i⟩ (negative)
□ Cannot visualize multi-qubit entanglement on single Bloch sphere
□ plot_bloch_multivector shows separate sphere per qubit (not entanglement directly)

STATE VISUALIZATION CONCEPTS:
□ plot_state_city shows density matrix as 3D bar chart (city skyline)
□ plot_state_city bar height = amplitude magnitude, bar color = phase
□ plot_state_city has real and imaginary projections on different axes
□ plot_state_qsphere shows probability (marker size) and phase (marker color) on sphere
□ Q-sphere is NOT the same as Bloch sphere (different purposes/representations)
□ Q-sphere: one sphere with multiple markers (one per basis state)
□ Bloch sphere: one sphere per qubit showing qubit state vector
□ plot_state_hinton shows density matrix as colored squares (Hinton diagram)
□ plot_state_paulivec shows expectation values of Pauli operators
□ plot_state_paulivec useful for understanding state in terms of observables
□ All state plots require Statevector or DensityMatrix (not counts)

MEASUREMENT VISUALIZATION CONCEPTS:
□ plot_histogram shows raw measurement counts (integer frequencies)
□ plot_histogram needs counts dict, NOT Statevector or circuit
□ plot_histogram can compare multiple results: plot_histogram([counts1, counts2])
□ legend parameter adds labels when comparing multiple histograms
□ plot_distribution shows normalized probabilities (each bar sums to 1)
□ plot_distribution converts counts to probabilities automatically
□ Histogram shows empirical frequencies, distribution shows probabilities
□ bar_labels parameter adds count/probability labels on top of bars
□ sort parameter controls x-axis ordering: 'asc', 'desc', 'value', 'hamming'
□ target_string parameter highlights specific outcome in histogram

BACKEND VISUALIZATION CONCEPTS:
□ plot_gate_map visualizes backend qubit connectivity (physical layout)
□ plot_gate_map shows which qubits can directly interact (coupling map)
□ plot_coupling_map shows same info but takes CouplingMap object instead
□ Coupling map is critical for transpilation (determines gate routing)
□ plot_gate_map useful for understanding hardware topology constraints
□ Qubit properties (T1, T2, gate errors) can be visualized separately
```

### 💻 Code Pattern Checklist
```
CIRCUIT DRAWING IMPORTS & METHODS:
□ from qiskit import QuantumCircuit  # Core circuit class
□ qc.draw() returns text representation (default output)
□ qc.draw('mpl') returns matplotlib.figure.Figure object
□ qc.draw('latex') returns IPython.display.Image object (LaTeX rendering)
□ qc.draw('latex_source') returns raw LaTeX string
□ qc.draw(output='text', filename='circuit.txt') saves text to file
□ qc.draw(output='mpl', reverse_bits=True) puts MSB (q[n-1]) on top
□ qc.draw(output='mpl', reverse_bits=False) puts LSB (q[0]) on top (default)
□ qc.draw(output='mpl', style='iqp') applies IBM Quantum Platform visual style
□ qc.draw(output='mpl', style='bw') applies black/white style (printer-friendly)
□ qc.draw(output='mpl', style='clifford') uses Clifford gate styling
□ qc.draw(output='mpl', style='textbook') uses textbook notation
□ qc.draw(output='mpl', style={'name': 'my_style', ...}) custom style dict
□ qc.draw(output='mpl', fold=20) wraps circuit after 20 columns
□ qc.draw(output='mpl', fold=-1) no folding (default, single line)
□ qc.draw(output='mpl', idle_wires=False) hides unused/empty wires
□ qc.draw(output='mpl', idle_wires=True) shows all wires (default)
□ qc.draw(output='mpl', with_layout=True) shows physical qubit mapping
□ qc.draw(output='mpl', initial_state=True) shows |0⟩ labels on left
□ qc.draw(output='mpl', plot_barriers=False) hides barrier gates
□ qc.draw(output='mpl', justify='left') left-aligns gates (default)
□ qc.draw(output='mpl', justify='right') right-aligns gates
□ qc.draw(output='mpl', justify='none') no alignment
□ qc.draw(output='mpl', scale=1.5) enlarges figure by 1.5x
□ qc.draw(output='mpl', filename='circuit.png') saves PNG file
□ qc.draw(output='mpl', filename='circuit.pdf') saves vector PDF
□ qc.draw(output='mpl', filename='circuit.svg') saves SVG file
□ qc.draw(output='mpl', cregbundle=True) bundles classical bits
□ qc.draw(output='mpl', cregbundle=False) shows individual classical wires (default)

STATEVECTOR IMPORTS & METHODS:
□ from qiskit.quantum_info import Statevector  # Main import
□ state = Statevector(qc) creates statevector from circuit (NO measurements!)
□ state = Statevector([1, 0, 0, 0]) creates |00⟩ from array
□ state = Statevector.from_label('01') creates statevector from label
□ state = Statevector.from_label('+0') creates (|00⟩ + |10⟩)/√2
□ state = Statevector.from_int(3, 4) creates |0011⟩ (int 3, 4 qubits)
□ state.data returns numpy.ndarray of complex128 amplitudes
□ state.data.shape returns (2^n,) for n-qubit state
□ state.dim returns dimension (2^n) as integer
□ state.num_qubits returns number of qubits as integer
□ state.probabilities() returns numpy array of probabilities (real, non-negative)
□ state.probabilities_dict() returns dict: {'00': 0.5, '01': 0.5, ...}
□ state.probabilities_dict(decimals=3) rounds probabilities to 3 decimals
□ state.sample_counts(shots=1024) simulates measurements, returns counts dict
□ state.sample_memory(shots=100) returns list of individual outcomes
□ state.evolve(gate) applies unitary gate, returns new Statevector
□ state.evolve(qc) evolves by circuit, returns new Statevector
□ state.is_valid() returns bool (True if normalized, sum |amp|^2 = 1)
□ state.draw('text') returns text representation of amplitudes
□ state.draw('latex') returns LaTeX representation
□ state.draw('qsphere') draws Q-sphere visualization
□ state.draw('bloch') draws Bloch sphere (single qubit only!)
□ state.draw('city') draws state city (3D bar chart)
□ state.draw('hinton') draws Hinton diagram
□ state.draw('paulivec') draws Pauli vector (expectation values)
□ state.expectation_value(operator) computes ⟨ψ|O|ψ⟩ expectation
□ state.inner(other_state) computes inner product ⟨ψ|φ⟩
□ state.purity() returns purity (1.0 for pure states)
□ state.entropy() returns Von Neumann entropy (0 for pure states)
□ state.to_dict() returns dict with all state information
□ state.conjugate() returns complex conjugate of state
□ state.tensor(other_state) computes tensor product |ψ⟩⊗|φ⟩
□ Statevector.from_instruction(instruction) creates state from gate

STATEVECTORSAMPLER IMPORTS & METHODS:
□ from qiskit.primitives import StatevectorSampler  # Main import
□ sampler = StatevectorSampler() creates sampler instance
□ sampler = StatevectorSampler(default_shots=2048) sets default shots
□ sampler = StatevectorSampler(seed=42) sets random seed for reproducibility
□ job = sampler.run([qc]) runs single circuit (qc MUST have measurements)
□ job = sampler.run([qc1, qc2, qc3]) runs multiple circuits in batch
□ job = sampler.run([qc], shots=1000) overrides default shots per run
□ result = job.result() returns PrimitiveResult object
□ result = job.result(timeout=30) waits up to 30 seconds for result
□ pub_result = result[0] gets first PubResult (one per input circuit)
□ pub_result.data returns DataBin with measurement data
□ pub_result.data.meas returns BitArray of measurement outcomes
□ pub_result.data.meas.get_counts() returns dict: {'00': 512, '01': 488, ...}
□ pub_result.data.meas.get_bitstrings() returns list: ['00', '01', '00', ...]
□ pub_result.data.meas.num_shots returns total number of shots as int
□ pub_result.data.meas.num_bits returns number of classical bits as int
□ counts = pub_result.data.meas.get_counts() standard way to extract counts
□ counts = pub_result.data.<register_name>.get_counts() for named register
□ sampler.options.default_shots = 4096 modifies default shots after creation
□ sampler.options.seed = 123 modifies seed after creation

BLOCH VISUALIZATION IMPORTS & METHODS:
□ from qiskit.visualization import plot_bloch_multivector  # Main import
□ plot_bloch_multivector(state) visualizes multi-qubit state (one sphere/qubit)
□ plot_bloch_multivector(state, title='My State') adds custom title
□ plot_bloch_multivector(state, reverse_bits=True) reverses qubit order
□ plot_bloch_multivector(state, filename='bloch.png') saves to file
□ fig = plot_bloch_multivector(state) returns matplotlib Figure object
□ from qiskit.visualization import plot_bloch_vector  # Single vector
□ plot_bloch_vector([0, 0, 1]) plots single vector on Bloch sphere
□ plot_bloch_vector([x, y, z], title='Vector') custom title
□ Input state must be Statevector or DensityMatrix object
□ plot_bloch_multivector automatically separates qubits (no need to trace)
□ Entangled qubits show reduced density matrix (arrow at origin)

STATE CITY/QSPHERE IMPORTS & METHODS:
□ from qiskit.visualization import plot_state_city  # 3D bar import
□ plot_state_city(state) shows 3D amplitude bars (real + imaginary axes)
□ plot_state_city(state, title='State City') adds custom title
□ plot_state_city(state, color=['red', 'blue']) custom bar colors
□ plot_state_city(state, filename='city.png') saves figure
□ from qiskit.visualization import plot_state_qsphere  # Q-sphere import
□ plot_state_qsphere(state) shows probability (size) + phase (color) markers
□ plot_state_qsphere(state, show_state_labels=True) adds basis state labels
□ plot_state_qsphere(state, show_state_phases=True) adds phase values
□ plot_state_qsphere(state, filename='qsphere.png') saves figure
□ from qiskit.visualization import plot_state_hinton  # Hinton diagram
□ plot_state_hinton(state) shows density matrix as colored squares
□ plot_state_hinton(state, filename='hinton.png') saves figure
□ from qiskit.visualization import plot_state_paulivec  # Pauli vector
□ plot_state_paulivec(state) shows Pauli operator expectation values
□ plot_state_paulivec(state, color='blue') custom bar color
□ All state plot functions return matplotlib Figure objects
□ All state plot functions require Statevector or DensityMatrix (not counts!)

HISTOGRAM/DISTRIBUTION IMPORTS & METHODS:
□ from qiskit.visualization import plot_histogram  # Main import
□ plot_histogram(counts) plots raw count frequencies (integers)
□ plot_histogram(counts, title='Results') adds custom title
□ plot_histogram(counts, legend=['Run 1']) adds legend label
□ plot_histogram(counts, bar_labels=True) shows count values on bars
□ plot_histogram(counts, sort='value') sorts by outcome value
□ plot_histogram(counts, sort='hamming') sorts by Hamming distance
□ plot_histogram(counts, sort='asc') sorts ascending by count
□ plot_histogram(counts, sort='desc') sorts descending by count
□ plot_histogram(counts, target_string='00') highlights target outcome
□ plot_histogram(counts, color=['blue']) custom bar color
□ plot_histogram(counts, number_to_keep=10) shows only top 10 outcomes
□ plot_histogram(counts, filename='histogram.png') saves figure
□ plot_histogram([counts1, counts2]) compares multiple results
□ plot_histogram([counts1, counts2], legend=['A', 'B']) labels comparison
□ from qiskit.visualization import plot_distribution  # Distribution import
□ plot_distribution(counts) shows normalized probabilities (sum = 1)
□ plot_distribution(counts, title='Distribution') custom title
□ plot_distribution(counts, bar_labels=True) shows probability values
□ plot_distribution(counts, sort='value') sorts by outcome value
□ plot_distribution(counts, legend=['Experiment']) adds legend
□ plot_distribution(counts, filename='dist.png') saves figure
□ plot_distribution([counts1, counts2]) compares distributions
□ Counts dict format: {'00': 512, '01': 488, '10': 24, '11': 0}
□ Both functions handle missing keys (zero counts) automatically

BACKEND VISUALIZATION IMPORTS & METHODS:
□ from qiskit.visualization import plot_gate_map  # Backend connectivity
□ from qiskit_ibm_runtime import QiskitRuntimeService
□ service = QiskitRuntimeService()
□ backend = service.backend('ibm_brisbane')
□ plot_gate_map(backend) visualizes qubit connectivity graph
□ plot_gate_map(backend, figsize=(12, 8)) custom figure size
□ plot_gate_map(backend, plot_directed=True) shows directional edges
□ plot_gate_map(backend, label_qubits=True) adds qubit labels
□ plot_gate_map(backend, filename='gatemap.png') saves figure
□ from qiskit.visualization import plot_coupling_map  # CouplingMap version
□ from qiskit.transpiler import CouplingMap
□ coupling_map = CouplingMap([[0, 1], [1, 2], [1, 3]])
□ plot_coupling_map(coupling_map) plots connectivity from CouplingMap
□ plot_coupling_map(coupling_map, num_qubits=4) specifies total qubits
□ plot_coupling_map(coupling_map, figsize=(10, 6)) custom size
□ plot_gate_map takes Backend object as input
□ plot_coupling_map takes CouplingMap or list of edges as input
□ from qiskit.visualization import plot_circuit_layout  # Transpiled layout
□ transpiled_qc = transpile(qc, backend)
□ plot_circuit_layout(transpiled_qc, backend) shows virtual-to-physical mapping
□ plot_circuit_layout requires transpiled circuit (not original!)
```

### ⚠️ Exam Trap Checklist
```
CIRCUIT DRAWING TRAPS:
□ TRAP: qc.draw() default is TEXT, not matplotlib!
  → Fix: Use qc.draw('mpl') for graphical output
  → Why: Default output='text' for backward compatibility
□ TRAP: style='iqp' parameter ignored when output='text'
  → Fix: Must use qc.draw(output='mpl', style='iqp')
  → Why: Style only affects matplotlib rendering, not text
□ TRAP: reverse_bits parameter name confusion
  → Fix: reverse_bits=True shows MSB (q[n-1]) on TOP
  → Mistake: Thinking reverse_bits=True puts qubit 0 on top
□ TRAP: fold parameter doesn't work with output='text'
  → Fix: Use qc.draw(output='mpl', fold=20) for line wrapping
  → Why: Text output has its own wrapping logic
□ TRAP: with_layout=True on non-transpiled circuit shows nothing
  → Fix: Must transpile circuit first: transpile(qc, backend)
  → Why: Layout only exists after transpilation
□ TRAP: filename parameter doesn't add extension automatically
  → Fix: Specify full filename: filename='circuit.png' (not just 'circuit')
  → Why: Qiskit doesn't infer format from output type
□ TRAP: scale parameter ignored when output='text'
  → Fix: scale only works with output='mpl'
  → Why: Text output has fixed character dimensions
□ TRAP: qc.draw('latex') fails without LaTeX installation
  → Fix: Install LaTeX (MacTeX, TeX Live) or use output='latex_source'
  → Why: LaTeX rendering needs external LaTeX compiler
□ TRAP: initial_state=True shows |0⟩ even after state prep gates
  → Fix: initial_state only labels INPUT state (not computed state)
  → Why: This is a label, not a dynamic state calculation
□ TRAP: cregbundle=True can hide classical bit details
  → Fix: Use cregbundle=False to see individual classical wires
  → Why: Bundling hides which specific bit is measured

STATEVECTOR TRAPS:
□ TRAP: Statevector(qc) with measurements gives COLLAPSED state!
  → Fix: Remove measurements: qc_no_measure = qc.remove_final_measurements()
  → Why: Measurements project state to computational basis
□ TRAP: Statevector(qc) on very large circuit (>30 qubits) crashes
  → Fix: Use smaller circuits or switch to sampling methods
  → Why: Memory requirement is O(2^n), grows exponentially
□ TRAP: state.data indexing confusion for multi-qubit states
  → Fix: state.data[i] corresponds to basis state |i⟩ in binary
  → Example: state.data[3] = amplitude for |11⟩ (3 = 0b11)
□ TRAP: state.probabilities() vs state.probabilities_dict()
  → Fix: probabilities() returns array, probabilities_dict() returns dict
  → Why: Array order is [|00⟩, |01⟩, |10⟩, |11⟩], dict has string keys
□ TRAP: state.draw('bloch') on multi-qubit state fails!
  → Fix: Use plot_bloch_multivector(state) for multi-qubit
  → Why: state.draw('bloch') only works for single-qubit states
□ TRAP: Global phase difference not visible in probabilities
  → Fix: Global phase is unobservable; use state.data for full info
  → Why: |ψ⟩ and e^(iθ)|ψ⟩ have identical measurement probabilities
□ TRAP: state.evolve(gate) mutates state (wrong!)
  → Fix: new_state = state.evolve(gate) creates NEW Statevector
  → Why: evolve() returns new object, doesn't modify original
□ TRAP: Statevector.from_label('++') fails!
  → Fix: Use from_label('+') for single qubit, or tensor products
  → Why: from_label expects single-qubit labels ('+', '-', '0', '1', 'i', 'j')
□ TRAP: state.expectation_value(pauli_string) with wrong format
  → Fix: Use Pauli('ZZ') from qiskit.quantum_info.operators
  → Why: Expectation value needs Operator object, not string
□ TRAP: Statevector simulation gives exact results (no sampling error)
  → Fix: This is correct! Statevector is deterministic simulation
  → Why: Statevector computes exact amplitudes, not statistical samples
□ TRAP: state.is_valid() returns False after manual amplitude modification
  → Fix: Renormalize manually or use Statevector constructor
  → Why: Direct modification of state.data breaks normalization
□ TRAP: Comparing Statevector equality with == operator
  → Fix: Use np.allclose(state1.data, state2.data) for numerical comparison
  → Why: Floating-point precision issues make exact == unreliable

SAMPLING TRAPS:
□ TRAP: StatevectorSampler without measurements produces empty results!
  → Fix: Circuit MUST have qc.measure() or qc.measure_all() calls
  → Why: Sampler simulates measurement; needs classical bits to record
□ TRAP: StatevectorSampler(qc) vs sampler.run([qc]) confusion
  → Fix: StatevectorSampler() creates sampler, then sampler.run([qc])
  → Why: Sampler is executor object, not direct circuit processor
□ TRAP: Accessing result without .result() call
  → Fix: job = sampler.run([qc]); result = job.result(); counts = result[0].data.meas.get_counts()
  → Why: .run() returns job object, need .result() to get PrimitiveResult
□ TRAP: result[0].data.meas when circuit has custom register name
  → Fix: Use result[0].data.<register_name>.get_counts() for named registers
  → Why: Default name is 'meas', but custom names differ
□ TRAP: shots=1000 gives exact 500/500 split for uniform superposition
  → Fix: This is coincidence! Statistical fluctuation causes variations
  → Why: Sampling is probabilistic; expect ±√(shots) variation
□ TRAP: seed parameter doesn't make different runs identical on different machines
  → Fix: Seed only controls pseudorandom generator, not environment
  → Why: NumPy/system differences can cause minor variations
□ TRAP: get_counts() returns dict with missing keys (zero counts)
  → Fix: Check dict.get(key, 0) to handle missing outcomes
  → Why: Keys with zero counts are omitted from dict
□ TRAP: get_bitstrings() returns array vs get_counts() returns dict
  → Fix: bitstrings is list of individual shots, counts aggregates them
  → Why: Different representations for different use cases
□ TRAP: Sampler.run() with circuit that has no classical register
  → Fix: Add classical register: qc.add_register(ClassicalRegister(n))
  → Why: Measurements need classical bits to store outcomes
□ TRAP: Running sampler.run([qc1, qc2]) expects same shot count
  → Fix: Use shots parameter per circuit if needed, or default_shots
  → Why: Single run uses same shot count for all circuits
□ TRAP: StatevectorSampler vs BackendSampler result format differences
  → Fix: Both return PrimitiveResult, but BackendSampler may have job queue
  → Why: Statevector is local simulation, Backend queues on hardware
□ TRAP: Sampler with parameterized circuit needs parameter binding
  → Fix: Use sampler.run([(qc, parameter_values)]) with tuples
  → Why: Sampler V2 API requires explicit parameter binding

BLOCH SPHERE TRAPS:
□ TRAP: plot_bloch_multivector(counts) → TypeError!
  → Fix: Needs Statevector: plot_bloch_multivector(Statevector(qc))
  → Why: Function expects quantum state object, not measurement counts
□ TRAP: Entangled Bell state shows arrows at CENTER on Bloch sphere
  → Fix: This is CORRECT! Center = maximally mixed reduced density matrix
  → Why: Tracing out entangled partner leaves mixed state (ρ = I/2)
□ TRAP: Expecting 2-qubit entanglement visible on Bloch plot
  → Fix: Can't visualize entanglement on individual Bloch spheres
  → Why: Bloch sphere shows single-qubit reduced state, not correlations
□ TRAP: Bloch sphere showing vector outside unit sphere
  → Fix: This indicates bug or non-normalized state
  → Why: Physical quantum states must have ||ψ|| = 1
□ TRAP: Bloch vector components don't match expectation values
  → Fix: Components are ⟨X⟩, ⟨Y⟩, ⟨Z⟩ (Pauli expectations)
  → Why: Bloch vector (x,y,z) = (⟨σx⟩, ⟨σy⟩, ⟨σz⟩)
□ TRAP: reverse_bits parameter on plot_bloch_multivector
  → Fix: reverse_bits=True reverses sphere display order (right-to-left)
  → Why: Matches qubit ordering convention in circuit diagrams

STATE VISUALIZATION TRAPS:
□ TRAP: plot_state_city(counts) → TypeError!
  → Fix: Needs Statevector: plot_state_city(Statevector(qc))
  → Why: State visualization functions need quantum state, not counts
□ TRAP: plot_state_qsphere(state) markers missing for zero-amplitude states
  → Fix: This is correct! Only non-zero amplitudes shown as markers
  → Why: Zero amplitude = zero probability = no marker needed
□ TRAP: Q-sphere is NOT Bloch sphere (conceptual confusion)
  → Fix: Q-sphere shows all basis states on ONE sphere
  → Bloch shows ONE qubit state as single vector
  → Why: Different visualization purposes and representations
□ TRAP: Q-sphere marker color doesn't match phase angle
  → Fix: Color scheme: Red = 0°, Green = 120°, Blue = 240°
  → Why: HSV color wheel mapped to phase angle [0, 2π)
□ TRAP: plot_state_city bar heights don't sum to 1
  → Fix: Bars show amplitude magnitude, not probability!
  → Why: Probability = |amplitude|^2, so sum of |amp|^2 = 1
□ TRAP: plot_state_hinton square size represents what?
  → Fix: Square size = amplitude magnitude, color = sign/phase
  → Why: Hinton diagram optimized for density matrix visualization
□ TRAP: plot_state_paulivec shows values outside [-1, 1]
  → Fix: This indicates error; Pauli expectations must be in [-1, 1]
  → Why: Expectation values of Hermitian operators are bounded
□ TRAP: State visualization functions return None instead of Figure
  → Fix: fig = plot_state_city(state) captures Figure object
  → Why: Some versions/configs may display without returning Figure

MEASUREMENT VISUALIZATION TRAPS:
□ TRAP: plot_histogram(Statevector(qc)) → TypeError!
  → Fix: Needs counts dict: plot_histogram(counts)
  → Why: Histogram visualizes empirical measurement data, not state
□ TRAP: plot_histogram vs plot_distribution look the same
  → Fix: Histogram shows raw counts (integers), distribution shows probabilities (sum=1)
  → Why: Different y-axis scales and interpretations
□ TRAP: plot_histogram([counts1, counts2]) bars overlap/hidden
  → Fix: Use legend parameter to distinguish: legend=['A', 'B']
  → Why: Multiple datasets plotted side-by-side need labels
□ TRAP: sort='hamming' without target_string does nothing
  → Fix: Provide target_string: sort='hamming', target_string='00'
  → Why: Hamming sort needs reference string for distance calculation
□ TRAP: number_to_keep parameter cuts off relevant outcomes
  → Fix: Adjust number_to_keep or use sort to prioritize important outcomes
  → Why: Only keeps top N by count, may miss rare but important states
□ TRAP: plot_histogram bar labels overlap when many outcomes
  → Fix: Use bar_labels=False or number_to_keep to reduce clutter
  → Why: Too many labels cause overlapping text
□ TRAP: Histogram x-axis shows outcomes in unexpected order
  → Fix: Use sort='value' for binary order, 'asc'/'desc' for count order
  → Why: Default sorting may not match desired presentation
□ TRAP: plot_distribution converts counts automatically (surprising)
  → Fix: This is correct! Distribution normalizes counts to probabilities
  → Why: plot_distribution computes sum and divides each count
□ TRAP: Comparing histograms with different shot counts misleading
  → Fix: Use plot_distribution for fair comparison (normalized)
  → Why: Absolute counts not comparable with different shot totals

BACKEND VISUALIZATION TRAPS:
□ TRAP: plot_gate_map(backend) vs plot_coupling_map(coupling_map)
  → Fix: plot_gate_map takes Backend object, plot_coupling_map takes CouplingMap
  → Why: Different input types for different use cases
□ TRAP: plot_gate_map shows more connections than actual hardware has
  → Fix: This may indicate bidirectional coupling (check backend.coupling_map)
  → Why: Coupling map may have directional edges shown as bidirectional
□ TRAP: plot_circuit_layout(qc, backend) on non-transpiled circuit fails
  → Fix: Must transpile first: transpiled_qc = transpile(qc, backend)
  → Why: Layout information only exists after transpilation
□ TRAP: plot_coupling_map with empty list shows no graph
  → Fix: Provide valid edge list: [[0,1], [1,2], [2,3], ...]
  → Why: Empty coupling map = no connections to visualize
□ TRAP: Backend qubit numbering doesn't match visual layout
  → Fix: Physical layout arbitrary; use plot_gate_map to see actual positions
  → Why: Qubit labels are logical, physical positions hardware-specific

DEPRECATED API TRAPS:
□ TRAP: Using qiskit.visualization.circuit_drawer() instead of qc.draw()
  → Fix: Use qc.draw() (modern API)
  → Why: circuit_drawer() is deprecated, qc.draw() is preferred
□ TRAP: Using qiskit.tools.visualization imports (old location)
  → Fix: from qiskit.visualization import plot_histogram
  → Why: Visualization tools moved from qiskit.tools to qiskit.visualization
□ TRAP: Using plot_state_city with title parameter (old API)
  → Fix: Check current API documentation for supported parameters
  → Why: Visualization APIs have changed across Qiskit versions
□ TRAP: StatevectorSampler() vs SamplerV2() confusion
  → Fix: StatevectorSampler is specific implementation of SamplerV2
  → Why: V2 API is interface, StatevectorSampler is local simulator
□ TRAP: Using .get_counts() on deprecated Result object format
  → Fix: Use result[0].data.meas.get_counts() for Sampler V2
  → Why: V2 primitives use different result structure

COMMON MISTAKES:
□ TRAP: Forgetting to import visualization functions
  → Fix: from qiskit.visualization import plot_histogram, plot_bloch_multivector
  → Why: Not auto-imported with main qiskit package
□ TRAP: Not saving figure before it closes in scripts
  → Fix: fig = qc.draw('mpl'); fig.savefig('circuit.png')
  → Why: Interactive plots close before saving in non-notebook environments
□ TRAP: Assuming plot functions automatically display (in scripts)
  → Fix: import matplotlib.pyplot as plt; plt.show()
  → Why: Notebooks auto-display, scripts need explicit plt.show()
□ TRAP: Mixing state visualization and count visualization functions
  → Fix: State plots need Statevector/DensityMatrix, count plots need counts dict
  → Why: Fundamentally different input types for different visualizations
□ TRAP: Not handling matplotlib backend issues (no display)
  → Fix: import matplotlib; matplotlib.use('Agg') for non-GUI environments
  → Why: Some environments don't support GUI backends
```

### 🧠 Mnemonic Recall Box
```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 2 MNEMONICS - MEMORIZE THESE!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 🎨 "MPL for My Pretty Layout"                                    │
│    qc.draw('mpl') = nice graphical output                       │
│    Default qc.draw() = boring text (TEXT is default!)          │
│    Think: "Make it Pretty with mpl, not plain text"            │
│                                                                  │
│ 📏 "Reverse Bits = Reading Order"                                │
│    reverse_bits=True → MSB (highest qubit index) on TOP         │
│    Think: "Reverse = Read from top-down like physics books"    │
│    Example: q[2] on top for 3-qubit system (physics style)     │
│    Default False → q[0] on top (computational style)            │
│                                                                  │
│ 🚫 "No M before S" (No Measure before Statevector)               │
│    Statevector needs measurement-FREE circuit                   │
│    Measurements collapse → gives you post-measurement state     │
│    Think: "State Vector Sees Everything (before measuring)"    │
│    Mnemonic: SVS = State Vector Sees (no measurement collapse) │
│                                                                  │
│ 📐 "Style ONLY with MPL" (Style parameter restriction)           │
│    style='iqp' or style='bw' only works with output='mpl'      │
│    Think: "Styling requires matplotlib canvas"                 │
│    Text/LaTeX ignore style parameter silently!                 │
│                                                                  │
│ 👁️ "State = IS, Sample = SEE"                                    │
│    Statevector = what the state IS (exact amplitudes & phase)  │
│    StatevectorSampler = what we would SEE (measurement counts) │
│    Think: "IS before SEE" (compute state, then sample it)      │
│    Statevector: math/theory | Sampler: experiment/observation  │
│                                                                  │
│ 🔬 "Sampler needs Something to Measure"                          │
│    StatevectorSampler requires circuit WITH measurements        │
│    Think: "Sample = See outcomes = need measurement operation"  │
│    No measurements → no classical bits → no counts dict!        │
│                                                                  │
│ 📊 "Histogram = How many times"                                  │
│    plot_histogram shows RAW integer counts (not probabilities)  │
│    Think: "Histogram = Historical count of occurrences"         │
│    Needs counts dict {'00': 512, '01': 488}, NOT Statevector!  │
│    Distribution normalizes (probabilities sum to 1)             │
│                                                                  │
│ 🎯 "Distribution = Divide by total"                              │
│    plot_distribution shows normalized probabilities (sum = 1)   │
│    Think: "Distribution Divides counts by total shots"          │
│    Auto-converts counts to probabilities (helpful!)             │
│                                                                  │
│ 🔗 "Center = Correlated/Confused"                                │
│    Arrow at center of Bloch sphere = entangled/mixed state      │
│    Think: "Confused qubit = can't point anywhere = entangled"   │
│    This is EXPECTED for Bell states (|Φ+⟩, |Ψ-⟩, etc.)         │
│    Reduced density matrix ρ = I/2 (maximally mixed)            │
│    Not a bug! Shows lack of local information about qubit      │
│                                                                  │
│ 🏙️ "City shows Complex heights"                                  │
│    plot_state_city = 3D bars for amplitude magnitudes           │
│    Think: "City skyline = Complex amplitude landscape"          │
│    Real and imaginary parts on different axes                   │
│    Bar height = |amplitude|, color indicates phase             │
│    Great for seeing exact amplitude values (not just probs)    │
│                                                                  │
│ 🌐 "Q-sphere = Quantity + hue (phase)"                           │
│    Marker Size = Quantity (probability |ψ|²)                    │
│    Marker Color = phase angle (hue = angle)                     │
│    Think: "Quality = Quantity × Phase information"              │
│    One sphere, multiple markers (one per basis state)           │
│    HSV color wheel: Red=0°, Green=120°, Blue=240°              │
│                                                                  │
│ ⚖️ "Bloch = One Ball per qubit"                                  │
│    plot_bloch_multivector: one Bloch sphere PER qubit           │
│    Think: "Bloch = individual Ball for each qubit"              │
│    Each sphere shows single-qubit reduced density matrix        │
│    NOT the same as Q-sphere (different purposes!)               │
│                                                                  │
│ 🚫 "Q vs B: One vs Each"                                         │
│    Q-sphere: ONE sphere, many markers (all basis states)        │
│    Bloch: EACH qubit gets own sphere (reduced states)           │
│    Think: "Q=single sphere, B=Ball per qubit"                   │
│    Q-sphere shows global state, Bloch shows local states        │
│                                                                  │
│ 🧮 "State.data[i] = amplitude of |i⟩"                            │
│    Statevector indexing: state.data[3] = amplitude of |11⟩      │
│    Think: "Index in binary = basis state"                       │
│    Example: 3 = 0b11 = |11⟩, 5 = 0b101 = |101⟩                 │
│    Little-endian: rightmost bit is qubit 0                      │
│                                                                  │
│ 🎲 "Shots = Statistical noise"                                   │
│    More shots = less statistical uncertainty (√shots)           │
│    Think: "S for Shots = S for Statistical accuracy"            │
│    1000 shots → ±3% uncertainty, 10000 shots → ±1%             │
│    Statevector exact, Sampler has sampling noise                │
│                                                                  │
│ 🔄 "Evolve returns NEW (doesn't mutate)"                         │
│    state.evolve(gate) returns NEW Statevector                   │
│    Think: "Evolution creates new timeline (immutable)"          │
│    Don't do: state.evolve(H) - this loses the result!          │
│    Do: new_state = state.evolve(H)                              │
│                                                                  │
│ 🗺️ "Gate Map = Graph of qubit connections"                       │
│    plot_gate_map shows which qubits can interact (edges)        │
│    Think: "Map shows roads (connections) between cities"        │
│    Critical for transpilation (routing 2-qubit gates)           │
│    Takes Backend object: plot_gate_map(backend)                 │
│                                                                  │
│ 🔌 "Coupling Map = CouplingMap object"                           │
│    plot_coupling_map takes CouplingMap, not Backend             │
│    Think: "Coupling needs CouplingMap (explicit object)"        │
│    Both show connectivity, different input types!               │
│    plot_coupling_map([[0,1], [1,2], ...]) or CouplingMap       │
│                                                                  │
│ 📦 "Layout needs Transpiled circuit"                             │
│    plot_circuit_layout requires transpiled circuit              │
│    Think: "Layout = where gates Live After Transpilation"       │
│    Original circuit has no physical qubit assignment            │
│    Transpilation maps virtual qubits → physical qubits          │
│                                                                  │
│ 🎨 "Fold = Line break after N columns"                           │
│    fold=20 wraps circuit diagram after 20 columns               │
│    Think: "Fold paper after N gates"                            │
│    fold=-1 (default) = no folding (one long line)               │
│    Only works with output='mpl', ignored for text               │
│                                                                  │
│ 👻 "idle_wires=False hides unused wires"                         │
│    idle_wires=False removes empty wires from diagram            │
│    Think: "Idle workers go home (hidden)"                       │
│    Useful for cleaner diagrams with many qubits                 │
│    Default True = show all wires even if unused                 │
│                                                                  │
│ 🎯 "probabilities() returns array, probabilities_dict() returns dict" │
│    state.probabilities() → numpy array [p0, p1, p2, ...]       │
│    state.probabilities_dict() → dict {'00': 0.5, '01': 0.5}    │
│    Think: "dict has string keys, array has integer indices"    │
│    Array order: [|00⟩, |01⟩, |10⟩, |11⟩] (binary value order)  │
│                                                                  │
│ 🧪 "Statevector = Exact, Sampler = Statistical"                  │
│    Statevector: deterministic, exact amplitudes (no noise)      │
│    Sampler: probabilistic, shot noise (like real experiments)   │
│    Think: "Theory (exact) vs Experiment (noisy)"                │
│    Use Statevector for learning, Sampler for realistic results  │
│                                                                  │
│ 🌍 "Global phase = Invisible to measurements"                    │
│    |ψ⟩ and e^(iθ)|ψ⟩ give identical measurement statistics     │
│    Think: "Global phase = Ghost (physically unobservable)"      │
│    Only relative phases between amplitudes matter               │
│    state.data shows global phase, probabilities() ignores it    │
│                                                                  │
│ 🔢 "result[0] gets first PubResult"                              │
│    sampler.run([qc1, qc2]) returns result with multiple entries │
│    Think: "Array index for each input circuit"                  │
│    result[0] = first circuit, result[1] = second circuit        │
│    Each PubResult has .data.meas.get_counts()                   │
│                                                                  │
│ 📝 "Register name determines data attribute"                     │
│    Default: result[0].data.meas.get_counts()                    │
│    Custom: result[0].data.my_register.get_counts()              │
│    Think: "Data attribute named after register"                 │
│    Default register name is 'meas' if not specified             │
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
║  🎨 CIRCUIT DRAWING (qc.draw())                                        ║
║  ├─ OUTPUT FORMATS                                                     ║
║  │  ├─ qc.draw() = 'text' (DEFAULT - exam trap!)                      ║
║  │  ├─ qc.draw('mpl') = matplotlib Figure (graphical)                 ║
║  │  ├─ qc.draw('latex') = LaTeX rendering (needs LaTeX installed)     ║
║  │  └─ qc.draw('latex_source') = raw LaTeX string                     ║
║  ├─ KEY PARAMETERS (output='mpl' required for most!)                  ║
║  │  ├─ reverse_bits=True → MSB (q[n-1]) on top (physics convention)   ║
║  │  ├─ reverse_bits=False → LSB (q[0]) on top (default, computation)  ║
║  │  ├─ style='iqp'/'bw'/'clifford' → visual styling (mpl only!)       ║
║  │  ├─ fold=20 → wrap after 20 columns (mpl only)                     ║
║  │  ├─ idle_wires=False → hide unused wires                           ║
║  │  ├─ with_layout=True → show physical qubits (needs transpiled!)    ║
║  │  ├─ initial_state=True → show |0⟩ labels on left                   ║
║  │  ├─ plot_barriers=True/False → show/hide barriers                  ║
║  │  ├─ scale=1.5 → enlarge figure (mpl only)                          ║
║  │  ├─ filename='circuit.png' → save to file (add extension!)         ║
║  │  └─ cregbundle=True → bundle classical wires                       ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ Default is TEXT, not 'mpl'! Must explicitly use qc.draw('mpl') ║
║     ├─ style parameter ignored when output='text' or 'latex'          ║
║     ├─ with_layout=True needs transpiled circuit (not original!)      ║
║     └─ filename needs full extension: 'file.png' not just 'file'      ║
║                                                                        ║
║  📊 STATEVECTOR (Exact Quantum State - NO measurements!)               ║
║  ├─ CREATION & REQUIREMENTS                                            ║
║  │  ├─ from qiskit.quantum_info import Statevector                    ║
║  │  ├─ state = Statevector(qc) → circuit must have NO measurements    ║
║  │  ├─ state = Statevector([1,0,0,0]) → from array (|00⟩)            ║
║  │  ├─ state = Statevector.from_label('01') → from label string       ║
║  │  └─ state = Statevector.from_int(3, 4) → |0011⟩ (int=3, 4 qubits) ║
║  ├─ KEY METHODS & ATTRIBUTES                                           ║
║  │  ├─ state.data → numpy array of complex amplitudes (shape: 2^n)    ║
║  │  ├─ state.data[i] → amplitude of basis state |i⟩ (binary index)    ║
║  │  ├─ state.probabilities() → array [p0, p1, p2, ...] (real-valued)  ║
║  │  ├─ state.probabilities_dict() → dict {'00': 0.5, '01': 0.5, ...}  ║
║  │  ├─ state.evolve(gate) → returns NEW Statevector (immutable!)      ║
║  │  ├─ state.is_valid() → check normalization (sum |amp|² = 1)        ║
║  │  ├─ state.expectation_value(Pauli('ZZ')) → compute ⟨ψ|O|ψ⟩         ║
║  │  ├─ state.sample_counts(shots=1024) → simulate measurements        ║
║  │  └─ state.draw('city'/'qsphere'/'bloch') → visualize state         ║
║  ├─ LIMITATIONS & CONSTRAINTS                                          ║
║  │  ├─ Exponential memory: O(2^n) → max ~30 qubits practical          ║
║  │  ├─ Classical simulation only (not real hardware)                  ║
║  │  ├─ Measurements collapse state (remove before Statevector!)       ║
║  │  └─ Global phase present but unobservable in measurements           ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ Statevector(qc) with measurements → collapsed state! Remove!   ║
║     ├─ state.evolve(gate) doesn't mutate! Use: new = state.evolve()   ║
║     ├─ state.draw('bloch') only works for SINGLE qubit states         ║
║     ├─ state.data[3] = |11⟩ amplitude (binary: 3 = 0b11)              ║
║     └─ Global phase e^(iθ)|ψ⟩ invisible in probabilities              ║
║                                                                        ║
║  🔬 STATEVECTORSAMPLER (Simulated Measurements - WITH measurements!)   ║
║  ├─ SETUP & EXECUTION                                                  ║
║  │  ├─ from qiskit.primitives import StatevectorSampler               ║
║  │  ├─ sampler = StatevectorSampler() → create instance               ║
║  │  ├─ sampler = StatevectorSampler(default_shots=2048) → set shots   ║
║  │  ├─ sampler = StatevectorSampler(seed=42) → reproducible random    ║
║  │  ├─ job = sampler.run([qc]) → qc MUST have measurements!           ║
║  │  ├─ job = sampler.run([qc], shots=1000) → override default shots   ║
║  │  └─ job = sampler.run([qc1, qc2, qc3]) → batch execution           ║
║  ├─ RESULT EXTRACTION                                                  ║
║  │  ├─ result = job.result() → get PrimitiveResult                    ║
║  │  ├─ pub_result = result[0] → get first PubResult (one per circuit) ║
║  │  ├─ pub_result.data.meas → BitArray of outcomes (default register) ║
║  │  ├─ counts = pub_result.data.meas.get_counts() → {'00': 512, ...}  ║
║  │  ├─ bitstrings = pub_result.data.meas.get_bitstrings() → ['00'...] ║
║  │  ├─ pub_result.data.<register_name>.get_counts() → custom register ║
║  │  ├─ pub_result.data.meas.num_shots → total shots (int)             ║
║  │  └─ pub_result.data.meas.num_bits → number of classical bits       ║
║  ├─ KEY CONCEPTS                                                       ║
║  │  ├─ Ideal simulation (no noise, perfect gates)                     ║
║  │  ├─ Statistical sampling (shot noise ~1/√shots)                    ║
║  │  ├─ Probabilistic outcomes (not exact like Statevector)            ║
║  │  └─ Classical simulation of quantum measurements                   ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ Circuit without measurements → empty results! Must measure!    ║
║     ├─ Need .result() call: job.result()[0].data.meas.get_counts()    ║
║     ├─ shots=1000 doesn't give exact 500/500 split (statistical!)     ║
║     ├─ Custom register: use .data.<name> not .data.meas               ║
║     └─ get_counts() dict omits zero-count keys (check with .get())    ║
║                                                                        ║
║  🌐 STATE VISUALIZATION (Needs Statevector/DensityMatrix - NO counts!) ║
║  ├─ BLOCH SPHERE (Individual Qubit States)                             ║
║  │  ├─ from qiskit.visualization import plot_bloch_multivector        ║
║  │  ├─ plot_bloch_multivector(state) → one sphere per qubit           ║
║  │  ├─ Each sphere shows single-qubit reduced density matrix          ║
║  │  ├─ Pure states: vector on surface (radius = 1)                    ║
║  │  ├─ Mixed states: vector inside sphere (radius < 1)                ║
║  │  ├─ Entangled qubits: arrow at CENTER (maximally mixed ρ = I/2)    ║
║  │  ├─ North pole = |0⟩, South = |1⟩, X-axis = |+⟩/|-⟩                ║
║  │  └─ Bloch coordinates: (x,y,z) = (⟨X⟩, ⟨Y⟩, ⟨Z⟩) Pauli expectations ║
║  ├─ Q-SPHERE (Global State with Phase)                                 ║
║  │  ├─ from qiskit.visualization import plot_state_qsphere            ║
║  │  ├─ plot_state_qsphere(state) → ONE sphere, multiple markers       ║
║  │  ├─ Marker size = probability |ψ_i|²                               ║
║  │  ├─ Marker color = phase angle (HSV: Red=0°, Green=120°, Blue=240°)║
║  │  ├─ One marker per non-zero basis state                            ║
║  │  └─ NOT the same as Bloch sphere! (Different purpose/representation)║
║  ├─ STATE CITY (3D Amplitude Bars)                                     ║
║  │  ├─ from qiskit.visualization import plot_state_city               ║
║  │  ├─ plot_state_city(state) → 3D bar chart (city skyline)           ║
║  │  ├─ Bar height = amplitude magnitude |ψ_i|                         ║
║  │  ├─ Bar color = phase angle                                        ║
║  │  ├─ Real and imaginary projections on different axes               ║
║  │  └─ Great for seeing exact amplitude values (not just probs)       ║
║  ├─ OTHER STATE VISUALIZATIONS                                         ║
║  │  ├─ plot_state_hinton(state) → density matrix as colored squares   ║
║  │  ├─ plot_state_paulivec(state) → Pauli operator expectations       ║
║  │  └─ All require Statevector/DensityMatrix (NOT counts dict!)       ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ plot_bloch_multivector(counts) → TypeError! Needs Statevector  ║
║     ├─ plot_state_city(counts) → TypeError! Needs Statevector         ║
║     ├─ Entangled qubits at center is CORRECT (not a bug!)             ║
║     ├─ Q-sphere ≠ Bloch: One sphere vs One-per-qubit                  ║
║     └─ State city bars: sum of |amp|² = 1 (not sum of |amp|)          ║
║                                                                        ║
║  📊 MEASUREMENT VISUALIZATION (Needs counts dict - WITH measurements!) ║
║  ├─ HISTOGRAM (Raw Counts)                                             ║
║  │  ├─ from qiskit.visualization import plot_histogram                ║
║  │  ├─ plot_histogram(counts) → bar chart of integer counts           ║
║  │  ├─ plot_histogram([counts1, counts2], legend=['A','B']) → compare ║
║  │  ├─ Parameters: title, bar_labels, sort, target_string, color      ║
║  │  ├─ sort options: 'asc'/'desc'/'value'/'hamming'                   ║
║  │  ├─ number_to_keep=10 → show only top 10 outcomes                  ║
║  │  └─ Shows empirical frequencies (not probabilities)                ║
║  ├─ DISTRIBUTION (Normalized Probabilities)                            ║
║  │  ├─ from qiskit.visualization import plot_distribution             ║
║  │  ├─ plot_distribution(counts) → normalized probabilities (sum=1)   ║
║  │  ├─ Automatically converts counts to probabilities                 ║
║  │  ├─ Same parameters as plot_histogram                              ║
║  │  └─ Better for comparing runs with different shot counts           ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ plot_histogram(Statevector(qc)) → TypeError! Needs counts!     ║
║     ├─ plot_histogram vs plot_distribution: counts vs probabilities   ║
║     ├─ Comparing different shot counts: use distribution (normalized) ║
║     ├─ sort='hamming' needs target_string parameter                   ║
║     └─ Missing dict keys (zero counts) need .get(key, 0) handling     ║
║                                                                        ║
║  🗺️ BACKEND VISUALIZATION (Hardware Topology)                          ║
║  ├─ GATE MAP (Qubit Connectivity)                                      ║
║  │  ├─ from qiskit.visualization import plot_gate_map                 ║
║  │  ├─ plot_gate_map(backend) → takes Backend object                  ║
║  │  ├─ Shows which qubits can directly interact (coupling map)        ║
║  │  ├─ Critical for understanding transpilation constraints           ║
║  │  └─ Parameters: figsize, plot_directed, label_qubits, filename     ║
║  ├─ COUPLING MAP                                                       ║
║  │  ├─ from qiskit.visualization import plot_coupling_map             ║
║  │  ├─ plot_coupling_map(coupling_map) → takes CouplingMap object     ║
║  │  ├─ plot_coupling_map([[0,1], [1,2], ...]) → edge list             ║
║  │  └─ Same visualization, different input type than plot_gate_map    ║
║  ├─ CIRCUIT LAYOUT                                                     ║
║  │  ├─ from qiskit.visualization import plot_circuit_layout           ║
║  │  ├─ plot_circuit_layout(transpiled_qc, backend)                    ║
║  │  ├─ Shows virtual-to-physical qubit mapping                        ║
║  │  └─ Requires TRANSPILED circuit (not original!)                    ║
║  └─ COMMON TRAPS                                                       ║
║     ├─ plot_gate_map(backend) vs plot_coupling_map(CouplingMap)       ║
║     ├─ plot_circuit_layout needs transpiled circuit (not original!)   ║
║     └─ Physical qubit numbering may not match visual layout           ║
║                                                                        ║
║  ⚠️⚠️⚠️ TOP 15 EXAM TRAPS - MEMORIZE THESE! ⚠️⚠️⚠️                        ║
║  1.  qc.draw() DEFAULT is TEXT, not 'mpl'! Use qc.draw('mpl')         ║
║  2.  style='iqp' IGNORED with text/latex! Only works with output='mpl'║
║  3.  Statevector(qc) with measurements → COLLAPSED state! Remove them!║
║  4.  StatevectorSampler without measurements → EMPTY results! Add them║
║  5.  plot_histogram(Statevector) → TypeError! Needs counts dict       ║
║  6.  plot_bloch_multivector(counts) → TypeError! Needs Statevector    ║
║  7.  Entangled qubits show arrow at CENTER on Bloch → this is CORRECT!║
║  8.  Q-sphere ≠ Bloch sphere (one sphere vs one-per-qubit)            ║
║  9.  reverse_bits=True puts MSB (q[n-1]) on TOP, not q[0]             ║
║  10. state.evolve(gate) returns NEW state (doesn't mutate original!)  ║
║  11. plot_circuit_layout needs TRANSPILED circuit (not original!)     ║
║  12. plot_gate_map(backend) vs plot_coupling_map(CouplingMap) inputs  ║
║  13. filename='circuit' needs extension: 'circuit.png' or 'circuit.pdf'║
║  14. with_layout=True needs transpiled circuit (no layout before!)    ║
║  15. result[0].data.meas for default, .data.<name> for custom register║
║                                                                        ║
║  🔄 STATEVECTOR vs STATEVECTORSAMPLER - KEY DIFFERENCES                ║
║  ┌──────────────────────┬─────────────────────┬──────────────────────┐ ║
║  │ Feature              │ Statevector         │ StatevectorSampler   │ ║
║  ├──────────────────────┼─────────────────────┼──────────────────────┤ ║
║  │ Measurements needed? │ NO (remove them!)   │ YES (must have!)     │ ║
║  │ Output type          │ Exact amplitudes    │ Counts dict          │ ║
║  │ Probabilistic?       │ No (deterministic)  │ Yes (shot noise)     │ ║
║  │ Memory scaling       │ Exponential O(2^n)  │ Linear O(n)          │ ║
║  │ Max practical qubits │ ~30 qubits          │ Unlimited (memory)   │ ║
║  │ Use case             │ Theory, learning    │ Realistic simulation │ ║
║  │ Global phase?        │ Yes (in .data)      │ No (unobservable)    │ ║
║  │ Noise model?         │ No (ideal)          │ No (but sampled)     │ ║
║  └──────────────────────┴─────────────────────┴──────────────────────┘ ║
║                                                                        ║
║  💡 QUICK DECISION TREE                                                ║
║  Do you need exact amplitudes? → Use Statevector (NO measurements!)   ║
║  Do you need measurement counts? → Use StatevectorSampler (+ measure!)║
║  Want to visualize state? → State plots (Statevector) or Histogram    ║
║  Want to compare experiment results? → plot_distribution (normalized) ║
║  Drawing circuit diagram? → qc.draw('mpl') with reverse_bits & style  ║
║  Understanding hardware? → plot_gate_map(backend) for connectivity    ║
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
