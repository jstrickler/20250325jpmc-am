name = 'Ann'
value = 12345
nvalue = -12345

# note: all of the following print in a field 10 characters widedd
print('[{0:10s}]'.format(name))    # Default (left) alignment 
print('[{0:<10s}]'.format(name))   # Explicit left alignment
print('[{0:>10s}]'.format(name))   # Right alignment
print('[{0:^10s}]'.format(name))   # Centered
print()
print('[{0:10d}] [{1:10d}]'.format(value, nvalue))    # Default (right) alignment
print('[{0:>10d}] [{1:>10d}]'.format(value, nvalue))  # Explicit right alignment
print('[{0:<10d}] [{1:<10d}]'.format(value, nvalue))  # Left alignment
print('[{0:^10d}] [{1:^10d}]'.format(value, nvalue))  # Centered
print('[{0:=10d}] [{1:=10d}]'.format(value, nvalue))  # Right alignment, but pad _after_ sign
