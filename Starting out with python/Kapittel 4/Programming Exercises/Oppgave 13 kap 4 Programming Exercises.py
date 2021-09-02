# Kap 4 Programming Exercises

# Oppgave 13 
# Write a program that uses nested loops to draw this pattern:

# *******
# ******
# *****
# ****
# ***
# **
# *

# Trekantmønster fra boka (opp-ned fra oppgaven):
# base_size = 7

# for r in range(base_size):
#     for c in range(r + 1):
#         print('*', end='')
#     print()

# Oppgaven beskrevet over:
base_size = 7

for r in range(base_size):
    for c in range(base_size - r):
        print('*', end='')
    print()