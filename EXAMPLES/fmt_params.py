person = 'Bob'
age = 22

print("{0} is {1} years old.".format(person, age))  # Placeholders can be numbered
print("{0}, {0}, {0} your boat".format('row'))  # Placeholders can be reused
print("The {1}-year-old is {0}".format(person, age))  # They do not have to be in order (but usually are)
print("{name} is {age} years old.".format(name=person, age=age))  # Selectors can be named
print()
print("{} is {} years old.".format(person, age))  # Empty selectors are autonumbered (but all selectors must either be empty or explicitly numbered)
print("{name} is {} and his favorite color is {}".format(22, 'blue', name='Bob'))  # Named and numbered selectors can be mixed
