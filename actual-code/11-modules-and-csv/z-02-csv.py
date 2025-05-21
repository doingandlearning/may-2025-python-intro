import csv

with open("people.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    # print(header)
    for name, row, country in reader:
        print(f"{name} is from {country} and is sitting in row {row}")
    # for row in reader:
    #     print(f"{row[0]} is from {row[2]} and is sitting in row {row[1]}")