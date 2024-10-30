# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Data set
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Basic plot
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
 
# use the plt.xticks function to custom labels
plt.xticks(y_pos, bars, color='orange', rotation=45, fontweight='bold', fontsize='17', horizontalalignment='right')
plt.show()
 
# remove labels
plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
plt.tick_params(labelbottom=False)
plt.show()