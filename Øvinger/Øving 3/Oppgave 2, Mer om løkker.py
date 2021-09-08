# Oppgave 2
# Mer om Løkker

# A)
sum = 0
for i in range(7):
    sum += int(input('Skriv inn et heltall: '))
print(f'Summer av tallene ble: {sum}')


# B)
sum = 1
for i in range(20):
    sum *= (i + 1)
    if sum >= 1000:
        break
print(sum)


# C)
guess = ''
count = 0
while guess != 'Oslo':
    guess = input('Hva heter hovedstaden i Norge? ')
    count += 1
print(f'Korrekt! Du brukte {count} forsøk.')