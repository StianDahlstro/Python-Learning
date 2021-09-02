# Programming Exercises kap 5
# Oppgave 1 - Kilometer to Miles Converter

# Write a program that asks the user to enter
# a distance in kilometers, and then converts 
# that distance to miles.
# The conversion formula is as follows:
# Miles = Kilometers x 0.6214

def km_to_miles(km):
    return km * 0.6214

kilometers = float(input('Enter the number of kms you want converted to miles: '))
print(km_to_miles(kilometers))