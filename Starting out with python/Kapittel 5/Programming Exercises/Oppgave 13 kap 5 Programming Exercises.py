# Programming Exercises kap 5
# Oppgave 13 - Falling Distance

# When an object is falling because of gravity, the following
# formula can be used to determine the distance an object falls
# in a specific time period:
# d = 0.5 * g * t^2
# Where 'd' is the distance in meters, 'g' is 9.8 (gravitanional acceleration),
# and 't' is the amount of time, in seconds, that the object has been falling.
# Write a function named "falling distance" that accepts an object's
# falling time (in seconds) as an argument. The function should return
# the distance, in meters, that the object has fallen during that time interval.
# Write a program that calls the function in a loop that passes the values 
# 1 through 10 as arguments and displays the return value.

def main():
    for i in range(1, 11):
        distance = falling_distance(i)
        distance_format = format(distance, ',.1f')
        print(f'Distance in {i} seconds:    {distance_format}m')
        
def falling_distance(time):
    distance = 0.5 * 9.8 * (time ** 2)
    return distance

main()