# Oppgave 5
# Gjett tallet

# A) & B) & C)
import random

nedre = int(input('Angi et heltall som nedre grense: '))
øvre = int(input('Angi et heltall som øvre grense: '))
count = 0
tilfeldigTall = random.randint(nedre, øvre)
guess = ''
while guess != tilfeldigTall:
    guess = int(input(f'Gjett et tall i intervallet {nedre}, {øvre}: '))
    count += 1
    if guess < tilfeldigTall:
        print('Det riktige tallet er høyere')
    elif guess > tilfeldigTall:
        print('Det riktige tallet er lavere')
print(f'Korrekt! Tallet var {tilfeldigTall}, og du brukte {count} forsøk')