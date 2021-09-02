# Kap 5 Algorithm Workbench
# Oppgave 3

# Look at the following function header:
# def my_function(a, b, c):
# Now look at the following call to my_function:
# my_function(3, 2, 1)
# When this call executes, what value will be assigned to a?
# What value will be assigned to b?
# What value will be assigned to c?

# The arguments in the function call assign 
# the values to the parameters in the same order
# they are used in the function. In this case,
# a will have the value 3
# b will have the value 2
# c will have the value 1

def my_function(a, b, c):
    print(a)
    print(b)
    print(c)

my_function(3, 2, 1)