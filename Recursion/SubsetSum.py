def SubsetSum(arr, n, target):
    if n == 0:
        return 1 if target == 0 else 0

    return SubsetSum(arr, n-1, target) + SubsetSum(arr, n-1, target - arr[n-1])


print(SubsetSum([10, 20, 15], 3, 0))
