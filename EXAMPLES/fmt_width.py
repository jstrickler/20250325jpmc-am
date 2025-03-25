name = 'Ann Elk'
value = 10000
airspeed = 22.347
# note: [] are used to show blank space, and are not part of the formatting
print('[{:s}]'.format(name))     # Default format -- no padding
print('[{:10s}]'.format(name))   # Left justify, 10 characters wide
print('[{:3s}]'.format(name))    # Left justify, 3 characters wide, displays entire string
print('[{:3.3s}]'.format(name))  # Left justify, 3 characters wide, truncates string to max width
print()
print('[{:8d}]'.format(value))       # Right justify, decimal, 8 characters wide (all numbers are right-justified by default)
print('[{:8f}]'.format(value))       # Right justify int as float, 8 characters wide
print('[{:8f}]'.format(airspeed))    # Right justify float as float, 8 characters wide
print('[{:.2f}]'.format(airspeed))   # Right justify, float, 3 decimal places, no maximum width
print('[{:8.3f}]'.format(airspeed))  # Right justify, float, 3 decimal places, maximum width 8
