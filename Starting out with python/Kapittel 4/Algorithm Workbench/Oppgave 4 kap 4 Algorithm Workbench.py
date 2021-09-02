# Kap 4 Algorithm Workbench

# Oppgave 4
# Write a loop that asks the user to enter a number.
# The loop should iterate 10 times and keep a 
# running total of the numbers entered.

accumulator = 0

for i in range(10):
    num = float(input("Enter a number you want to the total: "))
    accumulator += num
    print('The current accumulated total is:', format(accumulator, ',.2f'))