import sys
import os
from collections import Counter

start_dir = sys.argv[1]

for curr_dir, dir_list, file_list in os.walk(start_dir):
    for file_name in file_list:
        pass 
