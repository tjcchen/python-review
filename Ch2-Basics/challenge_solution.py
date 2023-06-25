#
# solutions to palindrome challenge
#

# check palindrome
def is_palindrome(teststr):
    # approach 1: calculate the reverse of the string
    reversestr = ""
    strindex = len(teststr) - 1
    while (strindex >= 0):
        reversestr += teststr[strindex]
        strindex -= 1
        
    if teststr == reversestr:
        return True
    else:
        return False
    
    # approach 2( advanced ): use the slice trick to reverse the string
    # if teststr == teststr[::-1]:
    #     return True
    # else:
    #     return False

# main entrypoint function
def main():
    run = True
    while (run):
        teststr = input("Enter string to test for palindrome or 'exit': ")
        
        # if the user types "exit" then quit the program
        if teststr == "exit":
            run = False
            break
        
        # convert the string to all lower case
        teststr = teststr.lower()
        
        # strip all the spaces and punctuation from the string
        # str.isalnum() returns True if all characters in the string are alphanumeric
        # and there is at least one character, False otherwise. 
        newstr = ""
        for x in teststr:
            if x.isalnum():
                newstr += x
                
        print("Palindrome test:", is_palindrome(newstr))


# run the program
if __name__ == "__main__":
    main()
