# Oppgave 6
# Tekstbasert Spill

# A) & B) & C)
def main():
    print('Du står utenfor en dør.')
    handling = input('')
    print(checkAction(handling.lower()))

def checkAction(action):
    if action == 'gå inn' or action == 'gå inn døra':
        return 'Døren er låst'
    elif action == 'bank på' or action == 'banker på':
        return 'Ingen svarer'
    elif action == 'lås opp' or action == 'låser opp':
        return 'Du låser opp døren'
    else:
        'Dette er ikke en støttet kommando'

main()