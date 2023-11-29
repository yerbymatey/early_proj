import random

print("should you buy that scratch-off")

guessCounter = 0
guessnumber = random.randint(1,5)

while True:
  number = int(input("pick a number"))
  if guessnumber < number :
    print("lower")
    guessCounter += 1
    continue
  elif guessnumber > number :
    print("higher")
    guessCounter += 1
    continue
  elif guessnumber == number :
    print("wow, u did it...")
    guessCounter += 1
    break
  elif guessnumber < 0 :
    exit()
  else: 
    print("i dont know how you did this. die")
print("it took you ", guessCounter, "tries")

##i dont know what happened here line 5 should have used 0 for the starting couunter number but the ex says to use 1..... also the else statement doesn't work when you use anythign other than an integer shrug emoji
