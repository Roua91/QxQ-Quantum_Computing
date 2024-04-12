import cirq

def main():
    # Initialize qubits
    qubits = [cirq.GridQubit(i, 0) for i in range(2)]

    # Create circuit
    circuit = cirq.Circuit()

    # Step 1: Initialize to superposition state using H gates
    circuit.append(cirq.H.on_each(*qubits))

    # Step 2: Oracle 
    circuit.append(cirq.CZ(qubits[0], qubits[1]))

    # Step 3: Diffusion Operators
    circuit.append(cirq.H.on_each(*qubits))
    circuit.append(cirq.X.on_each(*qubits))
    circuit.append(cirq.CZ(qubits[0], qubits[1]))
    circuit.append(cirq.X.on_each(*qubits))
    circuit.append(cirq.H.on_each(*qubits))

    # Step 4: Measurment
    circuit.append(cirq.measure(*qubits, key='result'))

    # Print the circuit
    print("Circuit:")
    print(circuit)

    # Simulation
    simulator = cirq.Simulator()
    results = simulator.run(circuit, repetitions=10)
    print("Results:")
    print(results)

if __name__ == '__main__':
    main()
