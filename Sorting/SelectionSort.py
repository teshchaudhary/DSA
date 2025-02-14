# Find the minimum and update it to the first place and then on second and so on
# O(n^2)

def selectionSort(arr):  # Unstable sorting algorithm
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                arr[j], arr[min_index] = arr[min_index], arr[j]

    return arr


print(selectionSort([1, 5, 4, 7]))
