# Kap 3 Programming Exercises
# Oppgave 3 - Age Classifier

# Write a program that asks the user to
# enter a person's age. The program should 
# display a message indicating wether the
# person is an infant, a child, a teenager,
# or an adult. Following are the guidelines:

# If the person is 1 year old or less, they're an infant.
    # age >=0 and age <= 1
# If the person is older than 1 year, but younger than 13, they're a child.
    # age > 1 and age < 13
# If the person is 13 or older, but younger than 20, they're a teenager
    # age >= 13 and age < 20
# If the person is at least 20 years old, they're an audult.
    # age >= 20
# add a message to display is the number given is invalid (negative)
    # age < 0

enter_age = int(input("Enter a person's age formatted as an integer. "))

if enter_age >= 0 and enter_age <= 1:
    print('Infant')
elif enter_age > 1 and enter_age < 13:
    print('Child')
elif enter_age >= 13 and enter_age < 20:
    print('Teenager')
elif enter_age >= 20:
    print('Adult')
else:
    print('Invalid age')