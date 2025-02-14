def intersection(arr1, arr2):
    res = []
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)

    while i < l1 and j < l2:
        if i > 0 and arr1[i-1] == arr1[i]:
            i += 1

        elif j > 0 and arr2[j-1] == arr2[j]:
            j += 1

        elif arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1

        elif arr1[i] > arr2[j]:
            j+=1
        
        else:
            i+=1
    
    return res

print(intersection([1,2,3,4,4], [4,5,6,7]))