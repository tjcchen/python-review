#
# variables
#

# Basic data types in Python( 5 types ): Number, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 4.5, False] # sequence
mytuple = (0, 1, 2)                # sequence, immutable - cannot be changed
mydict = {"one": 1, "two": 2}      # map key to value

# print(myint)      # 5
# print(myfloat)    # 13.2
# print(mystr)      # This is a string
# print(mybool)     # True
# print(mylist)     # [0, 1, 'two', 4.5, False]
# print(mytuple)    # (0, 1, 2)
# print(mydict)     # {'one': 1, 'two': 2}

# re-declaring a variable works
# myint = "abc"
# print(myint)      # abc

# to access a member of a sequence type, use []
# print(mylist[2])  # two
# print(mytuple[1]) # 1

# use slices to get parts of a sequence, original mylist is [0, 1, 'two', 4.5, False]
# print(mylist[1:5])   # [1, 'two', 4.5, False] - from second item to fifth item
# print(mylist[1:5:2]) # [1, 4.5] - from second item to fifth item with a step 2

# you can use slices to reverse a sequence
# print(mylist[::-1])  # [False, 4.5, 'two', 1, 0]

# dictionaries are accessed via keys, original mydict is {'one': 1, 'two': 2}
# print(mydict["one"])   # 1

# ERROR: variables of different types cannot be combined
# print("string type" + 123)      # TypeError: can only concatenate str (not "int") to str
# print("string type" + str(123)) # string type123

# Global vs local variables in functions
def someFunc1():
  mystr = "def"
  print(mystr)
  
someFunc1()   # def
print(mystr)  # This is a string


def someFunc2():
  global mystr  # this will affect the global variable
  mystr = "def"
  print(mystr)
  
someFunc2()   # def
print(mystr)  # def

# delete a variable
del mystr
print(mystr)  # NameError: name 'mystr' is not defined
