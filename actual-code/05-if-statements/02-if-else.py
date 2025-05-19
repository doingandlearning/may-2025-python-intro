number_from_user = int(input("What is your number? "))

print("Getting started")

if number_from_user > 0:
    print(f"{number_from_user*2} is double the number you entered.")
else:
    print("Sorry. We don't like negative numbers.")

print("All done.")