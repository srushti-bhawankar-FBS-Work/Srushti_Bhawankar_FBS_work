#2. Write a program to input any alphabet and check whether it is vowel or consonant.
ch=(input('Enter the albhabet:'))
if ch.lower() in ('a','e','i','o','u'):
    print('the alphabet is vowel.')
else:
    print('The alphabet is constant')
