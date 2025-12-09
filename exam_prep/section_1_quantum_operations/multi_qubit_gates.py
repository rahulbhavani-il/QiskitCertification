"""Multi-qubit gates and entanglement - See section_1_quantum_operations/README.md for detailed documentation."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator


def demonstrate_cnot_gate():
    """
    EXAM QUESTION:
    Q: How do you apply a CNOT gate in Qiskit, and what is its truth table?
       What is the syntax for specifying control and target qubits?
    
    ANSWER:
    A: Use qc.cx(control, target) or qc.cnot(control, target). 
       CNOT flips target qubit if control is |1⟩: |10⟩→|11⟩, |11⟩→|10⟩.
       First argument is control, second is target. See implementation for truth table.
    
    CNOT (CX) Gate - MOST IMPORTANT MULTI-QUBIT GATE
    
    Controlled-NOT: Flips target if control is |1⟩
    
    Syntax: qc.cx(control, target) or qc.cnot(control, target)
    
    Truth table:
    |00⟩ → |00⟩
    |01⟩ → |01⟩
    |10⟩ → |11⟩  (flips target)
    |11⟩ → |10⟩  (flips target)
    """
    print("\n" + "="*70)
    print("CNOT (CX) GATE - CONTROLLED-NOT")
    print("="*70)
    
    print("\n[1] CNOT Gate Basics")
    print("-" * 50)
    qc_cnot = QuantumCircuit(2)
    qc_cnot.cx(0, 1)  # Control=qubit 0, Target=qubit 1
    
    print(f"Circuit:\n{qc_cnot.draw()}")
    print("\nRemember: cx(control, target)")
    print("Top qubit (0) = control, Bottom qubit (1) = target")
    
    # Test all basis states
    print("\n[2] CNOT Truth Table")
    print("-" * 50)
    
    basis_states = ['00', '01', '10', '11']
    for state in basis_states:
        qc = QuantumCircuit(2)
        
        # Prepare input state
        if state[0] == '1':
            qc.x(0)
        if state[1] == '1':
            qc.x(1)
        
        # Apply CNOT
        qc.cx(0, 1)
        
        # Get output
        result = Statevector(qc)
        output = ''.join(['1' if abs(result.data[i]) > 0.5 else '0' 
                         for i in range(4) if abs(result.data[i]) > 0.5])
        
        print(f"|{state}⟩ → |{output}⟩")
    
    # Creating entanglement
    print("\n[3] Creating Entanglement with H + CNOT")
    print("-" * 50)
    qc_bell = QuantumCircuit(2)
    qc_bell.h(0)
    qc_bell.cx(0, 1)
    
    state = Statevector(qc_bell)
    print(f"Circuit:\n{qc_bell.draw()}")
    print(f"\nState vector: {state.data}")
    print(f"This is Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    # convert to probabilities
    probs = np.abs(state.data)**2
    print(f"Probabilities: |00⟩: {probs[0]:.2f}, |11⟩: {probs[3]:.2f}")
    
    print("\n🎯 EXAM TIP: H + CNOT is THE most common pattern!")
    print("   CNOT creates entanglement from superposition")
    print("   Used in EVERY Bell state circuit")


def demonstrate_cz_gate():
    """
    EXAM QUESTION:
    Q: What is the difference between CZ and CNOT gates, and what is the key
       property of the CZ gate regarding control and target qubits?
    
    ANSWER:
    A: CZ applies Z to target if control is |1⟩ (adds -1 phase to |11⟩ only).
       CZ is SYMMETRIC: cz(0,1) = cz(1,0), unlike CNOT. CZ ≡ H-CNOT-H sandwich.
       See implementation for verification.
    
    CZ Gate - Controlled-Z
    
    Applies Z to target if control is |1⟩
    
    Property: CZ is symmetric (control and target are interchangeable)
    
    Effect: Adds phase of -1 to |11⟩ state only
    """
    print("\n" + "="*70)
    print("CZ GATE - CONTROLLED-Z")
    print("="*70)
    
    print("\n[1] CZ Gate Basics")
    print("-" * 50)
    qc_cz = QuantumCircuit(2)
    qc_cz.cz(0, 1)
    
    print(f"Circuit:\n{qc_cz.draw()}")
    
    # Matrix representation
    cz_matrix = Operator(qc_cz).data
    print(f"\nCZ Matrix:\n{cz_matrix}")
    
    # Effect on basis states
    print("\n[2] CZ Effect on Basis States")
    print("-" * 50)
    print("|00⟩ → |00⟩")
    print("|01⟩ → |01⟩")
    print("|10⟩ → |10⟩")
    print("|11⟩ → -|11⟩  (phase flip)")
    
    # Equivalence with CNOT
    print("\n[3] CZ ≡ H-CNOT-H Sandwich")
    print("-" * 50)
    qc_equiv = QuantumCircuit(2)
    qc_equiv.h(1)
    qc_equiv.cx(0, 1)
    qc_equiv.h(1)
    
    equiv_matrix = Operator(qc_equiv).data
    print(f"H-CNOT-H circuit:\n{qc_equiv.draw()}")
    print(f"\nMatrices equal: {np.allclose(cz_matrix, equiv_matrix)}")
    
    print("\n🎯 EXAM TIP: CZ is symmetric!")
    print("   cz(0,1) = cz(1,0) unlike CNOT")


def demonstrate_swap_gate():
    """
    EXAM QUESTION:
    Q: How do you swap two qubits in Qiskit, and when would you use a SWAP gate?
    
    ANSWER:
    A: Use qc.swap(qubit1, qubit2). SWAP exchanges qubit states: |01⟩↔|10⟩.
       Used for qubit routing on hardware with limited connectivity. 
       Can be decomposed as 3 CNOTs. See implementation for examples.
    
    SWAP Gate - Swaps two qubits
    
    SWAP|01⟩ = |10⟩
    SWAP|10⟩ = |01⟩
    
    Used for: Qubit routing on hardware with limited connectivity
    """
    print("\n" + "="*70)
    print("SWAP GATE")
    print("="*70)
    
    print("\n[1] SWAP Gate Basics")
    print("-" * 50)
    qc_swap = QuantumCircuit(2)
    qc_swap.swap(0, 1)
    
    print(f"Circuit:\n{qc_swap.draw()}")
    
    # Test on |01⟩
    print("\n[2] SWAP |01⟩ = |10⟩")
    print("-" * 50)
    qc_test = QuantumCircuit(2)
    qc_test.x(1)  # Prepare |01⟩
    qc_test.swap(0, 1)
    
    state = Statevector(qc_test)
    print(f"Input: |01⟩")
    print(f"Output: {state.data}")
    print(f"Result: |10⟩ (qubits swapped)")
    
    # Decomposition
    print("\n[3] SWAP Decomposition (3 CNOTs)")
    print("-" * 50)
    qc_decomp = QuantumCircuit(2)
    qc_decomp.cx(0, 1)
    qc_decomp.cx(1, 0)
    qc_decomp.cx(0, 1)
    
    print(f"Circuit:\n{qc_decomp.draw()}")
    print("\nSWAP = CNOT(0,1) + CNOT(1,0) + CNOT(0,1)")
    
    decomp_matrix = Operator(qc_decomp).data
    swap_matrix = Operator(qc_swap).data
    print(f"Matrices equal: {np.allclose(swap_matrix, decomp_matrix)}")
    
    print("\n🎯 EXAM TIP: SWAP exchanges qubit states")
    print("   Can be decomposed into 3 CNOTs")


def demonstrate_toffoli_gate():
    """
    Toffoli Gate (CCX) - Controlled-Controlled-NOT
    
    Flips target if BOTH controls are |1⟩
    
    Syntax: qc.ccx(control1, control2, target) or qc.toffoli(...)
    
    Classical: Implements AND operation
    Quantum: Universal for reversible computation
    """
    print("\n" + "="*70)
    print("TOFFOLI GATE (CCX) - CONTROLLED-CONTROLLED-NOT")
    print("="*70)
    
    print("\n[1] Toffoli Gate Basics")
    print("-" * 50)
    qc_ccx = QuantumCircuit(3)
    qc_ccx.ccx(0, 1, 2)  # Controls: 0,1 | Target: 2
    
    print(f"Circuit:\n{qc_ccx.draw()}")
    print("\nSyntax: ccx(control1, control2, target)")
    
    # Truth table
    print("\n[2] Toffoli Truth Table (Target flips only if both controls=1)")
    print("-" * 50)
    
    test_states = ['000', '001', '010', '011', '100', '101', '110', '111']
    print("Input → Output")
    print("-" * 30)
    
    for state in test_states:
        qc = QuantumCircuit(3)
        
        # Prepare input
        for i, bit in enumerate(state):
            if bit == '1':
                qc.x(i)
        
        # Apply Toffoli
        qc.ccx(0, 1, 2)
        
        # Get output state
        result = Statevector(qc)
        # Find which basis state has amplitude 1
        for i, amp in enumerate(result.data):
            if abs(amp) > 0.9:
                output = format(i, '03b')
                break
        
        marker = " ← Target flipped" if state[:2] == '11' else ""
        print(f"|{state}⟩ → |{output}⟩{marker}")
    
    print("\n[3] Toffoli as AND Gate")
    print("-" * 50)
    qc_and = QuantumCircuit(3)
    # Start with |110⟩
    qc_and.x(0)
    qc_and.x(1)
    # Apply Toffoli
    qc_and.ccx(0, 1, 2)
    
    print(f"Circuit:\n{qc_and.draw()}")
    print(f"\n|110⟩ → |111⟩")
    print(f"Target qubit computes: q0 AND q1")
    
    print("\n🎯 EXAM TIP: Toffoli has 2 controls, 1 target")
    print("   Flips target ONLY if both controls are |1⟩")
    print("   Classical: Implements AND operation")


def create_bell_states():
    """
    All 4 Bell States - MEMORIZE THESE CIRCUITS!
    
    Bell states are maximally entangled 2-qubit states.
    
    |Φ+⟩ = (|00⟩ + |11⟩)/√2    [H + CNOT]
    |Φ-⟩ = (|00⟩ - |11⟩)/√2    [H + Z + CNOT]
    |Ψ+⟩ = (|01⟩ + |10⟩)/√2    [H + X + CNOT]
    |Ψ-⟩ = (|01⟩ - |10⟩)/√2    [H + X + Z + CNOT]
    
    GUARANTEED exam questions!
    """
    print("\n" + "="*70)
    print("BELL STATES - ALL 4 CIRCUITS")
    print("="*70)
    print("\n⚠️  MEMORIZE THESE FOR 100% EXAM SUCCESS! ⚠️\n")
    
    # Bell state |Φ+⟩
    print("\n[1] |Φ+⟩ = (|00⟩ + |11⟩)/√2")
    print("-" * 50)
    qc_phi_plus = QuantumCircuit(2)
    qc_phi_plus.h(0)
    qc_phi_plus.cx(0, 1)
    
    state_phi_plus = Statevector(qc_phi_plus)
    print(f"Circuit:\n{qc_phi_plus.draw()}")
    print(f"State vector: {state_phi_plus.data}")
    print(f"Recipe: H(0) + CNOT(0,1)")
    
    # Bell state |Φ-⟩
    print("\n[2] |Φ-⟩ = (|00⟩ - |11⟩)/√2")
    print("-" * 50)
    qc_phi_minus = QuantumCircuit(2)
    qc_phi_minus.h(0)
    qc_phi_minus.z(0)  # Add phase
    qc_phi_minus.cx(0, 1)
    
    state_phi_minus = Statevector(qc_phi_minus)
    print(f"Circuit:\n{qc_phi_minus.draw()}")
    print(f"State vector: {state_phi_minus.data}")
    print(f"Recipe: H(0) + Z(0) + CNOT(0,1)")
    
    # Bell state |Ψ+⟩
    print("\n[3] |Ψ+⟩ = (|01⟩ + |10⟩)/√2")
    print("-" * 50)
    qc_psi_plus = QuantumCircuit(2)
    qc_psi_plus.h(0)
    qc_psi_plus.x(1)  # Flip target first
    qc_psi_plus.cx(0, 1)
    
    state_psi_plus = Statevector(qc_psi_plus)
    print(f"Circuit:\n{qc_psi_plus.draw()}")
    print(f"State vector: {state_psi_plus.data}")
    print(f"Recipe: H(0) + X(1) + CNOT(0,1)")
    
    # Bell state |Ψ-⟩
    print("\n[4] |Ψ-⟩ = (|01⟩ - |10⟩)/√2")
    print("-" * 50)
    qc_psi_minus = QuantumCircuit(2)
    qc_psi_minus.h(0)
    qc_psi_minus.z(0)  # Add phase
    qc_psi_minus.x(1)  # Flip target
    qc_psi_minus.cx(0, 1)
    
    state_psi_minus = Statevector(qc_psi_minus)
    print(f"Circuit:\n{qc_psi_minus.draw()}")
    print(f"State vector: {state_psi_minus.data}")
    print(f"Recipe: H(0) + Z(0) + X(1) + CNOT(0,1)")
    
    # Summary table
    print("\n" + "="*70)
    print("BELL STATES SUMMARY - MEMORIZE THIS TABLE!")
    print("="*70)
    print("\nState  | Expression              | Gates")
    print("-" * 70)
    print("|Φ+⟩   | (|00⟩ + |11⟩)/√2       | H(0) + CNOT(0,1)")
    print("|Φ-⟩   | (|00⟩ - |11⟩)/√2       | H(0) + Z(0) + CNOT(0,1)")
    print("|Ψ+⟩   | (|01⟩ + |10⟩)/√2       | H(0) + X(1) + CNOT(0,1)")
    print("|Ψ-⟩   | (|01⟩ - |10⟩)/√2       | H(0) + Z(0) + X(1) + CNOT(0,1)")
    
    print("\n🎯 EXAM TIP: H + CNOT creates |Φ+⟩")
    print("   Add Z(0) for negative phase: Φ+ → Φ-")
    print("   Add X(1) to swap: Φ → Ψ")
    print("   Memorize all 4 circuits!")


def create_ghz_states():
    """
    GHZ States - Multi-qubit Entanglement
    
    GHZ = Greenberger-Horne-Zeilinger state
    
    3-qubit GHZ: |GHZ⟩ = (|000⟩ + |111⟩)/√2
    
    Pattern: H on first qubit + CNOT chain
    """
    print("\n" + "="*70)
    print("GHZ STATES - MULTI-QUBIT ENTANGLEMENT")
    print("="*70)
    
    # 3-qubit GHZ
    print("\n[1] 3-Qubit GHZ State")
    print("-" * 50)
    qc_ghz3 = QuantumCircuit(3)
    qc_ghz3.h(0)
    qc_ghz3.cx(0, 1)
    qc_ghz3.cx(0, 2)  # or cx(1, 2) for chain
    
    state_ghz3 = Statevector(qc_ghz3)
    print(f"Circuit:\n{qc_ghz3.draw()}")
    print(f"State vector: {state_ghz3.data}")
    print(f"|GHZ⟩ = (|000⟩ + |111⟩)/√2")
    
    # Alternative: CNOT chain
    print("\n[2] 3-Qubit GHZ (Chain Pattern)")
    print("-" * 50)
    qc_ghz3_chain = QuantumCircuit(3)
    qc_ghz3_chain.h(0)
    qc_ghz3_chain.cx(0, 1)
    qc_ghz3_chain.cx(1, 2)  # Chain from qubit 1
    
    print(f"Circuit:\n{qc_ghz3_chain.draw()}")
    print(f"Pattern: H(0) + CNOT(0,1) + CNOT(1,2)")
    
    # 4-qubit GHZ
    print("\n[3] 4-Qubit GHZ State")
    print("-" * 50)
    qc_ghz4 = QuantumCircuit(4)
    qc_ghz4.h(0)
    qc_ghz4.cx(0, 1)
    qc_ghz4.cx(0, 2)
    qc_ghz4.cx(0, 3)
    
    print(f"Circuit:\n{qc_ghz4.draw()}")
    print(f"|GHZ⟩₄ = (|0000⟩ + |1111⟩)/√2")
    
    # General pattern
    print("\n[4] General n-Qubit GHZ Pattern")
    print("-" * 50)
    print("Algorithm:")
    print("1. Apply H to qubit 0")
    print("2. Apply CNOT from qubit 0 to all other qubits")
    print("   OR apply CNOT chain: 0→1, 1→2, 2→3, ...")
    print("\nResult: (|000...0⟩ + |111...1⟩)/√2")
    
    print("\n🎯 EXAM TIP: GHZ extends Bell states to n qubits")
    print("   Pattern: H + CNOT cascade")
    print("   All qubits become correlated")


def multi_qubit_gate_comparison():
    """
    Compare all multi-qubit gates - Quick reference
    """
    print("\n" + "="*70)
    print("MULTI-QUBIT GATES COMPARISON")
    print("="*70)
    
    print("\nGate   | Qubits | Description                    | Key Property")
    print("-" * 70)
    print("CNOT   | 2      | Controlled-NOT                 | Creates entanglement")
    print("CZ     | 2      | Controlled-Z                   | Symmetric")
    print("SWAP   | 2      | Exchange qubits                | 3 CNOTs")
    print("CCX    | 3      | Toffoli (2 controls)           | Universal")
    print("Bell   | 2      | 4 maximally entangled states   | H + CNOT base")
    print("GHZ    | n      | Multi-qubit entanglement       | H + CNOT chain")
    
    print("\n" + "="*70)
    print("💡 MEMORIZE: CNOT signature and all Bell states!")
    print("="*70)


def run_all_examples():
    """
    Run all multi-qubit gate demonstrations.
    Essential for exam preparation!
    """
    print("\n" + "🎯" * 35)
    print(" " * 18 + "MULTI-QUBIT GATES")
    print(" " * 15 + "Section 1.2 - 16% of Exam (~11 questions)")
    print("🎯" * 35)
    
    demonstrate_cnot_gate()
    demonstrate_cz_gate()
    demonstrate_swap_gate()
    demonstrate_toffoli_gate()
    create_bell_states()
    create_ghz_states()
    multi_qubit_gate_comparison()
    
    print("\n" + "="*70)
    print("✅ MULTI-QUBIT GATES COMPLETE!")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. CNOT creates entanglement - MOST IMPORTANT")
    print("2. All 4 Bell states use H + CNOT pattern")
    print("3. CZ is symmetric, CNOT is not")
    print("4. SWAP exchanges qubits (3 CNOTs)")
    print("5. Toffoli (CCX) has 2 controls")
    print("6. GHZ extends entanglement to n qubits")
    print("\n🎓 Practice Bell states until you can draw them instantly!")


if __name__ == "__main__":
    """
    Run this module directly to see all multi-qubit gate examples.
    Usage: python -m section_1_quantum_operations.multi_qubit_gates
    """
    run_all_examples()
