# run: python UnEvenBin.py
import matplotlib.pyplot as plt
import numpy as np

# Set random seed and generate sample data
np.res = np.random.seed(42)
data = np.random.exponential(scale=10, size=500)

# Define UNEVEN bin edges (note how widths change: width 5, then 10, then 20)
bins = [0, 5, 10, 20, 40, 80]

plt.figure(figsize=(7, 5))

# edgecolor='black' helps clearly distinguish bins with different widths
# density=True normalizes the total area to 1 (relative frequency density)
n, bins, patches = plt.hist(
    data, bins=bins, edgecolor='black', color='#3182ce', alpha=0.8, density=True
)

plt.title(
    'Histogram with Uneven Bin Widths\n(Unit-Area / Frequency Density)',
    fontsize=12,
    fontweight='bold',
)
plt.xlabel('Value Range')
plt.ylabel('Frequency Density (Area = Frequency Proportion)')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
