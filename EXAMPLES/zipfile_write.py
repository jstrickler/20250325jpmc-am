from zipfile import ZipFile, ZIP_DEFLATED
import os.path

file_names = ["parrot.txt", "tyger.txt", "knights.txt", "alice.txt", "poe_sonnet.txt", "spam.txt"]
file_folder = "../DATA"

zipfile_name = "example.zip"

# creating new, empty, zip file
zip_out = ZipFile(zipfile_name, mode="w", compression=ZIP_DEFLATED)  # Create new zip file

# add files to zip file
for file_name in file_names:
    file_path = os.path.join(file_folder, file_name)
    zip_out.write(file_path, file_name)  # Add member to zip file
zip_out.close()

# list files in zip 
zip_in = ZipFile(zipfile_name)
print("Files in archive:")
print(zip_in.namelist())