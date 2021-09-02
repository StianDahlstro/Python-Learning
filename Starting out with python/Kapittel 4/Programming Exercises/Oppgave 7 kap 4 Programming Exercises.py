# Kap 4 Programming Exercises

# Oppgave 7 - Pennies for Pay
# Write a program that calculates the amount of money
# a person would earn over a period of time if their 
# salary is one penny the first day, two pennies the
# second day, and continues to double each day.
# The program should ask the user for the number of days.
# Display a table showing what the salary was for each day,
# and then show the total pay at the end of the period.
# The output should be displayed in a dollar amount,
# not the number of pennies.

pay = 0.01
total_pay = 0

days = int(input('How many days do you want to have the pay doubled for? '))

print('Day: \t \t \t Pay: ')

for day in range(1, days + 1):
    total_pay += pay
    print(day, '\t \t \t', pay)
    pay *= 2

print('The total pay after all the days are: $', format(total_pay, ',.2f'), sep='')