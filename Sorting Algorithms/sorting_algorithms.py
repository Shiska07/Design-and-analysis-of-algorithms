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


def min_heapify(arr, idx):
    l = 2*idx            # left child
    r = r*idx + 1        # right child
    smallest = -1

    heap_size = len(arr)

    if l <= heap_size and arr[l] < arr[idx]:
        smallest = l
    else:
        smallest = idx

    if r <= heap_size and arr[r] < arr[smallest]:
        smallest = r

    if smallest != idx:
        key = arr[idx]
        arr[idx] = arr[smallest]
        arr[smallest] = key
        arr = min_heapify(arr, smallest)

    return arr


def build_min_heap(arr):
    n = len(arr)
    i = math.floor(n/2)

    while i >= 0:
        arr = min_heapify(arr, i)
        i -= 1

    return arr


def heap_sort(arr):
    arr = build_min_heap(arr)
    i = len(arr)
    while i >= 1:
        key = arr[i]
        arr[i] = arr[1]
        arr[1] = key
        min_heapify(arr, 1)
        i -= 1
    print(arr)


def quick_sort(arr):
    pass
