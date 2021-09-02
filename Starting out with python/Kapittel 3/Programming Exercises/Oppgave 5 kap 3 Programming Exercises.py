# Kap 3 Programming Exercises
# Oppgave 5 - Mass and Weight

# Scientists measure an object's mass in
# kilograms and it's weight in newtons.
# If you know the amount of mass of an object
# in kilograms, you can calculate it's weight
# in newtons with the following formula:
# weight = mass * 9.8
# Write a program that asks the user to enter 
# an object's mass, and then calculate its weight.
# If the object weighs more than 500 newtons, 
# display a message indicating that it is too heavy.
# If the object weighs less than 100 newtons,
# display a message indicating that the object is too light.

mass_kg = float(input("Enter the object's mass in kilograms. "))
weight = mass_kg * 9.8

if weight >= 100 and weight <= 500:
    print("The object's weight is in an acceptable range.")
elif weight > 500:
    print("The object is too heavy.")
elif weight < 100 and weight > 0:
    print('The object is too light.')
else:
    print('Invalid weight. Input mass needs to be a positive number.')