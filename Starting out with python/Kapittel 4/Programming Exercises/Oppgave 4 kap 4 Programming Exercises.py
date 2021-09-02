# Kap 4 Programming Exercises

# Oppgave 4 - Distance Traveled
# The distance a vehicle travels can be calculated as follows:
#       Distance = speed x time
# For example, if a train travels 40 mph for three hours,
# the distance travelled is 120 miles.

# Write a program that asks the user for the speed of a vehicle
# (in mph) and the number of hours it has traveled. It should 
# then use a loop to display the distance the vehicle has traveled
# for each hour of that time period.

average_speed = float(input('What is the average speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))
total_distance = 0

print('Hour: \t \t Distance Traveled:')
print('-----------------------------------')

for hour in range(1, hours + 1):
    total_distance += average_speed
    print('%s\t\t\t%s' % (hour, total_distance))
    