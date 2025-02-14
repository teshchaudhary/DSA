# def sqrt(n):
#     i = 1
#     while i*i <= n:
#         i += 1

#     return i-1

# print(sqrt(24))

def sqrt(n):
    si = 0
    ei = n

    while si <= ei:
        mid = (si + ei) // 2
        mSq = mid*mid

        if mSq == n:
            return mid

        elif mSq > n: # Reduce it until the sq get less than the number
            ei = mid - 1

        else:
            si = mid + 1
            ans = mid

    return ans


print(sqrt(25))