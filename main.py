print("Mathematics Game! \n")
score = 0



try:
  multiplier = int(input("""Enter the number you'd 
  like to test your multiplication table with: > """ ))
except ValueError:
  print('That is not a number! Come back again when you are ready to play!')
  exit(1)
  

for i in range(1, 11):

  try:
     ans = int(input("What is " + str(i) + " X " + str(multiplier) + "?"))
  except ValueError:
    print('That is not a numer!')
    print('That is not a number! Come back again when you are ready to play!')
    exit(1)

 
  if ans == i * multiplier:
    score += 1
    print("Correct!\n")
  else:
    print("Sorry, wrong!\n")

print("You scored " + str(score) + " out of 10.")
if score == 10:
  print("You are a math genius! 🤓")