# Algorithm Workbench Kapittel 5
# Oppgave 8

# What will the following code display?
# xdef display(x,y):
# return(x%2==0)
# print(display(4,7))
# print(display(7,4))
# This is an invalid function and will not compile,
# however if we modify it like I did below it will execute.
# the 'y' parameter is not used in the function body though
# so it is effectively useless and requires an argument to
# call the function, but doesn't utilize it in any way.
# This can be used as a double check for a function to run though:
# Let's say the arguments are variables, both arguments need a value
# to call the function. This way we can call the function only if 
# both arguments are given a value, even if only one is used in the function.

def display(x, y):
    return(x%2==0)
print(display(4,7))
print(display(7,4))