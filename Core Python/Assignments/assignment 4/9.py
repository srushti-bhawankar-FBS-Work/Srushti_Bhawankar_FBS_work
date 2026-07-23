#9. WAP to print all numbers in a range divisible by a given number.
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
num=int(input("Enter the number:"))
print("Numbers divisible by given number=",num,"are:")
for i in range(start,end+1):
    if i % num == 0:
        print(i)