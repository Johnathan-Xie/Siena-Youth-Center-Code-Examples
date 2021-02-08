import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def __str__(self):
        return self.value + ' of ' + self.suit
    
    def __repr__(self):
        return "Card(%s, %s)" % (self.value, self.suit)

class Deck:
    '''Deck of cards example class'''
    #static variables(shared across class instances)
    values = ['two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine', 'ten', 'jack', 'queen',
          'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    
    #initalize non-static variables(unique for each class instance)
    def __init__(self):
        self.cards = []
        for val in Deck.values:
            for suit in Deck.suits:
                self.cards.append(Card(val, suit))
        random.shuffle(self.cards)
    
    def pick(self, num_cards):
        chosen_cards = [str(card) for card in self.cards[:num_cards]]
        del self.cards[:num_cards]
        return chosen_cards
    
    #have students type on their own
    def peek(self, num_cards):
        chosen_cards = [str(card) for card in self.cards[:num_cards]]
        return chosen_cards
    
    def __getitem__(self, idx):
        return self.cards[idx]
    
    def pop(self):
        return self.cards.pop()
    
    def append(self, card):
        self.cards.append(card)

if __name__ == '__main__':
    deck = Deck()
    deck.peek(10)