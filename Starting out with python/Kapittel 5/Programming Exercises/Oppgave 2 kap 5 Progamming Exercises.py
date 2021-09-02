# Programming Exercises kap 5
# Oppgave 2 - Sales Tax Program Refactoring

# Programming Exercises #6 in Chapter 2 was 
# the sales tax program. For that exercise
# you were asked to write a program that
# calculates and displays the country and 
# state sales tax on a purchase. If you have
# already written that program, redesign it so
# the subtasks are in functions. If you have not
# already written that program, write it using functions.

# Code from Programming Exercises #6 chapter 2:
# purchase_total = float(input("What is the amount of the purchase excluded taxes? "))
# purchase_total_formatted = format(purchase_total, ",.2f")
# state_tax_unformatted = purchase_total * 0.05
# state_tax_formatted = format(state_tax_unformatted, ",.2f")
# country_tax_unformatted = purchase_total * 0.025
# country_tax_formatted = format(country_tax_unformatted, ",.2f")
# total_price_formatted = format(purchase_total + state_tax_unformatted + country_tax_unformatted, ",.2f")
# print(f"The total price to pay is {total_price_formatted}, whereas the state sales tax amounts for", \
#     f"{state_tax_formatted} of the price and the country sales tax amounts for {country_tax_formatted} of the price")

init = input('Enter y to calculate tax on the products: ')
while init == 'y' or init == 'Y':

    def state_tax(product_cost):
        tax = float(format(product_cost * 0.05, ',.2f'))
        return tax
    
    def country_tax(product_cost):
        tax = float(format(product_cost * 0.025, ',.2f'))
        return tax
    
    def total_cost():
        purchase_total = float(input("What is the amount of the purchase excluded taxes? "))
        state_tax_calculated = state_tax(purchase_total)
        country_tax_calculated = country_tax(purchase_total)
        total_cost_unformatted = purchase_total + state_tax_calculated + country_tax_calculated
        total_cost_formatted = format(total_cost_unformatted, ',.2f')
        print(f"The total price to pay is ${total_cost_formatted}, whereas the state sales tax amounts for", \
            f"${state_tax_calculated} of the price, and the country sales tax amounts for ${country_tax_calculated} of the price.")
        
    total_cost()

    init = input('Enter y to calculate tax on another product, else press enter: ')