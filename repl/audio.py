from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    if choice == 2: 
      source.paused = True
    else:
      continue
      
while True:
  # clear the screen 
  os.system("clear")
  # Show the menu

  print("hiiiiiiii this plays music ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  # take user's input
  choice = int(input())
  if choice == 1:
    play()
    # continue
  elif choice == 2:
    exit()
  else:
    continue
  
  # check whether you should call the play() subroutine depending on user's input

