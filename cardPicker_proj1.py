import random
values = ['two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine', 'ten', 'jack', 'queen',
          'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
def pick_cards(num_cards, cards):
    chosenCards = cards[:num_cards]
    del cards[:num_cards]
    return chosenCards

def cards_init():
    cards = []
    for val in values:
        for suit in suits:
            cards.append(val + ' of ' + suit)

    random.shuffle(cards)
    return cards

if __name__ == 'main':
    cards = cards_init()
    print(pickCards(1, cards))