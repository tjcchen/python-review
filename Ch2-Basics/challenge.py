#
# Palindrome Challenge
# Palindrom is a word, phrase, or sequence that reads the same backward as forward,
# e.g: madam or nurses run.
#

def main():
    # init answer value with empty string
    answer = ""
    
    # interact with users
    while (answer != "exit"):
        answer = input("Enter string to test for palindrome or 'exit': ")

        if answer == "":
            print("The input string cannot be empty!")
            continue
        
        result = False
        forwardanswer = answer.replace(" ", "").replace(",", "")
        reversedanswer = forwardanswer[::-1]
            
        if forwardanswer == reversedanswer:
            result = True
        elif answer == "exit":
            result = False
            break
        else:
            result = False
        
        print("Palidrome test: ", result)

    # exit the application when input answer is "exit"
    if answer == "exit":
        exit(0)


if __name__ == "__main__":
    main()
