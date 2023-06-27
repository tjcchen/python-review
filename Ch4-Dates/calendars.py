#
# calendars
#

import calendar

def main():
    # create a plain text calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2024, 1, 0, 0)
    print(str)   # will print out a text calendar on Sunday basis
    
    # create an HTML formatted calendar
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    str = hc.formatmonth(2024, 1)
    print(str)   # will print out a html calendar with table element
    
    # loop over the days of a month
    # zeros mean that the day of the week is in an overlapping month
    for i in c.itermonthdays(2024, 5):
        print(i) # 0, 0, 0, 1, 2, ..., 31, 0
    
    # The Calendar module provides useful utilities for the given locale,
    # such as the names of days and months in both full and abbreviated forms
    for name in calendar.month_name:
        print(name) # January, February, ..., December
        
    for day in calendar.day_name:
        print(day)  # Monday, Tuesday, ..., Sunday
        
    # Calculate days based on a rule: For example, consider a team meeting
    # on the first Friday of every month. To figure out what days that
    # would be for each month, we can use this script:
    print("Team meetings will be on (1st Friday of each month):")
    for m in range(1, 13):
        cal = calendar.monthcalendar(2024, m)
        weekone = cal[0] # calendar row 1, eg: [0, 0, 0, 1, 2, 3, 4]
        weektwo = cal[1] # calendar row 2, eg: [5, 6, 7, 8, 9, 10, 11]
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY] # calendar.FRIDAY = 4
        else:
            meetday = weektwo[calendar.FRIDAY]
        print(calendar.month_name[m], meetday) # eg: January 5, February 2, March 1, ...

if __name__ == "__main__":
    main()
