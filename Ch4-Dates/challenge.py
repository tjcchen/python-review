#
# date & time challenge - calculate how many days of a specific weekday are within a month
#

import calendar

# This function counts the number of the given weekday for the
# specified year and month and returns the result
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

# Main Entry Point Function
def main():
    print("---Day Counter Program---\n")
    
    run = True
    while (run):
        try:
            print("Which day of the week do you want to count?")
            for idx, day in enumerate(calendar.day_name):
                print(str(idx) + ": " + str(day))
            print("Or 'exit' to quit")
            
            theday = input("? ")
            if theday == "exit":
                run = False
                break
            
            day = int(theday)
            
            yearstr = input("Enter year: ")
            year = int(yearstr)
            
            monthstr = input("Enter month: ")
            month = int(monthstr)
            
            result = countdays(year, month, day)
            print("There are", str(result), calendar.day_name[day] + "s", "in the month and year specified")
            print("----------\n")     
        except Exception as e:
            print(e)
            print("Sorry, that's not valid input")
            
# Execute the Main Function
if __name__ == "__main__":
    main()
