from pprint import pprint
import json

# json.loads(STRING)     load from string
# json.load(FILE_OBJECT) load from file-like object

with open('../DATA/solar.json') as solar_in:  # open JSON file for reading
    solar = json.load(solar_in)  # load from file object and convert to Python data structure

# uncomment to see raw Python data
# print('-' * 60)
# pprint(solar)
# print('-' * 60)
# print('\n\n')

print(solar['innerplanets'])  # solar is just a Python dictionary
print('*' * 60)
print(solar['innerplanets'][0]['name'])
print('*' * 60)
for planet in solar['innerplanets'] + solar['outerplanets']:
    print(planet['name'])

print("*" * 60)
for group in solar:
    if group.endswith('planets'):
        for planet in solar[group]:
            print(planet['name'])
