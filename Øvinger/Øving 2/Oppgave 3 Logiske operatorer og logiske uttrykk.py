# Oppgave 3
# Logiske operatorer og logiske uttrykk

# A)
# Uttrykk 1 = True
# Uttrykk 2 = False
# Uttrykk 3 = True
# Uttrykk 4 = False
# Uttrykk 5 = True

# B)
print('Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:')
a = int(input('Verdi for a: '))
b = int(input('Verdi for b: '))
if (40 <= a <= 50 or 70 <= a <= 90) and (40 <= b <= 50 or 70 <= b <= 90):
    print("Tallene er begge i gyldige intervall ^u^")
else:
    print("Minst ett av tallene er utenfor et gyldig intervall :(")

# C)
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
  
if p < 0 or p > 10:
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10-p
    print("Da blir det",p,"på deg og",r,"på meg :D")

# D)
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
s = input("Er du glad i pannekaker? (J/N) ")
 
if s.lower() == 'j':
    elsker_pannekaker = True
else:
    elsker_pannekaker = False
  
if (p < 0 or p > 10) or elsker_pannekaker == False:             #Kode mangler her
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10-p
    print("Da blir det",p,"på deg og",r,"på meg :D")