# Programming Exercises kap 5
# Oppgave 15 - Test Average and Grade

# Write a program that asks the user to enter five test scores.
# The program should display a letter grade for each score
# and the average test score.
# Write the following functions in the program:

# 1. calc_average - This function should accept five test scores 
# as arguments and return the average of the scores.

# 2. determine_grade - This function should accept a test score 
# as an argument and return a letter grade for the score
# based on the following grade scale:
# 90-100   = A
# 80-89    = B
# 70-79    = C
# 60-69    = D
# Below 60 = F

def main():
    scores = []
    for i in range(5):
        score = int(input('Enter the test score: '))
        scores.append(score)
        grade = determine_grade(score)
        print(f'The test score {score}, results in the grade {grade}.')
    calc_average(scores)
    
def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def calc_average(scores):
    average_score = sum(scores) / 5
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80 and average_score < 90:
        grade = 'B'
    elif average_score >= 70 and average_score < 80:
        grade = 'C'
    elif average_score >= 60 and average_score < 70:
        grade = 'D'
    else:
        grade = 'F'
    print(f'The average score from the five tests is {average_score}, ' \
        f'which makes the average grade {grade}.')


main()