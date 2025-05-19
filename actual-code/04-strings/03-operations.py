msg = "Hello world"

# method -> function / operation
print(msg.replace("Hello", "Goodbye"))
print(msg.replace("l", "1", 2))

print(msg.find("cruel"))

print("Hello" == "Goodbye") # tests for equality
print("Hello" != "Goodbye") # tests for inequality

print(msg.startswith("Hello"))
print(msg.isupper())
print(msg.upper().isupper())
print(msg)