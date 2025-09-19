import numpy as np
import matplotlib.pyplot as plt
import pickle

# --- Load the pre-calculated data from the pickle file ---
try:
    with open('gradient_data.pkl', 'rb') as f:
        data = pickle.load(f)
except FileNotFoundError:
    print("Error: 'gradient_data.pkl' not found.")
    print("Please run 'generate_data.py' first to create the data file.")
    exit()


# Unpack the data from the dictionary into variables
angles = data['angles']
exact_x = data['exact_x']
grads_2x = data['grads_2x']
grads_4x = data['grads_4x']
grads_x = data['grads_x']
hst_x = data['hst_x']


# --- Plotting Code ---
# Ensure inputs are numpy arrays
angles = np.array(angles)
grads_2x = np.array(grads_2x)
grads_4x = np.array(grads_4x)
exact_x = np.array(exact_x)
grads_x = np.array(grads_x)
hst_x = np.array(hst_x)

# Alternate indices for plotting sparse points
idx_ht = np.arange(0, len(angles), 4)

plt.figure(figsize=(6, 6))

plt.plot(angles, exact_x, label='Exact', linestyle='-', linewidth=2.5, color='tab:blue')

# Scatter plots for different gradient estimation methods
plt.scatter(angles[idx_ht], grads_2x[idx_ht], label='Two point',
            marker='o', facecolor='blue', s=50,  alpha=0.1, zorder=5)

plt.scatter(angles[idx_ht], grads_4x[idx_ht], label='Four point',
            marker='o', facecolor='blue', s=50,  alpha=0.3, zorder=5)

plt.scatter(angles[idx_ht], grads_x[idx_ht], label='HT',
            marker='o', facecolor='blue', s=50,  alpha=0.5, zorder=5)

plt.scatter(angles[idx_ht], hst_x[idx_ht], label='HST',
            marker='o', facecolor='blue', s=50, zorder=5)

# Labels and styling
plt.title('Gradient theta 0')
plt.xlabel('Angle')
plt.ylabel('Gradient')
plt.legend()
plt.tight_layout()

# Save the figure in multiple formats
plt.savefig('grad_y.pdf', format='pdf')
plt.savefig('grad_y.png')

print("Plot saved as 'grad_y.pdf' and 'grad_y.png'.")

# Display the plot
plt.show()