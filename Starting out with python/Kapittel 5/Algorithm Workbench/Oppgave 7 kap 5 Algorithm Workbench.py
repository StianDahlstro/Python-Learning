# Algorithm Workbench kap 5
# Oppgave 7

# The following statement calls a function named 'half',
# which returns a value that is half of the argument 
# passed to the function parameter.
# (Assume the number variable references a float value.)
# Write code for the funtion.
# result = half(number)

def half(number):
    return number / 2

num = float(input('Enter any number for the function to divide into 2 equal sizes: '))

if num == 0:
    print('Error, 0 cannot be divided into 2, and the returning value is 0.')
else:
    result = half(num)
    print(result)