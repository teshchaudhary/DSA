def grayToBinary(n):
    res = n

    while n > 0:
        res = res ^ (n >> 1)
        n >>= 1
    return res
