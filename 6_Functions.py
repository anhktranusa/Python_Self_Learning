"""
Lesson 6: Functions

You will learn about:
- Main functions
- Custom functions
- Parameters
- Returned values

"""


""" Functions """
# Functions are a way to split up your code into smaller, more manageable chunks.
# It's pretty much a mini-system of code: think of your entire file as a big building
# with things happening inside, and functions are the little rooms.
# The format of a function is as follows:
def function_name(parameters):
    print('Body of function!')
    print(parameters)
# Note that when you run the code, the code inside the function above does not execute.
# That is because the code inside a function is not executed unless you explicitly
# say you want it to be.

# TODO: uncomment the line below and watch the code execute!
function_name('See look, now it prints out stuff!')


""" Parameters """
# In the previous function, we saw a lot of vocab being used. While the function name
# and the body of function parts were probably self-explanatory, you may be wondering
# what a parameter is. Parameters are values you pass into a function so that the
# function has those values to use. Since functions are closed systems, they cannot
# access the values you have outside of the function. For example:
a = 6
def print_num(a):
    print(a)
print_num(3)
# Even though there is a variable 'a' with a value outside of the function, the
# function can only use what is passed into it.

# TODO: Write a function that takes in your name and age as parameters, and then prints
# 'My name is <name> and I am <age> years old.' Hint: make sure you call your function
# after you write it!

iname = input('what is your name? ')
iage = input('what is your age? ')

def print_name(iname):
	print(iname)

def print_age(iage):
	print(iage)

print('My name is ',print_name(iname),' and I am ', print_age(iage),' years old.' 

""" Returning values """
# Not only can functions take in values, but they can also output values. Let's say
# we want to do a small calculation and then return to our main thread of logic. We
# want to be able to store that value from the small calculation, and that's where
# returning is handy.
# This function 'returns' the product of two numbers


def multiply(num_1, num_2):
    return num_1 * num_2
# I want to print out 2 * 4
answer = multiply(2, 4)
print(answer)


# TODO: print out the multiples of 13 under 100 using a the multiply() function above.
# Hint: use a for loop!


""" 'Main' Functions """
# Since you've done C and C++, you probably remember the mandatory main() function.
# In Python, you don't actually need that. If your code is not inside a function,
# the interpreter will just run it.
print('Look, this is executed even though it is not in a main() function!')
print('But you already knew that, huh?')
# But sometimes we don't want that, especially at FreeWave. We like to be able to
# run our scripts as the main script, but sometimes we create custom modules, and in
# that case we avoid executing everything that would for a main script.
# Therefore, we usually put everything we want to run in main under:
if __name__ == '__main__':
    print('Main function-like content typically goes here!')
# It's just a convention, either Google it or as me if you want more detail as to
# why we do this. Here's a good explanation I found:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do


# Practice Problems 
# 1. Write a function that takes in the radius and returns the area of a circle with
# that radius. (The formula is pi*r^2)

irad = input('Please enter radius: ')
pi = 3.14
def area(irad):
	return irad * irad * pi
answer = area(irad)
print(answer)

# 2. Write a function that generates a random number from 1 to 5 and asks the user to
# guess it. If the user is correct, return True. Otherwise, return False.
# Hint: you don't always need parameters in a function!
