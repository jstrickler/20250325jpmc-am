import inspect
import geometry
from carddeck import CardDeck


def _PI():
    return 3.14

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
def spam(p1, p2='a', *p3, p4, p5='b', **p6):  # define a function
    print(p1, p2, p3, p4, p5, p6)

# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()

# get frame (function call stack) info
print("Current frame:", inspect.getframeinfo(inspect.currentframe()))

print(f"{inspect.getfile(geometry) = }")
import re
print(f"{inspect.getfile(re) = }")

# type(class-name, base-classes, class-attributes)
Dog = type("Dog", (), {'bark': lambda self: print("woof, woof")})

print(f"{dir(Dog) = }")

bark_obj = getattr(Dog, 'bark')
print(f"{bark_obj = }")
print(f"{type(bark_obj) = }")
print(f"{inspect.ismethod(bark_obj) = }")

for attr in dir(Dog):
    print(attr, getattr(Dog, attr))

class Cat:
    def meow(self):
        print("meooowwwww")

d = Dog()
c = Cat()

for animal in d, c:
    if hasattr(animal, 'bark'):
        bark_method = getattr(animal, 'bark')
        if inspect.ismethod(bark_method):
            bark_method()