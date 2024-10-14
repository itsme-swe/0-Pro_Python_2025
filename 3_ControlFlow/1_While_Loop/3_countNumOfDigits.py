# Counting the number of digits
n = int(input("Enter the value of n: "))

count = 0
while (n > 0):
  n = n // 10
  count += 1

print("The number of digits inside n are:",count)

