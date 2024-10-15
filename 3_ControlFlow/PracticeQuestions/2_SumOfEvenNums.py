# Calculate the sum of Even numbers upto a given n

n = int(input("Enter the value of n: "))

sum_EvenNums = 0

for i in range(1, n+1):
  if i % 2 == 0:
    sum_EvenNums += i

print("Sum of even number is: ", sum_EvenNums)
