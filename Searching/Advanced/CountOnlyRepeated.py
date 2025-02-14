# Given an array arr[] of N positive integers, where elements are consecutive (sorted). Also, there is a single element which is repeating X (any variable) number of times. Now, the task is to find the element which is repeated and number of times it is repeated.

# For an array with consecutive sorted elements
# The number of repeated element can be calculated in constant time with this formula
# count = n - (arr[n-1] - arr[0])

# For the element we can do binary search
# If the arr[mid] >= mid + arr[0] it means the repeating element is present in the second half as between two consecutive numbers the difference can be 1 only


def findRepeating(arr, n):
    si = 0
    ei = n - 1
    element = -1

    while si <= ei:
        mid = (si + ei) // 2

        if (mid > 0 and arr[mid] == arr[mid-1]) or (mid < n-1 and arr[mid] == arr[mid+1]):
            element = arr[mid]
            break

        if arr[mid] >= mid + arr[0]:
            si = mid + 1
        
        else:
            ei = mid - 1

    if element == -1:
        return [-1, -1]
    else:
        count = n - (arr[n-1] - arr[0])
        return [element, count]


# We can replace the condition for where to go (left of right) by

# Check if the repeating element is in the left half
# if arr[mid] - arr[low] >= mid - low:
#     high = mid - 1
# Check if the repeating element is in the right half
# else:
#     low = mid + 1