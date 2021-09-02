# Programming Exercises kap 5
# Oppgave 20 - Random Number Guessing Game

# Write a program that generates a random number in the range of 1 through 100,
# and asks the user to guess what the number is. If the user's guess is higher
# than the random number, the program should display "too high, try again". 
# If the user's guess is lower than the random number, the program should display
# "too low, try again". If the user guesses the number, the application should 
# congratulate the user and then generate a new random number so the game can start over.

# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that 
# the user makes. When the user correctly guesses the random number,
# the program should display the number of guesses.

import random

def main():
    rand_num = generate_num()
    guess_count = guess_num(rand_num)
    display_data(rand_num, guess_count)
    
def generate_num():
    return random.randint(1, 100)

def guess_num(rand_num):
    guess = int(input('Enter a number: '))
    guess_count = 1
    guess_bool = False
    while guess_bool == False:
        if guess < rand_num:
            print('Too low, try again.')
            guess_bool = False
            guess = int(input('Enter a number: '))
            guess_count += 1
        elif guess > rand_num:
            print('Too high, try again.')
            guess_bool = False
            guess = int(input('Enter a number: '))
            guess_count += 1
        else:
            print('Congratulations, that is the correct number!')
            guess_bool = True
    return guess_count

def display_data(rand_num, guess_count):
    if guess_count == 1:
        print(f'You guessed the correct number, {rand_num}. You used {guess_count} guess.')
    else:
        print(f'You guessed the correct number, {rand_num}. You used {guess_count} guesses.')

amount_of_quizzes = int(input('Enter the amount of numbers you want to guess: '))
for i in range(amount_of_quizzes):
    main()