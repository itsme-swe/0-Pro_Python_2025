# Check if the number is palindrome(Palindrome stands for original value and the reveresed value is same)

n = int(input("Enter the value of n: "))

m = n

rev = 0
while (n > 0):
  rem = n % 10
  n = n // 10
  rev = rev * 10 + rem

print("Palindrome") if (m == rev) else print("Not palindrome")