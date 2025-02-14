# Find the maximum range between two numbers in an array such that
# arr[j] > arr[i]
# j > i

# Make two arrays
# One will have the minimum element yet with respect to each index (left to right)
# One will have the maximum element yet with respect to each index (right to left)
def maxIndexDiff(A, N):
    minEle = [None]*N
    maxEle = [None]*N

    minEle[0] = A[0]
    for i in range(1, N):
        minEle[i] = min(minEle[i-1], A[i])

    maxEle[-1] = A[-1]
    for i in range(N-2, -1, -1):
        maxEle[i] = max(maxEle[i+1], A[i])

    i = j = 0
    res = 0

    # Compare the elements from both arrays and get the longest sequence
    while i < N and j < N:
        if minEle[i] <= maxEle[j]:
            res = max(res, j-i)
            j += 1

        else:
            i += 1

    return res
