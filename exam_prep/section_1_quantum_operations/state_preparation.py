"""State preparation and control operations - See section_1_quantum_operations/README.md for detailed documentation."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def demonstrate_initialize():
    """Initialize arbitrary quantum states"""
    print("\n" + "="*70)
    print("INITIALIZE() - ARBITRARY STATE PREPARATION")
    print("="*70)
    
    # Initialize to |1⟩
    print("\n[1] Initialize to |1⟩")
    qc = QuantumCircuit(1)
    qc.initialize([0, 1], 0)
    print(f"Circuit:\n{qc.draw()}")
    
    # Initialize to |+⟩
    print("\n[2] Initialize to |+⟩")
    qc = QuantumCircuit(1)
    qc.initialize([1/np.sqrt(2), 1/np.sqrt(2)], 0)
    print(f"Circuit:\n{qc.draw()}")
    
    # Bell state
    print("\n[3] Initialize 2-qubit Bell state")
    qc = QuantumCircuit(2)
    qc.initialize([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)], [0, 1])
    print(f"Circuit:\n{qc.draw()}")
    
    print("\n🎯 EXAM TIP: initialize() creates preparation circuit")


def demonstrate_barrier():
    """Barrier for circuit visualization and alignment"""
    print("\n" + "="*70)
    print("BARRIER() - CIRCUIT ALIGNMENT")
    print("="*70)
    
    qc = QuantumCircuit(3)
    qc.h(range(3))
    qc.barrier()  # Visual separator
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.barrier()
    qc.h(range(3))
    
    print(f"Circuit:\n{qc.draw()}")
    print("\n🎯 EXAM TIP: barrier() doesn't affect state, only visualization")


def demonstrate_reset():
    """Reset qubits to |0⟩"""
    print("\n" + "="*70)
    print("RESET() - RESET TO |0⟩")
    print("="*70)
    
    qc = QuantumCircuit(2)
    qc.x([0, 1])  # Both qubits to |1⟩
    qc.reset(0)   # Reset first qubit
    
    print(f"Circuit:\n{qc.draw()}")
    print("\n🎯 EXAM TIP: reset() forces qubit to |0⟩")


def demonstrate_delay():
    """Delay for pulse-level timing"""
    print("\n" + "="*70)
    print("DELAY() - TIMING CONTROL")
    print("="*70)
    
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.delay(100, 0, unit='ns')  # 100 nanoseconds
    qc.cx(0, 1)
    
    print(f"Circuit:\n{qc.draw()}")
    print("\n🎯 EXAM TIP: delay() for pulse-level control (ns, us, ms)")


def run_all_examples():
    """Run all state preparation examples"""
    print("\n" + "🎯" * 35)
    print(" " * 15 + "STATE PREPARATION & CONTROL")
    print(" " * 15 + "Section 1.3-1.4 - Part of 16% Section")
    print("🎯" * 35)
    
    demonstrate_initialize()
    demonstrate_barrier()
    demonstrate_reset()
    demonstrate_delay()
    
    print("\n✅ STATE PREPARATION COMPLETE!")


if __name__ == "__main__":
    run_all_examples()
