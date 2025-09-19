### Data for: *Exact gradient for universal cost functions in variational quantum algorithms*  
**Authors:** Jesus Urbaneja¹ and Le Bin Ho² ³  
¹ Department of Mechanical and Aerospace Engineering, Tohoku University, Sendai 980-0845, Japan  
² Department of Applied Physics, Graduate School of Engineering, Tohoku University, Sendai 980-8579, Japan  
³ Frontier Research Institute for Interdisciplinary Sciences, Tohoku University, Sendai 980-8578, Japan  

---

## Overview
This repository contains the numerical data and plotting scripts used in the paper:  
*Exact gradient for universal cost functions in variational quantum algorithms.*  

The paper introduces a generalized and exact formulation of the parameter-shift rule that is valid for any differentiable cost function in variational quantum algorithms (VQAs). The data provided here supports the figures and results, including comparisons between exact gradients, Hadamard/Hilbert–Schmidt test implementations, and finite-difference methods.  

---

## File Structure
- **`Fig4/`**  
  - `Fig4a`: Gradient data ∂C/∂θ_y vs θ_y.  
  - `Fig4b`: Gradient data ∂C/∂θ_z vs θ_z.  
  - `Fig4c`: Mean squared error (MSE) of gradient estimation as a function of step size for θ_y.  
  - `Fig4d`: Same as above, for θ_z.  

---

## Data Description
- **Exact Gradient (HT/HST):**  
  Derived using the generalized parameter-shift rule. Provides baseline results that coincide exactly with theoretical values.  

- **Finite-Difference (2-point and 4-point):**  
  Computed with varying step sizes. Data illustrates sensitivity to noise at small steps and systematic bias at large steps.  

- **MSE Analysis:**  
  Each MSE dataset was obtained by sampling 10³ random parameter points uniformly over the parameter space, for step sizes ranging from 0 to π.  

- **GHZ Compilation Case Study:**  
  Data from training a variational quantum circuit to approximate a two-qubit GHZ state using gates {Ry, Rz, CNOT}. Performance of exact gradient vs finite-difference methods is compared.  

---

## Requirements

To reproduce the plots, install:

- Python ≥ 3.9  
- [NumPy](https://numpy.org/)  
- [Matplotlib](https://matplotlib.org/)  

Optional: [Seaborn](https://seaborn.pydata.org/) for enhanced figure styling.  

---

## Usage

1. Clone or download this repository.  
2. Install the required Python packages.  
3. Run the plotting scripts

