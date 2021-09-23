# Oppgave 2
# Varierte funksjoner

# A)
def absol(_n):
    if _n >= 0:
        absoluttverdi = _n
    else:
        absoluttverdi = -_n
    return absoluttverdi

def main():
    n = int(input('Gi et tall for å finne dets absoluttverdi: '))
    print(f'Absoluttverdien til tallet {n} er {absol(n)}.')

main()

# B)
def knop2km_t(_knop):
    ms = _knop * 0.514444444
    km_t = ms * 3.6
    return km_t

def main():
    knop = float(input('Oppgi fart i knop: '))
    print(f'{knop} knop er {knop2km_t(knop)} km/t.')

main()

# C)
def imp2cm(_feet, _inches):
    inchesTotal = _feet * 12 + _inches
    inchesToCm = inchesTotal * 2.54
    return inchesToCm

def main():
    feet = int(input('Enter the amount of feet: '))
    inches = int(input('Enter the amount of inches: '))
    print(f'{feet} feet {inches} inches in imperial measurments is the same as {imp2cm(feet, inches)} cm in metric measurments')

main()

# D)
def cmykToRgb(_c, _m, _y, _k):
    r = 255 * (1 - _c) * (1 - _k)
    g = 255 * (1 - _m) * (1 - _k)
    b = 255 * (1 - _y) * (1 - _k)
    return int(r), int(g), int(b)

def main():
    c = float(input('Enter the value of Cyan: '))
    m = float(input('Enter the value of Magenta: '))
    y = float(input('Enter the value of Yellow: '))
    k = float(input('Enter the value of Black: '))
    r, g, b = cmykToRgb(c, m, y, k)
    print(f'{c, m, y, k} expressed as CMYK is the equivalent of {r, g, b} expressed as RGB respectively.')

main()