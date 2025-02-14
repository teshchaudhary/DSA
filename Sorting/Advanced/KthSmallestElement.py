def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthsmallest(arr, k) :
    l = 0 
    r = len(arr) - 1 
    while l <= r :
        p = partition(arr,l,r) 
        if p == k-1 :
            return p 
                
        elif p > k-1 :
            r = p - 1 
                
        else :
            l = p + 1 
    return -1