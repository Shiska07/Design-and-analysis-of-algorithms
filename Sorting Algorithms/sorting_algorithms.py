import numpy as np
import math
import random

# Helper function fot heap sort helps value float down
# Running time : O(lg(n))
def min_heapify(arr, idx):
    l = 2*idx + 1           # left child
    r = 2*idx + 2           # right child
    smallest = idx

    heap_size = len(arr)

    if l < heap_size and arr[l] < arr[idx]:
        smallest = l

    if r < heap_size and arr[r] < arr[smallest]:
        smallest = r

    if smallest != idx:
        key = arr[idx]
        arr[idx] = arr[smallest]
        arr[smallest] = key
        arr = min_heapify(arr, smallest)

    return arr

# Helper function fot heap sort helps build heap
# Running time : O(lg(n))
def build_min_heap(arr):
    heap_size = len(arr)
    i = math.floor((heap_size - 2)/2)

    while i >= 0:
        arr = min_heapify(arr, i)
        i -= 1
    return arr

# Helper function for quicksort
# Running time : O(n)
def randomized_partition(arr, p, r):

    # get a random index
    r_i = random.randint(p, r)

    # exchange last value with value at random index
    pivot = arr[r_i]
    arr[r_i] = arr[r]
    arr[r] = pivot

    i = p - 1
    j = p
    while j <= (r - 1):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
        j += 1
    (arr[i+1], arr[r]) = (arr[r], arr[i+1])
    return arr, i + 1


# O(n^2)
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


# O(nlg(n))
def heap_sort(arr):
    arr = build_min_heap(arr)
    i = len(arr) - 1
    j = 0
    sorted_arr = [0]*len(arr)
    while i >= 0:
        key = arr[i]
        sorted_arr[j] = arr[0]
        arr[0] = key
        arr = min_heapify(arr[:i+1], 0)
        i -= 1
        j += 1

    print(sorted_arr)         
    
    
# O(nlog(n)) average   
def quick_sort(arr, p, r):
    if p < r:
        arr, q = randomized_partition(arr, p, r)
        arr = quick_sort(arr, p, q-1)
        arr = quick_sort(arr, q+1, r)
    
    return arr
    
