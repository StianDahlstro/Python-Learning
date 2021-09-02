# Oppgaver kap 3
# Algorithm workbench


# Oppgave 1
# Write an if statement that checks if the
# Variable "a" is equal to 1. If it is equal
# to 1, print a message saying "a equals 1",
# else print "a is not equal to 1"

a = int(input('Give a random number between 0 to 2 to assign to the value "a". '))
if a == 1:
    print("a equals 1")
else:
    print("a is not equal to 1")


# Oppgave 2
# Write an if statement that checks if the 
# value "a" lies in the range of 10 to 30 
# and assign the value of the variable a to 20

a = 20
if 10 <= a <= 30:
    print('The value "a" is in the range of 10 to 30')
elif a < 10:
    print('The value "a" is less than 10')
elif a > 30:
    print('The value "a" is greater than 30')


# Oppgave 3
# Write an if-else statement that assigns 0
# to the variable "b" if the variable "a"
# is less than 10. Otherwise it should assign 
# 99 to the variable "b".

a = int(input('Assign a value to the variable "a" between 0 and 20. '))
if a < 10:
    b = 0
else:
    b = 99
print('Based on the value of variable "a", \n'
'variable "b" has been assigned the value', b)


# Oppgave 4
# The following code contains several nested if-else statements.
# Unfortunately, it was written without proper alignment and 
# indentation. Rewrite the code and use the proper conventions 
# of alignment and indentation.

# In this task I will use a nested if-else statements
# instead of if-elif-if statements.
a_score = 90
b_score = 80
c_score = 70
d_score = 60

score = int(input("What score did you get (0-100)? "))

if score >= a_score:
    print('Your grade is A.')
else:
    if score >= b_score:
        print('Your grade is B.')
    else:
        if score >= c_score:
            print('Your grade is C.')
        else:
            if score >= d_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# Oppgave 5
# Write an if-else statement that asks the user
# to enter the speed at which he is driving.
# If the speed is more (greater) than 50,
# print 'Speed in limit', else print 
# 'Speed should be checked'.

speed = float(input('What is the current speed? '))
speed_check_threshold = 50

if speed > speed_check_threshold:
    print('Speed in limit')
else:
    print('Speed should be checked')
# I honestly think the print outputs should
# be switched for the statements, 
# but this is the task description.


# Oppgave 6
# Write an if-else statement that displays 
# 'Speed is normal' if the speed variable 
# is within the range of 24 to 56.
# If the speed variable's value is outside
# this range, display 'Speed is abnormal'.

current_speed = float(input('What is your speed? '))
speed_low_range = 24
speed_high_range = 56

if speed_low_range <= current_speed <= speed_high_range:
    print('Speed is normal')
else:
    print('Speed is abnormal')


# Oppgave 7
# Write an if-else statement that determines
# wether the points variable is outside the
# range of 9 to 51. If the variable's value 
# is outside this range it should display
# "Invalid points". Otherwise, it should 
# display "Valid points".

points = int(input('How many points did you get? '))
low_range = 9
high_range = 51

if points >= low_range and points <= high_range:
    print('Valid points.')
else:
    print('Invalid points.')