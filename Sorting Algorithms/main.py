import datasets
import sorting_algorithms
import time

if __name__ == "__main__":
    res = input("Enter array size of name of file to read from:")
    if res.isdigit():
        n = int(res)
        arr = datasets.get_int_array(n)
    else:
        arr = datasets.read_file(res)

    algo = input(
        "Pick a sorting algorithm from:\n 1) insersion\n 2) heap sort\n 3) quicksort\n")

    start = time.monotonic()

    if int(algo) == 1:
        sorting_algorithms.insertion_sort(arr)
    elif int(algo) == 2:
        sorting_algorithms.heap_sort(arr)
    elif int(algo) == 3:
        arr = sorting_algorithms.quick_sort(arr, 0, (len(arr) - 1))
        print(arr)

    end = time.monotonic()

    diff = end - start

    print('Time elapsed: {:.5f}s.\n'.format(diff))
