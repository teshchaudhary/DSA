def deleteFromArray(arr, n, idx):  # Last element will be 0
    for i in range(idx, n-1):
        arr[i] = arr[i+1]

    arr[n-1] = 0
    return arr


print(deleteFromArray([1, 2, 3, 4, 5], 5, 3))