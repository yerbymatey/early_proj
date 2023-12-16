
def print_color(color):
  if color =="yellow":
    return "\033[33m"
  elif color =="red":
    return "\033[0;31m"
  elif color =="green":
    return "\033[32m"
  elif color =="light_red":
    return "\033[1;31m"
  elif color =="blue":
    return "\033[0;34m"
  else:
    return "\033[0m"

response = f"{print_color('red')}={print_color('bleh')}={print_color('blue')}={print_color('yellow')} Music App {print_color('blue')} ={print_color('white')}={print_color('red')}="

print(f"\t\t\t{response}")
print()
print(f"🔥▶️ \t{print_color('bleh')}Radio Gaga")
print(f"\t\t{print_color('yellow')}Queen")
print()
print()
previous = "PREV" 
next = "NEXT"
pause = "PAUSE"

print(f"{print_color('bleh')}{previous}")
print(f"{print_color('green')}{next:^12}")
print(f"{print_color('light_red')}{pause:^24}")


welcome = "WELCOME TO"
armbook = "--   ARMBOOK  --"

print()
print(f"{print_color('bleh')}{welcome:^35}")
print(f"{print_color('blue')}{armbook:^35}")
print()

definite = "Definitely not a rip off of"
aCertain = "a cerain other social"
networking = "networking site."
print(f"{print_color('yellow')}{definite:>40}")
print(f"{print_color('yellow')}{aCertain:>40}")
print(f"{print_color('yellow')}{networking:>40}")

honest = "Honest."
user = "Username:"
password = "Password:"

print()
print(f"{print_color('red')}{honest:^35}")
print()
print(f"{print_color('bleh')}{user:^35}")
print(f"{print_color('bleh')}{password:^35}")

##can i just use text every time? does it only recall the variable right before the f string is uhhh invoked
