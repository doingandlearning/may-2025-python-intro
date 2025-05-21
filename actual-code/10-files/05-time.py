import datetime

print(datetime.date.today())
print(datetime.date.weekday(datetime.date.today()))

print(datetime.datetime.now())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%a, %d. %B %y %I:%M:%S"))

with open("log.txt", "a") as file:
    now = datetime.datetime.now()
    file.write(f"[{now}] - Writing to file")
