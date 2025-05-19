savings = float(input("How much money is in your savings account? "))

if savings == 0:
    print("Oops! Try not to get any big bills.")
elif savings < 500:
    print("You're on your way - try to hit 1000!")
else:
    print("Phew! At least you have something!")