# def lastOccurence(arr, ele):
#     for i in reversed(len(arr)):
#         if arr[i] == ele:
#             return i

#     return -1

# O(log(n))

def lastOccurence(arr, ele):
    si = 0
    ei = len(arr)-1

    while si <= ei:
        mid = (si+ei)//2

        if ele < arr[mid]:
            ei = mid-1

        elif ele > arr[mid]:
            si = mid+1
        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                si = mid + 1
    return -1


print(lastOccurence([1, 1, 2, 2, 3, 4, 5, 6, 6], 7))
