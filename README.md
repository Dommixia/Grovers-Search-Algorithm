# Grover's Quantum Search Algorithm

A clean implementation of Grover's Search Algorithm built using **Qiskit** and compared directly against a traditional **Classical Linear Search**. 

This project simulates searching an unsorted database of $N = 1024$ items ($10 \text{ qubits}$) to find a specific target index with near-deterministic ($100\%$) probability, demonstrating the quadratic speedup provided by quantum computation.

---

## Overview

In a classical unstructured search, finding a specific item in a database of size $N$ takes $O(N)$ time on average. Grover's Algorithm utilizes quantum mechanics—specifically amplitude amplification—to locate the target element in only $O(\sqrt{N})$ operations. 

For $1024$ items, a classical algorithm may check up to $1024$ entries, while this quantum implementation achieves perfect confidence in just **22 iterations**.

---

## Project Structure & Mechanics

The script generates a synthetic dataset of random floating-point numbers, hides a `target_value` ($155$) at a random index, and benchmarks two distinct search strategies:

### 1. Classical Search
* A straightforward `for` loop checks elements line-by-line until a match is found. 
* **Worst-case runtime:** $O(N)$

### 2. Quantum Search (Grover's)
* **Initialization:** Places all $10$ qubits into a uniform superposition using Hadamard ($H$) gates.
* **Phase Oracle:** Evaluates the search space and flips the phase ($\pi$ radians) of only the state matching the `target_index`.
* **Diffuser:** Inverts all state amplitudes around their average, magnifying the target state's probability while suppressing the others.
* **Transpilation & Simulation:** Uses `qiskit_aer.AerSimulator` to compile down the high-level custom gates into standard hardware basis gates and measures the result over 1024 distinct shots.

---

## Prerequisites & Installation

Make sure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```
## How to Run
```bash
python main.py
```
## Example Output
```bash
Dataset Size: 1024
Target Value: 155 - Target Index: 813
--------------------------------------------------
Classical Search:
Time taken: 0.0001550000160932541
--------------------------------------------------
Grovers Algorithm:
Confidence: 1023/1024
Time taken: 0.381098 seconds
```