# Kap 4 Algorithm Workbench

# Oppgave 1:
# Write a while loop that lets the user enter a number.
# The number should be multiplied by 10, and the result
# assigned to a variable named product.
# The loop should iterate as long as product is less than 100.

product = 0

while product >= 0 and product < 100:
    if product != 0:
        print(f'The product of the numbers {num} and 10 is:', format(product, '.2f'))
    num = float(input('Enter a number: '))
    product = num * 10
    