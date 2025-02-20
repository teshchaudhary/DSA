def ceil(arr, x):
    si = 0
    ei = len(arr)-1

    while si < ei:
        mid = (si+ei)//2

        if arr[mid] >= x:
            ei = mid
        
        else:
            si = mid + 1
    
    return ei

def func(arr):
    n = len(arr)
    tail = [arr[0]]

    for i in range(1, n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            tail[ceil(tail, arr[i])] = arr[i]
    
    return len(tail)