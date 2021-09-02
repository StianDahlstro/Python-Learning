# Programming Exercises kap 5
# Oppgave 17 - Prime Numbers

# A prime number is a number that is only evenly divisible by itself and 1. 
# For example, the number 5 is prime because it can only be evenly divided
# by 1 and 5. The number 6, however, is not prime because it can be divided 
# evenly by 1, 2, 3, and 6.
# Write a Boolean function named is_prime which takes an integer as an 
# argument and returns true if the argument is a prime number, or false otherwise.
# Use the function in a program that prompts the user to enter a number and then 
# displays a message indicating wether the number is prime

def main():
    prime_test = int(input('Enter an integer to check if it is a prime: '))
    is_prime(prime_test)

def is_prime(prime_test):
    div_num = prime_test
    bool_list = []
    for i in range(2, prime_test):
        div_num -= 1
        prime = prime_test % div_num == 0
        bool_list.append(prime)
    if True in bool_list:
        print(f'The number {prime_test} is not prime.')
    else:
        print(f'The number {prime_test} is prime.')

main()