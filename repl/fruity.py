def print_color(color):
  if color =="y":
    print("\033[33m", end="")
  elif color =="r":
    print("\033[0;31m", end="")
  elif color =="g":
    print("\033[32m", end="")
  elif color =="p":
    print("\033[35m", end="")
  elif color =="b":
    print("\033[0;34m", end="")
  elif color == " ":
    print("\033[0m", end="")

myString = input("make a sentence pls: \n")
for letter in myString:
  print_color(letter.lower())
  print(letter, end="")
print()
