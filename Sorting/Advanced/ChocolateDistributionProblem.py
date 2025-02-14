# Distribute the chocolates in a way that the child that gets minimum number of chococlates and the one that gets maximum number of chocolates, the difference between them should be minimum

# m = number of children
# arr is such that arr[i] represents the number of chocolates in a packet

def minDiff(arr,m) :
    if (m == 0 or len(arr) == 0) :
        return 0
    
    if (len(arr) < m) :
        return -1
    
    arr.sort()
    res = arr[m-1] - arr[0]
    for i in range(1, len(arr)- m+1) :
        res = min(res,abs(arr[i + m-1] - arr[i]))
    print(res)
    