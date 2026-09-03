
import random

print("Welcome to Guess the Number Game!")

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🎉 Correct! You guessed it!")
else:
    print(f"❌ Wrong! The number was {secret_number}")