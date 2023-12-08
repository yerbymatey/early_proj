import random, os, time

# def char():
#   name = input("name ur character: ")
#   time.sleep(1)
#   races = ["human", "troll", "elf", "dwarf"]
#   selected_race = random.choice(races)
#   return name, selected_race

def dice(sides):
  dice_number = random.randint(1, sides)
  return dice_number

def health_stat():
  health = ((dice(6) * dice(12)) / 2) + 10
  return health

def strength_stat():
  strength = ((dice(6) * dice(12)) / 2) + 10
  return strength

#character 1 definitions
character1 = input("what's ur character's name?: ")
character1_race = input("what's ur character's race?: ")
character1_health = health_stat()
character1_strength = strength_stat()
print()
print("ur character's name is ", character1)
print("ur character's race is ", character1_race)
print("ur character has ", character1_health, "HP.")
print("ur character has ", character1_strength, "STR.")
print()

#character 2 definition
character2 = input("what's ur character's name?: ")
character2_race = input("what's ur character's race?: ")
character2_health = health_stat()
character2_strength = strength_stat()
print()
print("ur character's name is ", character2)
print("ur character's race is ", character2_race)
print("ur character has ", character2_health, "HP.")
print("ur character has ", character2_strength, "STR.")

round = 1

while True:
  time.sleep(1)
  os.system("clear")
  print("fight lol")
  print()
  if round == 1:
    print("start fighting")
  else:
    print("continue fighting")
    
  character_1_roll = dice(6)
  character_2_roll = dice(6)

  damage_routine = abs(character1_strength - character2_strength)+1

  if character_1_roll > character_2_roll:
    print("character 1 goes first")
    character2_health -= damage_routine
    print("character 1 did ", damage_routine, "to character 2! ")
  else:
    print("character 2 goes first")
    character1_health -= damage_routine
    print("character 2 did ", damage_routine, "to character 1! ")
  if character2_health > character1_health and character2_health > 0:
    print(character2, "wins round ", round)
  elif character1_health > character2_health and character2_health > 0:
    print(character1, "wins round ", round)  
  if character1_health <= 0:
    print("character 2 wins after", round, "rounds")
    break
  elif character2_health <= 0:
    print("character 1 wins after", round, "rounds")
    break
  round += 1
  print(character1)
  print(character1_health)
  print(character2)
  print(character2_health)

