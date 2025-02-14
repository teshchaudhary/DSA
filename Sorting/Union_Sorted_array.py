# Naive

# def union(arr1,arr2):
#     res = arr1+arr2
#     res.sort()
#     for i in range(len(res)):
#         if i == 0 or res[i] != res[i-1]:
#             print(res[i], end = " ")

def union(arr1, arr2):
    res = []
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)

    while i < l1 and j < l2:
        if arr1[i] == arr1[i-1]:
            i += 1

        if arr2[j] == arr2[j-1]:
            j += 1
            
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i += 1

        elif arr1[i]>arr2[j]:
            res.append(arr2[j])
            j += 1
        else:
            res.append(arr2[j])
            i += 1
            j +=1
    
    while i < l1:
        res.append(arr1[i])
        i += 1

    while j < l2:
        res.append(arr2[j])
        j += 1
    
    print(res)
union([1,2,3,4],
        [4,5,6,7])