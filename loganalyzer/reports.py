import csv
from config import *

log_files = LOG_FILES


def export_csv():

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

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Metric", "Count"])
        writer.writerow(["INFO", info])
        writer.writerow(["WARNING", warning])
        writer.writerow(["ERROR", error])
        writer.writerow(["CRITICAL", critical])

    print("CSV exported successfully.")


def export_html():

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

    with open(HTML_FILE, "w") as file:

        file.write("<html>\n")
        file.write("<head><title>Smart Log Analyzer Report</title></head>\n")
        file.write("<body>\n")
        file.write("<h1>Smart Log Analyzer Report</h1>\n")
        file.write("<table border='3'>\n")
        file.write("<tr><th>Metric</th><th>Count</th></tr>\n")
        file.write(f"<tr><td>INFO</td><td>{info}</td></tr>\n")
        file.write(f"<tr><td>WARNING</td><td>{warning}</td></tr>\n")
        file.write(f"<tr><td>ERROR</td><td>{error}</td></tr>\n")
        file.write(f"<tr><td>CRITICAL</td><td>{critical}</td></tr>\n")
        file.write("</table>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    print("HTML Report Generated Successfully!")



def generate_dashboard():

    total_logs = 0
    info = 0
    warning = 0
    error = 0
    critical = 0

    for log_file in LOG_FILES:
        with open(log_file, "r") as file:

            for line in file:
                total_logs += 1

                if "INFO" in line:
                    info += 1
                elif "WARNING" in line:
                    warning += 1
                elif "ERROR" in line:
                    error += 1
                elif "CRITICAL" in line:
                    critical += 1

    with open(DASHBOARD_FILE, "w") as file:

        file.write("<html><body>")
        file.write("<h1>Smart Log Analyzer Dashboard</h1>")
        file.write("<hr>")
        file.write(f"<h3>Total Logs : {total_logs}</h3>")
        file.write(f"<h3>INFO : {info}</h3>")
        file.write(f"<h3>WARNING : {warning}</h3>")
        file.write(f"<h3>ERROR : {error}</h3>")
        file.write(f"<h3>CRITICAL : {critical}</h3>")
        file.write("</body></html>")

    print("Dashboard Generated Successfully!")

generate_dashboard()   