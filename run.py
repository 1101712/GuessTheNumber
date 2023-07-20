"""
Defines the main() function which starts the game, along with the Game class
which is responsible for controlling the flow of the game.
"""
from pyfiglet import Figlet
import random
import json
import shutil


class GuessTheNumberGame:
    """
    A class to conduct a number-guessing game with leaderboard functionality.
    """
    def play_again(self):
        while True:
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again.lower() in ["yes", "no"]:
                if play_again.lower() == "yes":
                    self.select_difficulty()
                return play_again.lower() == "yes"
            else:
                print("Invalid input, please answer with 'yes' or 'no'.\n")

    def select_difficulty(self):
        valid = False
        while valid is False:
            print("1 - Easy mode")
            print("2 - Medium mode")
            print("3 - Hard mode")
            difficulty = input("Please select difficulty: ")
            if difficulty in ["1", "2", "3"]:
                if difficulty == "1":
                    self.start = 1
                    self.end = 20
                if difficulty == "2":
                    self.start = 1
                    self.end = 50
                if difficulty == "3":
                    self.start = -50
                    self.end = 50
                valid = True
            else:
                print("Invalid input, please select one of the options\n")
        self.target = random.randint(self.start, self.end)
        self.guesses = []

    def __init__(self):
        self.leaderboard_file = "leaderboard.json"
        self.select_difficulty()

    def check_guess(self, guess):
        if guess < self.start or guess > self.end:
            return False, "Your guess is out of bounds. Try again."
        elif guess < self.target:
            return True, "Too low! Try again."
        elif guess > self.target:
            return True, "Too high! Try again."
        else:
            return True, "Congratulations! You've guessed the number!"

    def play(self):
        while True:
            try:
                guess = int(input(f"Guess the number I'm thinking of between {self.start} and {self.end}: "))
                valid, result = self.check_guess(guess)
                if valid:
                    self.guesses.append(guess)
                print(result)
                if result == "Congratulations! You've guessed the number!":
                    self.update_leaderboard(len(self.guesses))
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
                print(f"You have made {len(self.guesses)} guesses.\n")
        if self.play_again():
            self.play()
        else:
            print("Thanks for playing!")

    def update_leaderboard(self, score):
        try:
            with open(self.leaderboard_file, 'r') as file:
                leaderboard = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            leaderboard = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf')}

        if self.end == 20:
            difficulty = "easy"
        elif self.end == 50:
            difficulty = "medium"
        else:
            difficulty = "hard"
            
        leaderboard[difficulty] = min(score, leaderboard[difficulty])

        with open(self.leaderboard_file, 'w') as file:
            json.dump(leaderboard, file)

        self.show_best_score(leaderboard)

    def show_best_score(self, leaderboard):
        for difficulty in ["easy", "medium", "hard"]:
            if leaderboard[difficulty] < float('inf'):
                print(f"The best score so far in {difficulty} mode is {leaderboard[difficulty]} guesses.")


if __name__ == "__main__":
    f = Figlet(font='slant')
    print(f.renderText('Welcome to Guess the Number Game!'))
    game = GuessTheNumberGame()
    game.play()
