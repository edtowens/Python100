# Guessing Game
import random
from art import logo
HARD_LEVEL = 5
EASY_LEVEL = 10
answer = random.randint(1,101)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "hard":
    attempts = HARD_LEVEL
else:
    attempts = EASY_LEVEL
    
for i in range(attempts, 0 , -1):
    guess = int(input(f"You have {i} attempts remaining to guess the number.\nMake a guess: "))
    if guess > answer:
        print("Too high.\nGuess again.")
    elif guess < answer:
        print("Too low.\nGuess again.")
    else:
        print("You've guessed correctly")
        quit()

print("You've run out of guesses, you lose.")