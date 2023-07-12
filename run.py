import random
import json

class GuessTheNumberGame:
    def __init__(self, low_limit=1, high_limit=100):
        # Set the lower and upper limits for the random number
        self.low_limit = low_limit
        self.high_limit = high_limit
        # Generate a random number within the specified range
        self.target = random.randint(self.low_limit, self.high_limit)
        # Initialize an empty list to store the guesses
        self.guesses = []
        self.leaderboard_file = "leaderboard.json"

    def check_guess(self, guess):
        # Validate the guess: it must be within the specified range
        if guess < self.low_limit or guess > self.high_limit:
            return "Your guess is out of bounds. Try again."
        # If the guess is less than the target, it's too low
        elif guess < self.target:
            return "Too low! Try again."
        # If the guess is more than the target, it's too high
        elif guess > self.target:
            return "Too high! Try again."
        # If none of the above conditions are met, the guess is correct
        else:
            return "Congratulations! You've guessed the number!"

    def play(self):
        # Start an infinite game loop
        while True:
            try:
                # Ask the user to guess a number within the specified range
                guess = int(input(f"Guess the number I'm thinking of between {self.low_limit} and {self.high_limit}: "))
                # Append the guess to the guesses list
                self.guesses.append(guess)
                # Check the user's guess and get the result
                result = self.check_guess(guess)
                print(result)
                # If the guess is correct, end the game loop
                if result == "Congratulations! You've guessed the number!":
                    self.update_leaderboard(len(self.guesses))  # Update the leaderboard with the number of guesses
                    break
            # Handle the case where the user's input can't be converted to an integer
            except ValueError:
                print("Invalid input. Please enter a number.")
            # Handle any other exceptions that occur during the game
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
                # Print the total number of guesses made so far
                print(f"You have made {len(self.guesses)} guesses.")

    def update_leaderboard(self, score):
        # This method updates the leaderboard and saves it to a file.
    
        # A try/except block is used to handle errors that might occur when attempting to open the file.
        try:
            # The open() function is used with 'r' mode (read mode) to attempt to open the file specified by 'self.leaderboard_file'.
            with open(self.leaderboard_file, 'r') as file:
                # If the file opens successfully, the json.load() function is used to load the JSON data from the file.
                # The loaded data is expected to be a list of scores and is assigned to the 'leaderboard' variable.
                leaderboard = json.load(file)
            
        # The FileNotFoundError exception is raised when the file specified by 'self.leaderboard_file' does not exist. 
        # This is expected to happen the first time this method is called, as the file has not yet been created.
        # The json.JSONDecodeError exception is raised when the json.load() function cannot parse the file's contents.
        # This could happen if the file is not formatted as valid JSON, for example, if it was edited manually.
        # When either of these exceptions occur, an empty list is assigned to the 'leaderboard' variable as a fallback.
        # This is because there are no scores to load from the file, either because it does not exist, or because its contents could not be read.
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or cannot be parsed, start a new leaderboard
            leaderboard = []

        # Append the new score
        leaderboard.append(score)

        # Write the updated leaderboard back to the file
        with open(self.leaderboard_file, 'w') as file:
            json.dump(leaderboard, file)

        # Show the best score
        self.show_best_score(leaderboard)

    def show_best_score(self, leaderboard):
        if leaderboard:
            print(f"The best score so far is {min(leaderboard)} attempts.")

# If this script is run directly (not imported as a module), start the game
if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.play()