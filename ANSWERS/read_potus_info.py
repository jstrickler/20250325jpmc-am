import pickle

with open('potus.pkl','rb') as POTUS:
    presidents = pickle.load(POTUS)

for p in presidents:
    print(f"{p.firstname} {p.lastname} {p.party}")
