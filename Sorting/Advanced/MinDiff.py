# Tell the minimum difference between any two elements in the array

def func(arr):
    arr.sort()
    res = float('inf')
    for i in range(1,len(arr)):
        res = min(res, arr[i] - arr[i-1])
    
    return res