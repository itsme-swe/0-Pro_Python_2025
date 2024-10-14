# Reverse the given number 

n = int(input("Enter the value of n: "))

reverse = 0
while (n > 0):
  r = n % 10
  n =  n // 10
  reverse = reverse * 10 + r

print(reverse)
