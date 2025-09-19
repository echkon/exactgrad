import qiskit
import numpy as np
import sys
import pickle

# Assuming 'kernal' and 'functions' are in your python path
sys.path.insert(0, '../..') # Uncomment if your custom modules are in a parent directory
from kernal.bases.ansatz import *
from kernal.bases.metric import *
from kernal.bases.target import *
from kernal.bases.hessian import *
from kernal.bases.gradient import *
from run.functions import *

from qiskit.circuit import Parameter

print("Starting calculations...")

# --- Calculation from Cell 3 ---
params = [Parameter(f'θ{i}') for i in range(2)]

n = 2
hst_circuit = hst_circuit_func(n,params)
params[0] = 1

top = 2*np.pi
angles = np.linspace(0, top, 100)
idx = 1
hst_x = []

for theta in angles:
    params[1] = theta
    grad = gradient_hst(hst_circuit,hst_cost, params)[1]
    hst_x.append(grad)

print("HST gradient calculated.")

# --- Calculation from Cell 4 ---
top = 2 * np.pi
angles = np.linspace(0, top, 100)

exact_x = []
grads_x = []
grads_2x = []
grads_4x = []

cost_func = infidelity_operator

for s in angles:
    uvd = [[ghz_ansatz, 2, [], [1, s]], [ghz_qc, 2, [], []]]
    dev_cost_x = gradient_central_difference(uvd, cost_func, method='theory', step_size=np.pi)
    dev_cost_2x = gradient_central_difference(uvd, cost_func, method='two_point', step_size=1)
    dev_cost_4x = gradient_central_difference(uvd, cost_func, method='four_point', step_size=1)

    grads_x.append(dev_cost_x[1])
    grads_2x.append(dev_cost_2x[1])
    grads_4x.append(dev_cost_4x[1])
    exact_x.append(exact_func(1, s)[1])

print("Other gradients calculated.")

# --- Save the data to a pickle file ---
plot_data = {
    'angles': angles,
    'exact_x': exact_x,
    'grads_2x': grads_2x,
    'grads_4x': grads_4x,
    'grads_x': grads_x,
    'hst_x': hst_x
}

with open('gradient_data.pkl', 'wb') as f:
    pickle.dump(plot_data, f)

print("\nAll calculations are complete and data has been saved to 'gradient_data.pkl'.")