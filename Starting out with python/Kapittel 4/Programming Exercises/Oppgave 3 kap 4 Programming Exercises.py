# Kap 4 - Programming Exercises

# Oppgave 3 - Budget Analysis
# Write a program that asks the user to enter the
# amount that they have budgeted for a month.
# A loop should then prompt the user to enter each
# of their expenses for the month and keep a running total.
# When the loop finishes, the program should display the 
# amount that the user is over or under the budget.

budget = int(input('What is your budget for the next month? '))
expenses_accumulated = 0
more_expenses = 'y'

while more_expenses == 'y' or more_expenses == 'Y':
    expense = float(input('Enter the amount of the expense: '))
    expenses_accumulated += expense
    more_expenses = input('Do you have more expenses for the month? Enter Y if you do: ')

under_over_budget = budget - expenses_accumulated

if under_over_budget == 0:
    print('Your expenses turned out to be exactly equal to the budget.')
elif under_over_budget > 0:
    print('You are under the budget for the month with $', under_over_budget, ', Great Job!', sep='')
else:
    print('You are over budget for the month by -$', -under_over_budget, sep='')