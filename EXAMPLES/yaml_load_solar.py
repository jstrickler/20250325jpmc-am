import yaml
try:
    from yaml import CLoader as Loader  # faster!
except ImportError:
    from yaml import Loader

PLANET_SECTIONS = "inner outer plutoid".split()

with open('../DATA/solar.yaml') as solar_in:
    solar_data = yaml.load(solar_in, Loader=Loader)

star = solar_data['star']
print(f"Our star is {star}\n")

for section in PLANET_SECTIONS:
    for planet in solar_data[section]:
        print(planet['name'])
        for moon in planet['moons']:
            print(f"    {moon}")



