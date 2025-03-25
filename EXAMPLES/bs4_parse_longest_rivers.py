import re
import bs4
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_river_systems_by_length'
NUM_RIVERS = 25 # max rivers to get from table

# use regular expression to get tag for desired table
TABLE_CLASS = re.compile(
    "^wikitable +", 
    re.DOTALL | re.MULTILINE,
)

def main():
    soup = get_soup()
    river_table = soup.find(class_=TABLE_CLASS)
    if river_table:
        parse_table(river_table)
    else:
        print("Table not found")

def get_soup():
    try:
        response = requests.get(URL)
    except Exception as err:
        print(err)
        exit()
    else:
        soup = bs4.BeautifulSoup(response.text, 'lxml')

    return soup

def parse_table(river_table):
    for row_number, row_data in enumerate(river_table.find_all("tr")):
        columns = row_data.find_all("td")
        if columns:
            if row_number > NUM_RIVERS:
                break
            river_name = columns[0].find('a').get('title')
            raw_length = columns[2].contents[0]
            river_length = convert_length(raw_length)
            print(f"{row_number:2d} {river_name:20s} {river_length:5d}")

def convert_length(raw_length):
    temp_length = raw_length.replace(',', '').replace('*','')
    return int(temp_length)

if __name__ == "__main__":
    main()