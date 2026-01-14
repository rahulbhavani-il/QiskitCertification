## ✅ Quantum Operations Key Takeaways

### 📚 Concept Checklist
```
□ Qubit exists in superposition until measured (spinning coin analogy)
□ Measurement collapses superposition to definite state (slapping coin down)
□ Classical bit: Heads OR Tails; Qubit: Heads AND Tails simultaneously
□ Global phase (e^iθ|ψ⟩) is unobservable - affects nothing physically
□ Relative phase (|0⟩+e^iθ|1⟩) matters - causes interference patterns
□ Phase affects interference but NOT measurement probabilities directly
□ Bloch sphere: |0⟩ at North pole, |1⟩ at South pole
□ Equator states: |+⟩, |-⟩ (X-basis), |+i⟩, |-i⟩ (Y-basis)
□ X-basis eigenstates: |+⟩ and |-⟩ with eigenvalues +1 and -1
□ Y-basis eigenstates: |+i⟩=(|0⟩+i|1⟩)/√2 and |-i⟩=(|0⟩-i|1⟩)/√2
□ Z-basis eigenstates: |0⟩ and |1⟩ (computational basis)
□ Pauli-X gate: Bit flip |0⟩↔|1⟩, π rotation around X-axis
□ Pauli-Y gate: Combined flip with complex phases, Y=iXZ relation
□ Pauli-Z gate: Phase flip, Z|0⟩=|0⟩ (unchanged!), Z|1⟩=-|1⟩
□ X flips amplitudes: X(α|0⟩+β|1⟩) = α|1⟩+β|0⟩
□ Z flips phase on |1⟩ component only: Z(α|0⟩+β|1⟩) = α|0⟩-β|1⟩
□ X²=Y²=Z²=I (all Paulis are self-inverse/involutory)
□ Pauli eigenvalues: Always ±1 for all Pauli operators
□ Paulis are Hermitian: X†=X, Y†=Y, Z†=Z
□ Paulis are unitary: X†X=I (preserves quantum state norm)
□ Hadamard creates equal superposition: H|0⟩=|+⟩=(|0⟩+|1⟩)/√2
□ Hadamard acts as basis transformer: computational ↔ X-basis
□ H is self-inverse: H²=I (applying twice returns to original)
□ Hadamard conjugation: HXH=Z, HZH=X (swaps X and Z bases)
□ HYH=-Y (Y picks up minus sign under Hadamard)
□ Hadamard appears in 80%+ of quantum algorithms (superposition creator)
□ S gate: π/2 phase rotation, S|1⟩=i|1⟩, also called √Z
□ T gate: π/4 phase rotation, T|1⟩=e^(iπ/4)|1⟩, also called √S or π/8 gate
□ Phase gate hierarchy: T²=S, S²=Z, T⁴=Z
□ P(λ) gate: General phase gate, P(π/2)=S, P(π/4)=T, P(π)=Z
□ Phase gates only affect |1⟩ component: P(λ)|0⟩=|0⟩, P(λ)|1⟩=e^(iλ)|1⟩
□ S and T are Clifford gates (important for error correction)
□ S† (S-dagger): Inverse of S, rotates phase by -π/2
□ T† (T-dagger): Inverse of T, rotates phase by -π/4
□ Rotation gates: RX(θ), RY(θ), RZ(θ) parameterized by angle θ
□ Rotation gates use HALF-ANGLE formula: cos(θ/2), sin(θ/2) in matrix
□ RX rotates around X-axis on Bloch sphere (like tilting globe east-west)
□ RY rotates around Y-axis (like tilting globe north-south)
□ RZ rotates around Z-axis (like spinning globe on its axis)
□ Special cases: RX(π)=X, RY(π)=Y, RZ(π)=Z (up to global phase)
□ Rotation gates are essential for VQE, QAOA variational algorithms
□ Pauli group: All tensor products of {I,X,Y,Z} with phases {±1, ±i}
□ Pauli class (quantum_info): Algebraic object for calculations, NOT a gate
□ Pauli operators anticommute: XY=-YX, YZ=-ZY, ZX=-XZ
□ Pauli operators commute with themselves: XX=I, XYX=-Y
□ Pauli composition: XY=iZ, YZ=iX, ZX=iY (cyclic with +i)
□ Reverse composition: YX=-iZ, ZY=-iX, XZ=-iY (anti-cyclic with -i)
□ Pauli string ordering: 'XYZ' means X⊗Y⊗Z (RIGHT-TO-LEFT: X on q2!)
□ Pauli phase prefixes: '' = +1, 'i' = +i, '-' = -1, '-i' = -i
□ Pauli X and Z array representation: I=[0,0], X=[1,0], Y=[1,1], Z=[0,1]
□ CNOT gate: Controlled-NOT, flips target if control is |1⟩
□ CNOT creates entanglement when combined with Hadamard
□ CNOT direction matters: CX(control, target) - order is CRITICAL!
□ CNOT truth table: |10⟩→|11⟩ (flip), |11⟩→|10⟩ (flip), |00⟩ and |01⟩ unchanged
□ CNOT is self-inverse: CX²=I (two CNOTs cancel)
□ Bell states: Four maximally entangled 2-qubit states
□ Bell state classification: Φ=same bits (00/11), Ψ=different bits (01/10)
□ Bell state signs: + has plus, - has minus between terms
□ |Φ⁺⟩=(|00⟩+|11⟩)/√2 most common, created by H+CX (just 2 gates!)
□ |Φ⁻⟩=(|00⟩-|11⟩)/√2 has minus sign between terms
□ |Ψ⁺⟩=(|01⟩+|10⟩)/√2 anti-correlated bits
□ |Ψ⁻⟩=(|01⟩-|10⟩)/√2 anti-correlated with minus sign
□ Measuring one Bell state qubit instantly determines the other (entanglement)
□ CZ gate: Controlled-Z, adds -1 phase to |11⟩ state only
□ CZ is symmetric: CZ(0,1)=CZ(1,0) - order doesn't matter!
□ CZ relation: CZ=H·CX·H (Hadamard conjugation of CNOT on target)
□ CZ only affects |11⟩→-|11⟩, all other states unchanged
□ SWAP gate: Exchanges states of two qubits |01⟩↔|10⟩
□ SWAP decomposition: 3 CNOTs required (CX(a,b)·CX(b,a)·CX(a,b))
□ SWAP is expensive on hardware - 3× CNOT cost
□ SWAP is symmetric: SWAP(0,1)=SWAP(1,0)
□ Toffoli gate (CCX): Double-controlled NOT, flips target if BOTH controls=|1⟩
□ Toffoli implements classical AND: Output=1 only if both inputs=1
□ Toffoli decomposition: 6 CNOTs on hardware (very expensive!)
□ Toffoli is reversible - quantum version of classical AND gate
□ Fredkin gate (CSWAP): Controlled-SWAP, swaps targets if control=|1⟩
□ Fredkin decomposition: 8+ gates on hardware (most expensive!)
□ Fredkin conserves Hamming weight (number of |1⟩s unchanged)
□ initialize() prepares arbitrary quantum state from amplitude vector
□ initialize() is expensive - synthesizes many gates for decomposition
□ initialize() is NOT a single gate - it's a gate synthesis routine
□ reset() returns qubit to |0⟩ via measurement + conditional flip
□ reset() is active reset (mid-circuit), not just initialization
□ reset() useful for qubit recycling in long algorithms
□ barrier() is visual separator - NO quantum effect whatsoever!
□ barrier() blocks transpiler optimization across it (debugging tool)
□ barrier() does NOT collapse superposition or affect state
□ GHZ state: Multi-qubit entangled state (|000⟩+|111⟩)/√2 for 3 qubits
□ GHZ creation: H on first qubit + CNOT cascade to others
```

