import random 

def statGen(sides):
  anyNumber = (random.randint(1, sides))
  return anyNumber
  
def sixAndEightDice():
  six = statGen(6)
  eight = statGen(8)
  health = six * eight
  return health

wantAnother = "yes"

while wantAnother == "yes":
  character = input("whats the nam eof ur character")
  health = str(sixAndEightDice())
  print("they have", health, "hp")
  wantAnother = input("another?")
