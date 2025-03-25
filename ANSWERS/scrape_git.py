import bs4
import requests
import json

URL = 'https://git-scm.com'

response = requests.get(URL)
links = {}

if response.status_code == requests.codes.OK:
    soup = bs4.BeautifulSoup(response.content.decode(), 'lxml')
    for link in soup.findAll('a'):
        href = link.get('href')
        if href.startswith('http'):
            print(href)
            links[link.get_text()] = href

    with open('links.json', 'w') as json_out:
        json.dump(links, json_out, indent=4)
