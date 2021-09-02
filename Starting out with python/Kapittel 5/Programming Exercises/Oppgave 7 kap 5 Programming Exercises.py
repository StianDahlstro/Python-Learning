# Programming Exercises kap 5
# Oppgave 7 - Stadium Seating

# There are three seating categories at a stadium.
# For a softball game, Class A seats cost $20,
# Class B seats cost $15, and Class C seats cost $10.
# Write a program that asks how many tickets for each class 
# of seats were sold, and then displays the amount
# of income generated from ticket sales.

def main():
    # The main function will call functions that asks 
    # how many seats were sold, and then store them in variables.
    # The main function should then call functions with the variables
    # as arguments that calculate the income from each seat class,
    # store them in variables and then calculate the total.
    seats_A = class_a_seats()
    seats_B = class_b_seats()
    seats_C = class_c_seats()
    class_A_income = a_income(seats_A)
    class_B_income = b_income(seats_B)
    class_C_income = c_income(seats_C)
    total_income = collective_income(class_A_income, class_B_income, class_C_income)
    display_seats(seats_A, seats_B, seats_C)
    display_income(total_income, class_A_income, class_B_income, class_C_income)


def class_a_seats():
    return int(input('Enter the amount of Class A seats sold: '))

def class_b_seats():
    return int(input('Enter the amount of Class B seats sold: '))

def class_c_seats():
    return int(input('Enter the amount of Class C seats sold: '))

def a_income(a_seats):
    return a_seats * 20

def b_income(b_seats):
    return b_seats * 15

def c_income(c_seats):
    return c_seats * 10

def collective_income(a_income, b_income, c_income):
    return a_income + b_income + c_income

def display_seats(a, b, c):
    total_seats = a + b + c
    print(f'The total amount of seats sold for the event is {total_seats},', \
        f'where {a} is the seats sold in Class A, {b} is the seats sold in Class B,', \
            f'and {c} is the amount of Class C seats sold.')

def display_income(total, a, b, c):
    print(f'The seats sold collectively earned ${total}, where Class A seats earned', \
        f'${a}, Class B seats earned ${b}, and Class C seats earned ${c}.')

main()