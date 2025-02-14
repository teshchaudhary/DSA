def func1(arr, si, ei):
    while si <= ei:
        mid = (si + ei)//2

        if mid == 0 or arr[mid] >= arr[mid+1] and mid == len(arr) - 1 or\
                arr[mid] > arr[mid-1]:
            return mid

        elif arr[mid] < arr[mid+1]:
            si = mid + 1

        else:
            ei = mid - 1

    return -1


print(func1([17, 19, 9, 5, 3, 6, 17, 7, 18, 16, 18, 11, 3, 15, 2], 0, 15))
