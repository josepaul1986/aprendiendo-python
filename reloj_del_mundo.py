import datetime

def show_menu():
    print("Please choose one of the following options: ")
    print("1. Check actual time")
    print("2. Check date and time")
    print("3. Check New York time")
    print("4. Check San Francisco time")
    print("5. Show menu again")
    print("6. Exit")

def show_time(msg, timezone_diff):
    time_zone = datetime.timezone(datetime.timedelta(hours=timezone_diff))
    output_time = datetime.datetime.now(time_zone).time()
    print(msg + output_time.strftime("%I:%M:%S %p"))

def show_date(msg, timezone_diff):
    time_zone = datetime.timezone(datetime.timedelta(hours=timezone_diff))
    output_date = datetime.datetime.now(time_zone)
    print(msg + output_date.strftime("%B %d, %Y %I:%M:%S %p"))

print("Welcome to World Clock")

repeat = "y"

while repeat == "y":
    show_menu()

    operation = "0"
    while operation != "6":
        operation = input(": ")

        if operation == "1":
            #1print(datetime.datetime.now().time())
            show_time("\nLocal time: ",-6)
        elif operation == "2":
            show_date("\nLocal date and time: ",-6)
        elif operation == "3":
            show_time("\nNYC time: ",-5)
        elif operation == "4":
            show_time("\nSan Francisco time: ",-8)
        elif operation == "5":
            show_menu()
        elif operation == "6":
            break
        else:
            print("\nError: Invalid option.")
    
    repeat = input("Do you want to continue? [y/n]").lower()
