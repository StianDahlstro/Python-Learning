# Oppgave 11
# Not Quite Blackjack
# A Blackjack Variation where the player doesn't get to choose the
# Value of the Ace, its value depends on the other cards drawn.
# If the Ace is drawn as one of the 2 first cards, its value will be 11
# Unless both cards are Ace. In that case, one Ace is 11 and the other is 1.
# If the Ace is drawn as a third card, it chooses the highest value
# That the player can have, without going over 21.
# E.g. If the player has 5 and 4 as the first two cards and gets an Ace, 
# The Ace will have the value 11 and grant the player a total of 20 points that round
# Hovewer, if the user had a 9 and a 10, the Ace will have the value 1.
import random

# card_values = {
#     'Ess': 1 or 10, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,'Six': 6,
#     'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10
# }

def dealerCards():
    cards = []
    cards.append(random.randint(1, 13))
    cards.append(random.randint(1, 13))
    return cards

def playerCardsStandard():
    cards = []
    cards.append(random.randint(1, 13))
    cards.append(random.randint(1, 13))
    return cards

def playerCardExtra():
    extraCard = random.randint(1, 13)
    if extraCard == 11 or extraCard == 12 or extraCard == 13:
        extra = 10
    return extra

def displayFunction(_dealer, _player):
    displayNum = random.randint(0,1)
    print(f'Dealers cards are {_dealer[displayNum]} and ?')
    print(f'Your score is: {sum(_player)}')
    while True:
        extraCard = input('Do you want another card? [j/n]').lower()
        if extraCard == 'j':
            extra = playerCardExtra()
            if sum(_player) <= 10 and extra == 1:
                extra = 11
                _player.append(extra)
            print(f'Your score is {sum(_player)}')
            if sum(_player) > 21:
                break
        else:
            break
    print(f'Dealers score is: {sum(_dealer)}')
    if sum(_dealer) > sum(_player) and sum(_dealer) <= 21:
        print('Unlucky, try again.')
    elif sum(_dealer) == sum(_player):
        print('Tie game!')
    elif sum(_player) > sum(_dealer) and sum(_player) <= 21:
        print('Massive dub, Bossman')
    else:
        print('Error, idk what went wrong')

def main():
    dealer = dealerCards()
    dealerHand = [10 if x == 11 or x == 12 or x == 13 else x for x in dealer]
    dealerHand = [11 if x == 1 else x for x in dealerHand]
    playerOriginalHand = playerCardsStandard()
    playerHand = [10 if x == 11 or x == 12 or x == 13 else x for x in playerOriginalHand]
    playerHand = [11 if x == 1 else x for x in playerHand]
    if sum(dealerHand) == 22:
        dealerHand = [11, 1]
    if sum(playerHand) == 22:
        playerHand = [11, 1]
    displayFunction(dealerHand, playerHand)

main()