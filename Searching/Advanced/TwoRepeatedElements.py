# Find the two repeated elements in the given array

def twoRepeated(arr):
    res = []

    for i in range(len(arr)):
        idx = abs(arr[i]) - 1

        arr[idx] *= -1

        if arr[idx] > 0:
            res.append(idx+1)

    return res


arr = [1, 2, 1, 3, 4, 3]
print(twoRepeated(arr))
