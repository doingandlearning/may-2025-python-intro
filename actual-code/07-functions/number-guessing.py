import random

number_to_guess = random.randint(1, 10)

count = 1

def print_feedback_on_guess(guess, actual):
    if guess > actual:
        print("You were too high")
    else:
        print("You were too low")

def get_int_from_user():
    while True:
        value = input("Guess a number: ")
        if value.isnumeric():
            return int(value)
        else:
            if value == "-1":
                return -1
            print("That wasn't a number. Try again.")

while count <= 4:
    guess = get_int_from_user()

    if guess == -1:
        print(f"Sssh! Don't tell anyone, the answer is {number_to_guess}")
        continue

    if guess == number_to_guess:
        print("Correct")
        break
    else:
        print("Wrong")
        print_feedback_on_guess(guess, number_to_guess)
        count += 1

print(f"Game over! You took {count} guesses.")