def sumExists(arr, sum):
    s = set()
    for i in range(len(arr)):
        if (sum-arr[i]) in s:
            return 1
        else:
            s.add(arr[i])
    return 0