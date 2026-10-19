# The game has a secret number. 
# The player keep guessing until they get it right.
# The player is limited to five attempts
    # and give hints such as "too high" or "too low"

import random

# Generate a secret number between 1 and 20
secret_number = random.randint(1, 20)

attempts = 5

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20.")
print("You have 5 attempts to guess it.")

while attempts > 0 #Game continues as long the player ha attempts remaining
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        break

    elif guess > secret_number:
        print("Too high! Try a lower number.")

    else:
        print("Too low! Try a higher number.")

    attempts = attempts - 1

    if attempts > 0:
        print("Attempts remaining:", attempts)

if attempts == 0 and guess != secret_number:
    print("Game over! The secret number was", secret_number)
