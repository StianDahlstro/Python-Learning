# Programming Exercises kap 5
# Oppgave 18 - Prime Number List

# This exercise assumes you have already written is_prime function in
# programming exercises 17. Write another program that displays all of 
# the prime numbers from 1 to 100. the program should have a loop
# that calls the is_prime function.

def main():
    for i in range(1, 101):
        num = is_prime(i)
        if num == True:
            print(f'The number {i} is not a prime.')
        else:
            print(f'The number {i} is prime.')

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return True
    return False

main()