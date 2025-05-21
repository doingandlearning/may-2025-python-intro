import csv

with open("people.csv", "a") as file:
    writer = csv.writer(file)
    while True:
        name = input("Name: ")
        seat = input("Row: ")
        country = input("Country: ")

        writer.writerow([name, seat, country])

        go_again = input("Continue? ")
        if go_again == "n":
            break