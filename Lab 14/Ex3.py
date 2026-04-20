import json
import matplotlib.pyplot as plt
import pandas as pd

# Load the trip data from the JSON file
with open('Trips from area 8.json', 'r') as file:
    trips_data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(trips_data)

# Drop rows with NA/null values in the tips column
df = df.dropna(subset=['tips'])

# Group by payment method and sum the tips
tips_by_payment = df.groupby('payment_method')['tips'].sum()

# Create the histogram/bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(tips_by_payment.index, tips_by_payment.values, color='coral', edgecolor='black', alpha=0.7)

# Add title and axis labels
plt.title('Total Tips by Payment Method - Area 8', fontsize=14, fontweight='bold')
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Sum of Tips', fontsize=12)

# Add grid
plt.grid(True, axis='y', alpha=0.3)

# Display the plot
plt.show()
