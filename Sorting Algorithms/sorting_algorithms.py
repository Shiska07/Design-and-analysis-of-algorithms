import numpy as np
import math


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

def merge(arr, p, q, r):
    n1 = 

def merge_sort(arr, p, r):
    if p < r:
        q = math.floor((p + r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def quick_sort(arr):
    pass


def heap_sort(arr):
    pass
