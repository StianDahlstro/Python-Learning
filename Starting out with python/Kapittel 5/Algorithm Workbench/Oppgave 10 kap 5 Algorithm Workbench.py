# Algorithm Workbench kap 5
# Oppgave 10

# Write a function named 'get_first_name'
# that asks the user to enter his or her 
# first name, and returns it.

def get_first_name(name):
    return f'Your first name is {name}!'

first_name = input('Enter your first name here: ')
print(get_first_name(first_name))

# Might also be done through a void function like this:
def get_first_name_2():
    first_name_2 = input('What is your first name? ')
    print('The name entered is:', first_name_2)

get_first_name_2()