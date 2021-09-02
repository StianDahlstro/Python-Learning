# Kap 4 Progamming Exercises

# Oppgave 12 - Population
# Write a program that predicts the approximate
# size of a population of organisms.
# The application should use text boxes to allow 
# the user to enter the starting number of organisms,
# the average daily population increase (as a percentage),
# and the number of days the organisms will be left
# to multiply. For example, assume the user enters
# the following values:

# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10

# The progam should display the following table of data:

# Day approximate:              Population
# 1                             2
# 2                             2.6
# 3                             3.38
# 4                             4.394
# 5                             5.7122
# 6                             7.42586
# 7                             9.653619
# 8                             12.5497
# 9                             16.31462
# 10                            21.209

days = int(input('How many days will the organisms multiply for? '))
multiply_percentage = float(input('What is the average daily increase in the organisms? (enter the number in %) '))
starting_organisms = int(input('Enter the amount of organisms that are present when the ecperiment starts: '))
total_organisms = starting_organisms
multiply_rate = 1 + (multiply_percentage / 100)

print('Day approximate: \t \t \t Population of organisms')

for day in range(1, days + 1):
    if day > 1:
        total_organisms *= multiply_rate
    print(day, '\t \t \t \t', format(total_organisms, ',.5f'))