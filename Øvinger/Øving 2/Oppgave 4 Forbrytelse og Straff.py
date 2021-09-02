# Oppgave 4
# Forbrytelse og Straff

# A) & B)
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ")
f = input("Var personen fører av vognen? (j/n) ")
leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
n = input("Var det nødrett? (j/n) ")
 
if (prom >= 0.2 and motor == "j" and f == "j") or (prom >= 0.2 and leds == "j" and n == "n"):
   print("Det var straffbar promillekjøring.")
else:
    print("Ikke straffbart, ingen bot.")

# C)
prom = float(input("Hvor stor var promillen? "))
if prom < 0.2:
    print("Ikke straffbart, ingen bot.")
elif  0.4 >= prom >= 0.2:
    print("Forelegg: 6000,-")
elif 0.5 >= prom > 0.4:
    print("Forelegg: 10000,-")
elif prom > 0.5:
    print("Bot: en halv brutto månedslønn, samt fengsel.")

# D)
prom = float(input("Hvor stor var promillen? "))
nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
if tidl == "j":
    år = int(input("Antall år siden siste domfellelse: "))
else:
    år = 999
  
if (tidl == "j" and prom >= 0.2) or (nekt == "j" and år < 5):
    print("Førerkort inndras for alltid.")
elif prom >= 1.2 or nekt == "j":
    print("Førerkort inndras minst 2 år.")
elif 1.2 > prom >= 0.8:
    print("Førerkort inndras 20-22 mnd.")
elif 0.8 > prom >= 0.5:
    print("Førerkort inndras vanligvis 18 mnd.")
elif 0.5 > prom >= 0.2:
    print("Førerkort inndras inntil 1 år.")
else:
    print("Ingen inndragning av førerkort.")

# E)
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ")
f = input("Var personen fører av vognen? (j/n) ")
leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
n = input("Var det nødrett? (j/n) ")
nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
if tidl == "j":
    år = int(input("Antall år siden siste domfellelse: "))
else: 
    år = 999

if (prom >= 0.2 and motor == "j" and f == "j") or (prom >= 0.2 and leds == "j" and n == "n"):
   print("Det var straffbar promillekjøring.")
else:
    print("Ikke straffbart, ingen bot.")

if (tidl == "j" and prom >= 0.2) or (nekt == "j" and år < 5):
    print("Førerkort inndras for alltid.")
elif prom >= 1.2 or nekt == "j":
    print("Førerkort inndras minst 2 år.")
elif 1.2 > prom >= 0.8:
    print("Førerkort inndras 20-22 mnd.")
elif 0.8 > prom >= 0.5:
    print("Førerkort inndras vanligvis 18 mnd.")
elif 0.5 > prom >= 0.2:
    print("Førerkort inndras inntil 1 år.")
else:
    print("Ingen inndragning av førerkort.")