trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

TaxTrips = {
"miles": trip_durations,
"fares": trip_fares
}

print(TaxTrips)

print(f"The third trip waas {TaxTrips['miles'][2]} miles long.")
print(f"The fare for the third trip was ${TaxTrips['fares'][2]}.")