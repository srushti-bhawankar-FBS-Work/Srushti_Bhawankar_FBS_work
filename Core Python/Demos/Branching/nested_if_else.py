gender=input('Enter gender(m/f):')
age=int(input('Enter age:'))
if(gender=='f'):
    if(age>=18):
        print('Girl is eligible for marriage.')
    else:
        print('Girl is not eligible for marriage.')

if(gender=='m'):
    if(age>=21):
        print('Boy is eligible for marriage.')
    else:
        print('Boy is not eligible for marriage.')