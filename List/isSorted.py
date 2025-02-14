def isSorted(arr, n):
    if n == 1:
        return 1

    if arr[0] > arr[1]:
        for i in range(2, n):
            if arr[i-1] < arr[i]:
                return 0

    elif arr[0] < arr[1]:
        for i in range(2, n):
            if arr[i-1] > arr[i]:
                return 0

    return 1

print(isSorted([1,2,3,4,5,6], 6))
print(isSorted([6,5,4,3,2,1], 6))