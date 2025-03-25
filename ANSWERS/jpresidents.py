import json

with open('../DATA/presidents.json') as PRES:
    p = json.load(PRES)

for pres in p['presidents']:
    name = pres['lastname'] + ', ' + pres['firstname']
    state = pres['birthstate']
    print(f'{name:40s} {state:30s}')
