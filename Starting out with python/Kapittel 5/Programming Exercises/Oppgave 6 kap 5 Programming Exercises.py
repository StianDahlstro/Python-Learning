# Programming Exercises kap 5
# Oppgave 6 - Calories from Fat and Carbohydrates

# A nutritionist who works for a fitness club helps members
# by evaluating their diets. As part of her evaluationm she asks
# members for the number of fat grams and carbohydrate grams
# that they consumed in that day. Then, she calculates the 
# number of calories that result from the fat,
# using the following formula:
# calories from fat = fat grams * 9
# Next, she calculates the number of calories that result from 
# the carbohydrates, using the following formula:
# calories from carbs = carb grams * 4
# The nutritionist asks you to write a program that will make these calculations.

def main():
    # The main function should call other functions to do tasks,
    # store the values in variables, then call a function to display the information.
    fat_calories = fat_grams_to_calories()
    carb_calories = carb_grams_to_calories()
    total_calories = kcal_total(fat_calories, carb_calories)
    display_kcals(fat_calories, carb_calories, total_calories)


def fat_grams_to_calories():
    return float(input('Enter the amount of fat grams you consumed this day: ')) * 9

def carb_grams_to_calories():
    return float(input('Enter the amount of carb grams you consumed this day: ')) * 4

def kcal_total(fat_kcals, carb_kcals):
    return fat_kcals + carb_kcals

def display_kcals(fat_kcals, carb_kcals, total):
    print('The total amount of kcals you had from fat and carbs was ', format(total, ',.2f'), \
        '. The total consisted of kcals from fat, which amounted to ', format(fat_kcals, ',.2f'), \
        ', and kcals from carbohydrates, which amounted to ', format(carb_kcals, ',.2f'), '.', sep='')


main()