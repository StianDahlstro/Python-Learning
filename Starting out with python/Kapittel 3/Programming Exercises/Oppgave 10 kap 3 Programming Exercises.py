# Kapittel 3 Programming Exercises
# Oppgave 10 - Money Counting Game

# Create a change-counting game that gets the user to enter
# the number of coins required to make exactly one dollar.
# The program should prompt the user to enter the number 
# of pennies, nickels, dimes and quarters. If the total value
# of the coins entered is equal to one dollar, the program should
# congratuate the user for winning the game. 
# Otherwise, the program should display a message indicating wether
# the amount entered was more than or less than 1 dollar.

pennies_value = 0.01
nickel_value = 0.05
dime_value = 0.1
quarter_value = 0.25

print('This game is about adding coins to amount to a total of 1 dollar, or 100 cents.')

pennies_amount = int(input('A penny is worth 1 cent. How many would you want to add? '))
nickel_amount = int(input('A nickel is worth 5 cents. How many would you like to add? '))
dime_amount = int(input('A dime is worth 10 cents. How many would you like to add? '))
quarter_amount = int(input('A quarter is worth 25 cents. How many would you like to add? '))

pennies_total_value = pennies_value * pennies_amount
nickel_total_value = nickel_value * nickel_amount
dime_total_value = dime_value * dime_amount
quarter_total_value = quarter_value * quarter_amount

total = pennies_total_value + nickel_total_value + dime_total_value + quarter_total_value
total_format = float(format(total, ',.2f'))

if total == 1:
    print('Congratulations! You successfully added coins together amounting to exactly 1 dollar!')
elif total < 1:
    print(f'Unfortunatly you did not successfully add enough coins to get exactly 1 dollar. You entered a total value of ${total_format}, missing $', format(1 - total_format, ',.2f'), sep='')
elif total > 1:
    print(f'Unfortunately you did not successfully add the right amount of coins to amount exactly 1 dollar. You entered a total value of ${total_format}, resulting in $', format(total_format - 1, ',.2f'), ' too much.', sep='')
else:
    print('Error.')