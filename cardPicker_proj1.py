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

if __name__ == '__main__':
    cards = cards_init()
    for card in pick_cards(10, cards):
        print(card)