# Kap 4 Programming Exercises

# Oppgave 11 - Calculating the Factorial of a Number
# In mathematics, the notation n! represents the 
# factorial of the nonnegative integer n.
# The factorial  of n is the product of all 
# the nonnegative integers from 1 to n.
# For example, 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040
# and 4! = 1 x 2 x 3 x 4 = 24
# Write a program that lets the user enter a nonnegative
# integer and then uses a for loop to calculate
# the factorial of that number. Display the factorial..

factorial = int(input('Enter a nonnegative integer to calculate the factorial of that number: '))
sum = 1

while factorial <= 0:
        print('Eror, invalid integer.')
        factorial = int(input('Enter a nonnegative integer to calculate the factorial of that number: '))

print('Factorial: \t \t \t Product:')
print('-----------------------------------------')
for num in range(1, factorial + 1):
    sum *= num
    print(num, '\t \t \t \t', format(sum, ','))