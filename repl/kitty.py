
while exit != "yes":
  animal = input("what animal do u want?: ")
  if animal == "cat" or animal == "Cat":
    sound = "meow"
  elif animal == "snail" or animal == "Snail":
    sound = "................"
  else:
    print("pick a fuckin animal that I TOLD YOU TO CHOOSE FROM MY PROGRAM")
  print("a", animal, "goes", sound)
  exit = input("do u wanna leave?: ")

 
