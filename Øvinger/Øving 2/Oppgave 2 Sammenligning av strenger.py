# Oppgave 2
# Sammenligning av strenger

# A)
matvare_1 = input('Angi en matvare: ')
matvare_2 = input('Angi en matvare: ')
if matvare_1.lower() == matvare_2.lower():
    print('Det er samme matvare.')
else:
    print('Dette er to forskjellige matvarer.')

# B)
navn_1 = input('Angi et navn: ')
navn_2 = input('Angi et navn: ')
print('Under følger navnene i alfabetisk rekkefølge')
if navn_1.lower() > navn_2.lower():
    print(f'{navn_2}, {navn_1}')
else:
    print(f'{navn_1}, {navn_2}')

# C)
# Kodesnutt 1: k er større enn b
# Kodesnutt 2: Los Angeles, New York
# Kodesnutt 3: druer