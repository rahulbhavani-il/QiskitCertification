"""Single-qubit gates implementation - See section_1_quantum_operations/README.md for detailed documentation."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator


def demonstrate_pauli_gates():
    """
    EXAM QUESTION:
    Q: What are the matrix representations of Pauli gates (X, Y, Z) and what 
       is the effect of each gate on basis states |0⟩ and |1⟩?
    
    ANSWER:
    A: X flips |0⟩↔|1⟩ with matrix [[0,1],[1,0]], Z adds -1 phase to |1⟩ with 
       matrix [[1,0],[0,-1]], Y does both with matrix [[0,-i],[i,0]]. 
       See implementation for verification code.
    
    Pauli Gates (X, Y, Z) - EXAM ESSENTIAL
    
    X Gate (NOT/Bit-flip): Flips |0⟩ ↔ |1⟩
    Matrix: [[0, 1], [1, 0]]
    
    Y Gate: Rotation around Y-axis
    Matrix: [[0, -i], [i, 0]]
    
    Z Gate (Phase-flip): Flips phase of |1⟩
    Matrix: [[1, 0], [0, -1]]
    """
    print("\n" + "="*70)
    print("PAULI GATES (X, Y, Z)")
    print("="*70)
    
    # X Gate (NOT Gate)
    print("\n[1] X Gate - Bit Flip")
    print("-" * 50)
    qc_x = QuantumCircuit(1)
    qc_x.x(0)
    
    # Get matrix
    x_matrix = Operator(qc_x).data
    print(f"X Matrix:\n{x_matrix}")
    
    # Test on |0⟩
    qc_x_test = QuantumCircuit(1)
    qc_x_test.x(0)
    state = Statevector(qc_x_test)
    print(f"X|0⟩ = {state.data}")  # Should be [0, 1] = |1⟩
    
    # Test on |1⟩
    qc_x_one = QuantumCircuit(1)
    qc_x_one.x(0)  # Start with |1⟩
    qc_x_one.x(0)  # Apply X again
    state_one = Statevector(qc_x_one)
    print(f"X|1⟩ = {state_one.data}")  # Back to [1, 0] = |0⟩
    print(f"Circuit:\n{qc_x_one.draw()}")
    
    # Y Gate
    print("\n[2] Y Gate - Pauli Y")
    print("-" * 50)
    qc_y = QuantumCircuit(1)
    qc_y.y(0)
    
    y_matrix = Operator(qc_y).data
    print(f"Y Matrix:\n{y_matrix}")
    
    # Test on |0⟩
    state_y = Statevector(qc_y)
    print(f"Y|0⟩ = {state_y.data}")  # Should be [0, i] = i|1⟩
    print(f"Circuit:\n{qc_y.draw()}")
    
    # Z Gate
    print("\n[3] Z Gate - Phase Flip")
    print("-" * 50)
    qc_z = QuantumCircuit(1)
    qc_z.z(0)
    
    z_matrix = Operator(qc_z).data
    print(f"Z Matrix:\n{z_matrix}")
    
    # Test on |0⟩ (no change)
    state_z0 = Statevector(QuantumCircuit(1))
    print(f"Z|0⟩ = |0⟩ (unchanged)")
    
    # Test on superposition
    qc_z_super = QuantumCircuit(1)
    qc_z_super.h(0)  # Create |+⟩
    qc_z_super.z(0)  # Apply Z
    state_z_super = Statevector(qc_z_super)
    print(f"Z|+⟩ = {state_z_super.data}")  # Should be |-⟩
    print(f"Circuit:\n{qc_z.draw()}")
    
    print("\n🎯 EXAM TIP: X flips bits, Z flips phase, Y does both!")
    print("   Remember: X² = Y² = Z² = I (applying twice gives identity)")


def demonstrate_hadamard_gate():
    """
    EXAM QUESTION:
    Q: How do you create an equal superposition state in Qiskit, and what is 
       the result of applying the Hadamard gate to |0⟩ and |1⟩?
    
    ANSWER:
    A: Use qc.h(0). H|0⟩ = |+⟩ = (|0⟩+|1⟩)/√2 and H|1⟩ = |-⟩ = (|0⟩-|1⟩)/√2.
       Hadamard is self-inverse (H²=I). See implementation below.
    
    Hadamard Gate (H) - MOST IMPORTANT FOR EXAM
    
    Creates superposition: H|0⟩ = |+⟩ = (|0⟩ + |1⟩)/√2
                           H|1⟩ = |-⟩ = (|0⟩ - |1⟩)/√2
    
    Matrix: (1/√2) * [[1, 1], [1, -1]]
    
    Property: H² = I (Hadamard is its own inverse)
    """
    print("\n" + "="*70)
    print("HADAMARD GATE (H) - EXAM CRITICAL")
    print("="*70)
    
    print("\n[1] H Gate on |0⟩")
    print("-" * 50)
    qc_h = QuantumCircuit(1)
    qc_h.h(0)
    
    # Matrix
    h_matrix = Operator(qc_h).data
    print(f"H Matrix:\n{h_matrix}")
    
    # Effect on |0⟩
    state = Statevector(qc_h)
    print(f"H|0⟩ = {state.data}")
    print(f"      = |+⟩ = (|0⟩ + |1⟩)/√2")
    print(f"      = [{1/np.sqrt(2):.4f}, {1/np.sqrt(2):.4f}]")
    
    # Effect on |1⟩
    print("\n[2] H Gate on |1⟩")
    print("-" * 50)
    qc_h1 = QuantumCircuit(1)
    qc_h1.x(0)  # Prepare |1⟩
    qc_h1.h(0)  # Apply H
    state1 = Statevector(qc_h1)
    print(f"H|1⟩ = {state1.data}")
    print(f"      = |-⟩ = (|0⟩ - |1⟩)/√2")
    print(f"      = [{1/np.sqrt(2):.4f}, {-1/np.sqrt(2):.4f}]")
    
    # H² = I
    print("\n[3] H² = I (Self-inverse property)")
    print("-" * 50)
    qc_h2 = QuantumCircuit(1)
    qc_h2.h(0)
    qc_h2.h(0)
    state2 = Statevector(qc_h2)
    print(f"H²|0⟩ = {state2.data}")
    print(f"      = |0⟩ (back to original)")
    
    print(f"\nCircuit:\n{qc_h.draw()}")
    
    print("\n🎯 EXAM TIP: H creates equal superposition!")
    print("   H is used in EVERY Bell state circuit")
    print("   Most common exam pattern: H followed by CNOT")


def demonstrate_phase_gates():
    """
    EXAM QUESTION:
    Q: What are the S and T phase gates in Qiskit, and what is the relationship 
       between them? How do you apply an arbitrary phase?
    
    ANSWER:
    A: S adds π/2 phase to |1⟩ (qc.s()), T adds π/4 phase (qc.t()), S=T². 
       For arbitrary phase λ use qc.p(lambda, qubit). S†=qc.sdg(), T†=qc.tdg().
       See implementation for matrices and relationships.
    
    Phase Gates: S, T, P(λ) - KNOW THESE WELL
    
    S Gate: S = [[1, 0], [0, i]] (Phase by π/2)
    T Gate: T = [[1, 0], [0, e^(iπ/4)]] (Phase by π/4)
    P(λ) Gate: [[1, 0], [0, e^(iλ)]] (Arbitrary phase)
    
    Relationships:
    - S = P(π/2) = T²
    - T = P(π/4)
    - S† = S³ = S^(-1)
    """
    print("\n" + "="*70)
    print("PHASE GATES (S, T, P)")
    print("="*70)
    
    # S Gate
    print("\n[1] S Gate - Phase by π/2")
    print("-" * 50)
    qc_s = QuantumCircuit(1)
    qc_s.s(0)
    
    s_matrix = Operator(qc_s).data
    print(f"S Matrix:\n{s_matrix}")
    
    # Effect on |+⟩
    qc_s_plus = QuantumCircuit(1)
    qc_s_plus.h(0)  # Create |+⟩
    qc_s_plus.s(0)  # Apply S
    state_s = Statevector(qc_s_plus)
    print(f"S|+⟩ = {state_s.data}")
    print(f"     = (|0⟩ + i|1⟩)/√2")
    
    # S dagger (inverse)
    print("\n[2] S† (S-dagger) - Inverse of S")
    print("-" * 50)
    qc_sdg = QuantumCircuit(1)
    qc_sdg.sdg(0)
    sdg_matrix = Operator(qc_sdg).data
    print(f"S† Matrix:\n{sdg_matrix}")
    print(f"Circuit:\n{qc_sdg.draw()}")
    
    # T Gate
    print("\n[3] T Gate - Phase by π/4")
    print("-" * 50)
    qc_t = QuantumCircuit(1)
    qc_t.t(0)
    
    t_matrix = Operator(qc_t).data
    print(f"T Matrix:\n{t_matrix}")
    
    # T dagger
    print("\n[4] T† (T-dagger) - Inverse of T")
    print("-" * 50)
    qc_tdg = QuantumCircuit(1)
    qc_tdg.tdg(0)
    tdg_matrix = Operator(qc_tdg).data
    print(f"T† Matrix:\n{tdg_matrix}")
    print(f"Circuit:\n{qc_tdg.draw()}")
    
    # P(λ) - Arbitrary phase
    print("\n[5] P(λ) Gate - Arbitrary Phase")
    print("-" * 50)
    lambda_val = np.pi / 3
    qc_p = QuantumCircuit(1)
    qc_p.p(lambda_val, 0)
    
    p_matrix = Operator(qc_p).data
    print(f"P(π/3) Matrix:\n{p_matrix}")
    print(f"Circuit:\n{qc_p.draw()}")
    
    # Relationship: S = T²
    print("\n[6] Relationship: S = T²")
    print("-" * 50)
    qc_t2 = QuantumCircuit(1)
    qc_t2.t(0)
    qc_t2.t(0)
    t2_matrix = Operator(qc_t2).data
    print(f"T² Matrix:\n{t2_matrix}")
    print(f"S Matrix:\n{s_matrix}")
    print(f"T² = S: {np.allclose(t2_matrix, s_matrix)}")
    
    print("\n🎯 EXAM TIP: Phase gates only affect |1⟩ component!")
    print("   S = phase by π/2, T = phase by π/4")
    print("   P(λ) is the general form")


def demonstrate_rotation_gates():
    """
    EXAM QUESTION:
    Q: How do you perform parameterized rotations in Qiskit, and what are the 
       common rotation angles used in variational quantum algorithms?
    
    ANSWER:
    A: Use qc.rx(theta,q), qc.ry(theta,q), qc.rz(theta,q) for rotations. 
       Common angles: π/2 for superposition, π for full flip. Used in VQE.
       See implementation for examples with different angles.
    
    Rotation Gates: RX, RY, RZ - PARAMETERIZED GATES
    
    RX(θ): Rotation around X-axis
    RY(θ): Rotation around Y-axis  
    RZ(θ): Rotation around Z-axis
    
    Used extensively in variational algorithms (VQE, QAOA)
    """
    print("\n" + "="*70)
    print("ROTATION GATES (RX, RY, RZ)")
    print("="*70)
    
    theta = np.pi / 4  # 45 degrees
    
    # RX Gate
    print(f"\n[1] RX(θ={theta:.4f}) - Rotation around X-axis")
    print("-" * 50)
    qc_rx = QuantumCircuit(1)
    qc_rx.rx(theta, 0)
    
    rx_matrix = Operator(qc_rx).data
    print(f"RX(π/4) Matrix:\n{rx_matrix}")
    
    # Effect on |0⟩
    state_rx = Statevector(qc_rx)
    print(f"RX(π/4)|0⟩ = {state_rx.data}")
    print(f"Circuit:\n{qc_rx.draw()}")
    
    # RY Gate
    print(f"\n[2] RY(θ={theta:.4f}) - Rotation around Y-axis")
    print("-" * 50)
    qc_ry = QuantumCircuit(1)
    qc_ry.ry(theta, 0)
    
    ry_matrix = Operator(qc_ry).data
    print(f"RY(π/4) Matrix:\n{ry_matrix}")
    
    state_ry = Statevector(qc_ry)
    print(f"RY(π/4)|0⟩ = {state_ry.data}")
    print(f"Circuit:\n{qc_ry.draw()}")
    
    # RZ Gate
    print(f"\n[3] RZ(θ={theta:.4f}) - Rotation around Z-axis")
    print("-" * 50)
    qc_rz = QuantumCircuit(1)
    qc_rz.rz(theta, 0)
    
    rz_matrix = Operator(qc_rz).data
    print(f"RZ(π/4) Matrix:\n{rz_matrix}")
    
    state_rz = Statevector(qc_rz)
    print(f"RZ(π/4)|0⟩ = {state_rz.data}")
    print(f"Circuit:\n{qc_rz.draw()}")
    
    # Common angles
    print("\n[4] Common Rotation Angles - MEMORIZE")
    print("-" * 50)
    print(f"RY(π/2)|0⟩ creates |+⟩_Y (equal superposition in Y basis)")
    qc_ry_90 = QuantumCircuit(1)
    qc_ry_90.ry(np.pi/2, 0)
    state_90 = Statevector(qc_ry_90)
    print(f"RY(π/2)|0⟩ = {state_90.data}")
    
    print(f"\nRY(π)|0⟩ = |1⟩ (complete flip)")
    qc_ry_180 = QuantumCircuit(1)
    qc_ry_180.ry(np.pi, 0)
    state_180 = Statevector(qc_ry_180)
    print(f"RY(π)|0⟩ = {state_180.data}")
    
    print("\n🎯 EXAM TIP: Rotation gates are parameterized!")
    print("   Used in VQE and variational circuits")
    print("   RX(π) ≈ X, RY(π) ≈ Y, RZ(π) ≈ Z (up to global phase)")


def demonstrate_universal_gate():
    """
    EXAM QUESTION:
    Q: How can you represent any single-qubit gate in Qiskit using one 
       universal gate, and how do you express common gates like H and X using it?
    
    ANSWER:
    A: Use qc.u(theta, phi, lambda, qubit). U can represent ANY single-qubit gate.
       H = U(π/2, 0, π), X = U(π, 0, π). Three parameters control rotation and phase.
       See implementation for examples.
    
    U Gate - Universal Single-Qubit Gate
    
    U(θ, φ, λ): Most general single-qubit gate
    
    Matrix: [[cos(θ/2), -e^(iλ)sin(θ/2)],
             [e^(iφ)sin(θ/2), e^(i(φ+λ))cos(θ/2)]]
    
    Can represent ANY single-qubit gate!
    """
    print("\n" + "="*70)
    print("U GATE - UNIVERSAL SINGLE-QUBIT GATE")
    print("="*70)
    
    theta = np.pi / 2
    phi = np.pi / 4
    lam = np.pi / 6
    
    print(f"\n[1] U(θ={theta:.4f}, φ={phi:.4f}, λ={lam:.4f})")
    print("-" * 50)
    qc_u = QuantumCircuit(1)
    qc_u.u(theta, phi, lam, 0)
    
    u_matrix = Operator(qc_u).data
    print(f"U Matrix:\n{u_matrix}")
    
    state_u = Statevector(qc_u)
    print(f"U|0⟩ = {state_u.data}")
    print(f"Circuit:\n{qc_u.draw()}")
    
    # Express common gates using U
    print("\n[2] Express Common Gates with U")
    print("-" * 50)
    
    # H as U
    print("Hadamard = U(π/2, 0, π)")
    qc_h_u = QuantumCircuit(1)
    qc_h_u.u(np.pi/2, 0, np.pi, 0)
    h_from_u = Operator(qc_h_u).data
    print(f"U(π/2, 0, π) ≈ H: Matrix:\n{h_from_u}")
    
    # X as U
    print("\nPauli X = U(π, 0, π)")
    qc_x_u = QuantumCircuit(1)
    qc_x_u.u(np.pi, 0, np.pi, 0)
    x_from_u = Operator(qc_x_u).data
    print(f"U(π, 0, π) ≈ X: Matrix:\n{x_from_u}")
    
    print("\n🎯 EXAM TIP: U gate can represent ANY single-qubit gate!")
    print("   Three parameters: θ (rotation), φ (phase), λ (phase)")


def demonstrate_identity_gate():
    """
    EXAM QUESTION:
    Q: What is the identity gate in Qiskit and when would you use it in 
       a quantum circuit?
    
    ANSWER:
    A: Use qc.id(qubit). Identity gate does nothing (I|ψ⟩=|ψ⟩, matrix=[[1,0],[0,1]]).
       Used for circuit alignment and timing in multi-qubit circuits.
       See implementation below.
    
    Identity Gate (I) - Do-Nothing Gate
    
    Matrix: [[1, 0], [0, 1]]
    
    Effect: I|ψ⟩ = |ψ⟩ (leaves state unchanged)
    
    Used for: Circuit alignment, timing
    """
    print("\n" + "="*70)
    print("IDENTITY GATE (I)")
    print("="*70)
    
    print("\n[1] I Gate - Identity")
    print("-" * 50)
    qc_i = QuantumCircuit(1)
    qc_i.id(0)
    
    i_matrix = Operator(qc_i).data
    print(f"I Matrix:\n{i_matrix}")
    
    # No effect on state
    state_i = Statevector(qc_i)
    print(f"I|0⟩ = {state_i.data}")
    print(f"     = |0⟩ (unchanged)")
    print(f"Circuit:\n{qc_i.draw()}")
    
    print("\n🎯 EXAM TIP: Identity gate does nothing!")
    print("   Used for circuit alignment in multi-qubit circuits")


def demonstrate_all_gates_comparison():
    """
    EXAM QUESTION:
    Q: Given a table showing the output states of different gates applied to |0⟩,
       how do you identify which gate was used?
    
    ANSWER:
    A: Compare output states: |1⟩→X gate, (|0⟩+|1⟩)/√2→H gate, |0⟩ with phase→Z/S/T.
       See implementation for complete comparison table of all single-qubit gates.
    
    Compare ALL single-qubit gates on |0⟩ state
    
    Shows the effect of each gate for easy comparison.
    Essential for exam questions that ask about gate effects!
    """
    print("\n" + "="*70)
    print("ALL SINGLE-QUBIT GATES COMPARISON TABLE")
    print("="*70)
    
    gates = {
        'I': lambda qc: qc.id(0),
        'X': lambda qc: qc.x(0),
        'Y': lambda qc: qc.y(0),
        'Z': lambda qc: qc.z(0),
        'H': lambda qc: qc.h(0),
        'S': lambda qc: qc.s(0),
        'T': lambda qc: qc.t(0),
        'S†': lambda qc: qc.sdg(0),
        'T†': lambda qc: qc.tdg(0),
    }
    
    print("\nGate | State after applying to |0⟩")
    print("-" * 70)
    
    for gate_name, gate_func in gates.items():
        qc = QuantumCircuit(1)
        gate_func(qc)
        state = Statevector(qc)
        
        # Format state for display
        amp0 = f"{state.data[0]:.4f}"
        amp1 = f"{state.data[1]:.4f}"
        print(f"{gate_name:4} | [{amp0:>12}, {amp1:>12}]")
    
    # Rotation gates with common angles
    print("\n" + "-" * 70)
    print("Rotation Gates (θ = π/4):")
    print("-" * 70)
    
    for gate_name, gate_func in [
        ('RX(π/4)', lambda qc: qc.rx(np.pi/4, 0)),
        ('RY(π/4)', lambda qc: qc.ry(np.pi/4, 0)),
        ('RZ(π/4)', lambda qc: qc.rz(np.pi/4, 0)),
    ]:
        qc = QuantumCircuit(1)
        gate_func(qc)
        state = Statevector(qc)
        amp0 = f"{state.data[0]:.4f}"
        amp1 = f"{state.data[1]:.4f}"
        print(f"{gate_name:8} | [{amp0:>12}, {amp1:>12}]")
    
    print("\n" + "="*70)
    print("💡 MEMORIZE THIS TABLE FOR EXAM SUCCESS!")
    print("="*70)


def run_all_examples():
    """
    Run all single-qubit gate demonstrations.
    Perfect for systematic study and review!
    """
    print("\n" + "🎯" * 35)
    print(" " * 20 + "SINGLE-QUBIT GATES")
    print(" " * 15 + "Section 1.1 - 16% of Exam (~11 questions)")
    print("🎯" * 35)
    
    demonstrate_pauli_gates()
    demonstrate_hadamard_gate()
    demonstrate_phase_gates()
    demonstrate_rotation_gates()
    demonstrate_universal_gate()
    demonstrate_identity_gate()
    demonstrate_all_gates_comparison()
    
    print("\n" + "="*70)
    print("✅ SINGLE-QUBIT GATES COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Pauli gates (X, Y, Z) are basis gates")
    print("2. Hadamard creates superposition - MOST IMPORTANT")
    print("3. Phase gates (S, T) modify phase of |1⟩")
    print("4. Rotation gates (RX, RY, RZ) are parameterized")
    print("5. U gate can represent ANY single-qubit gate")
    print("\n🎓 Practice these gates without looking at docs!")


if __name__ == "__main__":
    """
    Run this module directly to see all single-qubit gate examples.
    Usage: python -m section_1_quantum_operations.single_qubit_gates
    """
    run_all_examples()
