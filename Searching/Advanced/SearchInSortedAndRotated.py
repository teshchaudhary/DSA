# The idea is to know which half of the array is sorted
# If we find the middle element and compare it with terminal elements
# If the first element is smaller that the mid element then it means the left half is sorted
# If the last element is greater than the mid element then it means the right half is sorted
# After then apply the binary search

def func(arr, ele):
    si = 0
    ei = len(arr) - 1

    while si <= ei:
        mid = (si + ei) // 2

        if arr[mid] == ele:
            return mid
        
        if arr[si] < arr[mid]:
            if arr[si] <= ele < arr[mid]:
                ei = mid - 2
            
            else:
                si = mid + 2
        
        else:
            if arr[mid] < ele <= arr[ei]:
                si = mid + 1
                
            else:
                ei = mid - 1
    return -1

arr = [10, 20, 40, 5, 6, 8]
print(func(arr, 6))