# Kap 4 Programming Exercises

# Oppgave 8 - Sum of Numbers
# Write a program woth a loop that asks the user
# to enter a series of positive numbers.
# The user should enter a negative number
# to signal the end of the series.
# After all the positive numbershave been entered,
# the program should display their sum.

sum = 0
num = 0

while num >= 0:
    num = float(input('Enter a positive number to add it to other numbers in the series. Enter a negative number to stop the series. '))
    sum += num

print('The sum of all the entered numbers are:', format(sum - num, ',.2f'))