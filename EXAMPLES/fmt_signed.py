values = 123, -321, 14, -2, 0

for value in values:
    print("default: |{:d}|".format(value))  # default (pipe symbols just to show white space)
print()

for value in values:
    print("   plus: |{:+d}|".format(value))  # plus sign puts '+' on positive numbers (and zero) and '-' on negative
print()

for value in values:
    print("  minus: |{:-d}|".format(value)) # minus sign only puts '-' on negative numbers
print()

for value in values:
    print("  space: |{: d}|".format(value)) # space puts '-' on negative numbers and space on others
print()
