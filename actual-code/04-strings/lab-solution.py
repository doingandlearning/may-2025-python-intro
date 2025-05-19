original_string = "Kevin,Albus,Cunningham,42,Belfast,NI"
new_string = original_string.replace(",", " ")

print(f"Original string: {original_string}")
print(f"New string: {new_string}")

# first_name = input("What is your first name? ")
# family_name = input("What is your family name? ")
# # full_name = first_name + " " + family_name
# full_name = f"{first_name} {family_name}"
# print(full_name)

print(len(new_string))
# print(new_string.count(""))

print(new_string.find("Albus"))
print(new_string == "Hello World")
print(f"{new_string} - that was fun!")

value_in_km = int(input("What is the distance in km?"))

value_in_miles = value_in_km * 0.6214

print(f"{value_in_km}km is the same as {value_in_miles} miles")