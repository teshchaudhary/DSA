# Take k elements at a time and get the largest sum from all these pairs

# Naive Solution
# O(n*k)

def func1(arr, k):
    res = float('-inf')
    l = len(arr)
    i = 0

    while (i+k-1 < l): # To get elements such that there are k elements after the curr index
        curr_sum = 0
        for j in range(k):
            curr_sum += arr[i+j] # to sum k elements from each index possible

        res = max(res, curr_sum)
        i += 1
    
    return res

# print(func([10,5,-2,20,1],3))

# Sliding Window Technique
# Nullify the effect of the element to be left and add the new element

def func2(arr, k):

    l = len(arr)

    res = float('-inf')
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]

    res = max(res, curr_sum)
    si = 0
    ei = k

    while ei < l:
        curr_sum = curr_sum + arr[ei] - arr[si]
        res = max(res, curr_sum)
        si += 1
        ei += 1
    
    return res

# print(func([1,8,30,-5,20, 7], 4))


# Less LOC

def func3(arr, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]

    res = curr_sum

    for i in range(k, len(arr)):
        curr_sum = curr_sum + arr[i] - arr[i-k]
        res = max(res, curr_sum)

    return res