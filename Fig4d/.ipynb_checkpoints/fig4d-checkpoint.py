# generate_data_theta2.py

import qiskit
import numpy as np
import sys
import pickle
from qiskit.quantum_info import Pauli, Operator, DensityMatrix
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import TwoLocal
from qiskit.circuit import Parameter
from qiskit.extensions import UnitaryGate
from qiskit.primitives import Estimator

# Assuming kernal and functions modules are in the path
# If not, adjust the sys.path accordingly
sys.path.insert(0, '../..')
from kernal.bases.ansatz import *
from kernal.bases.metric import *
from kernal.bases.target import *
from kernal.bases.hessian import *
from kernal.bases.gradient import *
from kernal.randsearch.search import *
from run.functions import *

def generate_and_save_data():
    """
    Performs gradient calculations, computes the Mean Squared Error (MSE) for the
    second theta parameter, and saves the results to a pickle file.
    """
    print("Starting data generation for Theta 2...")
    
    # Define values and initialize lists
    step_sizes = np.linspace(10e-3, 0.99 * np.pi, 100)
    step_number = 10
    num_qubits = 2
    params = [Parameter(f'θ{i}') for i in range(2)]
    hst_circuit = hst_circuit_func(2, params)
    cost_func = infidelity_operator

    # Initialize arrays for y-component (Theta 2)
    y_2point = np.zeros(len(step_sizes), dtype=np.float64)
    y_4point = np.zeros(len(step_sizes), dtype=np.float64)
    y_ht = np.zeros(len(step_sizes), dtype=np.float64)
    y_hst = np.zeros(len(step_sizes), dtype=np.float64)

    # Perform calculations
    for i, value in enumerate(step_sizes):
        print(f"Processing step size {i+1}/{len(step_sizes)}...", end='\r')
        
        mse_2point_vals_y = np.zeros(step_number, dtype=np.float64)
        mse_4point_vals_y = np.zeros(step_number, dtype=np.float64)
        mse_ht_vals_y = np.zeros(step_number, dtype=np.float64)
        mse_hst_vals_y = np.zeros(step_number, dtype=np.float64)

        for j in range(step_number):
            x = np.random.uniform(0, 2 * np.pi)
            y = np.random.uniform(0, 2 * np.pi)
            exact = np.array(exact_func(x, y), dtype=np.float64)

            u = [ghz_ansatz, num_qubits, [], [x, y]]
            vd = [ghz_qc, num_qubits, [], []]
            uvd = [u, vd]

            grad_2point = gradient_central_difference(uvd, cost_func, method="two_point", step_size=value)
            grad_4point = gradient_central_difference(uvd, cost_func, method="four_point", step_size=value)
            grad_ht = gradient_central_difference(uvd, cost_func, method="theory", step_size=np.pi)
            grad_hst = gradient_hst(hst_circuit, hst_cost, [x, y], step_size=np.pi/2)
            
            mse_2point_vals_y[j] = np.square(np.abs(exact[1] - grad_2point[1]))
            mse_4point_vals_y[j] = np.square(np.abs(exact[1] - grad_4point[1]))
            mse_ht_vals_y[j] = np.square(np.abs(exact[1] - grad_ht[1]))
            mse_hst_vals_y[j] = np.square(np.abs(exact[1] - grad_hst[1]))

        # Mean Square Error for y-component
        y_2point[i] = np.mean(mse_2point_vals_y)
        y_4point[i] = np.mean(mse_4point_vals_y)
        y_ht[i] = np.mean(mse_ht_vals_y)
        y_hst[i] = np.mean(mse_hst_vals_y)

    # Store results in a dictionary to save
    data_to_save = {
        'step_sizes': step_sizes,
        'y_2point': y_2point,
        'y_4point': y_4point,
        'y_ht': y_ht,
        'y_hst': y_hst
    }

    # Save the dictionary to a pickle file
    with open('mse_data_theta2.pkl', 'wb') as f:
        pickle.dump(data_to_save, f)
        
    print("\nData generation complete. Results saved to mse_data_theta2.pkl")

if __name__ == "__main__":
    generate_and_save_data()