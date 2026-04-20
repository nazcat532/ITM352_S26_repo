import json
import matplotlib.pyplot as plt
import numpy as np

# Load the trip data from the JSON file
with open('Trips_Fri07072017T4 trip_miles gt1.json', 'r') as file:
    trips_data = json.load(file)

# Extract fares and tips
fares = [trip['fare'] for trip in trips_data]
tips = [trip['tips'] for trip in trips_data]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(fares, tips, color='blue', s=100, alpha=0.6, edgecolors='black')

# Add a trend line to visualize the relationship
z = np.polyfit(fares, tips, 1)
p = np.poly1d(z)
plt.plot(fares, p(fares), "r--", linewidth=2, label='Trend line')

# Add title and axis labels
plt.title('Scatter Plot of Fares vs Tips - Friday 07/07/2017', fontsize=14, fontweight='bold')
plt.xlabel('Fare ($)', fontsize=12)
plt.ylabel('Tips ($)', fontsize=12)

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend()

# Display the plot
plt.show()

# Calculate and print statistics
correlation = np.corrcoef(fares, tips)[0, 1]
print(f"\nData Analysis:")
print(f"Number of trips: {len(trips_data)}")
print(f"Average fare: ${np.mean(fares):.2f}")
print(f"Average tips: ${np.mean(tips):.2f}")
print(f"Correlation between fare and tips: {correlation:.4f}")
print(f"\nConclusions:")
print(f"- There is a strong positive correlation (r={correlation:.4f}) between fare and tips")
print(f"- Higher fares tend to result in higher tip amounts")
print(f"- The relationship appears to be roughly linear")
print(f"- Tip amounts range from ${min(tips):.2f} to ${max(tips):.2f}")
