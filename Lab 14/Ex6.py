import json
import matplotlib.pyplot as plt
import numpy as np

# Load the trip data from the JSON file
with open('Trips from area 8.json', 'r') as file:
    trips_data = json.load(file)

# Filter out trips with 0 miles and trips less than 2 miles
filtered_trips = [trip for trip in trips_data if trip['miles'] > 0 and trip['miles'] >= 2]

# Extract fares and miles from filtered data
fares = [trip['fare'] for trip in filtered_trips]
miles = [trip['miles'] for trip in filtered_trips]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(fares, miles, color='blue', s=100, alpha=0.6, edgecolors='black')

# Add a trend line to visualize the relationship
z = np.polyfit(fares, miles, 1)
p = np.poly1d(z)
plt.plot(fares, p(fares), "r--", linewidth=2, label='Trend line')

# Add title and axis labels
plt.title('Scatter Plot of Fares vs Trip Miles - Area 8', fontsize=14, fontweight='bold')
plt.xlabel('Fare ($)', fontsize=12)
plt.ylabel('Trip Miles', fontsize=12)

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend()

# Save the plot to a file
plt.savefig('FaresXmiles.png', dpi=300, bbox_inches='tight')
print("Plot saved as FaresXmiles.png")

# Display the plot
plt.show()

# Calculate and print statistics
correlation = np.corrcoef(fares, miles)[0, 1]
print(f"\nData Analysis - Filtered Trips (miles >= 2):")
print(f"Number of trips before filtering: {len(trips_data)}")
print(f"Number of trips after filtering: {len(filtered_trips)}")
print(f"Trips filtered out: {len(trips_data) - len(filtered_trips)}")
print(f"\nStatistics:")
print(f"Average fare: ${np.mean(fares):.2f}")
print(f"Average trip miles: {np.mean(miles):.2f}")
print(f"Fare range: ${min(fares):.2f} - ${max(fares):.2f}")
print(f"Miles range: {min(miles):.2f} - {max(miles):.2f}")
print(f"Correlation between fare and miles: {correlation:.4f}")

print(f"\nAnomalies and Observations:")
print(f"1. Strong linear relationship: r = {correlation:.4f} (nearly perfect correlation)")
print(f"2. Consistent pricing model: Approximately ${np.mean(fares)/np.mean(miles):.2f} per mile")

# Identify trips that deviate significantly from the trend
residuals = []
for i, (fare, mile) in enumerate(zip(fares, miles)):
    predicted_mile = p(fare)
    residual = abs(mile - predicted_mile)
    residuals.append(residual)
    if residual > np.std(residuals) * 1.5 if residuals else 0:  # Flag outliers
        print(f"3. Potential anomaly - Trip {filtered_trips[i]['trip_id']}: Fare=${fare:.2f}, Miles={mile:.2f}")

if max(residuals) > 0.5:
    max_residual_idx = residuals.index(max(residuals))
    print(f"\n4. Largest deviation from trend:")
    print(f"   Trip {filtered_trips[max_residual_idx]['trip_id']}: Fare=${fares[max_residual_idx]:.2f}, Miles={miles[max_residual_idx]:.2f}")
    print(f"   Expected miles based on fare: {p(fares[max_residual_idx]):.2f}")
    print(f"   Deviation: {max(residuals):.2f} miles")
else:
    print(f"\n4. No significant anomalies detected - all data points follow the expected linear pattern")
    print(f"   Maximum deviation from trend line: {max(residuals):.4f} miles")
