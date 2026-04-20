import matplotlib.pyplot as plt

# First set of data
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Second set of data
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot first set as line graph
plt.plot(x1, y1, label='Line 1', color='blue', linewidth=2)

# Plot first set as scatter plot
plt.scatter(x1, y1, label='Scatter 1', color='red', s=100, alpha=0.6)

# Plot second set as line graph
plt.plot(x2, y2, label='Line 2', color='green', linewidth=2)

# Add title and axis labels
plt.title('Simple Data Visualization', fontsize=14, fontweight='bold')
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)

# Add legend
plt.legend()

# Add grid
plt.grid(True, alpha=0.3)

# Display the plot
plt.show()
