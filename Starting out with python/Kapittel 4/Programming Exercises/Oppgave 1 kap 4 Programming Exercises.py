# Kap 4 Programming Exercises

# Oppgave 1 - Bug Collector
# A bug collector collects bugs every day for five days.
# Write a program that keeps a running total of the number
# of bugs collected during the five days. 
# The loop should ask for the number of bugs collected 
# each day, and when the loop is finished, the program
# should display the total number of bugs collected.

accumulator = 0

for i in range(7):
    bugs = int(input('Enter the number of bugs collected today: '))
    accumulator += bugs

print('The number of bugs collected during the week is', accumulator)