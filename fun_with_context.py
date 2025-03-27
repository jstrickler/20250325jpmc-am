
with open('DATA/mary.txt') as mary_in:  # _io.FileIOWrapper
    contents = mary_in.read()
# mary_in.close()


class Scream:
    def __enter__(self):
        print("Before...")
    
    def __exit__(*args):
        print("After")

with  Scream() as scream:
    print("using scream....")

