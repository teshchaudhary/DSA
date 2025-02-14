# Using Hoare's Partitioning
def rearrange(arr):
    i = -1
    j = len(arr)
    pivot = 0

    while True:
        i += 1

        while arr[i] > pivot:
            i += 1

        j -= 1

        while arr[j] < pivot:
            j -= 1

        if i >= j:
            return

        arr[i], arr[j] = arr[j], arr[i]


arr = [1, -3, 4, -5, -9, 7, 6, 2]

rearrange(arr)
print(arr)
