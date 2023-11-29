print("math lol")
multiple = int(input("pick a multiple: "))

trials = 0
for i in range (1, 11):
  realAnswer = i * multiple
  print(i, "X", multiple, "=")
  answer = int(input())
  if answer == realAnswer:
    print("niiiiice")
    trials += 1
  else:
    print("oopsie")

if trials == 10:
  print("wow. smort")
else:
  print("u scored", trials, " points out of 10")
