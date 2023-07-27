import random

def computer_guess(x):
    low = 1    # The lower bound of the range within which the computer will guess.
    high = x   # The upper bound of the range within which the computer will guess.
    feedback = ''  # Variable to store user feedback ('H', 'L', or 'C').

    while feedback != 'c':  # Loop until the computer's guess is correct ('C').
        if low != high:   # Check if there's a range of numbers left to guess.
            guess = random.randint(low, high)  # Generate a random number within the current range.
        else:
            guess = low  # If there's only one number left, set the guess to that number.

        # Ask the user for feedback on the computer's guess.
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ').lower()

        # Update the range based on the user's feedback.
        if feedback == 'h':
            high == guess - 1  # If the guess was too high, set the new upper bound.
        elif feedback == 'l':
            low = guess + 1   # If the guess was too low, set the new lower bound.

    # The loop ends when the user provides 'C' as feedback, meaning the computer guessed correctly.
    print(f'The computer guessed your number correctly, \nThe number you picked is {guess}')

computer_guess(10)  # Call the function with an upper bound of 10 (range from 1 to 10).
