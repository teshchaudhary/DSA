# def count(n):
#     res = 0
#     while n!= 0:
#         if n&1 == 1:
#             res += 1

#         n >>= 1

#     return res

# def count(n):
#     res = 0
#     while n!= 0:
#         res += (n&1)

#         n >>= 1

#     return res

# print(count(10))


# -------- Brian Kerningam's Algorithm --------
# In this algorithm we unset the last set bit
# In this we do an AND operation of a number n with n-1
# If there are bits after the first set bit of number these will be either 0 or there will be no bits
# In number n-1 all the bits after the first set bit in n will be 1 if there are bits in n after the first set bit.


# E.g.
# 40: 101000
# 39: 100111
# AND: 100000 = 32
def count(n):
    res = 0
    while n != 0:
        n = n & (n-1)
        res += 1

    return res


print(count(10))


# We can do this operation in O(1) time complexity but with an assumption
# Assumption: Our number is of some fixed bits eg 32 bits, 64 bits etc

# Lookup table bases solution

# We will only store (2^7)-1 number i.e. 8 bit numbers in our table

# Lookup Table
table = [0]*256  # 8 bit numbers are from 0-255

# Preprocessing
# It will be done using naive approach
# The table after preprocessing will contain the number of set bits in  each number 0-255


def preprocessing():
    table[0] = 0
    for i in range(256):
        table[i] = (i & 1) + table[i//2]

# 0xff is an 8 bit number with all set bits = 255


# This code is for 32 bit numbers
# We can increase the limit by adding more values in return statement
def countbits(n):
    return table[n & 0xff] + table[(n >> 8) & 0xff] + table[(n >> 16) & 0xff] + table[(n >> 24) & 0xff]


preprocessing()
print(countbits(5))