### 💻 Code Pattern Checklist
```
□ from qiskit import QuantumCircuit imports circuit class
□ qc = QuantumCircuit(n) creates n-qubit circuit
□ qc = QuantumCircuit(n, m) creates n qubits, m classical bits
□ qc.x(qubit) applies Pauli-X (bit flip) to specified qubit
□ qc.x(0) applies X to qubit 0 (zero-indexed)
□ qc.y(qubit) applies Pauli-Y (bit + phase flip with ±i factors)
□ qc.z(qubit) applies Pauli-Z (phase flip, Z|0⟩=|0⟩, Z|1⟩=-|1⟩)
□ qc.h(qubit) applies Hadamard (creates superposition from basis states)
□ qc.h(0); qc.h(1); qc.h(2) creates uniform superposition on 3 qubits
□ for i in range(n): qc.h(i) applies Hadamard to all n qubits
□ qc.s(qubit) applies S gate (π/2 phase rotation)
□ qc.sdg(qubit) applies S† (S-dagger, inverse: rotates -π/2)
□ qc.t(qubit) applies T gate (π/4 phase rotation)
□ qc.tdg(qubit) applies T† (T-dagger, inverse: rotates -π/4)
□ qc.p(lambda_angle, qubit) applies P(λ) arbitrary phase gate
□ qc.p(np.pi/2, 0) equivalent to S gate (up to global phase)
□ qc.p(np.pi/4, 0) equivalent to T gate (up to global phase)
□ qc.p(np.pi, 0) equivalent to Z gate
□ qc.rx(theta, qubit) rotates angle θ around X-axis (Bloch sphere)
□ qc.ry(theta, qubit) rotates angle θ around Y-axis
□ qc.rz(theta, qubit) rotates angle θ around Z-axis
□ import numpy as np; qc.rx(np.pi, 0) applies X gate (RX(π)=X)
□ qc.ry(np.pi/2, 0) rotates 90° around Y-axis
□ qc.ry(theta, 0); qc.rz(phi, 0) common VQE ansatz pattern
□ qc.rx(theta, qubit) for qubit in range(n) applies RX to all qubits
□ qc.cx(control, target) applies CNOT (control FIRST parameter!)
□ qc.cx(0, 1) flips qubit 1 if qubit 0 is |1⟩
□ qc.cnot(control, target) alternative name for CNOT (same as cx)
□ qc.h(0); qc.cx(0, 1) creates Bell state |Φ⁺⟩ = (|00⟩+|11⟩)/√2
□ qc.x(0); qc.h(0); qc.cx(0, 1) creates Bell state |Φ⁻⟩
□ qc.h(0); qc.cx(0, 1); qc.x(1) creates Bell state |Ψ⁺⟩
□ qc.x(0); qc.h(0); qc.cx(0, 1); qc.x(1) creates Bell state |Ψ⁻⟩
□ for i in range(n-1): qc.cx(i, i+1) creates CNOT chain
□ qc.h(0); for i in range(1,n): qc.cx(0,i) creates GHZ state
□ qc.cz(qubit1, qubit2) applies CZ gate (order doesn't matter!)
□ qc.cz(0, 1) equivalent to qc.cz(1, 0) - symmetric
□ qc.h(1); qc.cx(0, 1); qc.h(1) equivalent to qc.cz(0, 1)
□ qc.swap(qubit1, qubit2) swaps states of two qubits
□ qc.swap(0, 1) exchanges |01⟩↔|10⟩
□ qc.ccx(control1, control2, target) applies Toffoli (double-controlled NOT)
□ qc.toffoli(c1, c2, target) alternative name for Toffoli
□ qc.ccx(0, 1, 2) flips qubit 2 if both qubits 0 AND 1 are |1⟩
□ qc.cswap(control, target1, target2) applies Fredkin (controlled-SWAP)
□ qc.fredkin(control, t1, t2) alternative name for Fredkin
□ qc.cswap(0, 1, 2) swaps qubits 1↔2 if qubit 0 is |1⟩
□ qc.initialize(state_vector, qubits) prepares arbitrary state from amplitudes
□ qc.initialize([1, 0], 0) prepares |0⟩ state
□ qc.initialize([0, 1], 0) prepares |1⟩ state
□ qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0) prepares |+⟩ state
□ qc.initialize([1/np.sqrt(2), -1/np.sqrt(2)], 0) prepares |-⟩ state
□ state = [0.5, 0.5, 0.5, 0.5]; qc.initialize(state, [0,1]) equal superposition
□ qc.reset(qubit) resets qubit to |0⟩ via measurement + conditional X
□ qc.x(0); qc.reset(0) results in |0⟩ (reset always returns |0⟩)
□ qc.barrier() adds visual separator (no quantum operation!)
□ qc.barrier([0, 1]) adds barrier on specific qubits only
□ qc.barrier(); qc.measure_all() separates circuit from measurement visually
□ qc.h(0); qc.barrier(); qc.cx(0, 1) prevents optimization across barrier
□ from qiskit.quantum_info import Pauli imports Pauli class
□ p = Pauli('X') creates single-qubit Pauli-X object
□ p = Pauli('Y') creates Pauli-Y, p = Pauli('Z') creates Pauli-Z
□ p = Pauli('I') creates identity operator
□ p = Pauli('XY') creates X⊗Y (X on q1, Y on q0 - RIGHT-TO-LEFT!)
□ p = Pauli('XYZ') creates X⊗Y⊗Z (X on q2, Y on q1, Z on q0)
□ p = Pauli('iX') creates i·X with explicit +i phase
□ p = Pauli('-X') creates -X with minus phase
□ p = Pauli('-iZ') creates -i·Z with -i phase
□ X, Y, Z = Pauli('X'), Pauli('Y'), Pauli('Z') creates three Pauli objects
□ p.num_qubits returns number of qubits (e.g., Pauli('XYZ').num_qubits = 3)
□ p.phase returns phase as integer: 0=+1, 1=+i, 2=-1, 3=-i
□ p.x returns X bitarray [False, True] for Z means X bit = [0,1]
□ p.z returns Z bitarray [True, False] for X means Z bit = [1,0]
□ p1.commutes(p2) returns True if p1·p2 = p2·p1
□ Pauli('X').commutes(Pauli('X')) returns True (XX = XX)
□ Pauli('X').commutes(Pauli('Z')) returns False (XZ ≠ ZX)
□ p1.anticommutes(p2) returns True if p1·p2 = -p2·p1
□ Pauli('X').anticommutes(Pauli('Z')) returns True (XZ = -ZX)
□ (p1 @ p2).to_label() computes composition and returns string label
□ (Pauli('X') @ Pauli('Z')).to_label() returns 'iY' (XZ = iY)
□ (Pauli('Y') @ Pauli('Z')).to_label() returns 'iX' (YZ = iX)
□ (Pauli('Z') @ Pauli('X')).to_label() returns '-iY' (ZX = -iY)
□ p.tensor(q) creates tensor product p⊗q (left to right)
□ Pauli('X').tensor(Pauli('Z')) returns Pauli('XZ')
□ p.expand(n) adds n identity operators: Pauli('X').expand(2) → 'XII'
□ p.to_matrix() converts to numpy array (2^n × 2^n matrix)
□ Pauli('X').to_matrix() returns [[0,1],[1,0]]
□ p.to_instruction() converts Pauli to circuit instruction
□ qc.append(Pauli('XYZ').to_instruction(), [0,1,2]) adds Pauli to circuit
□ p.evolve(gate) returns Pauli after gate conjugation U·P·U†
□ from qiskit.circuit.library import HGate imports Hadamard gate class
□ Pauli('X').evolve(HGate()) returns Pauli('Z') (HXH = Z)
□ Pauli('Z').evolve(HGate()) returns Pauli('X') (HZH = X)
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 1: QUANTUM OPERATIONS - ONE-PAGE SUMMARY                  ║
║                (16% of Exam - ~11 Questions)                          ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  📐 SINGLE-QUBIT GATES (Pauli, Hadamard, Phase, Rotation)             ║
║  ├─ PAULI GATES (X, Y, Z)                                             ║
║  │   • X = bit flip: |0⟩↔|1⟩, qc.x(qubit)                            ║
║  │   • Y = both flips + i phases: Y=iXZ, qc.y(qubit)                 ║
║  │   • Z = phase flip: Z|0⟩=|0⟩, Z|1⟩=-|1⟩, qc.z(qubit)              ║
║  │   • All Paulis: X²=Y²=Z²=I (self-inverse)                         ║
║  ├─ HADAMARD (H) - The Superposition Creator                          ║
║  │   • H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2, qc.h(qubit)                        ║
║  │   • H|1⟩ = |-⟩ = (|0⟩-|1⟩)/√2                                     ║
║  │   • H² = I (self-inverse), HXH = Z, HZH = X                       ║
║  │   • Appears in 80%+ of quantum algorithms!                         ║
║  ├─ PHASE GATES (S, T, P)                                             ║
║  │   • S: π/2 phase, S² = Z, qc.s(qubit), qc.sdg(qubit)              ║
║  │   • T: π/4 phase, T⁴ = Z, T² = S, qc.t(qubit), qc.tdg(qubit)     ║
║  │   • P(λ): Arbitrary phase, qc.p(lambda, qubit)                    ║
║  │   • Relations: P(π/2)=S, P(π/4)=T, P(π)=Z                         ║
║  └─ ROTATION GATES (RX, RY, RZ)                                       ║
║      • qc.rx(θ, qubit), qc.ry(θ, qubit), qc.rz(θ, qubit)            ║
║      • Matrix uses θ/2 (half-angle formula!)                          ║
║      • RX(π)=X, RY(π)=Y, RZ(π)=Z (up to global phase)                ║
║      • Essential for VQE/QAOA variational algorithms                  ║
║                                                                        ║
║  🔗 MULTI-QUBIT GATES (CNOT, CZ, SWAP, Toffoli, Fredkin)              ║
║  ├─ CNOT/CX (Controlled-NOT) - THE Entanglement Creator              ║
║  │   • qc.cx(control, target) - control FIRST parameter!             ║
║  │   • |10⟩→|11⟩, |11⟩→|10⟩ (flips target if control=1)              ║
║  │   • Direction matters: CX(0,1) ≠ CX(1,0)                          ║
║  │   • CX² = I (self-inverse)                                        ║
║  ├─ CZ (Controlled-Z) - Symmetric Phase Gate                          ║
║  │   • qc.cz(q1, q2) - order DOESN'T matter!                         ║
║  │   • CZ(0,1) = CZ(1,0) unlike CNOT                                 ║
║  │   • Only affects |11⟩→-|11⟩                                        ║
║  │   • CZ = H·CX·H (Hadamard conjugate)                              ║
║  ├─ SWAP - Exchange Two Qubits                                        ║
║  │   • qc.swap(q1, q2)                                                ║
║  │   • Decomposes to 3 CNOTs (expensive!)                             ║
║  │   • SWAP = CX(a,b)·CX(b,a)·CX(a,b)                                ║
║  ├─ TOFFOLI (CCX) - Double-Controlled NOT                             ║
║  │   • qc.ccx(c1, c2, target) - quantum AND gate                     ║
║  │   • Flips target if BOTH controls = |1⟩                           ║
║  │   • Decomposes to 6 CNOTs (very expensive!)                        ║
║  └─ FREDKIN (CSWAP) - Controlled-SWAP                                 ║
║      • qc.cswap(control, t1, t2)                                      ║
║      • Swaps t1↔t2 if control = |1⟩                                  ║
║      • Decomposes to 8+ gates (most expensive!)                       ║
║                                                                        ║
║  💕 BELL STATES (Maximally Entangled 2-Qubit States)                  ║
║  ├─ Classification: Φ = same bits (00/11), Ψ = different (01/10)     ║
║  ├─ |Φ⁺⟩ = (|00⟩+|11⟩)/√2                                            ║
║  │   → qc.h(0); qc.cx(0,1)  [Just 2 gates!]                          ║
║  ├─ |Φ⁻⟩ = (|00⟩-|11⟩)/√2                                            ║
║  │   → qc.x(0); qc.h(0); qc.cx(0,1)                                  ║
║  ├─ |Ψ⁺⟩ = (|01⟩+|10⟩)/√2                                            ║
║  │   → qc.h(0); qc.cx(0,1); qc.x(1)                                  ║
║  └─ |Ψ⁻⟩ = (|01⟩-|10⟩)/√2                                            ║
║      → qc.x(0); qc.h(0); qc.cx(0,1); qc.x(1)                         ║
║                                                                        ║
║  🎯 STATE PREPARATION & CIRCUIT CONTROL                                ║
║  ├─ initialize(state_vector, qubits)                                  ║
║  │   • Prepares arbitrary quantum state                               ║
║  │   • Expensive! Synthesizes many gates                              ║
║  │   • Example: qc.initialize([1/√2, 1/√2], 0) → |+⟩                 ║
║  ├─ reset(qubit)                                                       ║
║  │   • Returns qubit to |0⟩ via measurement + conditional X          ║
║  │   • Mid-circuit operation (active reset)                           ║
║  └─ barrier()                                                          ║
║      • Visual separator - NO quantum effect!                          ║
║      • Blocks transpiler optimization                                  ║
║                                                                        ║
║  🧮 PAULI CLASS (qiskit.quantum_info.Pauli)                            ║
║  ├─ Algebraic object for calculations (NOT a circuit gate!)           ║
║  ├─ Creation: Pauli('X'), Pauli('XYZ'), Pauli('iX'), Pauli('-Z')    ║
║  ├─ ⚠️ RIGHT-TO-LEFT order: 'XYZ' = X⊗Y⊗Z (X on q2, Z on q0!)        ║
║  ├─ Methods:                                                           ║
║  │   • p1.commutes(p2) - check if XZ = ZX                            ║
║  │   • p1.anticommutes(p2) - check if XZ = -ZX                       ║
║  │   • (p1 @ p2).to_label() - composition (XZ → 'iY')                ║
║  │   • p.to_matrix() - convert to numpy array                         ║
║  │   • p.to_instruction() - convert to circuit gate                   ║
║  │   • p.evolve(HGate()) - conjugation (X → Z under H)               ║
║  └─ Pauli Algebra:                                                     ║
║      • XY = iZ, YZ = iX, ZX = iY (cyclic +i)                         ║
║      • YX = -iZ, ZY = -iX, XZ = -iY (reverse -i)                     ║
║      • X² = Y² = Z² = I (self-inverse)                               ║
║                                                                        ║
║  📊 KEY IDENTITIES (Must Memorize!)                                    ║
║  ├─ Hadamard: H² = I, HXH = Z, HZH = X, HYH = -Y                     ║
║  ├─ Phase: S² = Z, T² = S, T⁴ = Z                                    ║
║  ├─ Pauli: X² = Y² = Z² = I, Y = iXZ                                 ║
║  ├─ Commutation: XZ = -ZX (anticommute), XX = I (commute)            ║
║  ├─ CNOT: CX² = I (self-inverse)                                     ║
║  └─ Rotation: RX(π) = X, RY(π) = Y, RZ(π) = Z (up to global phase)  ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (Study These Carefully!)                        ║
║  1.  Z|0⟩ = |0⟩ (UNCHANGED!) - Z only adds phase to |1⟩             ║
║  2.  X|+⟩ = |+⟩ (unchanged!) - equal amplitudes swap to same         ║
║  3.  HXH = Z (NOT X!) - Hadamard swaps X↔Z bases                     ║
║  4.  S² = Z (NOT I!), T² = S (NOT Z!), T⁴ = Z                       ║
║  5.  CX(0,1) ≠ CX(1,0) - direction matters! Control FIRST!           ║
║  6.  CZ(0,1) = CZ(1,0) - CZ IS symmetric (unlike CNOT)               ║
║  7.  Pauli('XYZ') - RIGHT-TO-LEFT! (X on q2, Y on q1, Z on q0)      ║
║  8.  X and Z anticommute: XZ = -ZX (NOT XZ = ZX!)                    ║
║  9.  XY = iY (NOT Y!) - must include i phase factor                  ║
║  10. Rotation matrix uses θ/2 (half-angle!), not θ directly          ║
║  11. SWAP = 3 CNOTs (expensive!), not a single gate                  ║
║  12. Toffoli = 6 CNOTs (very expensive!), not 3                      ║
║  13. barrier() has ZERO quantum effect - visual only!                 ║
║  14. initialize() is expensive - synthesizes many gates               ║
║  15. Y|0⟩ = i|1⟩ (NOT |1⟩!) - Y includes complex phases              ║
║                                                                        ║
║  🧠 ESSENTIAL MNEMONICS                                                ║
║  • "X-Men Flip bits, Z-Men flip Phase"                               ║
║  • "Hadamard Makes Plus" (H|0⟩ = |+⟩)                                ║
║  • "S-Squared, T-Fourth" (S²=Z, T⁴=Z)                                ║
║  • "Control BEFORE Target" (qc.cx parameter order)                    ║
║  • "CZ is Symmetric" (no control/target)                              ║
║  • "Phi=same, Psi=different" (Bell state bits)                        ║
║  • "Three CNOTs to SWAP"                                              ║
║  • "Pauli RIGHT-TO-LEFT" (tensor order)                               ║
║  • "Barriers Block optimization, not qubits"                          ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---


## ✅ Visualization Key Takeaways

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

STATEVECTOR FOR VISUALIZATION (See Section 9 for full class details):
□ from qiskit.quantum_info import Statevector  # Main import
□ state = Statevector(qc) creates statevector from circuit (NO measurements!)
□ state = Statevector.from_label('+0') creates (|00⟩ + |10⟩)/√2
□ VISUALIZATION DRAW METHODS:
□ state.draw('text') returns text representation of amplitudes
□ state.draw('latex') returns LaTeX representation
□ state.draw('qsphere') draws Q-sphere visualization
□ state.draw('bloch') draws Bloch sphere (single qubit only!)
□ state.draw('city') draws state city (3D bar chart)
□ state.draw('hinton') draws Hinton diagram
□ state.draw('paulivec') draws Pauli vector (expectation values)
□ HELPER METHODS FOR VISUALIZATION:
□ state.probabilities_dict() returns dict: {'00': 0.5, '01': 0.5, ...}
□ state.sample_counts(shots=1024) simulates measurements, returns counts dict

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
║  📊 STATEVECTOR FOR VISUALIZATION (See Section 9 for full details)     ║
║  ├─ CREATION (NO measurements in circuit!)                             ║
║  │  ├─ from qiskit.quantum_info import Statevector                    ║
║  │  ├─ state = Statevector(qc) → circuit must have NO measurements    ║
║  │  └─ state = Statevector.from_label('01') → from label string       ║
║  ├─ VISUALIZATION METHODS                                              ║
║  │  ├─ state.draw('text'/'latex') → text/LaTeX representation         ║
║  │  ├─ state.draw('qsphere') → Q-sphere (phase + probability)         ║
║  │  ├─ state.draw('bloch') → Bloch sphere (single qubit only!)        ║
║  │  ├─ state.draw('city'/'hinton') → amplitude visualizations         ║
║  │  └─ state.probabilities_dict() → {'00': 0.5, '01': 0.5, ...}       ║
║  └─ VISUALIZATION TRAPS                                                ║
║     ├─ Statevector(qc) with measurements → collapsed state! Remove!   ║
║     └─ state.draw('bloch') only works for SINGLE qubit states         ║
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


## ✅ Create Circuits Key Takeaways

### 📚 Concept Checklist
```
CIRCUIT CREATION CONCEPTS:
□ QuantumCircuit(n, m) creates n qubits, m classical bits (Q before C!)
□ QuantumCircuit argument order: qubits FIRST, classical bits SECOND
□ QuantumCircuit() with no args creates empty circuit (add registers later)
□ QuantumCircuit can accept multiple registers: QuantumCircuit(qr1, qr2, cr)
□ QuantumRegister for named quantum registers (better organization)
□ ClassicalRegister for named classical registers (measurement storage)
□ Registers have .name and .size attributes
□ Qubits initialized to |0⟩ state by default (cannot specify initial state in constructor)
□ Classical bits initialized to 0 by default
□ Circuit objects are mutable (can add gates after creation)
□ Empty circuit has depth=0, size=0, width=0
□ QuantumCircuit.from_qasm_str() creates circuit from OpenQASM string
□ QuantumCircuit.from_qasm_file() loads circuit from QASM file
□ Circuit names can be set: qc.name = 'my_circuit'
□ Global phase tracked separately: qc.global_phase (doesn't affect measurements)

CIRCUIT PROPERTY CONCEPTS:
□ depth() = longest path through circuit (critical path length)
□ depth() includes ALL operations: gates, measurements, barriers
□ Parallel gates on different qubits share the same depth layer
□ Sequential gates on same qubit increase depth
□ Barrier gates add 0 to depth (they don't affect critical path)
□ size() = total operation count (sum of all gates + measurements)
□ size() includes barriers, measurements, all instructions
□ width() = total number of wires (qubits + classical bits)
□ width() = num_qubits + num_clbits (property calculation)
□ num_qubits is a PROPERTY (no parentheses!) returns int
□ num_clbits is a PROPERTY (no parentheses!) returns int
□ num_parameters returns count of unbound parameters (property)
□ count_ops() returns dict with gate counts: {'h': 2, 'cx': 3}
□ count_ops() does NOT include parameter information
□ Depth calculation: parallel ops = 1 layer, sequential = multiple layers
□ Empty circuit metrics: depth=0, size=0, width=total wires

COMPOSITION CONCEPTS:
□ compose() = sequential combination (gates applied one after another)
□ compose() operates on SAME qubits (width unchanged)
□ compose() default: appends qc2 after qc1 (front=False)
□ compose() with front=True prepends qc2 before qc1
□ compose() with qubits=[...] maps to specific target qubits
□ compose() with clbits=[...] maps classical bits
□ compose() with inplace=True modifies original circuit
□ compose() with inplace=False returns new circuit (default)
□ compose() preserves gate order and dependencies
□ compose() can map smaller circuit to subset of larger circuit
□ tensor() = parallel combination (side-by-side circuits)
□ tensor() ADDS qubits (width increases by qc2.num_qubits)
□ tensor() creates independent subsystems (no interaction)
□ tensor() equivalent to tensor product notation: qc1 ⊗ qc2
□ tensor() qubits from qc2 added after qc1's qubits
□ tensor() classical bits also concatenated
□ append() adds single instruction/gate to circuit
□ append() requires qubit list argument (even for single qubit)
□ append() can add custom gates, barriers, measurements
□ append() preserves instruction order (sequential addition)
□ Composition is associative: (A∘B)∘C = A∘(B∘C)
□ Tensor product is associative: (A⊗B)⊗C = A⊗(B⊗C)

PARAMETERIZED CIRCUIT CONCEPTS:
□ Parameter = symbolic placeholder for gate rotation angles
□ Parameter acts like variable in algebra (unbound value)
□ Parameter has .name attribute (string identifier)
□ Parameter identity matters: Parameter('θ') twice = TWO parameters!
□ Same name ≠ same parameter object (object identity, not string equality)
□ ParameterVector = efficient creation of multiple related parameters
□ ParameterVector creates indexed parameters: θ[0], θ[1], θ[2]...
□ ParameterVector useful for ansätze with many parameters
□ Parameters can appear in mathematical expressions: 2*theta, theta+phi
□ Parameter expressions supported: sin(theta), cos(theta), theta**2
□ Parameters must be bound before circuit execution (no unbound params on hardware)
□ Binding creates new circuit with concrete values (doesn't mutate original)
□ assign_parameters() is modern API (bind_parameters deprecated)
□ Partial binding allowed (bind subset of parameters)
□ qc.parameters returns ParameterView (set-like) of unbound parameters
□ len(qc.parameters) == 0 indicates fully bound circuit
□ Parameters enable variational algorithms (VQE, QAOA)
□ Parameters allow circuit reuse with different values
□ Parameter binding preserves circuit structure
□ Unbound parameters prevent transpilation (transpiler needs concrete angles)

CLASSICAL CONTROL CONCEPTS:
□ c_if() = legacy conditional execution (deprecated but still supported)
□ c_if() syntax: gate.c_if(clbit, value) - gate method first, then condition
□ c_if() operates on classical bit or classical register
□ c_if() register value interpreted as INTEGER (binary representation)
□ c_if() example: cr==3 means binary '11' (both bits set to 1)
□ c_if() condition evaluated at runtime (dynamic decision)
□ if_test() = modern conditional (context manager API)
□ if_test() requires TUPLE syntax: (clbit, value) not clbit, value
□ if_test() supports if-else blocks with 'as else_:' syntax
□ if_test() integrates with expr module for complex conditions
□ if_test() can test individual bits or full registers
□ expr.logic_and(), expr.logic_or() combine conditions
□ expr.equal(), expr.not_equal() for equality testing
□ expr.less(), expr.greater() for comparisons
□ Measurements must happen BEFORE conditionals (condition needs measured value)
□ Conditional gates only execute if condition is true
□ Conditional execution adds to circuit depth (branch taken)
□ Classical bits hold measurement outcomes (0 or 1)
□ Classical registers combine bits into integer values
□ Bit indexing: cr[0] is least significant bit (LSB)
□ Register interpretation: big-endian for bit ordering

DYNAMIC CIRCUIT CONCEPTS:
□ Dynamic circuits = circuits with runtime control flow
□ for_loop() executes block for fixed number of iterations
□ for_loop() syntax: with qc.for_loop(range(n)):
□ for_loop() loop variable can be used in block (parameter)
□ while_loop() executes while condition remains true
□ while_loop() syntax: with qc.while_loop((clbit, value)):
□ while_loop() condition checked at runtime (measurement-based)
□ switch() enables multi-way branching (multiple cases)
□ switch() syntax: with qc.switch(creg) as case:
□ switch() cases can be individual values or ranges
□ switch() default case with case(case.DEFAULT):
□ break_loop() and continue_loop() control loop flow
□ Dynamic circuits require hardware support (not all backends)
□ Dynamic circuits enable adaptive algorithms
□ Dynamic circuits allow feedback (measurement → gate decision)
□ Loop depth calculation includes iterations
□ Nested control flow supported (loops in conditionals)

CIRCUIT LIBRARY CONCEPTS:
□ qiskit.circuit.library contains pre-built circuits
□ QFT = Quantum Fourier Transform (basis of many algorithms)
□ QFT(n) creates n-qubit QFT circuit
□ QFT has do_swaps parameter (bit reversal swaps)
□ RealAmplitudes = VQE ansatz with RY rotations + CNOT entanglement
□ RealAmplitudes(n, reps) has reps repetition layers
□ RealAmplitudes uses only real amplitudes (no complex phase)
□ EfficientSU2 = hardware-efficient ansatz (RY + RZ + CNOT)
□ EfficientSU2 covers full SU(2) single-qubit space
□ EfficientSU2 efficient on hardware (basis gate compatible)
□ TwoLocal = customizable ansatz (rotation + entanglement)
□ TwoLocal(n, rotation, entanglement, reps) fully configurable
□ NLocal generalizes to n-qubit gates (N>2)
□ PauliEvolutionGate implements e^(-iHt) time evolution
□ Library circuits are parameterized (must bind before execution)
□ Library circuits compose with regular circuits
□ Library circuits optimize for specific use cases

TRANSPILER CONCEPTS (6 STAGES):
□ Transpiler = compiler from logical circuit to physical circuit
□ Transpiler has 6 sequential stages (pipeline architecture)
□ Stage 1 - Init: Decomposes high-level gates (3+ qubits)
□ Init stage: Unroll3qOrMore pass breaks down complex gates
□ Init stage ensures max 2-qubit gates for routing
□ Stage 2 - Layout: Maps logical qubits → physical qubits
□ Layout selection critical for circuit performance
□ TrivialLayout: q[i] → physical qubit i (simple, no optimization)
□ VF2Layout: Graph isomorphism for perfect subgraph embedding
□ VF2Layout finds optimal layout when it exists (may be slow)
□ SabreLayout: Heuristic search, best for general use
□ SabreLayout works well on large circuits (scales better)
□ DenseLayout: Places connected qubits on connected hardware qubits
□ Layout affects routing cost (good layout = fewer SWAPs)
□ Stage 3 - Routing: Inserts SWAP gates for non-adjacent qubits
□ Routing needed when 2-qubit gate spans non-connected qubits
□ Each SWAP = 3 CNOT gates (expensive operation!)
□ SabreSwap: Heuristic routing (default, generally good)
□ StochasticSwap: Random search with scoring (alternative)
□ Routing minimizes SWAP count (depth vs gate count tradeoff)
□ Coupling map defines allowed 2-qubit interactions
□ Stage 4 - Translation: Converts gates to hardware basis gates
□ Translation uses BasisTranslator pass
□ Basis gates: hardware-native operations (e.g., ['id','rz','sx','x','cx'])
□ Translation ensures all gates are executable on hardware
□ Some gates decompose into multiple basis gates
□ Stage 5 - Optimization: Reduces circuit depth and gate count
□ Optimization level 0: No optimization (TrivialLayout, minimal passes)
□ Optimization level 1: Light optimization (basic passes)
□ Optimization level 2: Medium optimization (default, balanced)
□ Optimization level 3: Heavy optimization (unitary synthesis, slow)
□ Higher optimization = more compilation time
□ Higher optimization ≠ always better results (diminishing returns)
□ Optimization passes: gate cancellation, commutation analysis, resynthesis
□ Stage 6 - Scheduling: Adds timing information (pulse-level)
□ Scheduling converts to time-domain representation
□ ASAP: As Soon As Possible (minimize idle at start)
□ ALAP: As Late As Possible (minimize idle at end)
□ ALAP better for decoherence (gates execute closer to measurement)
□ Scheduled circuits include Delay instructions
□ Delay instructions represent idle time (no gates)
□ Scheduling aligns gates with hardware constraints
□ Backend object provides: coupling map, basis gates, timing info
□ Transpiler without backend uses generic constraints
□ Transpilation deterministic given same seed (reproducible)
□ PassManager orchestrates all stages (configurable pipeline)
```

### 💻 Code Pattern Checklist
```
CIRCUIT CREATION PATTERNS:
□ from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
□ qc = QuantumCircuit(3) creates 3 qubits, 0 classical bits
□ qc = QuantumCircuit(3, 2) creates 3 qubits, 2 classical bits
□ qc = QuantumCircuit(n_qubits, n_clbits) standard creation pattern
□ qr = QuantumRegister(5, 'q') creates quantum register named 'q'
□ cr = ClassicalRegister(5, 'c') creates classical register named 'c'
□ qc = QuantumCircuit(qr, cr) creates circuit from registers
□ qc = QuantumCircuit(qr1, qr2, cr) multiple registers allowed
□ qc = QuantumCircuit() creates empty circuit
□ qc.add_register(qr) adds register to existing circuit
□ qc.add_register(cr) adds classical register
□ qc.qubits returns list of Qubit objects
□ qc.clbits returns list of Clbit objects
□ qc.qregs returns list of QuantumRegister objects
□ qc.cregs returns list of ClassicalRegister objects
□ qc.name = 'my_circuit' sets circuit name
□ qc.name returns circuit name (string)
□ qc.global_phase = np.pi/4 sets global phase
□ qc.metadata = {'key': 'value'} attaches metadata dict

CIRCUIT PROPERTY PATTERNS:
□ depth_value = qc.depth() returns int (METHOD with parentheses)
□ size_value = qc.size() returns int (METHOD with parentheses)
□ width_value = qc.width() returns int (METHOD with parentheses)
□ num_q = qc.num_qubits returns int (PROPERTY - NO parentheses!)
□ num_c = qc.num_clbits returns int (PROPERTY - NO parentheses!)
□ num_p = qc.num_parameters returns int (PROPERTY - NO parentheses!)
□ ops_dict = qc.count_ops() returns dict {'h': 2, 'cx': 3}
□ total_gates = sum(qc.count_ops().values()) sum all gate counts
□ qc.count_ops().get('cx', 0) safe access (0 if no CNOT)
□ qc.decompose() returns decomposed circuit (breaks down complex gates)
□ qc.decompose().depth() depth after decomposition
□ qc.inverse() returns inverse circuit (reverse order, conjugate gates)
□ qc.copy() creates deep copy of circuit
□ qc.copy(name='new_name') copy with new name
□ qc.clear() removes all instructions (empties circuit)
□ qc.remove_final_measurements() removes measurements at end
□ qc.remove_final_measurements(inplace=False) returns new circuit

GATE APPLICATION PATTERNS:
□ qc.h(0) applies Hadamard to qubit 0
□ qc.h([0, 1, 2]) applies Hadamard to multiple qubits (parallel)
□ qc.cx(0, 1) applies CNOT (control=0, target=1)
□ qc.cx([0, 1], [1, 2]) applies multiple CNOTs: 0→1, 1→2
□ qc.measure(0, 0) measures qubit 0 into classical bit 0
□ qc.measure([0, 1], [0, 1]) measures multiple qubits
□ qc.measure_all() adds measurements for all qubits
□ qc.measure_all(inplace=False) returns new circuit with measurements
□ qc.barrier() adds barrier across all qubits
□ qc.barrier([0, 1]) barrier on specific qubits
□ qc.reset(0) resets qubit 0 to |0⟩
□ qc.reset([0, 1]) resets multiple qubits

COMPOSITION PATTERNS:
□ result = qc1.compose(qc2) sequential composition (qc2 after qc1)
□ result = qc1.compose(qc2, inplace=False) returns NEW circuit (default)
□ qc1.compose(qc2, inplace=True) modifies qc1 directly (no return)
□ qc1.compose(qc2, qubits=[2, 3]) maps qc2 to specific qubits in qc1
□ qc1.compose(qc2, qubits=[2, 3], clbits=[0]) maps quantum and classical
□ qc1.compose(qc2, front=True) prepends qc2 BEFORE qc1
□ qc1.compose(qc2, front=True, inplace=True) prepend and modify
□ result = qc1.tensor(qc2) parallel composition (qc1 ⊗ qc2)
□ result = qc1.tensor(qc2, inplace=False) returns NEW circuit (default)
□ qc1.tensor(qc2, inplace=True) modifies qc1 directly
□ qc.tensor(qc2) adds qc2's qubits after qc1's qubits
□ from qiskit.circuit import Gate, Instruction
□ custom_gate = Gate('mygate', num_qubits=2, params=[])
□ qc.append(custom_gate, [0, 1]) adds custom gate
□ qc.append(HGate(), [0]) adds Hadamard via append
□ qc.append(CXGate(), [0, 1]) adds CNOT via append
□ qc.append(instruction, qargs=[0], cargs=[0]) append with classical args

PARAMETERIZED CIRCUIT PATTERNS:
□ from qiskit.circuit import Parameter, ParameterVector
□ theta = Parameter('θ') creates single parameter
□ phi = Parameter('φ') creates another parameter
□ params = ParameterVector('θ', 5) creates θ[0], θ[1], ..., θ[4]
□ qc.rx(theta, 0) rotation gate with parameter
□ qc.ry(2*theta, 0) parameter in expression
□ qc.rz(theta + phi, 0) combines parameters
□ import numpy as np
□ qc.ry(np.pi*theta, 0) parameter with constant
□ param_set = qc.parameters returns ParameterView (set-like)
□ list(qc.parameters) converts to list
□ len(qc.parameters) counts unbound parameters
□ param_dict = {theta: 0.5, phi: 1.2} binding dictionary
□ bound = qc.assign_parameters(param_dict) binds and returns new circuit
□ bound = qc.assign_parameters({theta: 0.5}) partial binding allowed
□ bound = qc.assign_parameters({params: [0.1, 0.2, 0.3, 0.4, 0.5]}) bind vector
□ bound = qc.assign_parameters([0.1, 0.2], inplace=False) positional binding
□ qc.assign_parameters(values, inplace=True) modifies circuit directly
□ len(bound.parameters) == 0 check if fully bound
□ qc.bind_parameters() DEPRECATED - use assign_parameters()
□ from qiskit.circuit import ParameterExpression
□ expr = 2*theta + np.sin(phi) complex parameter expression
□ qc.ry(expr, 0) use expression as gate parameter

CLASSICAL CONTROL PATTERNS (LEGACY):
□ qc.measure(0, 0) measure first (condition needs measured value)
□ qc.x(1).c_if(cr[0], 1) apply X if classical bit 0 is 1
□ qc.h(0).c_if(cr, 3) apply H if classical register equals 3 (binary '11')
□ qc.cx(0, 1).c_if(cr[1], 0) apply CNOT if bit 1 is 0
□ gate_instruction = qc.x(0).c_if(cr, 1) returns instruction
□ c_if syntax: gate.c_if(classical, value) - gate FIRST, condition second

CLASSICAL CONTROL PATTERNS (MODERN):
□ from qiskit.circuit.classical import expr
□ qc.measure(0, 0) measure first
□ with qc.if_test((cr[0], 1)): uses TUPLE (clbit, value)
□     qc.x(1) applies X inside if block
□ with qc.if_test((cr, 3)): register comparison (cr == 3)
□     qc.h(0) operations in if block
□ with qc.if_test((cr[0], 1)) as else_: if-else syntax
□     qc.x(1) if branch
□ with else_: else block
□     qc.h(1) else branch
□ condition = expr.logic_and(cr[0], cr[1]) create AND condition
□ with qc.if_test(condition): use complex condition
□     qc.x(0)
□ condition = expr.equal(cr, 5) equality test
□ condition = expr.not_equal(cr, 0) inequality test
□ condition = expr.less(cr, 10) less than comparison
□ condition = expr.greater(cr, 2) greater than comparison
□ condition = expr.logic_or(cr[0], cr[1]) OR condition
□ condition = expr.logic_not(cr[0]) NOT condition

DYNAMIC CIRCUIT PATTERNS:
□ with qc.for_loop(range(5)): fixed 5 iterations
□     qc.h(0) operation repeated 5 times
□ with qc.for_loop(range(3)) as i: loop with variable
□     qc.rx(i*0.1, 0) use loop variable
□ qc.measure(0, 0)
□ with qc.while_loop((cr[0], 0)): loop while bit 0 is 0
□     qc.h(0)
□     qc.measure(0, 0) re-measure in loop
□ with qc.switch(cr) as case: switch on register value
□     with case(0): case for value 0
□         qc.x(0)
□     with case(1): case for value 1
□         qc.h(0)
□     with case(case.DEFAULT): default case
□         qc.reset(0)
□ qc.break_loop() exit loop early
□ qc.continue_loop() skip to next iteration

CIRCUIT LIBRARY PATTERNS:
□ from qiskit.circuit.library import QFT, RealAmplitudes, EfficientSU2
□ from qiskit.circuit.library import TwoLocal, NLocal, PauliEvolutionGate
□ qft = QFT(num_qubits=4) create 4-qubit QFT
□ qft = QFT(4, do_swaps=True) QFT with bit reversal swaps (default)
□ qft = QFT(4, do_swaps=False) QFT without swaps
□ qft_inverse = qft.inverse() inverse QFT
□ qc.append(qft, range(4)) append QFT to circuit
□ ansatz = RealAmplitudes(num_qubits=3, reps=2) VQE ansatz
□ ansatz = RealAmplitudes(3, reps=2, entanglement='linear') linear entanglement
□ ansatz = RealAmplitudes(3, reps=2, entanglement='full') full entanglement
□ print(ansatz.num_parameters) check parameter count
□ bound_ansatz = ansatz.assign_parameters([0.1, 0.2, ...]) bind parameters
□ ansatz = EfficientSU2(num_qubits=4, reps=3) hardware-efficient ansatz
□ ansatz = EfficientSU2(4, su2_gates=['ry', 'rz']) custom single-qubit gates
□ ansatz = EfficientSU2(4, entanglement='sca') sca entanglement pattern
□ ansatz = TwoLocal(4, rotation_blocks='ry', entanglement_blocks='cx')
□ ansatz = TwoLocal(4, ['ry', 'rz'], 'cz', reps=2) custom rotation/entangle
□ from qiskit.circuit.library import PauliFeatureMap, ZFeatureMap
□ feature_map = PauliFeatureMap(feature_dimension=2, reps=2)
□ from qiskit.circuit.library import HGate, XGate, CXGate
□ h_gate = HGate()
□ qc.append(h_gate, [0])

TRANSPILER PATTERNS:
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
□ from qiskit.transpiler import PassManager, CouplingMap
□ from qiskit_ibm_runtime import QiskitRuntimeService
□ service = QiskitRuntimeService()
□ backend = service.backend('ibm_brisbane')
□ pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
□ pm = generate_preset_pass_manager(optimization_level=2, backend=backend) default
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend) heavy
□ pm = generate_preset_pass_manager(0, backend) level 0 (no optimization)
□ transpiled = pm.run(qc) transpile circuit
□ transpiled_circuits = pm.run([qc1, qc2, qc3]) batch transpilation
□ pm = generate_preset_pass_manager(2, backend, layout_method='sabre')
□ pm = generate_preset_pass_manager(2, backend, layout_method='vf2')
□ pm = generate_preset_pass_manager(2, backend, layout_method='trivial')
□ pm = generate_preset_pass_manager(2, backend, layout_method='dense')
□ pm = generate_preset_pass_manager(2, backend, routing_method='sabre') default
□ pm = generate_preset_pass_manager(2, backend, routing_method='stochastic')
□ pm = generate_preset_pass_manager(2, backend, scheduling_method='asap')
□ pm = generate_preset_pass_manager(2, backend, scheduling_method='alap') better
□ pm = generate_preset_pass_manager(2, backend, seed_transpiler=42) reproducible
□ pm = generate_preset_pass_manager(2, backend, approximation_degree=0.99)
□ coupling_map = CouplingMap([[0,1], [1,2], [2,3]]) custom coupling
□ pm = generate_preset_pass_manager(2, backend, coupling_map=coupling_map)
□ from qiskit import transpile
□ transpiled = transpile(qc, backend) simple transpile (uses defaults)
□ transpiled = transpile(qc, backend, optimization_level=2)
□ transpiled = transpile(qc, backend, basis_gates=['id','rz','sx','cx'])
□ transpiled = transpile(qc, backend, coupling_map=coupling_map)
□ transpiled = transpile(qc, backend, initial_layout=[0,1,3]) manual layout
□ transpiled.depth() check transpiled depth
□ transpiled.count_ops() check gate counts after transpilation
□ print(transpiled.layout) view qubit layout
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 3: CREATE CIRCUITS - ONE-PAGE SUMMARY                     ║
║              (18% of Exam - HIGHEST WEIGHT! ~12 Questions)            ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🏗️ CIRCUIT CREATION FUNDAMENTALS                                      ║
║  ├─ BASIC CREATION                                                     ║
║  │  ├─ QuantumCircuit(n_qubits, n_clbits) - Q before C! (trap!)      ║
║  │  ├─ QuantumCircuit(3, 2) = 3 qubits, 2 classical bits              ║
║  │  ├─ QuantumCircuit(qr, cr) - with named registers                  ║
║  │  ├─ qr = QuantumRegister(5, 'q') named quantum register            ║
║  │  ├─ cr = ClassicalRegister(5, 'c') named classical register        ║
║  │  └─ All qubits initialize to |0⟩ (cannot specify initial state)    ║
║  ├─ REGISTER MANAGEMENT                                                ║
║  │  ├─ qc.add_register(qr) adds register to existing circuit          ║
║  │  ├─ qc.qubits returns list of Qubit objects                        ║
║  │  ├─ qc.clbits returns list of Clbit objects                        ║
║  │  ├─ qc.qregs returns list of QuantumRegister objects               ║
║  │  └─ qc.cregs returns list of ClassicalRegister objects             ║
║  └─ CIRCUIT METADATA                                                   ║
║     ├─ qc.name = 'my_circuit' sets circuit name                       ║
║     ├─ qc.global_phase = np.pi/4 sets global phase                    ║
║     └─ qc.metadata = {'key': 'value'} attaches metadata               ║
║                                                                        ║
║  📏 CIRCUIT PROPERTIES & METRICS                                       ║
║  ├─ METHODS (require parentheses!)                                     ║
║  │  ├─ depth() = longest path through circuit (critical path)         ║
║  │  │   └─ Includes measurements, barriers count as 0                 ║
║  │  │   └─ Parallel gates share ONE layer (same depth)                ║
║  │  ├─ size() = total operation count (gates + measurements)          ║
║  │  │   └─ Counts all instructions including barriers                 ║
║  │  ├─ width() = total wires (num_qubits + num_clbits)                ║
║  │  └─ count_ops() = dict of gate types {'h': 2, 'cx': 3}             ║
║  │      └─ Does NOT include parameter values                          ║
║  ├─ PROPERTIES (NO parentheses!)                                       ║
║  │  ├─ num_qubits = qubit count (TRAP: no parentheses!)               ║
║  │  ├─ num_clbits = classical bit count (TRAP: no parentheses!)       ║
║  │  └─ num_parameters = unbound parameter count (property)            ║
║  └─ CIRCUIT MANIPULATION                                               ║
║     ├─ qc.decompose() breaks down complex gates                       ║
║     ├─ qc.inverse() returns circuit inverse (reverse + conjugate)     ║
║     ├─ qc.copy() creates deep copy                                    ║
║     ├─ qc.clear() removes all instructions                            ║
║     └─ qc.remove_final_measurements() removes end measurements        ║
║                                                                        ║
║  🔗 COMPOSITION & COMBINATION                                          ║
║  ├─ COMPOSE (Sequential - SAME qubits)                                 ║
║  │  ├─ result = qc1.compose(qc2) sequential combination               ║
║  │  ├─ qc1.compose(qc2, inplace=True) modifies qc1 directly           ║
║  │  ├─ qc1.compose(qc2, qubits=[2,3]) maps to specific qubits         ║
║  │  ├─ qc1.compose(qc2, front=True) prepends qc2 before qc1           ║
║  │  ├─ Width unchanged (uses existing qubits)                         ║
║  │  └─ TRAP: compose() returns NEW circuit (default inplace=False)    ║
║  ├─ TENSOR (Parallel - ADDS qubits)                                    ║
║  │  ├─ result = qc1.tensor(qc2) parallel combination (qc1 ⊗ qc2)      ║
║  │  ├─ qc1.tensor(qc2, inplace=True) modifies qc1 directly            ║
║  │  ├─ Width increases (adds qc2.num_qubits + qc2.num_clbits)         ║
║  │  ├─ Creates independent subsystems (no interaction)                ║
║  │  └─ qc2's qubits added after qc1's qubits                          ║
║  └─ APPEND (Single operation)                                          ║
║     ├─ qc.append(gate, [qubits]) adds single gate                     ║
║     ├─ TRAP: qubits must be LIST even for single qubit!               ║
║     ├─ qc.append(HGate(), [0]) correct syntax                         ║
║     ├─ qc.append(CXGate(), [0, 1]) two-qubit gate                     ║
║     └─ append() modifies in place (returns None)                      ║
║                                                                        ║
║  🎛️ PARAMETERIZED CIRCUITS                                             ║
║  ├─ PARAMETER CREATION                                                 ║
║  │  ├─ theta = Parameter('θ') creates symbolic parameter              ║
║  │  ├─ params = ParameterVector('θ', n) creates θ[0]...θ[n-1]         ║
║  │  ├─ TRAP: Parameter('θ') twice = TWO different objects!            ║
║  │  └─ Object identity matters, not name equality                     ║
║  ├─ PARAMETER USAGE                                                    ║
║  │  ├─ qc.rx(theta, 0) gate with parameter                            ║
║  │  ├─ qc.ry(2*theta, 0) parameter expressions allowed                ║
║  │  ├─ qc.rz(theta + phi, 0) combine parameters                       ║
║  │  └─ Complex expressions: sin(theta), cos(phi), theta**2            ║
║  ├─ PARAMETER BINDING                                                  ║
║  │  ├─ bound = qc.assign_parameters({theta: 0.5}) bind single         ║
║  │  ├─ bound = qc.assign_parameters({params: [0.1, 0.2, ...]})        ║
║  │  ├─ bound = qc.assign_parameters(values, inplace=False) default    ║
║  │  ├─ Partial binding allowed (bind subset of parameters)            ║
║  │  ├─ TRAP: bind_parameters() is DEPRECATED!                         ║
║  │  └─ Must bind before execution (hardware needs concrete values)    ║
║  └─ PARAMETER INSPECTION                                               ║
║     ├─ qc.parameters returns ParameterView (set-like)                 ║
║     ├─ len(qc.parameters) counts unbound parameters                   ║
║     ├─ len(qc.parameters) == 0 means fully bound                      ║
║     └─ Used for VQE, QAOA, variational algorithms                     ║
║                                                                        ║
║  🔀 CLASSICAL CONTROL (LEGACY c_if)                                    ║
║  ├─ SYNTAX & USAGE                                                     ║
║  │  ├─ qc.x(1).c_if(cr[0], 1) - gate FIRST, condition second          ║
║  │  ├─ TRAP: qc.c_if(0,1).x(1) WRONG ORDER!                           ║
║  │  ├─ qc.h(0).c_if(cr, 3) register comparison (cr==3)                ║
║  │  └─ Must measure BEFORE c_if (condition needs value)               ║
║  ├─ REGISTER INTERPRETATION                                            ║
║  │  ├─ Register value is INTEGER (binary representation)              ║
║  │  ├─ cr==3 means binary '11' (both bits set)                        ║
║  │  ├─ cr[0] is LSB (least significant bit)                           ║
║  │  └─ Little-endian bit ordering                                     ║
║  └─ STATUS                                                             ║
║     ├─ c_if() is LEGACY (deprecated but exam-relevant!)               ║
║     └─ Replaced by modern if_test() API                               ║
║                                                                        ║
║  🔀 CLASSICAL CONTROL (MODERN if_test)                                 ║
║  ├─ BASIC IF                                                           ║
║  │  ├─ from qiskit.circuit.classical import expr                      ║
║  │  ├─ with qc.if_test((cr[0], 1)): - TUPLE required!                 ║
║  │  │      qc.x(1) - operations in if block                           ║
║  │  ├─ TRAP: if_test(cr[0], 1) without tuple → ERROR!                 ║
║  │  └─ with qc.if_test((cr, 3)): register comparison                  ║
║  ├─ IF-ELSE                                                            ║
║  │  ├─ with qc.if_test((cr[0], 1)) as else_:                          ║
║  │  │      qc.x(1) - if branch                                        ║
║  │  ├─ with else_: - else block                                       ║
║  │  │      qc.h(1) - else branch                                      ║
║  │  └─ TRAP: Need 'as else_:' syntax for else block!                  ║
║  └─ COMPLEX CONDITIONS                                                 ║
║     ├─ condition = expr.logic_and(cr[0], cr[1]) AND                   ║
║     ├─ condition = expr.logic_or(cr[0], cr[1]) OR                     ║
║     ├─ condition = expr.logic_not(cr[0]) NOT                          ║
║     ├─ condition = expr.equal(cr, 5) equality                         ║
║     ├─ condition = expr.less(cr, 10) less than                        ║
║     └─ with qc.if_test(condition): use complex condition              ║
║                                                                        ║
║  🔁 DYNAMIC CIRCUITS (Control Flow)                                    ║
║  ├─ FOR LOOPS                                                          ║
║  │  ├─ with qc.for_loop(range(5)): fixed iterations                   ║
║  │  │      qc.h(0) - repeated 5 times                                 ║
║  │  ├─ with qc.for_loop(range(3)) as i: loop variable                 ║
║  │  │      qc.rx(i*0.1, 0) - use loop index                           ║
║  │  └─ TRAP: for_loop(5) wrong! Need range(5)                         ║
║  ├─ WHILE LOOPS                                                        ║
║  │  ├─ with qc.while_loop((cr[0], 0)): - TUPLE required               ║
║  │  │      qc.h(0)                                                    ║
║  │  │      qc.measure(0, 0) - re-measure in loop!                     ║
║  │  └─ TRAP: Must re-measure to update condition                      ║
║  ├─ SWITCH STATEMENTS                                                  ║
║  │  ├─ with qc.switch(cr) as case: multi-way branch                   ║
║  │  │      with case(0): qc.x(0) - case 0                             ║
║  │  │      with case(1): qc.h(0) - case 1                             ║
║  │  │      with case(case.DEFAULT): qc.reset(0) - default             ║
║  │  ├─ qc.break_loop() exit loop early                                ║
║  │  └─ qc.continue_loop() skip to next iteration                      ║
║  └─ CONSTRAINTS                                                        ║
║     ├─ Dynamic circuits require hardware support                      ║
║     ├─ Not all backends support dynamic circuits                      ║
║     └─ Enable adaptive algorithms and feedback                        ║
║                                                                        ║
║  📚 CIRCUIT LIBRARY (Pre-built Circuits)                               ║
║  ├─ QUANTUM FOURIER TRANSFORM                                          ║
║  │  ├─ from qiskit.circuit.library import QFT                         ║
║  │  ├─ qft = QFT(num_qubits=4) create 4-qubit QFT                     ║
║  │  ├─ qft = QFT(4, do_swaps=True) with bit reversal (default)        ║
║  │  ├─ qft_inverse = qft.inverse() inverse QFT (QFT†)                 ║
║  │  └─ qc.append(qft, range(4)) append to circuit                     ║
║  ├─ VQE ANSÄTZE                                                        ║
║  │  ├─ RealAmplitudes(n, reps=k) - real amplitudes only               ║
║  │  │   └─ Uses RY rotations + CNOT entanglement                      ║
║  │  ├─ EfficientSU2(n, reps=k) - hardware-efficient                   ║
║  │  │   └─ Uses RY + RZ rotations (covers full SU(2))                 ║
║  │  ├─ TwoLocal(n, rotation, entanglement, reps) - customizable       ║
║  │  │   └─ Specify rotation and entanglement blocks                   ║
║  │  └─ NLocal - generalizes to N-qubit gates                          ║
║  ├─ FEATURE MAPS                                                       ║
║  │  ├─ PauliFeatureMap(feature_dimension, reps) - Pauli encoding      ║
║  │  └─ ZFeatureMap(feature_dimension, reps) - Z-rotation encoding     ║
║  └─ LIBRARY CIRCUIT PROPERTIES                                         ║
║     ├─ TRAP: Library circuits are LOGICAL (need transpilation!)       ║
║     ├─ Most are parameterized (must bind before execution)            ║
║     ├─ ansatz.num_parameters shows parameter count                    ║
║     ├─ Compose with regular circuits normally                         ║
║     └─ Optimized for specific use cases (VQE, QAOA, etc.)             ║
║                                                                        ║
║  🔧 TRANSPILER PIPELINE (6 Stages: ILRTOS)                             ║
║  ├─ STAGE 1: INIT (Decomposition)                                      ║
║  │  ├─ Decomposes 3+ qubit gates into 2-qubit gates                   ║
║  │  ├─ Unroll3qOrMore pass breaks down complex gates                  ║
║  │  └─ Ensures max 2-qubit gates for routing stage                    ║
║  ├─ STAGE 2: LAYOUT (Logical→Physical Mapping)                         ║
║  │  ├─ Maps logical qubits to physical hardware qubits                ║
║  │  ├─ TrivialLayout: q[i]→i (simple, no optimization)                ║
║  │  ├─ VF2Layout: Perfect graph matching (best but slow/may fail)     ║
║  │  ├─ SabreLayout: Heuristic (default, good balance)                 ║
║  │  ├─ DenseLayout: Pack connected qubits together                    ║
║  │  └─ Good layout → fewer SWAPs → better performance                 ║
║  ├─ STAGE 3: ROUTING (SWAP Insertion)                                  ║
║  │  ├─ Inserts SWAP gates for non-adjacent 2-qubit gates              ║
║  │  ├─ TRAP: Each SWAP = 3 CNOT gates! (expensive!)                   ║
║  │  ├─ SabreSwap: Heuristic routing (default, generally good)         ║
║  │  ├─ StochasticSwap: Random search with scoring (alternative)       ║
║  │  ├─ Routing is NP-hard (heuristics may not be optimal)             ║
║  │  └─ Coupling map defines allowed 2-qubit interactions              ║
║  ├─ STAGE 4: TRANSLATION (Basis Gate Conversion)                       ║
║  │  ├─ Converts all gates to hardware basis gates                     ║
║  │  ├─ BasisTranslator pass handles conversion                        ║
║  │  ├─ Example basis: ['id','rz','sx','x','cx']                       ║
║  │  ├─ Some gates decompose into multiple basis gates                 ║
║  │  └─ Must specify valid basis gates for target hardware             ║
║  ├─ STAGE 5: OPTIMIZATION (Gate Reduction)                             ║
║  │  ├─ Level 0: No optimization (TrivialLayout, minimal passes)       ║
║  │  ├─ Level 1: Light optimization (basic passes)                     ║
║  │  ├─ Level 2: Medium optimization (default, balanced)               ║
║  │  ├─ Level 3: Heavy optimization (unitary synthesis, slow)          ║
║  │  ├─ Higher level = more compilation time                           ║
║  │  ├─ TRAP: Level 3 ≠ always better! (diminishing returns)           ║
║  │  └─ Passes: gate cancellation, commutation, resynthesis            ║
║  ├─ STAGE 6: SCHEDULING (Timing Information)                           ║
║  │  ├─ Adds pulse-level timing to circuit                             ║
║  │  ├─ ASAP: As Soon As Possible (minimize idle at start)             ║
║  │  ├─ ALAP: As Late As Possible (minimize idle before measure)       ║
║  │  ├─ TRAP: ALAP better for decoherence! (gates closer to measure)   ║
║  │  ├─ Scheduled circuits include Delay instructions                  ║
║  │  └─ Delay = idle time (no gates executing)                         ║
║  └─ TRANSPILER USAGE                                                   ║
║     ├─ from qiskit.transpiler.preset_passmanagers import generate_... ║
║     ├─ pm = generate_preset_pass_manager(level, backend)              ║
║     ├─ transpiled = pm.run(qc) execute transpilation                  ║
║     ├─ TRAP: Backend REQUIRED for realistic results!                  ║
║     ├─ Backend provides: coupling map, basis gates, timing            ║
║     ├─ seed_transpiler=42 for reproducibility                         ║
║     └─ Transpiled circuit usually has GREATER depth (SWAPs!)          ║
║                                                                        ║
║  ⚠️⚠️⚠️ TOP 15 EXAM TRAPS - MEMORIZE THESE! ⚠️⚠️⚠️                        ║
║  1.  QuantumCircuit(2,3) = 2 QUBITS, 3 CLASSICAL! (Q before C)        ║
║  2.  num_qubits is PROPERTY (no ()), depth() is METHOD (with ())      ║
║  3.  compose() = SAME qubits, tensor() = ADDS qubits                  ║
║  4.  compose() returns NEW circuit (default inplace=False)            ║
║  5.  qc.append(HGate(), [0]) needs LIST even for single qubit!        ║
║  6.  Parameter('θ') twice creates TWO different parameter objects!    ║
║  7.  qc.x(1).c_if(0,1) NOT qc.c_if(0,1).x(1) - gate FIRST!           ║
║  8.  if_test needs TUPLE: (clbit, value) not clbit, value             ║
║  9.  c_if register value is INTEGER: cr==3 means binary '11'          ║
║  10. Must measure BEFORE conditionals (c_if/if_test need value!)      ║
║  11. SWAP = 3 CNOT gates! (routing is VERY expensive)                 ║
║  12. bind_parameters() DEPRECATED → use assign_parameters()           ║
║  13. Transpiler needs backend for realistic results (coupling + basis)║
║  14. ALAP scheduling better than ASAP (minimize decoherence)          ║
║  15. Parallel gates = ONE depth layer (H on q[0,1,2] = depth 1!)      ║
║                                                                        ║
║  🎯 QUICK DECISION GUIDE                                               ║
║  Combining circuits sequentially? → compose() (same qubits)           ║
║  Combining circuits in parallel? → tensor() (adds qubits)             ║
║  Need symbolic gate angles? → Parameter() and assign_parameters()     ║
║  Legacy conditionals? → gate.c_if(clbit, value)                       ║
║  Modern conditionals? → with qc.if_test((clbit, value)):              ║
║  Need pre-built circuits? → Circuit library (QFT, ansätze)            ║
║  Compiling for hardware? → Transpiler with backend                    ║
║  Checking properties? → Remember: num_qubits (no ()), depth() (with ())║
║                                                                        ║
║  💡 CRITICAL CONCEPT SUMMARY                                           ║
║  ├─ Properties vs Methods: Know which use () and which don't!         ║
║  ├─ compose vs tensor: Same qubits vs adding qubits                   ║
║  ├─ Parameter identity: Object matters, not name string               ║
║  ├─ c_if vs if_test: Legacy vs modern (know both!)                    ║
║  ├─ Transpiler: 6-stage pipeline (ILRTOS mnemonic)                    ║
║  ├─ SWAP cost: 3 CNOTs per SWAP (expensive!)                          ║
║  └─ Circuit library: Logical circuits (transpile before running)      ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---


## ✅ Run Circuits Key Takeaways

### 📚 Concept Checklist
```
□ QiskitRuntimeService is the gateway to IBM Quantum backends
□ Credentials: save_account() stores token persistently (only once)
□ Channels: 'ibm_quantum' for public, 'ibm_cloud' for enterprise
□ Backend selection: service.backend('name') or service.least_busy()
□ Backend methods: service.backends() lists all available backends
□ Transpilation: See Section 3 for full 6-stage pipeline details (ILRTOS)
□ transpile(qc, backend, optimization_level=3) compiles for hardware
□ Transpilation is non-deterministic (use seed_transpiler=42 for reproducibility)
□ generate_preset_pass_manager() creates staged pass managers
□ resilience_level: 0=none, 1=M3 mitigation, 2=M3+ZNE
□ M3 = Matrix-free Measurement mitigation (readout error correction)
□ ZNE = Zero-Noise Extrapolation (estimates ideal result)
□ Session mode: reserved access for iterative algorithms (VQE, QAOA)
□ Sessions prevent re-queuing between iterations (max_time parameter)
□ Batch mode: parallel execution for independent circuits
□ Job mode: single submission (default, simplest)
□ mode= parameter (v0.24.0+): takes backend, Session, or Batch object
□ JobStatus flow: INITIALIZING → QUEUED → VALIDATING → RUNNING → DONE
□ Final states: DONE (success), ERROR (failed), CANCELLED (stopped)
□ Job retrieval: service.job(job_id) retrieves by unique ID
□ PrimitiveResult: Top-level container holding PubResult objects
□ PubResult: One result per PUB (Primitive Unified Bloc)
□ DataBin: Contains actual data (evs, stds, meas, etc.)
□ Backend V2 API: target object consolidates all hardware info
□ V1 API deprecated: configuration(), properties(), defaults()
□ V2 replaces scattered methods with unified target interface
□ T1 = relaxation time (energy decay, like battery life)
□ T2 = dephasing time (coherence loss, like clock drift)
□ Physical constraint: T2 ≤ 2×T1 (always true - fundamental physics!)
□ Circuit duration rule: Should be <10% of T2 for reliable results
□ Qubit frequency: Unique resonant frequency per qubit (~5 GHz)
□ Coupling map = connectivity graph for 2-qubit gates
□ Coupling maps are directional: [0,1] doesn't imply [1,0]
□ Distance metric: Minimum hops between qubits in coupling graph
□ SWAP gate = 3 CNOTs (expensive routing overhead)
□ Routing overhead: Each SWAP ≈ 3% error accumulation
□ BitArray: get_counts() returns string keys, get_int_counts() returns int keys
□ Little-endian bit ordering: q[0] is rightmost bit in string
□ Multiple registers: Each ClassicalRegister becomes separate DataBin attribute
□ Broadcasting: parameter/observable shapes must be compatible
□ NumPy-style broadcasting: Same shape or one dimension is 1
□ Outer product broadcasting: (M,1) × (1,N) → (M,N) result
□ Zip broadcasting: (N,) × (N,) → (N,) paired results
□ Primitives auto-transpile: Manual transpilation optional for control
□ apply_layout(): Must remap observables after manual transpilation
```

### 💻 Code Pattern Checklist
```
□ from qiskit_ibm_runtime import QiskitRuntimeService imports service
□ service = QiskitRuntimeService() connects to IBM Quantum
□ QiskitRuntimeService.save_account(channel='ibm_quantum', token='...') saves credentials
□ QiskitRuntimeService.save_account(channel='ibm_quantum', token='...', overwrite=True) updates credentials
□ backend = service.backend('ibm_brisbane') selects specific backend
□ backend = service.least_busy(simulator=False, min_num_qubits=5) selects best available
□ backends = service.backends() lists all available backends
□ for backend in backends: print(f"{backend.name}: {backend.num_qubits} qubits") iterates backends
□ from qiskit import transpile imports transpilation function
□ transpiled = transpile(qc, backend, optimization_level=3) compiles circuit
□ transpile(..., seed_transpiler=42) ensures reproducibility
□ transpile(..., basis_gates=['cx', 'rz', 'sx']) overrides basis gates
□ transpile(..., coupling_map=custom_map) overrides connectivity
□ transpile(..., initial_layout=[0,1,2]) manually maps virtual→physical qubits
□ print(f"Original: {qc.depth()}, Transpiled: {transpiled.depth()}") compares depths
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager imports PassManager
□ pm = generate_preset_pass_manager(optimization_level=2, backend=backend) creates PassManager
□ transpiled = pm.run(circuit) runs PassManager on circuit
□ from qiskit_ibm_runtime import Session imports Session context
□ with Session(backend=backend) as session: creates session context
□ with Session(backend=backend, max_time="1h") as session: sets max session time
□ from qiskit_ibm_runtime import Batch imports Batch context
□ with Batch(backend=backend) as batch: creates batch context
□ from qiskit_ibm_runtime import SamplerV2 as Sampler imports Sampler primitive
□ from qiskit_ibm_runtime import EstimatorV2 as Estimator imports Estimator primitive
□ sampler = Sampler(mode=backend) creates Sampler in Job mode
□ sampler = Sampler(mode=session) attaches primitive to session
□ estimator = Estimator(mode=batch) attaches primitive to batch
□ from qiskit_ibm_runtime import Options imports Options class
□ options = Options() creates configuration object
□ options.optimization_level = 3 sets optimization (NOT options.transpilation.optimization_level)

```
### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║     SECTION 4: RUN CIRCUITS ON BACKEND - ONE-PAGE SUMMARY             ║
║                      (15% of Exam - ~10 Questions)                     ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🔌 RUNTIME SERVICE (Authentication & Backend Access)                  ║
║  ├─ QiskitRuntimeService.save_account(token='...', overwrite=True)    ║
║  │   → Must save credentials ONCE before using service                ║
║  ├─ service = QiskitRuntimeService()  → Connect to IBM Quantum        ║
║  ├─ backend = service.backend('ibm_brisbane')  → Specific backend     ║
║  ├─ backend = service.least_busy(simulator=False, min_num_qubits=5)   ║
║  │   → Auto-select best available backend                             ║
║  └─ backends = service.backends()  → List all available backends      ║
║                                                                        ║
║  ⚙️ TRANSPILATION (See Section 3 for full 6-stage pipeline)           ║
║  ├─ transpile(qc, backend, optimization_level=3, seed_transpiler=42)  ║
║  ├─ Levels: 0=debug, 1=fast, 2=default, 3=best                        ║
║  ├─ PassManager: generate_preset_pass_manager(level, backend)         ║
║  └─ ⚠️ NOT deterministic without seed_transpiler!                      ║
║                                                                        ║
║  📋 OPTIONS (Execution Configuration)                                  ║
║  ├─ options = Options()  → Create configuration object                ║
║  ├─ options.optimization_level = 3  (0-3)                             ║
║  │   ⚠️ NOT options.transpilation.optimization_level!                 ║
║  ├─ options.resilience_level = 1  (0-2)                               ║
║  │   • Level 0: No error mitigation (fastest, raw results)            ║
║  │   • Level 1: M3 measurement mitigation (~20% overhead)             ║
║  │   • Level 2: M3 + ZNE zero-noise extrapolation (3-5× overhead)     ║
║  ├─ options.execution.shots = 4096  → Measurement repetitions         ║
║  │   • 1024: Minimum for reasonable statistics                        ║
║  │   • 4096: Standard production value                                ║
║  │   • 8192+: High precision experiments                              ║
║  ├─ options.dynamical_decoupling.enable = True                        ║
║  │   → Inserts DD sequences during idle times                         ║
║  └─ sampler = Sampler(backend=backend, options=options)               ║
║                                                                        ║
║  🔄 EXECUTION MODES (Job/Batch/Session)                                ║
║  ├─ Job Mode: Sampler(mode=backend)                                   ║
║  │   • Single circuit submission                                      ║
║  │   • Direct execution, simplest approach                            ║
║  │   • Best for: Testing, debugging, one-off measurements             ║
║  ├─ Batch Mode: with Batch(backend=backend) as batch:                 ║
║  │   • Multiple independent circuits executed in parallel             ║
║  │   • Backend optimizes execution order for efficiency               ║
║  │   • Best for: Parameter sweeps, benchmarking, comparisons          ║
║  ├─ Session Mode: with Session(backend=backend, max_time="1h"):       ║
║  │   • Reserved QPU access for sequential jobs                        ║
║  │   • No re-queuing between iterations                               ║
║  │   • Best for: VQE, QAOA, iterative algorithms with feedback        ║
║  └─ mode= parameter (v0.24.0+): Estimator(mode=session)               ║
║      ⚠️ OLD: session=session is DEPRECATED!                           ║
║                                                                        ║
║  📊 JOB STATUS & LIFECYCLE                                             ║
║  ├─ JobStatus Flow: INITIALIZING → QUEUED → VALIDATING → RUNNING     ║
║  │   Final states: DONE (success) | ERROR (failed) | CANCELLED        ║
║  ├─ job.status()  → Returns current JobStatus enum                    ║
║  ├─ job.done()  → Returns True when job complete                      ║
║  ├─ job.result()  → Blocks until complete, returns PrimitiveResult    ║
║  ├─ job.result(timeout=300)  → 5-minute timeout to prevent hanging    ║
║  ├─ job_id = job.job_id()  → Get unique identifier                    ║
║  └─ service.job(job_id)  → Retrieve job by ID (even days later!)      ║
║                                                                        ║
║  📦 RESULT STRUCTURE (PrimitiveResult → PubResult → DataBin)          ║
║  ├─ result = job.result()  → PrimitiveResult (top container)          ║
║  ├─ pub_result = result[0]  → First PubResult (one per PUB)           ║
║  ├─ data = pub_result.data  → DataBin (actual measurement data)       ║
║  ├─ SAMPLER Results:                                                   ║
║  │   • data.meas  → BitArray (default register from measure_all())    ║
║  │   • data.<name>  → BitArray (named ClassicalRegister)              ║
║  │   • bit_array.get_counts()  → {'00': 512, '11': 512} (strings)     ║
║  │   • bit_array.get_int_counts()  → {0: 512, 3: 512} (integers)      ║
║  │   • bit_array.get_bitstrings()  → ['00', '11', ...] (all shots)    ║
║  │   • bit_array.slice_bits([0,1])  → Extract specific qubits         ║
║  │   • bit_array.slice_shots(range(100))  → First 100 shots           ║
║  ├─ ESTIMATOR Results:                                                 ║
║  │   • data.evs  → np.array of expectation values ⟨O⟩                  ║
║  │   • data.stds  → np.array of standard deviations                   ║
║  └─ ⚠️ Little-endian: '01' means q[0]=1 (rightmost), q[1]=0 (left)    ║
║                                                                        ║
║  🎯 BACKEND TARGET (V2 API - Unified Hardware Interface)               ║
║  ├─ target = backend.target  → Unified hardware info (V2 API)         ║
║  │   ⚠️ V1 DEPRECATED: backend.configuration(), .properties()         ║
║  ├─ target.operation_names  → ['cx', 'rz', 'sx', ...] basis gates     ║
║  ├─ target.instruction_supported('cx', (0, 1))  → True/False          ║
║  ├─ Gate Properties:                                                   ║
║  │   • target['cx'][(0, 1)].error  → Error rate (e.g., 0.012 = 1.2%) ║
║  │   • target['cx'][(0, 1)].duration  → Gate time (in dt units)       ║
║  ├─ Qubit Properties:                                                  ║
║  │   • target.qubit_properties[i].t1  → Relaxation time (~100μs)      ║
║  │   • target.qubit_properties[i].t2  → Dephasing time (≤2×T1!)       ║
║  │   • target.qubit_properties[i].frequency  → Resonance (~5 GHz)     ║
║  └─ coupling_map = target.build_coupling_map()  → Connectivity graph  ║
║                                                                        ║
║  ⏱️ QUBIT PROPERTIES & COHERENCE                                       ║
║  ├─ T1 (Relaxation): Energy decay time, like "battery life"           ║
║  │   → How long |1⟩ state persists before decaying to |0⟩             ║
║  ├─ T2 (Dephasing): Phase coherence time, like "clock accuracy"       ║
║  │   → How long superposition maintains phase relationship            ║
║  ├─ ⚠️ CRITICAL CONSTRAINT: T2 ≤ 2×T1 (ALWAYS - physics law!)          ║
║  │   → If exam shows T2 > 2×T1, it's a TRAP question!                 ║
║  ├─ 10% Rule: Circuit execution time should be < 10% of T2            ║
║  │   → Example: T2=100μs → circuit should finish in <10μs             ║
║  └─ Frequency: Each qubit's resonant frequency for selective control  ║
║                                                                        ║
║  🗺️ COUPLING MAPS (Qubit Connectivity)                                 ║
║  ├─ Coupling map = directed graph of allowed 2-qubit gates            ║
║  ├─ coupling_map.get_edges()  → [[0,1], [1,0], [1,2], ...] edges     ║
║  ├─ coupling_map.distance(i, j)  → Minimum hops between qubits        ║
║  ├─ ⚠️ Direction matters! [0,1] doesn't imply [1,0] exists            ║
║  │   → CX(0,1) supported ≠ CX(1,0) supported                          ║
║  ├─ SWAP decomposition: SWAP = 3 CNOTs                                ║
║  │   → SWAP(0,2) = CX(0,2) + CX(2,0) + CX(0,2)                        ║
║  │   → Each SWAP ≈ 3% error accumulation!                             ║
║  └─ Routing overhead: Can double/triple circuit depth on linear chips ║
║                                                                        ║
║  📡 BROADCASTING (Parameter/Observable Arrays)                         ║
║  ├─ NumPy-style shape compatibility rules apply                       ║
║  ├─ Pattern 1: Single observable, multiple params                     ║
║  │   • Observable: shape () or (1,), Params: shape (N,)               ║
║  │   • Result: (N,) expectation values                                ║
║  ├─ Pattern 2: Zip (one-to-one pairing)                               ║
║  │   • Observables: (N,), Params: (N,) - same length                  ║
║  │   • Result: (N,) paired evaluations                                ║
║  ├─ Pattern 3: Outer product (all combinations)                       ║
║  │   • Observables: (M,1), Params: (1,N)                              ║
║  │   • Result: (M,N) matrix of all M×N combinations                   ║
║  └─ ⚠️ Incompatible: (5,) and (3,) - reshape to (1,5) and (3,1)       ║
║                                                                        ║
║  🔧 ADVANCED TOPICS                                                    ║
║  ├─ observable.apply_layout(transpiled.layout)                        ║
║  │   → CRITICAL: Remap observable after manual transpilation          ║
║  │   → Circuit auto-maps, but observables need manual remapping!      ║
║  ├─ Primitives auto-transpile internally                              ║
║  │   → Manual transpilation optional (gives control but not required) ║
║  └─ Multiple ClassicalRegisters: Each becomes data.<register_name>    ║
║      → ClassicalRegister(2, 'alpha') → data.alpha.get_counts()        ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (MEMORIZE!)                                      ║
║  1.  transpile() NOT deterministic → use seed_transpiler=42           ║
║  2.  mode=session (NOT session=session) for Runtime v0.24.0+          ║
║  3.  options.optimization_level (NOT options.transpilation.opt...)    ║
║  4.  T2 ≤ 2×T1 (ALWAYS - if T2 > 2×T1 in exam, it's a trap!)          ║
║  5.  SWAP = 3 CNOTs (routing is EXPENSIVE, ~3% error per SWAP)        ║
║  6.  save_account() BEFORE QiskitRuntimeService() - "SAVE before SERVE"║
║  7.  V2 API: target.operation_names (NOT configuration().basis_gates) ║
║  8.  apply_layout() for observables after transpilation               ║
║  9.  Coupling map is DIRECTIONAL: [0,1] ≠ [1,0]                       ║
║  10. Check job.done() BEFORE job.result() to avoid blocking           ║
║  11. Little-endian: q[0] is RIGHTMOST bit ('01' = q[0]=1, q[1]=0)     ║
║  12. data.meas or data.<name>, NOT data.counts                        ║
║  13. Higher opt level NOT always better (level 3 slower but usually best)║
║  14. Session for iterative (VQE), Batch for parallel (param sweeps)   ║
║  15. Primitives auto-transpile (manual transpilation gives control)    ║
║                                                                        ║
║  🧠 ESSENTIAL MNEMONICS                                                ║
║  • "ILRTOS" = Init, Layout, Routing, Translation, Opt, Scheduling     ║
║  • "0=Zero, 1=One, 2=Two-way, 3=Three+" = Optimization levels         ║
║  • "ORS" = Options: Optimization, Resilience, Shots                   ║
║  • "JBS" = Job (single), Batch (parallel), Session (sequential)       ║
║  • "T2 ≤ Two Times T1" = Fundamental physics constraint               ║
║  • "SWAP = 3 CX" = Routing cost                                       ║
║  • "SAVE before SERVE" = save_account() then QiskitRuntimeService()   ║
║  • "TARGET" = Timing, Availability, Reliability, Geometry, Environment║
║  • "mode is Modern" = Use mode=, not session= parameter               ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## ✅ Sampler Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS:
□ Primitives replace execute()/backend.run() in Qiskit 1.0+
□ Sampler returns counts/bitstrings, Estimator returns expectation values
□ Sampler REQUIRES measurements in circuit ("S needs M")
□ PUB format: [(circuit, params, shots)] - Primitive Unified Bloc
□ Result extraction chain: result[0].data.meas.get_counts()
□ get_counts() returns string keys, get_bitstrings() returns list of strings
□ Twirling defaults differ: Sampler (gates=False, measure=False), Estimator (gates=True, measure=True)
□ Dynamical Decoupling helps only with idle qubits during execution
□ Qiskit uses LSB bit ordering: rightmost = qubit 0 (little-endian)
□ StatevectorSampler for ideal simulation, SamplerV2 for hardware/noisy simulation
□ Multiple circuits in single run: [(qc1,), (qc2,), (qc3,)]
□ Each PUB in result accessed by index: result[i].data.meas

CONSTRAINTS & LIMITATIONS:
□ Sampler will ERROR if no measurements in circuit (not just return empty)
□ Maximum 300 circuits per job submission in runtime (exceeding causes error)
□ shots parameter must be positive integer (0 or negative causes ValueError)
□ Parameter binding must match circuit's num_parameters exactly
□ Classical register names must be unique within circuit (duplicate names error)
□ PUB tuple must have circuit first; other positions are positional
□ Cannot modify circuit after measurement gate has been added
□ BitArray slicing uses measurement register order, not qubit order
□ Sampler ignores observables if provided (they're for Estimator only)
□ Default shots=1024 if not specified (differs from old backend.run default 4096)
□ Session expires after 5 minutes idle (jobs fail if session closed)
□ Each PUB runs independently - no shared quantum state between PUBs

KEY DEFINITIONS:
□ PUB (Primitive Unified Bloc): Tuple format (circuit, parameters, shots) for unified API
□ DataBin: Container object holding measurement results per classical register
□ BitArray: 2D array structure [shots × num_bits] storing measurement outcomes
□ PrimitiveResult: Top-level result container holding list of PubResult objects
□ PubResult: Individual result for one PUB containing metadata and DataBin
□ Twirling: Randomized compilation technique converting coherent noise to stochastic
□ Dynamical Decoupling: Pulse sequences on idle qubits to reduce decoherence
□ LSB ordering: Least Significant Bit first (rightmost bit = qubit 0)
□ Shots: Number of circuit repetitions (samples) to estimate probability distribution
□ Classical register: Named bit collection for storing measurement outcomes
□ Measurement basis: Computational basis {|0⟩, |1⟩} unless rotated before measure

ARCHITECTURE & WORKFLOW:
□ Sampler uses V2 interface: run() returns Job, result() returns PrimitiveResult
□ StatevectorSampler simulates ideal quantum computer (no noise)
□ SamplerV2 connects to IBM Quantum hardware or noisy simulators
□ Runtime primitives batch-optimize multiple circuits for efficiency
□ Primitive options persist across multiple run() calls on same instance
□ Job queuing: jobs wait in QUEUED state until resources available
□ Results persist in cloud for 7 days after completion (then deleted)
□ Primitive sessions allow priority access and reduced queue times

VERSION-SPECIFIC:
□ V1 primitives deprecated: use V2 (SamplerV2, not Sampler)
□ Old execute() removed in Qiskit 1.0 - use primitives exclusively
□ backend.run() still exists but discouraged for new code
□ qiskit-ibm-runtime separate package required for hardware access
□ StatevectorSampler in qiskit.primitives (local), SamplerV2 in qiskit_ibm_runtime
```

### 💻 Code Pattern Checklist
```
ESSENTIAL IMPORTS:
□ from qiskit.primitives import StatevectorSampler  # ideal/local simulation
□ from qiskit_ibm_runtime import SamplerV2  # hardware/runtime
□ from qiskit_ibm_runtime import QiskitRuntimeService  # backend access
□ from qiskit import QuantumCircuit  # circuit creation
□ from qiskit.circuit import Parameter  # parameterized circuits
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager  # optimization

SAMPLER INITIALIZATION:
□ sampler = StatevectorSampler()  # no arguments, local ideal sim
□ service = QiskitRuntimeService(); backend = service.backend("ibm_brisbane")
□ sampler = SamplerV2(mode=backend)  # runtime with specific backend
□ sampler = SamplerV2(mode=backend, options=options_dict)  # with options
□ sampler = StatevectorSampler(default_shots=2048)  # custom default shots
□ sampler = StatevectorSampler(seed=42)  # reproducible random sampling

CIRCUIT PREPARATION (CRITICAL):
□ qc.measure_all()  # add measurements to all qubits (REQUIRED!)
□ qc.measure(qubit, clbit)  # selective measurement
□ qc.measure(qreg, creg)  # measure entire registers
□ from qiskit.circuit import ClassicalRegister; cr = ClassicalRegister(3, 'output')
□ qc.add_register(cr); qc.measure([0,1,2], cr)  # custom register
□ qc.barrier()  # optional: separate quantum ops from measurements visually

BASIC RUN PATTERNS:
□ job = sampler.run([(qc,)], shots=1024)  # single circuit (trailing comma!)
□ job = sampler.run([(qc,)])  # uses default shots (1024)
□ result = job.result()  # blocking call, waits for completion
□ counts = result[0].data.meas.get_counts()  # extract counts dict
□ bitstrings = result[0].data.meas.get_bitstrings()  # extract list

PARAMETERIZED CIRCUITS:
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.rx(theta, 0); qc.ry(phi, 1)  # add parameterized gates
□ job = sampler.run([(qc, [0.5, 1.2])])  # bind [θ=0.5, φ=1.2]
□ job = sampler.run([(qc, [0.5, 1.2], 2048)])  # with custom shots
□ job = sampler.run([(qc, None, 2048)])  # no params, custom shots (None placeholder)
□ param_values = [[0, 0], [0, π/2], [π/2, 0], [π/2, π/2]]
□ jobs = [sampler.run([(qc, vals)]) for vals in param_values]  # sweep parameters

MULTIPLE CIRCUITS:
□ job = sampler.run([(qc1,), (qc2,), (qc3,)])  # batch submission
□ result[0].data.meas.get_counts()  # qc1 results
□ result[1].data.meas.get_counts()  # qc2 results
□ result[2].data.meas.get_counts()  # qc3 results
□ for i, pub_result in enumerate(result):  # iterate all
□     counts = pub_result.data.meas.get_counts()
□ all_counts = [r.data.meas.get_counts() for r in result]  # list comprehension

RESULT EXTRACTION: See Section 7 for full chain and custom register patterns
□ counts = result[0].data.meas.get_counts()  # standard extraction
□ bitstrings = result[0].data.meas.get_bitstrings()  # all shot outcomes

OPTIONS CONFIGURATION:
□ options = sampler.options  # get current options
□ options.default_shots = 4096  # change default shots
□ sampler.options.default_shots = 2048  # direct assignment
□ options.twirling.enable_gates = True  # enable gate twirling
□ options.twirling.enable_measure = True  # enable measurement twirling
□ options.twirling.num_randomizations = 32  # set twirling rounds
□ options.dynamical_decoupling.enable = True  # enable DD
□ options.dynamical_decoupling.sequence_type = 'XY4'  # DD sequence
□ options.dynamical_decoupling.extra_slack_distribution = 'middle'
□ options.optimization_level = 3  # transpiler optimization (0-3)
□ options.resilience_level = 1  # error mitigation level (0-2)

JOB MANAGEMENT: See Section 7 for full job status and management patterns

ERROR HANDLING (Sampler-specific):
□ assert qc.num_clbits > 0, "Circuit missing measurements!"
□ if not any(isinstance(inst.operation, Measure) for inst in qc.data):
□     raise ValueError("Sampler requires measurements")

TRANSPILATION PATTERNS:
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
□ qc_transpiled = pm.run(qc)  # transpile before sampling
□ isa_circuit = qc.transpile(backend=backend)  # alternative
□ job = sampler.run([(qc_transpiled,)])  # run pre-transpiled circuit
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║           SECTION 5: SAMPLER - ONE-PAGE SUMMARY                       ║
║                      (12% of Exam - ~8 Questions)                      ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 BASIC USAGE WORKFLOW                                               ║
║  ├─ 1. IMPORTS                                                         ║
║  │   ├─ from qiskit.primitives import StatevectorSampler  # ideal    ║
║  │   └─ from qiskit_ibm_runtime import SamplerV2  # hardware         ║
║  ├─ 2. CREATE CIRCUIT + MEASUREMENTS (CRITICAL!)                      ║
║  │   ├─ qc = QuantumCircuit(2)                                        ║
║  │   ├─ qc.h(0); qc.cx(0,1)  # quantum operations                     ║
║  │   └─ qc.measure_all()  # ← REQUIRED! Sampler fails without this   ║
║  ├─ 3. INITIALIZE SAMPLER                                             ║
║  │   └─ sampler = StatevectorSampler()  # or SamplerV2(mode=backend) ║
║  ├─ 4. RUN WITH PUB FORMAT                                            ║
║  │   └─ job = sampler.run([(qc,)], shots=1024)  # note: (qc,) tuple! ║
║  ├─ 5. EXTRACT RESULTS                                                ║
║  │   ├─ result = job.result()  # PrimitiveResult                     ║
║  │   └─ counts = result[0].data.meas.get_counts()  # full chain      ║
║  └─ Key: MUST have measurements, MUST use tuple, MUST index result    ║
║                                                                        ║
║  📦 PUB FORMATS (Primitive Unified Bloc)                               ║
║  ├─ Anatomy: (circuit, parameters, shots)                             ║
║  │   ├─ circuit: QuantumCircuit with measurements                     ║
║  │   ├─ parameters: list of values or None (optional)                 ║
║  │   └─ shots: int override or None (optional, defaults to 1024)      ║
║  ├─ EXAMPLES:                                                          ║
║  │   ├─ Basic single:     [(qc,)]                    # trailing comma!║
║  │   ├─ With parameters:  [(qc, [0.5, 1.2])]        # 2 param values ║
║  │   ├─ Custom shots:     [(qc, None, 2048)]        # None placeholder║
║  │   ├─ Full spec:        [(qc, [0.5, 1.2], 2048)]  # all specified  ║
║  │   └─ Multiple PUBs:    [(qc1,), (qc2,), (qc3,)]  # batch 3 circuits║
║  └─ Critical: Each PUB must be TUPLE; list contains tuples            ║
║                                                                        ║
║  🔗 RESULT EXTRACTION CHAIN (MEMORIZE!)                                ║
║  ├─ Full path: result[0].data.meas.get_counts()                       ║
║  │   ├─ result       → PrimitiveResult (list-like container)          ║
║  │   ├─ [0]          → Index first PUB (PubResult object)             ║
║  │   ├─ .data        → DataBin (holds all classical registers)        ║
║  │   ├─ .meas        → BitArray for "meas" register (default name)    ║
║  │   └─ .get_counts()→ Method returning dict {'00': 512, '11': 512}   ║
║  ├─ Alternative methods on BitArray:                                   ║
║  │   ├─ .get_bitstrings()   → ['00', '11', '00', ...] (list)          ║
║  │   └─ .get_int_counts()   → {0: 512, 3: 512} (int keys)             ║
║  ├─ Custom register names:                                             ║
║  │   └─ result[0].data.output.get_counts()  # 'output' not 'meas'     ║
║  └─ Multi-PUB indexing:                                                ║
║      ├─ result[0].data.meas.get_counts()  # first circuit             ║
║      ├─ result[1].data.meas.get_counts()  # second circuit            ║
║      └─ result[i].data.meas.get_counts()  # i-th circuit              ║
║                                                                        ║
║  🔄 MULTIPLE CIRCUITS (Batch Processing)                               ║
║  ├─ Single submission:                                                 ║
║  │   └─ job = sampler.run([(qc1,), (qc2,), (qc3,)])                   ║
║  ├─ Individual access:                                                 ║
║  │   ├─ result[0]  → qc1 results                                      ║
║  │   ├─ result[1]  → qc2 results                                      ║
║  │   └─ result[2]  → qc3 results                                      ║
║  ├─ Iteration pattern:                                                 ║
║  │   ├─ for i, pub_result in enumerate(result):                       ║
║  │   │       counts = pub_result.data.meas.get_counts()                ║
║  │   └─ OR: all_counts = [r.data.meas.get_counts() for r in result]   ║
║  └─ Each PUB independent: separate shots, separate results            ║
║                                                                        ║
║  ⚙️ ADVANCED OPTIONS (sampler.options)                                 ║
║  ├─ Configuration types:                                               ║
║  │   ├─ .default_shots = 2048           # change default              ║
║  │   ├─ .optimization_level = 3         # transpiler (0-3)            ║
║  │   ├─ .resilience_level = 1           # error mitigation (0-2)      ║
║  │   ├─ .twirling.enable_gates = True   # randomized compilation      ║
║  │   ├─ .twirling.enable_measure = True # measurement twirling        ║
║  │   ├─ .twirling.num_randomizations=32 # rounds of twirling          ║
║  │   ├─ .dynamical_decoupling.enable=True  # idle qubit protection    ║
║  │   └─ .dynamical_decoupling.sequence_type='XY4'  # DD sequence      ║
║  ├─ Setting options:                                                   ║
║  │   ├─ options = sampler.options       # get current                 ║
║  │   ├─ options.default_shots = 4096    # modify                      ║
║  │   └─ sampler.options = options       # reassign (some cases)       ║
║  └─ Options persist across multiple run() calls on same instance      ║
║                                                                        ║
║  🎭 SAMPLER VS ESTIMATOR                                               ║
║  ├─ Sampler:                                                           ║
║  │   ├─ REQUIRES measurements in circuit                              ║
║  │   ├─ Returns: counts/bitstrings (discrete outcomes)                ║
║  │   ├─ PUB format: [(circuit,)]                                      ║
║  │   ├─ Use case: sampling probability distributions                  ║
║  │   └─ Twirling defaults: gates=False, measure=False (both OFF)      ║
║  ├─ Estimator:                                                         ║
║  │   ├─ NO measurements (forbidden)                                    ║
║  │   ├─ Returns: expectation values ⟨ψ|O|ψ⟩ (continuous)              ║
║  │   ├─ PUB format: [(circuit, observable)]                           ║
║  │   ├─ Use case: computing energy, observables                       ║
║  │   └─ Twirling defaults: gates=True, measure=True (both ON)         ║
║  └─ Key: Mutually exclusive patterns - don't mix!                     ║
║                                                                        ║
║  🔢 BIT ORDERING (Critical for Exam!)                                  ║
║  ├─ Qiskit uses LSB (Least Significant Bit first)                     ║
║  │   └─ Rightmost bit = qubit 0 (little-endian)                       ║
║  ├─ Reading bitstrings:                                                ║
║  │   ├─ '01' → q[0]=1, q[1]=0  (read right-to-left!)                  ║
║  │   ├─ '10' → q[0]=0, q[1]=1                                         ║
║  │   └─ '101' → q[0]=1, q[1]=0, q[2]=1                                ║
║  ├─ Conversion to integer:                                             ║
║  │   ├─ '01' in LSB = 2 in decimal (not 1!)                           ║
║  │   └─ Must reverse for standard conversion: int('01'[::-1], 2)      ║
║  └─ TRAP: Most frameworks use MSB (leftmost=q[0]); Qiskit opposite!   ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (HIGHEST PRIORITY!)                              ║
║  ╔════════════════════════════════════════════════════════════════╗  ║
║  ║ 1. ❌ No measurements → Sampler ERROR (not warning!)            ║  ║
║  ║    ✓ ALWAYS: qc.measure_all() before sampler.run()             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 2. ❌ sampler.run([qc]) - missing tuple wrapper                 ║  ║
║  ║    ✓ CORRECT: sampler.run([(qc,)]) with trailing comma         ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 3. ❌ sampler.run([(qc)]) - missing comma (NOT a tuple!)        ║  ║
║  ║    ✓ CORRECT: (qc,) with comma makes single-element tuple      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 4. ❌ result.data.meas.get_counts() - missing [0] index         ║  ║
║  ║    ✓ CORRECT: result[0].data.meas.get_counts()                 ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 5. ❌ result[0].meas.get_counts() - missing .data               ║  ║
║  ║    ✓ CORRECT: result[0].data.meas (never skip .data!)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 6. ❌ Assuming register always named "meas"                     ║  ║
║  ║    ✓ CHECK: qc.cregs[0].name for actual name                   ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 7. ❌ Twirling defaults: Sampler ≠ Estimator                    ║  ║
║  ║    ✓ Sampler: gates=False, measure=False (both OFF)            ║  ║
║  ║    ✓ Estimator: gates=True, measure=True (both ON)             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 8. ❌ Bit ordering: '01' ≠ q[0]=0, q[1]=1                       ║  ║
║  ║    ✓ CORRECT: '01' → q[0]=1, q[1]=0 (LSB = right-to-left)      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 9. ❌ get_counts() returns integers                             ║  ║
║  ║    ✓ Returns STRING keys: {'00': 512}                          ║  ║
║  ║    ✓ For ints use: get_int_counts() → {0: 512}                 ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 10. ❌ Wrong parameter count: [0.5] for 2-param circuit         ║  ║
║  ║     ✓ Must match exactly: 2 params need 2 values               ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 11. ❌ PUB order: (shots, circuit, params)                      ║  ║
║  ║     ✓ CORRECT: (circuit, params, shots) - "CPS"                ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 12. ❌ DD helps all circuits                                    ║  ║
║  ║     ✓ Only helps circuits with IDLE qubits during execution    ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 13. ❌ from qiskit.primitives import Sampler (V1, deprecated)   ║  ║
║  ║     ✓ CORRECT: import StatevectorSampler (V2) or SamplerV2     ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 14. ❌ Options set after run() affecting that job              ║  ║
║  ║     ✓ Options must be set BEFORE job submission                ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 15. ❌ Using shots=0 or negative                                ║  ║
║  ║     ✓ shots must be positive int (ValueError otherwise)        ║  ║
║  ╚════════════════════════════════════════════════════════════════╝  ║
║                                                                        ║
║  💡 MEMORY AIDS                                                        ║
║  ├─ "S needs M" - Sampler needs Measurements (CRITICAL!)              ║
║  ├─ "TiL" - Tuple in List: [(qc,)] format                             ║
║  ├─ "0-D-M-G" - result[0].data.meas.get_counts() chain                ║
║  ├─ "GOMO" - Gates Off, Measure Off (Sampler twirling defaults)       ║
║  ├─ "LSB = Little Side is Beginning" - rightmost = q[0]               ║
║  └─ "Comma Makes Tuple" - (qc,) is tuple, (qc) is not!                ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---


## ✅ Estimator Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS:
□ Estimator returns expectation values ⟨O⟩, Sampler returns counts/bitstrings
□ Estimator circuits MUST NOT have measurements ("ENM" - Estimator No Measures)
□ SparsePauliOp uses leftmost = qubit 0 ordering (opposite of bitstring convention)
□ PUB format: (circuit, observable, params, precision) for Estimator
□ Expectation value: ⟨O⟩ = ⟨ψ|O|ψ⟩ = sum of eigenvalues weighted by probabilities
□ VQE (Variational Quantum Eigensolver) minimizes ⟨H⟩ to find ground state energy
□ QAOA (Quantum Approximate Optimization) structure: Cost layer then Mixer layer
□ Resilience levels: 0=none (ideal), 1=M3 mitigation, 2=M3+ZNE
□ Twirling defaults: Estimator has enable_gates=True, enable_measure=True (both ON)
□ Gradient-free optimizers (COBYLA, SPSA) work best with noisy quantum hardware
□ Observable apply_layout() remaps qubits after transpilation
□ Multiple observables can share same circuit in single PUB
□ Result structure: result[0].data.evs (plural!) and result[0].data.stds

CONSTRAINTS & LIMITATIONS:
□ Estimator will ERROR if circuit contains any measurement gates (not just ignore)
□ Observable must match circuit qubit count (3-qubit circuit needs 3-character Pauli)
□ Maximum 300 PUBs per job submission in runtime (exceeding causes error)
□ precision parameter must be positive float (0 or negative causes ValueError)
□ Parameter binding must match circuit's num_parameters exactly
□ Cannot use ClassicalRegister with Estimator (no classical bits allowed)
□ SparsePauliOp coefficients must be real numbers (complex not supported for expectation)
□ Observable qubits cannot exceed circuit qubits (padding with 'I' if needed)
□ Each observable in list must have same number of qubits
□ Precision target is best-effort, not guaranteed (hardware limitations)
□ Session expires after 5 minutes idle (jobs fail if session closed)
□ Resilience level 2 significantly increases runtime (5-10x slower than level 0)

KEY DEFINITIONS:
□ Expectation value: Average measurement outcome ⟨ψ|O|ψ⟩ for observable O
□ Observable: Hermitian operator whose expectation value is computed
□ SparsePauliOp: Sparse representation of Pauli strings with coefficients
□ Pauli string: Tensor product of Pauli operators (I, X, Y, Z)
□ PUB (Primitive Unified Bloc): Tuple (circuit, observable, parameters, precision)
□ DataBin: Container holding evs (expectation values) and stds (standard deviations)
□ Hamiltonian: Energy operator whose ground state VQE finds
□ Ansatz: Parameterized quantum circuit (trial wavefunction)
□ Cost function: Objective to minimize, typically ⟨H⟩ in VQE
□ Resilience: Error mitigation techniques (M3, ZNE) to reduce noise impact
□ M3 mitigation: Matrix-free Measurement Mitigation
□ ZNE: Zero Noise Extrapolation - extrapolates to zero-noise limit
□ Twirling: Randomized compilation converting coherent to stochastic noise
□ apply_layout: Method to remap observable qubits after circuit transpilation

ARCHITECTURE & WORKFLOW:
□ Estimator uses V2 interface: run() returns Job, result() returns PrimitiveResult
□ StatevectorEstimator simulates ideal quantum computer (no noise)
□ EstimatorV2 connects to IBM Quantum hardware or noisy simulators
□ Runtime primitives batch-optimize multiple circuits for efficiency
□ Primitive options persist across multiple run() calls on same instance
□ Job queuing: jobs wait in QUEUED state until resources available
□ Results persist in cloud for 7 days after completion (then deleted)
□ Estimator internally samples and averages to estimate ⟨O⟩
□ Higher precision targets increase sampling shots automatically
□ Observable decomposition: complex observables split into Pauli basis

VQE & QAOA SPECIFICS:
□ VQE alternates: quantum (expectation) → classical (optimization) → repeat
□ QAOA structure: initial state (H gates) → Cost layer → Mixer layer → measure expectation
□ Cost layer encodes problem: phase gates implementing problem Hamiltonian
□ Mixer layer maintains superposition: typically X rotations on all qubits
□ QAOA parameter order: (γ, β) where γ = cost angle, β = mixer angle
□ VQE convergence depends on ansatz expressiveness and optimizer choice
□ COBYLA: Constrained Optimization BY Linear Approximation (gradient-free)
□ SPSA: Simultaneous Perturbation Stochastic Approximation (handles noise well)
□ Gradient-based optimizers (BFGS, L-BFGS-B) fail on noisy hardware

VERSION-SPECIFIC:
□ V1 Estimator deprecated: use V2 (EstimatorV2, not Estimator)
□ Old execute() removed in Qiskit 1.0 - use primitives exclusively
□ qiskit-ibm-runtime separate package required for hardware access
□ StatevectorEstimator in qiskit.primitives (local), EstimatorV2 in qiskit_ibm_runtime
□ SparsePauliOp replaces older Operator types in primitive workflows
```

### 💻 Code Pattern Checklist
```
ESSENTIAL IMPORTS:
□ from qiskit.primitives import StatevectorEstimator  # ideal/local simulation
□ from qiskit_ibm_runtime import EstimatorV2  # hardware/runtime
□ from qiskit_ibm_runtime import QiskitRuntimeService  # backend access
□ from qiskit.quantum_info import SparsePauliOp  # observable creation
□ from qiskit import QuantumCircuit  # circuit creation
□ from qiskit.circuit import Parameter  # parameterized circuits
□ from scipy.optimize import minimize  # VQE optimization
□ from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

ESTIMATOR INITIALIZATION:
□ estimator = StatevectorEstimator()  # no arguments, local ideal sim
□ service = QiskitRuntimeService(); backend = service.backend("ibm_brisbane")
□ estimator = EstimatorV2(mode=backend)  # runtime with specific backend
□ estimator = EstimatorV2(mode=backend, options=options_dict)  # with options
□ estimator = StatevectorEstimator(default_precision=0.01)  # custom precision
□ estimator = StatevectorEstimator(seed=42)  # reproducible simulation

OBSERVABLE CREATION:
□ obs = SparsePauliOp('Z')  # single qubit, single Pauli
□ obs = SparsePauliOp('ZZ')  # two qubits, Z⊗Z tensor product
□ obs = SparsePauliOp('XIZ')  # three qubits, X⊗I⊗Z (leftmost=q0)
□ obs = SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])  # weighted sum: 1.0*ZZ + 0.5*XX
□ obs = SparsePauliOp.from_list([('ZZ', 1.0), ('XX', 0.5)])  # alternative syntax
□ obs = SparsePauliOp(['ZI', 'IZ'], [0.5, 0.5])  # sum of single-qubit terms
□ H = SparsePauliOp(['ZZ', 'ZI', 'IZ', 'XX'], [1.0, -0.5, -0.5, 0.3])  # Hamiltonian
□ obs = SparsePauliOp('I' * n_qubits)  # identity (returns 1.0)
□ coeff, pauli_list = obs.coeffs, obs.paulis  # extract components

CIRCUIT PREPARATION (NO MEASUREMENTS!):
□ qc = QuantumCircuit(2)  # NO ClassicalRegister, NO measurements
□ qc.h(0); qc.cx(0, 1)  # quantum operations only
□ assert qc.num_clbits == 0, "Estimator requires no classical bits!"
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.ry(theta, 0); qc.rz(phi, 1)  # parameterized circuit
□ # DO NOT add qc.measure_all() or qc.measure() - ERROR!

BASIC RUN PATTERNS:
□ job = estimator.run([(qc, obs)])  # single circuit-observable pair
□ result = job.result()  # blocking call, waits for completion
□ ev = result[0].data.evs[0]  # extract first expectation value (note: evs is array!)
□ std = result[0].data.stds[0]  # extract first standard deviation
□ evs = result[0].data.evs  # all expectation values (if multiple observables)
□ stds = result[0].data.stds  # all standard deviations

PARAMETERIZED CIRCUITS:
□ theta = Parameter('θ'); phi = Parameter('φ')
□ qc.ry(theta, 0); qc.rz(phi, 1)  # add parameterized gates
□ job = estimator.run([(qc, obs, [0.5, 1.2])])  # bind [θ=0.5, φ=1.2]
□ job = estimator.run([(qc, obs, [0.5, 1.2], 0.01)])  # with precision target
□ job = estimator.run([(qc, obs, None, 0.01)])  # no params, custom precision
□ bound_qc = qc.assign_parameters([0.5, 1.2])  # pre-bind parameters
□ job = estimator.run([(bound_qc, obs)])  # run pre-bound circuit
□ param_values = [[0, 0], [0, π/2], [π/2, 0], [π/2, π/2]]
□ jobs = [estimator.run([(qc, obs, vals)]) for vals in param_values]  # sweep

MULTIPLE PUBS:
□ job = estimator.run([(qc1, obs1), (qc2, obs2), (qc3, obs3)])  # batch submission
□ result[0].data.evs  # qc1 expectation values
□ result[1].data.evs  # qc2 expectation values
□ result[2].data.evs  # qc3 expectation values
□ for i, pub_result in enumerate(result):  # iterate all
□     evs = pub_result.data.evs
□ all_evs = [r.data.evs for r in result]  # list comprehension

MULTIPLE OBSERVABLES (SAME CIRCUIT):
□ observables = [SparsePauliOp('ZZ'), SparsePauliOp('XX'), SparsePauliOp('YY')]
□ job = estimator.run([(qc, observables)])  # single PUB, multiple observables
□ evs = result[0].data.evs  # array: [⟨ZZ⟩, ⟨XX⟩, ⟨YY⟩]
□ stds = result[0].data.stds  # array: [σ_ZZ, σ_XX, σ_YY]
□ for obs, ev, std in zip(observables, evs, stds):  # iterate results

RESULT EXTRACTION: See Section 7 for full chain and metadata patterns
□ evs = result[0].data.evs  # array of expectation values (PLURAL!)
□ stds = result[0].data.stds  # array of standard deviations (PLURAL!)

TRANSPILATION & LAYOUT:
□ pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
□ qc_transpiled = pm.run(qc)  # transpile circuit
□ layout = qc_transpiled.layout  # extract layout information
□ obs_remapped = obs.apply_layout(layout)  # remap observable to match
□ job = estimator.run([(qc_transpiled, obs_remapped)])  # run with remapped obs

OPTIONS CONFIGURATION:
□ options = estimator.options  # get current options
□ estimator.options.default_precision = 0.01  # set precision target
□ options.resilience_level = 0  # no mitigation (ideal/debug)
□ options.resilience_level = 1  # enable M3 mitigation
□ options.resilience_level = 2  # enable M3 + ZNE (slower but better)
□ options.twirling.enable_gates = True  # gate twirling (default ON for Estimator)
□ options.twirling.enable_measure = True  # measurement twirling (default ON)
□ options.twirling.num_randomizations = 32  # set twirling rounds
□ options.dynamical_decoupling.enable = True  # enable DD
□ options.dynamical_decoupling.sequence_type = 'XY4'  # DD sequence
□ options.optimization_level = 3  # transpiler optimization (0-3)

VQE PATTERN (COMPLETE):
□ H = SparsePauliOp(['ZZ', 'ZI', 'IZ', 'XX'], [1.0, -0.5, -0.5, 0.3])  # Hamiltonian
□ ansatz = QuantumCircuit(2)  # NO measurements!
□ theta = Parameter('θ'); phi = Parameter('φ')
□ ansatz.ry(theta, 0); ansatz.ry(phi, 1); ansatz.cx(0, 1)
□ def cost_function(params):
□     bound_circuit = ansatz.assign_parameters(params)
□     job = estimator.run([(bound_circuit, H)])
□     return job.result()[0].data.evs[0]  # minimize this!
□ initial_params = [0.0, 0.0]
□ result = minimize(cost_function, initial_params, method='COBYLA')
□ optimal_energy = result.fun
□ optimal_params = result.x

QAOA PATTERN (COMPLETE):
□ def qaoa_circuit(gamma, beta, n_qubits):
□     qc = QuantumCircuit(n_qubits)
□     qc.h(range(n_qubits))  # initial superposition
□     # Cost layer (problem-specific)
□     for i in range(n_qubits-1):
□         qc.rzz(2*gamma, i, i+1)  # cost Hamiltonian
□     # Mixer layer
□     for i in range(n_qubits):
□         qc.rx(2*beta, i)  # mixer Hamiltonian
□     return qc  # NO measurements!
□ cost_hamiltonian = SparsePauliOp(['ZZ', 'ZI', 'IZ'], [1.0, 0.5, 0.5])
□ def qaoa_cost(params):
□     gamma, beta = params
□     qc = qaoa_circuit(gamma, beta, 2)
□     job = estimator.run([(qc, cost_hamiltonian)])
□     return job.result()[0].data.evs[0]
□ result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')

JOB MANAGEMENT: See Section 7 for full job status and management patterns

ERROR HANDLING (Estimator-specific):
□ assert qc.num_clbits == 0, "Estimator requires no classical bits!"
□ if any(isinstance(inst.operation, Measure) for inst in qc.data):
□     raise ValueError("Estimator circuits must not have measurements")
```


### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║         SECTION 6: ESTIMATOR - ONE-PAGE SUMMARY                       ║
║                      (12% of Exam - ~8 Questions)                      ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 BASIC USAGE WORKFLOW                                               ║
║  ├─ 1. IMPORTS                                                         ║
║  │   ├─ from qiskit.primitives import StatevectorEstimator  # ideal  ║
║  │   ├─ from qiskit_ibm_runtime import EstimatorV2  # hardware       ║
║  │   └─ from qiskit.quantum_info import SparsePauliOp                ║
║  ├─ 2. CREATE CIRCUIT WITHOUT MEASUREMENTS (CRITICAL!)                ║
║  │   ├─ qc = QuantumCircuit(2)  # NO ClassicalRegister               ║
║  │   ├─ qc.h(0); qc.cx(0,1)  # quantum operations                     ║
║  │   └─ NO qc.measure_all()! ← Estimator FORBIDS measurements        ║
║  ├─ 3. CREATE OBSERVABLE                                               ║
║  │   └─ obs = SparsePauliOp('ZZ')  # must match circuit qubit count  ║
║  ├─ 4. INITIALIZE ESTIMATOR                                            ║
║  │   └─ estimator = StatevectorEstimator()  # or EstimatorV2(backend)║
║  ├─ 5. RUN WITH PUB FORMAT                                             ║
║  │   └─ job = estimator.run([(qc, obs)])  # (circuit, observable)    ║
║  ├─ 6. EXTRACT EXPECTATION VALUES                                      ║
║  │   ├─ result = job.result()  # PrimitiveResult                     ║
║  │   └─ ev = result[0].data.evs[0]  # note: evs is array, [0] index!║
║  └─ Key: NO measurements, MUST have observable, evs plural            ║
║                                                                        ║
║  📊 SPARSEPAULI ORDERING (Critical for Exam!)                          ║
║  ├─ Convention: Leftmost character = qubit 0 (OPPOSITE of bitstrings)║
║  ├─ Examples:                                                          ║
║  │   ├─ SparsePauliOp('XIZ') = X⊗I⊗Z                                  ║
║  │   │   ├─ X acts on qubit 0 (leftmost)                              ║
║  │   │   ├─ I acts on qubit 1 (middle)                                ║
║  │   │   └─ Z acts on qubit 2 (rightmost)                             ║
║  │   ├─ SparsePauliOp('ZZ') = Z⊗Z on qubits 0,1                       ║
║  │   └─ Position matches qubit: string[i] → qubit i                   ║
║  └─ TRAP: Bitstrings use opposite convention! (rightmost = q0)        ║
║                                                                        ║
║  📦 PUB FORMATS (Primitive Unified Bloc)                               ║
║  ├─ Anatomy: (circuit, observable, parameters, precision)             ║
║  │   ├─ circuit: QuantumCircuit WITHOUT measurements                  ║
║  │   ├─ observable: SparsePauliOp (REQUIRED for Estimator!)           ║
║  │   ├─ parameters: list of values or None (optional)                 ║
║  │   └─ precision: float target or None (optional)                    ║
║  ├─ EXAMPLES:                                                          ║
║  │   ├─ Basic:           [(qc, obs)]                # minimal         ║
║  │   ├─ With params:     [(qc, obs, [0.5, 1.2])]  # 2 param values   ║
║  │   ├─ With precision:  [(qc, obs, None, 0.01)]  # None placeholder ║
║  │   ├─ Full spec:       [(qc, obs, [0.5], 0.01)] # all specified    ║
║  │   └─ Multiple PUBs:   [(qc1, obs1), (qc2, obs2), (qc3, obs3)]     ║
║  └─ Critical: Observable REQUIRED (unlike Sampler where it's absent)  ║
║                                                                        ║
║  🔗 RESULT EXTRACTION CHAIN (MEMORIZE!)                                ║
║  ├─ Full path: result[0].data.evs[0]                                  ║
║  │   ├─ result       → PrimitiveResult (list-like container)          ║
║  │   ├─ [0]          → Index first PUB (PubResult object)             ║
║  │   ├─ .data        → DataBin (holds expectation value arrays)       ║
║  │   ├─ .evs         → Array of expectation values (PLURAL!)          ║
║  │   └─ [0]          → Index first observable (evs is array)          ║
║  ├─ Alternative attributes:                                            ║
║  │   └─ .stds        → Array of standard deviations (also plural!)    ║
║  ├─ Multiple observables:                                              ║
║  │   ├─ evs = result[0].data.evs  # all values: [⟨O₁⟩, ⟨O₂⟩, ...]    ║
║  │   └─ stds = result[0].data.stds  # all stds: [σ₁, σ₂, ...]        ║
║  └─ Multi-PUB indexing:                                                ║
║      ├─ result[0].data.evs  # first circuit-observable                ║
║      ├─ result[1].data.evs  # second circuit-observable               ║
║      └─ result[i].data.evs  # i-th PUB                                ║
║                                                                        ║
║  🔄 MULTIPLE OBSERVABLES (Efficiency Pattern)                          ║
║  ├─ Single circuit, multiple observables (efficient!):                ║
║  │   ├─ obs_list = [SparsePauliOp('ZZ'), SparsePauliOp('XX')]        ║
║  │   ├─ job = estimator.run([(qc, obs_list)])  # one PUB             ║
║  │   ├─ evs = result[0].data.evs  # array: [⟨ZZ⟩, ⟨XX⟩]              ║
║  │   └─ Benefit: shares circuit evaluation across observables         ║
║  └─ Multiple PUBs (separate circuits):                                 ║
║      ├─ job = estimator.run([(qc1, obs1), (qc2, obs2)])               ║
║      ├─ ev1 = result[0].data.evs[0]  # from qc1                       ║
║      └─ ev2 = result[1].data.evs[0]  # from qc2                       ║
║                                                                        ║
║  🧬 VQE PATTERN (Variational Quantum Eigensolver)                      ║
║  ├─ Purpose: Find ground state energy of Hamiltonian                  ║
║  ├─ Components:                                                        ║
║  │   ├─ H = SparsePauliOp([...])  # Hamiltonian (energy operator)    ║
║  │   ├─ ansatz = parameterized circuit (NO measurements)              ║
║  │   ├─ cost_func: params → ⟨H⟩ (expectation value)                   ║
║  │   └─ optimizer: minimize cost_func (COBYLA recommended)            ║
║  ├─ Complete workflow:                                                 ║
║  │   ├─ 1. def cost_function(params):                                 ║
║  │   │       bound_qc = ansatz.assign_parameters(params)              ║
║  │   │       job = estimator.run([(bound_qc, H)])                     ║
║  │   │       return job.result()[0].data.evs[0]                       ║
║  │   ├─ 2. initial_params = [0.0, 0.0]  # or random                  ║
║  │   ├─ 3. result = minimize(cost_function, initial_params,           ║
║  │   │                        method='COBYLA')                        ║
║  │   ├─ 4. optimal_energy = result.fun                                ║
║  │   └─ 5. optimal_params = result.x                                  ║
║  └─ Key: Ansatz NO measurements, use COBYLA (gradient-free)           ║
║                                                                        ║
║  🔄 QAOA PATTERN (Quantum Approximate Optimization Algorithm)          ║
║  ├─ Purpose: Approximate solution to combinatorial optimization       ║
║  ├─ Structure (MEMORIZE ORDER!):                                       ║
║  │   ├─ 1. Initial state: qc.h(range(n))  # equal superposition      ║
║  │   ├─ 2. Cost layer: encode problem (γ parameter)                  ║
║  │   │   └─ qc.rzz(2*gamma, i, j)  # for each problem edge           ║
║  │   ├─ 3. Mixer layer: maintain superposition (β parameter)          ║
║  │   │   └─ qc.rx(2*beta, i)  # for each qubit                       ║
║  │   └─ 4. NO measurements! (Use Estimator to get ⟨H⟩)                ║
║  ├─ Parameter convention:                                              ║
║  │   ├─ γ (gamma) controls Cost layer                                 ║
║  │   ├─ β (beta) controls Mixer layer                                 ║
║  │   └─ Order: (γ, β) - "Cost then Mixer" or "CostMix"                ║
║  ├─ Complete example:                                                  ║
║  │   ├─ def qaoa_cost(params):                                        ║
║  │   │       gamma, beta = params                                     ║
║  │   │       qc = build_qaoa_circuit(gamma, beta)                     ║
║  │   │       job = estimator.run([(qc, cost_hamiltonian)])            ║
║  │   │       return job.result()[0].data.evs[0]                       ║
║  │   └─ result = minimize(qaoa_cost, [0.5, 0.5], method='COBYLA')    ║
║  └─ Critical: Cost BEFORE Mixer (γ before β)                          ║
║                                                                        ║
║  ⚙️ ADVANCED OPTIONS (estimator.options)                               ║
║  ├─ Error mitigation:                                                  ║
║  │   ├─ .resilience_level = 0  # none (ideal/fastest)                ║
║  │   ├─ .resilience_level = 1  # M3 mitigation (moderate)            ║
║  │   └─ .resilience_level = 2  # M3+ZNE (best but 5-10x slower)      ║
║  ├─ Twirling (randomized compilation):                                ║
║  │   ├─ .twirling.enable_gates = True   # default ON for Estimator  ║
║  │   ├─ .twirling.enable_measure = True # default ON for Estimator  ║
║  │   └─ .twirling.num_randomizations = 32  # rounds of randomization ║
║  ├─ Circuit optimization:                                              ║
║  │   ├─ .optimization_level = 3  # transpiler (0-3)                  ║
║  │   └─ .default_precision = 0.01  # target precision                ║
║  └─ Dynamical Decoupling:                                              ║
║      ├─ .dynamical_decoupling.enable = True                           ║
║      └─ .dynamical_decoupling.sequence_type = 'XY4'                   ║
║                                                                        ║
║  🎭 ESTIMATOR VS SAMPLER (See Section 5 for full comparison)           ║
║  ├─ Key difference: Estimator NO measurements, Sampler REQUIRES them   ║
║  ├─ Estimator: result[0].data.evs (expectation values, array)         ║
║  ├─ Sampler: result[0].data.meas.get_counts() (counts dict)           ║
║  └─ Twirling: Estimator ON/ON, Sampler OFF/OFF                        ║
║                                                                        ║
║  🔢 OBSERVABLE CONSTRUCTION                                            ║
║  ├─ Single Pauli string:                                               ║
║  │   ├─ SparsePauliOp('Z')    # single qubit                          ║
║  │   ├─ SparsePauliOp('ZZ')   # two qubits                            ║
║  │   └─ SparsePauliOp('XIZ')  # three qubits (X⊗I⊗Z)                  ║
║  ├─ Weighted sum (Hamiltonian):                                        ║
║  │   ├─ SparsePauliOp(['ZZ', 'XX'], [1.0, 0.5])  # 1.0*ZZ + 0.5*XX   ║
║  │   └─ Alternative: SparsePauliOp.from_list([('ZZ', 1.0), ...])     ║
║  ├─ Qubit count constraint:                                            ║
║  │   └─ Must match circuit: 3-qubit circuit → 3-char Pauli string     ║
║  └─ Special cases:                                                     ║
║      ├─ Identity: SparsePauliOp('III') → always returns 1.0           ║
║      └─ After transpile: obs.apply_layout(layout) to remap qubits     ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (HIGHEST PRIORITY!)                              ║
║  ╔════════════════════════════════════════════════════════════════╗  ║
║  ║ 1. ❌ Adding measurements → Estimator ERROR (not warning!)      ║  ║
║  ║    ✓ NEVER use measure() or measure_all() with Estimator       ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 2. ❌ Using string observable: estimator.run([(qc, 'ZZ')])      ║  ║
║  ║    ✓ MUST use SparsePauliOp: run([(qc, SparsePauliOp('ZZ'))])  ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 3. ❌ result[0].evs - missing .data                             ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (never skip .data!)           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 4. ❌ result[0].data.ev - using singular (no such attribute!)   ║  ║
║  ║    ✓ CORRECT: result[0].data.evs (plural with s!)              ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 5. ❌ Parameters as scalar: (qc, obs, 0.5)                      ║  ║
║  ║    ✓ MUST be list: (qc, obs, [0.5]) even for single param!     ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 6. ❌ Using Sampler PUB format: [(qc,)]                         ║  ║
║  ║    ✓ Estimator needs observable: [(qc, obs)]                   ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 7. ❌ Gradient optimizers: BFGS, L-BFGS-B (fail with noise)     ║  ║
║  ║    ✓ Use gradient-free: method='COBYLA' or 'SPSA'              ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 8. ❌ QAOA order: Mixer then Cost                               ║  ║
║  ║    ✓ CORRECT: Cost then Mixer (γ before β) "CostMix"           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 9. ❌ Ordering: 'ZIX' means X on q0 (WRONG!)                    ║  ║
║  ║    ✓ SparsePauliOp 'ZIX' = Z on q0, I on q1, X on q2 (L→R)     ║  ║
║  ║    ✓ OPPOSITE of bitstrings! ('01' = rightmost q0)             ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 10. ❌ Not using apply_layout() after transpilation             ║  ║
║  ║     ✓ MUST remap: obs.apply_layout(transpiled.layout)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 11. ❌ Twirling defaults: assuming same as Sampler              ║  ║
║  ║     ✓ Estimator: gates=True, measure=True (both ON)            ║  ║
║  ║     ✓ Sampler: gates=False, measure=False (both OFF)           ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 12. ❌ Observable qubit mismatch: 3-qubit circuit, 'ZZ' obs     ║  ║
║  ║     ✓ MUST match: 3 qubits → 'ZZI' or 'XIZ' (3 chars)          ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 13. ❌ Forgetting assign_parameters() in VQE loop               ║  ║
║  ║     ✓ MUST bind: bound = ansatz.assign_parameters(params)      ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 14. ❌ Treating evs as scalar when it's array                   ║  ║
║  ║     ✓ evs is array: use evs[0] to extract single value         ║  ║
║  ╟────────────────────────────────────────────────────────────────╢  ║
║  ║ 15. ❌ Using V1 import: from qiskit.primitives import Estimator ║  ║
║  ║     ✓ CORRECT V2: import StatevectorEstimator or EstimatorV2   ║  ║
║  ╚════════════════════════════════════════════════════════════════╝  ║
║                                                                        ║
║  💡 MEMORY AIDS (CRITICAL!)                                            ║
║  ├─ "ENM" - Estimator No Measures (MOST CRITICAL!)                    ║
║  ├─ "TiPO" - Tensor in Pauli Order (leftmost = q0)                    ║
║  ├─ "0-D-EVS" - result[0].data.evs chain (plural!)                    ║
║  ├─ "COPP" - Circuit Observable Params Precision                      ║
║  ├─ "COBYLA for Quantum" - gradient-free optimizer                    ║
║  ├─ "CostMix" - Cost layer then Mixer layer (γ before β)              ║
║  ├─ "012 = None-M3-ZNE" - resilience levels                           ║
║  └─ "GMGM vs GOMO" - Estimator (on/on) vs Sampler (off/off)           ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---


## ✅ Results Key Takeaways

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


## ✅ OpenQASM Key Takeaways

### 📚 Concept Checklist
```
CORE CONCEPTS - Version Differences
□ QASM 2.0 vs 3.0: Different syntax for headers, includes, registers, and measurements
□ QASM 2.0 is legacy format, widely supported, simpler syntax
□ QASM 3.0 is modern format with programming language features
□ QASM header MUST be first line: "OPENQASM 2.0;" or "OPENQASM 3.0;"
□ Version number in header determines parser behavior
□ QASM 2.0 header is case-sensitive: "OPENQASM" (not "OpenQASM")
□ QASM 3.0 supports backwards compatibility with 2.0 constructs
□ Include statement MUST come after OPENQASM header
□ qelib1.inc provides gate library for QASM 2.0
□ stdgates.inc provides standard gates for QASM 3.0
□ Cannot mix QASM 2.0 and 3.0 syntax in same file
□ QASM files typically use .qasm extension for both versions
□ QASM is human-readable text format (not binary)

MODULE FUNCTIONS - qasm2 and qasm3
□ qasm2 module functions: loads(), dumps(), load(), dump() for QASM 2.0
□ qasm3 module functions: loads(), dumps(), load(), dump() for QASM 3.0
□ Both modules must be explicitly imported: from qiskit import qasm2, qasm3
□ qasm2 and qasm3 are separate modules (not submodules of QuantumCircuit)
□ String methods end with 's': loads()/dumps() work with strings
□ File methods without 's': load()/dump() work with file objects
□ loads() returns QuantumCircuit object from QASM string
□ dumps() returns QASM string from QuantumCircuit object
□ load() returns QuantumCircuit object from file object
□ dump() writes QASM to file object (returns None)
□ All functions accept QuantumCircuit as input for export
□ All functions return QuantumCircuit for import operations
□ qasm2/qasm3 functions are NOT methods of QuantumCircuit

LEGACY QUANTUMCIRCUIT METHODS
□ QuantumCircuit legacy methods: qasm(), from_qasm_str(), from_qasm_file()
□ qc.qasm() is instance method - exports to QASM 2.0 ONLY
□ qc.qasm() returns string (equivalent to qasm2.dumps(qc))
□ from_qasm_str() is STATIC method (call on QuantumCircuit class)
□ from_qasm_file() is STATIC method (call on QuantumCircuit class)
□ from_qasm_str() accepts QASM 2.0 string only (not 3.0)
□ from_qasm_file() accepts filepath string (not file object)
□ from_qasm_file() opens and closes file automatically
□ Legacy methods maintained for backward compatibility
□ Prefer qasm2/qasm3 modules for new code (more explicit)

REGISTER SYNTAX DIFFERENCES
□ Register syntax: qreg/creg (QASM 2.0) vs qubit[]/bit[] (QASM 3.0)
□ QASM 2.0: qreg q[5]; declares 5-qubit quantum register
□ QASM 2.0: creg c[5]; declares 5-bit classical register
□ QASM 3.0: qubit[5] q; declares 5-qubit register (type-first syntax)
□ QASM 3.0: bit[5] c; declares 5-bit classical register
□ Register names must start with lowercase letter in both versions
□ Register size is specified in brackets: [n] for n qubits/bits
□ Individual qubit/bit access uses zero-based indexing: q[0], q[1], etc.
□ Registers must be declared before use in circuit
□ QASM 2.0 allows multiple qreg/creg declarations
□ QASM 3.0 supports array syntax for modern programming style

MEASUREMENT SYNTAX DIFFERENCES
□ Measurement syntax: arrow (QASM 2.0) vs assignment (QASM 3.0)
□ QASM 2.0: measure q[0] -> c[0]; (arrow from qubit to classical bit)
□ QASM 3.0: c[0] = measure q[0]; (assignment style)
□ QASM 2.0 arrow direction: qubit -> classical (left to right)
□ QASM 3.0 reverses order: classical = qubit (assignment semantics)
□ Both syntaxes measure single qubit to single classical bit
□ Can measure entire register: measure q -> c; (QASM 2.0)
□ Semicolon required at end of measurement statement in both versions
□ Measurement is destructive operation (collapses qubit state)

GATE DEFINITIONS AND OPERATIONS
□ Standard gates: h, x, y, z, s, t, rx, ry, rz, cx, etc.
□ Custom gates can be defined in QASM using 'gate' keyword
□ Gate parameters use parentheses: rx(pi/4) q[0];
□ Gate targets use brackets: cx q[0], q[1];
□ QASM 2.0 gates come from qelib1.inc include
□ QASM 3.0 gates come from stdgates.inc include
□ Gate definitions support parameterization with angles
□ U gate is universal single-qubit gate: U(θ,φ,λ)
□ CX gate is controlled-NOT (CNOT) in both versions

QASM 3.0 ADVANCED FEATURES
□ QASM 3.0 supports more features (conditionals, loops, expressions)
□ QASM 3.0 allows if statements: if (c == 1) { ... }
□ QASM 3.0 allows for loops: for i in [0:5] { ... }
□ QASM 3.0 supports arithmetic expressions: angle = pi/4 + theta;
□ QASM 3.0 has real type for floating-point values
□ QASM 3.0 supports classical computation within circuit
□ QASM 3.0 allows function definitions (not in 2.0)
□ QASM 3.0 supports arrays and complex data types

IMPORT/EXPORT CONSTRAINTS
□ Roundtrip import/export may lose some circuit information
□ Not all Qiskit features can be represented in QASM
□ Custom gates may need manual definitions in QASM
□ Metadata, labels, and names may not survive roundtrip
□ Complex instructions may be decomposed during export
□ Parameter expressions might be evaluated during export
□ Circuit barriers may or may not be preserved
□ Some optimizations may be applied during import/export

VERSION DETECTION AND COMPATIBILITY
□ QASM version identified by header: "OPENQASM 2.0;" vs "OPENQASM 3.0;"
□ Parser automatically detects version from header
□ Cannot parse QASM 3.0 file with qasm2 module (will error)
□ Cannot parse QASM 2.0 features with qasm3 if incompatible
□ Version mismatch causes parse errors
□ No automatic version conversion (must use qasm2→qasm3 explicitly)
```

### 💻 Code Pattern Checklist
```
IMPORT STATEMENTS
□ from qiskit import QuantumCircuit - imports QuantumCircuit class
□ from qiskit import qasm2 - imports QASM 2.0 module
□ from qiskit import qasm3 - imports QASM 3.0 module
□ from qiskit import qasm2, qasm3 - imports both modules (recommended)
□ from qiskit.qasm2 import loads, dumps - import specific functions
□ from qiskit.qasm3 import loads, dumps - import specific functions
□ No need to import QuantumCircuit.qasm() (already instance method)
□ qasm2/qasm3 are top-level imports from qiskit package

EXPORT TO STRING - dumps() and qasm()
□ qc.qasm() exports circuit to QASM 2.0 string (instance method)
□ qc.qasm() returns str type
□ qc.qasm() takes NO parameters (parameterless method)
□ qasm2.dumps(qc) exports circuit to QASM 2.0 string (function)
□ qasm2.dumps(qc) returns str type
□ qasm2.dumps(circuit) takes QuantumCircuit as first parameter
□ qasm3.dumps(qc) exports circuit to QASM 3.0 string (function)
□ qasm3.dumps(qc) returns str type
□ qasm3.dumps(circuit) takes QuantumCircuit as first parameter
□ qc.qasm() == qasm2.dumps(qc) - equivalent QASM 2.0 exports
□ print(qc.qasm()) - display QASM 2.0 string to console
□ print(qasm3.dumps(qc)) - display QASM 3.0 string to console
□ qasm_str = qc.qasm() - store QASM 2.0 string in variable
□ qasm3_str = qasm3.dumps(qc) - store QASM 3.0 string in variable

EXPORT TO FILE - dump() Methods
□ qasm2.dump(qc, file) writes circuit to QASM 2.0 file (function)
□ qasm2.dump(circuit, file) takes QuantumCircuit and file object
□ qasm2.dump() returns None (writes to file, no return value)
□ qasm3.dump(qc, file) writes circuit to QASM 3.0 file (function)
□ qasm3.dump(circuit, file) takes QuantumCircuit and file object
□ qasm3.dump() returns None (writes to file, no return value)
□ with open('circuit.qasm', 'w') as f: qasm2.dump(qc, f) - QASM 2.0 file write
□ with open('circuit.qasm', 'w') as f: qasm3.dump(qc, f) - QASM 3.0 file write
□ File must be opened in write mode 'w' for dump()
□ dump() parameter order: (circuit, file) NOT (file, circuit)
□ Always use context manager (with open) for file safety
□ dump() automatically flushes and writes to disk

IMPORT FROM STRING - loads() and from_qasm_str()
□ qasm2.loads(string) imports QASM 2.0 string (function)
□ qasm2.loads(qasm_str) returns QuantumCircuit object
□ qasm2.loads(str) takes string as only required parameter
□ qasm3.loads(string) imports QASM 3.0 string (function)
□ qasm3.loads(qasm_str) returns QuantumCircuit object
□ qasm3.loads(str) takes string as only required parameter
□ QuantumCircuit.from_qasm_str(string) imports QASM 2.0 string (STATIC!)
□ QuantumCircuit.from_qasm_str(s) is CLASS method (call on QuantumCircuit)
□ QuantumCircuit.from_qasm_str(s) returns QuantumCircuit object
□ QuantumCircuit.from_qasm_str() ONLY works with QASM 2.0 (not 3.0)
□ from_qasm_str() is legacy method (prefer qasm2.loads() for clarity)
□ qc = qasm2.loads(qasm_string) - import QASM 2.0 string
□ qc = qasm3.loads(qasm_string) - import QASM 3.0 string
□ qc = QuantumCircuit.from_qasm_str(qasm_string) - legacy QASM 2.0 import

IMPORT FROM FILE - load() and from_qasm_file()
□ qasm2.load(file) imports QASM 2.0 from file object (function)
□ qasm2.load(file_obj) returns QuantumCircuit object
□ qasm2.load(f) takes file object as parameter (not filepath string)
□ qasm3.load(file) imports QASM 3.0 from file object (function)
□ qasm3.load(file_obj) returns QuantumCircuit object
□ qasm3.load(f) takes file object as parameter (not filepath string)
□ QuantumCircuit.from_qasm_file(filepath) imports QASM 2.0 file (STATIC!)
□ QuantumCircuit.from_qasm_file(path) is CLASS method (call on QuantumCircuit)
□ QuantumCircuit.from_qasm_file(path) returns QuantumCircuit object
□ from_qasm_file() takes filepath STRING (not file object)
□ from_qasm_file() opens/closes file automatically (convenience method)
□ from_qasm_file() is legacy method (prefer qasm2.load() for clarity)
□ with open('circuit.qasm', 'r') as f: qc = qasm2.load(f) - QASM 2.0 file import
□ with open('circuit.qasm', 'r') as f: qc = qasm3.load(f) - QASM 3.0 file import
□ qc = QuantumCircuit.from_qasm_file('circuit.qasm') - legacy QASM 2.0 import
□ File must be opened in read mode 'r' for load()

PARAMETER TYPES AND RETURN VALUES
□ dumps(circuit) parameter: QuantumCircuit object (required)
□ dumps() return type: str (QASM string)
□ dump(circuit, file) parameters: QuantumCircuit, file object (both required)
□ dump() return type: None (side effect: writes to file)
□ loads(string) parameter: str (QASM string, required)
□ loads() return type: QuantumCircuit object
□ load(file) parameter: file object in read mode (required)
□ load() return type: QuantumCircuit object
□ qasm() parameter: None (parameterless method)
□ qasm() return type: str (QASM 2.0 string)
□ from_qasm_str(string) parameter: str (QASM 2.0 string, required)
□ from_qasm_str() return type: QuantumCircuit object
□ from_qasm_file(filepath) parameter: str (filepath, required)
□ from_qasm_file() return type: QuantumCircuit object

CONVERSION PATTERNS
□ qasm3.dumps(qasm2.loads(qasm2_str)) converts QASM 2.0 to 3.0
□ qasm2.dumps(qasm3.loads(qasm3_str)) converts QASM 3.0 to 2.0 (if compatible)
□ qc_copy = qasm2.loads(qc.qasm()) - create copy via QASM roundtrip
□ qc_copy = qasm2.loads(qasm2.dumps(qc)) - alternative roundtrip
□ Conversion may lose version-specific features (e.g., QASM 3.0 loops)
□ Always test roundtrip fidelity for critical circuits

ROUNDTRIP TESTING
□ imported_qc = qasm2.loads(qc.qasm()) roundtrip test
□ assert qc == imported_qc may fail (use circuit equivalence check)
□ Compare circuit depth, gate count, qubit count after roundtrip
□ qasm_str = qc.qasm(); qc2 = qasm2.loads(qasm_str) - two-step roundtrip
□ Verify gate sequence preserved: qc.data == imported_qc.data (may differ)

FILE PATH HANDLING
□ Use raw strings for Windows paths: r'C:\Users\file.qasm'
□ Use forward slashes for cross-platform: 'path/to/circuit.qasm'
□ Relative paths: './circuit.qasm' or 'circuits/bell.qasm'
□ Absolute paths: '/home/user/circuit.qasm'
□ Path objects: from pathlib import Path; Path('circuit.qasm')
□ Check file exists: import os; os.path.exists('circuit.qasm')

ERROR HANDLING PATTERNS
□ try: qc = qasm2.loads(qasm_str) except Exception as e: print(e)
□ Catch parse errors for invalid QASM syntax
□ Catch FileNotFoundError for missing files
□ Catch PermissionError for file access issues
□ Validate QASM header before parsing
□ Check version compatibility before loading

COMMON USAGE PATTERNS
□ Save circuit: with open('out.qasm', 'w') as f: qasm2.dump(qc, f)
□ Load circuit: with open('in.qasm', 'r') as f: qc = qasm2.load(f)
□ Quick export: qasm_string = qc.qasm()
□ Quick import: qc = QuantumCircuit.from_qasm_str(qasm_string)
□ Version conversion: qasm3_str = qasm3.dumps(qasm2.loads(qasm2_str))
□ String comparison: assert qc.qasm() == qasm2.dumps(qc)
□ Print to file: print(qc.qasm(), file=open('out.qasm', 'w'))
□ Read from file: qasm_str = open('circuit.qasm').read(); qc = qasm2.loads(qasm_str)

EQUIVALENCE CHECKS
□ qc.qasm() == qasm2.dumps(qc) - ALWAYS True (equivalent methods)
□ qasm2.loads(qc.qasm()) creates equivalent circuit (not identical object)
□ Use circuit.depth(), circuit.size() for structural comparison
□ Compare num_qubits, num_clbits for register compatibility
□ Whitespace and comments may differ in QASM string output
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║         SECTION 8: OPENQASM - ONE-PAGE SUMMARY                        ║
║                      (6% of Exam - ~4 Questions)                       ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  📤 EXPORT (Circuit → String/File)                                     ║
║  ├─ STRING EXPORT                                                      ║
║  │  ├─ QASM 2.0: qc.qasm() [instance method, returns str]             ║
║  │  ├─ QASM 2.0: qasm2.dumps(qc) [function, returns str]              ║
║  │  └─ QASM 3.0: qasm3.dumps(qc) [function, returns str]              ║
║  ├─ FILE EXPORT                                                        ║
║  │  ├─ QASM 2.0: qasm2.dump(qc, file_obj) [returns None]              ║
║  │  └─ QASM 3.0: qasm3.dump(qc, file_obj) [returns None]              ║
║  ├─ KEY POINTS                                                         ║
║  │  ├─ qc.qasm() is LEGACY, QASM 2.0 ONLY                             ║
║  │  ├─ dumps() has 's' → returns String                               ║
║  │  ├─ dump() no 's' → writes to File, returns None                   ║
║  │  └─ dump() parameter order: dump(circuit, file) NOT (file, circuit)║
║                                                                        ║
║  📥 IMPORT (String/File → Circuit)                                     ║
║  ├─ STRING IMPORT                                                      ║
║  │  ├─ QASM 2.0 Legacy: QuantumCircuit.from_qasm_str(s) [STATIC!]     ║
║  │  ├─ QASM 2.0 Modern: qasm2.loads(string) [returns QuantumCircuit]  ║
║  │  └─ QASM 3.0: qasm3.loads(string) [returns QuantumCircuit]         ║
║  ├─ FILE IMPORT                                                        ║
║  │  ├─ QASM 2.0 Legacy: QuantumCircuit.from_qasm_file(path) [STATIC!] ║
║  │  │                    Takes filepath STRING                         ║
║  │  ├─ QASM 2.0 Modern: qasm2.load(file_obj) [returns QuantumCircuit] ║
║  │  └─ QASM 3.0: qasm3.load(file_obj) [returns QuantumCircuit]        ║
║  ├─ KEY POINTS                                                         ║
║  │  ├─ from_qasm_* are STATIC methods (call on CLASS, not instance!)  ║
║  │  ├─ from_qasm_* ONLY support QASM 2.0                              ║
║  │  ├─ loads() has 's' → takes String parameter                       ║
║  │  ├─ load() no 's' → takes File object parameter                    ║
║  │  ├─ from_qasm_file() takes filepath STRING (auto opens/closes)     ║
║  │  └─ load() takes FILE OBJECT (use with context manager)            ║
║                                                                        ║
║  📦 REQUIRED IMPORTS                                                   ║
║  ├─ from qiskit import QuantumCircuit  [for from_qasm_*]              ║
║  ├─ from qiskit import qasm2           [for qasm2.loads/dumps/etc]    ║
║  ├─ from qiskit import qasm3           [for qasm3.loads/dumps/etc]    ║
║  └─ NOTE: qc.qasm() needs NO import (instance method)                 ║
║                                                                        ║
║  📊 VERSION COMPARISON TABLE                                           ║
║  ┌──────────────────┬─────────────────────┬────────────────────────┐  ║
║  │ Feature          │ QASM 2.0            │ QASM 3.0               │  ║
║  ├──────────────────┼─────────────────────┼────────────────────────┤  ║
║  │ Header           │ OPENQASM 2.0;       │ OPENQASM 3.0;          │  ║
║  │ Include file     │ qelib1.inc          │ stdgates.inc           │  ║
║  │ Qubit register   │ qreg q[2];          │ qubit[2] q;            │  ║
║  │ Classical reg    │ creg c[2];          │ bit[2] c;              │  ║
║  │ Measurement      │ measure q -> c;     │ c = measure q;         │  ║
║  │ Gate syntax      │ h q[0];             │ h q[0]; (same)         │  ║
║  │ Conditionals     │ ✗ Not supported     │ ✓ if (c==1) { ... }    │  ║
║  │ Loops            │ ✗ Not supported     │ ✓ for i in [0:5] {...} │  ║
║  │ Expressions      │ ✗ Limited           │ ✓ angle = pi/4 + x;    │  ║
║  │ Real type        │ ✗ Not supported     │ ✓ real theta;          │  ║
║  └──────────────────┴─────────────────────┴────────────────────────┘  ║
║                                                                        ║
║  🔄 CONVERSION PATTERNS                                                ║
║  ├─ QASM 2.0 → 3.0 (usually safe):                                    ║
║  │  └─ qasm3_str = qasm3.dumps(qasm2.loads(qasm2_str))                ║
║  ├─ QASM 3.0 → 2.0 (may fail if QASM 3.0 features used):              ║
║  │  └─ qasm2_str = qasm2.dumps(qasm3.loads(qasm3_str))                ║
║  ├─ Roundtrip test:                                                    ║
║  │  └─ qc_new = qasm2.loads(qc.qasm())                                ║
║  └─ Version equivalence check:                                         ║
║     └─ assert qc.qasm() == qasm2.dumps(qc)  # Always True             ║
║                                                                        ║
║  📁 FILE OPERATION PATTERNS                                            ║
║  ├─ SAVE QASM 2.0:                                                     ║
║  │  └─ with open('circuit.qasm', 'w') as f: qasm2.dump(qc, f)         ║
║  ├─ LOAD QASM 2.0:                                                     ║
║  │  └─ with open('circuit.qasm', 'r') as f: qc = qasm2.load(f)        ║
║  ├─ SAVE QASM 3.0:                                                     ║
║  │  └─ with open('circuit.qasm', 'w') as f: qasm3.dump(qc, f)         ║
║  ├─ LOAD QASM 3.0:                                                     ║
║  │  └─ with open('circuit.qasm', 'r') as f: qc = qasm3.load(f)        ║
║  └─ LEGACY LOAD (QASM 2.0 only):                                      ║
║     └─ qc = QuantumCircuit.from_qasm_file('circuit.qasm')             ║
║                                                                        ║
║  🔑 KEY SYNTAX DIFFERENCES                                             ║
║  ├─ MEASUREMENT                                                        ║
║  │  ├─ QASM 2.0: measure q[0] -> c[0];  [arrow: qubit -> classical]   ║
║  │  └─ QASM 3.0: c[0] = measure q[0];   [assignment: classical = ...]  ║
║  ├─ REGISTER DECLARATION                                               ║
║  │  ├─ QASM 2.0: qreg q[5]; creg c[5];  [keyword: qreg/creg]          ║
║  │  └─ QASM 3.0: qubit[5] q; bit[5] c;  [type annotation: qubit/bit]  ║
║  ├─ INCLUDE FILES                                                      ║
║  │  ├─ QASM 2.0: include "qelib1.inc";   [standard gate library]      ║
║  │  └─ QASM 3.0: include "stdgates.inc"; [standard gates]             ║
║  ├─ HEADER (ALWAYS FIRST LINE)                                        ║
║  │  ├─ QASM 2.0: OPENQASM 2.0;  [case-sensitive, uppercase]           ║
║  │  └─ QASM 3.0: OPENQASM 3.0;  [case-sensitive, uppercase]           ║
║  └─ ADVANCED FEATURES (QASM 3.0 ONLY)                                 ║
║     ├─ Conditionals: if (c == 1) { h q[0]; }                          ║
║     ├─ Loops: for i in [0:4] { rx(pi/4) q[i]; }                       ║
║     ├─ Variables: real angle = pi/4;                                   ║
║     └─ Expressions: angle = theta + phi;                              ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (MEMORIZE!)                                      ║
║  ┌────────────────────────────────────────────────────────────────┐   ║
║  │ STATIC METHOD TRAPS                                            │   ║
║  │ 1. from_qasm_str() is STATIC                                   │   ║
║  │    ✗ qc.from_qasm_str(s)                                       │   ║
║  │    ✓ QuantumCircuit.from_qasm_str(s)                           │   ║
║  │ 2. from_qasm_file() is STATIC                                  │   ║
║  │    ✗ qc.from_qasm_file(path)                                   │   ║
║  │    ✓ QuantumCircuit.from_qasm_file(path)                       │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ STRING VS FILE TRAPS                                           │   ║
║  │ 3. loads() takes STRING, load() takes FILE OBJECT              │   ║
║  │    ✗ qasm2.load("OPENQASM 2.0;...")                            │   ║
║  │    ✓ qasm2.loads("OPENQASM 2.0;...")                           │   ║
║  │ 4. dumps() returns STRING, dump() returns NONE                 │   ║
║  │    ✗ qasm_str = qasm2.dump(qc, file)  # Returns None!          │   ║
║  │    ✓ qasm_str = qasm2.dumps(qc)       # Returns string         │   ║
║  │ 5. dump() parameter order: (circuit, file) NOT (file, circuit) │   ║
║  │    ✗ qasm2.dump(f, qc)                                         │   ║
║  │    ✓ qasm2.dump(qc, f)                                         │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ VERSION CONFUSION TRAPS                                        │   ║
║  │ 6. qc.qasm() ONLY returns QASM 2.0 (never 3.0)                 │   ║
║  │    ✗ Expecting qc.qasm() to return QASM 3.0                    │   ║
║  │    ✓ Use qasm3.dumps(qc) for QASM 3.0                          │   ║
║  │ 7. from_qasm_str() ONLY supports QASM 2.0                      │   ║
║  │    ✗ QuantumCircuit.from_qasm_str(qasm3_string)                │   ║
║  │    ✓ qasm3.loads(qasm3_string)                                 │   ║
║  │ 8. Arrow (2.0) vs Assignment (3.0) measurement syntax          │   ║
║  │    QASM 2.0: measure q -> c;                                   │   ║
║  │    QASM 3.0: c = measure q;  (reversed order!)                 │   ║
║  │ 9. qelib1.inc (2.0) vs stdgates.inc (3.0)                      │   ║
║  │    ✗ include "stdgates.inc"; in QASM 2.0                       │   ║
║  │    ✓ include "qelib1.inc"; in QASM 2.0                         │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ MODULE VS METHOD TRAPS                                         │   ║
║  │ 10. qasm2/qasm3 are MODULES, not circuit methods               │   ║
║  │     ✗ qc.qasm2.dumps()                                         │   ║
║  │     ✓ qasm2.dumps(qc)                                          │   ║
║  │ 11. Must import qasm2/qasm3 modules                            │   ║
║  │     ✗ qasm2.dumps(qc)  # Without import                        │   ║
║  │     ✓ from qiskit import qasm2; qasm2.dumps(qc)                │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ FILE HANDLING TRAPS                                            │   ║
║  │ 12. from_qasm_file() takes FILEPATH STRING                     │   ║
║  │     load() takes FILE OBJECT                                   │   ║
║  │     ✗ qasm2.load('circuit.qasm')  # Expects file object!       │   ║
║  │     ✓ with open('circuit.qasm') as f: qasm2.load(f)            │   ║
║  │ 13. Wrong file mode causes errors                              │   ║
║  │     dump() needs 'w', load() needs 'r'                         │   ║
║  │     ✗ open('file.qasm', 'r') with dump()                       │   ║
║  │     ✓ open('file.qasm', 'w') with dump()                       │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ SYNTAX TRAPS                                                   │   ║
║  │ 14. OPENQASM must be UPPERCASE (case-sensitive)                │   ║
║  │     ✗ OpenQASM 2.0; or openqasm 2.0;                           │   ║
║  │     ✓ OPENQASM 2.0;                                            │   ║
║  │ 15. Register syntax differs by version                         │   ║
║  │     QASM 2.0: qreg q[2]; creg c[2];                            │   ║
║  │     QASM 3.0: qubit[2] q; bit[2] c;                            │   ║
║  │     ✗ Mixing syntaxes causes parse error                       │   ║
║  └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║  💡 QUICK REFERENCE CHEATSHEET                                         ║
║  ├─ Export to string: qc.qasm() or qasm2.dumps(qc) or qasm3.dumps(qc) ║
║  ├─ Import from string: qasm2.loads(s) or qasm3.loads(s)              ║
║  ├─ Export to file: qasm2.dump(qc, f) or qasm3.dump(qc, f)            ║
║  ├─ Import from file: qasm2.load(f) or qasm3.load(f)                  ║
║  ├─ Remember: 's' = string, no 's' = file                             ║
║  ├─ Remember: from_qasm_* are STATIC (call on class)                  ║
║  ├─ Remember: qc.qasm() is QASM 2.0 ONLY                              ║
║  └─ Remember: dump(circuit, file) order, returns None                 ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```

---

## ✅ Quantum Info Key Takeaways

### 📚 Concept Checklist
```
CLIFFORD GATES AND CIRCUITS
□ Clifford gates: H, S, CNOT, Pauli (X, Y, Z) - efficiently simulatable
□ T gate is NOT Clifford (HSCP mnemonic excludes T)
□ Tdg (T-dagger) is also NOT Clifford (conjugate of T)
□ Clifford circuits can be simulated classically in polynomial time
□ Gottesman-Knill theorem: Clifford circuits are classically simulatable
□ Clifford group: normalizer of Pauli group
□ H (Hadamard) gate: creates superposition, Clifford
□ S gate: phase gate (√Z), Clifford
□ CNOT (CX) gate: two-qubit Clifford gate
□ Pauli gates (X, Y, Z): single-qubit Clifford gates
□ Identity gate (I) is trivially Clifford
□ SWAP gate is Clifford (can be decomposed into CNOTs)
□ CZ (Controlled-Z) gate is Clifford
□ Clifford gates preserve computational basis under stabilizer formalism
□ Clifford + T gates form universal gate set
□ Clifford circuits map Pauli operators to Pauli operators
□ Non-Clifford gates: T, Tdg, Toffoli, rotation gates (Rx, Ry, Rz)
□ Clifford tableau representation: compact stabilizer representation

OPERATOR CLASS AND OPERATIONS
□ Operator class represents full unitary matrix for gates/circuits
□ Operator stores 2^n × 2^n complex matrix for n qubits
□ operator.equiv() compares operators ignoring global phase
□ == operator checks exact equality (phase matters!)
□ Global phase difference: e^(iφ) doesn't affect measurements
□ Operators can represent gates, circuits, or arbitrary unitaries
□ Operator composition: op1.compose(op2) applies op2 first
□ Operator tensor product: op1.tensor(op2) creates op1 ⊗ op2
□ Operator.from_label() creates operator from Pauli string
□ Operator supports arithmetic: +, -, *, @ (matrix multiply)
□ Operator.power(n) raises operator to power n
□ Operator.conjugate() returns complex conjugate
□ Operator.transpose() returns matrix transpose
□ Operator.adjoint() returns Hermitian adjoint (dagger)
□ Unitary operators satisfy U†U = I (adjoint is inverse)
□ Operator.is_unitary() checks if operator is unitary

STATEVECTOR - PURE QUANTUM STATES
□ Statevector represents pure quantum states: |ψ⟩ = Σ αᵢ|i⟩
□ Statevector stores complex amplitudes for 2^n basis states
□ Normalization constraint: Σ |αᵢ|² = 1 (probability conservation)
□ Statevector.from_label() creates from computational basis label
□ Statevector.from_instruction() creates from circuit/gate
□ Statevector.from_int() creates basis state from integer
□ Statevector can only represent pure states (no mixed states)
□ Superposition states are pure states (e.g., |+⟩, |−⟩)
□ Entangled states are pure states (e.g., Bell states)
□ Statevector.probabilities() returns measurement probabilities
□ Statevector.sample_counts() simulates measurement outcomes
□ Statevector.expectation_value() computes ⟨ψ|O|ψ⟩
□ Statevector supports arithmetic operations (+, -, scalar multiply)
□ Inner product: sv1.inner(sv2) computes ⟨ψ₁|ψ₂⟩
□ Statevector.evolve() applies gate/circuit to state
□ Statevector is represented as column vector (ket)

DENSITYMATRIX - PURE AND MIXED STATES
□ DensityMatrix represents pure AND mixed states: ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|
□ DensityMatrix stores 2^n × 2^n Hermitian matrix
□ Pure state: purity = 1, Mixed state: purity < 1
□ Pure state: ρ = |ψ⟩⟨ψ|, rank-1 matrix
□ Mixed state: ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|, rank > 1 (classical mixture)
□ Superposition (|+⟩) is pure state, not mixed state
□ Thermal states, maximally mixed states are mixed
□ DensityMatrix.purity() returns Tr(ρ²), range [1/d, 1]
□ Trace constraint: Tr(ρ) = 1 (total probability = 1)
□ Positive semidefinite: ρ ≥ 0 (non-negative eigenvalues)
□ Hermitian: ρ = ρ† (equal to its adjoint)
□ DensityMatrix.from_label() creates from basis label
□ DensityMatrix.from_instruction() creates from circuit
□ DensityMatrix(statevector) converts pure state to density matrix
□ Partial trace: reduces system by tracing out subsystems
□ DensityMatrix.partial_trace() removes qubits from density matrix
□ Mixed states arise from decoherence, noise, or partial information
□ Maximally mixed state: ρ = I/d, purity = 1/d
□ DensityMatrix.evolve() applies channels/unitaries
□ DensityMatrix.expectation_value() computes Tr(ρO)

FIDELITY MEASURES
□ Fidelity measures similarity between states/operators, range [0, 1]
□ state_fidelity() returns 1 for identical states, 0 for orthogonal
□ State fidelity: F(ρ, σ) = [Tr√(√ρ σ √ρ)]²
□ Pure state fidelity: F(|ψ⟩, |φ⟩) = |⟨ψ|φ⟩|²
□ Process fidelity: compares quantum channels/operations
□ Average gate fidelity (AGF): average over all input states
□ AGF = (d·F_avg + 1)/(d+1) where d is dimension
□ Fidelity is symmetric: F(ρ, σ) = F(σ, ρ)
□ Fidelity = 1: states/processes are identical
□ Fidelity = 0: states/processes are orthogonal
□ Fidelity is continuous and concave
□ Bures distance: D(ρ, σ) = √(2 - 2√F(ρ, σ))
□ process_fidelity() for comparing unitaries/channels
□ average_gate_fidelity() is standard gate quality metric
□ Fidelity invariant under unitary transformations
□ Trace distance: alternative distance measure for states

QUANTUM CHANNELS AND NOISE
□ Quantum channels: Kraus (physical), SuperOp (mathematical), Choi (tomography)
□ Kraus representation: E(ρ) = Σᵢ Kᵢ ρ Kᵢ†
□ Kraus operators satisfy completeness: Σᵢ Kᵢ†Kᵢ = I
□ SuperOp: vectorized representation, maps vec(ρ) to vec(E(ρ))
□ Choi representation: Choi-Jamiołkowski isomorphism
□ All channel representations are mathematically equivalent
□ Completely positive trace-preserving (CPTP) maps
□ Depolarizing channel: ρ → (1-p)ρ + p·I/d
□ Amplitude damping: models energy dissipation (T1 decay)
□ Phase damping: models dephasing (T2 decay)
□ Pauli channel: combination of X, Y, Z errors
□ Bit-flip channel: applies X with probability p
□ Phase-flip channel: applies Z with probability p
□ Channel composition: apply channels sequentially
□ Quantum channels are linear maps on density matrices

RANDOMIZED BENCHMARKING
□ Randomized Benchmarking (RB) measures gate errors (SPAM-free)
□ Average gate fidelity (AGF) is standard metric for gate quality
□ RB protocol: apply random Clifford sequences
□ SPAM-free: insensitive to State Preparation And Measurement errors
□ RB measures average error rate over gate set
□ Decay curve: fidelity vs sequence length
□ Error per Clifford (EPC) extracted from decay rate
□ Interleaved RB: measures specific gate fidelity
□ Simultaneous RB: characterizes cross-talk errors
□ RB assumes time-independent, Markovian errors
□ Standard RB uses only Clifford gates
□ Purity benchmarking: variant measuring purity decay

OPERATOR COMPOSITION AND ALGEBRA
□ compose() order: op1.compose(op2) applies op2 first, then op1 (right-to-left)
□ Composition follows matrix multiplication convention
□ op1 @ op2 is matrix product (equivalent to compose in reverse)
□ Tensor product: op1.tensor(op2) creates product state/operator
□ Tensor product is associative: (A⊗B)⊗C = A⊗(B⊗C)
□ Partial trace reduces density matrix by tracing out subsystems
□ Partial trace over qubits: sum over traced qubit basis states
□ Partial trace preserves total probability (trace)
□ Schmidt decomposition: entanglement measure for pure bipartite states
□ Operator power: op.power(n) computes op^n

ADVANCED CONCEPTS
□ Stabilizer states: special class of quantum states
□ Stabilizer formalism: efficient classical simulation
□ Pauli group: all n-qubit Pauli operators
□ Measurement in different bases: computational, Hadamard, etc.
□ Expectation values: ⟨O⟩ = ⟨ψ|O|ψ⟩ or Tr(ρO)
□ Variance: ⟨O²⟩ - ⟨O⟩² for observable O
□ Entropy: S(ρ) = -Tr(ρ log ρ) for density matrix
□ Entanglement entropy: entropy of reduced density matrix
□ Concurrence: entanglement measure for two-qubit states
□ Negativity: entanglement measure using partial transpose
□ Process tomography: reconstruct quantum channel
□ State tomography: reconstruct quantum state
```

### 💻 Code Pattern Checklist
```
IMPORT STATEMENTS
□ from qiskit.quantum_info import Clifford - import Clifford class
□ from qiskit.quantum_info import Operator - import Operator class
□ from qiskit.quantum_info import Statevector - import Statevector class
□ from qiskit.quantum_info import DensityMatrix - import DensityMatrix class
□ from qiskit.quantum_info import state_fidelity - import state fidelity function
□ from qiskit.quantum_info import process_fidelity - import process fidelity
□ from qiskit.quantum_info import average_gate_fidelity - import AGF
□ from qiskit.quantum_info import partial_trace - import partial trace
□ from qiskit.quantum_info import entropy - import entropy calculation
□ from qiskit.quantum_info import concurrence - import concurrence measure
□ All quantum_info imports from qiskit.quantum_info module
□ Can combine imports: from qiskit.quantum_info import Clifford, Operator

CLIFFORD CLASS - CREATION AND CONVERSION
□ clifford = Clifford(circuit) creates Clifford object from circuit
□ Clifford(circuit) raises QiskitError if non-Clifford gates present
□ clifford = Clifford(gate) creates Clifford from single gate
□ clifford = Clifford.from_circuit(circuit) alternative constructor
□ clifford = Clifford.from_label(label) creates from Pauli string
□ circuit = clifford.to_circuit() converts Clifford back to circuit
□ circuit = clifford.to_circuit(method='optimal') optimized conversion
□ clifford.to_operator() converts to Operator (full matrix)
□ Clifford objects are more memory-efficient than Operator for Clifford gates
□ clifford.num_qubits returns number of qubits
□ clifford.conjugate() returns conjugate Clifford
□ clifford.transpose() returns transpose Clifford
□ clifford.adjoint() returns Hermitian adjoint
□ clifford.compose(other) composes two Cliffords
□ clifford.tensor(other) tensor product of Cliffords
□ clifford.expand(other) reverse tensor product

OPERATOR CLASS - CREATION
□ op = Operator(gate) creates operator from gate
□ op = Operator(circuit) creates operator from circuit
□ op = Operator(matrix) creates operator from NumPy array
□ op = Operator.from_label(label) creates from Pauli string label
□ op = Operator.from_circuit(circuit) alternative constructor
□ Operator stores full 2^n × 2^n unitary matrix
□ op.data returns NumPy array of operator matrix
□ op.dim returns tuple (input_dim, output_dim)
□ op.num_qubits returns number of qubits (None if not power of 2)
□ Operator(Statevector) creates projection operator |ψ⟩⟨ψ|
□ Operator can represent any unitary or non-unitary matrix

OPERATOR CLASS - COMPARISON AND EQUIVALENCE
□ op1.equiv(op2) checks equivalence ignoring global phase (returns bool)
□ op1.equiv(op2, rtol=1e-5) specify relative tolerance
□ op1 == op2 checks exact equality including phase
□ op1 != op2 checks inequality (exact)
□ equiv() is recommended for quantum operator comparison
□ Global phase e^(iφ) doesn't affect physical predictions
□ op.is_unitary() checks if operator is unitary
□ op.is_unitary(atol=1e-8) specify absolute tolerance

OPERATOR CLASS - COMPOSITION AND ALGEBRA
□ composed = op1.compose(op2) applies op2 first, then op1
□ composed = op1.compose(op2, qargs=[0,1]) compose on specific qubits
□ composed = op1.compose(op2, front=True) applies op1 first (reversed)
□ composed = op1 & op2 shorthand for compose (& operator)
□ tensor_prod = op1.tensor(op2) creates tensor product op1 ⊗ op2
□ tensor_prod = op1 ^ op2 shorthand for tensor (^ operator)
□ expanded = op1.expand(op2) reverse tensor: op2 ⊗ op1
□ result = op1 @ op2 matrix multiplication (same as compose reversed)
□ result = op1 + op2 operator addition
□ result = op1 - op2 operator subtraction
□ result = scalar * op scalar multiplication
□ result = op * scalar scalar multiplication (commutative)
□ powered = op.power(n) raises operator to power n
□ powered = op ** n shorthand for power (** operator)
□ conjugated = op.conjugate() returns complex conjugate
□ transposed = op.transpose() returns matrix transpose
□ adjointed = op.adjoint() returns Hermitian adjoint (dagger)

STATEVECTOR CLASS - CREATION
□ sv = Statevector(array) creates from NumPy array/list
□ sv = Statevector.from_label('+') creates |+⟩ state from label
□ sv = Statevector.from_label('0') creates |0⟩ state
□ sv = Statevector.from_label('-') creates |−⟩ state
□ sv = Statevector.from_label('01') creates |01⟩ multi-qubit state
□ sv = Statevector.from_instruction(circuit) creates state from circuit
□ sv = Statevector.from_instruction(gate) creates state from gate
□ sv = Statevector.from_int(i, dims) creates basis state |i⟩
□ sv = Statevector.from_int(0, 2**n) creates |0...0⟩ n-qubit state
□ Statevector automatically normalizes input (or raises error if zero)
□ sv.data returns NumPy array of amplitudes
□ sv.num_qubits returns number of qubits
□ sv.dim returns dimension (2^n for n qubits)

STATEVECTOR CLASS - METHODS AND OPERATIONS
□ sv.draw() displays statevector (default: text)
□ sv.draw('text') displays as text
□ sv.draw('latex') displays in LaTeX format (Jupyter)
□ sv.draw('qsphere') displays on Q-sphere
□ sv.draw('bloch') displays single qubit on Bloch sphere
□ probs = sv.probabilities() returns measurement probability array
□ probs = sv.probabilities(qargs=[0]) probabilities for specific qubits
□ counts = sv.sample_counts(shots) simulates measurement outcomes
□ memory = sv.sample_memory(shots) returns list of measurement results
□ exp_val = sv.expectation_value(op) computes ⟨ψ|O|ψ⟩
□ exp_val = sv.expectation_value(pauli_string) expectation of Pauli
□ inner_prod = sv1.inner(sv2) computes ⟨ψ₁|ψ₂⟩
□ sv_new = sv.evolve(gate) applies gate to statevector
□ sv_new = sv.evolve(circuit) applies circuit to statevector
□ sv.conjugate() returns complex conjugate
□ result = sv1 + sv2 adds statevectors (not normalized)
□ result = sv1 - sv2 subtracts statevectors
□ result = scalar * sv scalar multiplication
□ sv.is_valid() checks if statevector is normalized
□ sv.measure() performs measurement, returns outcome and post-measurement state
□ sv.reset(qargs) resets specified qubits to |0⟩

DENSITYMATRIX CLASS - CREATION
□ dm = DensityMatrix(statevector) converts pure state to density matrix
□ dm = DensityMatrix(operator) creates from operator
□ dm = DensityMatrix(matrix) creates from NumPy array
□ dm = DensityMatrix.from_label('0') creates density matrix from label
□ dm = DensityMatrix.from_label('+') creates |+⟩⟨+| density matrix
□ dm = DensityMatrix.from_instruction(circuit) creates from circuit
□ dm = DensityMatrix.from_instruction(gate) creates from gate
□ dm = DensityMatrix.from_int(i, dims) creates basis state density matrix
□ dm.data returns NumPy array of density matrix
□ dm.num_qubits returns number of qubits
□ dm.dim returns dimension (2^n for n qubits)

DENSITYMATRIX CLASS - METHODS AND PROPERTIES
□ dm.draw() displays density matrix (default: text)
□ dm.draw('latex') displays in LaTeX format
□ dm.draw('qsphere') displays on Q-sphere
□ purity = dm.purity() returns purity Tr(ρ²), range [1/d, 1]
□ purity = 1 indicates pure state
□ purity < 1 indicates mixed state
□ dm.is_valid() checks if valid density matrix (Hermitian, positive, trace=1)
□ exp_val = dm.expectation_value(op) computes Tr(ρO)
□ probs = dm.probabilities() returns measurement probabilities
□ probs = dm.probabilities(qargs=[0]) probabilities for specific qubits
□ dm_reduced = partial_trace(dm, qargs) traces out specified qubits
□ dm.evolve(channel) applies quantum channel to density matrix
□ dm.evolve(unitary) applies unitary to density matrix
□ dm_new = dm.evolve(gate) applies gate evolution
□ counts = dm.sample_counts(shots) simulates measurements
□ memory = dm.sample_memory(shots) returns measurement results
□ dm.measure(qargs) performs measurement on specified qubits
□ dm.reset(qargs) resets specified qubits to |0⟩
□ result = dm1 + dm2 adds density matrices
□ result = dm1 - dm2 subtracts density matrices
□ result = scalar * dm scalar multiplication

FIDELITY FUNCTIONS - STATE FIDELITY
□ fid = state_fidelity(state1, state2) computes state fidelity
□ state_fidelity(sv1, sv2) works with Statevectors
□ state_fidelity(dm1, dm2) works with DensityMatrices
□ state_fidelity(sv, dm) mixed input types allowed
□ fid = state_fidelity(state1, state2, validate=False) skip validation
□ Returns float in range [0, 1]
□ 1 means identical states, 0 means orthogonal
□ State fidelity is symmetric: F(ρ,σ) = F(σ,ρ)
□ For pure states: F = |⟨ψ₁|ψ₂⟩|²

FIDELITY FUNCTIONS - PROCESS AND GATE FIDELITY
□ fid = process_fidelity(op1, op2) computes process fidelity
□ process_fidelity works with Operators, Channels
□ process_fidelity(op1, op2, require_cp=True) check completely positive
□ process_fidelity(op1, op2, require_tp=True) check trace preserving
□ Returns float in range [0, 1]
□ agf = average_gate_fidelity(op1, op2) computes average gate fidelity
□ average_gate_fidelity is standard metric for gate quality
□ AGF averages fidelity over all input states
□ Relationship: AGF = (d·F_process + 1)/(d+1)
□ average_gate_fidelity(op1, op2, require_cptp=True) validate channel

PARTIAL TRACE AND SUBSYSTEM OPERATIONS
□ reduced = partial_trace(dm, qargs) traces out specified qubits
□ partial_trace(dm, [0, 2]) traces out qubits 0 and 2
□ partial_trace returns DensityMatrix of reduced system
□ Partial trace preserves trace: Tr(reduced) = Tr(dm)
□ Used to obtain reduced density matrix of subsystem
□ partial_trace(sv, qargs) also works with Statevectors

ENTROPY AND ENTANGLEMENT MEASURES
□ S = entropy(dm) computes von Neumann entropy
□ entropy(dm, base=2) specify base (default: 2 for qubits)
□ Returns entropy S(ρ) = -Tr(ρ log ρ)
□ Entropy = 0 for pure states
□ Entropy > 0 for mixed states
□ conc = concurrence(state) computes concurrence (2-qubit entanglement)
□ Concurrence ∈ [0, 1], 0 = separable, 1 = maximally entangled
□ Concurrence only defined for two-qubit states

QUANTUM CHANNELS (ADVANCED)
□ from qiskit.quantum_info import Kraus, SuperOp, Choi
□ kraus = Kraus(operators_list) creates Kraus channel
□ superop = SuperOp(matrix) creates SuperOp channel
□ choi = Choi(matrix) creates Choi channel
□ channel.to_operator() converts channel to operator (if unitary)
□ dm_out = channel(dm_in) applies channel to density matrix
□ All channels can be composed: ch1.compose(ch2)
□ Channels support conversion between representations
```

### 📋 One-Page Summary Box
```
╔═══════════════════════════════════════════════════════════════════════╗
║      SECTION 9: QUANTUM INFORMATION - ONE-PAGE SUMMARY                ║
║                      (8% of Exam - ~5-6 Questions)                     ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  🎯 CLIFFORD CIRCUITS                                                  ║
║  ├─ CLIFFORD GATES (HSCP - No T!)                                     ║
║  │  ├─ H (Hadamard): creates superposition                            ║
║  │  ├─ S gate: phase gate (√Z)                                        ║
║  │  ├─ CNOT (CX): two-qubit controlled-NOT                            ║
║  │  ├─ Pauli gates: X, Y, Z                                           ║
║  │  ├─ Also Clifford: I, CZ, SWAP                                     ║
║  │  └─ NOT Clifford: T, Tdg, Rx, Ry, Rz, Toffoli                      ║
║  ├─ PROPERTIES                                                         ║
║  │  ├─ Efficiently simulatable (Gottesman-Knill theorem)              ║
║  │  ├─ Map Pauli operators to Pauli operators                         ║
║  │  └─ Polynomial-time classical simulation                           ║
║  ├─ CODE USAGE                                                         ║
║  │  ├─ clifford = Clifford(circuit)  # Error if non-Clifford          ║
║  │  ├─ circuit = clifford.to_circuit()  # Convert back                ║
║  │  └─ clifford.to_operator()  # Convert to full matrix               ║
║  └─ EXAM TIP: "HSCP - No T!" mnemonic                                 ║
║                                                                        ║
║  🔧 OPERATOR CLASS                                                     ║
║  ├─ CREATION                                                           ║
║  │  ├─ op = Operator(gate)  # From single gate                        ║
║  │  ├─ op = Operator(circuit)  # From entire circuit                  ║
║  │  ├─ op = Operator(matrix)  # From NumPy array                      ║
║  │  └─ op = Operator.from_label('XYZ')  # Pauli string                ║
║  ├─ COMPARISON (CRITICAL FOR EXAM!)                                   ║
║  │  ├─ op1.equiv(op2)  # Phase-invariant (USE THIS!)                  ║
║  │  ├─ op1 == op2  # Exact equality (phase matters)                   ║
║  │  └─ Global phase e^(iφ) doesn't affect measurements                ║
║  ├─ COMPOSITION (order matters!)                                      ║
║  │  ├─ composed = op1.compose(op2)  # op2 FIRST, then op1             ║
║  │  ├─ Like matrix: AB applies B first (right-to-left)                ║
║  │  ├─ compose(op2, front=True)  # Reverses order                     ║
║  │  └─ op1 @ op2  # Matrix multiply (op2 first)                       ║
║  ├─ TENSOR PRODUCT                                                     ║
║  │  ├─ tensor = op1.tensor(op2)  # op1 ⊗ op2                          ║
║  │  ├─ tensor = op1 ^ op2  # Shorthand for tensor                     ║
║  │  └─ Creates product space (parallel qubits)                        ║
║  └─ UNITARY OPERATIONS                                                 ║
║     ├─ op.adjoint()  # Hermitian adjoint (†)                          ║
║     ├─ op.conjugate()  # Complex conjugate                            ║
║     ├─ op.transpose()  # Matrix transpose                             ║
║     └─ op.is_unitary()  # Check U†U = I                               ║
║                                                                        ║
║  📐 STATEVECTOR (Pure States Only)                                     ║
║  ├─ CREATION METHODS                                                   ║
║  │  ├─ sv = Statevector(array)  # From NumPy array                    ║
║  │  ├─ sv = Statevector.from_label('+')  # Standard labels            ║
║  │  │    Labels: '0', '1', '+', '-', 'r', 'l'                         ║
║  │  ├─ sv = Statevector.from_instruction(circuit)  # From circuit     ║
║  │  └─ sv = Statevector.from_int(i, dims)  # Basis state |i⟩          ║
║  ├─ KEY PROPERTIES                                                     ║
║  │  ├─ Represents PURE states only (no mixed states)                  ║
║  │  ├─ Normalization: Σ |αᵢ|² = 1                                     ║
║  │  ├─ Superposition states are pure (|+⟩, |−⟩)                       ║
║  │  └─ Entangled states are pure (Bell states)                        ║
║  ├─ METHODS                                                            ║
║  │  ├─ sv.probabilities()  # Measurement probabilities                ║
║  │  ├─ sv.sample_counts(shots)  # Simulate measurements               ║
║  │  ├─ sv.expectation_value(op)  # ⟨ψ|O|ψ⟩                            ║
║  │  ├─ sv.evolve(gate)  # Apply gate                                  ║
║  │  ├─ sv.inner(sv2)  # Inner product ⟨ψ₁|ψ₂⟩                         ║
║  │  └─ sv.draw('latex')  # Visualize                                  ║
║  └─ SIZE: 2^n complex amplitudes for n qubits                         ║
║                                                                        ║
║  🎭 DENSITYMATRIX (Pure + Mixed States)                                ║
║  ├─ CREATION METHODS                                                   ║
║  │  ├─ dm = DensityMatrix(statevector)  # Pure from SV                ║
║  │  ├─ dm = DensityMatrix(matrix)  # From array                       ║
║  │  ├─ dm = DensityMatrix.from_label('0')  # Standard labels          ║
║  │  └─ dm = DensityMatrix.from_instruction(circuit)                   ║
║  ├─ PURE VS MIXED                                                      ║
║  │  ├─ Pure state: ρ = |ψ⟩⟨ψ|, purity = 1, rank = 1                  ║
║  │  ├─ Mixed state: ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|, purity < 1, rank > 1           ║
║  │  ├─ purity = dm.purity()  # Tr(ρ²) ∈ [1/d, 1]                      ║
║  │  └─ Superposition ≠ mixed (|+⟩ is pure!)                           ║
║  ├─ CONSTRAINTS (ALL must be satisfied)                               ║
║  │  ├─ Hermitian: ρ = ρ†                                              ║
║  │  ├─ Positive semidefinite: ρ ≥ 0 (eigenvalues ≥ 0)                 ║
║  │  ├─ Trace = 1: Tr(ρ) = 1                                           ║
║  │  └─ Pure iff: Tr(ρ²) = 1                                           ║
║  ├─ METHODS                                                            ║
║  │  ├─ dm.expectation_value(op)  # Tr(ρO)                             ║
║  │  ├─ dm.probabilities()  # Measurement probs                        ║
║  │  ├─ dm.evolve(channel)  # Apply channel/unitary                    ║
║  │  └─ partial_trace(dm, qargs)  # Trace out qubits                   ║
║  └─ SIZE: 2^n × 2^n Hermitian matrix for n qubits                     ║
║                                                                        ║
║  📊 FIDELITY MEASURES (Range: [0, 1])                                  ║
║  ├─ STATE FIDELITY                                                     ║
║  │  ├─ fid = state_fidelity(state1, state2)                           ║
║  │  ├─ Works with Statevector or DensityMatrix                        ║
║  │  ├─ Pure states: F = |⟨ψ₁|ψ₂⟩|²                                    ║
║  │  └─ General: F = [Tr√(√ρ σ √ρ)]²                                   ║
║  ├─ PROCESS FIDELITY                                                   ║
║  │  ├─ fid = process_fidelity(op1, op2)                               ║
║  │  ├─ Compares Operators or Channels                                 ║
║  │  └─ Measures how similar two processes are                         ║
║  ├─ AVERAGE GATE FIDELITY (AGF)                                       ║
║  │  ├─ agf = average_gate_fidelity(op1, op2)                          ║
║  │  ├─ Standard gate quality metric                                   ║
║  │  ├─ Averaged over all input states                                 ║
║  │  └─ AGF = (d·F_process + 1)/(d+1)                                  ║
║  ├─ INTERPRETATION                                                     ║
║  │  ├─ 1 = perfect match (identical)                                  ║
║  │  ├─ 0 = orthogonal (maximally different)                           ║
║  │  ├─ NEVER negative or >1                                           ║
║  │  └─ Symmetric: F(ρ,σ) = F(σ,ρ)                                     ║
║  └─ EXAM TIP: Match function to type (state vs process)               ║
║                                                                        ║
║  🔄 QUANTUM CHANNELS (Noise Models)                                    ║
║  ├─ REPRESENTATIONS (all equivalent)                                  ║
║  │  ├─ Kraus: E(ρ) = Σᵢ Kᵢ ρ Kᵢ† (physical)                           ║
║  │  ├─ SuperOp: vectorized matrix (mathematical)                      ║
║  │  └─ Choi: Choi-Jamiołkowski isomorphism (tomography)               ║
║  ├─ PROPERTIES                                                         ║
║  │  ├─ Completely positive (CP)                                       ║
║  │  ├─ Trace-preserving (TP)                                          ║
║  │  └─ Kraus completeness: Σᵢ Kᵢ†Kᵢ = I                               ║
║  ├─ COMMON CHANNELS                                                    ║
║  │  ├─ Depolarizing: ρ → (1-p)ρ + p·I/d                               ║
║  │  ├─ Amplitude damping: energy loss (T1)                            ║
║  │  ├─ Phase damping: dephasing (T2)                                  ║
║  │  └─ Pauli channel: X, Y, Z errors                                  ║
║  └─ CODE: from qiskit.quantum_info import Kraus, SuperOp, Choi        ║
║                                                                        ║
║  🎲 RANDOMIZED BENCHMARKING (RB)                                       ║
║  ├─ PURPOSE: Gate error characterization                              ║
║  │  ├─ Measures average gate fidelity                                 ║
║  │  ├─ SPAM-free (no state prep/measurement errors)                   ║
║  │  └─ "RB = Really 'Bout Gates"                                      ║
║  ├─ PROTOCOL                                                           ║
║  │  ├─ Apply random Clifford sequences                                ║
║  │  ├─ Vary sequence length                                           ║
║  │  ├─ Measure decay of fidelity                                      ║
║  │  └─ Extract error per Clifford (EPC)                               ║
║  ├─ VARIANTS                                                           ║
║  │  ├─ Standard RB: average over all gates                            ║
║  │  ├─ Interleaved RB: measure specific gate                          ║
║  │  └─ Simultaneous RB: measure cross-talk                            ║
║  └─ LIMITATIONS                                                        ║
║     ├─ Assumes Markovian errors                                       ║
║     ├─ Assumes time-independent errors                                ║
║     └─ Standard RB uses only Clifford gates                           ║
║                                                                        ║
║  🔍 ADVANCED OPERATIONS                                                ║
║  ├─ PARTIAL TRACE                                                      ║
║  │  ├─ reduced = partial_trace(dm, [0,1])  # Trace OUT qubits 0,1     ║
║  │  ├─ Returns DensityMatrix of remaining qubits                      ║
║  │  ├─ Pure entangled → mixed reduced state                           ║
║  │  └─ Preserves total probability: Tr(reduced) = 1                   ║
║  ├─ ENTROPY                                                            ║
║  │  ├─ S = entropy(dm)  # von Neumann entropy                         ║
║  │  ├─ S(ρ) = -Tr(ρ log ρ)                                            ║
║  │  ├─ S = 0 for pure states                                          ║
║  │  └─ S > 0 for mixed states                                         ║
║  └─ ENTANGLEMENT MEASURES                                              ║
║     ├─ concurrence(state)  # 2-qubit only                             ║
║     ├─ Range [0,1]: 0=separable, 1=max entangled                      ║
║     └─ Use for Bell states, Werner states                             ║
║                                                                        ║
║  ⚠️ TOP 15 EXAM TRAPS (MEMORIZE!)                                      ║
║  ┌────────────────────────────────────────────────────────────────┐   ║
║  │ CLIFFORD GATE TRAPS                                            │   ║
║  │ 1. T gate is NOT Clifford (only HSCP)                          │   ║
║  │    ✗ Clifford + T gate                                         │   ║
║  │    ✓ Clifford gates: H, S, CNOT, Pauli only                    │   ║
║  │ 2. Clifford(circuit) raises error if non-Clifford gates        │   ║
║  │    ✗ Clifford(circuit_with_T_gate)                             │   ║
║  │    ✓ Check gates before creating Clifford                      │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ OPERATOR COMPARISON TRAPS                                      │   ║
║  │ 3. Use .equiv() not == for operator comparison                 │   ║
║  │    ✗ op1 == op2  # Phase matters                               │   ║
║  │    ✓ op1.equiv(op2)  # Phase-invariant                         │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ COMPOSITION ORDER TRAPS                                        │   ║
║  │ 4. compose() order: op1.compose(op2) applies op2 FIRST         │   ║
║  │    Think: right-to-left like matrix multiplication             │   ║
║  │    op1.compose(op2) = op1 ∘ op2 = op1(op2(...))                │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ FIDELITY RANGE TRAPS                                           │   ║
║  │ 5. Fidelity ALWAYS in [0, 1] (never negative or >1)            │   ║
║  │    1 = perfect match, 0 = orthogonal                           │   ║
║  │    Minimum is 0, not -1                                        │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ PURE VS MIXED STATE TRAPS                                      │   ║
║  │ 6. Superposition ≠ mixed state                                 │   ║
║  │    |+⟩ is PURE state (purity = 1)                              │   ║
║  │    Mixed requires classical uncertainty                        │   ║
║  │ 7. Statevector for pure only, DensityMatrix for pure+mixed     │   ║
║  │    ✗ Statevector(mixed_state)  # Cannot represent              │   ║
║  │    ✓ DensityMatrix handles both pure and mixed                 │   ║
║  │ 8. Entangled states are pure (not mixed)                       │   ║
║  │    Bell states: maximally entangled AND pure                   │   ║
║  │    Purity = 1 for pure entangled states                        │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ PURITY TRAPS                                                   │   ║
║  │ 9. Purity range: [1/d, 1] where d = dimension                  │   ║
║  │    purity = 1: pure state                                      │   ║
║  │    purity < 1: mixed state                                     │   ║
║  │    Minimum purity = 1/d (maximally mixed)                      │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ FIDELITY FUNCTION TRAPS                                        │   ║
║  │ 10. Use correct fidelity function for data type                │   ║
║  │     state_fidelity() for Statevector/DensityMatrix             │   ║
║  │     process_fidelity() for Operator/Channel                    │   ║
║  │     average_gate_fidelity() for gate quality                   │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ RANDOMIZED BENCHMARKING TRAPS                                  │   ║
║  │ 11. RB is SPAM-free (only measures gate errors)                │   ║
║  │     Does NOT measure state prep or measurement errors          │   ║
║  │     "RB = Really 'Bout Gates"                                  │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ PARTIAL TRACE TRAPS                                            │   ║
║  │ 12. partial_trace(dm, [0,1]) traces OUT qubits 0,1             │   ║
║  │     Returns density matrix of REMAINING qubits                 │   ║
║  │     Pure entangled state → mixed reduced state                 │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ NORMALIZATION TRAPS                                            │   ║
║  │ 13. Statevector: Σ |αᵢ|² = 1 (amplitudes squared)              │   ║
║  │     DensityMatrix: Tr(ρ) = 1 (trace = 1)                       │   ║
║  │     Both must be normalized                                    │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ ENTROPY TRAPS                                                  │   ║
║  │ 14. Entropy S(ρ) = 0 only for pure states                      │   ║
║  │     S > 0 for mixed states                                     │   ║
║  │     Maximally mixed → maximum entropy                          │   ║
║  ├────────────────────────────────────────────────────────────────┤   ║
║  │ CONCURRENCE TRAPS                                              │   ║
║  │ 15. concurrence() only for 2-qubit states                      │   ║
║  │     ✗ concurrence(3_qubit_state)  # Error!                     │   ║
║  │     ✓ Use for Bell states, 2-qubit systems only                │   ║
║  └────────────────────────────────────────────────────────────────┘   ║
║                                                                        ║
║  💡 QUICK REFERENCE CHEATSHEET                                         ║
║  ├─ Import: from qiskit.quantum_info import Clifford, Operator, ...   ║
║  ├─ Clifford check: "HSCP - No T!" (H, S, CNOT, Pauli)                ║
║  ├─ Operator compare: use .equiv() not ==                             ║
║  ├─ Compose order: op1.compose(op2) applies op2 first                 ║
║  ├─ Fidelity range: always [0, 1], never outside                      ║
║  ├─ Pure check: purity = 1 or Tr(ρ²) = 1                              ║
║  ├─ State type: SV for pure only, DM for pure+mixed                   ║
║  └─ Partial trace: traces OUT specified qubits                        ║
║                                                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
```
