# 20-Month Quantum Computing Curriculum
## Comprehensive Teaching Plan for Maximum Retention

**Source Material:** QCFundamentals (Parts 1–5) · QC Algorithms (Parts 1–5)  
**Design Principles:** Spaced repetition · Progressive complexity · Theory/Lab interleaving · Active recall projects

---

## Curriculum Architecture

| Phase | Months | Theme |
|-------|--------|-------|
| **Phase I: Foundations** | 1–4 | Mathematical prerequisites + quantum mechanics postulates |
| **Phase II: Closed Systems** | 5–8 | Qubits, gates, entanglement, measurement |
| **Phase III: Open Systems & Errors** | 9–10 | Decoherence, noise, error correction |
| **Phase IV: Classical Algorithms → Quantum** | 11–14 | Oracle algorithms, QFT, phase estimation |
| **Phase V: Cryptographic & Search Algorithms** | 15–16 | Shor's & Grover's |
| **Phase VI: Variational & Near-Term** | 17–18 | VQE, QAOA, NISQ devices |
| **Phase VII: Advanced & Emerging** | 19–20 | HHL, QML, adiabatic computing, capstone |

---

## Month 1 — Why Quantum Computing? Philosophy & Mathematical Toolkit I

### Learning Goals
- Understand the philosophical motivation for quantum computing
- Build comfort with complex numbers, linear algebra notation
- Understand the limits of classical computation

### Topics
1. **Course Philosophy & Framing**
   - Deutsch's principle: *"Computers are physical objects; computation is a physical process"*
   - Feynman's insight: simulating nature requires quantum mechanics
   - Four central questions of quantum mechanics (preview)

2. **Classical Computing Limits**
   - Turing machines and computational complexity
   - Why classical simulation of quantum systems scales exponentially
   - Moore's Law and physical limits

3. **Mathematical Toolkit: Complex Numbers**
   - Complex numbers: Cartesian and polar forms
   - Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$
   - Complex conjugates, modulus, argument
   - Complex arithmetic and geometric interpretation

4. **Mathematical Toolkit: Vectors & Matrices**
   - Column and row vectors in $\mathbb{R}^n$ and $\mathbb{C}^n$
   - Matrix multiplication, transpose, conjugate transpose (Hermitian adjoint $A^\dagger$)
   - Inner products and orthonormality

### Lab / Active Recall
- Python refresher: complex number arithmetic with NumPy
- Visualize complex numbers on the Argand plane
- **Month project:** Write a 1-page reflection on *"what makes quantum computers different"*

---

## Month 2 — Mathematical Toolkit II: Linear Algebra Deep Dive

### Learning Goals
- Master the algebraic tools that underpin all of quantum mechanics
- Understand eigenvalues, eigenvectors, and spectral decomposition
- Gain fluency with Dirac notation

### Topics
1. **Dirac (Bra-Ket) Notation**
   - Ket $|\psi\rangle$: column vector in Hilbert space
   - Bra $\langle\psi|$: conjugate transpose (row vector)
   - Inner product $\langle\phi|\psi\rangle$, outer product $|\psi\rangle\langle\phi|$
   - Bra-ket sandwich and expectation values

2. **Hilbert Spaces**
   - Definition: complete inner product space over $\mathbb{C}$
   - Orthonormal bases and completeness relation $\sum_i |i\rangle\langle i| = I$
   - Separable Hilbert spaces; countable bases
   - Physical states as *rays* (global phase invariance)

3. **Linear Operators**
   - Hermitian operators: $H = H^\dagger$, real eigenvalues
   - Unitary operators: $UU^\dagger = I$, norm-preserving
   - Projection operators: $P^2 = P$, $P = P^\dagger$
   - Spectral decomposition theorem

4. **Eigenvalue Problems**
   - Characteristic equation, eigenvalue spectrum
   - Diagonalization of Hermitian operators
   - Pauli matrices $\sigma_x, \sigma_y, \sigma_z$: eigenstates and eigenvalues
   - Tensor products of vectors and matrices

5. **Trace and Determinant**
   - Trace: $\text{tr}(A) = \sum_i A_{ii}$; cyclic property
   - Partial trace for composite systems

### Lab / Active Recall
- Implement Pauli matrices and verify eigenvalues in Python
- Compute inner products and confirm orthonormality of qubit basis states
- **Month project:** Prove that unitary operators preserve inner products

---

## Month 3 — Quantum Mechanics Postulate 1: Quantum States & Superposition

### Learning Goals
- Understand the first postulate: quantum states as unit vectors in Hilbert space
- Internalize the superposition principle
- Distinguish classical vs. quantum probability

### Topics
1. **Postulate 1: State Description**
   - Closed quantum system state: unit vector $|\psi\rangle \in \mathcal{H}$ with $\langle\psi|\psi\rangle = 1$
   - Basis states for a 2-level system: $|0\rangle = \begin{pmatrix}1\\0\end{pmatrix}$, $|1\rangle = \begin{pmatrix}0\\1\end{pmatrix}$

2. **The Qubit**
   - Definition: quantum bit — 2-dimensional quantum system
   - General qubit state: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, where $|\alpha|^2 + |\beta|^2 = 1$
   - Complex amplitudes $\alpha, \beta \in \mathbb{C}$
   - Why we need *many* complex numbers to specify one quantum state (vs. one classical number)

3. **The Superposition Principle**
   - Linear combinations of valid quantum states are valid quantum states
   - Superposition is *not* ignorance — it is a physical reality
   - The ball-in-potential analogy: classical vs. quantum ensemble

4. **Multi-Qubit Systems**
   - $n$-qubit state space: $2^n$-dimensional Hilbert space
   - Tensor product: $|0\rangle \otimes |1\rangle = |01\rangle$
   - Computational basis: all $2^n$ bit strings
   - Why quantum state description scales exponentially in classical resources

5. **Global vs. Relative Phase**
   - Global phase invariance: $|\psi\rangle \equiv e^{i\phi}|\psi\rangle$
   - Relative phase: physically measurable, creates interference
   - Preview: interference is a key quantum resource

