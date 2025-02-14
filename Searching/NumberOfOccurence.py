def firstOccurence(arr,n,x):
    si = 0
    ei = n-1
    
    while si <= ei:
        mid = (si+ei)//2
        
        if arr[mid] < x:
            si = mid + 1
        
        elif arr[mid] > x:
            ei = mid - 1
        
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            
            else:
                ei = mid - 1
    
    return -1

def lastOccurence(arr,n,x):
    si = 0
    ei = n-1
    
    while si <= ei:
        mid = (si+ei)//2
        
        if arr[mid] < x:
            si = mid + 1
        
        elif arr[mid] > x:
            ei = mid - 1
        
        else:
            if mid == n-1 or arr[mid] != arr[mid+1]:
                return mid
            
            else:
                si = mid + 1
    
    return -1
    
class Solution:

	def count(self,arr, n, x):
		fo = firstOccurence(arr,n,x)
	    lo = lastOccurence(arr,n,x)
	    
	    if fo == lo == -1:
	        return 0
        
        else:
            return (lo - fo)+1