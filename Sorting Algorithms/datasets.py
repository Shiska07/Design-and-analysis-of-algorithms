import numpy as np
import random
import sys

# returns an array of size 'n' filled with random integers


def get_int_array(n):
    arr = [0]*n
    for i in range(0, n):
        arr[i] = random.randint(-99999, 99999)
    return arr

# reads a file contraining a list of integers and creates an array


def read_file(filename):
    try:
        f = open(filename, 'r')
    except OSError:
        print(f"Could not open/read file: {filename}")
        sys.exit()

    line = str(f.readline())
    int_list = line.split(',')
    arr = []*len(int_list)
    for i, item in enumerate(int_list):
        item = item.strip('\r\n')
        arr[i] = np.int32(item)
    return arr
