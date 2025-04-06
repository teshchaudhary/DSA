"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
"""

class Solution:
    def largestDivisibleSubset(self, nums):
        # if 8 is divisible by 4 and 4 is divisble by 2 and 8 is divisible by 2 as well thats why sorting is needed
        nums.sort()


        # The below code is for LIS
        # The only modification is we need the divisibility check instead of increasing check
        n = len(nums)
        dp = [1 for _ in range(n)]
        prev_indexes = [-1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_indexes[i] = j
        
        result_length = max(dp)
        index = dp.index(result_length)

        result = []

        while index != -1:
            result.append(nums[index])
            index = prev_indexes[index]

        return result