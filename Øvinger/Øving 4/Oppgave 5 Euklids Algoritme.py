# Oppgave 5
# Euklids Algoritme

# A) & B)
def gcd(_a, _b):
    while _b > 0:
        oldB = _b
        _b = _a % _b
        _a = oldB
    return _a

def reduceFraction(_a, _b):
    d = gcd(_a, _b)
    aReduced = _a / d
    bReduced = _b / d
    return int(aReduced), int(bReduced)

a = int(input('Enter an integer: '))
b = int(input('Enter an integer: '))
print(f'The greatest common divisor of the numbers entered are: {gcd(a, b)}')
aReduced, bReduced = reduceFraction(a, b)
print(f'The ratio of the numbers {a} and {b} can also be displayed as {aReduced} and {bReduced}.')