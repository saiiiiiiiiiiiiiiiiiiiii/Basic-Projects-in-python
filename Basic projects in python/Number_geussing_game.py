
# Project Name
# Number Guessing Game

# Description
# Created a command-line number guessing game in Python. The game generates a random number within a user-defined range and prompts the player to guess the number. It provides feedback on whether the guess is too high or too low, tracks the number of attempts, and informs the player when they guess correctly.




import random

attempt = 1
stop_range = input('Set a stop range: ')
if stop_range.isdigit():
  stop_range = int(stop_range)

else:
  print('Invalid Input!')
  print('Type Whole Number!')
  quit()

random_number = random.randint(0, stop_range)
print("Let's start!")

while True:
  guess = input('Guess a Number: ')
  if guess.isdigit():
    guess = int(guess)
  else:
    print('Invalid Input!')
    print('Type Whole Number!')

  if guess == random_number:
    print('You Won!')
    print(f"You Got it right in {attempt} attempt")
    break
  elif guess <= random_number:
    print('Too Low!')
    attempt = attempt + 1
  elif guess >= random_number:
    print('Too High!')
    attempt = attempt + 1
  else:
    print('Invalid Input!')
    attempt = attempt + 1



