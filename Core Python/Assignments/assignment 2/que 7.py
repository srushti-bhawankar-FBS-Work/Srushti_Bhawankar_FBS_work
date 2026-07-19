#7. Find the sum of three-digit number.

num=int(input('Enter the three digit number:'))
digit_1=num//100
digit_2=(num//10)%10
digit_3=num%10

sum_digit=digit_1+digit_2+digit_3

print("Sum of three digit is:",sum_digit)