# Oppgave 10
# Hangman

# A)
hemmelig_ord = input('Avgi ditt hemmelige ord: ').lower()
antall_liv = int(input('Hvor mange liv skal gjetterne få? '))
oppdatert_ord = hemmelig_ord

while True:
    gjett = input('Gjett en bokstav! ').lower()
    if gjett not in oppdatert_ord:
        antall_liv -= 1
        print(f'Desverre er ikke {gjett} i ordet. Du har nå {antall_liv} liv igjen.')
    if gjett in oppdatert_ord:
        for i in gjett:
            oppdatert_ord = oppdatert_ord.replace(i, '')
        print(f'Gratulerer! Bokstaven {gjett} er i ordet.')
    if antall_liv == 0:
        print('Desverre, du tapte spillet')
        break
    elif oppdatert_ord == '':
        print(f'Gratulerer, du gjettet hele ordet: {hemmelig_ord}!')
        break