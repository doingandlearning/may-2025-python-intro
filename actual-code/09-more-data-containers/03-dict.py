empty_dict = {}  # dict()
print(empty_dict)
print(type(empty_dict))

cities = {
    'Wales': 'Cardiff',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Switzerland': 'Bern'
}

print(cities)
print(cities["Wales"])
print(cities.get("Italy", "Not currently in our dictionary"))
print(cities.keys())
print(cities.values())
print(cities.items())

print("Paris" in cities)  # checks the keys and not the values

for country in cities:
    print(f"{country}'s capital is {cities[country]}")

for country, city in cities.items():
    print(f"{country}'s capital is {city}")


cities["Netherlands"] = "Amsterdam"
cities["Wales"] = "Swansea"








