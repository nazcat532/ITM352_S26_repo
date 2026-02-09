trip_duration = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

# Create a list of dictionaries, where each dictionary represents a trip.
trips = [
	{'duration': 1.1, 'fare': 6.25},
	{'duration': 0.8, 'fare': 5.25},
	{'duration': 2.5, 'fare': 10.50},
	{'duration': 2.6, 'fare': 8.05},
]

trips = dict(zip(trip_duration, trip_fares))
print ("\nTrips dictionary:")
print(trips)

print(f"The third trip was {list(trips.keys())[2]} miles long.")
print(f"The fare for the third trip was ${list(trips.values())[2]}.")