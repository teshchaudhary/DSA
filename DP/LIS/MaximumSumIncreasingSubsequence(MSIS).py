def max_sum_increasing_subsequence(nums):
    """
    This function calculates the maximum sum of an increasing subsequence 
    in the given list `nums` using dynamic programming (tabulation).
    
    Approach:
    - We maintain a `dp` array where `dp[i]` stores the maximum sum of an 
      increasing subsequence ending at index `i`.
    - We iterate through each pair of elements to check if they can form 
      an increasing subsequence and update `dp` accordingly.
    - The final answer is the maximum value in `dp`.

    Time Complexity: O(n^2), where n is the length of `nums`.
    Space Complexity: O(n) for storing the `dp` array.
    """
    
    n = len(nums)
    dp = [num for num in nums]  # Initialize dp with the values of nums

    for i in range(1, n):
        for j in range(i):
            # Check if we can extend the increasing subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], nums[i] + dp[j])

    return max(dp)

# Example usage
arr = [3, 1, 10, 4, 7]
print(max_sum_increasing_subsequence(arr))
