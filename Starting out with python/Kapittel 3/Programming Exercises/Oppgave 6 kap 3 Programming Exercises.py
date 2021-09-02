# Kap 3 Programming Exercises
# Oppgave 6 - Magic Dates

# The date June 10, 1960, is special becuase 
# when it is written in the following format,
# the month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter
# a month (in numeric form), a day and a 
# two-digit year. The program should then 
# determine wether the month times the day
# equals the year . If so, it should display
# a message saying the date is magic.
# Otherwise, it should display a message
# saying the date is not magic.

month = int(input('Enter a month in numeric form (1 through 12): '))
day = int(input('Enter a day (1 through 31): '))
year = int(input('Enter a year with 2 digits (e.g 60 for 1960 etc): '))

if month * day == year:
    print('The date is magic!')
else:
    print('The date is not magic.')