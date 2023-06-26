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
  # solution 2: 
  
  totalbytes = 0
  
  # create dir and open file for writing
  os.mkdir("results")
  resultsfile = open("results/results.txt", "w+")
  
  # write file header
  resultsfile.write("List all files:" + "\n")
  resultsfile.write("-----------------------------\n")
  
  # write names to the file
  for entry in os.listdir("./"):
    if path.isfile(entry):
      resultsfile.write(entry + "\n")
      totalbytes += path.getsize(entry)
  
  resultsfile.write("-----------------------------\n")
  resultsfile.write("Total bytes: " + str(totalbytes) + " bytes")
  
  # close the file when done
  resultsfile.close()
  
if __name__ == "__main__":
  main()