### Lab / Active Recall
- Create and normalize qubit states in Qiskit (Qiskit installation walkthrough)
- Verify $|\alpha|^2 + |\beta|^2 = 1$ for random normalized states
- **Month project:** Build a quiz on superposition vs. classical mixture for peer review

---

## Month 4 — Postulate 2: Quantum Evolution (Unitary Dynamics)

### Learning Goals
- Understand Schrödinger's equation as the generator of quantum evolution
- Identify which transformations are allowed on quantum states
- Connect Hamiltonians to physical systems (spin in a field)

### Topics
1. **Postulate 2: Time Evolution**
   - Closed system evolution: $i\hbar \frac{d|\psi\rangle}{dt} = H|\psi\rangle$
   - Solution: $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$
   - The time-evolution operator $U(t) = e^{-iHt/\hbar}$ is unitary

2. **Why Unitarity?**
   - Unitarity preserves probability: $\langle\psi(t)|\psi(t)\rangle = 1$ for all $t$
   - Reversibility: $U^{-1} = U^\dagger$ — quantum evolution is reversible
   - Contrast with classical irreversible computation

3. **The Hamiltonian as Energy Operator**
   - $H$ is Hermitian: real eigenvalues (energies)
   - Energy eigenstates: $H|E_n\rangle = E_n|E_n\rangle$
   - Energy eigenstates evolve by picking up a phase only

4. **Physical Example: Spin in a Magnetic Field**
   - Hamiltonian: $H = -\frac{\hbar\omega}{2}\vec{\sigma}\cdot\hat{n}$
   - Larmor precession: spin precesses around magnetic field axis
   - Rabi oscillations: oscillation between $|0\rangle$ and $|1\rangle$ under resonant drive
   - Physical qubit realization preview

5. **Matrix Exponentials**
   - $e^{i\theta\hat{n}\cdot\vec{\sigma}} = \cos\theta I + i\sin\theta(\hat{n}\cdot\vec{\sigma})$
   - Computing rotation operators from Hamiltonians

### Lab / Active Recall
- Simulate Larmor precession numerically
- Verify unitarity: confirm $UU^\dagger = I$ for computed evolution operators
- **Month project:** Derive the time evolution for a spin-1/2 particle; plot the state on the Bloch sphere over time

---

## Month 5 — The Bloch Sphere & Single-Qubit Geometry

### Learning Goals
- Visualize all single-qubit states using the Bloch sphere
- Understand every unitary single-qubit operation as a rotation
- Build geometric intuition for quantum gates

### Topics
1. **Bloch Sphere Representation**
   - Parameterization: $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$
   - Polar angle $\theta \in [0,\pi]$, azimuthal angle $\phi \in [0,2\pi)$
   - North/south poles: $|0\rangle$, $|1\rangle$; equator: equal-superposition states
   - Why the sphere is a sphere (not a circle)

2. **Key Equatorial States**
   - $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$, $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ along $x$
   - $|i\rangle = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$, $|-i\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$ along $y$

3. **Rotations on the Bloch Sphere**
   - $R_x(\theta) = e^{-i\theta\sigma_x/2}$: rotation around $x$-axis
   - $R_y(\theta) = e^{-i\theta\sigma_y/2}$: rotation around $y$-axis
   - $R_z(\theta) = e^{-i\theta\sigma_z/2}$: rotation around $z$-axis
   - Euler angle decomposition: any $SU(2)$ rotation = $R_z(\alpha)R_y(\beta)R_z(\gamma)$

4. **Named Single-Qubit Gates**
   - Hadamard gate $H$: maps poles to equator ($|0\rangle \to |+\rangle$)
   - Pauli $X$, $Y$, $Z$: $\pi$-rotations around respective axes
   - $S$ gate (Phase): $\pi/2$ rotation around $z$
   - $T$ gate: $\pi/4$ rotation around $z$

5. **Bloch Vector for Mixed States (preview)**
   - Pure state: Bloch vector on the surface of the sphere ($r = 1$)
   - Mixed state: Bloch vector inside the sphere ($r < 1$) — motivation for Part 2

### Lab / Active Recall
- Implement Bloch sphere visualizations using Qiskit's `plot_bloch_vector`
- Apply each named gate and observe the rotation on the Bloch sphere
- **Month project:** Decompose an arbitrary single-qubit unitary into $R_z R_y R_z$ and verify numerically

---

## Month 6 — Multi-Qubit States, Entanglement & Bell States

### Learning Goals
- Understand entanglement as the defining non-classical resource
- Analyze Bell states and their properties
- Apply the CHSH inequality to understand non-locality

### Topics
1. **Composite Quantum Systems (Postulate 4)**
   - Tensor product of Hilbert spaces: $\mathcal{H}_A \otimes \mathcal{H}_B$
   - Product states: $|\psi\rangle_A \otimes |\phi\rangle_B$
   - Entangled states: not expressible as a product state

2. **Entanglement — Definition & Intuition**
   - Schmidt decomposition: $|\psi\rangle = \sum_k \lambda_k |a_k\rangle|b_k\rangle$
   - Schmidt rank: 1 = separable, >1 = entangled
   - Entanglement as correlation beyond classical correlations
   - EPR paradox: Einstein's "spooky action at a distance"

3. **Bell States**
   - $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
   - $|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$
   - $|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$
   - $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$
   - Bell states as maximally entangled states
   - Circuit to prepare Bell states: $H \otimes I$ followed by $\text{CNOT}$

4. **CHSH Inequality**
   - Local hidden variable theories and Bell's theorem
   - CHSH game: cooperative game without communication
   - Classical bound: $\langle\text{CHSH}\rangle \leq 2$
   - Quantum bound (Tsirelson): $\langle\text{CHSH}\rangle \leq 2\sqrt{2}$
   - Experimental violation → quantum mechanics is non-local

5. **Multi-Qubit Gates**
   - CNOT gate: controlled-NOT, creates entanglement
   - SWAP gate
   - Toffoli (CCNOT): universal for classical computation
   - General controlled-$U$ gates

