import datetime

print("This program outputs the day of the week for a given date.")
print()


def print_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    day_of_week = date.strftime("%A")  # %A: full name of the day of the week (e.g.Monday)
    print("The day of the week is:" + " " + str(day_of_week))


# main-------------------------------------------------------------
print_day_of_week(12, 12, 2050)
