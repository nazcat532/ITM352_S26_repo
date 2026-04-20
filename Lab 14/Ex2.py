import json
import matplotlib.pyplot as plt

# Load the trip data from the JSON file
with open('Trips from area 8.json', 'r') as file:
    trips_data = json.load(file)

# Extract trip miles
trip_miles = [trip['miles'] for trip in trips_data]

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(trip_miles, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

# Add title and axis labels
plt.title('Histogram of Trip Miles - Area 8', fontsize=14, fontweight='bold')
plt.xlabel('Trip Miles', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Add grid
plt.grid(True, axis='y', alpha=0.3)

# Display the plot
plt.show()
