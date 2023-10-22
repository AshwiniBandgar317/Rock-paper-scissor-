import random

options = ["rock", "paper", "scissor"]
print("select one option \n 1.Rock \n 2.Paper \n 3.Scissor")
user_input = input("Enter your option :")

computer_input = random.choice(options)

if user_input == computer_input:
    print("tie")

elif user_input == "rock" and computer_input == "paper":
    print("You win")

elif user_input == "rock" and computer_input == "scissor":
    print("You win")

elif user_input == "paper" and computer_input == "scissor":
    print("Computer win")

elif user_input == "paper" and computer_input == "rock":
    print("Computer win")

elif user_input == "scissor" and computer_input == "rock":
    print("Computer win")

elif user_input == "scissor" and computer_input == "paper":
    print("Computer win")
