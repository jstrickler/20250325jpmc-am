import pickle
from pprint import pprint

# some data structures
airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}

colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]

values = [
    3/7, 1/9, 14.5
]

data = [  # list of data structures
    colors,
    airports,
    values,
]

print("BEFORE:")
pprint(data)
print('-' * 60)



with open('../TEMP/pickled_data.pkl', 'wb') as pkl_out:  # open pickle file for writing in binary mode
    pickle.dump(data, pkl_out)  # serialize data structures to pickle file

with open('../TEMP/pickled_data.pkl', 'rb') as pkl_in:  # open pickle file for reading in binary mode
    pickled_data = pickle.load(pkl_in)  # de-serialize pickle file back into data structures

print("AFTER:")
pprint(pickled_data)  # view data structures
