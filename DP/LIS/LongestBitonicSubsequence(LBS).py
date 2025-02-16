def LongestBitonicSequence(n, arr):
    lis = [1 for i in range(n)]
    lds = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], 1+lis[j])
            
    for i in range(n-1, 0, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                lds[i] = max(lds[i], 1+lds[j])
    
    res = 0
    
    if sum(lis)==n or sum(lds)==n:
        return 0
    
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            res = max(res, lis[i] + lds[i] - 1)
    
    return res