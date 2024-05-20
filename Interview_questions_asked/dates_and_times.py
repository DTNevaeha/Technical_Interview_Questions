# Count the number of instances of a particular weekday in a given month and year

import calendar

def count_days(year, month, whichday):
    # Get the number of days in the month
    days = calendar.monthrange(year, month)[1]
    count = 0
    for i in range(1, days + 1):
        if calendar.weekday(year, month, i) == whichday:
            count += 1
    return count

testyear = 2025
testmonth = 12
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
testday = 0

# Test the function
print(count_days(testyear, testmonth, testday))