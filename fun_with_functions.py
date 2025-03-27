from datetime import datetime
import logging
from functools import wraps

logging.basicConfig(filename="functioncalls.log",
                    format="%(levelname)s %(asctime)s %(message)s",
                    datefmt="%x-%X",
                    level=logging.INFO)

def timestamp(f):
    @wraps(f)
    def _(*args, **kwargs):
        logging.info(f.__name__)
        return f(*args, **kwargs)
    return _

@timestamp
def spam():
    print("SPAM!")
    return 100

# spam = timestamp(spam)

spam()
spam()
r = spam()
print(f"{r = }")

@timestamp
def ham(count):
    print("HAM!" * count)

# ham = timestamp(ham)
ham(5)
spam()
ham(10)

@timestamp
def toast(x, y, *extra, ignore_case):
    print(x, y, extra, ignore_case)

toast(5, 10, 15, ignore_case=True)

print(f"{ham.__name__ = }")
print(f"{spam.__name__ = }")
print(f"{toast.__name__ = }")
