# It is a Divide and Conquer Algorithm
# Partition function is key factor
# Inplace (Uses space for recursive call only), Cache Friendly
# Average Case O(NlogN)
# Worst Case (O(N^2))
# When we don't need stability then quicksort is the fastest

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

def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]

    return i + 1

# QuickSort by Hoare's Partition

def qSorth(arr, l, h):
    if l < h:
        p = hoarsePartition(arr, l, h)
        qSorth(arr, l, p)
        qSorth(arr, p + 1, h)


def qSortl(arr, l, h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        qSortl(arr, l, p-1)
        qSortl(arr, p + 1, h)


arr = [8, 4, 7, 9, 3, 10, 5]
qSorth(arr, 0, 6)
print(arr)

arr = [8, 4, 7, 9, 3, 10, 5]
qSortl(arr, 0, 6)
print(arr)