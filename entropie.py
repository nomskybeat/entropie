import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
from mpl_toolkits.mplot3d import Axes3D

# Generate random temperatures for a mix of molecules
np.random.seed(0)
num_molecules = 100
temperatures = np.random.uniform(200, 800, num_molecules)  # Temperatures between 200K and 800K

# Calculate the entropy for each temperature
# For simplicity, assume a uniform probability distribution for each temperature
prob_dist = np.ones(num_molecules) / num_molecules
entropies = entropy(prob_dist, base=2) * np.ones(num_molecules)

# Generate random positions for the molecules in 3D space
positions = np.random.rand(num_molecules, 3) * 100  # Positions in a 100x100x100 cube

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use temperatures to color the points
sc = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c=temperatures, cmap='viridis')

# Add color bar to show temperature scale
cbar = plt.colorbar(sc)
cbar.set_label('Temperature (K)')

# Set labels
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.set_title('Entropy Visualization of Molecules with Different Temperatures')

plt.show()