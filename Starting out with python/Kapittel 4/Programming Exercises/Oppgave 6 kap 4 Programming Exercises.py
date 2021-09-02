# Kap 4 Programming Exercises

# Oppgave 6 - Celsius to Farenheit Table
# Write a program that displays a table of the Celsius
# temperatures 0 through 20 and ther Farenheit equivalents.
# The formula for converting a temperature from Celsius to 
# Farenheit is:
# F = 9/5 C + 32
# Where F is the Farenheit temperature and C is the Celsius
# temperature. Your program must use a loop to display the table.

for temp in range(21):
    farenheit = 9 / 5 * temp + 32
    print('Celsius temp: \t \t Farenheit temp:')
    print('%s \t \t \t %s' % (temp, format(farenheit, '.2f')))
    print(temp, '\t \t \t', farenheit)