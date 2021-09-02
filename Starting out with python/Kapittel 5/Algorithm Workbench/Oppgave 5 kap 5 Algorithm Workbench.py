# Algorithm Workbench kap 5
# Oppgave 5

# Look at the following function definition:
# def my_function(a, b, c):
#   d = (a + c) / b
#   print(d)
# 
# a) Write a statement that calls this function and uses
# keyword arguments to pass 2 into a, 4 into b, and 6 into c
#   my_function(a=2, b=4, c=6) 
# b) What value will be displayed when the function calls executes?
#   print((a + c) / b) = print((2 + 6) / 4) = 2.0

def my_function(a, b, c):
    d = (a + c) / b
    print(d)

my_function(c=6, b=4, a=2) # "Feil" rekkefølge for å tydeliggjøre at 
# plassering av argumenter ikke spiller noen rolle når alle argumentene 
# bruker keywords når de gis til paramaterene i funksjonen.
# Plassering spiller dog en rolle når kun noen av argumentene angis til 
# parametrene i en funksjon ved bruk av keywords. 