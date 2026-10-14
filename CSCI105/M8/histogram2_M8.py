# run: python histogram2_M8.py

import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate mock exam scores for 100 students (n = 100)
# Centered around 68, clipped between a minimum of 40 and a maximum of 90
scores = np.random.normal(loc=68, scale=12, size=100)
scores = np.clip(scores, 40, 90)

# Define 10 custom bins with a width of 5 points from 40 to 95
# (40-45, 45-50, 50-55, ..., 90-95)
bins = np.arange(40, 95, 5)

plt.figure(figsize=(6, 5))

# Create histogram
n, bins, patches = plt.hist(
    scores, bins=bins, edgecolor='white', color='#3182ce', rwidth=0.9
)

# Titles and labels matching the style
plt.title(
    '1. Histogram\nDistribution of one numeric variable in bins',
    loc='left',
    fontsize=11,
    fontweight='bold',
)
plt.xlabel('Exam score (bins of 5 points)')
plt.ylabel('Frequency (students)')
plt.ylim(0, 30)  # Scaled appropriately for 100 students
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
