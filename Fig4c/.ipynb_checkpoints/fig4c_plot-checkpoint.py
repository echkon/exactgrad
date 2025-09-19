# plot_data.py

import matplotlib.pyplot as plt
import numpy as np
import pickle

def plot_from_file():
    """
    Loads MSE data from a pickle file and generates a plot.
    """
    # Load the data from the file
    try:
        with open('mse_data.pkl', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print("Error: mse_data.pkl not found. Please run generate_data.py first.")
        return

    # Unpack the data from the dictionary
    step_sizes = data['step_sizes']
    x_2point = data['x_2point']
    x_4point = data['x_4point']
    x_ht = data['x_ht']
    x_hst = data['x_hst']

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plotting the curves with distinct line styles and markers
    plt.plot(step_sizes, x_2point, label='two point', color='#1f77b4', linewidth=2)
    plt.plot(step_sizes, x_4point, label='four point', color='#ff7f0e', linewidth=2)
    plt.plot(step_sizes, x_ht, label='HT', color='#2ca02c', linewidth=2)
    plt.plot(step_sizes, x_hst, label='HST', color='#d62728', linewidth=2)

    # Standard deviation shading with transparent fill
    # Note: The original calculation for the shaded region is preserved.
    plt.fill_between(step_sizes, -np.sqrt(x_2point) - x_2point, np.sqrt(x_2point) + x_2point, alpha=0.2, color='#1f77b4')
    plt.fill_between(step_sizes, -np.sqrt(x_4point) - x_4point, np.sqrt(x_4point) + x_4point, alpha=0.2, color='#ff7f0e')
    plt.fill_between(step_sizes, -np.sqrt(x_ht) - x_ht, np.sqrt(x_ht) + x_ht, alpha=0.2, color='#2ca02c')
    plt.fill_between(step_sizes, -np.sqrt(x_hst) - x_hst, np.sqrt(x_hst) + x_hst, alpha=0.2, color='#d62728')

    # Title and labels with better font style
    plt.title('Theta 1 - MSE vs Step Size', fontsize=16)
    plt.xlabel('Step Size', fontsize=14)
    plt.ylabel('MSE', fontsize=14)

    # Adding legend
    plt.legend(loc='upper left', fontsize=12)

    # Save the plot
    plt.savefig('theta1.pdf', format='pdf')
    plt.savefig('theta1.png')
    print("Plot saved as theta1.pdf and theta1.png")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_from_file()