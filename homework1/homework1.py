# File: homework1.py

# --- Variables and Data Types ---
#For each variable given below:
#1. Print the variable.
#2. Print the data type of the variable.
#3. Leave a comment describing what kind of data it is.
#Example:

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number that has decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of items that are ordered and mutable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of key-value pairs

g =(1, 2)
print(g)
print(type(g)) # g is a tuple, a collection of items that are ordered and immutable

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of items that are ordered and mutable

i = True
print(i)
print(type(i)) # i is a boolean, a data type that can be either True or False

j = None
print(j)
print(type(j)) # j is a NoneType, a data type that represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of items that are ordered and mutable

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number that has decimals

# 1: How many different data types did you find? 
# I found 9 different data types
# 2: list all the data types you found.
# integer, float, complex number, string, list, dictionary, tuple, boolean, and NoneType.
# 3: what variables have the same data type?
# e and h are both lists, m and b are floats, d and l are strings, 
# 4: What was the data type of l? Why is it not an integer? What does str() do?
# the data type of l is a string because the str() function converts the integer 14 into a string.
# 5: Look up one more data type not given above. Repeat the same procedure

n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, a collection of unique items that are unordered and mutable

# Booleans

print(10 > 9) # True
print(10 == 9) # False
print(10 <= 9) # False
print(bool("abc")) # True
print(bool(123)) # True
print(bool(["apple", "cherry", "banana"])) # True
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) # False
print(bool("")) # False
print(bool(" "))   # True
print(bool( () )) # False
print(bool([] )) # False
print(bool( {} )) # False
print(bool(True and False)) # False
print(bool(True and True)) # True
print(bool(False and False)) # False
print(bool(True or False)) # True
print(bool(True or True)) # True
print(bool(False or False)) # False
print(bool(not(False)))#True
print(bool(not(True)))#False

# 1: What pattern do you notice about expressions returning true or false?
# Expressions that evaluate to a non-zero number, a non-empty string, list, tuple,
# or set or the boolean value True return True. Expressions that are empty or equal 0, or booleans
# that are false return False
#2: Which expressions surprised you about its result?
# at first 123 surprised me because I didn't realize what boolean functions recognized as true or false 
# other than inequalities, until I looked it up that nonzero integers are true and lists and strings containing
# items are also true
# 3: Create an expression not given above that returns True.
bool(5 > 3) # True, because 5 is greater than 3 and the bool() sees that as true as well
# 4: Create an expression not given above that returns False.
bool(2 == 3) # False, because 2 is not equal to 3

# Operators

print(10 + 5) # 15 addition
print(10 - 5) # 5 subtraction
print(2 * 4) # 8 multiplication
print(6 / 3) # 2.0 division - returns a float
print(5 % 2) # 1 modulus - returns the remainder of the division
print(3 ** 2) # 9 exponentiation - raises the number to the power of the other number
print(15 // 2) # 7 floor division - returns the largest integer less than or equal to the division result

# Comparison Operators

print(5 == 2) # false, equality comparison
print(10 != 10) # false, 10 is equal to 10
print(2 < 5) # true, less than comparison
print(12 > 5) # true, greater than comparison
print(5 <= 6) # true, less than or equal to comparison
print(1 >= 10) # false, greater than or equal to comparison

# Assignments Operators

x = 5

x += 5 # x = x + 5 ; 10
x -= 4 # x = x - 4 ; 6
x *= 3 # x = x * 3 ; 18

print(x) # 18

# 1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
#and returns true if both expressions are true.
bool(5 > 3 and 4 < 6) # True, because both expressions are true
bool(5 > 3 and 4 > 6) # False, because one expression is false

# 2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
#or returns true if at least one of the expressions is true.
bool(5 > 3 or 4 > 6) # True, because one expression is true
bool(5 < 3 or 4 > 6) # False, because both expressions are false

# 3. What does the operator not do? Write an expression that results in True. Write an expression that results in False.
# not negates the boolean value of an expression, making true false and false true.
bool(not(5 > 3)) # False, because 5 is greater than 3
bool(not(5 < 3)) # True, because 5 is not less than 3

#1. What is the difference between / and //?
# / performs standard division and returns a float, while // performs floor division and returns the largest integer less than or equal to the division result.
# 2. What is the difference between % and //?
# % returns the remainder of a division operation, while // returns the largest integer less than or equal to the division result.
# 3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
# modulus operator (%), for example, 10 % 3 returns 1 because 10 divided by 3 leaves a remainder of 1.
# 4. How do assignment operators work?
# Assignment operators perform an operation on a variable and then assign the result back to that variable. 
# For example, x += 5 adds 5 to the current value of x and assigns the result back to x.

#Strings

my_string = "hello"

print(my_string) # prints the entire string
print(my_string[0]) # prints the first character of the string, which is 'h
print(my_string[1]) # prints the second character of the string, which is 'e'
print(my_string[2]) # prints the third character of the string, which is 'l'
print(my_string[3]) # prints the fourth character of the string, which is 'l
print(my_string[4]) # prints the fifth character of the string, which is 'o
print(my_string[-1]) # prints the last character of the string, which is 'o
print(my_string[1:3]) # prints characters from index 1 to 2, which is 'el'
print(my_string[0:5:2]) # prints characters from index 0 to 4 with a step of 2, which is 'hlo'
print(len(my_string)) # prints the length of the string, which is 5
my_string += "goodbye" 
print(my_string) # prints the updated string, which is 'hellogoodbye'
my_string *= 7
print(my_string) # prints the string repeated 7 times

#1. slicing is when you return a portion of the string, and i sliced it for [1:3] and [0:5:2]

name = "Oski"
print("Hello, my name is", name) # prints "Hello, my name is Oski"
print(f"Hello, my name is {name}") # prints "Hello, my name is Oski"
#f strings are a way to format strings by embedding expressions inside string literals, using curly braces {}
# you dont need to use commas to separate variables and strings and it inserts the exact value of the variable
#f strings are useful and have different forms and manipulations you can do with them

# Terminal commands
# cd - current directory, used to change the current working directory
# ls - list, used to list files and directories in the current directory
# ls -a - list all, used to list all files and directories including hidden ones
# mkdir - make directory, used to create a new directory
# cat - concatenate, used to display the contents of a file
# pwd - print working directory, used to display the current working directory
# cd .. - change directory up one level, used to move up one directory level
# cd . - change directory to current directory, used to stay in the current directory
# cd ~ - change directory to home directory, used to navigate to the user's home directory
# cp - copy, used to copy files or directories from one location to another
# mv - move, used to move or rename files or directories
# rm - remove, used to delete files or directories
# clear - used to clear the terminal screen
# grep - global regular expression print, used to search for specific patterns in files or output

# 3 other commands not present are touch, 
# which creates a new empty file,
# echo, which displays a line of text or variable value,
# and rmdir, which removes an empty directory.
# the difference between ls and ls -a is that ls - a shows all files including hidden files,
# while ls only shows visible files.
# a hidden file is a file that is not normally visible in the file explorer or terminal,
# usually because its name starts with a dot (.) and is used for configuration or system purposes
# 3 other flags like -a are -l, which shows a detailed list of files with permissions, sizes, and modification dates,
# -h, which shows file sizes in a human-readable format (e.g., KB, MB),
# and -r, which lists files in reverse order.
