def findMin(arr):
    si = 0
    ei = len(arr) - 1

    res = arr[0]

    while si <= ei:
            
        if arr[si] < arr[ei]:
            return min(arr[si], res)

        mid=(si+ei)//2
        res = min(res,arr[mid])

        if arr[mid] >= arr[si]:
            si = mid+1

        else:
            ei = mid-1

    return res


arr = [4,5,1,2,3]
print(findMin(arr))