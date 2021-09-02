# Oppgave 8
# Billettpriser og Rabatter

# A) & B) & C)
dager = int(input('Hvor mange dager er det til avreise? '))
under_16 = input('Er du under 16 år? (j/n) ')
annen_rabatt = input('Er du over 60, student eller militær i uniform? (j/n) ')
if dager >= 14:
    bestille_mini = input('Du kan bestille miniprisbillett for 199 kr, men billetten kan da ikke refunderes. Ønskes dette? (j/n)')
    if bestille_mini.lower() == 'j':
        print('Takk for handelen, god tur')
    elif under_16.lower() == 'j':
        print('Ettersom du er under 16 kan du få 50 prosent rabatt og prisen blir kr 220.')
    elif annen_rabatt.lower() == 'j':
        print('Ettersom du kvalifiserer for 25 prosent rabatt vil prisen bli kr 330.')
    else:
        print('Fullpris  for en billett er kr 440.')
elif under_16.lower() == 'j':
    print('Ettersom du er under 16 kan du få 50 prosent rabatt og prisen blir kr 220.')
elif annen_rabatt.lower() == 'j':
    print('Ettersom du kvalifiserer for 25 prosent rabatt vil prisen bli kr 330.')
else:
    print('Fullpris  for en billett er kr 440.')