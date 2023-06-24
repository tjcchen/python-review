#
# loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    print(x)   # 0, 1 , 2, 3, 4
    x = x + 1
    
  # define a for loop
  for x in range(5, 10):
    print(x)   # 5, 6, 7, 8, 9

  # use a for loop over a collection
  days1 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days1:
    print(d)   # Mon, Tue, Wed, Thu, Fri, Sat, Sun
    
  # use the break and continue statements
  for x in range(5, 10):
    # if x == 7:   # when x equals to 7, it will break the loop
    #   break
    if x % 2 == 0: # when x modular 2 is equal to zero, then continue, continue means skip the rest part of code inside the loop and go back up to the top
      continue
    print(x)     # 5, 6 | 5, 7, 9
    
  # using the enumerate() function to get index
  days2 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days2):
    print(i, d)  # 0 Mon, 1 Tue, 2 Wed, 3 Thu, 4 Fri, 5 Sat, 6 Sun


if __name__ == "__main__":
  main()
