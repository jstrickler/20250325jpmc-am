import sys
import json

def main(args):
    data = get_meteorite_data()
    if args:
        display_args = [data, args[0]]
    else:
        display_args = [data]
    display_data(*display_args)

def get_meteorite_data():
    with open('../DATA/meteorite_events.json') as solar_in:
        meteorite_events = json.load(solar_in)
    return meteorite_events


def by_mass(event):
    return float(event.get('mass', 0))

def by_year(event):
    return event.get('year',"UNKNOWN")[:4]

def by_name(event):
    return event.get('name', 'Unknown')

def display_data(data, sort_type="name"):
    if sort_type == 'name':
        key_function = by_name
    elif sort_type == "mass":
        key_function = by_mass
    elif sort_type == 'year':
        key_function = by_year
    else:
        raise TypeError("Invalid sort type")

    for event in sorted(data, key=key_function):
        name = event.get('name', 'Unknown')
        mass = float(event.get('mass', 0))/1000
        year = (event.get('year')[:4] if event.get('year') else "None")
        print(f"{name:25s} {mass:8.3f} {year}")

if __name__ == '__main__':
    main(sys.argv[1:])
