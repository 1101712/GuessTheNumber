import random
import json
import argparse


class GuessTheNumberGame:
    def __init__(self, start=1, end=100):
        # Set the lower and upper limits for the random number
        self.start = start
        self.end = end
        # Generate a random number within the specified range
        self.target = random.randint(self.start, self.end)
        # Initialize an empty list to store the guesses
        self.guesses = []
        self.leaderboard_file = "leaderboard.json"

    def check_guess(self, guess):
        # Validate the guess: it must be within the specified range
        if guess < self.start or guess > self.end:
            return False, "Your guess is out of bounds. Try again."
        # If the guess is less than the target, it's too low
        elif guess < self.target:
            return True, "Too low! Try again."
        # If the guess is more than the target, it's too high
        elif guess > self.target:
            return True, "Too high! Try again."
        # If none of the above conditions are met, the guess is correct
        else:
            return True, "Congratulations! You've guessed the number!"

    def play(self):
        # Start an infinite game loop
        while True:
            try:
                # Ask the user to guess a number within the specified range
                guess = int(input(
                    f"Guess the number I'm thinking of between {self.start}"
                    f"and {self.end}: "))
                # Check the validity of the guess and get the corresponding
                # message
                valid, result = self.check_guess(guess)
                # If the guess is valid (in bounds), append it to the list
                # of guesses
                if valid:
                    self.guesses.append(guess)
                print(result)
                # If the guess is correct, end the game loop
                if result == "Congratulations! You've guessed the number!":
                    self.update_leaderboard(len(self.guesses))  # Update the
                    # leaderboard with the number of guesses
                    break
            # Handle the case where the user's input can't be converted
            # to an integer
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
        # A try/except block is used to handle errors that might occur
        # when attempting to open the file.
        try:
            # The open() function is used with 'r' mode (read mode)
            # to attempt to open the file specified by 'self.leaderboard_file'.
            with open(self.leaderboard_file, 'r') as file:
                # If the file opens successfully, the json.load() function
                # is used to load the JSON data from the file.
                # The loaded data is expected to be a list of scores and is
                # assigned to the 'leaderboard' variable.
                leaderboard = json.load(file)
        # The FileNotFoundError exception is raised when the file specified
        # by 'self.leaderboard_file' does not exist.
        # This is expected to happen the first time this method is called,
        # as the file has not yet been created.
        # The json.JSONDecodeError exception is raised when
        # the json.load() function cannot parse the file's contents.
        # This could happen if the file is not formatted as valid JSON,
        # for example, if it was edited manually.
        # When either of these exceptions occur, an empty list is assigned
        # to the 'leaderboard' variable as a fallback.
        # This is because there are no scores to load from the file,
        # either because it does not exist,
        # or because its contents could not be read.
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or cannot be parsed,
            # start a new leaderboard
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
# Create an instance of ArgumentParser
# which will handle the command-line arguments.
# The description "Play a game of 'Guess the Number'"
# will be displayed when help is requested using -h or --help.


parser = argparse.ArgumentParser(
    description="Play a game of 'Guess the Number'."
)
# Add the command-line argument --start.
# The default=1 argument indicates that if the user doesn't provide a value
# for this argument, the default value of 1 will be used.
# The help argument provides a help text for this argument
# which will be displayed when help is requested.
parser.add_argument(
    '--start', type=int, default=1, help='The lower limit of the number range.'
)

# Add the command-line argument --end, similar to --start.
parser.add_argument(
    '--end', type=int, default=100, help='The upper limit of the number range.'
)

# The parse_args() method parses the arguments
# that were provided when the script was run and returns them as a namespace.
# In this namespace, the values of the arguments are accessible as attributes
# (e.g., args.start and args.end).
args = parser.parse_args()
# If this script is run directly (not imported as a module), start the game
if __name__ == "__main__":
    game = GuessTheNumberGame(args.start, args.end)
    game.play()