class Special():

    def __init__(self, value):
        self._value = str(value)  # all Special instances are strings

    def __add__(self, other):  # define what happens when a Special instance is added to another Special object
        return self._value + other._value

    def __mul__(self, num):  # define what happens when a Special instance is multiplied by a value
        return ''.join((self._value for i in range(num)))

    def __str__(self):  # define what happens when str() called on a Special instance
        return self._value.upper()

    def __eq__(self, other):  # define equality between two Special valuess
        return self._value == other._value


if __name__ == '__main__':
    s = Special('spam')
    t = Special('eggs')
    u = Special\
        ('spam')
    v = Special(5)  # parameter to Special() is converted to a string
    w = Special(22)

    print("s + s", s + s)  # add two Special instances
    print("s + t", s + t)
    print("t + t", t + t)
    print("s * 10", s * 10)  # multiply a Special instance by an integer
    print("t * 3", t * 3)
    print(f"str(s)={s!s}  str(t)={t!s}")
    print(f"id(s)={id(s)} id(t)={id(t)} id(u)={id(u)}")
    print("s == s", s == s)
    print("s == t", s == t)
    print("s == u", s == u)
    print("v + v", v + v)
    print("v + w", v + w)
    print("w + w", w + w)
    print("v * 10", v * 10)
    print("w * 3", w * 3)
