import random
#pick a category (cars with the most DUI'S)
carsWithMostDUI = {}

while True:
  #key field should be name
  car_names = ["Acura NSX", "Chevy Astro"]
  #data in subdictionary includes stats about the object
  #store info of two different objects in a 2d dictionary
  carsWithMostDUI[car_names[0]] = {
    "car": car_names[0],
    "modesty": random.randint(0,99),
    "speed": random.randint(0,99),
    "mpg": random.randint(0,99)
  }
  carsWithMostDUI[car_names[1]] = {
    "car": car_names[0],
    "modesty": random.randint(0,99),
    "speed": random.randint(0,99),
    "mpg": random.randint(0,99)
  }

  cardChoice = input(f"hey, pick a card: \n{car_names[0]}: 1, or {car_names[1]}: 2 \n")
  statChoice = input("choose a stat: \n 1. modesty \n 2. speed \n 3. mpg \n")
  #use infinite loop to get user to pick one of two cards, then pick stat from that card
  if cardChoice == "1":
    chosen_car = carsWithMostDUI[car_names[0]]
    other_car = carsWithMostDUI[car_names[1]]
  else:
    chosen_car = carsWithMostDUI[car_names[1]]
    other_car = carsWithMostDUI[car_names[0]]
    
  if statChoice == "1":
    stat_name = "modesty"
    chosen_stat = chosen_car["modesty"]
    other_stat = other_car["modesty"]
  elif statChoice == "2":
    stat_name = "speed"
    chosen_stat = chosen_car["speed"]
    other_stat = other_car["speed"]
  else:
    stat_name = "mpg"
    chosen_stat = chosen_car["mpg"]
    other_stat = other_car["mpg"]

#display chosen stat for both cars and output which wins
  print(f"{chosen_car['car']} has a {stat_name} stat of {chosen_stat}\n")
  
  print(f"{other_car['car']} has a {stat_name} stat of {other_stat}\n")

  if chosen_stat > other_stat:
    print(f"{chosen_car['car']} wins!")
  else:
    print(f"{other_car['car']} wins!")
  print()

  

  

