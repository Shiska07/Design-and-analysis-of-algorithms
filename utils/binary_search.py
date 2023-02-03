# O(logn)
def binary_search_iterative(arr, low, high, val):
    
    while high >= low:
        mid = high + low // 2
        
        if arr[mid] == val:
            return mid
        
        if arr[mid] > val:
            high = mid - 1
            
        else:
            low = mid + 1
    
    return -1
           
            