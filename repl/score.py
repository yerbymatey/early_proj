print("this is a gradebook generator lol")

name = input("what's the name of the test?: ")
max_score = int(input("what's the maximum score you can get on this test?: "))
points_req = float(input("what's ur score?: "))

rounded_score = (points_req / max_score) * 100
print()
print(round(rounded_score, 2))
print ()
if (rounded_score >= 90):
  print("you got an A.......")
elif (rounded_score >= 80):
  print("you got a B.....")
elif (rounded_score >= 70):
  print("you got a C.....")
elif (rounded_score >= 60):
  print("you got a D.....")
else: 
  print("you suuuuuuck")
