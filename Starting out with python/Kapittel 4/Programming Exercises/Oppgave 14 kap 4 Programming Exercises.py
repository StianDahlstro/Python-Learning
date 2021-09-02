# Kap 4 Progamming Exercises

# Oppgave 14
# Write a program that uses nested loops to draw this pattern:
# ##
# # #
# #  #
# #   #
# #    #
# #     #

# Eksempel fra boka:
# num_steps = 6

# for r in range(num_steps):
#     for c in range(r):
#         print(' ', end='')
#     print('#')


# Oppgaven beskrevet over:
num_steps = 6

for r in range(num_steps):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')