empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

fib_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)  # Fibonacci numbers
print(fib_tuple[0])
print(fib_tuple[1:4])
print(fib_tuple[2:])
print(fib_tuple[:5:2])
print(len(fib_tuple))

print(fib_tuple.count(100))
print(fib_tuple.index(34))  # if it's not there, it crashes!

value = 35
if value in fib_tuple:  # check for membership!
    print(fib_tuple.index(value))
else:
    print("Not in tuple.")

for num in fib_tuple:
    print(num)


people = ("Richard", "Matheiu", "Maria Christina", "Maxime")
places = ("France", "Germany", "Italy", "UK")
number = (1,2,3,4,5)

test_tuple = (people, places, number)
print(test_tuple[0][3], test_tuple[1][0], test_tuple[2][3])