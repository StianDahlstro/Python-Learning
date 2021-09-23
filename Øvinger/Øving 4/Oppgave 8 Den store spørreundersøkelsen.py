# Oppgave 8
# Den Store Spørreundersøkelsen

def main():
    global femaleCount
    global maleCount
    global totalAge
    global persSomTarFag
    global antallFag
    global antallITGK
    global antallTimerLekser
    femaleCount = 0
    maleCount = 0
    totalAge = 0
    persSomTarFag = 0
    antallFag = 0
    antallITGK = 0
    antallTimerLekser = 0   
    while True:
        print('Velkommen til spørreundersøkelsen. Svar "hade" på et spørsmål for å avslutte.')
        print()
        kjønn = input('Hvilket kjønn er du? [f/m] ').lower()
        if kjønn == 'hade':
            break
        alder = input('Hvor gammel er du? ')
        if alder == 'hade':
            break
        elif 15 > int(alder) or int(alder) > 25:
            print('Du kan desverre ikke ta undersøkelsen.')
            continue
        fag = input('Tar du ett eller flere fag? [j/n] ').lower()
        if fag == 'hade':
            break
        elif fag == 'j':
            fagAntall = int(input('Hvor mange fag tar du? '))
        elif fag == 'n':
            continue
        if 16 <= int(alder) <= 22:
            itgk = input('Tar du ITGK? [j/n] ')
        else:
            itgk = input('Tar du virkelig ITGK? [j/n] ').lower()
        timer = input('Hvor mange timer bruker du daglig på lekser? ')
        if timer == 'hade':
            break
        kjønnCount(kjønn)
        alderCount(int(alder))
        fagCount(fag, fagAntall, itgk)
        leksetimer(float(timer))
        print()
    statistikk(
        femaleCount, maleCount, totalAge, persSomTarFag, antallFag, antallITGK, antallTimerLekser
    )


def kjønnCount(_kjønn):
    global femaleCount
    global maleCount
    if _kjønn == 'f':
        femaleCount += 1
    elif _kjønn == 'm':
        maleCount += 1

def alderCount(_alder):
    global totalAge
    totalAge += _alder


def fagCount(_pers, _fag, _itgk):
    global persSomTarFag
    global antallFag
    global antallITGK
    if _pers == 'j':
        persSomTarFag += 1
    antallFag += _fag
    if _itgk == 'j':
        antallITGK += 1
    

def leksetimer(_timer):
    global antallTimerLekser
    antallTimerLekser += _timer

def statistikk(_female, _male, _age, _persFag, _totaltFag, _totaltITGK, _timer):
    print('Antall Kvinner:', _female)
    print('Antall Menn:', _male)
    print('Gjennomsnittlig Alder:', _age / (_female + _male))
    print('Antall Personer som Tar Fag:', _persFag)
    print('Antall Fag som Tas Til Sammen:', _totaltFag)
    print('Antall Personer som Tar ITGK:', _totaltITGK)
    print('Antall timer brukt på lekser i gjennomsnitt per dag:', _timer/ (_male + _female))

main()