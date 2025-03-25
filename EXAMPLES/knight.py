
class Knight():
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color

    @property  # getter property decorator
    def name(self):  # property implemented by name() method
        return self._name

    @property
    def color(self):
        return self._color

    @color.setter  # setter property decorator
    def color(self, color):
        self._color = color

    @property
    def title(self):
        return self._title


if __name__ == '__main__':
    k = Knight("Lancelot", "Sir", 'blue')

    # Bridgekeeper's question
    print(f'Sir {k.name}, what is your...favorite color?')  # use property

    # Knight's answer
    print(f"red, no -- {k.color}!")

    k.color = 'red'  # set property

    print(f"color is now: {k.color}")
