import random
import datetime
import time

number_file = open("current_number.txt", "r+")

current_number = int(number_file.read())
next_number = current_number + 1
number_file.seek(0)
number_file.write(str(next_number))
number_file.close()


filename = f"{datetime.date.today()}-{current_number}-log.txt"

temp_log = open(filename, "a")
count = 0
while count < 10:
    temp = random.randrange(0, 300)
    now = datetime.datetime.now()
    temp_log.write(f"{now} - {temp}\n")
    if temp > 100:
        print("Alert on call team")
    time.sleep(1)
    count += 1

temp_log.close()
