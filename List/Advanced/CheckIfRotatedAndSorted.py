# If the array is rotated and sorted then
# In case of ascending there will only be one element which is smallers than the previous element
# In case of descending there will only be one element which is greater then the previous element

# In corner cases check the first and last elements

def checkRotatedAndSorted(arr, n):
    if n == 1 or n == 2:
        return True

    elif arr[0] > arr[1]:
        count = 0
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                count += 1

        return True if arr[-1] > arr[0] and count == 1 else False

    elif arr[0] < arr[1]:
        count = 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                count += 1

        return True if arr[-1] < arr[0] and count == 1 else False
