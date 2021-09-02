# Kap 3 Programming Exercises
# Oppgave 7 - Color Mixer

# The colors red, blue and yellow are known as the 
# Primary colors because they cannot be made by mixing other colors.
# When you mix two primary colors, you get a secondary color, as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.

# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user enters anything other than "red", "blue"
# or "yellow", the program should display an error message. 
# Otherwise, the program should display the name of the secondary color.

print('The primary colors are red, blue and yellow.')
primary_1 = input('Enter your first primary color in all lower case: ')
primary_2 = input('Enter your other primary color in all lower case: ')

if primary_1 + primary_2 == 'red' + 'blue' or primary_1 + primary_2 == 'blue' + 'red':
    print(f'The secondary color made by mixing {primary_1} and {primary_2} is purple.')
elif primary_1 + primary_2 == 'red' + 'yellow' or primary_1 + primary_2 =='yellow' + 'red':
    print(f'The secondary color made by mixing {primary_1} and {primary_2} is orange.')
elif primary_1 + primary_2 == 'blue' + 'yellow' or primary_1 + primary_2 == 'yellow' + 'blue':
    print(f'The secondary color made by mixing {primary_1} and {primary_2} is green.')
else:
    print('Error, incorrect input. Make sure you enter two different types of primary colors in all lower case.')
