# To check if the bit in the element of the array is also set bit (To make the AND bigger)
# check it from msb to lsb


def checker(pattern, arr, N):
    count = 0
    for i in range(N):
        # If the bits are set then it will give the same number
        # We need two numbers like this
        if pattern == pattern & arr[i]:
            count += 1

    return count


def maxAND(arr, N):
    res = 0
    for i in range(18, -1, -1):

        # Check the bits one by one having common set bits from msb to lsb
        count = checker(res | (1 << i), arr, N)

        # Count to check if there are two numbers like this as two numbers will be needed to get AND of.
        if count >= 2:
            res = res | 1 << i

    return res
