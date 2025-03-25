class AnimalBase():  # create primary base class
    def __init__(self, name):
        self._name = name


    def get_id(self):
        print(self._name)


class CanBark():  # create additional (mixin) base class
    def bark(self):
        print("woof-woof")


class CanFly():  # create additional (mixin) base class
    def fly(self):
        print("I'm flying")


class Dog(CanBark, AnimalBase):  # inherit from primary base class plus mixin
    pass


class Sparrow(CanFly, AnimalBase):  # inherit from primary base class plus mixin
    pass


d = Dog('Dennis')
d.get_id()  # all animals have id()
d.bark()  # dogs can bark() (from mixin)
print()

s = Sparrow('Steve')
s.get_id()
s.fly()  # sparrows can fly() (from mixin)
print()

print("Sparrow mro:", Sparrow.mro())
