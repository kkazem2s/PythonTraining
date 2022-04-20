import calendar


def print_calendar(year, month):
    print(calendar.month(year, month))


def print_calendar_with_input():
    year = int(input("Input the year as an int:\n"))
    month = int(input("Input the month as an int:\n"))
    print(calendar.month(year, month))


print_calendar(1998, 5)
print("-----------")
print_calendar_with_input()
