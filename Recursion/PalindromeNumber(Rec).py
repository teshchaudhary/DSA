def helper(N, temp):
    if N == 0:
        return temp
    
    temp = (temp*10) + (N%10)
    
    return helper(N//10, temp)

def isPalin(N):
    a = helper(N,0)
        
    if N == a:
        return 1
    else:
        return 0

print(isPalin(121))