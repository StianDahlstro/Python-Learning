# Kap 4 Algorithm Workbench

# Oppgave 8
# Write code that prompts the user to enter 
# a positive nonzero number and validates the input.


another_num = 'y'

while another_num == 'y' or another_num == 'Y':
    num = int(input('Enter a positive integer that is not 0: '))
 
    while num <= 0:
        print('The integer value you entered is:', num)
        print('The input value is not a natural number and you can therefore not proceed')
        num = int(input('Enter a positive integer that is not 0: '))
    
    print('The number entered is:', num)

    another_num = input('Enter y to keep going, else press any other key: ')