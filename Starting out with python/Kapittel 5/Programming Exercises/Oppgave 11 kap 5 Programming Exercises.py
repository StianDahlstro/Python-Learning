# Programming Exercises kap 5
# Oppgave 11 - Math Quiz

# Write a program that gives multiple math quizzes.
# The program should display two random numbers 
# that are to be added, such as:
# 247 + 129
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations 
# should be displayed. If the answer is incorrect,
# a message showing the correct answer should be displayed.

import random

def main():
    quizzes = int(input('Enter the amount of quizzes you want to have: '))
    quiz_addition(quizzes)


def quiz_addition(times):
    total_right = 0
    for i in range(times):
        num_1 = random.randint(1, 1000)
        num_2 = random.randint(1, 1000)
        total = num_1 + num_2
        answer = int(input(f'Enter your answer to the operation {num_1} + {num_2}: '))
        if answer == total:
            print('Congratulations! That is the right answer.')
            total_right += 1
        else:
            print(f'Unfortunately, the correct answer is {total}, and you answered {answer}.')
    print(f'Your quiz is now done, and you got {total_right} out of {times} quizzes right.')

main()