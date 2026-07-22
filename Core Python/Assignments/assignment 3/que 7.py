#7. Write a program to check if user has entered correct userid and password.
user_id=(input("Enter the user_id:"))
password=(input("Enter the password:"))

if user_id=='Admin' and password=='1234':
    print('Login succesfully')
else:
    print('The credentials does not match')
