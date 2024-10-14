# Reverse the number using while loop

n = int(input("Enter the value of n: "))

while (n > 0):
  r = n % 10
  n = n // 10
  print(r, end=" ") #output: 4 3 2 1




