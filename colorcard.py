from dataclasses import dataclass
from card import Card

@dataclass
class ColorCard(Card):
    def __init__(self, rank, suit, color):
        super().__init__(rank, suit)
        self._color = color

    @property
    def color(self):
        return self._color

if __name__ == "__main__":
    cc = ColorCard("2", "diamonds", "blue")
    print(f"{cc = }")
    print(cc.rank, cc.suit, cc.color)
    