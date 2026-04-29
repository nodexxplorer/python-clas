# def my_function():
#     print("Hello from David!")
    
# # my_function()

# # def my_func(how_are_you):
# #     print("Hello From My Function!")
# #     print(f"I'm {how_are_you}")

# # my_func("fine, thanks!")
#  def my_func():
#     print("thank you for subscribing to python")


# a = 30.4
# print(a)
# print(type(a))
# it has a dynamic typing
# intenstive standard library: Python comes with an intensive library that provided rules and functions for a variety of task.
# Cross platform: python runs on various operating systems
# Community and ecosystem: Python has a large and active community
# Educational use: Python is used as a teaching language in schools


# Uses of python
# python is used to build backend for facebook and goggle
# used in machine learning and ai automation
# used for IOT

# IDE is a toolbox that offers development tools like write, debug and test to developers saving them a lot of time. it makes programming easy.
# Data and Data types
# data are raw facts that can be coolected and processed in the computer
# Data type are types of data
# string (str)
# integer (int)
# complex number
# boolean (bool)
# float
#  string: "",'',"""" (str)
# print(type(12))
# a = 20.0
# b = 100
# d42367 = a>b
# print(c)
# print(type(d42367))

# Variables are storage location area or reserved spaces in memory.
# examples of variable
# z,b, c are variables

# Variables are the name  of the memory locator. it is used to store data. it is a container.

# naming rules of variables 
# variable names cant start with a digit 
# they are case sensitive
# keywords cannot be used as variables names
  
#   type conversion
# this is the act of converting from one type to another. e.g from string to int, float to int and vice versa
# int()
# float()
# str()
# bool()

# a = 40.6
# a = str (a)
# print(a)
# print(type(a))

# a = "2"
# b = "20"
# c = int(a) - int(b)
# print(c)


# Arithmetic Operator

# exponential operator
# print(10**3)
# print(2**5)

# floor division
# print(10//3)
# print(10//2)

# division
# print(10/3)
# print(10/2)

# multiplication
# print(10*2)
# print(34*4*48)

# addition
# print(10+2)
# print(int(30.4+5+1))

# sustraction
# print(10-2)
# print(int(30.4-5-1))

# modules
# print(10%3)

# Relational / Comparison Operator is used  to compare two values or expressions, returning a Boolean value (true / false)

# greater than
# print(10>2)
# print(29>60)

# less than
# print(10<2)
# print(10<60)

# greater than or equal to
# print(10>=2)
# print(10>=10)
# print(10>=60)


# less than or equal to
# print(10<=2)
# print(10<=10)
# print(10<=60)

# equal to
# print(10==2)
# print(10==10)
# print(60.1==60)


# not equal to
# print(10!=2)
# print(10!=10)
# print(60.3!=60)

# Logical Operators combine conditional statements and return a Boolean value (True or False)


# and
# T and T = True
# T and F = False
# F and T = False
# F and F = False

# print(10>2 and 10<20)
# print(10>2 and 100<20)
# print(10<2 and 10<20)
# print(10<2 and 100<20)

# or
# T or T = True
# T or F = True
# F or T = True
# F or F = False

# print(10>2 or 10<20)
# print(10>2 or 10<5)
# print(10<2 or 10>20)
# print(10<2 or 100<20)

# not
# T not T = False
# T not F = True
# F not T = True
# F not F = True

# print(10>2 and not 10<20)
# print(10>2 and not 10<5)
# print(10>2 and not 10>20)
# print(10>2 and not 100<20)

# Assignment operator are symbols used in programming to store values in variables, with the basic operator being the equals sign (=).

# Examples of assignment operators:
# = (simple assignment)
# += (add and assign)
# -= (subtract and assign)
# *= (multiply and assign)
# /= (divide and assign)
# %= (modulo and assign)

# a = 23
# print(a)


# Input and F.string 
# 
# Input Function is The input() function in Python is used to get data from the user via the console.

# a = input("Write your first name:  ")
# b = input("write your last name: ")
# # a = int(a)
# # b = int(b)
# c = a + b
# print(c)

# name = input("What is your name? ") # Stored as a string
# age = int(input("How old are you? ")) # Converted to an integer for calculations
# dept = input("what course are you learning? ")
# print(name)
# print(age)
# print(dept)


