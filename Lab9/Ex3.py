import csv
total_fare = 0
count = 0
mix_miles = 0

with open("taxi_100.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        fare = float(row["fare"])
        miles = float(row["Trip miles"])
        total_fare += fare
        count += 1
        mix_miles += miles

print(f"Total fare: {total_fare}")
print(f"Average fare: {total_fare / count if count > 0 else 0}")
print(f"Maximum trip miles: {max_miles}")