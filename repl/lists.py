import os, time

toDo = []

def print_color(color):
  if color =="yellow":
    return "\033[33m"
## how to end color??

print(f"{print_color('yellow')} to do list manager")

def printList():
  for item in toDo:
    print(item)
  print()

while True:
  item = input("do you want to view, add, or edit your to do list?")
  if item == "view":
    printList()
    time.sleep(2)
    os.system("clear")
  elif item == "add":
    item = input("what do you want to add?: ")
    toDo.append(item)
    time.sleep(2)
    os.system("clear")
  elif item == "edit":
    item = input("what task did you want to edit?: ")
    if item in toDo:
      toDo.remove(item)
    else:
      print(f"{item} doesn't exist in your list yet.")
    time.sleep(2)
    os.system("clear")
printList()
