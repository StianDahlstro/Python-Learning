# Oppgave 11
# Andregradsligning

import math

# A) & B)
a = float(input('Gi a en verdi: '))
b = float(input('Gi b en verdi: '))
c = float(input('Gi c en verdi: '))

d = (b**2) - (4*a*c)
if d >= 0:
    x_1 = (((-b) + math.sqrt(d)) / (2 * a))
    x_2 = (((-b) - math.sqrt(d)) / (2 * a))

if d < 0:
    print('Ligningen har to imaginære løsninger.')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir to imaginære løsninger')
elif d > 0:
    print('Ligningen har to reelle løsninger')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir løsningene:')
    print(x_1, '&', x_2)
else:
    print('Ligningen har en reel dobbeltrot.')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir løsningen:')
    print(x_1)

# C)
a = float(input('Gi a en verdi: '))
b = float(input('Gi b en verdi: '))
c = float(input('Gi c en verdi: '))

d = (b**2) - (4*a*c)

if b >= 0 and d >= 0:
    x_1 = ((-b) - math.sqrt(d)) / (2 * a)
    x_2 = (2 * c) / ((-b) - math.sqrt(d))
elif b < 0 and d >= 0:
    x_1 = (2 * c) / ((-b) + math.sqrt(d))
    x_2 = ((-b) + math.sqrt(d)) / (2 * a)

x_1_format = format(x_1, ',.3e')
x_2_format = format(x_2, ',.3e')


if d < 0:
    print('Ligningen har to imaginære løsninger.')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir to imaginære løsninger')
elif d > 0:
    print('Ligningen har to reelle løsninger')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir løsningene:')
    print(x_1_format, '&', x_2_format)
else:
    print('Ligningen har en reel dobbeltrot.')
    print(f'Andregradsligningen {a}x^2 + {b}x + {c} gir løsningen:')
    print(x_1_format)