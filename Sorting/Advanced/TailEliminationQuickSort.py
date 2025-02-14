def hoarsePartition(arr, l, h):
    i = l - 1
    j = h + 1
    pivot = arr[l]

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def qSorth(arr, l, h):
    while l < h:
        p = hoarsePartition(arr, l, h)
        qSorth(arr, l, p)
        l = p + 1

arr = [8, 4, 7, 9, 3, 10, 5]
qSorth(arr, 0, 6)
print(arr)