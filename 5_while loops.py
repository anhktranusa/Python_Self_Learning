"""
Lesson 5: while loops

You will learn about:
- The similarities and differences between a while loop and a for loop
- Infinite loops
- Components: condition and counter

"""

""" Basic while loop structure """
# While loops are loops that can have a dynamic number of iterations.
# For example, if you wanted to ask the user to if they wanted to keep
# playing in a game, you would use a while loop since that number changes.

# The structure of a while loop is as follows:
"""
counter = starting_value
while <condition>:
    <body of code>
    counter changes
"""
# The two main components to pay attention to here are the condition and the
# increment variable. The condition must be true in order for the loop to execute,
# and the counter value (or changing value in general, it doesn't have to be
# counting) enables the loop to end eventually. Here's an example:
counter = 0
while counter < 5:
    print(counter)
    counter += 1
# TODO: write a while loop that prints your name 10 times

counter = 0
while counter < 10:
    print('Anh Tran')
    counter += 1


""" Infinite Loops """
# CAUTION: infinite loops are the worst! They occur when the loop's condition is
# true forever, in which case, the code will never get past it. That is why it is
# essential that you add the changing value: infinite loops = bad

# Here's an example
# TODO: uncomment it, run it, and then use control-C to exit
"""
while True:
    print('Hello World! (on steroids)')
"""


""" Comparing while loops and for loops """
# While loops and for loops differ in one main way: for loops have a set amount of
# iterations. However, while loops can have any number of iterations. You can pretty
# much write a while loop that can do the same thing as any for loop.

# Remember this example? It prints the odd numbers under 10
for whatever_var_name_i_want in range(1, 10, 2):
    print(whatever_var_name_i_want)
# We can do the same thing with a while loop
counter = 1
while counter < 10:
    print(counter)
    counter += 2


""" Practice Problems """
# We'll be using the practice problems from the last lesson to show you how to
# translate for loops to while loops!

# 1. Create a list and fill it with all the even numbers below 100
"""
#from last lesson
even_nums = []
for i in range(2, 100, 2):
	even_nums.append(i)
print(even_nums)
"""
counter = 2
even_nums = []

while counter < 100:
    even_nums.append(counter)
    counter += 2
print(even_nums)

# 2. Use the list you made above and remove all of the numbers that are divisible
# by 8.
"""
#from last lesson
for item in even_nums:
	if item % 8 == 0:
		even_nums.remove(item)
print(even_nums)
"""
counter = 2
while counter < 100:
	if counter % 8 == 0:
		even_nums.remove(counter)
	counter += 2
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
# From lesson 4
sq_num = input('Enter a number then it will print twice the square shape of that number ')

for i in range(int(sq_num)):

	print (sq_num * int(sq_num))

# Another way to write this loop

for i in range(int(sq_num)):
    for j in range(int(sq_num)):
        print(sq_num, end='')
    print()
"""
sq_num = input('Enter a number then it will print twice the square shape of that number ')
counter = 0
while counter < (int(sq_num)):
	print (sq_num * int(sq_num))
	counter += 1

# another way to write this loop
counter_out = 0

while counter_out < int(sq_num):
	counter_in = 1


	while counter_in < int(sq_num):
		print(sq_num, end='')
		counter_in += 1
	print(sq_num)      # HINT: do you need to print another sq_num here?
	counter_out += 1
