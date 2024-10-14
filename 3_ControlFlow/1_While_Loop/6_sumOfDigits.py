# Find sum of digits in a number 

n = int(input("Enter the value of n: "))

sum = 0
while (n > 0):
  r = n % 10
  n = n // 10
  sum += r

print("The sum of digits is: ", sum)