# Observations and steps
# breakpoint -> the index from which the next permutation will be made
# find breakpoint
# if array is strictly increaseing from right to left (no breakpoint) then just reverse the string as that is the highest permutation for the given array or number (breakpoint = -1)
# if there is a breakpoint just swap it with the smallest greater number in array after the breakpoint and swap
# now reverse the array after breakpoint

# eg: 2 3 5 4 1 0 0
# breakpoint = 1
# -> 2 4 5 3 1 0 0
# -> 2 4 0 0 1 3 5

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        breakpoint_ = -1

        # finding breakpoint
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                breakpoint_ = i
                break
        
        # no breakpoint
        if breakpoint_ == -1:
            i, j = 0, n-1
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return


        for i in range(n-1,breakpoint_,-1):
            if nums[breakpoint_] < nums[i]:
                nums[breakpoint_], nums[i] = nums[i], nums[breakpoint_]
                break
        
        i, j = breakpoint_+1, n-1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

