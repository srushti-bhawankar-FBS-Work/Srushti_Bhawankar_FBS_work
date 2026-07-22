#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1=int(input('Enter the sub1 marks:'))
sub2=int(input('Enter the sub2 marks:'))
sub3=int(input('Enter the sub3 marks:'))
sub4=int(input('Enter the sub4 marks:'))
sub5=int(input('Enter the sub5 marks:'))

total= sub1+sub2+sub3+sub4+sub5
percentage=total/5

print("percentage=",percentage)

if percentage>=75:
    print('Distinction')
elif percentage>=60:
    print("First class")
elif percentage>=50:
    print("Second class")
else:
    print("Fail")
