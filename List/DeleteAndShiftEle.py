def das(arr, ele):
    i = 0
    l = len(arr)
    while i < l:
        if arr[i] == ele:
            for j in range(i, l-1):
                arr[j] = arr[j+1]
            arr[l-1] = 0
        i += 1

    return arr


print(das([1, 2, 3, 3, 4, 5], 3))
