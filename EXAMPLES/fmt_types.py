person = 'Bob'
value = 488
bigvalue = 3735928559
result = 234.5617282027

print('{:s}'.format(person))    # String 
print('{name:s}'.format(name=person))    # String
print('{:d}'.format(value))    # Integer (displayed as decimal)
print('{:b}'.format(value))    # Integer (displayed as binary)
print('{:o}'.format(value))    # Integer (displayed as octal)
print('{:x}'.format(value))    # Integer (displayed as hex)
print('{:X}'.format(bigvalue))    # Integer (displayed as hex with uppercase digits)
print('{:f}'.format(result))    # Float (defaults to 6 places after the decimal point)
print('{:.2f}'.format(result))    # Float rounded to 2 decimal places
