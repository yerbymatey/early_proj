from getpass import getpass

player_1 = getpass("hi player one, pick R, P, or S")
player_2 = getpass("hi player two, pick R, P, or S")

if (player_1 == "R" or player_1 == "r") and (player_2 == "P" or player_2 == "p"):
  print("player two wins")

elif (player_1 == "P" or player_1 == "p") and (player_2 == "R" or player_2 == "r"):
  print("player two wins")
  
elif (player_1 == "S" or player_1 == "s") and (player_2 == "P" or player_2 == "p"):
  print("player one wins")
  
else:
  print("type in R, P, or S......")
