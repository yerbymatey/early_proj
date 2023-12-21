print("people's names list lol")
print()

nameList = []

def printName():
  for name in nameList:
    print(name)
  print()
  
while True:
  firstName = input("what's ur first name?: \n").strip().capitalize()
  lastName = input("what's ur last name?: \n").strip().capitalize()
  if (f"{firstName} {lastName}") in nameList:
    print("sorry, that name's already on the list")
  else:
    nameList.append(f"{firstName} {lastName}")
  printName()
  
