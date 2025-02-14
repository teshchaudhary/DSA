def func1(arr, k):
    for i in range(len(arr)):
        curr = 0

        for j in range(i, len(arr)):
            curr += arr[j]
            if curr == k:
                return True

    return False

# arr = [3,2,0,4,7]
# print(func1(arr,6))

# Efficient Solution
# O(n)

# Sliding Window Approach
# Keep adding till the current sum is less than the given sum and keep increasing the ending index
# While current sum is greater than the given sum, keep subtracting the elements from the start of array and keep increasing the starting index


def func2(arr, k):
    si = 0
    curr_sum = 0

    for ei in range(len(arr)):
        curr_sum += arr[ei]

        while curr_sum > k:
            curr_sum -= arr[si]
            si += 1
        if curr_sum == k:
            return True

    return False

# arr = [1,4,20,3,10,15]
# print(func2(arr,23))