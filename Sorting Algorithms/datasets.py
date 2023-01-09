import numpy as np
import random
import sys

# returns an array of size 'n' filled with random integers
def get_int_array(n):
    arr = np.zeros(n, dtype=np.int32)
    for i in range(0, n):
        arr[i] = random.randomint(-99999, 99999)
    return arr

# reads a file contraining a list of integers and creates an array
def read_file(filename):
    try:
        f = open(filename, 'rb')
    except OSError:
        print(f"Could not open/read file: {filename}")
        sys.exit()

    line = f.readline()
    int_list = line.split(',')
    arr = np.zeros(len(int_list), dtype=np.int32)
    for i, item in enumerate(int_list):
        arr[i] = item
    return arr
