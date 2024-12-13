import random

tries = 0
success = False
gRandome = random.randint(1, 1000000)

for i in range(1, 11):
  tries = i
  guess = int(input("Guess a number between 0 and 1000000: "))

  if guess == gRandome:
    print("You guessed the number!")
    success = True
    break
  elif guess > gRandome:
    print("Too high!")
  elif guess < gRandome:
    print("Too low!")
  
  if not success:
    print("sadly you did not guess the number after", tries, "tries")
    
if success:
  print("You guessed the number in", tries, "tries! genius! 🧠")
else:
  print("You did not guess the number in 10 tries. 🐐!")
  