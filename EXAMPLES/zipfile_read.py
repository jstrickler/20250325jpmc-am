from zipfile import ZipFile

# read & extract from zip file
zip_in = ZipFile("../DATA/textfiles.zip")  # Open zip file for reading
print(zip_in.namelist())  # Print list of members in zip file
tyger_text = zip_in.read('tyger.txt').decode()  # Read (raw binary) data from member and convert from bytes to string
print(tyger_text[:100], '\n')
zip_in.extract('parrot.txt')  # Extract member

