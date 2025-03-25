from bs4 import BeautifulSoup
import re

rx_digit = re.compile(r'\d')

with open('../DATA/people.xml') as people_in:
    soup = BeautifulSoup(
        markup=people_in, 
        features="xml",
    )

for person in soup.findAll('person'):
    print(person.string)
print('-' * 60)

for tag in soup.findAll(re.compile(r'^s')):
    print(tag)
print('-' * 60)

for tag in soup.findAll(['street', 'state']):
    print(f"{tag}\n  {tag.string}")
print('-' * 60)

all_tags = soup.findAll(True)
print(f"There were {len(all_tags)} tags")
print('-' * 60)


def has_digit(tag):
    'Return True if specified string contains at least one digit'
    return tag.string != None and rx_digit.search(tag.string)

for tag in soup.findAll(has_digit):
    print(tag.string)
print('-' * 60)

for tag in soup.findAll(class_='number'):
    print(tag)
print('-' * 60)

for tag in soup.findAll(re.compile(r'wacker', re.IGNORECASE)):
    print(tag)
print('-' * 60)
