# 0x55555555 is a number representing set bits at odd positions
# 5 = 0101 so 0X55555555 has 16 ones, 16 zeros and the ones,zeros take alternate positions.

# 0xAAAAAAAA is a number representing set bits at even positions
# A = 1010 in hex to binary conversion and makes similar pattern

def swap(n):

    # First we make two numbers from out given number
    # One with only even bits
    # One with only odd bits
    eb = n & (0xAAAAAAAA)
    ob = n & (0x55555555)

    # Since we want to swap so we right shift the even bit number and left shift the odd bit number

    eb >>= 1
    ob <<= 1

    return eb & ob

#            Eg: 23 = 00010111
#        0xAAAAAAAA = 10101010
# eb = (AND of two) = 00010010

# Similariliy,
#                        23 = 00010111
#                0x55555555 = 01010101
# ob = (AND of n and 0x5..) = 00010101

# right shift eb = 00001001
#  left shift ob = 00101010
#   OR of result = 00101011 ( This is the resultant of swapping odd bits with even bits)
