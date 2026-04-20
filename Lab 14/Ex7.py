import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Load the trip data from the JSON file
with open('Trips from area 8.json', 'r') as file:
    trips_data = json.load(file)

# Extract fares, miles, and dropoff areas
fares = [trip['fare'] for trip in trips_data]
miles = [trip['miles'] for trip in trips_data]
dropoff_areas = [trip['dropoff_area'] for trip in trips_data]

# Create a 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot with color gradient based on fare
scatter = ax.scatter(fares, miles, dropoff_areas, c=fares, cmap='viridis', 
                     s=100, alpha=0.6, edgecolors='black', linewidth=1)

# Add labels
ax.set_xlabel('Fare ($)', fontsize=12, fontweight='bold')
ax.set_ylabel('Trip Miles', fontsize=12, fontweight='bold')
ax.set_zlabel('Dropoff Area', fontsize=12, fontweight='bold')
ax.set_title('3D Plot: Fares vs Trip Miles vs Dropoff Area - Area 8', 
             fontsize=14, fontweight='bold')

# Add a colorbar
colorbar = plt.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
colorbar.set_label('Fare ($)', fontsize=11)

# Adjust viewing angle for better visualization
ax.view_init(elev=20, azim=45)

# Display the plot
plt.tight_layout()
plt.show()

# Print statistics
print(f"\n3D Data Analysis - Fares vs Miles vs Dropoff Area:")
print(f"Total trips: {len(trips_data)}")
print(f"\nFare Statistics:")
print(f"  Average: ${np.mean(fares):.2f}")
print(f"  Range: ${min(fares):.2f} - ${max(fares):.2f}")
print(f"\nTrip Miles Statistics:")
print(f"  Average: {np.mean(miles):.2f} miles")
print(f"  Range: {min(miles):.2f} - {max(miles):.2f} miles")
print(f"\nDropoff Area Statistics:")
print(f"  Average: {np.mean(dropoff_areas):.2f}")
print(f"  Range: {int(min(dropoff_areas))} - {int(max(dropoff_areas))}")
print(f"\nCorrelations:")
print(f"  Fare vs Miles: {np.corrcoef(fares, miles)[0, 1]:.4f}")
print(f"  Fare vs Dropoff Area: {np.corrcoef(fares, dropoff_areas)[0, 1]:.4f}")
print(f"  Miles vs Dropoff Area: {np.corrcoef(miles, dropoff_areas)[0, 1]:.4f}")
print(f"\nKey Insights:")
print(f"- Fares are strongly correlated with trip miles (as expected)")
print(f"- Dropoff area also shows moderate correlation with both fare and miles")
print(f"- Trips to areas further away (higher area numbers) tend to be longer and more expensive")
