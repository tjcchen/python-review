#
# Read and write files using the built-in Python file methods
#

def main():
    # Write
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w+") # w create a new file, + means if it doesn't exit, then we create one
    
    # Open the file for appending text to the end
    # myfile = open("textfile.txt", "a+") # a means append some new text
    
    # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some new text\n")
        
    # close the file when done
    # myfile.close()
    
    # ==============================================
    # Read
    myfile = open("textfile.txt", "r") # read does not need to close the file
    if myfile.mode == "r":
        # read all the content
        # contents = myfile.read()       # read all the content
        # print(contents)                # all the content from "textfile.txt" will be printed out

        # read by lines
        filelines = myfile.readlines()
        for x in filelines:
            print(x)

if __name__ == "__main__":
    main()
