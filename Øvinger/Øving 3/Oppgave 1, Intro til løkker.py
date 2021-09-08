# Oppgave 1
# Intro til løkker

# A)
repetisjoner = int(input('Hvor mange adjektiv vil du gi? '))
for i in range(repetisjoner):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")


# B)
j = 0
while j != '':
    j = input("Beskriv deg selv med et adjektiv? ")
    if j != '':
        print("Hah, du", j + "!? Jeg er mye", j + "ere!")
print("Takk for nå!")


# C)
i = 42
while i > 0:
    print(f'Du har {i} bokstaver igjen og beskrive deg med.')
    adj = input("Beskriv deg selv med et adjektiv? ")
    if len(adj) > i:
        print("Hah, du", adj[0:i] + "!? Jeg er mye", adj[0:i] + "ere!")
    else:
        print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    i -= len(adj)
print("Takk for nå!")


# D)
print("Oddetallene fra 1 til 20:")
for number in range(1, 20, 2):
    print(number, end = " ")
print()
  
print("Tallene i 3-gangen mellom 12 og 25:")
for number in range(12, 25, 3):
    print(number, end = " ")
print()
  
print("Tallene i 5-gangen mellom 20 og 81:")
for number in range(20, 81, 5):
    print(number, end = " ")
print()
  
print("Tallsekvensen 48, 56, 64, 72, 80")
for number in range(48, 81, 8):
    print(number, end = " ")
print()
  
print("Telle baklengs fra 100 til 80, med intervall på -3, dvs. 100, 97, ...:")
for number in range(100, 80, -3):
    print(number, end = " ")
print()


# E)
for i in range(5):
    print(i + 1)


# F)
for i in range(15):
    print(15 - i)