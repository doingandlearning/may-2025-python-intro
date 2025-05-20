import random

number_to_guess = random.randint(1, 10)

count = 1
guesses = []

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

def get_play_again():
    while True:
        value = input("Do you want to play again? (y/n)").lower()
        if value in ["y", "n"]:
            return value
        print("Not valid value - try y or n.")

while True:
    while count <= 4:
        guess = get_int_from_user()

        if guess == -1:  # magic number
            print(f"Sssh! Don't tell anyone, the answer is {number_to_guess}")
            continue

        guesses.append(guess)

        if guess == number_to_guess:
            print("Correct")
            break
        else:
            print("Wrong")
            print_feedback_on_guess(guess, number_to_guess)
            count += 1

    print(f"Game over! You took {count} guesses.")
    print(f"Here were your guesses: {guesses}")
    play_again = get_play_again()
    if play_again == "n":
        print("Thanks for playing.")
        break
    guesses.clear()




















