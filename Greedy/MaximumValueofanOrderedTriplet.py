"""
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""

class Solution:
    def maximumTripletValue(self, nums) -> int:
        n = len(nums)
        lMax = [0] * n
        rMax = [0] * n
        res = 0

        for i in range(1, n):
            lMax[i] = max(lMax[i - 1], nums[i - 1])
            rMax[n - 1 - i] = max(rMax[n - i], nums[n - i])
        
        for j in range(1, n - 1):
            res = max(res, (lMax[j] - nums[j]) * rMax[j])
        return res