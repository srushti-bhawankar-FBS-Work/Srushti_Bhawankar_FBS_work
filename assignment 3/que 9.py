#9. Input 5 subject marks from user and display grade(eg.First class,Second class.

sub1=int(input('Enter the sub1 marks:'))
sub2=int(input('Enter the sub2 marks:'))
sub3=int(input('Enter the sub3 marks:'))
sub4=int(input('Enter the sub4 marks:'))
sub5=int(input('Enter the sub5 marks:'))

if (sub1+sub2+sub3+sub4+sub5>=450):
    print('Student has passed with First class')
else:
    print('Student has passed with second class')