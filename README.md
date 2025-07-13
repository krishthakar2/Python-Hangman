# Hangman Game 

A Python-based console Hangman game designed for solo play. The game randomly selects a word, and the player must guess it one letter at a time before they run out of lives.

---

## How the Game Works

- A random word is selected from a predefined list.
- The player guesses one letter per turn.
- If the guess is correct, the letter is revealed in the word.
- If the guess is wrong, the player loses a life.
- The game continues until:
  - The player correctly guesses the entire word (🎉 win), or
  - The player runs out of lives (💀 game over).

---

## Features

- Random word selection from a word list.
- Tracks guessed letters and prevents duplicate guesses.
- Displays progress after every guess.
- Displays number of lives remaining.
- Shows winning or losing messages.
- Uses functions for modularity and readability.