# F-strings provide a concise and readable way to embed variables and expressions directly within a string. (f"")

# print(f"Hello, I am {name}! I am {age} years old. I'm learning {dept}.")

# assigment
# My name is (Desire Martins).

# I’m proud to announce that I am now a teenager. I clocked (13) years last week.
# I am a (girl), and I’m in (JSS3). My best subject is Basic Science. I have a love-hate relationship with Maths, and I hate Business Studies — passionately.
# (I do not have a best color) — I like every one of them. My best food is (rice and beans). I eat anything, but I can eat (rice and beans) for seven days straight.
# My best friend is (Adeola Adenuga), and my hobbies are (reading, playing games and cooking).

# print('Python is a "programming" language.')
# print('Python is a \'programming\' language.')

# import random
# secret_number = random.randint(1, 4)
# guess = int(input("Guess a number (1-4): "))

# if guess < secret_number:
#     print("Your guess is too low!")
# elif guess > secret_number:
#     print("Your guess is too high!")
# else:
#     print("Congratulations! You guessed the number!")

# print("Simple Calculator")

# a = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /, %, //): ")
# b = float(input("Enter second number: "))

# if op == "+":
#     print("Result:", a + b)
# elif op == "-":
#     print("Result:", a - b)
# elif op == "*":
#     print("Result:", a * b)
# elif op == "/":
#     print("Result:", a / b)
# elif op == "%":
#     print("Result:", a % b)
# elif op == "//":
#     print("Result:", a // b)
# else:
#     print("Invalid operator")





# Control Flow
# Control flow dictates the order in which individual statements, instructions, or function calls are executed in a program. While code typically runs sequentially (top-to-bottom), control flow statements—such as conditionals (if/else), loops (for/while), and branches (switch)—allow programs to make decisions, repeat actions, and jump to different sections, enabling dynamic behavior.
# Without it, every program would just run the same lines top to bottom every time.

# if / elif / else — Making Decisions
# The if statement evaluates a condition. If it is True, the indented block runs. If False, Python skips it.

# types of if / elif / else
# 1. if / else  (basic)
# 2. if / elif / else (multiple conditions)

# Basic(if/else)
# temperature = 30
# if temperature >= 30:
#     print("It's a hot day!")
# else:
#     print("It's not that hot.")

# temperature = int(input("Enter the temperature: "))
# if temperature > 30:
#     print(f"{temperature} is a hot!")
# else:
#     print(f"{temperature} is not that hot.")

# score = int(input("Enter your score: "))
# if score >= 50:
#     print(f"You passed with a score of {score}!")
# else:
#     print(f"You failed with a score of {score}!")

# 5, you passed


# if / elif / else — Multiple Conditions
# elif is short for "else if". Python checks conditions in order and runs ONLY the first matching block. Once a match is found, the rest are skipped.

# score = int(input("Enter your score: "))
# if score >= 70:
#     print(f"You scored {score} and got an A!")
# elif score >= 60:
#     print(f"You scored {score} and got a B!")
# else:
#     print(f"You scored {score} and failed.")

# score = int(input("Enter your score: "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
 
# print(f"Score: {score}  Grade: {grade}")  


# While and for loop

# while Loops — Repeat While True
# A while loop runs its block repeatedly for as long as its condition is True. Use it when you do not know in advance how many iterations you need.


# count = 0
# while count > 100:
#     print(count)
#     # count -= 1
#     break

# age = int(input("Enter your age: "))
# while age < 0 or age > 120:
#     print("Invalid. Please enter 0-120.")
#     age = int(input("Enter your age: "))
# print(f"Age set to: {age}")


# for char in "Python":
#     if char == "n":
#         break # Loop terminates when 'n' is reached
#     print(char)

    # A for loop iterates over each item in a sequence (list, string, range, etc.) and executes its block once per item. Use it when you know what you are looping over.

    
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I like {fruit}")
 
# Loop over a string
# for letters in "Python":
#     print(letters)

# for i in range(0,10,4):
#     print(i)


# total = 0
# for n in range(1, 101):
#     # total += n
# print(f"1+2+...+100 = {total}")

# students = ["Fortune", "Ada", "Linus", "Grace"]
# scores = [80, 75, 90, 85]
 
# for index, (name, score) in enumerate(zip(students, scores), start=1):
    # print(f"{index}. {name} - Score: {score}/100")