### Lab / Active Recall
- Prepare all four Bell states in Qiskit and verify by simulation
- Run a Bell state preparation on IBM quantum hardware and analyze noise effects
- **Month project:** Implement the CHSH game in Qiskit; measure the quantum advantage

---

## Month 7 — Postulate 3: Measurement & The Born Rule

### Learning Goals
- Understand how information is extracted from quantum systems
- Apply the Born rule correctly in diverse measurement settings
- Understand projective measurements, POVMs, and expectation values

### Topics
1. **Postulate 3: Measurement (Projective)**
   - Observable $M$: Hermitian operator with spectral decomposition $M = \sum_m m P_m$
   - Born rule: probability of outcome $m$ is $p(m) = \langle\psi|P_m|\psi\rangle$
   - Post-measurement state: $|\psi'\rangle = P_m|\psi\rangle / \sqrt{p(m)}$
   - Measurement is irreversible — collapses the superposition

2. **Computational Basis Measurement**
   - Measuring in the $\{|0\rangle, |1\rangle\}$ basis
   - For $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$: $P(0) = |\alpha|^2$, $P(1) = |\beta|^2$
   - Measuring an $n$-qubit system: $2^n$ possible outcomes
   - Statistical nature: need many shots to estimate probabilities

3. **Expectation Values**
   - $\langle M\rangle = \langle\psi|M|\psi\rangle$
   - Variance: $\Delta M^2 = \langle M^2\rangle - \langle M\rangle^2$
   - Heisenberg uncertainty principle: $\Delta A \cdot \Delta B \geq \frac{1}{2}|\langle[A,B]\rangle|$

4. **Measuring in Arbitrary Bases**
   - Change of basis before measurement
   - Hadamard before measurement = measuring in $\{|+\rangle, |-\rangle\}$ basis
   - Basis choice determines what information is extracted

5. **Generalized Measurements (POVMs)**
   - Positive operator-valued measures: $\{E_m\}$, $E_m \geq 0$, $\sum_m E_m = I$
   - More general than projective measurements; relevant for quantum information

6. **No-Cloning Theorem (First Encounter)**
   - Cannot copy an arbitrary unknown quantum state
   - Proof by contradiction using linearity
   - Why this is important for quantum cryptography

### Lab / Active Recall
- Simulate measurements in Qiskit; plot histograms for various states
- Verify Born rule probabilities match analytical predictions
- **Month project:** Demonstrate the no-cloning theorem with a proof and a failed circuit attempt

---

## Month 8 — Quantum Teleportation & No-Cloning Deep Dive

### Learning Goals
- Understand how entanglement enables quantum teleportation
- Connect postulates 1–4 in a complete protocol
- Appreciate limitations imposed by the no-cloning theorem

### Topics
1. **No-Cloning Theorem (Complete Treatment)**
   - Full formal proof
   - Implications: quantum information cannot be copied
   - No-deleting theorem (dual)
   - Contrast: classical bits can always be copied

2. **Quantum Teleportation Protocol**
   - Resource: shared Bell pair between Alice and Bob
   - Step 1: Alice performs a Bell-basis measurement on her qubit + the qubit to teleport
   - Step 2: Alice sends 2 classical bits to Bob
   - Step 3: Bob applies conditional corrections ($X$ and/or $Z$)
   - The qubit state is transferred, not the qubit itself
   - No faster-than-light signaling (classical channel required)

3. **Teleportation Circuit Analysis**
   - Circuit decomposition: Bell preparation, Bell measurement, corrections
   - Verifying the protocol works for all four Bell measurement outcomes
   - Resource count: 1 ebit + 2 classical bits = 1 qubit teleported

4. **Superdense Coding (Dual Protocol)**
   - Using 1 shared Bell pair + 1 qubit transmission to send 2 classical bits
   - Circuit construction and verification
   - Holevo bound and quantum channel capacity context

5. **Spooky Action & Causality**
   - Why teleportation does not violate causality
   - No-communication theorem
   - The role of the classical channel

### Lab / Active Recall
- Implement full quantum teleportation protocol in Qiskit
- Run on IBM quantum hardware and analyze fidelity vs. simulator
- **Month project:** Implement superdense coding and write a comparison of teleportation vs. superdense coding

---

## Month 9 — Open Quantum Systems I: Density Matrices

### Learning Goals
- Extend quantum state description to mixed states and open systems
- Master the density matrix formalism
- Distinguish pure from mixed states

### Topics
1. **Motivation: Why Open Systems?**
   - Real quantum computers interact with environment (thermal bath, EM fields)
   - Environmental interaction destroys quantum resources
   - Cannot describe a subsystem of an entangled state by a ket vector alone

2. **Quantum Ensembles**
   - Ensemble: set of states $\{|\psi_j\rangle\}$ with probabilities $\{p_j\}$
   - Two types of probability: quantum (intrinsic) vs. classical (ignorance)
   - The density matrix unifies both

3. **Density Matrix Formalism**
   - Definition: $\rho = \sum_j p_j |\psi_j\rangle\langle\psi_j|$
   - Properties: Hermitian, positive semi-definite, unit trace ($\text{tr}(\rho) = 1$)
   - Pure state: $\rho = |\psi\rangle\langle\psi|$, $\rho^2 = \rho$, $\text{tr}(\rho^2) = 1$
   - Mixed state: $\rho = \sum_j p_j |\psi_j\rangle\langle\psi_j|$, $\text{tr}(\rho^2) < 1$

4. **Bloch Vector Revisited**
   - Single-qubit density matrix: $\rho = \frac{1}{2}(I + \vec{r}\cdot\vec{\sigma})$, $|\vec{r}| \leq 1$
   - Pure state: $|\vec{r}| = 1$ (on sphere surface)
   - Mixed state: $|\vec{r}| < 1$ (inside sphere)
   - Maximally mixed state: $\rho = I/2$, $\vec{r} = 0$ (center of sphere)

5. **Measurement in Density Matrix Formalism**
   - Born rule: $p(m) = \text{tr}(P_m \rho)$
   - Post-measurement state: $\rho' = P_m \rho P_m / \text{tr}(P_m \rho)$
   - Expectation value: $\langle M\rangle = \text{tr}(M\rho)$

