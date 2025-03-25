import bs4

with open('../DATA/craigslist.html', 'r') as CL:
    soup = bs4.BeautifulSoup(CL, 'lxml')

for input_tag in soup.findAll('input'):
    tag_name = input_tag.get('name', "*NO NAME*")
    tag_type = input_tag.get('type', '*NO TYPE*')
    print(f"{tag_name} ({tag_type})")
