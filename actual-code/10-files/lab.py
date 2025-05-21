import datetime

events = [
    "Door opened",
    "Lights on",
    "Projector turned on",
    "Students arrive",
    "Heading for coffee"
]

log = open("event_log.txt", "a")

for event in events:
    now = datetime.datetime.now()
    log.write(f"{now} - {event}\n")

log.close()

with open("event_log.txt", "a") as file:
    file.write("Doing this using with\n")
    for event in events:
        now = datetime.datetime.now()
        file.write(f"{now} - {event}\n")