6. **Reduced Density Matrix & Partial Trace**
   - System $AB$ in state $\rho_{AB}$
   - Reduced state: $\rho_A = \text{tr}_B(\rho_{AB})$
   - Entanglement and mixed reduced states: maximally entangled → maximally mixed subsystem

### Lab / Active Recall
- Compute density matrices for various ensembles in Python
- Verify purity $\text{tr}(\rho^2)$ for pure vs. mixed states
- **Month project:** Show that tracing out half of a Bell state gives the maximally mixed state

---

## Month 10 — Open Quantum Systems II: Quantum Channels & Decoherence

### Learning Goals
- Understand the most general quantum evolution (CPTP maps)
- Model all physically relevant noise channels
- Quantify how decoherence destroys quantum information

### Topics
1. **Postulate 2 Revisited for Open Systems**
   - Unitary evolution of the closed universe: $U$ on system + environment
   - Open system evolution: non-unitary map $\mathcal{E}(\rho)$
   - Requirements: trace-preserving, completely positive (CPTP)

2. **Kraus Operator Representation**
   - Operator-sum representation: $\mathcal{E}(\rho) = \sum_k K_k \rho K_k^\dagger$
   - Completeness: $\sum_k K_k^\dagger K_k = I$
   - Interpretation: $K_k$ is the operation that occurs with probability $\text{tr}(K_k\rho K_k^\dagger)$

3. **Standard Noise Channels**
   - **Bit-flip channel**: $\mathcal{E}(\rho) = (1-p)\rho + p X\rho X^\dagger$
   - **Phase-flip channel**: $\mathcal{E}(\rho) = (1-p)\rho + p Z\rho Z^\dagger$
   - **Depolarizing channel**: $\mathcal{E}(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$
   - **Amplitude damping**: $K_0 = \begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix}$, $K_1 = \begin{pmatrix}0&\sqrt{\gamma}\\0&0\end{pmatrix}$; models energy relaxation ($T_1$)
   - **Phase damping (dephasing)**: models loss of phase coherence ($T_2$)

4. **Decoherence**
   - Definition: decay of off-diagonal elements of $\rho$ in the computational basis
   - $T_1$: energy relaxation time (amplitude damping)
   - $T_2$: dephasing time ($T_2 \leq 2T_1$)
   - Physical causes: coupling to phonons, photons, charge noise, flux noise
   - Decoherence as the primary obstacle to scalable quantum computing

5. **Lindblad Master Equation**
   - Continuous-time Markovian evolution: $\dot\rho = -\frac{i}{\hbar}[H,\rho] + \sum_k \gamma_k(L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k,\rho\})$
   - Lindblad operators $L_k$: jump operators modeling environment couplings
   - Steady state and relaxation dynamics

### Lab / Active Recall
- Implement all noise channels as Kraus operators; plot Bloch vector decay
- Simulate $T_1$ and $T_2$ decay using Qiskit Aer noise models
- **Month project:** Measure the effect of each noise channel on a prepared Bell state; compute fidelity vs. noise rate

---

## Month 11 — Quantum Circuits & Universal Gate-Based Computing

### Learning Goals
- Map quantum postulates onto the circuit model of computation
- Understand universality and what gates are needed
- Build intuition for circuit depth, width, and complexity

### Topics
1. **Quantum Circuit Model**
   - Circuit diagram conventions: wires = qubits, gates = unitaries, dials = measurements
   - Time flows left to right
   - No fanout (no-cloning), no loops (unitary)
   - Classical control wires for conditional operations

2. **Single-Qubit Gates (Comprehensive)**
   - $I$, $X$, $Y$, $Z$ (Pauli group)
   - $H$ (Hadamard), $S$, $T$, $R_z(\theta)$, $R_y(\theta)$, $R_x(\theta)$
   - Relationship between gates and Bloch sphere rotations (revisited with circuit context)
   - Matrix representations and circuit symbols

3. **Two-Qubit Gates**
   - $\text{CNOT}$: the primary entangling gate
   - $\text{CZ}$, $\text{SWAP}$, $\text{iSWAP}$
   - Controlled-$U$ gates: general construction
   - $\text{Toffoli}$ (CCNOT): 3-qubit universal classical gate

4. **Universality**
   - Classical universality: NAND gate
   - Quantum universality: $\{H, T, \text{CNOT}\}$ is universal
   - Solovay-Kitaev theorem: approximating any unitary to precision $\epsilon$ in $O(\log^c(1/\epsilon))$ gates
   - Why $T$ is the "expensive" gate (resource for fault tolerance)

5. **Circuit Identities & Optimization**
   - Common circuit identities: $H X H = Z$, $H Z H = X$, etc.
   - Gate cancellation and commutation rules
   - Clifford + T decomposition
   - Circuit depth vs. gate count trade-offs

6. **Why Build a Quantum Computer?**
   - Quantum advantage hierarchy: Shor, Grover, VQE, QML
   - Complexity theory: BQP, NP, and quantum speedup regimes

### Lab / Active Recall
- Build circuits for all named gates in Qiskit; verify with statevector simulator
- Decompose a random single-qubit unitary into $\{H, T, S, \text{CNOT}\}$
- **Month project:** Prove that $\{H, T, \text{CNOT}\}$ can approximate any single-qubit unitary; demonstrate numerically

---

## Month 12 — Quantum Error Correction Basics

### Learning Goals
- Understand why quantum error correction is fundamentally different from classical
- Implement the 3-qubit and Shor codes
- Understand the threshold theorem

### Topics
1. **Why QEC is Hard**
   - Continuous error space (vs. discrete classical bit errors)
   - Measurement disturbs state (no-cloning prevents redundancy)
   - Decoherence acts continuously
   - Key insight: measuring *syndromes* (not the state) allows error identification

2. **Classical Repetition Code (Review)**
   - 3-bit repetition: $0 \to 000$, $1 \to 111$
   - Majority vote correction
   - Fails against quantum errors

