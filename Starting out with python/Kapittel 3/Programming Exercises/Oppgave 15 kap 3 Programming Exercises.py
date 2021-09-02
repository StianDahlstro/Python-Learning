# Kap 3 Programming Exercises
# Oppgave 15 - Time Calculator

# Write a program that asks the user to enter a number
# of seconds and works as follows:

# 1.    There are 60 seconds in a minute. If the number of seconds
#       entered by the user is greater than or equal to 60,
#       the program should display the number of minutrs in that many seconds.
# 2.    There are 3600 seconds in an hour. If the number of seconds
#       entered by the user is greater than or equal to 3600, 
#       the program should display the number of hours in that many seconds.
# 3.    There are 86400 seconds in a day. If the number of seconds entered
#       by the user is greater than 86400, the program should display the
#       number of days in that many seconds.

seconds = int(input('How many seconds do you want converted? '))

if 0 <= seconds < 60:
    converted = seconds
    print('The given number of seconds is less than a minute and the output is therefore the same as the input,', converted, 'seconds.')
elif seconds >= 60 and seconds < 3600:
    converted = seconds / 60
    print('The given number of seconds amounts to over a minute, but less than an hour. The input equals', format(converted, '.2f'), 'minutes.')
elif seconds >= 3600 and seconds < 86400:
    converted = seconds / 3600
    print('The given number of seconds amounts to over an hour but less than a day. The input then equals', format(converted, '.2f'), 'hours.')
elif seconds > 86400:
    converted = seconds / 86400
    print('The given number of seconds amounts to over a day. The input equals to', format(converted, '.2f'), 'days.')
else:
    print('Error, invalis input. The amount of seconds needs to be a positive integer.')