import random 

randomNumber = int(input("how many sides"))
def rollDice(randomNumber):
  while True:
    print("you rolled", random.randint(1, randomNumber))
    choice = input("do u wanna try again")
    if choice == "yes":
      continue
    else:
      break
rollDice(randomNumber)
