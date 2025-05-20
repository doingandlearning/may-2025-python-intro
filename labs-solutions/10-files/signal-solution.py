from datetime import datetime

# Step 1: Collect signal values from user
print("Enter signal values (type 'done' to finish):")

readings = []
while True:
    user_input = input("> ")
    if user_input.lower() == "done":
        break
    if user_input.replace(".", "", 1).isdigit():
        value = float(user_input)
        timestamp = datetime.now()
        readings.append((timestamp, value))
    else:
        print("Invalid input. Please enter a number or 'done'.")
        continue

# Step 2: Write the readings to a file
filename = "signal_log.txt"
with open(filename, "w") as f:
    for ts, value in readings:
        f.write(f"{ts} | {value}\n")

print(f"Data saved to {filename}")

# Step 3 (Extension): Read the data back and parse
print("\nReading from log:")

with open(filename, "r") as f:
    for line in f:
        ts_str, value_str = line.strip().split(" | ")
        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S.%f")
        value = float(value_str)
        print(f"At {ts}, signal was {value}")
