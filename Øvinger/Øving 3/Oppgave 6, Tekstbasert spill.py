# Oppgave 6
# Tekstbasert spill

# A) & B) & C) & D)
def main():
    print('Du står utenfor en dør med en postkasse.')
    postkasse = handlingPostkasse()
    if postkasse != '':
        print(postkasse)
        dør = handlingDør()
        if dør != '':
            print(dør)

def handlingPostkasse():
    valg = input('')
    print()
    while valg != 'Åpne postkassen'.lower():
        print('Du står utenfor en dør med en postkasse.')
        valg = input('')
        print()
        if valg == '':
            return ''
    return 'Du åpner postkassen og finner en nøkkel.'

def handlingDør():
    valg = ''
    print()
    while valg != 'Åpne døren'.lower():
        print('Du står utenfor en dør med en postkasse.')
        valg = input('')
        print()
        if valg == '':
            return ''
    return 'Du åpner døren og går inn.'

main()