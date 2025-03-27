class Animal:
    def move(self):
        print("moving...")

class Cat(Animal):
    def make_sound(self):
        print("Meowwwww")

class Thing:
    def move(self):
        print("hopping on one foot")

# type(NAME, BASE_CLASSES, ATTRIBUTES)
Cat = type('Cat', (Animal,), {'make_sound': lambda self: print("Meowwwww")})
Dog = type('Dog', (Animal, Thing), {'make_sound': lambda self: print("Woof! Woof!"),
                              'move': lambda self: print("running")})

c = Cat()
c.move()
c.make_sound()

d = Dog()
d.move()
d.make_sound()
print(f"{Dog.mro() = }")
