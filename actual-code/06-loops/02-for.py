print("I'm doing important work!")

for _ in range(0, 10):
    print("Hello!")

for number in range(10):
    print(number)

print("I'm doing even more important work!")

for experiment in range(0, 100):
    if experiment == 47:
        print("Got it!")
        break
    else:
        print(f"Tried {experiment} - it wasn't the one!")


for num in range(100):
    if num % 2 == 0:
        print("Skipping because it is even")
        continue
    print(num)