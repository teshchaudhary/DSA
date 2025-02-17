def ceil(arr, target):
    si, ei = 0, len(arr)-1

    while si <  ei:
        mid = (si+ei)//2

        if arr[mid] >= target:
            ei = mid
        
        else:
            si = mid + 1
    
    return ei

def lis(arr):
    n = len(arr)
    tail = [arr[0][1]]

    for i in range(1, n):
        if arr[i][1] > tail[-1]:
            tail.append(arr[i][1])
        else:
            tail[ceil(tail, arr[i][1])] = arr[i][1]
    
    return len(tail)

def func(arr):
    arr = sorted(arr, key=lambda x: (x[0], x[1]))

    return lis(arr)


a = [[6,2],[4,3],[2,6],[1,5]]
b = [[8,1],[1,2],[4,5],[3,4],[2,6],[6,7],[7,8],[5,5]]
print(func(a))
print(func(b))