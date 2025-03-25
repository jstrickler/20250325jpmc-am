import sqlite3

colors = []
colors = list()   # list colors = new list();

count = 0

db_conn = sqlite3.connect("wombats.db")

print(f"{type(sqlite3) = }")
print(f"{type(colors) = }")
print(f"{type(count) = }")
print(f"{type(db_conn) = }")

colors.append('blue')
colors.append('sea green')
colors.insert(0, 'white')
colors.sort()  #  list.sort(colors)
print(f"{colors = }")

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()  # Dog d1 = new Dog(); 
d2 = Dog()
d1.bark()
d2.bark()

t1 = 5
t2 = t1

from copy import deepcopy
x = []
y = x    # alias
z = list(x)   # shallow copy
m = deepcopy(x)  # deep copy