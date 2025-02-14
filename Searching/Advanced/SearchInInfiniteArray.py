# Return the index if element is found
# O(index_of_element)
# Naive Solution
# def func(arr, ele):
#     i = 0
#     while True:
#         if arr[i] == ele:
#             return i

#         elif arr[i] > ele:
#             return -1

#         i += 1


# arr = list(range(1, 10000001,2))
# print(func(arr,994))

# Better Solution
# O(log(index_of_element))

def binarySearch(arr, si, ei, ele):

    while si <= ei:
        mid = (si + ei) // 2

        if arr[mid] == ele:
            return mid

        elif ele < arr[mid]:
            ei = mid

        else:
            si = mid+1

    return -1


def func1(arr, ele):

    # Check it because we any number multiplied with 0 will be 0
    if arr[0] == ele:
        return 0

    i = 1

    while arr[i] < ele:
        i *= 2

        if arr[i] == ele:
            return i

    # A little more optimised as we have checked for i//2 and i
    return binarySearch(arr, i//2+1, i-1, ele)


arr = list(range(1, 10000001, 2))
print(func1(arr, 994))
