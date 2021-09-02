# Programming Exercises kap 5
# Oppgave 12 - Maximum of Two Values

# Write a function named 'max' that accepts two integer values 
# as arguments and returns the value that is greater of the two.
# For example, if 7 and 12 are passed as arguments to the function,
# The function should return 12. Use the function in a program that 
# prompts the ser to enter two integer values.
# The program should display the value that is greater of the two.

def main():
    int_1 = int(input('Enter an integer: '))
    int_2 = int(input('Enter another integer: '))
    highest = max(int_1, int_2)
    display_highest(highest)

def max(int_1, int_2):
    if int_1 >= int_2:
        return int_1
    else:
        return int_2

def display_highest(highest):
    print(f'The highest number of the two entered is {highest}.')

main()