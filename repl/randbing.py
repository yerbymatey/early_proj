import random, os, time

print("bingo game")

bingoNumbers = []
#initializing bingo grid

def randBingGen():
  aNumber = random.randint(1, 90)
  return aNumber
  #function to generate a random number from 1 to 90, aNumber is result of running randBingGen()
def createCard():
  global bingoNumbers
  numbers = []
  #place to store randBingGen() results
  
  while len(numbers) <= 8 :
    genNumber = randBingGen()
    randBingGen()
    if genNumber not in numbers:
      randBingGen()
      numbers.append(genNumber)
      numbers.sort()
    else:
      numbers.sort()
  #while the number of items in the list "numbers" is less than or equal to 8, set subroutine randBingGen() to variable "genNumber", run randBingGen(). if variable is not in list, run subroutine, append with result. else, sort the numbers(numbers will be sorted due to probability of duplicate numbers)
  
  bingoNumbers = [
    [numbers[0], numbers[1],numbers[2]],      [numbers[3], "bingo",numbers[4]],         [numbers[5],numbers[6],numbers[7]]
  ]
# create the bingo list as a 3d matrix, center cell is bingo, bingoNumbers has 3 rows with 3 item per row
  for row in bingoNumbers:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()
createCard()

  
bingo = False

while not bingo:
  whatNumber = input("what number did u pull out \n")
  time.sleep(0.5)
  os.system("clear")
  
  for item in bingoNumbers:
    if whatNumber in item:
      location = item.index(whatNumber)
      bingoNumbers[location] = ("X")
      time.sleep(1)
      os.system("clear")
  
  for row in bingoNumbers:
    if bingoNumbers == 'X':
      print("bingo")
      bingo = True
      break

      





    
    
    

