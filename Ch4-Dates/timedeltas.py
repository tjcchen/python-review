#
# timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    # construct a basic timedelta and print it( timedelta is a span of time )
    print(timedelta(days=365, hours=5, minutes=1))   # 365 days, 5:01:00
    
    # print today's date
    now = datetime.now()
    print("Today is", now)   # Today is 2023-06-27 09:45:02.942544
    
    # print today's date one year from now
    print("One year from now it will be", str(now + timedelta(days=365)))   # One year from now it will be 2024-06-26 09:45:02.942544
    
    # create a timedelta that uses more than one argument
    print("In two weeks and 3 days it will be", str(now + timedelta(weeks=2, days=3))) # In two weeks and 3 days it will be 2023-07-14 09:49:11.556998
    
    # calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was", s)   # One week ago it was Tuesday June 20, 2023
    
    ## How many days until April Fools' Day?
    today = date.today()
    afd = date(today.year, 4, 1)
    
    # if it has, use the replace() function to get the date for next year
    if afd < today:
        print("April Fools' Day already went by:", ((today - afd).days))      # April Fools' Day already went by: 87
        afd = afd.replace(year = today.year + 1)
        
    time_to_afd = afd - today
    print("It is", time_to_afd.days, "days until the next April Fool's Day!") # It is 279 days until the next April Fool's Day!
    
if __name__ == "__main__":
    main()