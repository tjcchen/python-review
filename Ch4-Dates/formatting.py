#
# formatting time and date output
#

from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string to
    # control codes
    now = datetime.now()
    
    ##### Date Formatting #####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))   # The current year is: 2023
    print(now.strftime("%a, %d %B, %y"))             # Mon, 26 June, 23
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))  # Locale date and time: Mon Jun 26 20:29:10 2023
    print(now.strftime("Locale date: %x"))           # Locale date: 06/26/23
    print(now.strftime("Locale time: %X"))           # Locale time: 20:29:10
    
    ##### Time Formatting #####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p")) # Current time: 08:36:06 PM
    print(now.strftime("24-hour time: %H:%M:%S"))    # 24-hour time: 20:36:06
    
    
if __name__ == "__main__":
    main()