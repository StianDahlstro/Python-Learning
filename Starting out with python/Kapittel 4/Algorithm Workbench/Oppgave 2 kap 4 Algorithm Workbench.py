# Kap 4 Algorithm Workbench

# Oppgave 2
# Write a program that accepts two numbers by the user,
# checks if the denominator is zero, divides them and
# then prints their division. If the denominator is zero,
# it should promtpt the user "Division is not possible".

# 1. Input Numerator
# 2. Input Denominator
# 3. Check if the denominator is 0
#    If True --> Print "Division not possible"
# 4. Divide the numerator by the denominator
# 5. Print the division

denominator = 1

while denominator != 0:
    numerator = float(input('Enter any number for the numerator: '))
    denominator = float(input('Enter any number except 0 for the denominator: '))
    while denominator == 0:
        print('Error. Division not possible. Denominator cannot be 0.')
        numerator = float(input('Enter a number for the numerator: '))
        denominator = float(input('Enter a number for the denominator that is not 0: '))
    division = numerator / denominator
    print('The output of the division is: ', format(division, ',.3f'))