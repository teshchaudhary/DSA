# Check if a pair makes the target sum when added in a sorted array
# This technique works well only with sorted array if we want to use it we need to sort the array first
# For unsorted array hashing works
# O(n)

def func(arr, target_sum):
    l = len(arr)
    i = 0
    j = l - 1

    while i < j:

        # In sorted array of the sum is more than target sum then the values at last side will give more values with others
        if arr[i] + arr[j] > target_sum:
            j -= 1

        # In sorted array of the sum is less than target sum then the values at starting side will give less values with others
        elif arr[i] + arr[j] < target_sum:
            i += 1

        elif arr[i] + arr[j] == target_sum:
            return True

    return False


arr = [1, 2, 3, 4, 5]
print(func(arr, 10))
