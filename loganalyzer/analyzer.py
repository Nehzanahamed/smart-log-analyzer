from config import LOG_FILES

log_files = LOG_FILES
report = "report.txt"

def summary():

    info = 0
    warning = 0
    error = 0
    critical = 0

    for log_file in log_files:
        with open(log_file, "r") as file:
            for line in file:

                line = line.strip()
                parts = line.split(" ", 3)

                level = parts[2]

                if level == "INFO":
                    info += 1

                elif level == "WARNING":
                    warning += 1

                elif level == "ERROR":
                    error += 1

                elif level == "CRITICAL":
                    critical += 1

    print("\n----REPORT----\n")
    print(f"INFO     : {info}")
    print(f"WARNING  : {warning}")
    print(f"ERROR    : {error}")
    print(f"CRITICAL : {critical}")


def search_logs():

    keyword = input("Enter the keyword to search: ").lower()

    print("\n---SEARCH RESULT---")

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                if keyword in line.lower():
                    print(line.strip())


def show_errors():

    print("\n----SHOW ERRORS----")

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                parts = line.strip().split(" ", 3)

                if parts[2] == "ERROR":
                    print(line.strip())


def filter_logby_time():

    start_time = input("Enter Start Time (HH:MM:SS): ")
    end_time = input("Enter End Time (HH:MM:SS): ")

    print("\n-----FILTER BY TIME-----")

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                parts = line.strip().split(" ", 3)

                if start_time <= parts[1] <= end_time:
                    print(line.strip())


def filter_logby_date():

    date = input("Enter Date (YYYY-MM-DD): ")

    print("\n-----FILTER BY DATE-----")

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                parts = line.strip().split(" ", 3)

                if parts[0] == date:
                    print(line.strip())


def most_error():

    errors = {}

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                parts = line.strip().split(" ", 3)

                if parts[2] == "ERROR":

                    message = parts[3]

                    if message in errors:
                        errors[message] += 1
                    else:
                        errors[message] = 1

    sorted_errors = sorted(errors.items(),
                           key=lambda item: item[1],
                           reverse=True)

    print("\n-----TOP 5 ERRORS-----")

    for message, count in sorted_errors[:5]:
        print(f"{message} : {count}")

def filter_log_level():

    level = input("entert the level(INFO/WARNING/ERROR/CRITICAL) : ").upper()
    found = False


    for log_file in log_files:
        with open(log_file,"r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(" ",3)

                if parts[2] == level:
                    print(line.strip())
                    found = True
    if not found:
        print("no logs found")

def sort_logs():

    logs = []    

    for log_file in log_files:
        with open(log_file,"r") as file:
            for line in file:
                line = line.strip()

                if line:
                    logs.append(line)

    print("\n1. oldest first / 2.newest first : ")
    choice = input("enter the choice (1 - 2) :")


    if choice == "1":
        logs.sort()

    elif choice == "2":
        logs.sort(reverse = True)

    else:
        print("invalid choice")
        return

    print("\n-----sorted logs----------")

    for log in logs:
        print(log)