# for name, score in zip(students, scores):
#     print(f"{name}: {score}/100")



# Arrays
# An array is an ordered collection or arrangement of data elements, typically of the same type, identified by numerical indices, usually starting at zero.
# it is denoted with the square bracket "[]"

# where Array is used 

    # Structure: Elements are stored in contiguous memory, allowing for efficient access using integer indexes.

    # Data Types: In many languages, arrays are designed to hold elements of the same data type.Indexing: In most programming languages, including JavaScript and Python (lists), the first element is at index [0].

    # Use Cases: Used in programming for ordered data.

    # Alternative Definition: More broadly, an array refers to an impressive, large display, or orderly arrangement of people or objects

# types of arrays
# 1. one-Dimension Array: This is a single row of items, like a shopping list or a row of lockers. You only need one number (an index) to find something.
# Example: [ "Apple", "Banana", "Cherry" ]

# 2. Multi-Dimensional Array: This is an "array of arrays." The most common is 2D, which looks like a table with rows and columns. To find a value, you need two numbers: the row and the column.Example (A 2x3 Grid):[
#   [10, 20, 30],  // Row 0
#   [40, 50, 60]   // Row 1
# ]


# Break and continue
# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement.

# Pass is used to tell the complier to do nothing

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# for char in "Python":
#     if char == "n":
#         break # Loop terminates when 'n' is reached
#     print(char)

# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
#     my_function()
#     # my_func()

# for char in "Python":
#     if char == "n":
#         pass # Loop terminates when 'n' is passed
#     print(char)


# Functions

# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. A function is a named, reusable block of code that performs a specific task. 

# Define the function with "def" keyword
# def greet():
#     print("Hello!")
#     print("Welcome to Python.")

# # Call the function
# greet()

# def my_function():
    # print("Hello from David!")
    
# my_function()

# def my_func(how_are_you):
#     print("Hello From My Function!")
#     print(f"I'm {how_are_you}")

# my_func("fine, thanks!")

# my_func("fine, thanks!")
# def my_func():
    # print("thank you for subscribing to python")

# input("this is my function class in python class, Im using python 3.13.5 Press Enter to continue...")
# my_function()
# my_func()

# when defining the function what you put in the bracket is the parameter, but when calling the function what you put in the bracket is an argument. you can have multiple parameters 


# def introduce(name, age, city):
#     print(f"I am {name}, {age} years old, I am from {city}.")
 
# introduce("Fortune", 20, "Lagos")
# introduce("Ada", 36, "London")
# introduce(input("my name is? "), input("my age is? "), input("i am from? "))


# def add(a, b):
#     return a + b          # sends result back
 
# result = add(10, 5)
# print(result)             # 15
# print(add(3, 4) * 2)      # 14 — use return value directly
# print(result * add(3, 4) * 2) 


# def absolute_value(n):
#     if n >= 0:
#         return n          # exits here for positive numbers
#     return -n             # only reached for negative numbers
 
# print(absolute_value(7))   # 7
# print(absolute_value(3))  # 3


# Local and Global Variables
# A variable created inside a function is local only when it exists within that function and disappears when the function ends. A variable outside all functions is global because it is accessible everywhere.

# x = 10

# def david():
#     y = 50
#     print(x)
#     print(y)
# david()

# print(x)


# for i in range(1, 31):
#     if i % 15 == 0:    print("FizzBuzz")
#     elif i % 3 == 0:   print("Fizz")
#     elif i % 5 == 0:   print("Buzz")
#     else:              print("🤣")


# for row in range(1, 6):
    # print("^" * row)


# def calculator():
#     print("simple calculator")
    
#     def km_to_miles(km):    return km * 0.621371
#     def kg_to_lbs(kg):      return kg * 2.20462
#     def celsius_to_f(c):    return (c * 9/5) + 32
#     def add(a, b):  return a + b
#     def substrate(a, b):  return a - b
#     def multiple(a, b): return a * b
#     def divide(a, b): return a / b if b != 0 else "Error: Division by zero"
#     def floordivide(a, b): return a // b
#     def module(a, b): return a % b
#     def complex(a, b, c): return (a + b) * c
    
#     while True:
#         print("\n 1) km->miles  2) kg->lbs  3) C->F 4) Addition  5) Subtraction  6) Multiplication  7) Division  8) Floor Division  9) Module  10) Complex  0) Quit")
#         choice = input("Choice: ")
        
