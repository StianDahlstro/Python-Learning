# Oppgave 9
# Skatteetaten

# A) & B) & C)
boligtype = input('Skriv inn boligtype, s for sekundær, f for fritid og p for primær: ').lower()
if boligtype == 'p':
    prosent = int(input('Oppgi hvor mange prosent av boligen som leies ut: '))
    leieinntekter = int(input('Oppgi leieinntektene for året: '))
    if prosent <= 50 or (prosent > 50 and leieinntekter <= 20000):
        print('Inntekten er ikke skattepliktig')
    else:
        print(f'Hele inntekten er skattepliktig, kr{leieinntekter}.')
elif boligtype == 's':
    inntekt_sek = int(input('Oppgi hvor mye sekundærboligen(e) tjener ila et år: '))
    print(f'Hele inntekten er skattepliktig, kr{inntekt_sek}.')
else:
    eget_bruk = input('Brukes boligen i stor grad privat (uten leie) (j/n)? ').lower()
    antall = int(input('Hvor mange fritidsboliger leier du ut? '))
    inntekt_fri = int(input('Hvor stor inntekt har hver fritidsbolig? '))
    if eget_bruk == 'j' and inntekt_fri <= 10000:
        print('Ingen skattepliktig inntekt')
    elif eget_bruk == 'j' and inntekt_fri > 10000:
        skattepliktig = (inntekt_fri - 10000) * 0.85 * antall
        print(f'Total skattepliktig inntekt er på kr{skattepliktig}.')
    elif eget_bruk == 'n':
        print(f'Totalt skattepliktig inntekt er på kr{inntekt_fri*antall}')