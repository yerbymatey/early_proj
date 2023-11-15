##old code

year = input("is this a leap year? ")
regular_year = 60 * 60 * 24 * 365
leap_year = 60 * 60 * 24 * 366
if year == "no" or year == "No":
  print(regular_year)
else:
  print(leap_year)


#so i think i keep defining certain variables without naming them i just put down the numerical value and not doing it step by step 
#making a lot of assumptions

print("this is a calculator to find out how many seconds are in a year")

seconds=60
minutes=60
hours=24
days=365
leapdays=366

year = input("is this a leap year? ")
if year == "yes" or year == "Yes":
  leap_year=seconds*minutes*hours*leapdays
  print(leap_year)
else:
  reg_year=seconds*minutes*hours*days
  print(reg_year)
  
