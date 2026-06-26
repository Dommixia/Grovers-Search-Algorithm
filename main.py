from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit
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