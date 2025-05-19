age = int(input("What is your age? "))
status = None

if age > 12 and age < 20:
    status = "teenager"
else:
    status = "not teenager"

print(status)
