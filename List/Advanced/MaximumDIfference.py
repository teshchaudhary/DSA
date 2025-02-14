# Find the maximum of arr[j] - arr[i] where j>i
# Both for sorted and unsorted

# Naive Solution
def nsol(arr):
    l = len(arr)
    res = arr[1] - arr[0]
    for i in range(0, l-1):
        for j in range(i+1, l):
            res = max(res, arr[j] - arr[i])

    return res


arr = [2, 3, 10, 6, 4, 8, 1]
print(nsol(arr))

# Efficient Solution


def esol(arr):
    l = len(arr)
    minEle = arr[0]
    res = arr[1] - arr[0]

    for i in range(1, l):
        # Get the maximum difference yet
        res = max(res, arr[i]-minEle)

        # Get the minimum element to get the maximum difference
        minEle = min(minEle, arr[i])

    return res


print(esol(arr))
