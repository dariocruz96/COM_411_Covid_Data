def welcome():

    message = "COVID-19 (January) Data"
    for i in range(len(message)):
        print("-", end="")
    print(f'\n{message}')
    for i in range(len(message)):
        print("-", end="")
    print()


def error(msg):

    print(f'Error! {msg}')


def progress(operation, value):

    status = 0
    if value == 0:
        status = "has started"
    elif 0 < value < 100:
        status = f"is in progress ({value}% completed)"
    elif value == 100:
        status = "has completed"
    print(f'{operation} {status}')


def menu(variant=0):

    if variant == 0:
        print("[1] Process Data\n"
              "[2] Visualise Data\n"
              "[3] Export Data\n"
              "[4] Exit")
        variant = int(input())
        if 4 >= variant > 0:
            return variant

    elif variant == 1:
        print("[1] Record by Serial Number\n"
              "[2] Records by Observation Date\n"
              "[3] Group Records by Country / Region\n"
              "[4] Summarise Records")
        variant = int(input())
        if 4 >= variant > 0:
            return variant

    elif variant == 2:
        print("[1] Country/Region Pie Chart\n"
              "[2] Observations Chart\n"
              "[3] Animated Summary")
        variant = int(input())
        if 3 >= variant > 0:
            return variant

    elif variant == 3:
        print("[1] All Data\n"
              "[2] Data for Specific Country/Region")
        variant = int(input())
        if 2 >= variant > 0:
            return variant


def total_records(num_records):

    print(f"There are {num_records} records in the data set.")


def serial_number():

    print("Please enter a serial number for a record")
    number = int(input())
    return number


def observation_dates():

    observation_dates_list = []
    print("Please enter some observation dates(in format mm/dd/yyyy, X - finish)")
    while True:
        date = input()
        if date.lower() == "x":
            break
        elif len(date) == 10:
            observation_dates_list.append(date)
        else:
            print("Please enter a valid date")
    return observation_dates_list


def display_record(record, cols=None):

    if cols is None:
        print(record)
    else:
        for i in cols:
            display_record(record[i])


def display_records(records, cols=None):

    for i in records:
        if cols is None:
            display_record(i)
        else:
            display_record(i, cols)