import random  

# Docstring for the assignment
"""
Username: Ktha770
ID: 
"""

def main():
    """Main function to run the Hangman game."""
    print_banner()  # Display the welcome banner
    words = get_words("Hangman_Words.txt")  # Get list of words from a file
    target_word = get_random_word(words)  # Select a random word from the list
    guess = ["_"] * len(target_word)  # Initialize the guess with underscores
    suggested_letters = []  # Initialize a list to keep track of suggested letters
    run_game(guess, target_word, suggested_letters)  # Start the game
    display_result(guess, target_word)  # Show the final result

def display_result(guess, target_word):
    """Display the result of the game (win or lose)."""
    # Check if the guess matches the target word
    if "".join(guess) == target_word:
        print(f"\nYou have guessed the word '{target_word}' correctly!\nWell done!")  # Player wins
    else:
        print(f"\nThe word was '{target_word}'.\nBetter luck next time!")  # Player loses

def run_game(guess, target_word, suggested_letters):
    """Run the game loop, handling guesses and mistakes."""
    mistakes_left = 7  # Set the number of mistakes allowed
    while mistakes_left > 0 and "_" in guess:  # Continue if mistakes are left and not all letters are guessed
        display_game_info(guess, suggested_letters)  # Show current game status
        letter = get_letter(suggested_letters)  # Get a valid letter from the player
        is_correct = process_guess(guess, target_word, letter)  # Check if the letter is in the target word
        if is_correct:
            print(f"Great! '{letter}' is in the target word!")  # Correct guess
        else:
            mistakes_left -= 1  # Decrease mistakes if the guess is wrong
            print(f"Bad luck! '{letter}' is not in the target word!")  # Incorrect guess
            if mistakes_left > 0:
                print(f"{mistakes_left} mistake(s) left!\n")  # Show remaining mistakes

    display_game_info(guess, suggested_letters)  # Show final game status

def display_game_info(guess, suggested_letters):
    """Display current guess and suggested letters."""
    # Print the current guess (with underscores for unguessed letters) and suggested letters
    print(f"Current guess: {' '.join(guess)}")
    print(f"Suggested letters: {suggested_letters}\n")

def get_letter(suggested_letters):
    """Prompt user for a new letter and validate it."""
    while True:
        letter = input("Suggest a letter: ").lower()  # Get letter from user and convert to lowercase
        if letter in suggested_letters:
            print("Letter already suggested.")  # Check if the letter has been guessed before
            print("Suggest another letter: ", end="")  # Prompt again
        else:
            suggested_letters.append(letter)  # Add letter to suggested letters
            return letter  # Return the valid letter

def process_guess(guess, target_word, letter):
    """Update guess if letter is in target_word, return True/False."""
    if letter not in target_word:  # Check if the letter is in the target word
        return False  # Letter is incorrect
    for index, char in enumerate(target_word):  # Iterate through the target word
        if char == letter:  # If the letter matches, update the guess
            guess[index] = letter
    return True  # Letter is correct

def print_banner():
    """Print the welcome banner with the user's name."""
    name = input("Please enter your name: ")  # Ask for the player's name
    message = f"*Welcome {name} to the COMPSCI 101 Hangman Game*"  # Welcome message
    border = "*" * len(message)  # Create a border based on the length of the message
    print(f"\n{border}\n{message}\n{border}\n")  # Print the banner

def get_words(filename):
    """Read words from a file and return as a list."""
    words = []  # Initialize an empty list for words
    with open(filename, 'r') as file:  # Open the file in read mode
        for line in file:  # Loop through each line in the file
            words.append(line.strip().lower())  # Add each word (lowercased) to the list
    return words  # Return the list of words

def get_random_word(words):
    """Return a random word from the list (provided)."""
    random_index = random.randrange(len(words))  # Get a random index from the word list
    return words[random_index]  # Return the random word

if __name__ == "__main__":  # If the script is run directly (not imported)
    main()  # Call the main function to start the game
