# 
# Technical Name
# Rock-Paper-Scissors Game

# Description
# Implemented a Rock-Paper-Scissors game using Python, featuring a user interface for input and a computer opponent generating random choices. The game tracks and displays scores for both the user and computer, counts ties and attempts, and allows users to quit the game while showing final statistics.

import random
user_wins = 0
computer_wins = 0 
options = ["rock", "paper", "scissor"]
attempts = 0
tie = 0
while True:
  random_choice = random.randint(0,2)
  computer_choice = options[random_choice]
  user_choice = input("Enter a choice (rock, paper, scissor) or Quit: ").lower()
  if user_choice == "quit":
    print(f'Final User Score is {user_wins}')
    print(f'Final Computer Score is {computer_wins}')
    print(f"The total  {tie} tie games ")
    print(f"The {attempts} times you have attempted.")
    print("Try again later :)")
    quit()
  if user_choice not in options:
    print("Invalid choice")
    quit()
  if user_choice == 'rock' and computer_choice == 'scissor':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("User wins!")
    print("Computer Lost!")
    user_wins = user_wins + 1
    attempts = attempts + 1
    continue
  elif user_choice == 'paper' and computer_choice == 'rock':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("User wins!")
    print("Computer Lost!")
    user_wins = user_wins + 1
    attempts = attempts + 1
    continue
  elif user_choice == 'scissor' and computer_choice == 'paper':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("User wins!")
    print("Computer Lost!")
    user_wins = user_wins + 1
    attempts = attempts + 1
    continue
  elif user_choice == 'rock' and computer_choice == 'rock':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("It's a tie!")
    attempts = attempts + 1
    tie = tie + 1
    continue
  
  elif user_choice == 'paper' and computer_choice == 'paper':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("It's a tie!")
    attempts = attempts + 1
    tie = tie + 1
    continue
  elif user_choice == 'scissor' and computer_choice == 'scissor':
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print("It's a tie!")
    attempts = attempts + 1
    tie = tie + 1
    continue

  else:
    print(f"User chose ({user_choice}), computer chose ({computer_choice}).")
    print('User Lost!')
    print('computer wins')
    computer_wins = computer_wins + 1
    attempts = attempts + 1
    


  print(f'Final User Score is {user_wins}')
  print(f'Final Computer Score is {computer_wins}')
  print(f"The {attempts} times you have attempted.")
  print(f"The total {tie} tie games ")
