import time, os

toDo = []
#make a menu to ask if adding, viewing, moving, or editing a "todo"

def add():
  toDoItem = input("whats the task? :\n")
  dueDate = input("when's the due date? :\n")
  priority = input("what's the priority? :\n")
  row = [toDoItem, dueDate, priority]
  toDo.append(row)
  print("ur task has been added!")
  #if choose add, prompt user to input what todo is, when it's due, and priority, then add to list

def view():
  whichView = input("would you like to view all or by priority? enter 1 for all and 2 for priority.")
  if whichView == "1".strip():
    for row in toDo:
      for item in row:
        print(item, end = " | ")
      print()
  elif whichView == "2".strip():
    whichPriority = input("what priority would uu wanna sort by?")
    for row in toDo:
      if whichPriority in row:
        for item in row:
          print(item, end = " | ")
        print()
    
#if choose view, make view all and view priority
#edit lets info change in "todo"
def edit():
    whichEdit = input("which task do u wanna edit? :\n")
    found = True
    for row in toDo:
    # if whichEdit in toDo:
      # whatEdit = input(f"what do you want to chnange {whichEdit} to? :\n")
      # location = toDo.index(whichEdit)
      # toDo[location] = whatEdit
      # print(f"ok! task edited from {whichEdit} to {whatEdit}. :\n")
      if whichEdit == row[0]:
        found = True 
        toDo.remove(row)
        whatEdit = input("what's the new task?")
        newDate = input("what's the new due date?")
        newPriority = input("what's the new priority?")
        toDo.append([whatEdit, newDate, newPriority])
        print("task updated")
    if not found:
      print("task is not on the list lol")
    #changes info in any one "todo"
def remove():
    whichRemove = input("which task do you want to remove? :\n")
    for row in toDo:
      if whichRemove in row:
        toDo.remove(row)
#remove completely removes a "to do" when it's "to done"
while True:
  menu = input("want to add, view, edit, or remove a todo? if u also wanna leave the menu say quit:\n")
  if menu == "add".strip().lower():
    add()
    time.sleep(2)
    os.system("clear")
  elif menu == "view".strip().lower():
    view()
    time.sleep(2)
    os.system("clear")
  elif menu == "edit".strip().lower():
    edit()
    time.sleep(2)
    os.system("clear")
  elif menu == "remove".strip().lower():
    remove()
    time.sleep(2)
    os.system("clear")
  elif menu == "quit".strip().lower():
    break

