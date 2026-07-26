import matplotlib.pyplot as plt
from config import LOG_FILES, CHART_FILE

log_files = LOG_FILES


def generate_charts():

    info = warning = error = critical = 0

    for log_file in log_files:
        with open(log_file, "r") as file:

            for line in file:

                level = line.strip().split(" ", 3)[2]

                if level == "INFO":
                    info += 1
                elif level == "WARNING":
                    warning += 1
                elif level == "ERROR":
                    error += 1
                elif level == "CRITICAL":
                    critical += 1

    levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
    counts = [info, warning, error, critical]

    plt.figure(figsize=(6, 4))
    plt.bar(levels, counts)
    plt.title("Log Data Reader")
    plt.xlabel("Log Levels")
    plt.ylabel("Counts")

    plt.savefig(CHART_FILE)
    plt.close()

    print("Graph created successfully.")