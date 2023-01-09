import numpy as np
import random
import sys

# returns an array of size 'n' filled with random integers


def get_int_array(n):
    arr = np.zeros(n, dtype=np.int32)
    for i in range(0, n):
        arr[i] = random.randint(-99999, 99999)
    return arr

# reads a file contraining a list of integers and creates an array


def read_file(filename):
    try:
        f = open(filename, 'rb')
    except OSError:
        print(f"Could not open/read file: {filename}")
        sys.exit()

    line = str(f.readline())
    line = line.strip('\r\n')
    int_list = line.split(',')
    arr = np.zeros(len(int_list), dtype=np.int32)
    for i, item in enumerate(int_list):
        arr[i] = np.int32(item)
    '''
    for i, item in enumerate(int_list):
        try:
            arr[i] = np.int32(item)
        except ValueError:
            print(item, "\n")
    '''
    return arr
