# Oppgave 4
# Globale Variabler

# A) & B)
def setGravity(_gravity):
    global GRAVITY
    GRAVITY = _gravity

def getFallTime(_meters, _gravity):
    setGravity(_gravity)
    return round(((2 * _meters) / GRAVITY) ** 0.5, 3)

metersToFall = float(input('Enter the total meters the object should fall to determine the time: '))
gravityCoefficient = input('Enter the desired coefficient for the gravity: ')
if gravityCoefficient == '':
    gravityCoefficient = 9.81
else:
    gravityCoefficient = float(gravityCoefficient)
print(f'It takes {getFallTime(metersToFall, gravityCoefficient)} seconds for the object to fall {metersToFall} meters with a gravity coefficient of {gravityCoefficient} m/s^2.')