# # """ 1)\

#         if choice == "0": 
#             break
#         elif choice == "1":
#             value  = float(input("Value: "))
#             km_to_miles(value)
#             print(km_to_miles(value))
#         elif choice == "2":
#             value  = float(input("Value: "))
#             kg_to_lbs(value)     
#             print(kg_to_lbs(value))
#         elif choice == "3":
#             value  = float(input("Value: "))
#             celsius_to_f(value)
#             print(celsius_to_f(value))
#         elif choice == "4":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(add(a, b))
#         elif choice == "5":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(substrate(a, b))
#         elif choice == "6":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(multiple(a, b))
#         elif choice == "7":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(divide(a, b))
#         elif choice == "8":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(floordivide(a, b))
#         elif choice == "9":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             print(module(a, b))
#         elif choice == "10":
#             a = float(input("First value: "))
#             b = float(input("Second value: "))
#             c = float(input("Third value: "))
#             print(complex(a, b, c))

#         else:
#             print("Invalid choice")
# calculator()


        
#Data Structures
# Data structures organise multiple pieces of data in a single variable. Python has four essential built-in structures: list, dict, tuple, and set. Choosing the right one for the right job is a key skill. examples are:
# dict{}, list[], tuple(), set{}

# A list stores multiple items in order, allows duplicates, and can be modified. It is the most frequently used data structure in Python. 

# fruits  = ["apple", "banana", "cherry"]
# numbers = [10, 20, 30, 40, 50]
# mixed   = ["hello", 42, True, 3.14, None]  # different types allowed
# empty   = []
# print(mixed)


# Indexing allows you to retrieve a single element from a sequence using its position
# Zero-Based: Python starts counting at 0. The first item is at index 0, the second at 1, etc. 
# Negative Indexing: You can count from the end of a sequence using negative numbers. -1 refers to the last item, -2 to the second-to-last, and so on.
# Syntax: Use square brackets with the index number: sequence[index].

# colours = ["red", "green", "blue", "yellow", "purple"]
#            0       1       2        3          4
#           -5      -4      -3       -2         -1

# Single item access
# print(colours[-5])    
# print(colours[-3])    
# print(colours[1])     

# Slicing extracts a range of elements (a "slice") from a sequence, creating a new sequence of the same type.
# Syntax: sequence[start:stop:step].
# start: The index where the slice begins (inclusive). Defaults to 0.
# stop: The index where the slice ends (exclusive). Defaults to the length of the sequence.
# step (optional): The increment between each index. Defaults to 1.

# colours = ["red", "green", "blue", "yellow", "purple"]
#            0       1       2        3          4
#           -5      -4      -3       -2         -1

# slicing: list[start:stop:step]
# print(colours[1:4])   # Output: ['green', 'blue', 'yellow']
# print(colours[:3])    # Output: ['red', 'green', 'blue']
# print(colours[2:5])   # Output: ['blue', 'yellow', 'purple']
# print(colours[::2])   # Output: ['red', 'blue', 'purple']



# common list Method
# append(x) - this add one item to the end of the list. Example (L.append("mango"))
# insert(index, x) - this adds an item at a specific index. Example (L.insert(2, "mango"))
# extend(iterable) - this adds multiple items to the end of the list. Example (L.extend(["mango", "orange"]))
# remove(x) - this removes the first occurrence of an item from the list. Example (L.remove("mango"))
# pop([index]) - this removes and returns an item at a specific index. Example (L.pop(2))
# clear() - this removes all items from the list. Example (L.clear())
# index(x) - this returns the index of the first occurrence of an item. Example (L.index("mango"))
# count(x) - this returns the number of occurrences of an item. Example (L.count("mango"))
# sort() - this sorts the list in ascending order. Example (L.sort())
# reverse() - this reverses the order of the list. Example (L.reverse())
# sum() - this returns the sum of all items in the list. Example (L.sum())


# colours.append("mango")
# colours.insert(2, "mango")
# colours.extend(["lilac","peach", "gold"])
# colours.remove("red")
# colours.pop(2)
# colours.clear()
# colours.count("yellow")
# colours.sort()



# colours.pop(2)
# print(pop)
# print(colours) 

