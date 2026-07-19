#5. Write a Program to input two angles from user and find third angle of the triangle.

angle1=int(input("Enter the first angle of the triangle:"))
angle2=int(input("Enter the second angle of the triangle:"))

angle3= 180-(angle1+angle2)

print("Third Angle=", angle3)

#Second Approach
A=int(input("Enter the first angle of the triangle:"))
B=int(input("Enter the second angle of the triangle:"))

C= 180-(A+B)

print("Third Angle=", C)
