# Count 1's in a sorted Binary array


def firstOcc(arr, ele):
    si = 0
    ei = len(arr) - 1

    while si <= ei:
        mid = (si+ei)//2
        if ele < arr[mid]:
            ei = mid-1
        elif ele > arr[mid]:
            si = mid+1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                ei = mid - 1
    return -1


def countOnes(arr):
    l = len(arr)
    if firstOcc(arr, 1) == -1:
        return 0

    return l - firstOcc(arr, 1)


print(countOnes([0, 0, 0, 0, 1, 1, 1, 1, 1]))
