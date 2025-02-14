# def firstOcc(arr, ele):
#     for i in range(len(arr)):
#         if arr[i] == ele:
#             return i
    
#     return -1

# def firstOcc(arr, ele):
#     i = 0
#     l = len(arr)
#     while i<l:
#         if arr[i]==ele:
#             return i
#         i+=1
#     return -1

# print(firstOcc([1,2,3,4,5],5))

# O(log(n))
def firstOcc(arr,ele):
    si = 0
    ei = len(arr) - 1

    while si<=ei:
        mid = (si+ei)//2
        if ele < arr[mid]:
            ei = mid-1
        elif ele > arr[mid]:
            si = mid+1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                ei = mid - 1
    return -1

print(firstOcc([1,2,3,4,5],6)) 