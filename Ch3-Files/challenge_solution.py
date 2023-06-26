#
# solution to file creation challenge
#

import os
from os import path

def main():
    totalbytes = 0
    
    # get a list of all the files in the current directory
    dirlist = os.listdir()
    for entry in dirlist:
        if path.isfile(entry):
            # add the file size to the total
            totalbytes += path.getsize(entry)
            
    # create a subdirectory called "results"
    os.mkdir("results")
    
    # create the output file
    resultsfile = open("results/results.txt", "w+")
    if resultsfile.mode == "w+":
        resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
        resultsfile.write("Files list:\n")
        resultsfile.write("--------------------\n")
        # write the results into the file
        for entry in dirlist:
            if path.isfile(entry):
                resultsfile.write(entry + "\n")
        # close the file when done
        resultsfile.close()
    
if __name__ == "__main__":
    main()
