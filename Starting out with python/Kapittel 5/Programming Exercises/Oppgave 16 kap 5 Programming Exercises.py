# Programming Exercises kap 5
# Oppgave 16 - Odd/Even Counter

# In this chapter, you saw an example of how to write an algorithm that
# determines wether a number is even or odd. Write a program that
# generates 100 random numbers an keeps a count of how many of those
# random numbers are even and how many of them are odd.

import random

def main():
    odd = 0
    even = 0
    for i in range(100):
        number = random.randint(1,100)
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'100 random numbers resulted in {odd} odd numbers and {even} even numbers.')

main()