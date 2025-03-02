def longest_increasing_subsequence(arr):
    """
    Finds the length of the Longest Increasing Subsequence (LIS) in the array.

    Time Complexity: O(n^2)
    """
    n = len(arr)
    dp = [1] * n  # Initialize LIS values for all elements

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # The length of the LIS


def min_deletions_to_make_increasing(arr):
    """
    Finds the minimum number of deletions required to make the array strictly increasing.

    Formula: 
        min_deletions = total_length - length_of_LIS

    Time Complexity: O(n^2)
    """
    lis_length = longest_increasing_subsequence(arr)
    return len(arr) - lis_length  # Elements to remove to make the sequence increasing


# Example usage
arr1 = [5, 1, 6, 2, 3, 4]
arr2 = [1, 2, 3, 4, 5]  # Already increasing, so 0 deletions
arr3 = [5, 4, 3, 2, 1]  # Needs to remove all but one element

print(min_deletions_to_make_increasing(arr1))  # Output: 2
print(min_deletions_to_make_increasing(arr2))  # Output: 0
print(min_deletions_to_make_increasing(arr3))  # Output: 4
