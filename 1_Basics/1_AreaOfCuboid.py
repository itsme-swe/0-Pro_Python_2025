# 🍁Taking input from user and finding the total surface area of Cuboid.

length = int(input("Enter the length of cuboid: "))

breadth = int(input("Enter the breadth of cuboid: "))

height = int(input("Enter the height of cuboid: "))


totalSurfaceArea = 2 * (length * breadth + length * height + breadth * height)

print("The total surface area of cuboid is: ",totalSurfaceArea)