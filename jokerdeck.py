from card import Card
from carddeck import CardDeck
import inspect
from pprint import pprint

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()    
        joker1 = Card("Joker", "Joker1")
        joker2 = Card("Joker", "Joker2")
        self._cards.extend([joker1, joker2])

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for _ in range(5):
        print(j.draw())
    print(f"{j.cards = }")
    print(j)
    print(f"{j = }")

    pprint(inspect.getclasstree([Card, JokerDeck, CardDeck]))    
