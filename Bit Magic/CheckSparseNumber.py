# A number is called a sparse number if it has no two consecutive ones

def isSparse(n):
    return n & (n >> 1) == 0

print(isSparse(4))