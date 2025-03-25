class Rabbit:
    LOCATION = "the Cave of Caerbannog"  # class data (not duplicated in instances)

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(self.LOCATION, self.weapon))  # instance method

    @classmethod  # the @classmethod decorator makes a function receive the class object, not the instance object
    def get_location(cls):  # get_location() is a _class_ method
        return cls.LOCATION  # class methods can access class data via cls


r = Rabbit("a nice cup of tea")
print(Rabbit.get_location())  # call class method from class
print(r.get_location())  # call class method from instance
