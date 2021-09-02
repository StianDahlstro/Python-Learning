# Algorithm Workbench kap 5
# Oppgave 6

# Write a funcion named welcome() that asks
# the user to enter his or her name and displays
# it followed by a welcome message.

init = 'y'

while init == 'y' or init =='Y':
    def welcome(name):
        print(f"Welcome to this event, {name}, we're happy to have you!")

    your_name = input('What is your name? ')

    if your_name != "":
        welcome(your_name)
    else:
        print('Error, no name entered.')
    init = input('Enter y if you would you like to add or greet another name: ')