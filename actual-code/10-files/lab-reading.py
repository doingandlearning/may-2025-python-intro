file = open("event_log.txt")
door_file = open("door_log.txt", "a")
lines = file.readlines()

for line in lines:
    line_list = line.strip().split(" - ")
    if line_list[1].find("Door") >= 0:
        door_file.write(f"{line_list[1]} at {line_list[0]}\n")

file.close()