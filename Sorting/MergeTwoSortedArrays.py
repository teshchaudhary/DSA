def mergeTwoSorted(arr1, arr2):
    res = []
    l1 = len(arr1)
    l2 = len(arr2)
    i = 0
    j = 0

    # While loop is used as it is good when we need to exhasust two arrays not knowing about which will be empty first

    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < l1:
        res.append(arr1[i])
        i += 1

    while j < l2:
        res.append(arr2[j])
        j += 1

    return res


a1 = [1, 20, 30, 40, 50]
a2 = [6, 8, 90, 101]

a3 = mergeTwoSorted(a1, a2)
print(a3)
