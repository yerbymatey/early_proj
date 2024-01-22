while True:
  #add 2-3 scores for testing in a loop
  #every new entry score should go on new line as "initials space score"
  initialText = input("input ur initials\n")
  #start new line for next entry
  scoreText = input("now input ur score\n")
  #save both values into a file called "high.score"
  #ask the user to input their three letter initials and score (out of ~100k)
  #use append mode, if file doesn't exist, it should be created. if it does, score should be added to the end
  f = open("high.score", "a+")
  f.write(f"{initialText}\n")
  f.write(f"{scoreText}\n")
  f.close()
  addAnother = input("added to high score table\n wanna add another? y/n?\n")
  #loop asks user if they've finished entering data and stop if they have
  if addAnother == "y":
    continue
  else:
    break










