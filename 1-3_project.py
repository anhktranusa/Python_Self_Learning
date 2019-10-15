"""
Mini-Project 1: Rock, Paper, Scissors

Welcome to our first mini-project! You can't learn to code without coding, so these mini projects will pop up every few lessons or so
for you to practice. For our first one, let's make a simple game that will exercise all the skills we've been learning thus far.

____Game Flow____
1. Show the menu to the user:
    1. Rock
    2. Paper
    3. Scissors
2. Generate a random number from 1-3 (use the 'math' module - hint: Google it!) as the computer's choice.
3. Compare the user's value and the computer's. Determine who wins based on the rules listed below.

____Rules____
1. Rock beats scissors, scissors beats paper, and paper beats rock.
2. If the computer and the user have the same selection, state that it was a tie.
3. If the user enters a value that is invalid (as in not a number from 1-3), state that the input was invalid and end the game.
"""
import random

print("Let play game. ") 
print("1. Rock ")
print("2. Paper ")
print("3. Scissors ")


p_input = 1

while (p_input <= 3 and p_input >=1):
	p_input = int(input('Please enter an interger 1-3 to play game.  Enter other than 1-3 will end game '))
	c_number = random.randint(1, 3)
	if (c_number == p_input):
		print(' It a tie! ')
	elif (c_number == 1 and p_input == 2):
		print(' You win! ')
	elif (c_number == 2 and p_input == 1):
		print('Sorry You loose ')

	elif (c_number == 2 and p_input == 3):
		print(' You win! ')
	elif (c_number == 3 and p_input == 2):
		print('Sorry You loose ')

	elif (c_number == 3 and p_input == 1):
		print(' You win! ')
	elif (c_number == 1 and p_input == 3):
		print('Sorry You loose ')


print('Game over. ')
