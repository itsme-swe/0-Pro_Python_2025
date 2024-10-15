# Movie tickets are priced are based on age: $12 for adults(18 and over), $8 for children. Everyone gets $2 discount on wednesday

userAge = int(input("Enter the age of user: "))

day = input("Enter the day: ").lower()

price = 12 if userAge >= 18 else 8

if day == "wednesday":
  price = price - 2

print(price)