3. **3-Qubit Bit-Flip Code**
   - Encoding: $|0\rangle \to |000\rangle$, $|1\rangle \to |111\rangle$
   - Syndrome measurement: $Z_1Z_2$, $Z_2Z_3$ parity checks
   - Correction without measuring the logical qubit
   - Handles single bit-flip errors only

4. **3-Qubit Phase-Flip Code**
   - Encoding in Hadamard basis: $|+\rangle^{\otimes 3}$, $|-\rangle^{\otimes 3}$
   - Syndrome measurement in $X$ basis
   - Handles single phase-flip errors only

5. **Shor's 9-Qubit Code**
   - Concatenates bit-flip and phase-flip codes
   - Encoding circuit and stabilizers
   - Corrects any single-qubit error (bit-flip, phase-flip, or both)
   - First quantum error-correcting code

6. **Stabilizer Formalism (Introduction)**
   - Stabilizer states: defined by a set of commuting Pauli operators
   - Logical operators: $\bar{X}$, $\bar{Z}$ acting on the logical qubit
   - Syndrome measurement = measuring stabilizers
   - Cayley table of the Pauli group

7. **Fault Tolerance Threshold Theorem**
   - If physical error rate $p < p_{\text{th}}$, scalable fault-tolerant QC is possible
   - Typical threshold: $p_{\text{th}} \sim 10^{-2}$ to $10^{-3}$
   - Current hardware: $p \sim 10^{-2}$ — near but not below threshold

### Lab / Active Recall
- Implement 3-qubit bit-flip code in Qiskit; inject errors and verify correction
- Implement Shor's 9-qubit code; verify correction for $X$, $Z$, $Y$ errors
- **Month project:** Determine the minimum number of ancilla qubits needed for syndrome extraction; design the circuit

---

## Month 13 — Surface Codes & Modern Error Correction

### Learning Goals
- Understand surface codes as the leading candidate for fault-tolerant QC
- Connect stabilizer formalism to topological codes
- Appreciate the engineering challenges of physical error correction

### Topics
1. **Motivation: Why Not Just Scale Shor's Code?**
   - Overhead of Shor's code is high
   - We need codes with high threshold and low overhead

2. **Stabilizer Codes (Deep Dive)**
   - $[[n, k, d]]$ notation: $n$ physical qubits, $k$ logical qubits, distance $d$
   - Distance $d$: minimum number of single-qubit errors to cause logical error
   - Error correction capability: corrects up to $\lfloor(d-1)/2\rfloor$ errors

3. **Toric Code (Kitaev)**
   - Qubits on edges of a torus lattice
   - Vertex stabilizers (star operators): $A_v = \prod_{e\in v} X_e$
   - Plaquette stabilizers (plaquette operators): $B_p = \prod_{e\in p} Z_e$
   - Anyonic excitations as error syndromes
   - Logical operators as non-contractible loops

4. **Surface Code (Planar Version)**
   - Physical realization: 2D grid of qubits + ancilla qubits
   - Data qubits and syndrome qubits
   - $X$-type and $Z$-type stabilizer checks
   - Threshold: ~1% (much higher than Shor's code)
   - Resource overhead: ~1000 physical qubits per logical qubit for useful computation

5. **Decoding Algorithms**
   - Minimum weight perfect matching (MWPM)
   - Logical error rate vs. code distance
   - The ladder toward fault-tolerant quantum computing

6. **Hardware Requirements for Fault Tolerance**
   - Qubit count needed for useful algorithms post-error-correction
   - Current state (2024): ~1000 qubits, but need ~1M physical for Shor's at scale
   - The road from NISQ to fault-tolerant

### Lab / Active Recall
- Implement a small surface code ($d=3$) in Qiskit using the Qiskit QEC library
- Visualize syndrome measurement and MWPM decoding
- **Month project:** Research paper summary: "Google's below-threshold surface code (2023)"

---

## Month 14 — Introduction to Quantum Algorithms & Qiskit

### Learning Goals
- Set up the full quantum algorithm development environment
- Understand the oracle model and query complexity
- Implement the Deutsch-Jozsa and Bernstein-Vazirani algorithms

### Topics
1. **Qiskit Environment Setup**
   - IBM Quantum account setup and IBM Quantum Lab
   - Qiskit Terra (circuit building), Aer (simulation), IBMQ (hardware access)
   - Running on local simulators vs. real hardware
   - Understanding shot noise and hardware noise

2. **The Oracle (Black Box) Model**
   - Function $f: \{0,1\}^n \to \{0,1\}$
   - Oracle as a quantum gate: $U_f|x\rangle|y\rangle = |x\rangle|y \oplus f(x)\rangle$
   - Phase kickback trick: $U_f|x\rangle|-\rangle = (-1)^{f(x)}|x\rangle|-\rangle$
   - Query complexity: how many oracle calls to solve a problem

3. **Deutsch Problem (1-bit warm-up)**
   - Problem: is $f(0) = f(1)$ (constant) or not (balanced)?
   - Classical: 2 queries needed
   - Quantum: 1 query (Deutsch algorithm)
   - Circuit: $H \to U_f \to H \to$ measure

4. **Deutsch-Jozsa Algorithm**
   - $n$-bit generalization: constant vs. balanced function on $\{0,1\}^n$
   - Classical (deterministic): up to $2^{n-1}+1$ queries
   - Quantum: exactly 1 query
   - Circuit: $H^{\otimes n}|0\rangle^n \otimes H|1\rangle \to U_f \to H^{\otimes n} \to$ measure
   - Analysis: interference cancels all non-$|0\rangle^n$ amplitudes iff $f$ is constant

5. **Bernstein-Vazirani Algorithm**
   - Problem: find a hidden bit string $s$ from the linear function $f(x) = s \cdot x \pmod 2$
   - Classical: $n$ queries
   - Quantum: 1 query (same circuit as Deutsch-Jozsa!)
   - Shows that quantum mechanics can learn global properties of functions

6. **Key Insight: Interference as Computation**
   - Constructive interference on the answer
   - Destructive interference on all wrong answers
   - Hadamard transform creates and applies interference

### Lab / Active Recall
- Implement Deutsch-Jozsa for $n = 1, 2, 3, 4$ in Qiskit
- Run Bernstein-Vazirani on IBM quantum hardware; verify recovered $s$
- **Month project:** Prove mathematically that Deutsch-Jozsa requires exactly 1 quantum query for any $n$

---

## Month 15 — Simon's Algorithm & Quantum Fourier Transform

### Learning Goals
- Understand the first algorithm with exponential quantum speedup (Simon's)
- Master the Quantum Fourier Transform as a fundamental subroutine
- Implement QFT efficiently in Qiskit

### Topics
1. **Simon's Algorithm**
   - Problem: find hidden period $s$ where $f(x) = f(x \oplus s)$
   - Classical: exponential queries ($\Omega(2^{n/2})$)
   - Quantum: polynomial queries ($O(n)$ with classical post-processing)
   - Circuit: two $H^{\otimes n}$ layers + oracle + linear algebra post-processing
   - Why it works: interference picks out vectors orthogonal to $s$
   - Historical significance: first proof of exponential separation (before Shor!)

2. **Discrete Fourier Transform (Review)**
   - DFT: $\tilde{f}_k = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} e^{2\pi ijk/N} f_j$
   - Periodicity detection: DFT peaks at integer multiples of $N/T$ for period-$T$ function
   - Classical FFT: $O(N\log N)$ operations on $N$ amplitudes

3. **Quantum Fourier Transform**
   - QFT acts on computational basis: $|j\rangle \mapsto \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} e^{2\pi ijk/N}|k\rangle$
   - Efficient circuit: $O(n^2)$ gates for $n$-qubit QFT (vs. $O(n 2^n)$ classical)
   - Building blocks: Hadamard + controlled phase gates $R_k$
   - Circuit diagram: $n$-qubit QFT decomposition
   - Swap network to reverse qubit order at the end

