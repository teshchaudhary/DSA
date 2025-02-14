# Naive Solution
def checkn(n):
    if n == 0:
        return False

    while n != 1:
        if (n%2) != 0:
            return False
        
        n //= 2
    
    return True

# Property: In power of 2 there is only one set bit
# AND of a power of two with a number less than that is always zero

def checke(n):
    if n == 0:
        return False
    
    return n&(n-1) == 0