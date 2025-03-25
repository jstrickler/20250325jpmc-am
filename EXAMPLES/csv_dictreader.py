import csv

field_names = ['term', 'firstname', 'lastname', 'birthplace', 'state', 'party'] # field names, which will become dictionary keys on each row

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.DictReader(presidents_in, fieldnames=field_names)  # create reader, passing in field names (if not specified, uses first row as field names)
    for row in rdr:  # iterate over rows in file
        print(f"{row['firstname']:25} {row['lastname']:12} {row['party']}")
