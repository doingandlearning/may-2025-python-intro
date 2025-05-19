command = input("What are we doing next? ")

if command == "quit":
    print("quit the program")
elif command == "look":
    print("Looking out")
elif command == "up" or command == "down":
    print("Up or down")
else:
    print("I don't know how to do that.")
    

match command:
    case "quit":
        print("quitting the program")
    case "look":
        print("looking around")
    case "up" | "down": # | <- pipe symbol is used for "or" here
        print("up or down")
    case _:
        print("I don't know how to do that.")