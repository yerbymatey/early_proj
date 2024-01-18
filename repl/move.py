beastList = {}

print("mokebeast")
print()


def prettyPrint():
  print()
  
  for key, value in beastList.items():
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()
    #store multiple creatures using a loop
  
while True: 
  name = input("name :\t")
  type = input("type :\t")
  sMove = input("special move: \t")
  hP = input("HP :\t")
  mP = input("MP :\t")
  #get user input of beast details
  beastList[name] = {"Name:": name, "Type:": type, "Special Move:": sMove, "HP:": hP, "MP:":mP}
  #add details to 2D dictionary
  prettyPrint()
  quit = input("continue or quit? press 1 to continue or 2 to quit")
  if quit == "2":
    break
  


