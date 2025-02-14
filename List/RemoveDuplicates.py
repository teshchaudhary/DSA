# Remove duplicates in a sorted array

def rem(arr):
    res = 1
    for i in range(1,len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1
            
    return res

arr = [1,1,2,2,3,3,4,4]
x = rem(arr)
print(arr[:x])