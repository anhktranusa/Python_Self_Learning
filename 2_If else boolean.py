"""
Lesson 2: Conditional Statements

You will learn about:
- if statements
- else statements
- Boolean operators

REMINDER: First, run the script! Look for instructions in lesson 1 if you forgot how.
"""

""" if statements """
# if statements are a tool used in programming that executes code based on whether the
# given condition is true. This is where the boolean data type (True or False) comes
# in handy:
if True:
    print('This printed in the if statement that was True!')
if False:
    print('This printed in the if statement that was False!')
# By running the script, you can see that only the first statement was printed.
# This is because if statements only execute the stuff in its body section if the
# condition is true.

# TODO: You try! How can you make the code inside the if statement output to
# the console, if you only change the condition?
"""
    General if statement format
    
    if <condition>:
        <body of code>
"""
if 3 < 5:
    print('Print me!')


""" else statements """
# Else statements contain the code that should happen if the if condition is false.
if 3 > 5:
    print('Ex. 1, Entered if statement')
else:
    print('Ex. 1, Entered else statement')
# Now, if the if condition is true, the else statement block will not be used
if 6 > 5:
    print('Ex. 2, Entered if statement')
else:
    print('Ex. 2, Entered else statement')

# TODO: Add an else statement to the code below that prints your name if the condition
# in the if statement is false
if False:
    print('This should not print')
else:
    print('Anh')

""" Boolean operators """
# In math, you can compare numbers and say whether a statement is true or not. In our
# previous problems, we compared integers using the greater than (>) and less than (<) symbols.
# Let's show you the rest of them.
print('Greater than:', 4 > 4, 4 > 5)
print('Greater than or equal to:', 4 >= 4, 4 >= 5)
print('Less than:', 4 < 4, 4 < 5)
print('Less than or equal to:', 4 <= 4, 4 <= 5)
print('Equal to:', 4 == 4, 4 == 5)
print('Not equal to:', 4 != 4, 4 != 5)


""" Practice Problems """
# 1. Ask the user for a temperature and print 'Hot' if it is greater than 80 and
# 'Cold' if it's less than that.
temper = input('What is the temperature?')
if float(temper) > 80.0:
    print('Hot')
if float(temper) < 80.0:
    print('cold')
# 2. Ask the user to enter in their grade (out of 100). If it is greater than or equal
# to 70, then tell the user than they passed. Otherwise, they failed.
grade = input('what is your grade between 0 and 100?')
if float(grade) >= 70.0:
    print('You are passed')
else:
    print('You are fail')
