def zigZag(arr, n):
    for i in range(1, n, 2):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if i != n-1 and arr[i] < arr[i+1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return
