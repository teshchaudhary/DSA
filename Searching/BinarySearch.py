# def BinarySearch(arr, ele):
#     l = len(arr)
#     mid = l//2

#     if arr[mid] == ele:
#         return mid
    
#     else:
#         if ele<arr[mid]:
#             for i in range(mid):
#                 if arr[i] == ele:
#                     return i
#         else:
#             for i in range(mid,l):
#                 if arr[i] == ele:
#                     return i
    
#     return -1

# print(BinarySearch([1,2,3,4,5],5))

def BinarySearch(arr, ele):
    si = 0
    ei = len(arr) - 1

    while si<=ei:
        mid = (si+ei)//2
        if arr[mid] == ele:
            return mid
        
        elif ele < arr[mid]:
            ei = mid
            
        else:
            si = mid + 1

    return -1

print(BinarySearch([1,2,3,5],5))