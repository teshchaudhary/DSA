# We divide and then merge the lists

# Theta(nlogn) Time Complexity
# O(n) Auxilliary Space
# For arrays quicksort works better than mergesort


def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low


    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1

        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r): # Stable
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [9,8,1,5,3,4]

mergeSort(arr, 0, len(arr))
print(arr)