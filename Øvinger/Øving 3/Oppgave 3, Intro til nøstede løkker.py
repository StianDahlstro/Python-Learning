# Oppgave 3
# Intro til nøstede løkker

# A)
stud = int(input('Hvor mange studenter? '))
emne = int(input('Hvor mange emner? '))
for student in range(stud):
    for emner in range(emne):
        print(f'Student {student + 1} elsker emne {emner + 1}', end = ' ; ')
    print()


# B)
for hour in range(24):
    for minute in range(60):
        print(f'{hour}:{minute}')


# C)
for x in range(10):
    for y in range(10):
        print((x + 1) * (y + 1), end='  ')
    print()