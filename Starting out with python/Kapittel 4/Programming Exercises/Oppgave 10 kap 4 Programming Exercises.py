# Kap 4 Programming Exercises

# Oppgave 10 - Tuition Incerase
# At one college, the tuition for a full-time
# student is $8,000 per semester. It has been 
# announced that the tuition will increase by
# 3 percent each year for the next 5 years.
# Write a program wth a loop that displays 
# the projected semester tuition amount for
# the next 5 years

cost = 8000
annual_increase = 1.03

print('Year: \t \t \t Semester tuition:')

for year in range(1, 6):
    if year > 1:
        cost *= annual_increase
    print(year, '\t \t \t \t', '$', format(cost, ',.2f'), sep='')