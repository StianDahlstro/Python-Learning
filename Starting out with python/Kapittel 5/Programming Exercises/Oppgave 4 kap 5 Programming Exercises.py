# Programming Exercises kap 5
# Oppgave 4 - Automobile Costs

# Write a program that asks the user to enter the 
# monthly costs for the following expenses incurred
# from operating his or her automobile: 
# Loan Payment, Insurance, Gas, Oil, Tires, and maintenance.
# The program should then display the total monthly cost of 
# these expenses, and the total annual cost of these expenses.


def main():
    get_input()

def get_input():
    loan_payment = float(input('Enter the monthly loan payment for your automobile: $'))
    insurance = float(input('Enter the monthly cost for insurance on your automobile: $'))
    gas = float(input('Enter the monthly gas cost for your automobile: $'))
    oil = float(input('Enter the monthly cost for oil for your automobile: $'))
    tires = float(input('Enter the average monthly cost for tires for your automobile: $'))
    maintenance = float(input('Enter the average cost for monthly maintenance on your automobile: $'))
    calculate(loan_payment, insurance, gas, oil, tires, maintenance)

def calculate(loan, insurance, gas, oil, tires, maintenance):
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    total_year = total_monthly * 12
    display_total(total_monthly, total_year)

def display_total(month, year):
    print('The total monthly cost is on average $', format(month, ',.2f'), sep='')
    print('The total yearly average cost is $', format(year, ',.2f'), sep='')


main()