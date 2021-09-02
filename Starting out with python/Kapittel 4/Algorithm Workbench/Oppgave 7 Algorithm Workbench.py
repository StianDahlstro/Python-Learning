# Kap 4 Algorithm Workbench

# Oppgave 7 
# Write a program that accepts a number entered
# by the user and validates if it is odd or even. 
# If it is even, print a series up to 4 using range()
# and if it is odd, print a series up to 7.

num = int(input('Enter a random integer: '))

if num % 2 == 0:
    print('The number', num, 'is even, and the following 3 numbers are: ')
    for i in range(num, num + 4):
        print(i)
else:
    print('The number', num, 'is odd, and the following 6 numbers are: ')
    for i in range(num, num + 7):
        print(i)