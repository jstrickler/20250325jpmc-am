import pickle

with open('presidents.pkl','rb') as presidents_in:
    presidents = pickle.load(presidents_in)

for term_number, president_info in presidents.items():
    print(f"{president_info['firstname']:20.20s} {president_info['lastname']:20.20s} {president_info['party']}")
