print("super subroutine")
print()
print("with my ")

#in subroutine print_color with variables word and color
def print_color(word, color):
  #if print_color(word, **color**) is yellow
  if color =="yellow":
    #print the word in color, immediately string next argument and end color
    print("\033[33m", word, sep="", end="")
  elif color =="purple":
    print("\033[35m", word, sep="", end="")
  elif color =="green":
    print("\033[32m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

#print_color(word= lemons..., color = yellow)
print_color("lemons slkdjflasjf;lsjf;alsdkf ", "yellow")
print_color("weehaw ", "purple")
print_color("weehaw ", "green")
print_color("weehaw ", "fuck u")



