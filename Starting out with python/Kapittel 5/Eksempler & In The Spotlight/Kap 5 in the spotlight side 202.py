# Kap 5 In the spotlight
# Passing an argument to a Function

# This progam converts cups to fluid ounces
def main():

    # Display the intro screen
    intro()

    # Get the number of cups
    cups_needed = int(input('How many cups do you need? '))

    #Convert the cups to ounces
    cups_to_ounces(cups_needed)

# The intro function displays an introductory screen
def intro():
    print('This program converts measurments from cups to ounces.')
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'The amount of ounces needed is {ounces}')

# Take ENTER as the input to call the function
function_call = input('Press enter to get the measurment calculator: ')

if function_call != True:
    main()