"""
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.
"""

def findMax(arr, n):
    # Helper function to check if we can distribute at least `n` parts of size `x`
    def isValid(x):
        count = sum(val // x for val in arr)  # Count total parts of size `x`
        return count >= n  # Return True if we can distribute at least `n` parts

    # If total sum of elements is less than `n`, it's impossible to distribute
    if sum(arr) < n:
        return 0

    # Define the binary search range: minimum size is 1, maximum is the largest value in `arr`
    left, right = 1, max(arr)

    # Binary search to find the maximum possible size of each part
    while left <= right:
        mid = (left + right) // 2  # Middle value as a candidate size
        if isValid(mid):  # Check if we can distribute `n` parts of size `mid`
            left = mid + 1  # Increase lower bound to try for a larger size
        else:
            right = mid - 1  # Decrease upper bound to reduce the size
    
    # The right pointer will hold the maximum valid size when the loop ends
    return right
