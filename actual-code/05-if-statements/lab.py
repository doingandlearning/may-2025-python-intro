number = int(input("Give me a number: "))

if number > 0:
    print("It's positive")
elif number < 0:
    print("It's negative!")
else:
    print("It's zero!")

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")