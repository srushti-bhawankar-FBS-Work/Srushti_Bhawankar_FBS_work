#3. Write a program to input angles of a triangle and check whether triangle is valid or not.
a=int(input("Enter the angle1:"))
b=int(input("Enter the angle2:"))
c=int(input("Enter the angle3:"))

if a+b+c==180:
    print('The triangle is valid')
else:
    print('The triangle is not valid')
