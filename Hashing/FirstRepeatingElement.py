def firstRepeated(arr):
    d = {}

    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in arr:
        if d[i] > 1:
            return arr.index(i) + 1

    return -1
