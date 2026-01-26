# This program is a simple number guessing game, The computer selects a number and the user tries to guess it

import random                                                  # to generate random number
secret_number = random.randint(1, 50)                          # Generate a random number between 1 and 50
guess = 0                                                      # Initialize guess variable

while guess != secret_number:                                  
    guess = int(input("Guess a number between 1 and 50: "))    # Input: ask user to guess a number

    if guess < secret_number:                                  # Check if guess is too low or too high
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number correctly")
