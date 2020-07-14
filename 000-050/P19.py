"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    And on leap years, February twenty-nine days.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def is_leap(year):
    if year % 100 != 0:
        if year % 4 == 0:
            return True
    elif year % 400 == 0:
        return True
    return False

# Returns the weekday of the first day of year
def get_first_day(year):
    years = year - 1900
    if year >= 1904: # First leap year of the century 
        leap_years = (year - 1904) // 4 + 1
    else:
        leap_years = 0
    if is_leap(year):
        leap_years -= 1 # Do not count current leap year
    years -= leap_years
    days = years * 365 + leap_years * 366
    first_day = 1 # First day of that year was a monday
    day_index = (first_day + (days % 7)) % 7
    return day_index

# Returns the weekday of any day of 1900. daynum [0 - 364(365)]
def weekday_year(daynum, year):
    first_day = get_first_day(year) 
    day_index = (first_day + (daynum % 7)) % 7
    days_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',\
     4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    #return days_dict[day_index]
    return day_index

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_day_month = [sum(months[:i]) for i in range(len(months))]
#first_day_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_day_month_leap = [sum(months_leap[:i]) for i in range(len(months_leap))]
#first_day_month_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

sundays = 0

for year in range(1901, 2001):
    if is_leap(year):
        first_day_month_current = first_day_month_leap
    else:
        first_day_month_current = first_day_month
    for day in first_day_month_current:
        # day_index == 0 for sundays
        if weekday_year(day, year) == 0:
            sundays += 1

print('During the XXth century, there where', sundays, 'sundays on the 1st of the month')