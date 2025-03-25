import csv

FRUIT_DATA = [
    ("pomegranate", 'each', .99),
    ("cherry", 'pound', 2.25),
    ("apricot", 'pound', 3.49),
    ("date", 'pound', 1.20),
    ("apple", 'pound', .55),
    ("lemon", 'each', .69),
    ("kiwi", 'each', .88),
    ("orange", 'each', .49),
    ("lime", 'each', .49),
    ("watermelon", 'each', 4.50),
    ("guava", 'pound', 2.88),
    ("papaya", 'pound', 1.79),
    ("fig", 'pound', 2.29),
    ("pear", 'pound', 1.10),
    ("banana", 'pound', .65),
]

with open('../DATA/fruit_data.csv', 'w') as fruit_out:
    wtr = csv.writer(fruit_out, quoting=csv.QUOTE_NONNUMERIC)
    for row in FRUIT_DATA:
        wtr.writerow(row)