# students = ["Alice", "Bob", "Charlie"]
 
# students.append("Diana")              # ["Alice","Bob","Charlie","Diana"]
# students.insert(0, "Zara")            # ["Zara","Alice","Bob","Charlie","Diana"]
# students.remove("Bob")                # ["Zara","Alice","Charlie","Diana"]
# removed = students.pop()              # removes "Diana"
 
# students.sort()                       # ["Alice","Charlie","Zara"]
# print(len(students))                  # 3
# print("Alice" in students)            # True
# print(students.index("Charlie"))      # 1

# Dictionaries
# A dictionary maps unique keys to values. Instead of accessing items by position, you look them up by name (key). A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.


# students = {"Name": "Alice", 
#             "Score": 85,
#             "Age": 25,
#             "School": "Mita School",
#             "Course": "Python"
#             }
            
# del students["Course"]
# students["email"] = "f@mail.com"     

# print(students["Name"])  # Output: Alice
# print(students["Age"])
# print(students["School"])
# print(students["email"])
# print(students["Score"])

# for keys in students:
    # print(keys)

# for val in students.values():
#     print(val)

# for key, val in students.items():
    # print(f"{key}: {val}")

# print(students.get("Bob"))  # Output: 90

# Nested Dictionaries

# Each student stores their own dict
# classroom = {
#     "Fortune": { "score": 92, "grade": "A", "school": "Mita School" },
#     "Ada":     { "score": 85, "grade": "B", "school": "Mita School" },
#     "Linus":   { "score": 60, "grade": "D", "school": "Mita School" },
# }

# work = {
#     "hope": { "score": 75, "grade": "C", "school": "Mita School" },


# }
 
# for name, data in work.items():
#     print(f"{name:12} {data['score']}/100  Grade: {data['grade']}")




# Tuples is like a list but it cannot be changed after creation. We use tuple for data that should remain constant. example: coordinates = (10, 20), rgb = (255, 0, 0), function parameters((10, 20)), and named record.

# point = (30, 40, 20, 60)
# rgb_red = ("red", "green", "blue")
# months     = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

# print(point[0])
# print(months[6])
# print(rgb_red[1])

# north, south, east, west = point
# r, g, b  = rgb_red
# print(f"point: {north}, {south}, {east}, {west} \nRed, green, blue channels: {r} {g} {b} ")


# A set stores only unique values in no guaranteed order. Use them to remove duplicates.
# tags = {"python", "code", "python", "tutorial", "code"}
# print(tags)      # {"python", "code", "tutorial"} — order may vary

# set operations
# tags.add("programming")
# tags.remove("code")
# print(tags)    

# a = {1,2,3,4,5,6}
# b = {4,5,6,7,8,9}
#  (&) - Intersection Returns only the elements that exist in both sets. It is useful for finding common items between datasets.
#  (|) - union Combines all unique elements from both sets. Any duplicates between the sets are automatically removed
#  (-) - difference Returns a set containing elements that exist only in the first set and not in the second.
#  (^) - symmetric difference Returns a set containing elements that are in either of the sets, but not in both 

# print(a & b)
# print(a | b)
# print(a - b)
# print(b - a)
# print(a ^ b)

# Build a contact book using a dictionary. Support: add contact, search by name, delete, list all. Loop until user quits.

contacts = {}

# while True:
#     print("\n 1) Add Contact 2) Search Contact  3) Delete Contact 4) List All Contacts 0) Quit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name = input("Enter contact name: ")
#         phone = input("Enter contact phone: ")
#         contacts[name] = phone
#         print(f"Contact added: {name} - {phone}")
#     elif choice == "2":
#         name = input("Enter contact name to search:")
#         if name in contacts:
#             print(f"Contact found: {name} - {contacts[name]}")
#         else:
#             print("Contact not found.")
#     elif choice == "3":
#         name = input("Enter contact name to delete:")
#         if name in contacts:
#             del contacts[name]
#             print(f"Contact deleted: {name}")
#         else:
#             print("Contact not found.")
#     elif choice == "4":
#         if contacts:
#             print("All Contacts:")
#             for name, phone in contacts.items():
#                 print(f"  {name}: {phone}")
#         else:
#             print("No contacts available.")
#     elif choice == "0":
#         print("Quitting...")
#         print("Exited")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# Assignment
# Build a program using a dictionary (student name -> list of scores) that supports: add student, add a score, display all students with their average, display the top scorer.


