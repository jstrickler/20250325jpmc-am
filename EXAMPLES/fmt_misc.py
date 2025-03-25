'''Demonstrate misc formatting'''

big_number = 2303902390239

print("Big number: {:,d}".format(big_number))  # Add commas for readability
print()

value = 27

print("Binary: {:#010b}".format(value))  # Binary format with leading 0b
print("Octal:  {:#010o}".format(value))  # Octal format with leading 0o
print("Hex:    {:#010x}".format(value))  # Hexadecimal format with leading 0x
print()
