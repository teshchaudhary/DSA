def helper(arr, ele, si, ei):
    if si > ei:
        return -1

    mid = (si+ei)//2

    if arr[mid] == ele:
        return mid

    elif ele > arr[mid]:
        return helper(arr, ele, mid+1, ei)

    else:
        return helper(arr, ele, si, mid)


def BinarySearchRec(arr, ele):
    return helper(arr, ele, 0, len(arr)-1)


print(BinarySearchRec([1, 2, 3, 4, 5], 4))
