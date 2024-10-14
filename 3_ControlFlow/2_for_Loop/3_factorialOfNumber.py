# Find the factorial of a given number 

n = int(input("Enter the value of n: "))

fact = 1

for ele in range(1, n+1):
  fact = fact * ele

print(fact)