# Get the length of maximum consecutive ones in a binary number

def maxConsecutiveOnes(N):
    res = 0
    count = 0
    while N:
        if N % 2 == 1:
            count += 1
            res = max(res, count)

        else:
            count = 0

        N >>= 1

    return res
