#4. Write a program to enter P, T, R and calculate Compound Interest.
P=int(input("Enter the principal amount:"))
R=int(input("Enter the rate of interest:"))
T=int(input("Enter the time in years:"))


A= P * (1+R/100) ** T
CI=A-P


print("CI=", CI)