def peak(arr):
    si = 0
    ei = len(arr)-1

    while ei >= si:
        mid = (si+ei)//2

        if (mid == 0 or arr[mid] > arr[mid-1]) and (mid == len(arr)-1 or arr[mid] > arr[mid+1]):
            return mid
        
        elif arr[mid] < arr[mid+1]:
            si = mid + 1
        
        else:
            ei = mid - 1

print(peak([1,2,3,4,5]))