myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
tip = 1.2 * answer
tip = round(tip, 2)
print("You all owe", tip)
