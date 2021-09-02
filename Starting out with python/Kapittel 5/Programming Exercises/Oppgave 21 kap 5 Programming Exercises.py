# Programming Exercises kap 5
# Oppgave 21 - Rock, Paper, Scissors Game

# Write a program that lets the user play the game of rock, paper, scissors agains the computer.
# The program should work as follows:

# 1. When the program begins, a random number in the range of 1 through 3 is generated.
# If the number is 1, then the computer has chosen rock. If the number is 2,
# then the computer has chosen paper. If the number is s3, then the computer
# has chosen scissors. (Don't display the computer's choice yet.)

# 2. The user enters their choice of "rock", "paper" or "scissors" at the keyboard.

# 3. The computer's choice is displayed.

# 4. A winner is selected according to the following rules:
#   If one chooses rock and another scissors, the rock wins
#   If one chooses scissors and another paper, the scissors wins
#   If one chooses paper and the other rock, paper wins
#   If both makes the same choice, play again.

import random

def main():
    init = 'error'
    while init == 'error':
        comp_choice = generate_random()
        play_choice = player_choice()
        init = check_result(comp_choice, play_choice)
    display_data(comp_choice, play_choice, init)
    
def generate_random():
    rand = random.randint(1,3)
    if rand == 1:
        return 'rock'
    elif rand == 2:
        return 'paper'
    else:
        return 'scissors'

def player_choice():
    return input('Enter the move you want to play in all lowercase: ')

def check_result(computer, player):
    if computer == 'scissors' and player == 'paper':
        return 'computer'
    elif computer == 'rock' and player == 'paper':
        return 'player'
    elif computer == 'rock' and player == 'scissors':
        return 'computer'
    elif computer == 'paper' and player == 'rock':
        return 'computer'
    elif computer == 'paper' and player == 'scissors':
        return 'player'
    elif computer == 'scissors' and player == 'rock':
        return 'player'
    else:
        return 'error'
    
def display_data(comp, player, init):
    if init == 'player':
        print(f"Congratulations, the player won using {player} against the computer's {comp}!")
    else:
        print(f"Unfortunately, the computer won using {comp} against the player's {player}!")

main()