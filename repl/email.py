import os, time
listOfEmail = ["a","b","c"]

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)

# i misinterpreted this to mean that you create the subroutine for only ten emails, not that you should make the subroutine to send it to everyone on the list then to change the parameter inside of the subroutine "howManyEmail(max)" vs "howManyEmail(10)". still don't get why they used {i + 1} though, i guess that's to eliminate the counter 
def howManyEmail():
  os.system("clear")
  time.sleep(1)
  counter = 1
  for email in listOfEmail[:10]:
    print(f"""
Dear {email},
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III""")
    counter += 1
    time.sleep(2)
    os.system("clear")

    
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    howManyEmail()
      
  time.sleep(1)
  os.system("clear")


