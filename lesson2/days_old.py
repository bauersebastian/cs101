__author__ = 'Sebastian'

def daysInMonth(year, month):
    leapyear = isLeapYear(year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        monthdays = 31
    elif month == 2 and leapyear == False:
        monthdays = 28
    elif month == 2 and leapyear == True:
        monthdays = 29
    elif month == 4 or month == 6 or month == 9 or month == 11:
        monthdays = 30
    return monthdays

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    monthdays = daysInMonth(year, month)

    if day == monthdays and month == 12:
                year = year + 1
                day = 1
                month = 1
    elif day < monthdays:
        day = day + 1
    else:
        day = 1
        if month <12:
            month = month + 1
        else:
            month = 1

    return year, month, day

def isLeapYear(year):
#Check if the given year is a leap year
#Pseudocode:
# if year is divisible by 4 then leap year
# else if year is divisible by 100 then common year
# else if year is divisible by 400 then leap year
# else common year
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def checkdate(year1, month1, day1, year2, month2, day2):
#Check if the first date is before the second date
    if year1<year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not checkdate(year2, month2, day2, year1, month1, day1)
    days = 0
    while checkdate(year1,month1,day1,year2,month2,day2):
        year1, month1, day1 = nextDay(year1,month1,day1)
        days = days + 1
    return days

def test():
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1
    assert nextDay(2013,1,1) == (2013,1,2)
    print 'test finished'

# test()

print daysBetweenDates(2004,7,31,2014,7,6)
