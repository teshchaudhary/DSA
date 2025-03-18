"""
x⊕y == x+y if and only if x&y=0
Why This Property Works
If x ^ y == x + y, it means there are no overlapping 1s in their binary representations.
Since x & y checks for common bits, if it's 0, then x and y have distinct bit positions.
This property allows us to check for a "nice subarray" without explicitly using & in a separate condition."""

# The above condition is True for any no of elements x^y^z^..... == x+y+z+..... if and only if x&y&z&....= 0

def longestNiceSubarray(nums):
    xor_sum, curr_sum, left, res = 0, 0, 0, 0
            
    for right in range(len(nums)):
        xor_sum ^= nums[right]
        curr_sum += nums[right]
        while (xor_sum) != (curr_sum):
            # It removes the left most element by XOR (How?)
            # Suppose the array was like 1 2 3
            # left most is 1 so xor of 1 and 1 will cancel out and only xor of 2 and 3 will be remaining
            # i.e. 1^1^2^3 will be 2^3 only
            xor_sum ^= nums[left]
            curr_sum -= nums[left]
            left += 1

        res = max(res, right - left + 1)

    return res


