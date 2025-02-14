import math

def countSetBits(n):
    if (n <= 1):
        return n
    
    x = int(math.log2(n)) # Number of Set bits of all permutations before the
    # [(largest power of 2) -(1)] less than n
    s1 = (x * (1<<(x - 1)))
    # Count of all first set bit of all the permutations after that
    # 
    s2 = (n - (1<<x) + 1)
    
    return s1 + s2 + countSetBits(n - (1<<x))


print(countSetBits(16))
