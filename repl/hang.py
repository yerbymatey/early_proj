import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
# the list of words to be picked randomly from for wordChosen

wordChosen = random.choice(listOfWords)
# picks a random word from listOfWords

print("hangman............")
#takes user input to start solving the word?

word = []
#the array of combo of underscores and revealed letters
listOfLettersUsed = []
#make it not list the same letter more than once
lives = 6
#sets up counter for number of incorrect guesses
  
while True:
  inputLetter = input("pick a letter\n").lower()
  if inputLetter in listOfLettersUsed:
    print("you already chose this letter LOL")
    continue
  else:
    listOfLettersUsed.append(inputLetter)
    
  if inputLetter not in wordChosen:
    print("sorry lol")
    lives -= 1
    print(f"u have {lives} guesses left")
    #adds one guess to the counter on l 14
  
  found_letter = True
  
  for i in wordChosen:
    if i in listOfLettersUsed:
      print(i, end="")
    else:
      print("_", end="") 
      found_letter = False
  print()

  if found_letter:
    print("u won lol")
    break
  
  if lives <= 0:
    print(" u lost lol")
    break
      # if the incorrect guesses pass 6, player's booted out game



