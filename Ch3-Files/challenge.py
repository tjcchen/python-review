#
# dir & files creation challenge
#

import os
from os import path

def main():
  # create a directory and a file
  # solution 1:
  # newpath = "result/results.txt"
  # if not path.exists(newpath):
  #   os.makedirs(newpath)
  #
  # solution 2: 
  os.mkdir("result")
  myfile = open("result/results.txt", "w+")

  # write file header
  myfile.write("List all the files in current folder\n")
  myfile.write("------------------------------------\n")
  
  # write names to the file
  for file in os.listdir("./"):
    if path.isfile(file):
      myfile.write(file + "\n")
  
  # close the file when done
  myfile.close()
  
if __name__ == "__main__":
  main()
