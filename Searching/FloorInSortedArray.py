# Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.

def findFloor(A,N,X):
        si = 0
        ei = N-1
        res = -1
        
        if A[ei] < X:
            return ei
            
        while si <= ei:
            mid = (si+ei)//2
            
            if A[mid] == X:
                return mid
                
            elif A[mid] < X:
                res = mid
                si = mid + 1
            
            else:
                ei = mid-1
            
                
        return res

N = 7
X = 0 
A = [1,2,8,10,11,12,19]

print(findFloor(A,N,X))