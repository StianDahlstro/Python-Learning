# Oppgave 10
# Sekantmetoden

# A)
from math import e

def f(_x):
    return (_x - 12) * (e ** (_x / 2)) - 8 * ((_x + 2) ** 2)

def g(_x):
    return (-_x) - (2 * (_x ** 2)) - (5 * (_x ** 3)) + (6 * (_x ** 4))

x = int(input('Enter a number: '))
print(f(x))
print(g(x))

# B)
def differentiate(_x_k, _x_k1, _func):
    if _func == 'f':
        _func = f
    elif _func == 'g':
        _func = g
    else:
        print('Invalid function unput. Enter "f" or "g".')
    return (_func(_x_k) - _func(_x_k1)) / (_x_k - _x_k1)

x_k = int(input('Enter a number for Xk: '))
x_k1 = int(input('Enter a number for Xk-1: '))
func = input('Enter "f" or "g" depending on which function you want to use: ')

print(differentiate(x_k, x_k1, func))

# C)
# def secantMethod(_x0, _x1, _func, _tol):