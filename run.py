import random

class GuessTheNumberGame:
    def __init__(self, low_limit=1, high_limit=10):
        # Set the lower and upper limits for the random number
        self.low_limit = low_limit
        self.high_limit = high_limit
        
        # Generate a random number within the specified range
        self.target = random.randint(self.low_limit, self.high_limit)
        
        # Initialize an empty list to store successful guesses
        self.guesses = []

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
            # Append the successful guess to the guesses list
            self.guesses.append(guess)
            return "Congratulations! You've guessed the number!"

    def play(self):
        # Start an infinite game loop
        while True:
            try:
                # Ask the user to guess a number within the specified range
                guess = int(input(f"Guess a number between {self.low_limit} and {self.high_limit}: "))
                
                # Check the user's guess and get the result
                result = self.check_guess(guess)
                print(result)
                
                # If the guess is correct, end the game loop
                if result == "Congratulations! You've guessed the number!":
                    break
            # Handle the case where the user's input can't be converted to an integer
            except ValueError:
                print("Invalid input. Please enter a number.")
            # Handle any other exceptions that occur during the game
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
                # Print the number of successful guesses made so far
                print(f"You have made {len(self.guesses)} guesses.\n")

# If this script is run directly (not imported as a module), start the game
if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.play()