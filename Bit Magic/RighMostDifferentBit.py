# Get the position of the right most different bit

def posOfRightMostDiffBit(m, n):
    res = 0
    if m == n:
        return -1

    while m or n:
        if (m % 2) != (n % 2):
            return res+1
        m >>= 1
        n >>= 1
        res += 1

    return res+1
