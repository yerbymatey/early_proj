import os, time

toDo = []

def print_color(color):
  if color =="yellow":
    return "\033[33m"

print(f"{print_color('yellow')}to do list manager")

def printList():
  for item in toDo:
    print(item)
  print()
  

while True:
  item = input("do you want to view, add, edit, remove an item from ur to do list?\n")
  if item == "view":
    printList()
    time.sleep(1)
    os.system("clear")
  elif item == "add":
    item = input("what do you want to add?:\n ")
    if item in toDo:
      print("u can't add duplicates, sorry")
    toDo.append(item)
    time.sleep(1)
    os.system("clear")
  elif item == "edit":
    item = input("what task did you want to edit?:\n ")
    if item in toDo:
      toDo.remove(item)
      addition = input(f"what did you want to replace {item} with?\n")
      toDo.append(addition)
    else:
      print(f"{item} doesn't exist in your list yet.")
      time.sleep(1)
  elif item == "remove":
    item = input("what did u want to remove?:\n ")
    if item in toDo:
      confirm = input(f"are u sure u want to remove {item}?\n")
      if confirm == "yes":
        toDo.remove(item)
    elif item == "everything":
      confirmDel = input("are u sure u want to delete everything?\n")
      if confirmDel == "yes":
        toDo.clear()
os.system("clear")
printList()
