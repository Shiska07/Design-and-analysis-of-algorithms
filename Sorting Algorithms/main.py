import datasets
import sorting_algorithms

if __name__ == "__main__":
    res = input("Enter array size of name of file to read from:")
    if res.isdigit():
        n = int(res)
        arr = datasets.get_int_array(n)
    else:
        arr = datasets.read_file(res)

    algo = input(
        "Pick a sorting algorithm from 1) insersion\n 2) merge\n 3) quicksort\n 4) heapsort\n")

    if int(algo) == 1:
        sorting_algorithms.insertion_sort(arr)
    elif int(algo) == 2:
        sorting_algorithms.merge_sort(arr)
    elif int(algo) == 3:
        sorting_algorithms.quick_sort(arr)
    else:
        sorting_algorithms.heap_sort(arr)
