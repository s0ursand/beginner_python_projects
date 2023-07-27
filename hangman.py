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

    # The game loop runs until all letters of the word are guessed
    while len(word_letters) > 0:
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
        elif user_letter in used_letters:
            print('You have already used that character. Try Again')
        else: 
            print('Invalid character')

    # The loop ends when all letters are guessed, and the user wins the game
    print(f'Congratulations! You guessed the word: {word}')

# Start the hangman game
hangman()
