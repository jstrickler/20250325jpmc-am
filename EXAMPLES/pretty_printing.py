from pprint import pprint

struct = {  # nested data structure
    'epsilon': [
        ['a', 'b', 'c'], ['d', 'e', 'f']
    ],
    'theta': {
        'red': 55,
        'blue': [8, 98, -3],
        'purple': ['Chicago', 'New York', 'L.A.'],
    },
    'alpha': ['g', 'h', 'i', 'j', 'k'],
    'gamma': [39029384, 3827539203, 94838402, 249398063],
}

print('Without pprint (normal output:')
print(struct)  # print normally
print()

print('With pprint:')
pprint(struct)  # pretty-print
print()

print('With pprint (sort_dicts=False):')
pprint(struct, sort_dicts=False)  # Leave dictionary in default order
print()

print('With pprint (depth=2):')
pprint(struct, depth=2)  # only print top two levels of structure
print()

print('With pprint (width=40):')
pprint(struct, width=40)  # set display width
print()

print('With pprint (underscore_numbers=True):')
pprint(struct, underscore_numbers=True)  # Put underscores in large numbers for readability
