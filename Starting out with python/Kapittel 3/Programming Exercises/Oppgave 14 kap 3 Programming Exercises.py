# Kap 3 Programming Exercises
# Oppgave 14 - Body Mass Index

# Write a program that calculates and displays a person's
# Body Mass Index . The BMI is often used to determine 
# wether a person is overweight or underweight for their height.
# A person's BMI is calculated with the following formula:
# BMI = Weight * 703 / height^2
# Where weight is measured in pounds and height is measured in inches.

# The program should ask the user to enter the user's weight and
# height and then display the user's BMI.
# The program should also display a message indicating wether
# the person has optimal weight, is underweight or overweight.
# A person's weight is considered optimal if their BMI is in
# the range 18.5 - 25. If the BMI is less than the ideal range,
# the person is underweight and if the BMI is above the ideal range,
# the person is considered overweight.

weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

bmi = weight * (703 / (height ** 2))
bmi_format = format(bmi, '.2f')

if 0 < bmi < 18.5:
    print(f"Your BMI is {bmi_format}, and it indicates that you're underweight.")
elif 18.5 <= bmi <= 25.0:
    print(f"Your BMI is {bmi_format}, and it indicates that you're in the range of optimal weight.")
elif bmi > 25.0:
    print(f"Your BMI is {bmi_format}, and it indicates that you're overweight.")
else:
    print('Error. Invalid weight or height parameters.')