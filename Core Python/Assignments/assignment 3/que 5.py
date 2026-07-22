#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))

if a==b==c:
    print("The triangle is equilateral.")
elif a==b or b==c or a==c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
