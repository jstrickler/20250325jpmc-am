import re
from pymongo import MongoClient, errors

FIELD_NAMES = (
    'termnumber lastname firstname '
    'birthdate '
    'deathdate birthplace birthstate '
    'termstartdate '
    'termenddate '
    'party'
).split()  # define some field name

mc = MongoClient()  # get a Mongo client

try:
    mc.drop_database("presidents")  # delete 'presidents' database if it exists
except errors.PyMongoError as err:
    print(err)

db = mc["presidents"]  # create a new database named 'presidents'

coll = db.presidents  # get the collection from presidents db

with open('../DATA/presidents.txt') as presidents_in:  # open a data file
    for line in presidents_in:
        flds = line[:-1].split(':')
        kvpairs = zip(FIELD_NAMES, flds)
        record_dict = dict(kvpairs)
        coll.insert_one(record_dict)  # insert a record into collection

print(db.list_collection_names())  # get list of collections
print()

abe = coll.find_one({'termnumber': '16'})  # search collection for doc where termnumber == 16
print(abe, '\n')

for field in FIELD_NAMES:
    print(f"{field.upper():15s} {abe[field]}")  # print all fields for one record

print('-' * 50)

for president in coll.find():  # loop through all records in collection
    print(f"{president['firstname']:25s} {president['lastname']:30s}")
print('-' * 50)

rx_lastname = re.compile('^roo', re.IGNORECASE)
for president in coll.find({'lastname': rx_lastname}):  # find record using regular expression
    print(f"{president['firstname']:25s} {president['lastname']:30s}")
print('-' * 50)

for president in coll.find({"birthstate": 'Virginia'}):  # find record searching multiple fields
    print(f"{president['firstname']:25s} {president['lastname']:30s}")

print('-' * 50)
print("removing Millard Fillmore")
result = coll.delete_one({'lastname': 'Fillmore'})  # delete record
print(result)
result = coll.delete_one({'lastname': 'Roosevelt'})  # delete record
print(result)
print('-' * 50)


result = coll.delete_one({'lastname': 'Bush'})
print(dir(result))
print()

result = coll.count_documents({})  # get count of records
print(result)


for president in coll.find():  # loop through all records in collection
    print(f"{president['firstname']:25s} {president['lastname']:30s}")
print('-' * 50)

animals = db.animals

print(animals, '\n')

animals.insert_one({'name': 'wombat', 'country': 'Australia'})
animals.insert_one({'name': 'ocelot', 'country': 'Mexico'})
animals.insert_one({'name': 'honey badger', 'country': 'Iran'})

for doc in animals.find():
    print(doc['name'])
