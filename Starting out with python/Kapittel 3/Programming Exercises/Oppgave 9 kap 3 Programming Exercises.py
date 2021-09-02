# Kap 3 Programming Exercises
# Oppgave 9 - Roulette Wheel Colors

# On a roulette wheel, the pockets are numbered
# from 0 to 36. The colors of the pockets are as follows:
# Pocket 0 is green
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red

# Write a program that asks the user to enter a pocket number and display wether the pocket is 
# green, red or black. The program should display an error message if the user enters a number
# that is outside of the range 0 through 36.

input_number = int(input('Enter a number in the range 0 through 36 to check what color the roulette wheel pocket has: '))

if input_number == 0:
    print("The pocket's color is green.")
elif 1 <= input_number <= 10 and input_number % 2 == 0:
    print("The pocket's color is black.")
elif 1 <= input_number <= 10 and input_number % 2 != 0:
    print("The pocket's color is red.")
elif 11 <= input_number <= 18 and input_number % 2 == 0:
    print("The pocket's color is red.")
elif 11 <= input_number <= 18 and input_number % 2 != 0:
    print("The pocket's color is black.")
elif 19 <= input_number <= 28 and input_number % 2 == 0:
    print("The pocket's color is black.")
elif 19 <= input_number <= 28 and input_number % 2 != 0:
    print("The pocket's color is red.")
elif 29 <= input_number <= 36 and input_number % 2 == 0:
    print("The pocket's color is red.")
elif 29 <= input_number <= 36 and input_number % 2 != 0:
    print("The pocket's color is black.")
else:
    print("Error. Invalid Number. Number must be within the range 0-36.")