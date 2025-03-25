import bs4

with open('../DATA/people.xml') as people_in:  # Open input file
    soup = bs4.BeautifulSoup(
        people_in,
        features='xml',
    )  # Create a BeautifulSoup object

new_tag = soup.new_tag('person', org='Oracle')  # Create a new XML 'person' tag with XML attribute 'org'
new_tag.string = 'Larry Ellison'  # Add the string contents for the new tag

people = soup.find('people')  # Find the 'people' tag
people.append(new_tag)  # Append the new tag as a child of 'people'

suite_tag = soup.find('suite')  # Find the 'suite' tag
suite_tag.decompose()   # Remove the 'suite' tag

new_xml = soup.prettify()  # Create an XML string
print(new_xml)
