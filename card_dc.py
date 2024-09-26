from dataclasses import dataclass

@dataclass  # auto-generate predefined methods
class Card:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    c1 = Card("Q", "spades")
    print(f"{c1 = }")  # repr()
    print(c1)   # str()
    print(c1.rank)
    print(f"{c1.suit = }")
        