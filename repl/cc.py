import os, time

def contactCardMaking():
  contactCard = {"name": "", "DOB":"", "number":"", "email":""}
  os.system("clear")
  time.sleep(0.5)
  contactCard["name"] = input("Input your name >\t").strip()
  os.system("clear")
  time.sleep(0.5)
  contactCard["DOB"] = input("Input your date of birth >\t").strip()
  os.system("clear")
  time.sleep(0.5)
  contactCard["number"] = input("Input your telephone number >\t").strip()
  os.system("clear")
  time.sleep(0.5)
  contactCard["email"] = input("Input your email >\t").strip()
  os.system("clear")
  time.sleep(0.5)
  contactCard["address"] = input("Input your address > \t").strip()
  os.system("clear")
  time.sleep(0.5)

  print(f"""hi, {contactCard['name']}, our dictionary says that you're born on {contactCard['DOB']}, we can call you at {contactCard['number']}, email {contactCard['email']}, or write to {contactCard['address']}.""")
  
contactCardMaking()
