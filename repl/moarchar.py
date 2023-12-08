import random 
import os, time

def char():
  name = input("name ur character: ")
  time.sleep(1)
  races = ["human", "troll", "elf", "dwarf"]
  selected_race = random.choice(races)
  return name, selected_race
  
def dice(sides):
  dice_number = random.randint(1, sides)
  return dice_number
  
def health_stat():
  health = ((dice(6) * dice(12)) / 2) + 10
  return health
  
def strength_stat():
  strength = ((dice(6) * dice(12)) / 2) + 10
  return strength

print(char())
print("health", health_stat())
time.sleep(1)
print("strength", strength_stat())
time.sleep(1)

make_another = input("make another character?")

while make_another == "yes":
  os.system("clear")
  time.sleep(1)
  print(char())
  time.sleep(1)
  print("health", health_stat())
  time.sleep(1)
  print("strength", strength_stat())
  time.sleep(1)
  make_another = input("make another character?")
  time.sleep(1)

else:
  exit



##look at the formatting make the while True loop global and not just confined to running it again when the user is prompted if they wanna go again
