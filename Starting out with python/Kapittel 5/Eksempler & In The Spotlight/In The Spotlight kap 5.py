# In the spotlight side 194

def main():
    # Display the startup message
    startup_message()
    input('Press the enter key to get the next set of instructions: ')
    print()

    # Display the first step message
    first_message()
    input('Press the enter key to get the next set of instructions: ')
    print()
    
    # Display the second step message
    second_message()
    input('Press the enter key to get the next set of instructions: ')
    print()
    
    # Display the third step message
    third_message()
    input('Press the enter key to get the next set of instructions: ')
    print()

    # Display the fourth step message
    fourth_message()
    print()

def startup_message():
    print('Welcome to the disassembly guide!')
    print()

def first_message():
    print('Step 1:')
    print('Unplug the dryer and move it away from the wall.')
    print()

def second_message():
    print('Step 2:')
    print('Remove the six screws from the back of the dryer.')
    print()

def third_message():
    print('Step 3:')
    print("Remove the dryer's back panel.")
    print()

def fourth_message():
    print('Step 4:')
    print('Pull the top of the dryer straight up.')
    print()

init = input('Enter y to start the disassembly: ')

if init == 'y' or init == 'Y':
    main()