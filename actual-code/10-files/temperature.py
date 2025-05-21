import random
import datetime
import time
from utils import get_new_file_name

filename = get_new_file_name()
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
