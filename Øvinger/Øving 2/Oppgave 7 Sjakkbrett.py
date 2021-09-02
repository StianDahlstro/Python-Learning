# Oppgave 7
# Sjakkbrett

# A) & B)
def main():
    posisjon = input('Angi posisjonen til ruten du vil sjekke fargen til: ')
    kolonne = posisjon[0].lower()
    rad = int(posisjon[1])
    if 'a' <= kolonne < 'i' and 1 <= rad < 9 and len(posisjon) == 2:
        print(f'Posisjonen {posisjon} har farge:')
        print(fargeSjekk(kolonne, rad))
    else:
        print('Error, ingen gyldig posisjon på sjakkbrettet')

def fargeSjekk(bokstav, tall):
    partallsjekk = tall % 2
    if partallsjekk == 0 and bokstav == 'a':
        return 'Hvit'
    elif partallsjekk != 0 and bokstav == 'a':
        return 'Svart'
    elif partallsjekk == 0 and bokstav == 'b':
        return 'Svart'
    elif partallsjekk != 0 and bokstav == 'b':
        return 'Hvit'
    elif partallsjekk == 0 and bokstav == 'c':
        return 'Hvit'
    elif partallsjekk != 0 and bokstav == 'c':
        return 'Svart'
    elif partallsjekk == 0 and bokstav == 'd':
        return 'Svart'
    elif partallsjekk != 0 and bokstav == 'd':
        return 'Hvit'
    elif partallsjekk == 0 and bokstav == 'e':
        return 'Hvit'
    elif partallsjekk != 0 and bokstav == 'e':
        return 'Svart'
    elif partallsjekk == 0 and bokstav == 'f':
        return 'Svart'
    elif partallsjekk != 0 and bokstav == 'f':
        return 'Hvit'
    elif partallsjekk == 0 and bokstav == 'g':
        return 'Hvit'
    elif partallsjekk != 0 and bokstav == 'g':
        return 'Svart'
    elif partallsjekk == 0 and bokstav == 'h':
        return 'Svart'
    else:
        return 'Hvit'


main()