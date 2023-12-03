realUsername = "genie"
realPassword = "no"


def login():
  while True:
    inputUsername = input("whats ur username")
    inputPassword = input("whats ur password")
    if inputUsername == realUsername and inputPassword == realPassword:
      print("welcome")
      break
    else:
      print("nope")
      continue
      
login()
