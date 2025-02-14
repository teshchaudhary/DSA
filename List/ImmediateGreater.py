def immediateGreater(arr, x):
    res = -1

    for i in range(len(arr)):
        if arr[i] > x:
            if res == -1 or res > arr[i]:
                res = arr[i]

    return res


print(immediateGreater([9, 11, 12, 13], 10))
