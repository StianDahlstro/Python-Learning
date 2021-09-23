# Oppgave 3
# Lokale Variabler

# A)
# Kodesnutt 3 kan compiles og runnes, da den kun caller en funksjon, og den funksjonen er komplett

# B)
def heltallsdivisjon(_x, _y):
    return _x // _y

def kvadrat(_x):
    return _x**2

xDiv = float(input('Angi telleren til heltallsdivisjonen: '))
yDiv = float(input('Angi nevneren til heltallsdivisjonen: '))
print(f'Heltallsdivisjon av {xDiv} over {yDiv} gir {heltallsdivisjon(xDiv, yDiv)}.')

xKvadrat = float(input('Angi et tall for å finne kvadratet dets: '))
print(f'Kvadratet av {xKvadrat} er {kvadrat(xKvadrat)}')

# C)
# Variabler og parametere i funksjonene kan være like, da deres scope kun er lokalt i funksjonen.