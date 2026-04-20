import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the taxi trips data
df = pd.read_csv('taxi trips Fri 7_7_2017.csv')

# Create a crosstab (contingency table) of pickup and dropoff areas
heatmap_data = pd.crosstab(df['pickup_community_area'], df['dropoff_community_area'])

# Create the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt='d', cbar_kws={'label': 'Number of Trips'})

# Add title and labels
plt.title('Heatmap of Taxi Trips: Pickup vs Dropoff Community Areas\nFriday 7/7/2017', 
          fontsize=14, fontweight='bold')
plt.xlabel('Dropoff Community Area', fontsize=12, fontweight='bold')
plt.ylabel('Pickup Community Area', fontsize=12, fontweight='bold')

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print statistics
print(f"\nHeatmap Data Analysis:")
print(f"Total trips: {len(df)}")
print(f"Unique pickup areas: {df['pickup_community_area'].nunique()}")
print(f"Unique dropoff areas: {df['dropoff_community_area'].nunique()}")
print(f"\nPickup area distribution:")
print(df['pickup_community_area'].value_counts().sort_index())
print(f"\nDropoff area distribution:")
print(df['dropoff_community_area'].value_counts().sort_index())
print(f"\nTop 5 Routes (pickup -> dropoff):")
route_counts = df.groupby(['pickup_community_area', 'dropoff_community_area']).size().reset_index(name='count')
print(route_counts.nlargest(5, 'count'))
