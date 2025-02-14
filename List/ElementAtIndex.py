def getByIndex(arr, n, idx):
    l = len(arr)
    if idx > n-1 or idx < 0:
        return -1

    else:
        return arr[idx]

print(getByIndex([1,2,3,4,5],5,3))