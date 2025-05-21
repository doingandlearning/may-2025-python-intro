#! /usr/local/bin/python3

empty_set = set()  # [] -> list(), () -> tuple()
print(empty_set)
print(type(empty_set))

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(len(basket))

for item in basket:
    print(item)

print("ice cream" in basket)

basket.add("ice cream")  # equivalent to list.append()
basket.add("ice cream")
basket.add("ice cream")

print(len(basket))
basket.update(["apricot", "mango", "grapefruit"])  # equivalent to list.extend()
print(len(basket))
print(basket)
basket.remove("ice cream")
print(basket)