class Rabbit:
    LOCATION = "the Cave of Caerbannog"  # class data

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(self.LOCATION, self.weapon))  # look up class data via instance


r1 = Rabbit("a nice cup of tea")
r1.display()  # instance method uses class data

r1 = Rabbit("big pointy teeth")
r1.display()  # instance method uses class data
