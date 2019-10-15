"""
Lesson 3: Conditional Statements (cont.)

You will learn about:
- elif statements
- Logic operators

REMINDER: First, run the script! Look for instructions in lesson 1 if you forgot how.
"""

""" elif statements """
# Now that you know both if and else statements, it's time to learn about the combination of the two: the elif statement!
# 'elif' stands for else if; the elif statement is pretty much another condition you want to check after you've done the if
# statement, but before you resort to the else statement. Here's an example:

# This first if/else statement has a false condition, so we go straight to the else statement.
if 3 > 5:
  print('if statement')
else:
  print('else statement')
# Now, for the if/elif/else statement, after seeing that the if condition is false, we check the elif statement.
# The condition for the elif statement is true, so we execute whatever is inside the elif statement instead of the else.
if 3 > 5:
  print('if statement')
elif 3 < 5:
  print('elif statement')
else:
  print('else statement')

# TODO: Let's do the temperature problem again, except this time the boundaries are: x>85 = Hot, 50<x<85 = Fair, x<50 = Cold
# Ask the user what the temperature is, and then print the correct word for the temperature according to the guidelines above.
itemp = input('What is the temperature? ')
if float(itemp) >  85:
	print('Hot')
elif (float(itemp) <= 85 and float(itemp) >= 50):
	print('Fair')
else:
	print('Cold')


""" Logic operators """
# So we learned about mathematical operators in Python, such as + or - and > or <. Introducing: the 'and' and 'or' operators!
# The 'and' operator requires the conditions it joins to all be true in order for the entire statement to be true. The 'or'
# operator only requires one condition to be true. Here are some truth tables below:

print()
print('AND operator truth table')
#           True    |  False
print(True and True, True and False)    # True
print(True and False, False and False)  # False

print()
print('OR operator truth table')
#           True   |  False
print(True or True, True or False)    # True
print(True or False, False or False)  # False

# TODO: Ask the user to choose a number. If the number is both odd and divisble by 3, say 'You win!'. Otherwise, if it is either
# even or divisible by 5, say 'Cool!'. Otherwise, say 'Neato!'
inumbr = input(' Please choose a number ')
if (float(inumbr) % 2 == 1 and float(inumbr) % 3 == 0):
	print('You win!')
elif (float(inumbr) % 2 == 0 or float(inumbr) % 5 == 0):
	print('Cool!')
else:
	print('Neato!')


""" Practice Problems """
# 1. Ask the user for a year (like 2019). Identify whether it's a leap year.
#   Criteria for a leap year:
#   1. If the year can be evenly divided by 4 then it is a leap year
#   2. If the year can be evenly divided by 100, and it is not evenly divided by 400, then it is NOT a leap year.
#   3. If the year is evenly divisible by 400, then it is a leap year

iyear = input('Please enter any year ')
if (float(iyear) % 4 == 0 or float(iyear) % 400 == 0):
	print('It is a leap year ')
elif (float(iyear) % 100 == 0 and float(iyear) % 400 != 0):  # wrong statement, never execute !!!
	print('It is Not a leap year ')
else:
	print('It is not a leap year ')

# 2. Ask the user for a number between 0 and 23, inclusive (this number represents a time). If the number is greater than 21 or
#    less than 6, say they are asleep. If the number is between 8 and 16, say they are at work. For any other number, say that
#    you have no idea what they are doing.

ihour = input('Please enter any hour between 0-23 ')
if (float(ihour) > 21 and float(ihour) <= 24):
	print('they are asleep ')

elif (float(ihour) <= 6 and float(ihour) >= 0):
	print('they are asleep ')
elif (float(ihour) >= 8 and float(ihour) <= 16):
	print('they are at work ')
else:
	print('no idea what they are doing ')