def solution(A, n):

    # To know how long should be the check array
    m = max(A)

    if m < 1:
        return 1
    
    if len(A) == 1:
        # If it contains only one element
        return 2 if A[0] == 1 else 1
    
    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1:
                # Changing the value status at the index of our list
                l[A[i] - 1] = 1
    
    for i in range(len(l)):
        # Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
    return n + 1


arr = [1,2,3,4,5]
print(solution(arr, 5))


# Efficient Solution

def firstMissingPositive(arr, n):

    # Loop to traverse the whole array
    for i in range(n):

        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
            

    # Checking any element which
    # is not equal to i + 1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1

    # Nothing is present return last index
    return n + 1


arr = [0, 10, 2, -10, -20]
n = len(arr)
ans = firstMissingPositive(arr, n)
print(ans)