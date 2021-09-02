# Kap 4 Programming Exercises

# Oppgave 9 - Ocean Levels
# Assuming the ocean's level is currently rising
# at about 1.6 millimeters per year, 
# create an application that displays the number of
# millimeters that the ocean will have risen
# each year for the next 25 years.

rise_year = 1.3
total_rise = 0

print('Years from now: \t\t Total mm ocean level rise:')
print('-------------------------------------------------------')

for year in range(1, 26):
    total_rise += rise_year
    print(year, ' \t \t \t \t ', format(total_rise, ',.2f'), 'mm', sep='')
