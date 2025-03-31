import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    while True:
        try:
            # Ask the user for a guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempts on each guess
            # Provide feedback
            if user_guess < random_number:
                print("Your guess is too low. Try again!")
            elif user_guess > random_number:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
number_guessing_game()