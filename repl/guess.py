from getpass import getpass

guessCounter = 0
guessnumber = int(input("hi pick nomber from 1 to 10k"))

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
print("it took u ", guessCounter, "tries")
