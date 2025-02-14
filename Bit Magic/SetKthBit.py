# 10            :   001010
# 1 << 3	    :   001000 (Left shift 1 by k-1 bits)
# AND Operation :   001000

# 10            :   001010
# 10 >> 3       :   000001 (right shift 1 by k-1 bits)
# 1		        :   000001
# AND Operation :   000001

# Since 1 is shifted by k bits therefore if the bit is set in the given number at kth position then the result will become 1 as AND of bits between the different bits after the kth bit will become zero during AND otherwise the result will be 0

# Using left shift operator
# def funcl(n, k):
#     if n & (1 << (k-1)):
#         print("SET")
#     else:
#         print("NOT SET")


# funcl(10, 4)


# This will shift the kth bit of the number to the LSB and if it is set then its AND with 1 will give 1 otherwise 0

# Using right shift operator
# def funcr(n, k):
#     if (n >> (k-1)) & 1:
#         print("SET")

#     else:
#         print("NOT SET")


# funcr(10, 4)
