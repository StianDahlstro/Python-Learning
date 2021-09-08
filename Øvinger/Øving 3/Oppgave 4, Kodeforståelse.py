# Oppgave 4
# Kodeforståelse

# A)
a=345
b=''
while a or b=='':
    b=str(a%2)+b
    a=a//2
print(b)


# B)
for x in range(0, 10, 2):
    print(x, end='')
    if x%4==0:
        print( ": Dette tallet går opp i 4-gangern")
    else:
        print()


# C)
i = 1
while i<10:
    i = i*2
print(i)


# D)
i = 1
j = 3
while j>0:
    i = i*2
    j = j - 1
print(i)


# E)
i = 5
for x in range(i):
    for y in range(x+1):
        print("*", end="")
    print()