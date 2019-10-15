"""
Lesson 1: Input/output and variables

You will learn about:
- Running files
- Print statements
- Basic data types
- Variables and their uses
- Getting input from the user

NOTE: These lessons are supposed to be trial and error based! I will provide
instructions in the comments, but what you actually code is up to you. Feel free
to be creative, and remember: you can always run the file!
"""

""" Running Files """
# Running files is very simple in python. Follow these steps:
# 1. Open your console. In Windows, your console is called Command Prompt.
# 2. Change to the correct folder (also called directory). Our folder is called
#    'Python Lessons' - find this folder just like you would in File Explorer
#    (although you might want to ask for help here).
# 3. Type 'python <name of your script>' and then ENTER to run your script

# TODO: Run this script! The command is: python 1.py
#       and the output you will see is:
# I like cheese
# string
# How many eggs do I have?

# NOTE: press CTRL-C to exit the program for now.

""" Print Statements """
# Let's do that classic rite-of-passage, the "Hello World!" program!
# Below is a print statement. This shows output to the user.
print('I like cheese')
# TODO: Write your hello world program below!
print('Hello world')


""" Data Types and Variables """
# Variables just store values (data), like in math.
# All sorts of data can be stored in computers. Here are a couple basic ones:
x = 1               # Integer
y = 2.3             # Float: decimal value
z = True            # Boolean: True or False
silly = 'string'    # String: multiple characters between quotation marks
print(silly)
# TODO: try printing all of these variables! (x, y, and z)
# BONUS: print the sum of the variables x and y (Hint: +, -, *, / are the math operators)
print(x, y, z, silly)
print(x*y)

""" User Input """
# You can ask the user for information too! The input() function shows the user a prompt,
# and whatever the user replies with can be stored in a variable.
eggs = input('How many eggs do I have?')
print('The user says I have', eggs, 'eggs.')
# TODO: Your turn, ask a question!
shoes = input('how many pairs of shoes do I have?')
print('The user say I have', shoes, 'shoes')

""" Practice Problems """
# 1. Ask the user for their name and age. Then print out what they are in the format:
# 'Hello, my name is Michelle and I am 19 years old.'
iname = input('what is your name?')
iage = input('how old are you?')
print('Hello, my name is', iname, 'and I am', iage, 'years old')


# 2. Ask the user for a radius and calculate the area of a circle and volume of sphere with that radius.
# Formulas: V = 4/3*pi*r^3  ;   A = pi*r^2          <- NOTE: not proper syntax here
radius = input('Please enter the radius')
pi = 3.14
flrad = float(radius)
print('The area is', pi*flrad**2, 'and the volume of sphere is', 4/3*pi*flrad**3)