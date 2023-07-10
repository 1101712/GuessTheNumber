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

    def is_over(self):
        """
        Function to check if the game is over. The game is over when the correct number is guessed.
        """
        return self.attempts > 0 and self.make_guess(self.target) == "correct"


game = NumberGuessingGame()

while not game.is_over():
    try:
        # Asking user for a number
        user_input = input("Guess a number between 1 and 100: ")
        guess = int(user_input)
        if guess < 1 or guess > 100:
            # Raising a ValueError if the number is not in the expected range
            raise ValueError("Number must be in the range 1 to 100.")