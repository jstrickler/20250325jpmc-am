#

class OpenableThing():
    def __init__(self):
        print("Creating an OpenableThing")

    def __enter__(self):  # called at beginning of block
        print("Entering block")
        return self  # assigned to variable

    def __exit__(self, exc_type, value, traceback):  # called at end of block
        print("Leaving block")
        if exc_type is not None:
            print('*********************** EXCEPTION ************************')
            print("exception type:", exc_type)  # all None unless Exception occurs
            print("value:", value)
            print("traceback:", traceback)
            print('*************** * *******************************************')
        else:
            self.close()
        return True  # suppress exception raised in block

    def close(self):
        print("Closing")

    def hello(self):
        print("Hello from an OpenableThing")

with OpenableThing() as ot:  # create Blorch object; obj.__enter__() is called
    print("In the context...")
    ot.hello()  # after last line, obj.__exit__() is called

print('-' * 60)

with OpenableThing() as ot:  # create Blorch object; obj.__enter__() is called
    print("In the context....")
    raise Exception("Oh nooooooo")  # exception is raised (but suppressed)

    