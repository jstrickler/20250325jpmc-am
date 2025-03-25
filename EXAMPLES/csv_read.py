import csv

with open('../DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)  # create CSV reader
    for name, title, color, quest, comment, number, ladies in rdr:  # Read and unpack records one at a time; each record is a list
        print(f'{title:4s} {name:9s} {quest}')
