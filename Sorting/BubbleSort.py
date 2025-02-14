def bblsrt(arr):  # Stable sorting algorithm
    l = len(arr)
    for i in range(l):  # for n-1 passes
        swapped = False
        for j in range(l-i-1):  # At ith pass last element will be fixed
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swapped = True

        if swapped == False:
            return


arr = [1, 5, 6, 3]
bblsrt(arr)
print(arr)
