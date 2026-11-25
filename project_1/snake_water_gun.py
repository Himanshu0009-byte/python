list_of_games=["snake","water","gun"]
choice_of_user=str(input("Enter the choice of user:"))
import random

choices = ["snake", "water", "gun"]
computer_choice = random.choice(list_of_games)
if choice_of_user==computer_choice:
    print("Draw Game")
elif (choice_of_user == "snake" and computer_choice == "water") or \
     (choice_of_user == "water" and computer_choice == "gun") or \
     (choice_of_user == "gun" and computer_choice == "snake"):
    print("You Win!")

else:
    print("Computer Wins!")