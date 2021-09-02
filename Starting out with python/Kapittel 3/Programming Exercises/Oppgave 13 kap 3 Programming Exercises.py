# Kap 3 Programming Exercises
# Oppgave 13 - Shipping Charges

# The Fast Freight Shipping Company charges the following rates:

# Weight of package:            Rate per Pound:
# x <= 2                           $1.50
# 2 < x <= 6                       $3.00
# 6 < x <= 10                      $4.00
# 10 < x                           $4.75

# Write a program that asks the user to enter the weight 
# of a package and then display the shipping charges.

weight = int(input('How many pounds is the package (only full pounds)? '))

if 0 < weight <= 2:
    price_per_pound = 1.5
elif 2 < weight <= 6:
    price_per_pound = 3.0
elif 6 < weight <= 10:
    price_per_pound = 4.0
elif weight > 10:
    price_per_pound = 4.75
else:
    price_per_pound = 0

total_price = weight * price_per_pound

print('Based on the weight of the package, the total shipping cost is estimated to $', format(total_price, ',.2f'), sep='')