"""
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
"""

def minimumIndex(nums):
    n = len(nums)
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1

    dom_ele = max(d, key=d.get)
    total_count = d[dom_ele] # Count the number of dominant elements in the array

    left_count = 0
    for i in range(n):
        if nums[i] == dom_ele:
            left_count += 1 # Encountered by now

        right_count = total_count - left_count # the remaining ones must be rightwards of the current index

        if left_count * 2 > (i + 1) and right_count * 2 > (n - (i + 1)):
            return i
    
    return -1