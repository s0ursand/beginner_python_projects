import random

# Set the number of digits in the secret number and the maximum number of guesses allowed
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    # Print the game introduction and rules
    print(f'''
    I am thinking of a {NUM_DIGITS} digit number with no repeated digits.
    Try to guess what it is, here are some clues:
    _______________________________________________________________
    When I say:     That means:
    Pico            One digit is correct but in the wrong position
    Fermi           One digit is correct and in the right position
    Bagels          No digit is correct
    _______________________________________________________________
    For example, if the secret number was 248 and your guess was 843, 
    the clues would be Fermi Pico.
    ''')

    while True:
        # Generate the secret number for the player to guess
        secretNum = getSecretNum()
        print(f'Are you ready? You have {MAX_GUESSES} guesses to get it. ')
        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Prompt the user for their guess and validate it
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess attempt: {numGuesses}')
                guess = input('> ')

            # Get the clues for the current guess and the secret number
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            # Break the loop if the player guesses correctly or runs out of guesses
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guess attempts')
                print(f'The number was {secretNum}')

        # Ask the player if they want to play again
        print('Wanna play again? (y/n): ')
        if not input('> ').lower() == 'y':
            print('Thanks for playing! ')
            break

def getSecretNum():
    # Generate a random secret number with no repeated digits
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Compare the player's guess with the secret number and provide clues
    if guess == secretNum:
        return 'You got it! '

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')  # Add "Fermi" if the guessed digit is in the correct position
        elif guess[i] in secretNum:
            clues.append('Pico')  # Add "Pico" if the guessed digit is present but in the wrong position

    if len(clues) == 0:
        return 'Bagels'  # If no clues were added, it means none of the digits were correct
    else:
        clues.sort()  # Sort the clues alphabetically to not give away the position of the numbers
        return '\n'.join(clues)  # Join the clues into a string and return them

if __name__ == '__main__':
    main()
