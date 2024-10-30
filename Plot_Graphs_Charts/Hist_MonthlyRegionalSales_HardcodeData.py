import matplotlib.pyplot as plt
import numpy as np

# Data for 2019
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
north_2019 = [14.77, 6.45, 6.58, 14.99, 7.11, 6.55]
south_2019 = [15.48, 7.75, 6.24, 14.56, 6.47, 7.68]
east_2019 = [7.88, 6.83, 14.71, 8.45, 14.94, 6.27]
west_2019 = [6.27, 6.68, 6.60, 6.49, 7.25, 14.19]

# Set up the bar graph
x = np.arange(len(months))  # Label locations
width = 0.2  # Width of the bars

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - 1.5*width, north_2019, width, label='North')
bars2 = ax.bar(x - 0.5*width, south_2019, width, label='South')
bars3 = ax.bar(x + 0.5*width, east_2019, width, label='East')
bars4 = ax.bar(x + 1.5*width, west_2019, width, label='West')

# Add labels, title, and legend
ax.set_xlabel('Month')
ax.set_ylabel('Sales (Million SAR)')
ax.set_title('Sales by Region for Each Month in 2019')
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
