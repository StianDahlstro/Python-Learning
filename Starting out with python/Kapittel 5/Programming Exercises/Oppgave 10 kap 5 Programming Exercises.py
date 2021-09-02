# Programming Exercises kap 5
# Oppgave 10 - Feet to inches

# One foot equals 12 inches. Write a function named
# feet_to_inches that accepts a number of feet as
# an argument and returns the number of inches in 
# that many feet. Use the function in a program that
# prompts the user to enter a number of feet and then
# displays the number of inches in that many feet.

def main():
    feet = float(input('Enter the number of feet you want converted to inches: '))
    inches = feet_to_inches(feet)
    display(feet, inches)

def feet_to_inches(feet):
    return feet * 12

def display(feet, inches):
    print(f'{feet} feet is the same length as {inches} inches.')

main()