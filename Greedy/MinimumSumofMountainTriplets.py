"""
You are given a 0-indexed array nums of integers.

A triplet of indices (i, j, k) is a mountain if:

i < j < k
nums[i] < nums[j] and nums[k] < nums[j]
Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
"""

class Solution:
    def minimumSum(self, nums) -> int:
        n = len(nums)
        lMin = [float('inf')] * n
        rMin = [float('inf')] * n
        res = float('inf')

        for i in range(1, n):
            lMin[i] = min(lMin[i - 1], nums[i-1])
            rMin[n - 1 - i] = min(rMin[n-i], nums[n-i])

        for j in range(1, n - 1):
            if lMin[j] < nums[j] and rMin[j] < nums[j]:
                res = min(res, lMin[j] + nums[j] + rMin[j])

        return res if res != float('inf') else -1 