4. **QFT Circuit Construction**
   - Stage 1: apply $H$ and $R_k$ gates qubit by qubit
   - Stage 2: reverse order with SWAP gates
   - Approximate QFT: dropping small-angle rotations
   - Inverse QFT: same circuit in reverse

5. **Hadamard Transform vs. QFT**
   - $H^{\otimes n}$: implements QFT mod 2 (Hadamard transform)
   - QFT: implements DFT for general moduli $N = 2^n$
   - Relationship to Simon's algorithm (Hadamard = QFT over $\mathbb{Z}_2^n$)

### Lab / Active Recall
- Implement Simon's algorithm in Qiskit for several hidden strings $s$
- Implement $n$-qubit QFT from scratch; verify it matches the DFT matrix
- **Month project:** Apply QFT to a known periodic function; recover the period from measurement statistics

---

## Month 16 — Quantum Phase Estimation & Shor's Algorithm

### Learning Goals
- Understand quantum phase estimation as a universal subroutine
- Derive and implement Shor's factoring algorithm
- Analyze the quantum advantage in number theory

### Topics
1. **Quantum Phase Estimation (QPE)**
   - Problem: given unitary $U$ and eigenstate $|\psi\rangle$, estimate phase $\phi$ where $U|\psi\rangle = e^{2\pi i\phi}|\psi\rangle$
   - Circuit: QFT register + controlled-$U^{2^k}$ applications
   - Output: $t$-bit binary approximation to $\phi$
   - Precision: $t$ bits → $|\phi_{\text{est}} - \phi| \leq 2^{-t}$
   - Success probability analysis

2. **QPE Circuit Architecture**
   - Phase kickback from eigenstates
   - Controlled-$U^{2^k}$ gates: power-of-two repetitions
   - Inverse QFT to decode the phase
   - Resource count: $t$ ancilla qubits for $t$-bit precision

3. **Order Finding Problem**
   - Classical: find smallest $r$ such that $a^r \equiv 1 \pmod{N}$
   - Reduction to factoring (number theory)
   - Connection to QPE: $f(x) = a^x \bmod N$ has period $r$

4. **Shor's Algorithm**
   - Reduction: factoring $N$ → order finding → phase estimation
   - Step 1: check for trivial factors
   - Step 2: pick random $a$, compute $\gcd(a, N)$
   - Step 3: quantum order finding using QPE
   - Step 4: classical post-processing to extract factors
   - Runtime: $O((\log N)^3)$ quantum gates — exponentially faster than classical

5. **Classical Complexity Context**
   - Best classical: General Number Field Sieve, sub-exponential $O(e^{(\log N)^{1/3}})$
   - Shor's: polynomial in $\log N$
   - Implication for RSA cryptography and post-quantum cryptography
   - NIST post-quantum standards (Kyber, Dilithium)

6. **Shor's Algorithm Lab**
   - Implement for small $N$ (e.g., $N = 15$, $N = 21$) in Qiskit
   - Quantum circuit for modular exponentiation
   - Run on simulator; analyze success probability

### Lab / Active Recall
- Implement QPE for a known unitary; recover the phase
- Run Shor's algorithm for $N = 15$ in Qiskit; verify factors
- **Month project:** Research and present: "Why does Shor's algorithm break RSA?" Connect to post-quantum cryptography

---

## Month 17 — Grover's Search Algorithm & Amplitude Amplification

### Learning Goals
- Understand Grover's algorithm and its quadratic speedup for unstructured search
- Generalize to amplitude amplification
- Analyze the optimality of the quadratic speedup

### Topics
1. **Unstructured Search Problem**
   - $N = 2^n$ items, $M$ marked items
   - Classical: $O(N/M)$ queries expected
   - Quantum: $O(\sqrt{N/M})$ queries

2. **Grover's Algorithm**
   - Initial state: uniform superposition $|s\rangle = H^{\otimes n}|0\rangle^n$
   - Oracle $O_f$: phase oracle flipping amplitude of marked states
   - Diffusion operator $D = 2|s\rangle\langle s| - I$: reflection about $|s\rangle$
   - Grover iteration: $G = D \cdot O_f$
   - Geometric interpretation: rotation by $2\theta$ in 2D subspace

