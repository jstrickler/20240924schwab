import inspect
import alpha.mathlib.geometry as geometry
from carddeck import CardDeck

deck = CardDeck("Leonard")

things = (
    geometry,
    geometry.circle_area,
    CardDeck,
    CardDeck.get_ranks,
    deck,
    deck.shuffle,
)

print("Name               Module?  Function?  Class?  Method?")
for thing in things:
    try:
        thing_name = thing.__name__
    except AttributeError:
        thing_name = type(thing).__name__ + " instance"
    print("{:18s} {!s:6s}   {!s:6s}     {!s:6s}  {!s:6s}".format(
        thing_name,
        inspect.ismodule(thing),  # test for module
        inspect.isfunction(thing),  # test for function
        inspect.isclass(thing),  # test for class
        inspect.ismethod(thing),
    ))


print()
def spam(p0: int, /, p1: float, p2: str='a', *p3, p4: list, p5: str='b', **p6) -> int:  # define a function
    print(p0, p1, p2, p3, p4, p5, p6)
    return 0

# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()

# get frame (function call stack) info
print("Current frame:", inspect.getframeinfo(inspect.currentframe()))
