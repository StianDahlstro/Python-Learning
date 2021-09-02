# Kap 5 Algorithm Workbench
# Oppgave 1

# Write a function named times_ten.
# The function should accept an argument 
# and display the product of the argument times 10.


def times_ten(x):
    print(x * 10)

number = float(input('Enter any number you want multiplied by ten: '))

if number != "":
    times_ten(number)