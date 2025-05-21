def get_new_file_name():
    number_file = open("current_number.txt", "r+")
    current_number = int(number_file.read())
    next_number = current_number + 1
    number_file.seek(0)
    number_file.write(str(next_number))
    number_file.close()

    return f"{datetime.date.today()}-{current_number}-log.txt"
