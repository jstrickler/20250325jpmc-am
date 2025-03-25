name = 'Ann'
value = 123

print('[{:>10s}]'.format(name))    # Right justify string, pad with space (default)
print('[{:.>10s}]'.format(name))   # Right justify string, pad with '.'
print('[{:->10s}]'.format(name))    # Right justify string, pad with '-'
print('[{:.10s}]'.format(name))    # Left justify string, pad with '.'
print()
print('[{:10d}]'.format(value))    # Right justify number, pad with space (default
print('[{:010d}]'.format(value))   # Right justify number, pad with zeroes
print('[{:_>10d}]'.format(value))  # Right justfy, pad with '_' ('>' required)
print('[{:+>10d}]'.format(value))  # Right justfy, pad with '+' ('>' required)
