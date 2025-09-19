# plot_data_theta2.py

import matplotlib.pyplot as plt
import numpy as np
import pickle

def plot_from_file():
    """
    Loads MSE data for Theta 2 from a pickle file and generates a plot.
    """
    # Load the data from the file
    try:
        with open('mse_data_theta2.pkl', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print("Error: mse_data_theta2.pkl not found. Please run generate_data_theta2.py first.")
        return

    # Unpack the data from the dictionary
    step_sizes = data['step_sizes']
    y_2point = data['y_2point']
    y_4point = data['y_4point']
    y_ht = data['y_ht']
    y_hst = data['y_hst']

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plotting the curves for Theta 2 (y-variables)
    plt.plot(step_sizes, y_2point, label='two point', color='#1f77b4', linewidth=2)
    plt.plot(step_sizes, y_4point, label='four point', color='#ff7f0e', linewidth=2)
    plt.plot(step_sizes, y_ht, label='HT', color='#2ca02c', linewidth=2)
    plt.plot(step_sizes, y_hst, label='HST', color='#d62728', linewidth=2)

    # Standard deviation shading with transparent fill
    # Note: The original calculation for the shaded region is preserved.
    plt.fill_between(step_sizes, -np.sqrt(y_2point) - y_2point, np.sqrt(y_2point) + y_2point, alpha=0.2, color='#1f77b4')
    plt.fill_between(step_sizes, -np.sqrt(y_4point) - y_4point, np.sqrt(y_4point) + y_4point, alpha=0.2, color='#ff7f0e')
    plt.fill_between(step_sizes, -np.sqrt(y_ht) - y_ht, np.sqrt(y_ht) + y_ht, alpha=0.2, color='#2ca02c')
    plt.fill_between(step_sizes, -np.sqrt(y_hst) - y_hst, np.sqrt(y_hst) + y_hst, alpha=0.2, color='#d62728')

    # Title and labels with better font style
    plt.title('Theta 2 - MSE vs Step Size', fontsize=16)
    plt.xlabel('Step Size', fontsize=14)
    plt.ylabel('MSE', fontsize=14)

    # Adding legend
    plt.legend(loc='upper left', fontsize=12)

    # Save the plot
    plt.savefig('theta2.pdf', format='pdf')
    plt.savefig('theta2.png')
    print("Plot saved as theta2.pdf and theta2.png")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_from_file()