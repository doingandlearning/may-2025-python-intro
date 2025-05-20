
value_in_km = input("What is the distance in km?")

if not value_in_km.isalpha():
    if value_in_km.replace(".", "", 1).isnumeric():
        value_in_km = float(value_in_km)
        value_in_miles = value_in_km * 0.6214
        print(f"{value_in_km}km is the same as {value_in_miles} miles")
    else:
        print("That wasn't a valid number!")
else:
    print("Oi! Only give me whole positive numbers!")

