import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer_choice = random.randint(0, 2)
if user_choice == 0:
    if computer_choice == 0:
        print("Draw")
    if computer_choice == 1:
        print("You lose")
    if computer_choice == 2:
        print("You win")
if user_choice == 1:
    if computer_choice == 0:
        print("you win")
    if computer_choice == 1:
        print("draw")
    if computer_choice == 2:
        print("You lose")
if user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    if computer_choice == 1:
        print("you win")
    if computer_choice == 2:
        print("Draw")