# Finding and Fixing Errors
# Type 1 — SyntaxError (Code Will Not Even Start): Python cannot parse your code. Usually a missing colon, bracket, or quote. The error message shows exactly which line.
# name = input("Enter your name: ")

# if name in contacts:
#     print("today class:)")
  
# else:
#     print("go home")


# Type 2 — RuntimeError / Exception (Crashes During Execution)
# Syntax is correct but something goes wrong while running. Python raises an exception with a descriptive error message.

# we have:

# name error is raised when you try to use a variable that hasn't been defined
# type error is raised when you try to use an operator or function with the wrong type of data
# index error is raised when you try to access an index that doesn't exist in a sequence
# key error is raised when you try to access a key that doesn't exist in a dictionary
# file not found error is raised when you try to open a file that doesn't exist

# print("5" + "3")
# print(float("douglas"))
# students = {"Name": "Alice", 
#             "Score": 85,
#             "Age": 25,
#             "School": "Mita School",
#             "Course": "Python",
#             # "douglas": "5years"
#             }
            
# del students["douglas"]
# students["email"] = "f@mail.com"  
# open("index.html")

# Type 3 — Logic Error (Wrong Answer, No Crash)
# The hardest type. Code runs without error but gives wrong results. You must trace through your logic to find where the reasoning went wrong.

# scores = int(input("enter number "))
# def class_average(scores):
    # return sum(scores) / len(scores)    # wrong: hardcoded 10


# Debugging Techniques
# 4.	Read the error message — Python gives file name, line number, and error type. Never ignore it.
# 5.	Print debugging — add temporary print() statements to check variabble values at key points:
# def process(data):
    # print(f"DEBUG input: {data}")    # check what came in
# 6.	Use the VS Code debugger: set a breakpoint (click left of line number), press F5, step line by line, inspect variables in real time.
# 7.	Rubber duck debugging: explain your code line by line out loud (to a rubber duck or a friend). Often the bug becomes obvious when you verbalise it.
# 8.	Simplify: isolate the broken piece in a small test script. Remove everything else until you have the minimum code that shows the bug.

# Note: use ai for advanced debugging

# clean code eand pep 8 style
# PEP 8 is the official Python style guide. Following it makes your code readable by any Python developer in the world.

# ── Naming Conventions ──
# student_name  = "Fortune"       # variables:  snake_case
# MAX_ATTEMPTS  = 5               # constants:  UPPER_SNAKE_CASE
 
# def calculate_average(scores):  # functions:  snake_case
    # pass
 
# class StudentRecord:            # classes:    PascalCase  (Week 6)
    # pass
 
# ── Spacing ──
# x = 5 + 3                       # spaces around operators
# result = calculate_average(scores)
 
# def greet(name, greeting="Hi"): # no spaces around = in default args
    # pass

# print(5 + 3) # adding 5 to 3
# Open 'data.txt' in read ('r') mode


#  Files, JSON & Error Handling

# file handling

# f =  open("index.html", "r")
# content = f.read()
# f.close()

# "r(read)" - open files to read only
# "w(write)" - open files to write (overwrites existing content)
# "a(append)" - open files to append (adds to existing content)
# "r+" - open files to read and write
# "x" - open files for exclusive creation

# with open('data.txt', 'r') as file:
    # content = file.read()
    # print(content)

# try:
#     with open('data.txt', 'w') as file:
#         file.write("Hello, World!")
#         file.write("\nThis is a new line.")
#         file.write("\nIn mita school, we have favour and compassion.")
# except FileNotFoundError:
#     print("the file was not found")

# with open('data.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('data.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('data.txt', 'w') as file:
#     file.write("lets see how it goes and what works")

# try:
#     with open("name.txt", "x") as file:
#         file.write("This file is brand new!")
# except FileExistsError:
#     print("Error: That file already exists. Choose a different name.")

# try:
#     with open("name.txt","rt") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file was not found.")

# try:
#     with open("country.txt", "x") as file:
#         file.write ("Uyo is the capital of Akwa Ibom State")
# except FileExistsError:
#     print("Error: That file already exists. Choose a different name.")

# with open("country.txt", "w") as file:
#      file.write("You will love staying in Uyo")
# # print("Error: The file was not found.")