3. **Geometric Analysis**
   - Initial angle $\theta = \arcsin(\sqrt{M/N}) \approx \sqrt{M/N}$
   - Optimal iterations: $k^* \approx \frac{\pi}{4}\sqrt{N/M}$
   - Success probability after $k^*$ iterations: $\geq 1 - M/N \approx 1$
   - Over-rotation: what happens if you apply too many iterations

4. **Multi-Target Search**
   - $M > 1$ marked items
   - Amplitude amplification: generalization to arbitrary initial states

5. **Oracle Construction**
   - Phase oracle for arbitrary Boolean functions
   - Multi-controlled gates and ancilla qubits
   - Grover oracle for 3-SAT and other NP problems

6. **BBHT Algorithm: Unknown Number of Solutions**
   - Brassard-Hoyer-Tapp: search without knowing $M$
   - Quantum counting: using QPE to estimate $M$

7. **Optimality**
   - Lower bound: $\Omega(\sqrt{N})$ queries for unstructured search
   - Grover's is optimal — no further quantum speedup possible for this problem
   - Contrast: Shor's is exponential, Grover's is quadratic

### Lab / Active Recall
- Implement Grover's search for 2-qubit and 3-qubit databases in Qiskit
- Run on IBM hardware; observe amplitude amplification
- **Month project:** Implement quantum counting to estimate the number of solutions in a 4-qubit database

---

## Month 18 — Adiabatic Quantum Computing & Quantum Annealing

### Learning Goals
- Understand the adiabatic paradigm of quantum computation
- Connect adiabatic and gate-based models
- Understand quantum annealing and its applications to optimization

### Topics
1. **Adiabatic Evolution**
   - Adiabatic theorem: if Hamiltonian changes slowly enough, system stays in instantaneous ground state
   - Condition: evolution time $T \gg \hbar / \Delta^2$ where $\Delta$ = minimum spectral gap
   - Physical example: spin in a slowly rotating magnetic field

2. **Adiabatic Quantum Computing (AQC)**
   - Start in ground state of simple $H_0$ (e.g., $H_0 = -\sum_i X_i$)
   - Slowly interpolate: $H(t) = (1-s(t))H_0 + s(t)H_P$ where $H_P$ encodes the problem
   - Final ground state = solution to problem
   - Problem encoding: NP optimization problems as Ising/QUBO Hamiltonians

3. **Equivalence to Gate-Based QC**
   - AQC is polynomially equivalent to gate-based QC
   - Any AQC algorithm can be simulated by gates (and vice versa)
   - AQC may have advantages for certain hardware implementations

4. **Ising Model and QUBO**
   - Ising Hamiltonian: $H = \sum_{i<j} J_{ij} \sigma_i^z \sigma_j^z + \sum_i h_i \sigma_i^z$
   - QUBO (Quadratic Unconstrained Binary Optimization): $\min_x x^T Q x$
   - Mapping classical optimization problems to Ising/QUBO
   - Examples: Max-Cut, Traveling Salesman, portfolio optimization

5. **Quantum Annealing**
   - Heuristic version of AQC: no guarantee of staying in ground state
   - Tunneling through barriers vs. classical thermal hopping
   - D-Wave systems: $\sim$5000+ qubits, flux qubit hardware
   - Advantages and limitations: not universal, good for optimization heuristics

6. **QAOA Introduction (Gate-Based Ansatz for Optimization)**
   - Quantum Approximate Optimization Algorithm: discretized adiabatic evolution
   - Two parameterized layers: $e^{-i\gamma H_P}$ (phase separator) and $e^{-i\beta H_0}$ (mixer)
   - $p$ layers: more layers = closer approximation ratio
   - Connection to adiabatic evolution for large $p$

### Lab / Active Recall
- Encode a small Max-Cut instance as an Ising Hamiltonian
- Run AQC simulation; plot gap as a function of interpolation
- **Month project:** Compare quantum annealing vs. simulated annealing on a small optimization problem

---

## Month 19 — Variational Quantum Algorithms: VQE & QAOA

### Learning Goals
- Implement the VQE and QAOA algorithms end-to-end
- Understand the hybrid quantum-classical optimization loop
- Connect variational algorithms to quantum chemistry and combinatorial optimization

### Topics
1. **Variational Quantum Eigensolver (VQE)**
   - Problem: find the lowest eigenvalue of a Hamiltonian $H$ (ground state energy)
   - Variational principle: $E_0 \leq \langle\psi(\theta)|H|\psi(\theta)\rangle$ for any $|\psi(\theta)\rangle$
   - Parameterized ansatz: $|\psi(\theta)\rangle = U(\theta)|0\rangle$
   - Classical optimizer: minimize $E(\theta) = \langle\psi(\theta)|H|\psi(\theta)\rangle$
   - Hybrid loop: quantum computer evaluates $E(\theta)$; classical computer updates $\theta$

2. **Quantum Chemistry via VQE**
   - Second quantization: creation/annihilation operators $a^\dagger, a$
   - Fock space: many-particle Hilbert space
   - Jordan-Wigner and Bravyi-Kitaev transformations: fermions → qubits
   - H₂ molecule: minimal example (4 spin-orbitals → 4 qubits)
   - Hartree-Fock reference state as initial ansatz
   - UCCSD ansatz: unitary coupled cluster singles and doubles

3. **VQE Practical Details**
   - Measurement of Pauli operators: decompose $H$ as sum of Paulis
   - Shot noise and variance of energy estimates
   - Barren plateaus: vanishing gradients at large circuit depth
   - Hardware-efficient ansatz vs. chemically motivated ansatz

4. **QAOA Deep Dive**
   - Problem Hamiltonian: MaxCut as example $H_P = \frac{1}{2}\sum_{(i,j)\in E}(1 - Z_iZ_j)$
   - Mixer Hamiltonian: $H_B = \sum_i X_i$
   - QAOA circuit: alternating $e^{-i\gamma_k H_P}e^{-i\beta_k H_B}$ layers
   - Parameter optimization: COBYLA, Nelder-Mead, gradient methods
   - Approximation ratio for $p=1$: $\geq 0.6924$ for MaxCut on 3-regular graphs

