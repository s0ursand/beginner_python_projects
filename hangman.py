import random
from hangman_words import words  # Importing the list of words from hangman_words.py
import string

def get_valid_word(words):
    # Function to get a valid word from the list (without '-' or ' ')
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    # Get a valid word from the list
    word = get_valid_word(words)
    
    # Convert the word into a set of unique letters
    word_letters = set(word)
    
    # Create a set containing all uppercase letters of the alphabet
    alphabet = set(string.ascii_uppercase)
    
    # Create an empty set to store the letters guessed by the user
    used_letters = set()
    
    # Set the maximum number of attempts allowed
    max_attempts = int(input('Select number of attempts before losing the game: '))
    
    # Counter for the number of attempts made
    attempts = 0

    # The game loop runs until all letters of the word are guessed or maximum attempts are reached
    while len(word_letters) > 0 and attempts < max_attempts:
        # Display the current state of the word with underscores for unknown letters using list comprehension
        word_display = '|'.join([letter if letter in used_letters else '_' for letter in word])
        print(word_display)

        # Get the user's letter as input and convert it to uppercase
        user_letter = input('Guess a letter: ').upper()

        # Check if the user's input is a valid letter (uppercase) and not used before
        if user_letter in alphabet - used_letters:
            # Add the letter to the used_letters set
            used_letters.add(user_letter)
            
            # Check if the user's letter is in the word's letters
            if user_letter in word_letters:
                # If it is, remove the letter from the word_letters set
                word_letters.remove(user_letter)
            else:
                # If the letter is not in the word, increment the attempts counter
                attempts += 1
                print(f'The letter "{user_letter}" is not in the word. Attempts left: {max_attempts - attempts}')
        elif user_letter in used_letters:
            print('You have already used that character. Try Again')
        else: 
            print('Invalid character')

    # Check if the user won or lost the game
    if len(word_letters) == 0:
        print(f'Congratulations! You guessed the word: {word}')
    else:
        print(f'Sorry, you ran out of attempts. The word was: {word}')

# Start the hangman game
hangman()
