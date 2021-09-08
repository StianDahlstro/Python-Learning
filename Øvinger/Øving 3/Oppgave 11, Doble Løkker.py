# Oppgave 11
# Doble Løkker

# A)
for i in range(6):
    for n in range(i):
        print(n + 1, end=' ')
    print()

# B)
for i in range(5):
    print('X ', end='')
    for n in range(i):
        print(' ', end='')
    print('X')

# C)
n = int(input('Skriv inn et positivt heltall: '))
i = 2
factors = []
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factors.append(i)
if n > 1:
    factors.append(n)
print(factors)

# D) & E)
import random

def generateRandomNumber(slutt):
    return random.randint(0, slutt)

def main():
    failed = False
    counter_main = 1
    counter_riktig = 5
    fortsette = int(input('Skriv 1 for å starte, 0 for å avbryte: '))
    while fortsette == 1:
        faktor_1 = generateRandomNumber(counter_main * 5)
        faktor_2 = generateRandomNumber(counter_main * 5)
        counter_1 = 0
        print(f'Hva blir {faktor_1} * {faktor_2}?')
        while counter_1 < 3:
            svar = int(input('Svar her: '))
            if svar == faktor_1 * faktor_2:
                counter_1 = 3
                print('Gratulerer, det er riktig svar.')
            else: 
                counter_1 += 1
                if counter_1 == 3:
                    print('Desverre, test avbrutt.')
                    failed = True
                    break
                print(f'{svar} var desverre feil svar, men du har {3 - counter_1} forsøk igjen. Hva er {faktor_1 * faktor_2}?')
        if failed == True:
            break
        counter_riktig += 1
        print(f'Du har nå {counter_riktig - 5} riktige svar.')
        if counter_riktig % 5 == 0:
            counter_main = counter_riktig / 5
        fortsette = int(input(f'Ønsker du å fortsette? Neste spørsmål vil inneholde gangestykker med tall mellom 0 og {counter_main * 5}. 1 for å fortsette, 0 for å avslutte: '))

main()