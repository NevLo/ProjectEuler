# Project Euler problem 19

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
if __name__ == "__main__":
    numSundays = 0
    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day = 1
    year = 1
    for i in range(1,len(months)+1):
        day+=months.get(i)
    if(day % 7 == 0):
        numSundays += 1
    for i in range(100):
        for j in range(1,len(months)+1):
            if(j == 2 and year % 4 == 0 and year % 100 != 0):
                day+1
            day += months.get(j)

            if(day % 7 == 0):
                numSundays += 1
        year += 1
    dayOfTheWeek = day % 7
    print(f"The number of 1st of the months on sunday between 1/1/1901 - 12/31/2000 is: {numSundays}")