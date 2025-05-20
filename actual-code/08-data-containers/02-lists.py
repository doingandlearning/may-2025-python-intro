empty_list = []

print(empty_list)
print(type(empty_list))

beatles = ["George", "Paul", "John", "Ringo"]
print(beatles[0])
print(beatles[1:])
print(len(beatles))
beatles.append("Pablo")
print(beatles)
beatles.extend(["Gareth", "Fatima", "Batuhan"])
print(beatles)
beatles.remove("John")
print(beatles)
beatles.insert(2, "Samuel")
print(beatles)

print(beatles.index("Samuel"))
print(beatles.count("Batuhan"))

if "Kevin" in beatles:
    print("He is!")
else:
    print("Sadly, no.")

for member in beatles:
    print(f"{member} is in the Beatles - well done, them!")

