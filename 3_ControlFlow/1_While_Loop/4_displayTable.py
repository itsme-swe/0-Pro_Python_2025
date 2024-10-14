# Print the table of n and take n as input from user.

n = int(input("Enter the value of n: "))
count = 1

while (count <= 10):
  print(n, "*", count, "=", n * count)
  count += 1

