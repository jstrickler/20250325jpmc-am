import sys
import os
from collections import Counter

start_dir = sys.argv[1]

ext_counter = Counter()

for curr_dir, dir_list, file_list in os.walk(start_dir):
    for file_name in file_list:
        base, ext = os.path.splitext(file_name)
        if ext:
            ext_counter[ext] += 1

for ext in ext_counter:
    print(ext, ext_counter[ext])