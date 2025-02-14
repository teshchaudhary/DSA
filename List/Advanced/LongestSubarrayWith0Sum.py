# O(N) space + time
# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

def func(arr):
    res = 0
    pSum = 0
    d = {}

    for i in range(len(arr)):
        pSum += arr[i]

        if pSum == 0:
            res = i + 1

        if pSum in d:
            res = max(res, i-d[pSum])

        # Storing the indices in the dictionary
        else:
            d[pSum] = i

    return res


print(func([15, -2, 2, -8, 1, 7, 10, 23]))
