# Calendar Generator

# Print a simple calendar for any month/year input by the user.

from datetime import datetime
import calendar

# year =2025
# month = 8

# print(calendar.month(year,month))



def print_calender(month,year):
    cal = calendar.TextCalendar(calendar.SATURDAY)
    cal_format = cal.formatmonth(month,year)
    return cal_format


year = int(input("Enter year : "))
month = int(input("Enter month (1-12): "))
print(print_calender(year,month))