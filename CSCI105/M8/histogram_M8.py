# Run: python histogram_M8.py

import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate mock exam scores clustered around 72, clipped between 50 and 90
scores = np.random.normal(loc=72, scale=10, size=66)
scores = np.clip(scores, 50, 90)

# Define custom bins of 5 points from 50 to 90
bins = np.arange(50, 95, 5)

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
plt.ylim(0, 20)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
