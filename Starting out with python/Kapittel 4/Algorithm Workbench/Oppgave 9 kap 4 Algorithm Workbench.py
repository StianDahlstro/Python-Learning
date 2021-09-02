# Kap 4 Algorithm Workbench

# Oppgave 9
# Write code that prompts the user to enter a number 
# in the range of 1 through 100 and validate the input.

k_g = 'y'

while k_g == 'y' or k_g == 'Y':
    num = float(input('Enter a number in the range of 1 through 100: '))
    while num < 1 or num > 100:
        print('Error, invalid number. Number must be in the range 1 through 100.')
        num = float(input('Enter a number in the range of 1 through 100: '))
    print('The number entered is', num, 'and it is in the range of 1 through 100.')
    k_g = input('Enter y to keep going: ')