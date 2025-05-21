flights = {
    'London': ('EY123', 'Monday', '12:00', 'Geneva'),
    'Geneva': ('AI454', 'Tuesday', '13:00', 'London'),
    'Dublin': ('BA987', 'Wednesday', '14:00', 'Dublin'),
    'Seville': ('SA527', 'Thursday', '11:00', 'Cardiff'),
    'Cardiff': ('WA129', 'Friday', '10:00', 'Dublin')
}

"""
Print out all the keys.
Print out all the values.
Find the flight associated with a particular city (for example, Dublin).
Add a new flight for France to the dictionary and print out all the key-value pairs. The flight for France could be ('AF429', 'Saturday', '09:00', 'London').
Remove the flight from the dictionary for Cardiff and reprint all items
"""
#
# print(flights.keys())
# print(flights.values())
# print(flights["Dublin"])
# print(flights.get("Dublin"))
# flights["Paris"] = ('EZY123', 'Wednesday', '13:21', 'Marseille')
# print(flights)
#
# del flights["Cardiff"]
#
# print(flights)

# target_day = input("Enter a day to search for flights: ")

for city, flight in flights.items():
    print(city)
    print(flight[0])
    print(flight[1])

name, age  = ("Kevin", 42)

print(f"{name} is {age}")

# for city, (flight_no, day, time, dest) in flights.items():
#
#     if day.lower() == target_day.lower():
#         print(f"{city} → {dest} at {time} [{flight_no}]")
