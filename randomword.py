import random


class RandomWord():
    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._words = [word.rstrip('\n\r') for word in words_in.readlines()]

    def __call__(self):
        return random.choice(self._words)
    
if __name__ == "__main__":
    rw = RandomWord()
    for _ in range(10):
        print(rw())  # NOT rw.get_word()
