loan = 1000
apr = 0.05
for i in range(11):
  loan += (loan*apr)
  print(i+1, round(loan, 2))
