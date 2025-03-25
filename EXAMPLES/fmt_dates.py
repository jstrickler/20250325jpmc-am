from datetime import datetime

event = datetime(2016, 1, 2, 3, 4, 5)

print(event)  # Default string version of date
print()

print("Date is {0:%m}/{0:%d}/{0:%y}".format(event))  # Use three placeholders for month, day, year
print("Date is {:%m/%d/%y}".format(event))  # Format month, day, year with a single placeholder
print("Date is {:%A, %B %d, %Y}".format(event))  # Another single placeholder format
