# Programming Exercises kap 5
# Oppgave 9 - Monthly Sales Tax

# A retail company must file for a monthly sales tax report 
# listing the total sales for the month, and the amount of
# state and country sales tax collected. The state sales tax 
# rate is 5 percent and the country sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for
# the month. From this figure, the application should calculate
# and display the following:
# The amount of country sales tax
# The amount of state sales tax
# The total sales tax

def main():
    total_sales = float(input('Enter the total sales for the month: $'))
    s_tax = state_tax(total_sales)
    c_tax = country_tax(total_sales)
    t_tax = total_tax(s_tax, c_tax)
    display_data(s_tax, c_tax, t_tax)

def state_tax(income):
    return income * 0.05

def country_tax(income):
    return income * 0.025

def total_tax(state, country):
    return state + country

def display_data(state, country, total):
    print(f'The 5% state sales tax amounts to ${state}, ' \
        f'the 2.5% country tax amounts to ${country}, ' \
            f'and the total tax for the month is ${total}.')

main()