string_1 = "G' \n"
string_2 = "day"
string_3 = string_1 + string_2

print(string_3)
print(len(string_1), len(string_2), len(string_3), len(string_1) + len(string_2))

# indexable
my_great_string = "This is a0string. Strings are great. I like strings a lot."
#                  0123456789

print(my_great_string[5]) # one number, one character
print(my_great_string[5:])  # number + colon, from there up to the end
print(my_great_string[5:9])
print(my_great_string[5:15:3])

print(my_great_string[:10])
print(my_great_string[::2])
print(my_great_string[::-1])