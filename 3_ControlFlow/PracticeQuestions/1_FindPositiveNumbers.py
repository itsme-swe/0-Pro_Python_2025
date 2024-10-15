# Given a list of positive numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positiveNums = 0

for i in numbers:
  if i > 0:
    positiveNums += 1
print("Final count of positive number is: ", positiveNums)