import random
from card import Card

class OutOfCardsError(Exception):
    pass

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "clubs diamonds hearts spades".split()

    def __init__(self):
        self._cards = list()
        self._make_deck()

    def _make_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self._cards) == 0:
            raise OutOfCardsError("No more cards!")
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}-{len(self)}"
    
    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

    def to_json(str):
        return "{some JSON string...}"

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        try:
            card = d1.draw()
        except OutOfCardsError as err:
            print(err)
        else:
            print(card)
    print(f"{len(d1) = }")
    
    print(f"{d1 = }")
    print(d1)    

    METHOD_NAME = 'to_json'
    if hasattr(d1, METHOD_NAME):
        method = getattr(d1, METHOD_NAME)
        result = method()
        print(f"{result = }")
        