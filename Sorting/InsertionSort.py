# We split in two lists one is sorted part another is unsorted as we iterate, we increase the sorted part by inserting one element from the unsorted part to the sorted part

# Worst Case O(n^2)
# Good for small inputs
# Best Case O(n)

def insertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        ele = arr[i]  # The element of unsorted list
        j = i-1  # Just the left side of the unsorted element i.e in sorted list
        # We'll never go inside this loop if the elements are already sorted
        while j >= 0 and ele < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = ele


arr = [9,8,7,6]
insertionSort(arr)
print(arr)
