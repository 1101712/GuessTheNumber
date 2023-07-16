# Guess The Number Game

## Overview
This project is a simple, console-based game where a user is tasked with guessing a random number within a user-defined or deafault range. The game includes a leaderboard feature that keeps track of the fewest number of guesses needed to find the correct number.
## Features
- **User-Defined Number Range**: The user has the option to define their preferred range within which a random number will be generated for guessing (default is 1-100).
- **Random Number Generation**: The game generates a random number within the specified range for the user to guess.
- **Input Validation**: The game validates user inputs to ensure they are numerical and within the specified range.
- **Guess Evaluation**: The game provides feedback to the user if their guess is too high, too low, or correct.
- **Leaderboard**: The game keeps track of the number of guesses made and saves this to a leaderboard.
## Existing Features
All features described above are currently implemented and operational.
## User Experience (UX)
This game provides a straightforward user experience. Users can define their preferred range for the random number, guess a number within this range, and receive immediate feedback on their guess.
## Site Goals

The main goal of this project is to provide a simple and engaging game for users to play. It aims to test and improve the user's intuitive reasoning and guessing abilities while providing them the flexibility to define their own number range.

## Compatibility and Responsiveness Testing


## Languages Used

- [Python](https://www.python.org/)

## Frameworks, Libraries & Programs Used

- [random](https://docs.python.org/3/library/random.html): for generating random numbers
- [json](https://docs.python.org/3/library/json.html): for storing and retrieving leaderboard data
- [argparse](https://docs.python.org/3/library/argparse.html): for handling command-line arguments and allowing the user to define the range of numbers