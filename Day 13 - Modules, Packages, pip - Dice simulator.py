# Dice simulator
import random

print("Welcome to Dice Simulator 🎲")

while True:
    choice = input("Do you want to roll the dice? (y/n)):")
    if choice.lower() == "y":
        num = random.randint(1, 6)
        print(f"You rolled {num}!")
    elif choice.lower() == "n":
        break
    else:
        print("Please provide correct input.")

print("\nThank you for playing!")
        