# with open("country.txt", "a") as file:
#     file.write("I love Uyo")

#     with open("country.txt", "r") as file:
#         content = file.read()
#         print(content) 

# import datetime
 
# def log_event(message):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("events.log", "a") as file:
#         file.write(f"[{timestamp}] {message}\n")
 
# log_event("User logged in")
# log_event("User viewed dashboard")
# log_event("User logged out")


# JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data, frequently used for APIs and configuration files. In Python, you interact with this format using the built-in json module

# python types -> JSON equivalents  -->> examples
# dict -> object  -->> {"name": "Alice", "age": 30}
# list, tuple -> array  -->> [1, 2, 3]
# str -> string  -->> "Hello, World!"
# int, float -> number  -->> 42, 3.14
# bool -> boolean  -->> true, false
# None -> null  -->> null

# 1. dump() – Saving DataThe dump() function is used to write a Python object directly into a file-like object.

# Purpose: To persist data to a physical file on disk.


# Purpose: To restore saved data into the program's memory.

# import json

# students = {"Alice": 30, 
#             "Bob": 25, 
#             "Charlie": 35, 
#             "scores": [85, 90, 78]
#             }       # from python object JSON string

# json_text = json.dumps(students)
# # print(json_text)
# print(json.dumps(students, indent=2))

# indent tells Python to add line breaks and spaces of indentation to each level of the JSON data.


# 2. load() – Retrieving Data The load() function is the reverse of dump(). it reads data from a file-like object and converts it back into a native Python object.

# json_string = '{"city": "New York", "country": "USA"}'       #JSON string → Python object 
# data = json.loads(json_string)
# print(data)

#  3. json.dump() — Write Python object to JSON file 
# contacts = [
#     {
#     "name": "Alice", "phone": "080132452674"
#    },
#    {
#     "name": "bao", "phone": "080123456789"
#    },
# ]
# with open("contacts.json", "w") as file:
#     json.dump(contacts, file, indent=4)


# contat = [
#     {
#         "name": "David", "phone": "09150921509"
#     },
#     {
#         "name": "Overcommer", "phone": "07059305834"
#     },
#     {
#         "name": "Hope", "phone": "08012345655"
#     },
#     {
#         "name": "Fortune", "phone": "070012345678"
#     },
# ]
# with open("contacts.json", "a") as file:
#     file.write('{"name": "Nqama", "phone": "080123456789"}, \n{"name": "david", "phone": "080987654321"}')

#     json.dump(contacts, file, indent=2)



# #  4. json.load() — Read JSON file → Python object 
# with open("contacts.json", "r") as file:
#     data = json.load(file)
#     print(data) 

# def car(model, model1):
#     print(f"This is a {model} and {model1}")
# car("Toyota", "nissan") 


# import os
# import json

# FILE = "todo.json"

# def load_todos():
#     if os.path.exists(FILE):
#         with open(FILE, "r") as file:
#             return json.load(file)
#     return []

# def save_todos(todos):
#     with open(FILE, "w") as file:
#         json.dump(todos, file, indent=2)


# def add_todo(task):
#     todos = load_todos()
#     todos.append({"task": task, "completed": False})
#     save_todos(todos)
#     print(f"Task added: {task}")


# def complete_todo(index):
#     todos = load_todos()
#     if 0 <= index < len(todos):
#         todos[index]["completed"] = True
#         save_todos(todos)
#         print(f"Task marked as complete: {todos[index]['task']}")
#     else:
#         print("Invalid task index.")


# def show_todos():
#     todos = load_todos()
#     for i, todo in enumerate(todos):
#         status = "✓" if todo["completed"] else "✗"
#         print(f"{i + 1}. [{status}] {todo['task']}")



# add_todo("Buy groceries")
# add_todo("go shopping")
# add_todo("Walk the dog")
# add_todo("Learn everything about python")
# complete_todo(0)
# complete_todo(3)
# show_todos()



# assignment
# 1. Write a program that asks for an expense name and amount, validates the amount (must be a positive number), saves each expense to a JSON file, and loads the file at startup. Handle all possible errors gracefully.

# 2.  Build a full expense tracker. It must: load existing expenses from a JSON file on startup, let the user add expenses (name, amount, category), save to JSON after every addition, show total by category, and handle all invalid input with try/except.