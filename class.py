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