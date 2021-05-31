# game.py


import os

import dotenv

dotenv.load_dotenv()


Player_name = os.getenv("Player_Name")
print(Player_name)


print("--------------------")
print("Welcome " + Player_name + " to Rock, Paper, Scissors, Shoot!")
 
user_choice=input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOICE:",user_choice)


if (user_choice == "rock")  or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid. KEEP GOING")
else:
    print("OOPS, invalid input. Please Try again.")
    exit()

import random
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)


if(computer_choice==user_choice):
    print("It's a tie!")

elif(computer_choice=="rock"):
    if(user_choice=="scissors"):
        print("Rock beats scissors. You lose!")
    else:
        print("Paper beats rock. Congrats, you win!")

elif(computer_choice=="paper"):
    if(user_choice=="scissors"):
        print("Scissors beat paper. You win!")
    else:
        print("Paper beats rock. You lose!")


elif(computer_choice=="scissors"):
    if(user_choice=="paper"):
        print("Scissors beat paper. You lose!")
    else:
        print("Rock beat scissors. You win!")




print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")
