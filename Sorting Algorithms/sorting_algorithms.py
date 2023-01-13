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
    n1 = q - p + 1
    n2 = r - q

    # left and right subarrays
    L = np.zeros(n1, np.int32)
    R = np.zeros(n2, np.int32)

    for i in range(0, n1):
        L[i] = arr[p + i]

    for i in range(0, n2):
        R[i] = arr[q + 1 + i]

    i = 0
    j = 0
    k = p

    while (k >= p) and (k <= r):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


def merge_sort(arr, p, r):
    if p < r:
        q = p + (r-1)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
    print(arr)


def quick_sort(arr):
    pass


def heap_sort(arr):
    pass
