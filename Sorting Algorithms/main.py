import datasets

if __name__ == "__main__":
    res = input("Enter array size of name of file to read from:")
    if res.isdigit():
        n = int(res)
        arr = datasets.get_int_array(n)
    else:
        arr = datasets.read_file(res)

    print("The array is: ", arr)
