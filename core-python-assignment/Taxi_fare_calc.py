def calculate_fare(distance):
    base_fare = 50
    distance_rate = 10
    return base_fare + (distance * distance_rate)

trips = [5, 10, 3]
total = 0
for i, dist in enumerate(trips, start=1):
    fare = calculate_fare(dist)
    total += fare
    print("Trip", i, ":", "$" + str(fare))
print("Total Fare:", "$" + str(total))
