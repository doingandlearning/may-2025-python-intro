temperatures = (
        (10.05, '04/05/23', '12:00', 'Celsius'),
        (11.00, '04/05/23', '13:00', 'Celsius'),
        (12.34, '04/05/23', '14:00', 'Celsius'),
        (11.95, '04/05/23', '15:00', 'Celsius'),
        (9.25, '04/05/23', '16:00', 'Celsius'),
)


def write_to_csv(filename, headers, data):
    """
    Takes a collection of collections (tuples or lists) and writes them to csv.
    Accepts headers in the form of tuple or list

    :param filename: Name of file
    :param headers: A list/tuple of the headers
    :param data: A list or tuple of the rows of data
    :return: None
    """
    import csv
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for reading in data:
            writer.writerow(reading)

write_to_csv(filename="function_temperatures.csv",
             headers=("temperature", "date", "time", "unit"),
             data=temperatures
             )