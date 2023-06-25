#
# os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS
    print(os.name)   # posix
    
    # Check for item existence and type
    print("Item exists: ", str(path.exists("textfile.txt")))   # Item exists:  True
    print("Item is a file: ", path.isfile("textfile.txt"))     # Item is a file:  True
    print("Item is a directory: ", path.isdir("textfile.txt")) # Item is a directory:  False
    
    # Work with file paths
    print("Item's path: ", path.realpath("textfile.txt"))                       # Item's path:  /Users/chen/python-review/Ch3-Files/textfile.txt
    print("Item's path and name: ", path.split(path.realpath("textfile.txt")))  # Item's path and name:  ('/Users/chen/python-review/Ch3-Files', 'textfile.txt')

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(path.getmtime("textfile.txt"))   # 1687683048.127628
    print(t)                               # Sun Jun 25 16:50:48 2023
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) # 2023-06-25 16:50:48.127628
    
    # calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("Now is: ", datetime.datetime.now())                # Now is:  2023-06-25 17:45:28.007394
    print("It has been", td, "since the file was modified")   # It has been 0:54:39.879728 since the file was modified
    print("Or,", td.total_seconds(), "seconds")               # Or, 3279.879728 seconds
    
if __name__ == "__main__":
    main()