snowing = input("Is it snowing? (y/n)")
temp = float(input("What is the temperature? "))

if temp < 0:
    print("It's freezing!")
    if snowing == "y":
        print("Put on boots")
    print("Time for hot chocolate")

print("Bye")

# <=
# >=
# !=