import csv

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)  # <1>
    for row in rdr:  # <2>
        print(f'{row[1]:25s} {row[2]:12s} {row[-1]}')
