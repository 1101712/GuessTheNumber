# Your code goes here.
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class NumberGuessingGame:
    def __init__(self):
        self.target = random.randint(1, 100)  # Target number to guess
        self.attempts = 0  # Number of attempts made by player

    def make_guess(self, guess):
        """
        Function to process a player's guess. If the guess is correct, the game is over. 
        If the guess is incorrect, provides a hint to the player and increments attempts.
        """
        self.attempts += 1
        if guess == self.target:
            return "correct"
        elif guess < self.target:
            return "too low"
        else:  # guess > self.target
            return "too high"