5. **Combinatorial Optimization via QAOA**
   - Mapping MaxCut, Vertex Cover, Number Partitioning to QUBO
   - QAOA vs. classical approximation algorithms
   - Current limitations: shallow circuits, noisy hardware, classical simulation bottleneck

6. **Error Mitigation for Variational Algorithms**
   - Zero-noise extrapolation (ZNE)
   - Probabilistic error cancellation (PEC)
   - Symmetry verification
   - Clifford data regression (CDR)

### Lab / Active Recall
- Run full VQE for H₂ dissociation curve in Qiskit Nature
- Run QAOA for MaxCut on a 5-node graph; optimize $(\gamma, \beta)$
- **Month project:** Compare QAOA at $p=1, 2, 3$ for a fixed graph; plot approximation ratio vs. $p$

---

## Month 20 — Advanced Topics, HHL, Quantum ML & Capstone

### Learning Goals
- Understand quantum linear systems solving (HHL)
- Survey quantum machine learning (QML) landscape
- Synthesize all 20 months into an integrated capstone project

### Topics
1. **NISQ Era: Current Hardware Landscape**
   - Google Sycamore (2019): quantum supremacy claim (random circuit sampling)
   - IBM Condor/Heron, IonQ Forte, Quantinuum H2
   - Qubit modalities comparison: superconducting, trapped ion, photonic, neutral atom
   - Key metrics: qubit count, gate fidelity, $T_1$/$T_2$, connectivity
   - The road to fault tolerance: where we are today

2. **HHL Algorithm (Harrow-Hassidim-Lloyd)**
   - Problem: solve $Ax = b$ for $x$
   - Classical: $O(Ns\kappa\log(1/\epsilon))$ for $N\times N$ matrix with sparsity $s$ and condition number $\kappa$
   - Quantum: $O(s^2 \kappa^2 \log N / \epsilon)$ — exponential speedup in $N$, but caveats apply
   - Circuit: quantum phase estimation + ancilla rotation + inverse QPE + amplitude amplification
   - Fine print: input/output problem (state preparation and readout costs)
   - Applications: linear systems in ML, fluid dynamics, financial modeling

3. **Quantum Machine Learning (QML)**
   - Classical neural network refresher
   - Quantum Neural Networks (QNNs): parameterized quantum circuits as function approximators
   - Data encoding strategies: amplitude encoding, angle encoding, basis encoding
   - Quantum kernel methods: $K(x,x') = |\langle\phi(x)|\phi(x')\rangle|^2$
   - Variational quantum classifier (VQC)
   - Quantum generative models: QGAN, Born machine
   - Challenges: barren plateaus, no-free-lunch, classical simulability

4. **The Bigger Picture: Where Quantum Advantage Lives**
   - Proven speedups: Shor's (factoring), Grover's (search), QFT-based algorithms
   - Heuristic hopes: VQE, QAOA for optimization, QML
   - Dequantization: classical algorithms matching certain quantum claims
   - Industry applications timeline: cryptography (near), chemistry (5-10 years), ML (speculative)

5. **Capstone Project**
   - Students implement a complete quantum algorithm end-to-end on IBM hardware
   - Suggested options:
     - Option A: **VQE for molecular ground state** (H₂ or LiH dissociation curve)
     - Option B: **QAOA for logistics optimization** (MaxCut on a supply chain graph)
     - Option C: **Grover's search for database problem** (with oracle construction)
     - Option D: **QPE-based quantum simulation** (time evolution of a spin chain)
   - Deliverables: circuit diagrams, noise analysis, error mitigation, results vs. classical baseline

### Lab / Active Recall
- Implement HHL for a $2\times 2$ linear system in Qiskit
- Build a quantum neural network with Qiskit Machine Learning; train on a simple dataset
- **Final project presentations:** Each student presents their capstone with results

---

## Curriculum Summary & Topic Map

### Topics by Source Material

| Month | QCFundamentals Source | QC Algorithms Source |
|-------|----------------------|---------------------|
| 1–2 | Prerequisites | — |
| 3–4 | Part 1 (Postulates 1 & 2) | — |
| 5–6 | Part 1 (Bloch, Entanglement, Bell) | — |
| 7–8 | Part 1 (Measurement, Teleportation) | — |
| 9–10 | Part 2 (Open Systems, Channels) | — |
| 11–12 | Part 3a (Circuits, Universality, QEC) | — |
| 13 | Part 3b (Surface Codes) | — |
| 14 | — | Part 1 (Qiskit, Deutsch-Jozsa, BV) |
| 15 | — | Part 2 (Simon's, QFT) |
| 16 | — | Part 3 (QPE, Shor's) |
| 17 | — | Part 3 (Grover's) |
| 18 | Part 4 (Adiabatic, Annealing) | Part 5 (QAOA intro) |
| 19 | Part 5 (NISQ, variational) | Part 4 (VQE) + Part 5 (QAOA) |
| 20 | Part 5 (NISQ, QML) | Part 5 (HHL, QNN) |

### Pedagogical Principles Applied

| Principle | Implementation |
|-----------|----------------|
| **Spaced repetition** | Core concepts (superposition, entanglement, measurement) revisited in months 3, 6, 7, 9, 14 |
| **Progressive complexity** | Math → postulates → circuits → algorithms → applications |
| **Theory + lab** | Every month includes hands-on Qiskit coding |
| **Interleaving** | Fundamentals and algorithms are interleaved (not all fundamentals first) |
| **Active recall** | Monthly projects require synthesis, proof, or demonstration |
| **Real hardware** | IBM Quantum hardware used from Month 14 onwards |
| **Concept revisiting** | Bloch sphere (Month 5, 9), Measurement (Month 7, 9, 14), QFT (Month 15, 16, 20) |

### Prerequisites (Assumed Before Month 1)

- Calculus (derivatives, integrals, series)
- Classical probability and statistics
- Basic programming in Python
- Classical circuits and Boolean logic (recommended)

---

*Total: 20 months · ~4 weeks/month · ~8–10 hours/week study load*
