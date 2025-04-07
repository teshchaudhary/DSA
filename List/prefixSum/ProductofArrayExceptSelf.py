# The intuition is for every index i we will make prduct of elements till i-1 and i+1


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1 for _ in range(n)]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res