import random

def is_win(player, opponent):
    # Function to determine if the player wins against the opponent based on the choices.
    # Returns True if the player wins, False otherwise.

    # Check the different winning scenarios for the player.
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play():
    # Function to play a round of rock-paper-scissors game against the computer.
    
    user = input("select 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])  # Randomly select computer's choice ('r', 'p', or 's').

    if user == computer: 
        # If the user's choice matches the computer's choice, it's a tie.
        return 'It\'s a tie'

    if is_win(user, computer):
        # If the user wins based on the is_win function, return 'You Won! :)'.
        return 'You Won! :)'

    # If none of the above conditions are met, the user has lost.
    return 'You Lost! :('

print(play())  # Call the play function and print the result.
