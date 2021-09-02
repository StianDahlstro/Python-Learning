# Kap 3 Programming Exercises
# Oppgave 12 - Software Sales'

# A software company sells a package that retails for 
# $99. Quantity dicounts are given according to the 
# following table:

# Quantity:         Discount
# 10 - 19           10%
# 20 - 49           20%
# 50 - 99           30%
# 100 or more       40%

# Write a program that asks the user to enter the number
# of packages purchased. The program should then display 
# the amount of the discount (if any) and the total amount 
# of the purchase after the dicount.

units_sold = int(input('How many packages are you purchasing? '))
retail_price = 99
total_retail_price = units_sold * retail_price

if 10 <= units_sold <= 19:
    discount = 0.1
elif 20 <= units_sold <= 49:
    discount = 0.2
elif 50 <= units_sold <= 99:
    discount = 0.3
elif units_sold >= 100:
    discount = 0.4
else:
    discount = 0

total_discount = total_retail_price * discount
discounted_price = total_retail_price - total_discount

print(f'The total discount based on ', units_sold,  ' packages sold is $', format(total_discount, ',.2f'), ' and the total price is $', format(discounted_price, ',.2f'), sep='')