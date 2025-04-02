# Also known as three way partitioning

"""
The main idea is:

If arr[mid] == 0, swap it with arr[low] and move both low and mid forward.

If arr[mid] == 1, it is already in the correct place, so just move mid forward.

If arr[mid] == 2, swap it with arr[high] and move high backward (without moving mid because the new element at mid needs checking).
"""
class Solution:
    def sortColors(self, nums) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1