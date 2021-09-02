# Programming Exercises kap 5
# Oppgave 14 - Kinetic Energy

# In physics, an object that is in motion is said to have kinetic energy.
# The following formula can be used to determine a moving object's kinetic energy:
# KE = 0.5 * m * v^2
# Where 'KE' is the Kinetic Energy, 'm' is the object's mass in kilograms,
# and 'v' is the object's velocity in meters per second.

# Write a function named 'kinetic_energy' that accepts an object's mass 
# (in kilograms) and velocity (in meters per second) as arguments. 
# The function should return the amount of kinetic energy that the object has.

# Write a program that asks the user to enter values for mass and velocity,
# and then calls the kinetic_energy function to get the object's kinetic energy.

def main():
    mass = float(input("Enter the object's mass in kilograms: "))
    velocity = float(input("Enter the object's velocity in meters per second: "))
    kin_en = kinetic_energy(mass, velocity)
    print(f'An object with the mass {mass}kg and the velocity {velocity}m/s, ' \
        f'has an estimated kinetic energy value of {kin_en} Joules.')

def kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

main()