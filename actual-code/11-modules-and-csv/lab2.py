import csv

data = []

with open("temperatures.csv") as file:
    reader = csv.reader(file)

    header_row = next(reader)

    for row in reader:
        data.append(row)

lower_bound = int(input("What is the lower bound you care about? "))

for reading in data:
    if float(reading[0]) > lower_bound:
        print(reading)

total = 0
for reading in data:
    total += float(reading[0])

print(f"{total/len(data)} is the average temperature")




