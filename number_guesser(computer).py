# Import the random module to generate a random number later in the code
import random

# Define a function called "guess" that takes a single parameter "x"
def guess(x):
    # Generate a random number between 1 and "x" (inclusive)
    random_number = random.randint(1, x)
    
    # Initialize a variable "guess" with the value 0
    guess = 0
    
    # Enter a loop that continues until the user's guess matches the random number
    while guess != random_number:
        # Prompt the user to input a number between 1 and "x" 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # Check if the user's guess is less than the random number
        if guess < random_number:
            # If the guess is too low, print a message to inform the user and prompt them to guess again
            print('Sorry, guess again, too low.')
        # Check if the user's guess is greater than the random number
        elif guess > random_number:
            # If the guess is too high, print a message to inform the user and prompt them to guess again
            print('Sorry, guess again, too high.')
    
    # If the loop exits, it means the user has guessed the correct number
    # Print a congratulatory message along with the correct number
    print(f'Congrats! You have guessed correctly. \nThe number is {random_number}')

# Call the "guess" function with an argument of 10 to play the game with a range of 1 to 10
guess(10)
