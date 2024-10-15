# Classify persons age group: Child(< 13), Teenager(13 - 19), Adult(20-59) and Senior(60+)

userAge = int(input("Enter the age of person: " ))

if userAge < 13:
  print("Child")

elif userAge < 20:
  print("Teenager")

elif userAge < 60:
  print("Adult")

else:
  print("Senior")