# Given two numbers X and Y, and a range [L, R] where 1 <= L <= R <= 31. You have to copy the set bits of 'Y' in the range L to R in 'X'. Return this modified X.

# Note: Range count will be from Right to Left & start from 1.

# Example 1:

# Input: 
# X = 44, Y = 3 
# L = 1,  R = 5

# Output: 
# 47


# so here
# r = 5
# l = 1
# x = 3 = 000011

# 1 << (r-l+1)
# 1 << (5)
# 000011000

# Concept of Brian Keringham's
# When we subtract one, all the bits to the rightmost set bits of the number get inverted.
# So the number will become 000000111

# So I will left shift by l - 1 to get the desired mask
# mask = 000000111
# x = 00000011
# And_X  = 000000011

# res = And_X | y
# y = 101100
# res = 000101111 == 47

def setSetBit(x, y, l, r):
      # Get a mask of the set bits we needed in sequence
      mask = ((1 << (r-l+1)) - 1) << (l-1)
      extractedSetBits = y & mask
      res = extractedSetBits | x
      
      return res