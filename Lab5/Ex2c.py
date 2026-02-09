trip_duration = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

# Create a list of dictionaries, where each dictionary represents a trip.
trips = [
	{'duration': 1.1, 'fare': 6.25},
	{'duration': 0.8, 'fare': 5.25},
	{'duration': 2.5, 'fare': 10.50},
	{'duration': 2.6, 'fare': 8.05},
]
print("List of trip dictionaries:")
print(trips)

#trips = dict(zip(trip_duration, trip_fares))
#print ("\nTrips dictionary:")
#print(trips)

trip_num = input("What trip do you want? [1-4]: ")
trip_index = int(trip_num) - 1
selected = trips[trip_index]
# print(f"Duration: {selected['duration']} miles")
print(f"Fare: ${selected['fare']:.2f}")
