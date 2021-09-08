# Oppgave 7
# Geometrisk rekke

# A)
print('En geometrisk rekke er sum av alle r, opphøyd i tall fra 0 til n')
print('r er et tall mellom -1 og 1, n kan være så stort som ønsket.')
r = float(input('Enter a number between -1 and 1 for r: '))
n = int(input('Enter any number for n: '))
sum = 0
if n > 0:
    for i in range(n + 1):
        sum += r**i
elif n == 0:
    sum = 1
else:
    for i in range(n - 1):
        sum += r**i

print(sum)