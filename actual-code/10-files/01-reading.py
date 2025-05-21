file = open("test.txt")

print(file.read())
file.seek(0)


for line in file.readlines():
    print(line.strip())

file.seek(0)

line = file.readline()

total = 0

while line:
    total += len(line.strip())
    line = file.readline()

print(total)
file.close()