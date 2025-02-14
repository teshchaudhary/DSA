def binary_search_recursive(arr, ele, si, ei):
    
    if ei >= si: 
        mid = (si+ei)//2

        if arr[mid] == ele:
            return mid

        elif arr[mid] > ele:
            return binary_search_recursive(arr, ele, si, mid-1)

        else:
            return binary_search_recursive(arr, ele, mid+1, ei)

    else:
        return -1

print(binary_search_recursive([1,2,3,4,5], 6, 0, 4))