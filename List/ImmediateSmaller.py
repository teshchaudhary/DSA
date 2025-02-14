def immediateSmaller(arr, x):
    res = -1

    for i in range(len(arr)):
        if arr[i] < x:
            if res == -1 or res < arr[i]:
                res = arr[i]

    return res


print(immediateSmaller([1, 2, 3, 4, 5, 6], 4))
