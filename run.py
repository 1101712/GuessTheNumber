"""
Defines the main() function which starts the game, along with the Game class
which is responsible for controlling the flow of the game.
"""
from pyfiglet import Figlet
import random
import json
import shutil
from colorama import Fore, Style

class GuessTheNumberGame:
    """
    A class to conduct a number-guessing game with leaderboard functionality.
    """
    def play_again(self):
        # A while loop to continually ask the user if they want to play again
        while True:
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again.lower() in ["yes", "no"]:
                if play_again.lower() == "yes":
                    # Call the select_difficulty method to start a new game
                    self.select_difficulty()
                    # This will print a blank line for better readability.
                    print()
                # Return a boolean indicating whether the user wants to play again      
                return play_again.lower() == "yes"
            else:
                print("Invalid input, please answer with 'yes' or 'no'.\n")

    def select_difficulty(self):
        valid = False
        # This while loop will run until a valid difficulty level is chosen
        while valid is False:
            print("1 - Easy mode")
            print("2 - Medium mode")
            print("3 - Hard mode")
            difficulty = input("Please select difficulty: ")
            # Check if the player's choice is among the valid options
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
                # Set valid to True to exit the while loop
                valid = True
            else:
                print("Invalid input, please select one of the options\n")
            # Generate a random target number for the player to guess
        self.target = random.randint(self.start, self.end)
        # Reset the list of guesses
        self.guesses = []
        print()  # print a blank line for better readability.

    def __init__(self):
        """
        Initialize the GuessTheNumberGame class.
        The `leaderboard_file` attribute is set to the filename where the 
        leaderboard data is stored.
        The `select_difficulty` method is called to let the player select the 
        difficulty level and set the range of numbers to be used in the game.
        """
        self.leaderboard_file = "leaderboard.json"
        self.select_difficulty()

    def check_guess(self, guess):
        # Validate the guess: it must be within the specified range
        if guess < self.start or guess > self.end:
            return False, f"{Fore.BROWN}Your guess is out of bounds. Please try again.{Style.RESET_ALL}"
        elif guess < self.target:
            return True, f"{Fore.YELLOW}Too low! Please try again.{Style.RESET_ALL}"
        elif guess > self.target:
            return True, f"{Fore.YELLOW}Too high! Please try again.{Style.RESET_ALL}"
        else:
            return True, f"{Fore.GREEN}Congratulations! You've guessed the number!{Style.RESET_ALL}"

    def play(self):
        # Start an infinite game loop
        while True:
            try:
                guess = int(input(
                    f"Guess the number I'm thinking of between "
                    f"{self.start} and {self.end}: "))
                valid, result = self.check_guess(guess)
                # If the guess is valid (in bounds), append it to the list of guesses
                if valid:
                    self.guesses.append(guess)
                print(result)
                if "Congratulations! You've guessed the number!" in result:
                    # Update the leaderboard with the number of guesses
                    self.update_leaderboard(len(self.guesses))
                    break # exit the loop when the game ends
            # Handle the case where the user's input can't be converted to an integer
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
            # Print the total number of guesses made so far
                print(f"You have made {len(self.guesses)} guesses.\n")
        # After the game has ended and we're out of the loop, ask if the player wants to play again
        if self.play_again():
            # If play_again returns True, start a new game
            self.play()
        else:
            print("Thanks for playing!")

    def update_leaderboard(self, score):
        # This method updates the leaderboard and saves it to a file.
        # Try opening the leaderboard file and loading the contents into a dictionary
        try:
            with open(self.leaderboard_file, 'r') as file:
                leaderboard = json.load(file)
        # If file not found or content is not valid JSON,
        # create a new leaderboard with infinite scores for each difficulty        
        except (FileNotFoundError, json.JSONDecodeError):
            leaderboard = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf')}
    
        # Identify the difficulty of the current game based on the start and end numbers
        if self.start == 1 and self.end == 20:
            difficulty = "easy"
        elif self.start == 1 and self.end == 50:
            difficulty = "medium"
        elif self.start == -50 and self.end == 50:
            difficulty = "hard"
    
        # Update the score for the current difficulty in the leaderboard
        leaderboard[difficulty] = min(score, leaderboard[difficulty])
    
        # Write the updated leaderboard back to the file
        with open(self.leaderboard_file, 'w') as file:
            json.dump(leaderboard, file)
    
        # Call the show_best_score method with the updated leaderboard and current difficulty
        self.show_best_score(leaderboard, difficulty)

    def show_best_score(self, leaderboard, difficulty):
        if leaderboard[difficulty] < float('inf'):
            print(
                f"The best score so far in {difficulty} mode is "
                f"{leaderboard[difficulty]} guesses.")   

if __name__ == "__main__":
    # Use the Figlet library to generate ASCII art for the welcome message 
    f = Figlet(font='slant')
    print(f.renderText('Welcome to Guess the Number Game!'))
    # Create an instance of the GuessTheNumberGame class
    game = GuessTheNumberGame()
    # Start the game by calling the play method
    game.play()
