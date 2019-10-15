"""
Lesson 4: for loops

You will learn about:
- Iteration
- Lists

"""

""" The Basic For Loop """
# For loops are loops that execute a task for a known/finite number of times.
# For example, let's say I want to say I am cool 5 times. That would look like:
print('----- Example 1 -----')
for i in range(5):
    print('I am cool')
# In this for loop, a variable named i is created and it increases by 1 each time
# (this is called iterating) the loop executes the command. So if I printed
# the variable i each time rather than printing 'I am cool', we would see numbers that
# increase. Try running the code!
print('----- Example 2 -----')
for i in range(5):
    print(i)
# NOTE: if you run the code, you'll notice that the numbers are from 0 to 4. This is
# because counting almost always starts with zero in computer science, and the number
# you plug into the range (so in our case, 5) is not inclusive, as it in goes to one
# less than the value you entered.

# TODO: Print out the odd numbers that are less than 10 using a for loop

for x in range(10):
   
 	# Check if x is even
   
	if x % 2 == 0:
        
		continue
    
	print(x)


# There are lots of cool ways you can customize for loops! Be sure to google some
# techniques. For example, I can solve the same problem you did above by skipping numbers!
# Note: the iterating varible can be named whatever you want, it doesn't have to be i
print('----- Example 3 -----')
for whatever_var_name_i_want in range(1, 10, 2):
    print(whatever_var_name_i_want)


""" Using Loops with Lists """
# A list in a structure that holds information in a linear fashion -- in C and C++,
# it's called an array. An example of a list is:
fruits = ['apples', 'oranges', 'bananas', 'limes', 'blueberries', 'grapes']
# Lists are super awesome because it's pretty easy to add, remove, and get items
# from them.
print('----- Example 4 -----')
print('Original fruit list:', fruits)
fruits.append('plums')
print('Added a fruit:', fruits)
# You can reference a specific item from the list by referencing its index
print('Fruit at index 3 (remember counting starts at zero):', fruits[3])
print('There are a lot of ways to delete items, so here are a few:')
del fruits[1]
print('Delete with del (specify index):', fruits)
fruits.remove('grapes')
print('Delete with remove (specify item):', fruits)
print('Delete with pop (returns the popped valued):', fruits.pop(1), fruits)

# Now let's learn how to use them with for loops.
print('----- Example 5 -----')
for item in fruits:
    print(item)
# The loop above skips all of the numbering and stuff: instead of having a variable
# that is an integer and increases numerically, python just increases the index
# of the list item that it goes through

# TODO: Use the following list and only print the even numbers using a for loop
numbers = [2, 5, 8, 3, 7, 2, 4, 7, 9]
for item in numbers:
	if item % 2 == 1:
		continue
	print(item)

""" Practice Problems """
# 1. Create a list and fill it with all the even numbers below 100

even_nums = []
for i in range(2, 100, 2):
	even_nums.append(i)
print(even_nums)



# 2. Use the list you made above and remove all of the numbers that are divisible
# by 8.

for item in even_nums:
	if item % 8 == 0:
		even_nums.remove(item)
print(even_nums)


# BONUS: Let's try a nested for loop, which is putting a for loop inside of another one.
# It looks like this:
print('----- BONUS Example -----')
for i in range(5):
    for j in range(5):
        print(i, j)
# Write a program that asks the user for a number, and then print a square with
# that number as the side length. For examples:
"""
User entered: 2
Output:
22
22

User enetered: 5
Output:
55555
55555
55555
55555
55555
"""

sq_num = input('Enter a number then it will print twice the square shape of that number ')

for i in range(int(sq_num)):
	
	print (sq_num * int(sq_num))

# Another way to write this loop

for i in range(int(sq_num)):
    for j in range(int(sq_num)):
        print(sq_num, end='')
    print()
    
			
