from analyzer import *
from reports import *
from charts import *

while True:

    print("\n-----LOG ANALYZER-----")
    print("1. Show Summary")
    print("2. Search Logs")
    print("3. Show Errors")
    print("4. Filter Log by Time")
    print("5. Filter Log by Date")
    print("6. Most Error")
    print("7. Export CSV")
    print("8. Export HTML")
    print("9. Graph Create")
    print("10.filter_log_level")
    print("11.sort logs")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        summary()

    elif choice == "2":
        search_logs()

    elif choice == "3":
        show_errors()

    elif choice == "4":
        filter_logby_time()

    elif choice == "5":
        filter_logby_date()

    elif choice == "6":
        most_error()

    elif choice == "7":
        export_csv()

    elif choice == "8":
        export_html()

    elif choice == "9":
        generate_charts()

    elif choice == "10":
        filter_log_level()

    elif choice == "11":
        sort_logs()

    elif choice == "12":
        print("Log Analyzer Exit")
        break

    else:
        print("Invalid Choice")