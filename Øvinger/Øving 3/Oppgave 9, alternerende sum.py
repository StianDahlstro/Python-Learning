# Oppgave 9
# Alternerende sum

# A)
antall_tall = int(input('Angi hvor mange tall tallrekken skal omfavne: '))
total = 0
for i in range(1, antall_tall + 1):
    if i % 2 != 0:
        total += i ** 2
    else:
        total -= i ** 2
    
print(f'Summen av tallrekken er: {total}.')

# B)
k = int(input('Angi et tall rekken ikke skal overstige: '))
n = 1
count = 0
total = 0
check = 0
while total <= k:
    if n % 2 == 0:
        check -= n**2
        if check <= k:
            total -= n**2
        else:
            break
    else:
        check += n**2
        if check <= k:
            total += n**2
        else:
            break
    count += 1
    n += 1

print(f'Summen av tallene før summen blir større enn k er {total}. Antall iterasjoner: {count}')