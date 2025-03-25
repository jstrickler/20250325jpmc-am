from zipfile import ZipFile

with ZipFile('potus.zip','w') as zip_out:
    zip_out.write('save_potus_info.py')
    zip_out.write('read_potus_info.py')
    zip_out.write('potus.pkl')
