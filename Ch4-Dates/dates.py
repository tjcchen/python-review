#
# dates
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is", today)   # Today's date is 2023-06-26
    
    # Print out the date's individual components
    print("Date components:", today.day, today.month, today.year)   # Date components: 26 6 2023
    
    # Retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is:", today.weekday())   # Today's weekday # is: 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Which is a", days[today.weekday()])        # Which is a Monday
    
    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is:", today)     # The current date and time is: 2023-06-26 19:55:19.284407
    
    # Get the current time
    t = datetime.time(datetime.now())
    print("The current time is:", t)                  # The current time is: 19:58:27.295464

if __name__ == "__main__":
    main()
