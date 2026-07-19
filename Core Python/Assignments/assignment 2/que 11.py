#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

Amount=int(input("Enter the amount:"))

n1000=Amount//1000
Amount=Amount%1000

n500=Amount//500
Amount=Amount%500

n100=Amount//100
Amount=Amount%100

n50=Amount//50
Amount=Amount%50

n10=Amount//10
Amount=Amount%10

print("1000 notes=", n1000)
print("500 notes=", n500)
print("100 notes=", n100)
print("50 notes=", n50)
print("10 notes=", n10)

