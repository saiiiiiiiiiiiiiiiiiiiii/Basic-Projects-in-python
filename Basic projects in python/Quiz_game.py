


# Computer Quiz Game
# Technical Definition
# Created a command-line quiz application in Python that evaluates user knowledge on computer-related acronyms. The application features a series of questions with predefined correct answers, awarding points for correct responses and tracking overall performance. It calculates and displays the final score, total attempts, successful attempts, and unsuccessful attempts, offering a simple yet interactive way to assess and improve computer terminology understanding.
print('************************************Welcome to my computer quiz!.********************************************')
playing = input('Do you want to play?.').lower()

if playing != 'yes':
  print('Okay, maybe some other time then!')
  quit()

print("Okay let's play:) ")
score = 0
attempts = 0
successfull_attempts = 0
unsuccessfull_attempts = 0
answer = input("What does CPU stands for?").lower()
if answer == "central processing unit":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1

answer = input("What does RAM stands for?").lower()
if answer == "random access memory":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1

answer = input("What does ROM stands for?").lower()
if answer == "read only memory":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1


answer = input("What does HTTP stands for?").lower()
if answer == "hyper text transfer protocol":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1

answer = input("What does GUI stands for?").lower()
if answer == "graphical user interface":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1


answer = input("What does GPU stands for?").lower()
if answer == "graphics processing unit":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect! ")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1


answer = input("What does HTTPS stands for?").lower()
if answer == "hyper text transfer protocol security":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1


answer = input("What does TCP stands for?").lower()
if answer == "transmission control protocol":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1

answer = input("What does IP stands for?").lower()
if answer == "internet protocol":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  attempts = attempts + 1
  unsuccessfull_attempts = unsuccessfull_attempts + 1

answer = input("What does PS stands for?").lower()
if answer == "power supply":
  print("Correct! (+2)")
  attempts = attempts + 1
  score = score + 2
  successfull_attempts = successfull_attempts + 1
else:
  print("Incorrect!")
  unsuccessfull_attempts = unsuccessfull_attempts + 1
  attempts = attempts + 1



print(f"The final score is {score} Out of 20 ")
print(f"The Questions You Have attempted: {attempts}")
print(f"The Successfull Attempts:{successfull_attempts}")
print(f"The Unsuccessfull Attempts: {unsuccessfull_attempts}")