from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile
import numpy as np
import time

num_qubits = 10
N = 2**num_qubits
dataset = np.random.uniform(1,100, N)
print(f"Dataset Size: {N}")
target_value = 155
target_index = np.random.randint(N)
dataset[target_index] = target_value
print(f"Target Value: {target_value} - Target Index: {target_index}")
print("--------------------------------------------------")
#CLASSICAL SEARCH
print("Classical Search")
found_index = -1
c_start = time.perf_counter()
for i in range(len(dataset)):
    if dataset[i] == target_value:
        found_index = i
        break
c_end= time.perf_counter()
c_time = c_end - c_start
print(f"Time taken: {c_time}")

print("--------------------------------------------------")

#Quantum Search
print("Grovers Algorithm")

def phase_oracle(num_qubits, target_index):
    qc = QuantumCircuit(num_qubits)
    bin_target = format(target_index, f'0{num_qubits}b')
    for i, bit in enumerate(bin_target):
        if bit == '0':
            qc.x(i)
    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)

    # Undo X-gates to restore state
    for i, bit in enumerate(bin_target):
        if bit == '0':
            qc.x(i)
    return qc.to_gate(label='Oracle')

def diffuser(num_qubits):
    qc = QuantumCircuit(num_qubits)
    qc.h(range(num_qubits))
    qc.x(range(num_qubits))
    # Multi-controlled Z gate
    qc.h(num_qubits - 1)
    qc.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    qc.h(num_qubits - 1)
    qc.x(range(num_qubits))
    qc.h(range(num_qubits))
    return qc.to_gate(label="Diffuser")

qc = QuantumCircuit(num_qubits, num_qubits)
qc.h(range(num_qubits))
iterations = int(np.floor(np.pi/4*np.sqrt(N)))

oracle_gate = phase_oracle(num_qubits, target_index)
diffuser_gate = diffuser(num_qubits)

for _ in range(iterations):
    qc.append(oracle_gate, range(num_qubits))
    qc.append(diffuser_gate, range(num_qubits))
qc.measure(range(num_qubits), range(num_qubits))