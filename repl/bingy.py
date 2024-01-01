Skip to content

Search & run commands
⌘
K

YE

yellowstripesbl
.config
.tutorial
venv
main.py
Packager files
poetry.lock
pyproject.toml
Config files
.replit
replit.nix
import random

print("gene's nan's bingo card generator")

randBing = []
#initialize an empty list to supply the bingo grid

def randBingGen():
  aNumber = random.randint(1, 90)
  return aNumber
  #function to generate a random number from 1 to 90, aNumber is result of running randBingGen()

def bingoOrg():
  for row in bingoNumbers:
    print(row)
#for every item in the list bingoNumbers print item
eight = 8

while len(randBing) <= 8 :
  genNumber = randBingGen()
  randBingGen()
  if genNumber not in randBing:
    randBingGen()
    randBing.append(genNumber)
  else:
    randBing.sort()



# for i in randBing:
#   number = randBingGen()
#   if number not in randBing:
#     randBing.append(number)
#   #for 8 times (8 numbers required for the bingo board), add the result(aNumber) from the function randBingGen() to the randBing list
  
randBing.sort()
#sort the numbers in randBing in ascending order

bingoNumbers = [
  [randBing[0],randBing[1],randBing[2]],      [randBing[3], "bingo",randBing[4]],         [randBing[5],randBing[6],randBing[7]]
]
#create the bingo list as a 3d matrix, center cell is bingo, bingoNumbers has 3 rows with 3 item per row

bingoOrg()
#bingo card should be displayed on screen when ran

icon

Day43_100Days
YE

yellowstripesbl
yellowstripesbl
Jan 1, 2024
·
Forked from 
replit
/
Day43_100Days
Day43_100Days - Replit

