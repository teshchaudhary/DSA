# Count occurences in sorted array

# def count(arr, ele):
#     res = 0
#     for i in arr:
#         if i == ele:
#             res += 1

#     return res


# print(count([1, 2, 2, 3, 4, 5], 2))

# Optimized
def firstOcc(arr, ele):
    si = 0
    ei = len(arr)

    while si <= ei:
        mid = (si+ei)//2
        if ele < arr[mid]:
            ei = mid - 1

        elif ele > arr[mid]:
            si = mid + 1

        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                ei = mid - 1


def lastOcc(arr, ele):
    si = 0
    ei = len(arr)

    while si <= ei:
        mid = (si+ei)//2
        if ele < arr[mid]:
            ei = mid - 1

        elif ele > arr[mid]:
            si = mid + 1

        else:
            if mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                si = mid + 1


def count(arr, ele):
    if firstOcc(arr, ele) == -1:
        return 0
    return (lastOcc(arr, ele) - firstOcc(arr, ele)) + 1


print(count([1, 2, 2, 2, 3, 4, 5], 2))
