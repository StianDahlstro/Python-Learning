# Oppgave 5
# Årstider

def main():
    måned = input('Angi måneden: ')
    dag = int(input('Angi dagen i måneden: '))
    print(årstid(måned.lower(), dag))


def årstid(m, d):
    if (m == 'mars' and d >= 20) or m == 'april' or m == 'mai' or (m == 'juni' and d < 21):
        return 'Vår'
    elif (m == 'juni' and d >= 21) or m == 'juli' or m == 'august' or (m == 'september' and d < 22):
        return 'Sommer'
    elif (m == 'september' and d >= 22) or m == 'oktober' or m == 'november' or (m == 'desember' and d < 21):
        return 'Høst'
    elif (m == 'desember' and d >= 21) or m == 'januar' or m == 'februar' or (m == 'mars' and d < 20):
        return 'Vinter'
    return 'Error, wrong month or date.'
    
main()