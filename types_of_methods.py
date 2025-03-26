class Spam:
    # instance method
    def foo(self):
        pass

    # class method
    @classmethod
    def bar(cls):
        pass

    @staticmethod
    def blah():
        pass

if __name__ == "__main__":
    s = Spam()
    s.foo()
    s.bar()
    Spam.bar()
    s.blah()
    Spam.blah()