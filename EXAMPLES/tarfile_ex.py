import tarfile
import os

for tar_file in ('pres.tar', 'NOT_A.tar', 'potus.tar.gz'):  # iterate over sample files
    filename = os.path.join('../DATA', tar_file)
    is_valid = tarfile.is_tarfile(filename)  # check to see if file is a tarfile
    text = 'IS' if is_valid else 'IS NOT'
    print(f"{filename} {text} a tarfile")
print()

with tarfile.open('../DATA/pres.tar') as tarfile_in:  # open tar file
    for member in tarfile_in:  # iterate over members
        print(member.name, member.size)  # access member data
    print()

with tarfile.open('../DATA/pres.tar') as tarfile_in:
    tarfile_in.extract('presidents.txt', path='../TEMP')  # extract member to local file

with tarfile.open('../DATA/potus.tar.gz') as tarfile_in:
    tarfile_in.extract('presidents.csv', path='../TEMP')  # extract member to local file

with tarfile.open('../TEMP/text_files.tar', 'w') as tarfile_out:  # open new tar archive for writing
    tarfile_out.add('../DATA/parrot.txt')  # add member
    tarfile_out.add('../DATA/alice.txt')  # add member

with tarfile.open('../TEMP/more_text_files.tar.gz', 'w:gz') as tar_gz_write:  # open new tar archive for writing; archive is compressed with gzip
    tar_gz_write.add('../DATA/parrot.txt')  # add member
    tar_gz_write.add('../DATA/alice.txt')  # add member
