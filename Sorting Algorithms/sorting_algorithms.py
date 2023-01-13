import numpy as np
import sys
sys.setrecursionlimit(1500)


def insertion_sort(arr):
    length = len(arr)
    for j in range(1, length):
        key = arr[j]
        i = j - 1
        while (i >= 0) & (arr[i] > key):
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    print(arr)


def quick_sort(arr):
    pass


def heap_sort(arr):
    pass
