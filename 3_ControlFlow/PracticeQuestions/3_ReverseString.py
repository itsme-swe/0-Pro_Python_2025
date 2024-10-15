# Reverse string using loop

input_String = input("Enter the string: ")

revString = ""

for char in input_String:
  revString = char + revString  # yaha pae hum har char ko empty reverse string kae andar add kar rahe hai

print(revString)