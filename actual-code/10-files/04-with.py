file = open("log.txt")
print(file.readlines())
file.close()

# Pythonic -> Idiomatic Python

with open("log.txt", "a") as file:
    file.write("I was here.\n")