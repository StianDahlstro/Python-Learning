# Oppgave 1 
# Ulike typer if-setninger

# A)
tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))
if tid >= 50:
    print("Kaken kan tas ut av ovnen.")
print("Tips til servering: vaniljeis.")

# B)
epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))
if barn > 0:
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
print("Takk for i dag!")

# C)
alder = int(input('Hvor gammel er du? '))
alder_for_å_stemme = 18
if alder >= alder_for_å_stemme:
    print('Du kan stemme :)')

# D)
alder_2 = int(input('Hvor gammel er du? '))
if alder_2 >= 18:
    print('Du kan stemme både ved lokalvalg og stortingsvalg')
elif alder_2 >= 16 and alder_2 < 18:
    print('Du kan stemme ved lokalvalg, men ikke stortingsvalg')
else:
    print('Du kan ikke stemme i noen politiske valg enda')

# E)
alder_3 = int(input('Hvor gammel er du? '))
if alder_3 < 3:
    print('Billetten er gratis.')
elif 3 <= alder_3 <= 11:
    print('Billetten koster 30kr.')
elif 12 <= alder_3 <= 25:
    print('Billetten koster 50kr.')
elif 26 <= alder <= 66:
    print('Billetten koster 80kr.')
else:
    print('Billetten koster 40kr.')

