# Oppgave 6
# Primtall

# A) & B) & C)
def divisible(_a, _b):
    if _a % _b == 0:
        return True
    else:
        return False

def isPrime(_a):
    for i in range(2, _a - 1):
        if divisible(_a, i) != True:
            return True
    return False

def isPrime2(_a):
    for i in range(3, round((_a**0.5)+0.5), 2):
        if divisible(_a, i) != True and _a % 2 != 0:
            return True
    return False


a = int(input('Enter an integer to see if it is divisible by the next integer: '))
b = int(input('Enter an integer to see if it is divisible by the last integer: '))
print('Divisible?', divisible(a, b))
print()
c = int(input("Enter an integer to see if it's a prime: "))
print('Prime?', isPrime2(c))