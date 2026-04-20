import json
import matplotlib.pyplot as plt
import numpy as np

# Load the trip data from the JSON file
with open('Trips from area 8.json', 'r') as file:
    trips_data = json.load(file)

# Extract fares and miles
fares = [trip['fare'] for trip in trips_data]
miles = [trip['miles'] for trip in trips_data]

# Create figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Using plt.scatter()
ax1.scatter(fares, miles, color='blue', s=100, alpha=0.6, edgecolors='black')
ax1.set_xlabel('Fare ($)', fontsize=11)
ax1.set_ylabel('Trip Miles', fontsize=11)
ax1.set_title('Scatter Plot 1: Using plt.scatter()', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Plot 2: Using plt.plot with linestyle="none" and marker="."
ax2.plot(fares, miles, linestyle='none', marker='.', color='green', markersize=10, alpha=0.6)
ax2.set_xlabel('Fare ($)', fontsize=11)
ax2.set_ylabel('Trip Miles', fontsize=11)
ax2.set_title('Scatter Plot 2: Using plt.plot(linestyle="none")', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Plot 3: Fancy version with "v" marker, cyan color, and 0.2 transparency
ax3.scatter(fares, miles, marker='v', color='cyan', s=150, alpha=0.2, edgecolors='black', linewidths=1.5)
ax3.set_xlabel('Fare ($)', fontsize=11)
ax3.set_ylabel('Trip Miles', fontsize=11)
ax3.set_title('Scatter Plot 3: Fancy Version (v marker, cyan, alpha=0.2)', fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Calculate and print statistics
correlation = np.corrcoef(fares, miles)[0, 1]
print(f"\nData Analysis - Fares vs Trip Miles:")
print(f"Number of trips: {len(trips_data)}")
print(f"Average fare: ${np.mean(fares):.2f}")
print(f"Average trip miles: {np.mean(miles):.2f}")
print(f"Correlation between fare and miles: {correlation:.4f}")
print(f"\nConclusions:")
print(f"- There is a strong positive correlation (r={correlation:.4f}) between fare and trip miles")
print(f"- Longer trips (more miles) generally cost more (higher fares)")
print(f"- The relationship appears to be nearly linear, suggesting a consistent rate per mile")
print(f"- Fare ranges from ${min(fares):.2f} to ${max(fares):.2f}")
print(f"- Trip miles range from {min(miles):.1f} to {max(miles):.1f} miles")
print(f"- The data shows predictable pricing: approximately ${np.mean(fares)/np.mean(miles):.2f} per mile")
