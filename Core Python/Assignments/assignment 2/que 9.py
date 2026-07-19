#9. Write a program to swap two numbers without using third variable.
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

a=a + b
b=a - b
a=a - b

print("After Swapping")
print("a=",a)
print("b=",b)

#another method
x=10
y=20

print(f'Before Swapping:x={x},y={y},')
x,y=y,x
print(f'After Swapping:x={x},y={y},')