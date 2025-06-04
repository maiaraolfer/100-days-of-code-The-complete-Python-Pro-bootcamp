print("Welcome to Rock, Paper, Scissors!")
input = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
input = int(input)  # Convert input string into an integer / whole number

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if input == 0:
    print("You chose Rock!")
    print(rock)
elif input == 1:
    print("You chose Paper!")
    print(paper)
else:
    print("You chose Scissors!")
    print(scissors)
    
    
import random
# Generate a random choice for the computer
computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("The computer chose Rock!")
    print(rock)
elif computer_choice == 1:
    print("The computer chose Paper!")
    print(paper)
else:
    print("The computer chose Scissors!")
    print(scissors)
    

# Determine the winner 0 = rock; 1 = paper; 2 = scissors

if input == 0 and computer_choice == 2: # 0-2
    print("You win! Rock beats Scissors.")
elif input == 0 and computer_choice == 1: # 0-1
    print("You lose! Paper beats Rock.")
elif input == 1 and computer_choice == 0: #1-0
    print("You win! Paper beats Rock.")
elif input == 1 and computer_choice == 2: #1-2
    print("You lose! Scissors beats Paper.")
elif input == 2 and computer_choice == 1: #2-1
    print("You win! Scissors beats Paper.")
elif input == 2 and computer_choice == 0: #2-0
    print("You lose! Rock beats Scissors.")
elif input >= 3 or input < 0: # invalid input
    print("Invalid input! Please choose 0, 1, or 2.")
else: # combinations 0-0, 1-1, 2-2
    print("It's a draw! You both chose the same.")