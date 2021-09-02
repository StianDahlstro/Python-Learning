# Programming Exercises kap 5
# Oppgave 8 - Paint Job Estimator

# A painting company has determined that for every
# 112 square feet of wall space, one gallon of paint
# and 8 hours of labor will be required.
# The company charges $35.00 per hour for labor.
# Write a program that asks the user to enter
# The square feet of wall space to be painted
# and the price of paint per gallon.

# The program should then display the following data:
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job

def main():
    # Take input, save it in variables and use them as arguments when calling functions.
    # Do some easy calculations and pass the values as arguments to the display function.
    sq_feet_wall = float(input('Enter the amount of square feet you want painted: '))
    paint_cost_per_g = float(input('Enter the gallon price for the paint: $'))
    paint_buckets_amount = paint_buckets(sq_feet_wall)
    paint_cost = paint_buckets_amount * paint_cost_per_g
    hours_of_labor = labor_hours(sq_feet_wall)
    labor_cost = hours_of_labor * 35
    display_data(sq_feet_wall, paint_buckets_amount, paint_cost_per_g, paint_cost, hours_of_labor, labor_cost)


def paint_buckets(sq_feet):
    # This function takes the input value of square feet as an argument to 
    # calculate wether you need to buy more than one gallon of paint or not.
    # If you just need 1 more sq feet than the gallon supports, you need to buy
    # another gallon, as they come in gallon-buckets.
    # The function then returns the value of how many buckets are needed
    # to the variable in the main function, so it can be used in other functions.
    if sq_feet % 112 != 0:
        paint_buckets = (sq_feet // 112) + 1
    else:
        paint_buckets = sq_feet / 112
    return paint_buckets

def labor_hours(sq_feet):
    # This function takes the input value of square feet as an argument to 
    # calculate how many hours of labor it takes to paint the wall area.
    # The text says it takes 8 hours to paint 112 sq feet, which is 14 sq feet each hour.
    # The function then checks to see how many hours of work it is, 
    # and assuming you can only pay the company in full hours, even if the area to paint
    # is simply 1 sq feet over what comes to an hour, you'll need to "buy" a new hour.
    # The function then returns the value of how many labor hours are needed
    # to the variable in the maon function, so it can be used in other functions.
    sq_feet_an_hour = 112 / 8
    if sq_feet % sq_feet_an_hour != 0:
        hours_of_labor = (sq_feet // sq_feet_an_hour) + 1
    else:
        hours_of_labor = sq_feet / sq_feet_an_hour
    return hours_of_labor

def display_data(sq_feet, gallons, paint_cost, paint_cost_total, labor_hours, labor_cost):
    # This functions takes all the relevant variables in the main function as arguments,
    # and calculates the total cost of the project. It then displays all the data points
    # in the print statement.
    total_cost = paint_cost_total + labor_cost
    print(f'For painting {sq_feet} square feet of wall space with your desired paint, ' \
        f'the total cost is ${total_cost}. This price is the sum of labor cost, which amounts to ' \
            f'${labor_cost} based on the hourly labor rate and {labor_hours} hours of work,' \
                f'and paint cost, where you need to buy {gallons} gallons of paint, to the ' \
                    f'price of ${paint_cost}, amounting to ${paint_cost_total}.')

main()