# Oppgave 1 - Day of the week
# Write a program that asks the user
# for a number in the range of 1 through 7.
# The program should display the corresponding
# day of the week, where 1 = monday, 
# 2 = tuesday, etc. The program should display 
# an error message if the user enters a number 
# that is outside of the range 1 through 7.

input_number = int(input('Input a number in the range 1 through 7 to display the corresponding day: '))

if input_number == 1:
    print('Monday')
elif input_number == 2:
    print('Tuesday')
elif input_number == 3:
    print('Wednesday')
elif input_number == 4:
    print('Thursday')
elif input_number == 5:
    print('Friday')
elif input_number == 6:
    print('Saturday')
elif input_number == 7:
    print('Sunday')
else:
    print('Error, invalid number. Only numbers 1 through 7 have been assigned corresponding days.')