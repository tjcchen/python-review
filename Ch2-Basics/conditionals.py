#
# conditional structures
#

def main():
    x, y = 10, 100
    
    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"
        
    print(result)   # x is less than y
    
    # conditional statements let you use "a if c else b"
    result = "x is less than y" if x < y else "x is greater or equal to y"
    
    print(result)   # x is less than y
    
    # match-case makes it easy to compare multiple values( phthon 3.10 above )
    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":   # or
            result = (3, 4)      # tuple
        case _:                  # default
            result = -1
    print(result)   # (3, 4)

    
if __name__ == "__main__":
    main()
