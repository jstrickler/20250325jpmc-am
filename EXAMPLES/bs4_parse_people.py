import bs4

with open('../DATA/people.xml') as people_in:
    soup = bs4.BeautifulSoup(
        people_in, 
        features="xml",
)

for person in soup.findAll('person'):
    print(f"{person.string}, {person.get('org')}")
