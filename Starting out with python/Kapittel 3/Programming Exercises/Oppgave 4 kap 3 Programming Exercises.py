# Kap 3 Programming Exercises
# Oppgave 4 - Roman Numerals

# Write a prorgam that prompts the user
# to enter a number within the range of 
# 1 through 10. The program should display
# The Roman numeral version of that number.
# If the number is outside the range of 
# 1 through 10, the program should display
# an error message. The following table shows
# the Roman numerals for the numbers 1 through 10.

# Number        Roman Numeral
# 1             I
# 2             II
# 3             III
# 4             IV
# 5             V
# 6             VI
# 7             VII
# 8             VIII
# 9             IX
# 10            X

value = int(input('Enter a number 1 through 10 to see the equivalent Roman numeral. '))

if value == 1:
    print('I')
elif value == 2:
    print('II')
elif value == 3:
    print('III')
elif value == 4:
    print('IV')
elif value == 5:
    print('V')
elif value == 6:
    print('VI')
elif value == 7:
    print('VII')
elif value == 8:
    print('VIII')
elif value == 9:
    print('IX')
elif value == 10:
    print('X')
else:
    print('Invalid input number. Input an integer in the range 1 through 10.')