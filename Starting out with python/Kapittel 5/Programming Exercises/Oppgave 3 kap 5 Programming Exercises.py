# Programming Exercises kap 5
# Oppgave 3 - How Much Insurance?

# Many financial experts advise that property owners should
# insure their homes or buildings for at least 80 percent
# of the amount it would cost to replace the structure.
# Write a program that asks the user to enter the replacement 
# cost of a building and then displays the minimum amount
# of insurance he or she should buy for the property.

def main():
    replacement_cost = int(input('Enter the cost of replacing the property: $'))
    eighty_percent = min_insurance(replacement_cost)
    print(f'The minimum amount of insurance you should buy for the property is ${eighty_percent}.')

def min_insurance(cost_to_replace):
    eighty_percent = format(cost_to_replace * 0.8, ',.0f')
    return eighty_percent

main()