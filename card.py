class Card:   # inherits from 'object'
    def __init__(self, rank_, suit):
        self._rank = rank_  # private instance variable
        self._suit = suit

    # public instance variable
    @property
    def rank(self):  # getter property
        return self._rank
    # rank = property(rank)  SPOILER ALERT!!

    @property
    def suit(self):
        return self._suit

    def __str__(self):   #  str(card-instance)
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):  # repr(card-instance)
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("Q", "spades")
    print(f"{c1 = }")  # repr()
    print(c1)   # str()
    print(c1.rank)
    print(f"{Card.rank = }")
    print(f"{c1.suit = }")
        